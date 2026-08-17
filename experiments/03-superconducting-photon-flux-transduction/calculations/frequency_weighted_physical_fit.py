#!/usr/bin/env python3
"""Frequency-weighted fit directly inside the coupled-Lindblad physical cone.

The objective, ranks, grids, primary-rank rule, and stopping rule were frozen in
`FREQUENCY_WEIGHTED_PHYSICAL_ACCEPTANCE_2026-08-17.md` before this calculation.

For fixed stable ERA A,r, the physical BCF
    C_Y(t)=r^dag Y exp(A t) r
and spectrum are affine in the Hermitian metric Y.  We therefore fit the actual
BCF/spectrum while imposing the Huang coupled-Lindblad LMIs, rather than fitting
an unconstrained realization and minimizing coefficient projection afterward.
"""
from __future__ import annotations

import math
import numpy as np
import cvxpy as cp
from scipy.linalg import expm, svdvals

import direct_era_coupled_harmonic as era
import two_pole_cold_variance as fdt
import heom_harmonic_pade_depth as base

RANKS=(12,16,24)
NT=121
NX=241


def lin_c_expr(Y,A,r,t):
    q=expm(A*float(t))@r
    M=np.outer(q,np.conj(r))
    return cp.trace(Y@M)


def lin_s_expr(Y,A,r,x):
    v=np.linalg.solve(A+1j*float(x)*np.eye(A.shape[0]),r)
    M=np.outer(v,np.conj(r))
    return -2.0*cp.real(cp.trace(Y@M))


def physical_from_y(A,r,Y):
    Lam=1j*A
    return era.reconstruct_physical(Lam,r,Y)


def solve_weighted(A,r,C0,times,ctarget,xpos,starget_p,starget_m,wx,wu,S0):
    n=len(r); I=np.eye(n)
    Lam=1j*A

    def build_and_solve(solver):
        Y=cp.Variable((n,n),hermitian=True)
        Q=1j*(Y@Lam-Lam.conj().T@Y)
        Qh=(Q+Q.H)/2
        M0=np.outer(r,np.conj(r))
        c0expr=cp.real(cp.trace(Y@M0))
        constraints=[Y >> 1e-9*I, Qh >> 0, c0expr == float(C0)]

        jt_terms=[]
        for t,tar in zip(times,ctarget):
            z=lin_c_expr(Y,A,r,float(t))
            jt_terms.append(cp.square((cp.real(z)-float(tar.real))/C0) +
                            cp.square((cp.imag(z)-float(tar.imag))/C0))
        Jt=cp.sum(cp.hstack(jt_terms))/len(jt_terms)

        jx=[]; ju=[]
        for x,sp,sm,w1,w2 in zip(xpos,starget_p,starget_m,wx,wu):
            splus=lin_s_expr(Y,A,r,float(x))
            sminus=lin_s_expr(Y,A,r,float(-x))
            ssym=0.5*(splus+sminus)
            target=0.5*(float(sp)+float(sm))
            rr=(ssym-target)/S0
            jx.append(float(w1)*cp.square(rr))
            ju.append(float(w2)*cp.square(rr))
        Jx=cp.sum(cp.hstack(jx))
        Ju=cp.sum(cp.hstack(ju))
        objective=cp.Minimize(Jt+Jx+Ju)
        prob=cp.Problem(objective,constraints)
        if solver=='CLARABEL':
            prob.solve(solver=solver,verbose=False,tol_gap_abs=1e-10,
                       tol_gap_rel=1e-10,tol_feas=1e-10,max_iter=1500)
        else:
            prob.solve(solver=solver,verbose=False,eps=5e-9,max_iters=400000)
        if Y.value is None:
            return None
        Yv=np.asarray(Y.value,complex); Yv=.5*(Yv+Yv.conj().T)
        Qv=1j*(Yv@Lam-Lam.conj().T@Yv); Qv=.5*(Qv+Qv.conj().T)
        return dict(Y=Yv,solver=solver,status=prob.status,value=float(prob.value),
                    Ymin=float(np.linalg.eigvalsh(Yv).min()),
                    Qmin=float(np.linalg.eigvalsh(Qv).min()))

    out=build_and_solve('CLARABEL')
    if out is None or out['Ymin']<=0 or out['Qmin'] < -1e-9:
        out=build_and_solve('SCS')
    if out is None:
        raise RuntimeError('weighted physical SDP returned no solution')
    return out


def objective_components(A,r,Y,C0,times,ctarget,xpos,sp,sm,wx,wu,S0):
    c=np.array([np.vdot(r,Y@(expm(A*float(t))@r)) for t in times])
    Jt=float(np.mean(np.abs(c-ctarget)**2)/(C0*C0))
    ss=[]
    for x in xpos:
        vp=np.linalg.solve(A+1j*float(x)*np.eye(A.shape[0]),r)
        vm=np.linalg.solve(A-1j*float(x)*np.eye(A.shape[0]),r)
        splus=-2*np.real(np.vdot(r,Y@vp)); sminus=-2*np.real(np.vdot(r,Y@vm))
        ss.append(.5*(splus+sminus))
    ss=np.asarray(ss,float); target=.5*(sp+sm)
    rr=(ss-target)/S0
    Jx=float(np.sum(wx*rr*rr)); Ju=float(np.sum(wu*rr*rr))
    return Jt,Jx,Ju,c,ss


def susceptibility_weights(xpos,wc):
    vals=[]
    for x in xpos:
        yp=fdt.admittance(wc*float(x),base.R,base.ALPHA*wc)
        den=1.0-float(x)**2+1j*float(x)*yp/(base.C*wc)
        vals.append(1.0/(abs(den)**2))
    chi2=np.asarray(vals,float)
    wx=chi2/np.sum(chi2)
    rawu=xpos*xpos*chi2
    wu=rawu/np.sum(rawu)
    return wx,wu,chi2


def evaluate_model(rank,label,A,r,Y,ref,exact_eval,c0):
    phys=physical_from_y(A,r,Y)
    eg=np.linalg.eigvalsh(phys['Gamma'])
    pcorr=era.physical_corr(phys['K'],phys['g'],era.T_EVAL)
    pcm=era.bcf_metrics(pcorr,exact_eval,c0)
    pspec=era.physical_spectrum(phys['K'],phys['g'],era.X_SPEC)
    exact_spec=np.asarray(era.p.exact_dimless(era.X_SPEC),float)
    psm=era.spectrum_metrics(pspec,exact_spec)
    wings=np.concatenate([-np.geomspace(1e4,4.001,1200),era.X_SPEC,
                          np.geomspace(6.001,1e4,1200)])
    sw=era.physical_spectrum(phys['K'],phys['g'],wings)
    mins=float(sw.min())
    db=era.db_metrics_from_spectrum(lambda x: era.p.sexp(float(x),phys['K'],phys['g']))
    bath=dict(wc=era.WC,K=phys['K'],g=phys['g'],H=phys['H'],Gamma=phys['Gamma'])
    state=era.gaussian_state_metrics(bath,ref)
    rho=era.hg.gaussian_rho_from_cov(state['Vsys'],era.REF_DIM)[0]
    print(f'WEIGHTED_EVAL rank={rank} label={label} GammaMin={eg.min():+.12e} '
          f'minS={mins:+.12e} Cmaxabs={pcm[0]:.12e} Crms={pcm[1]:.12e} '
          f'Cmaxrel={pcm[2]:.12e} Smaxabs={psm[0]:.12e} Srms={psm[1]:.12e} '
          f'Smaxrel={psm[2]:.12e} maxwidth={state["maxwidth"]:.12e} '
          f'nuclear={state["nuclear"]:.12e}',flush=True)
    for x,(ratio,ex,e) in db.items():
        print(f'WEIGHTED_DB rank={rank} label={label} x={x:.2f} ratio={ratio:.12e} '
              f'exact={ex:.12e} logerr={e:.12e}',flush=True)
    physical=(eg.min()>=-1e-9 and mins>=-1e-9)
    impl=(state['bcferr']<1e-10 and state['vacres']<1e-12 and
          state['omega_relerr']<2e-9 and state['maxRe']<-1e-8 and
          state['lyap']<1e-10 and state['numin']>=.5-1e-9 and state['recon']<1e-7)
    return dict(phys=phys,pcm=pcm,psm=psm,db=db,state=state,rho=rho,
                gammaMin=float(eg.min()),minS=mins,physical=physical,impl=impl)


def half_nuclear(rho1,rho2):
    return .5*float(np.sum(svdvals(np.asarray(rho1.full())-np.asarray(rho2.full()))))


def main():
    era.synthetic_era_selftest()
    wc,sigma0,ref=era.physical_wc_sigma0()
    era.WC=wc
    samp_err=era.exact_sampler_audit(wc)
    if samp_err>=2e-6: raise RuntimeError('exact sampler audit failed')

    ttrain=np.arange(2*era.M)*era.DT
    samples=era.exact_correlation(ttrain,wc)
    era.T_EVAL=(np.arange(2*era.M-1)+.5)*era.DT
    exact_eval=era.exact_correlation(era.T_EVAL,wc)
    c0=float(abs(samples[0]))
    era.X_SPEC=np.linspace(-4.,6.,2401)

    times=np.linspace(0.,24.,NT)
    ctarget=era.exact_correlation(times,wc)
    xpos=np.linspace(.02,4.,NX)
    sp=np.asarray(era.p.exact_dimless(xpos),float)
    sm=np.asarray(era.p.exact_dimless(-xpos),float)
    S0=float(np.asarray(era.p.exact_dimless(np.array([0.])),float)[0])
    wx,wu,chi2=susceptibility_weights(xpos,wc)
    print(f'WEIGHT_GRID NT={NT} NX={NX} C0={c0:.12e} S0={S0:.12e} '
          f'x_peak={xpos[np.argmax(chi2)]:.6f} wx_peak={wx.max():.6e} '
          f'wu_peak_x={xpos[np.argmax(wu)]:.6f}',flush=True)

    rows={}
    for rank in RANKS:
        model=era.era_realization(samples,era.DT,era.M,rank)
        if model['max_re']>=0: raise RuntimeError(f'ERA rank {rank} unstable')
        l,r,alpha=era.balance_scalar_gauge(model['C'],model['B'])
        A=model['Ac']; Lam=1j*A

        # Prior coefficient-projection physicalization baseline.
        bsd=era.solve_general_sdp(Lam,l,r)
        base_eval=evaluate_model(rank,'coefficient',A,r,bsd['Y'],ref,exact_eval,c0)

        fit=solve_weighted(A,r,c0,times,ctarget,xpos,sp,sm,wx,wu,S0)
        Jt,Jx,Ju,_c,_ss=objective_components(A,r,fit['Y'],c0,times,ctarget,
                                             xpos,sp,sm,wx,wu,S0)
        c0_model=float(np.real(np.vdot(r,fit['Y']@r)))
        c0rel=abs(c0_model-c0)/c0
        print(f'WEIGHTED_SOLVE rank={rank} solver={fit["solver"]} status={fit["status"]} '
              f'objective={fit["value"]:.12e} Jtime={Jt:.12e} Jx={Jx:.12e} Ju={Ju:.12e} '
              f'Ymin={fit["Ymin"]:+.12e} Qmin={fit["Qmin"]:+.12e} '
              f'C0rel={c0rel:.12e}',flush=True)
        opt_eval=evaluate_model(rank,'weighted',A,r,fit['Y'],ref,exact_eval,c0)
        rows[rank]=dict(model=model,fit=fit,base=base_eval,opt=opt_eval,c0rel=c0rel,
                        J=(Jt,Jx,Ju))

    # Mandatory conditions for every optimized rank.
    mandatory=all(rows[r]['fit']['Ymin']>0 and rows[r]['fit']['Qmin']>=-1e-9 and
                  rows[r]['opt']['physical'] and rows[r]['opt']['impl'] and
                  rows[r]['c0rel']<1e-8 for r in RANKS)
    primary=rows[16]['opt']['state']
    primary_pass=(mandatory and ref['basis_err']<1e-7 and
                  primary['maxwidth']<1e-6 and primary['nuclear']<5e-6 and
                  primary['cross']<1e-5)
    control_dist=half_nuclear(rows[24]['opt']['rho'],rows[16]['opt']['rho'])
    control_ok=(rows[24]['opt']['physical'] and rows[24]['opt']['impl'] and control_dist<5e-6)
    finalpass=primary_pass and control_ok

    for r in RANKS:
        gainC=rows[r]['base']['pcm'][0]/rows[r]['opt']['pcm'][0]
        gainW=rows[r]['base']['state']['maxwidth']/rows[r]['opt']['state']['maxwidth']
        gainN=rows[r]['base']['state']['nuclear']/rows[r]['opt']['state']['nuclear']
        print(f'WEIGHTED_GAIN rank={r} gainC={gainC:.6e} gainWidth={gainW:.6e} '
              f'gainNuclear={gainN:.6e}',flush=True)
    print(f'WEIGHTED_CONTROL rank16_rank24_half_nuclear={control_dist:.12e}',flush=True)
    print(f'WEIGHTED_ACCEPTANCE mandatory={int(mandatory)} primary_pass={int(primary_pass)} '
          f'control_ok={int(control_ok)} finalpass={int(finalpass)}',flush=True)
    print('FREQUENCY_WEIGHTED_PHYSICAL_PASS' if finalpass else
          'FREQUENCY_WEIGHTED_PHYSICAL_FAIL',flush=True)


if __name__=='__main__': main()
