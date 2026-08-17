#!/usr/bin/env python3
"""Variable-pole physical coupled-mode optimization for Experiment 03.

The parameterization, ranks, grids, optimizer schedule, acceptance thresholds,
and stopping rule were frozen in
`VARIABLE_POLE_PHYSICAL_ACCEPTANCE_2026-08-17.md` before this script was run.

The model is physical at every iterate:

    C(t)=g^dag exp[(-iH-Gamma)t] g,
    H=H^dag tridiagonal,
    Gamma=L L^dag > 0,
    g=sqrt(C_exact(0)) e1.

Only the stable physical realization moves.  There is no post-fit projection.
"""
from __future__ import annotations

import argparse
import math
import numpy as np
from scipy.linalg import expm, svdvals

import torch

import direct_era_coupled_harmonic as era
import frequency_weighted_physical_fit as fw
import direct_port_bath_correlation as bc

RANKS=(12,16,24)
N_UNIFORM=401
N_PHYS=241
ADAM_STEPS=1500
ADAM_LR=2e-3
LBFGS_STEPS=500
LOSS_SCALE=1e8
REF_DIM=16


def exact_terms(wc):
    cscale=(era.PHI_BAR/bc.HBAR)**2/(wc*wc)
    ds=[]; zs=[]
    for pole in bc.bath_poles():
        ds.append(bc.bath_coeff(pole)*cscale)
        zs.append(1j*pole/wc)
    n=np.arange(1,era.NMATS+1,dtype=float)
    nu=2*math.pi*n/(bc.BETA*bc.HBAR)
    ds.extend(((-2*bc.G*nu*bc.WD**4/(bc.BETA*(nu**4+bc.WD**4)))*cscale).tolist())
    zs.extend((nu/wc).tolist())
    return np.asarray(ds,complex),np.asarray(zs,complex)


def exact_transfer(xs,d,z,chunk=1000):
    xs=np.asarray(xs,float).ravel()
    out=np.zeros(xs.size,complex)
    for j in range(0,len(d),chunk):
        dd=d[j:j+chunk]; zz=z[j:j+chunk]
        out += np.sum(dd[:,None]/(zz[:,None]-1j*xs[None,:]),axis=0)
    return out


def lanczos_gauge(H,Gamma,g):
    H=np.asarray(H,complex); Gamma=np.asarray(Gamma,complex); g=np.asarray(g,complex)
    n=len(g); gn=float(np.linalg.norm(g)); q=g/gn
    Q=[]; alpha=[]; beta=[]
    qprev=np.zeros(n,complex); bprev=0.0
    for k in range(n):
        Q.append(q.copy())
        w=H@q-bprev*qprev
        a=float(np.real(np.vdot(q,w)))
        w=w-a*q
        # Full double reorthogonalization.  This is deterministic and protects
        # the gauge identities for nearly rank-saturated ERA models.
        for _ in range(2):
            for qq in Q:
                w -= qq*np.vdot(qq,w)
        alpha.append(a)
        if k<n-1:
            b=float(np.linalg.norm(w))
            if b<1e-13*max(np.linalg.norm(H),1.0):
                raise RuntimeError(f'Lanczos breakdown at k={k}: beta={b}')
            beta.append(b)
            qprev=q; q=w/b; bprev=b
    U=np.column_stack(Q)
    T=np.diag(alpha)
    if beta:
        T+=np.diag(beta,1)+np.diag(beta,-1)
    Gp=U.conj().T@Gamma@U
    gp=U.conj().T@g
    unit=float(np.linalg.norm(U.conj().T@U-np.eye(n),ord='fro'))
    herr=float(np.linalg.norm(U.conj().T@H@U-T,ord='fro')/max(np.linalg.norm(H,ord='fro'),1e-300))
    gerr=float(np.linalg.norm(gp-np.r_[gn,np.zeros(n-1)])/gn)
    Gp=.5*(Gp+Gp.conj().T)
    mine=float(np.linalg.eigvalsh(Gp).min())
    shift=0.0
    if mine<=0:
        if mine < -1e-12:
            raise RuntimeError(f'Lanczos Gamma has material negative eigenvalue {mine}')
        shift=1e-12-mine
        Gp=Gp+shift*np.eye(n)
    L=np.linalg.cholesky(Gp)
    gamerr=float(np.linalg.norm(Gp-L@L.conj().T,ord='fro')/max(np.linalg.norm(Gp,ord='fro'),1e-300))
    return dict(U=U,H=T,Gamma=Gp,g=gp,L=L,unit=unit,herr=herr,gerr=gerr,
                gamerr=gamerr,shift=shift)


def baseline_physical(rank,samples):
    model=era.era_realization(samples,era.DT,era.M,rank)
    if model['max_re']>=0:
        raise RuntimeError(f'baseline ERA rank {rank} unstable')
    l,r,_=era.balance_scalar_gauge(model['C'],model['B'])
    Lam=1j*model['Ac']
    sdp=era.solve_general_sdp(Lam,l,r)
    phys=era.reconstruct_physical(Lam,r,sdp['Y'])
    return model,sdp,phys


def pack_np(H,L):
    n=H.shape[0]
    hd=np.real(np.diag(H)).copy()
    hb=np.real(np.diag(H,1)).copy()
    if np.any(hb<=0): raise RuntimeError('Lanczos offdiagonal not positive')
    ld=np.real(np.diag(L)).copy()
    if np.any(ld<=0): raise RuntimeError('Cholesky diagonal not positive')
    ii,jj=np.tril_indices(n,-1)
    return dict(hd=hd,logb=np.log(hb),logld=np.log(ld),
                lr=np.real(L[ii,jj]).copy(),li=np.imag(L[ii,jj]).copy(),
                ii=ii,jj=jj)


def unpack_np(p):
    n=len(p['hd'])
    H=np.diag(p['hd']).astype(complex)
    b=np.exp(p['logb']); H+=np.diag(b,1)+np.diag(b,-1)
    L=np.zeros((n,n),complex); L[np.diag_indices(n)]=np.exp(p['logld'])
    L[p['ii'],p['jj']]=p['lr']+1j*p['li']
    return H,L,L@L.conj().T


def torch_params(p):
    return [
        torch.tensor(p['hd'],dtype=torch.float64,requires_grad=True),
        torch.tensor(p['logb'],dtype=torch.float64,requires_grad=True),
        torch.tensor(p['logld'],dtype=torch.float64,requires_grad=True),
        torch.tensor(p['lr'],dtype=torch.float64,requires_grad=True),
        torch.tensor(p['li'],dtype=torch.float64,requires_grad=True),
    ]


def build_torch(params,ii,jj,n):
    hd,logb,logld,lr,li=params
    cdtype=torch.complex128
    H=torch.diag(hd).to(cdtype)
    b=torch.exp(logb).to(cdtype)
    H=H+torch.diag(b,diagonal=1)+torch.diag(b,diagonal=-1)
    L=torch.zeros((n,n),dtype=cdtype)
    inds=torch.arange(n,dtype=torch.long)
    L[inds,inds]=torch.exp(logld).to(cdtype)
    ti=torch.tensor(ii,dtype=torch.long); tj=torch.tensor(jj,dtype=torch.long)
    L[ti,tj]=lr.to(cdtype)+1j*li.to(cdtype)
    Gamma=L@L.conj().T
    return H,L,Gamma


def transfer_torch(H,Gamma,g,x):
    n=H.shape[0]
    I=torch.eye(n,dtype=torch.complex128)
    M=(Gamma+1j*H)[None,:,:]-1j*x[:,None,None].to(torch.complex128)*I[None,:,:]
    gg=g.expand(x.numel(),n)
    v=torch.linalg.solve(M,gg.unsqueeze(-1)).squeeze(-1)
    return torch.sum(torch.conj(gg)*v,dim=1)


def objective_torch(params,meta,data):
    H,_L,Gamma=build_torch(params,meta['ii'],meta['jj'],meta['n'])
    Fu=transfer_torch(H,Gamma,data['g'],data['xu'])
    ep=transfer_torch(H,Gamma,data['g'],data['xp'])-data['Fpex']
    em=transfer_torch(H,Gamma,data['g'],-data['xp'])-data['Fmex']
    du=Fu-data['Fuex']
    den=data['F0abs2']
    Ju=torch.mean(torch.abs(du)**2)/den
    pair=.5*(torch.abs(ep)**2+torch.abs(em)**2)/den
    Jx=torch.sum(data['wx']*pair)
    Jv=torch.sum(data['wu']*pair)
    return Ju+Jx+Jv,(Ju,Jx,Jv)


def clone_params(params):
    return [x.detach().clone() for x in params]


def restore_params(params,saved):
    with torch.no_grad():
        for p,s in zip(params,saved): p.copy_(s)


def optimize(params,meta,data):
    best={'J':math.inf,'params':clone_params(params),'where':'initial'}
    def observe(where):
        with torch.no_grad():
            J,parts=objective_torch(params,meta,data)
            val=float(J)
            if math.isfinite(val) and val<best['J']:
                best['J']=val; best['params']=clone_params(params); best['where']=where
            return val,tuple(float(x) for x in parts)

    j0,p0=observe('initial')
    print(f'OPT_INITIAL J={j0:.12e} Juniform={p0[0]:.12e} Jx={p0[1]:.12e} Ju={p0[2]:.12e}',flush=True)
    opt=torch.optim.Adam(params,lr=ADAM_LR,betas=(.9,.999),eps=1e-8)
    for k in range(ADAM_STEPS):
        opt.zero_grad(set_to_none=True)
        J,_=objective_torch(params,meta,data)
        (LOSS_SCALE*J).backward()
        opt.step()
        if (k+1)%100==0 or k==0:
            val,parts=observe(f'adam{k+1}')
            print(f'OPT_ADAM step={k+1} J={val:.12e} Juniform={parts[0]:.12e} Jx={parts[1]:.12e} Ju={parts[2]:.12e}',flush=True)
    observe('adam_final')

    lb=torch.optim.LBFGS(params,lr=1.0,max_iter=LBFGS_STEPS,history_size=100,
                         tolerance_grad=1e-12,tolerance_change=1e-14,
                         line_search_fn='strong_wolfe')
    calls={'n':0}
    def closure():
        lb.zero_grad(set_to_none=True)
        J,parts=objective_torch(params,meta,data)
        loss=LOSS_SCALE*J
        loss.backward()
        calls['n']+=1
        val=float(J.detach())
        if math.isfinite(val) and val<best['J']:
            best['J']=val; best['params']=clone_params(params); best['where']=f'lbfgs_call{calls["n"]}'
        return loss
    lb.step(closure)
    observe('lbfgs_final')
    restore_params(params,best['params'])
    jf,pf=observe('best_restore')
    print(f'OPT_BEST where={best["where"]} J={jf:.12e} Juniform={pf[0]:.12e} Jx={pf[1]:.12e} Ju={pf[2]:.12e} lbfgs_calls={calls["n"]}',flush=True)
    return j0,jf,p0,pf,best['where']


def numpy_from_torch(params,meta):
    arr=[x.detach().cpu().numpy() for x in params]
    p=dict(hd=arr[0],logb=arr[1],logld=arr[2],lr=arr[3],li=arr[4],ii=meta['ii'],jj=meta['jj'])
    return unpack_np(p)


def transfer_np(H,Gamma,g,xs):
    xs=np.asarray(xs,float).ravel(); I=np.eye(H.shape[0])
    return np.array([np.vdot(g,np.linalg.solve(Gamma+1j*H-1j*x*I,g)) for x in xs])


def synthetic_oracle():
    n=4
    hd=np.array([-.7,.2,1.1,2.0]); b=np.array([.45,.62,.38])
    H=np.diag(hd)+np.diag(b,1)+np.diag(b,-1)
    L=np.array([[.55,0,0,0],[.08+.03j,.44,0,0],[-.02+.04j,.06-.01j,.36,0],
                [.01-.02j,-.03+.02j,.05+.01j,.31]],complex)
    Gamma=L@L.conj().T
    p=pack_np(H,L); Hr,Lr,Gr=unpack_np(p)
    erH=np.linalg.norm(Hr-H)/np.linalg.norm(H); erG=np.linalg.norm(Gr-Gamma)/np.linalg.norm(Gamma)
    pars=torch_params(p); meta=dict(ii=p['ii'],jj=p['jj'],n=n)
    Ht,Lt,Gt=build_torch(pars,p['ii'],p['jj'],n)
    x=np.linspace(-4,6,41); g=np.zeros(n,complex); g[0]=1.3
    Ft=transfer_torch(Ht,Gt,torch.tensor(g,dtype=torch.complex128),torch.tensor(x,dtype=torch.float64)).detach().numpy()
    Fn=transfer_np(H,Gamma,g,x)
    ert=float(np.max(np.abs(Ft-Fn))/max(np.max(np.abs(Fn)),1e-300))

    # Gradient audit at a deterministic perturbation of h_0.
    with torch.no_grad(): pars[0][0]+=0.017
    target=torch.tensor(Fn,dtype=torch.complex128)
    xx=torch.tensor(x,dtype=torch.float64); gg=torch.tensor(g,dtype=torch.complex128)
    def small_obj():
        HH,_LL,GG=build_torch(pars,p['ii'],p['jj'],n)
        ff=transfer_torch(HH,GG,gg,xx)
        return torch.mean(torch.abs(ff-target)**2)
    J=small_obj(); J.backward(); ga=float(pars[0].grad[0])
    h=1e-6
    with torch.no_grad():
        orig=float(pars[0][0]); pars[0][0]=orig+h
    jp=float(small_obj().detach())
    with torch.no_grad(): pars[0][0]=orig-h
    jm=float(small_obj().detach())
    with torch.no_grad(): pars[0][0]=orig
    gf=(jp-jm)/(2*h)
    gerr=abs(ga-gf)/max(abs(gf),1e-30)
    gok=(gerr<2e-5) if abs(gf)>=1e-6 else (abs(ga-gf)<1e-8)
    print(f'VARIABLE_ORACLE packH={erH:.12e} packGamma={erG:.12e} transfer={ert:.12e} '
          f'grad_auto={ga:+.12e} grad_fd={gf:+.12e} grad_err={gerr:.12e} grad_ok={int(gok)}',flush=True)
    if erH>=1e-12 or erG>=1e-12 or ert>=1e-11 or not gok:
        raise RuntimeError('variable-pole implementation oracle failed')


def holdout(rank,label,H,Gamma,g,ref,exact_eval,c0):
    K=H-1j*Gamma
    phys=dict(K=K,g=g,H=H,Gamma=Gamma)
    eg=np.linalg.eigvalsh(Gamma)
    corr=era.physical_corr(K,g,era.T_EVAL)
    cm=era.bcf_metrics(corr,exact_eval,c0)
    spec=era.physical_spectrum(K,g,era.X_SPEC)
    exact_spec=np.asarray(era.p.exact_dimless(era.X_SPEC),float)
    sm=era.spectrum_metrics(spec,exact_spec)
    wings=np.concatenate([-np.geomspace(1e4,4.001,1200),era.X_SPEC,np.geomspace(6.001,1e4,1200)])
    sw=era.physical_spectrum(K,g,wings); mins=float(sw.min())
    db=era.db_metrics_from_spectrum(lambda x: era.p.sexp(float(x),K,g))
    state=era.gaussian_state_metrics(dict(wc=era.WC,K=K,g=g,H=H,Gamma=Gamma),ref)
    rho=era.hg.gaussian_rho_from_cov(state['Vsys'],REF_DIM)[0]
    drift=float(np.max(np.linalg.eigvals(-1j*H-Gamma).real))
    print(f'VARIABLE_HOLDOUT rank={rank} label={label} Hmin={np.linalg.eigvalsh(H).min():+.12e} '
          f'Hmax={np.linalg.eigvalsh(H).max():+.12e} GammaMin={eg.min():+.12e} GammaMax={eg.max():+.12e} '
          f'driftMaxRe={drift:+.12e} minS={mins:+.12e} Cmaxabs={cm[0]:.12e} Crms={cm[1]:.12e} '
          f'Cmaxrel={cm[2]:.12e} Smaxabs={sm[0]:.12e} Srms={sm[1]:.12e} Smaxrel={sm[2]:.12e} '
          f'maxwidth={state["maxwidth"]:.12e} nuclear={state["nuclear"]:.12e}',flush=True)
    for x,(ratio,ex,e) in db.items():
        print(f'VARIABLE_DB rank={rank} label={label} x={x:.2f} ratio={ratio:.12e} exact={ex:.12e} logerr={e:.12e}',flush=True)
    physical=(eg.min()>0 and mins>=-1e-10 and drift<-1e-8)
    impl=(state['bcferr']<1e-10 and state['vacres']<1e-12 and state['omega_relerr']<2e-9 and
          state['maxRe']<-1e-8 and state['lyap']<1e-10 and state['numin']>=.5-1e-9 and state['recon']<1e-7)
    return dict(H=H,Gamma=Gamma,g=g,cm=cm,sm=sm,state=state,rho=rho,physical=physical,impl=impl,
                GammaMin=float(eg.min()),minS=mins,drift=drift)


def run_rank(rank,samples,ref,exact_eval,c0,data):
    model,sdp,bphys=baseline_physical(rank,samples)
    gauge=lanczos_gauge(bphys['H'],bphys['Gamma'],bphys['g'])
    print(f'VARIABLE_GAUGE rank={rank} unit={gauge["unit"]:.12e} Herr={gauge["herr"]:.12e} '
          f'gerr={gauge["gerr"]:.12e} GammaFact={gauge["gamerr"]:.12e} shift={gauge["shift"]:.12e}',flush=True)
    if max(gauge['unit'],gauge['herr'],gauge['gerr'],gauge['gamerr'])>=1e-10:
        raise RuntimeError(f'rank{rank} Lanczos gauge audit failed')
    pre0=era.physical_corr(bphys['K'],bphys['g'],era.T_EVAL)
    pre1=era.physical_corr(gauge['H']-1j*gauge['Gamma'],gauge['g'],era.T_EVAL)
    ge=float(np.max(np.abs(pre1-pre0)/np.maximum(np.abs(pre0),1e-14)))
    print(f'VARIABLE_GAUGE_BCF rank={rank} maxrel={ge:.12e}',flush=True)
    if ge>=1e-10: raise RuntimeError('Lanczos gauge changes BCF')

    base=holdout(rank,'initializer',gauge['H'],gauge['Gamma'],gauge['g'],ref,exact_eval,c0)
    pp=pack_np(gauge['H'],gauge['L']); params=torch_params(pp)
    meta=dict(ii=pp['ii'],jj=pp['jj'],n=rank)
    j0,jf,p0,pf,where=optimize(params,meta,data)
    H,L,Gamma=numpy_from_torch(params,meta)
    opt=holdout(rank,'optimized',H,Gamma,gauge['g'],ref,exact_eval,c0)
    print(f'VARIABLE_RESULT rank={rank} J0={j0:.12e} Jbest={jf:.12e} gainJ={j0/jf:.12e} best={where} '
          f'width0={base["state"]["maxwidth"]:.12e} width1={opt["state"]["maxwidth"]:.12e} '
          f'nuclear0={base["state"]["nuclear"]:.12e} nuclear1={opt["state"]["nuclear"]:.12e}',flush=True)
    return dict(rank=rank,base=base,opt=opt,j0=j0,jf=jf,parts0=p0,partsf=pf,where=where)


def make_data(wc):
    d,z=exact_terms(wc)
    xu=np.linspace(-4.,6.,N_UNIFORM); xp=np.linspace(.02,4.,N_PHYS)
    Fue=exact_transfer(xu,d,z); Fpe=exact_transfer(xp,d,z); Fme=exact_transfer(-xp,d,z)
    F0=exact_transfer(np.array([0.]),d,z)[0]
    wx,wu,_=fw.susceptibility_weights(xp,wc)
    return dict(
        xu=torch.tensor(xu,dtype=torch.float64), xp=torch.tensor(xp,dtype=torch.float64),
        Fuex=torch.tensor(Fue,dtype=torch.complex128), Fpex=torch.tensor(Fpe,dtype=torch.complex128),
        Fmex=torch.tensor(Fme,dtype=torch.complex128), wx=torch.tensor(wx,dtype=torch.float64),
        wu=torch.tensor(wu,dtype=torch.float64), F0abs2=torch.tensor(abs(F0)**2,dtype=torch.float64),
        g=None, F0=F0, d=d, z=z,
    )


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,choices=RANKS); args=ap.parse_args()
    torch.set_default_dtype(torch.float64); torch.manual_seed(0); torch.set_num_threads(1)
    print(f'TORCH_VERSION={torch.__version__}',flush=True)
    synthetic_oracle()
    wc,sigma0,ref=era.physical_wc_sigma0(); era.WC=wc
    if era.exact_sampler_audit(wc)>=2e-6: raise RuntimeError('exact sampler audit failed')
    ttrain=np.arange(2*era.M)*era.DT; samples=era.exact_correlation(ttrain,wc)
    era.T_EVAL=(np.arange(2*era.M-1)+.5)*era.DT; exact_eval=era.exact_correlation(era.T_EVAL,wc)
    c0=float(np.real(samples[0])); era.X_SPEC=np.linspace(-4.,6.,2401)
    data=make_data(wc)

    ranks=(args.rank,) if args.rank else RANKS
    rows={}
    for rank in ranks:
        gg=np.zeros(rank,complex); gg[0]=math.sqrt(c0)
        data_rank=dict(data); data_rank['g']=torch.tensor(gg,dtype=torch.complex128)
        rows[rank]=run_rank(rank,samples,ref,exact_eval,c0,data_rank)

    if args.rank:
        r=rows[args.rank]
        print(f'VARIABLE_RANK_DONE rank={args.rank} physical={int(r["opt"]["physical"])} impl={int(r["opt"]["impl"])} '
              f'maxwidth={r["opt"]["state"]["maxwidth"]:.12e} nuclear={r["opt"]["state"]["nuclear"]:.12e} '
              f'objective_improved={int(r["jf"]<r["j0"])}',flush=True)
        return

    mandatory=all(rows[r]['opt']['physical'] and rows[r]['opt']['impl'] for r in RANKS)
    primary=rows[16]['opt']['state']
    primary_pass=(mandatory and ref['basis_err']<1e-7 and rows[16]['jf']<rows[16]['j0'] and
                  primary['maxwidth']<1e-6 and primary['nuclear']<5e-6 and primary['cross']<1e-5)
    control=0.5*float(np.sum(svdvals(np.asarray(rows[24]['opt']['rho'].full())-
                                    np.asarray(rows[16]['opt']['rho'].full()))))
    control_ok=rows[24]['opt']['physical'] and rows[24]['opt']['impl'] and control<5e-6
    finalpass=primary_pass and control_ok
    print(f'VARIABLE_CONTROL rank16_rank24_half_nuclear={control:.12e}',flush=True)
    print(f'VARIABLE_ACCEPTANCE mandatory={int(mandatory)} primary_pass={int(primary_pass)} '
          f'control_ok={int(control_ok)} finalpass={int(finalpass)}',flush=True)
    print('VARIABLE_POLE_PHYSICAL_PASS' if finalpass else 'VARIABLE_POLE_PHYSICAL_FAIL',flush=True)


if __name__=='__main__': main()
