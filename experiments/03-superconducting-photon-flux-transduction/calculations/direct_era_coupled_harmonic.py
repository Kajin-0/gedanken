#!/usr/bin/env python3
"""Direct exact-BCF ERA -> coupled-Lindblad -> harmonic FDT benchmark.

Acceptance and the only allowed refinement were frozen in
`DIRECT_ERA_COUPLED_ACCEPTANCE_2026-08-17.md` before this calculation.

This branch changes the quasi-Lindblad realization coordinates only.  The exact
physical direct-port BCF, published coupled-Lindblad SDP conditions, exact
counterterm, and harmonic FDT/full-state oracle are unchanged.
"""
from __future__ import annotations

import math
import numpy as np
import cvxpy as cp
from scipy.linalg import hankel, logm, svd, expm, solve_continuous_lyapunov, svdvals

import direct_port_bath_correlation as bc
import run_coupled_lindblad_pade_sdp as runner
import coupled_lindblad_harmonic_gaussian as hg
import heom_harmonic_final_state_gate as finalgate
import heom_harmonic_pade_depth as base
from quantum_initial_capture import PHI_BAR

p = runner.probe

DT = 0.05
M = 512
RANKS = (12, 16, 24)
NMATS = 10000
REF_DIM = 16


def physical_wc_sigma0():
    ref = finalgate.exact_reference(REF_DIM)
    sigma0 = ref['sigma0']
    wc = base.HBAR / (2.0 * base.C * PHI_BAR**2 * sigma0**2)
    return wc, sigma0, ref


def exact_correlation(taus, wc, nmats=NMATS):
    """Vectorized exact 10000-Matsubara BCF in Gate-B coupling convention."""
    taus = np.asarray(taus, float).ravel()
    cscale = (PHI_BAR / bc.HBAR)**2 / (wc * wc)
    out = np.zeros(len(taus), complex)

    for pole in bc.bath_poles():
        d = bc.bath_coeff(pole) * cscale
        z = 1j * pole / wc
        out += d * np.exp(-z * taus)

    n = np.arange(1, nmats + 1, dtype=float)
    nu_phys = 2.0 * math.pi * n / (bc.BETA * bc.HBAR)
    z = nu_phys / wc
    coeff = (-2.0 * bc.G * nu_phys * bc.WD**4 /
             (bc.BETA * (nu_phys**4 + bc.WD**4))) * cscale
    # Chunk Matsubara modes to keep peak memory modest.
    for j in range(0, nmats, 500):
        zz = z[j:j+500]
        cc = coeff[j:j+500]
        out += np.exp(-np.outer(taus, zz)) @ cc
    return out


def exact_sampler_audit(wc):
    taus = np.array([0.0, 0.25, 1.0, 4.0])
    ys = exact_correlation(taus, wc)
    cscale = (PHI_BAR / bc.HBAR)**2 / (wc * wc)
    errs = []
    for tau, val in zip(taus, ys):
        q = bc.corr_quad(float(tau) / wc) * cscale
        err = abs(val-q) / max(abs(q), 1e-300)
        errs.append(err)
        print(f'EXACT_SAMPLER tau={tau:.3f} series=({val.real:+.12e}{val.imag:+.12e}j) '
              f'quad=({q.real:+.12e}{q.imag:+.12e}j) relerr={err:.12e}', flush=True)
    mx = float(max(errs))
    print(f'EXACT_SAMPLER_MAXERR={mx:.12e}', flush=True)
    return mx


def era_realization(samples, dt, m, rank):
    y = np.asarray(samples, complex)
    if len(y) < 2*m:
        raise ValueError('ERA needs at least 2m samples')
    H0 = hankel(y[:m], y[m-1:2*m-1])
    H1 = hankel(y[1:m+1], y[m:2*m])
    U, s, Vh = svd(H0, full_matrices=False, lapack_driver='gesdd')
    if rank > len(s) or s[rank-1] <= 0:
        raise RuntimeError('requested ERA rank exceeds numerical Hankel rank')
    Ur = U[:, :rank]
    Vhr = Vh[:rank, :]
    sr = s[:rank]
    sq = np.sqrt(sr)
    isq = 1.0 / sq
    V = Vhr.conj().T

    # Balanced ERA realization H_k = C A^k B.
    Ad = (isq[:, None] * (Ur.conj().T @ H1 @ V)) * isq[None, :]
    B = sq * Vhr[:, 0]
    C = U[0, :rank] * sq

    evd = np.linalg.eigvals(Ad)
    rho = float(np.max(np.abs(evd)))
    Ac = np.asarray(logm(Ad), complex) / dt
    evc = np.linalg.eigvals(Ac)
    max_re = float(np.max(evc.real))
    return dict(Ad=Ad, Ac=Ac, B=B, C=C, sing=s, rho=rho,
                max_re=max_re, evd=evd, evc=evc)


def eval_realization(era, taus):
    A, B, C = era['Ac'], era['B'], era['C']
    return np.array([complex(C @ (expm(A*float(t)) @ B)) for t in taus])


def generic_spectrum(era, xs):
    A, B, C = era['Ac'], era['B'], era['C']
    I = np.eye(A.shape[0], dtype=complex)
    vals = []
    for x in np.asarray(xs, float):
        integ = -C @ np.linalg.solve(A + 1j*x*I, B)
        vals.append(2.0 * float(np.real(integ)))
    return np.asarray(vals, float)


def synthetic_era_selftest():
    z = np.array([0.31+1.10j, 0.73-0.37j, 1.47+1.83j])
    d = np.array([1.0+0.15j, 0.42-0.07j, 0.18+0.03j])
    dt = 0.05
    m = 40
    ts = np.arange(2*m) * dt
    y = np.sum(d[None, :] * np.exp(-ts[:, None]*z[None, :]), axis=1)
    era = era_realization(y, dt, m, 3)
    te = (np.arange(79)+0.5)*dt
    ye = np.sum(d[None, :] * np.exp(-te[:, None]*z[None, :]), axis=1)
    yr = eval_realization(era, te)
    rel = np.max(np.abs(yr-ye) / np.maximum(np.abs(ye), 1e-12*abs(ye[0])))
    print(f'ERA_SELFTEST maxrel={rel:.12e} rho={era["rho"]:.12e} '
          f'maxRe={era["max_re"]:+.12e}', flush=True)
    if rel >= 1e-10 or era['max_re'] >= 0:
        raise RuntimeError('synthetic ERA self-test failed')
    return float(rel)


def balance_scalar_gauge(C, B):
    l = np.conj(np.asarray(C, complex))
    r = np.asarray(B, complex).copy()
    nl = float(np.linalg.norm(l)); nr = float(np.linalg.norm(r))
    if nl == 0 or nr == 0:
        raise RuntimeError('zero ERA input/output vector')
    alpha = math.sqrt(nl/nr)
    return l/alpha, r*alpha, alpha


def solve_general_sdp(Lam, l, r):
    n = len(r)
    I = np.eye(n)

    def one(solver):
        Y = cp.Variable((n,n), hermitian=True)
        Q = 1j*(Y@Lam - Lam.conj().T@Y)
        Qh = (Q+Q.H)/2
        cons = [Y >> 1e-9*I, Qh >> 0]
        obj = cp.Minimize(cp.sum_squares(cp.abs(l-Y@r)))
        prob = cp.Problem(obj, cons)
        if solver == 'CLARABEL':
            prob.solve(solver=solver, verbose=False, tol_gap_abs=1e-10,
                       tol_gap_rel=1e-10, tol_feas=1e-10, max_iter=1000)
        else:
            prob.solve(solver=solver, verbose=False, eps=1e-9,
                       max_iters=300000)
        if Y.value is None:
            return None
        Yv = np.asarray(Y.value, complex)
        Yv = 0.5*(Yv+Yv.conj().T)
        Qv = 1j*(Yv@Lam-Lam.conj().T@Yv)
        Qv = 0.5*(Qv+Qv.conj().T)
        ymin = float(np.linalg.eigvalsh(Yv).min())
        qmin = float(np.linalg.eigvalsh(Qv).min())
        res = float(np.linalg.norm(l-Yv@r))
        rel = res/max(float(np.linalg.norm(l)), 1e-300)
        return dict(Y=Yv, status=prob.status, solver=solver, ymin=ymin,
                    qmin=qmin, residual=res, rel=rel, objective=res*res)

    out = one('CLARABEL')
    if out is None or out['ymin'] <= 0 or out['qmin'] < -1e-9:
        if 'SCS' not in cp.installed_solvers():
            raise RuntimeError('general SDP failed and SCS unavailable')
        out = one('SCS')
    if out is None:
        raise RuntimeError('general coupled-Lindblad SDP returned no solution')
    print(f'GENERAL_SDP solver={out["solver"]} status={out["status"]} '
          f'Ymin={out["ymin"]:+.12e} Qmin={out["qmin"]:+.12e} '
          f'residual={out["residual"]:.12e} rel={out["rel"]:.12e}', flush=True)
    return out


def reconstruct_physical(Lam, r, Y):
    ey, U = np.linalg.eigh(Y)
    if ey.min() <= 0:
        raise RuntimeError(f'Y not positive: {ey.min()}')
    X = (U*np.sqrt(ey)) @ U.conj().T
    Xi = (U*(1.0/np.sqrt(ey))) @ U.conj().T
    K = X @ Lam @ Xi
    g = X @ r
    H = 0.5*(K+K.conj().T)
    Gamma = (K.conj().T-K)/(2j)
    Gamma = 0.5*(Gamma+Gamma.conj().T)
    return dict(K=K, g=g, H=H, Gamma=Gamma, Yev=ey)


def bcf_metrics(vals, exact, c0):
    diff = vals-exact
    maxabs = float(np.max(np.abs(diff))/c0)
    rms = float(np.sqrt(np.mean(np.abs(diff)**2))/c0)
    mask = np.abs(exact) >= 1e-4*c0
    maxrel = float(np.max(np.abs(diff[mask])/np.abs(exact[mask])))
    return maxabs, rms, maxrel


def spectrum_metrics(vals, exact):
    s0 = float(np.interp(0.0, X_SPEC, exact))
    diff = vals-exact
    maxabs = float(np.max(np.abs(diff))/s0)
    rms = float(np.sqrt(np.mean(diff*diff))/s0)
    mask = exact >= 1e-3*s0
    maxrel = float(np.max(np.abs(diff[mask])/exact[mask]))
    return maxabs, rms, maxrel


def db_metrics_from_spectrum(fun):
    out = {}
    beta_wc = bc.BETA * bc.HBAR * WC
    for x in (0.5, 1.0, 1.13, 1.5, 2.0):
        sp = float(fun(+x)); sm = float(fun(-x))
        ex = math.exp(-beta_wc*x)
        err = math.inf if sp <= 0 or sm <= 0 else abs(math.log(sm/sp)-math.log(ex))
        out[x] = (sm/sp if sp != 0 else math.nan, ex, err)
    return out


def physical_corr(K, g, taus):
    return np.array([p.cc(float(t), K, g) for t in taus])


def physical_spectrum(K, g, xs):
    return np.array([p.sexp(float(x), K, g) for x in np.asarray(xs,float)])


def gaussian_state_metrics(bath, ref):
    sigma0 = ref['sigma0']
    # Convention identities.
    bcferr = max(abs(hg.bcf_from_real(float(t), bath) - p.cc(float(t),bath['K'],bath['g'])) /
                 max(abs(p.cc(float(t),bath['K'],bath['g'])),1e-14) for t in hg.TAUS)
    Aa, Da, _ = hg.aux_real_matrices(bath['H'], bath['Gamma'])
    Vvac = 0.5*np.eye(Aa.shape[0])
    vacres = float(np.linalg.norm(Aa@Vvac+Vvac@Aa.T+Da,ord='fro') /
                   max(np.linalg.norm(Da,ord='fro'),1.0))
    Gmat, A, Diff, Om, _lam = hg.enlarged_matrices(bath, sigma0)
    nm = len(bath['g'])+1
    omega_iso = math.sqrt(Gmat[0,0]*Gmat[nm,nm])
    omega_relerr = abs(omega_iso/hg.EXPECTED_OMEGA_RATIO-1.0)
    maxRe = float(np.max(np.linalg.eigvals(A).real))
    if maxRe >= 0:
        raise RuntimeError(f'physicalized ERA full drift unstable: {maxRe}')
    V = solve_continuous_lyapunov(A,-Diff)
    V = np.asarray(np.real_if_close(V,tol=1000),float)
    V = 0.5*(V+V.T)
    lyap = float(np.linalg.norm(A@V+V@A.T+Diff,ord='fro') /
                 max(np.linalg.norm(Diff,ord='fro'),1.0))
    numin = float(hg.symplectic_nu(V,Om).min())
    Vsys = np.array([[V[0,0],V[0,nm]],[V[nm,0],V[nm,nm]]],float)
    sx = math.sqrt(2*sigma0*sigma0*Vsys[0,0]); su=math.sqrt(2*sigma0*sigma0*Vsys[1,1])
    relx=sx/ref['target_x']-1; relu=su/ref['target_u']-1
    maxwidth=max(abs(relx),abs(relu))
    cross=abs(Vsys[0,1])/math.sqrt(Vsys[0,0]*Vsys[1,1])
    rho,gr=hg.gaussian_rho_from_cov(Vsys,REF_DIM)
    nuclear=0.5*float(np.sum(svdvals(np.asarray(rho.full())-np.asarray(ref['rho'].full()))))
    out=dict(bcferr=float(bcferr),vacres=vacres,omega_relerr=omega_relerr,maxRe=maxRe,
             lyap=lyap,numin=numin,Vsys=Vsys,sx=sx,su=su,relx=relx,relu=relu,
             maxwidth=maxwidth,cross=cross,nuclear=nuclear,recon=gr['recerr'])
    print(f'ERA_GAUSSIAN bcferr={out["bcferr"]:.12e} vacres={vacres:.12e} '
          f'omega_relerr={omega_relerr:.12e} maxRe={maxRe:+.12e} lyap={lyap:.12e} '
          f'numin={numin:.12e} relx={relx:+.12e} relu={relu:+.12e} '
          f'maxwidth={maxwidth:.12e} cross={cross:.12e} nuclear={nuclear:.12e} '
          f'recon={gr["recerr"]:.12e}',flush=True)
    return out


def run_rank(rank, samples, exact_eval, c0, exact_spec, ref):
    print(f'ERA_RANK_BEGIN rank={rank}',flush=True)
    era = era_realization(samples,DT,M,rank)
    singratio = era['sing'][rank-1]/era['sing'][0]
    print(f'ERA_MODEL rank={rank} rho={era["rho"]:.12e} maxRe={era["max_re"]:+.12e} '
          f'sigma_r/sigma_1={singratio:.12e} next_ratio=' +
          (f'{era["sing"][rank]/era["sing"][0]:.12e}' if rank < len(era['sing']) else 'NA'),flush=True)
    if era['max_re'] >= 0:
        raise RuntimeError(f'ERA rank {rank} continuous realization unstable')

    qcorr = eval_realization(era,T_EVAL)
    qcm = bcf_metrics(qcorr,exact_eval,c0)
    qspec = generic_spectrum(era,X_SPEC)
    qsm = spectrum_metrics(qspec,exact_spec)
    qdb = db_metrics_from_spectrum(lambda x: generic_spectrum(era,np.array([x]))[0])
    print(f'ERA_QUASI rank={rank} Cmaxabs={qcm[0]:.12e} Crms={qcm[1]:.12e} '
          f'Cmaxrel={qcm[2]:.12e} Smaxabs={qsm[0]:.12e} Srms={qsm[1]:.12e} '
          f'Smaxrel={qsm[2]:.12e}',flush=True)

    l,r,alpha=balance_scalar_gauge(era['C'],era['B'])
    Lam=1j*era['Ac']
    sdp=solve_general_sdp(Lam,l,r)
    phys=reconstruct_physical(Lam,r,sdp['Y'])
    eg=np.linalg.eigvalsh(phys['Gamma'])
    pcorr=physical_corr(phys['K'],phys['g'],T_EVAL)
    pcm=bcf_metrics(pcorr,exact_eval,c0)
    pspec=physical_spectrum(phys['K'],phys['g'],X_SPEC)
    psm=spectrum_metrics(pspec,exact_spec)
    wings=np.concatenate([-np.geomspace(1e4,4.001,1200),X_SPEC,np.geomspace(6.001,1e4,1200)])
    sw=physical_spectrum(phys['K'],phys['g'],wings)
    minS=float(sw.min())
    pdb=db_metrics_from_spectrum(lambda x: p.sexp(float(x),phys['K'],phys['g']))
    print(f'ERA_PHYSICAL rank={rank} gauge={alpha:.12e} relSDP={sdp["rel"]:.12e} '
          f'Ymin={sdp["ymin"]:+.12e} Qmin={sdp["qmin"]:+.12e} '
          f'GammaMin={eg.min():+.12e} minS={minS:+.12e} '
          f'Cmaxabs={pcm[0]:.12e} Crms={pcm[1]:.12e} Cmaxrel={pcm[2]:.12e} '
          f'Smaxabs={psm[0]:.12e} Srms={psm[1]:.12e} Smaxrel={psm[2]:.12e}',flush=True)
    for x,(ratio,ex,err) in pdb.items():
        print(f'ERA_DB rank={rank} x={x:.2f} ratio={ratio:.12e} exact={ex:.12e} '
              f'logerr={err:.12e}',flush=True)

    bath=dict(wc=WC,K=phys['K'],g=phys['g'],H=phys['H'],Gamma=phys['Gamma'])
    state=gaussian_state_metrics(bath,ref)
    physical_ok=(sdp['ymin']>0 and sdp['qmin']>=-1e-9 and eg.min()>=-1e-9 and minS>=-1e-9)
    impl_ok=(state['bcferr']<1e-10 and state['vacres']<1e-12 and state['omega_relerr']<2e-9 and
             state['maxRe']<-1e-8 and state['lyap']<1e-10 and state['numin']>=0.5-1e-9 and
             state['recon']<1e-7)
    return dict(rank=rank,era=era,qcm=qcm,qsm=qsm,sdp=sdp,phys=phys,pcm=pcm,psm=psm,
                minS=minS,gammaMin=float(eg.min()),state=state,
                physical_ok=physical_ok,impl_ok=impl_ok)


def main():
    global WC,T_EVAL,X_SPEC
    synthetic_era_selftest()
    WC,sigma0,ref=physical_wc_sigma0()
    sampler_err=exact_sampler_audit(WC)
    if sampler_err>=2e-6:
        raise RuntimeError('exact 10000-Matsubara sampler failed quadrature audit')

    ttrain=np.arange(2*M)*DT
    samples=exact_correlation(ttrain,WC)
    # Independent off-grid midpoint evaluation over the same full horizon.
    T_EVAL=(np.arange(2*M-1)+0.5)*DT
    exact_eval=exact_correlation(T_EVAL,WC)
    c0=float(abs(samples[0]))
    X_SPEC=np.linspace(-4.0,6.0,2401)
    exact_spec=np.asarray(p.exact_dimless(X_SPEC),float)

    print(f'ERA_GRID dt={DT} m={M} horizon={ttrain[-1]:.6f} C0={c0:.12e} '
          f'ref_basis_err={ref["basis_err"]:.12e}',flush=True)

    rows=[]
    failures=[]
    for rank in RANKS:
        try:
            rows.append(run_rank(rank,samples,exact_eval,c0,exact_spec,ref))
        except Exception as exc:
            failures.append((rank,repr(exc)))
            print(f'ERA_RANK_FAILURE rank={rank} error={exc!r}',flush=True)

    by={r['rank']:r for r in rows}
    have_all=all(r in by for r in RANKS)
    mandatory=have_all and all(by[r]['physical_ok'] and by[r]['impl_ok'] for r in RANKS)
    monotone=False
    if have_all:
        monotone=(by[16]['pcm'][0] < by[12]['pcm'][0] and by[24]['pcm'][0] < by[16]['pcm'][0] and
                  by[16]['state']['maxwidth'] < by[12]['state']['maxwidth'] and
                  by[24]['state']['maxwidth'] < by[16]['state']['maxwidth'] and
                  by[16]['state']['nuclear'] < by[12]['state']['nuclear'] and
                  by[24]['state']['nuclear'] < by[16]['state']['nuclear'])
    finalpass=(mandatory and monotone and ref['basis_err']<1e-7 and
               by[24]['state']['maxwidth']<1e-6 and by[24]['state']['nuclear']<5e-6 and
               by[24]['state']['cross']<1e-5)

    authorize=False
    if 16 in by and 24 in by:
        authorize=(by[16]['physical_ok'] and by[16]['impl_ok'] and by[24]['physical_ok'] and by[24]['impl_ok'] and
                   by[24]['state']['maxwidth']<by[16]['state']['maxwidth'] and
                   by[24]['state']['nuclear']<by[16]['state']['nuclear'] and
                   by[24]['state']['maxwidth']<2e-5 and by[24]['state']['nuclear']<2e-5 and
                   by[24]['pcm'][0]<5e-5 and not finalpass)

    print(f'ERA_ACCEPTANCE have_all={int(have_all)} mandatory={int(mandatory)} '
          f'monotone={int(monotone)} finalpass={int(finalpass)} '
          f'authorize_refined={int(authorize)} failures={failures}',flush=True)
    if finalpass:
        print('DIRECT_ERA_HARMONIC_PASS',flush=True)
    elif authorize:
        print('DIRECT_ERA_AUTHORIZE_REFINED_MATRIX',flush=True)
    else:
        print('DIRECT_ERA_FIRST_MATRIX_FAIL',flush=True)


if __name__=='__main__':
    main()
