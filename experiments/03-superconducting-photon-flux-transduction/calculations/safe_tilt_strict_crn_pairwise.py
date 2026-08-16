#!/usr/bin/env python3
"""Strict common-random-number comparison for the safe interior tilt optimum.

The first CRN workflow reused only RNG seeds.  That is not rigorous because the
cold prehistory length is 12*tau_cold and therefore the FFT length changes with
design; identical seeds then map to different Fourier variates.

This worker fixes that defect.  For one absorber area it:

1. constructs all five dark-rate-constrained designs;
2. chooses one common prehistory equal to 12 times the *slowest* cold decay time;
3. uses one common dt and therefore one common FFT grid / history length;
4. reinitializes the RNG with the same seed for every design, so the underlying
   standard-normal Fourier coefficients are identical while each design applies
   its own physically correct PSD scaling;
5. returns each trajectory's final basin label;
6. reports paired discordant counts and a paired standard error / exact McNemar
   binomial p-value for differences between designs.

The purpose is ranking, not final efficiency certification.  Capture remains a
symmetrized-FDT TWA screen.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.stats import binomtest

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from causal_two_pole_environment import filter_components
from directional_recovery_barriers import directional_barriers
from history_fdt_reformation_margin import cold_pole_data, state_matrix
from quantum_initial_capture import quantum_covariance
from two_pole_cold_variance import variance_ratios
from nonlinear_fdt_twa_convergence import wilson
import safe_tilt_optimum_worker as sw

DELTAS=(.21200,.21225,.21250,.21275,.21300)
# High-resolution roots already established in this session.  The .212 root is
# solved once below because the earlier .212 screen used a periodic-only target.
KNOWN_ROOTS={
    .21225:10.749111487,
    .21250:10.885578211,
    .21275:11.035674041,
    .21300:11.2051409652,
}
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
NTRAJ=2048; BATCH=64; DT_PS=.125; TPOST_NS=2.0
SEEDS={490.:8834901,495.:8834951,500.:8835001}


def make_design(delta,root):
    original=fd.CASES[.6]
    C=C0*root*root; R=R0/root
    fd.BETA_COLD=.80; fd.DELTA_TILT=delta
    fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
    model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
    cov=quantum_covariance(model,.6)
    x_c=cov['x_c']; wc=cov['omega_c']; wd=ALPHA*wc
    Lf,Cf=filter_components(R,wd)
    Acold=state_matrix(model,R,x_c,fd.T0,Lf,Cf)
    _,_,_,tau=cold_pole_data(Acold)
    return dict(delta=delta,root=root,C=C,R=R,model=model,cov=cov,wc=wc,wd=wd,
                Lf=Lf,Cf=Cf,tau=tau,original=original)


def run_fixed(design,area,tpre,seed):
    model=design['model']; R=design['R']; C=design['C']; wc=design['wc']; wd=design['wd']
    cov=design['cov']; x_c=cov['x_c']; kappa=cov['kappa_c']
    Lf,Cf=design['Lf'],design['Cf']; L=L0
    dt=DT_PS*1e-12; npre=int(round(tpre/dt)); tpre=npre*dt
    tpost=TPOST_NS*1e-9; npost=int(round(tpost/dt))+1; ntotal=npre+npost
    _,Tarr=nf.thermal_trace(14.,dt,tpost,area_um2=area,rise_ps=20.)
    Tf=model.fold_temperature(); imax=int(np.argmax(Tarr)); ids=np.where(Tarr[imax:]<Tf)[0]
    if not len(ids): raise RuntimeError('no cooling-side reformation')
    ireform=imax+int(ids[0])
    saddle=directional_barriers(model,Tf-2e-5)['saddle']; left,right=model.cold_states()
    _rq,_rv,sxratio,svratio,_=variance_ratios(model,.6,R,ALPHA)
    sx_ref=cov['sigma_x']*sxratio; su_ref=cov['sigma_x']*svratio

    rng=np.random.default_rng(seed)
    labels=[]; reform_labels=[]; x0all=[]; u0all=[]; xfall=[]
    for start in range(0,NTRAJ,BATCH):
        nb=min(BATCH,NTRAJ-start)
        # Because ntotal, batch and seed are common across designs, this call
        # uses identical underlying standard Gaussian FFT coefficients.  Only
        # the PSD scale changes with the physical design.
        noise=nf.gaussian_noise_batch(rng,nb,ntotal,dt,L,R,wd)
        dx=np.zeros(nb); v=np.zeros(nb); dd=np.zeros(nb); w=np.zeros(nb)
        for i in range(npre-1):
            dx,v,dd,w=nf.linear_step_heun(dx,v,dd,w,noise[:,i],noise[:,i+1],dt,
                                         L,C,kappa,Lf,Cf,R)
        x=x_c+dx; x0all.append(x.copy()); u0all.append((v/wc).copy())
        base=npre-1; xr=None
        for j in range(npost-1):
            x,v,dd,w=nf.nonlinear_step_heun(model,x,v,dd,w,noise[:,base+j],noise[:,base+j+1],
                                            Tarr[j],Tarr[j+1],dt,L,C,Lf,Cf,R)
            if j+1==ireform: xr=x.copy()
        if xr is None: raise RuntimeError('missing reform sample')
        reform_labels.append(xr>saddle)
        labels.append(np.abs(x-right)<np.abs(x-left)); xfall.append(x.copy())
    labels=np.concatenate(labels); reform=np.concatenate(reform_labels)
    x0=np.concatenate(x0all); u0=np.concatenate(u0all); xf=np.concatenate(xfall)
    return dict(labels=labels,reform=reform,P=float(labels.mean()),Preform=float(reform.mean()),
                failures=int((~labels).sum()),coldRegX=float(np.std(x0,ddof=1)/sx_ref),
                coldRegU=float(np.std(u0,ddof=1)/su_ref),xf=float(np.mean(xf)),
                sxf=float(np.std(xf,ddof=1)),Tf=Tf,reform_ps=ireform*dt*1e12,
                tpre_ns=tpre*1e9,ntotal=ntotal)


def paired(a,b):
    # Difference P_b-P_a. n10: b succeeds where a fails; n01 vice versa.
    n10=int(np.count_nonzero((~a)&b)); n01=int(np.count_nonzero(a&(~b)))
    d=(n10-n01)/len(a); disc=n10+n01
    # Variance of paired Bernoulli difference values {-1,0,+1}.
    z=b.astype(float)-a.astype(float); se=float(np.std(z,ddof=1)/math.sqrt(len(z)))
    p=1.0 if disc==0 else float(binomtest(min(n10,n01),disc,.5,alternative='two-sided').pvalue)
    return n10,n01,d,se,p


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--area',type=float,required=True); a=ap.parse_args()
    area=float(a.area)
    if area not in SEEDS: raise SystemExit('supported area: 490,495,500')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        r212,_,_,_=sw.solve_root(.21200)
        roots={.21200:r212,**KNOWN_ROOTS}
        designs=[]
        for d in DELTAS:
            designs.append(make_design(d,roots[d]))
            fd.CASES[.6]=original; nf.CASES[.6]=original
        tpre=12*max(z['tau'] for z in designs)
        dt=DT_PS*1e-12; npre=int(math.ceil(tpre/dt)); tpre=npre*dt
        print(f'area={area:g}um2 N={NTRAJ} strict_CRN=yes common_tpre={tpre*1e9:.6f}ns '
              f'common_ntotal={npre+int(round(TPOST_NS*1e-9/dt))+1} seed={SEEDS[area]}')
        outs={}
        for z in designs:
            # Re-activate design globals for the force helper methods.
            fd.BETA_COLD=.80; fd.DELTA_TILT=z['delta']; fd.CASES[.6]=(L0,z['C'],original[2]); nf.CASES[.6]=fd.CASES[.6]
            o=run_fixed(z,area,tpre,SEEDS[area]); outs[z['delta']]=o
            k=NTRAJ-o['failures']; lo,hi=wilson(k,NTRAJ)
            msg=(f'delta={z["delta"]:.5f} r={z["root"]:.9f} C={z["C"]*1e12:.6f}pF '
                 f'fc={z["wc"]/(2*math.pi)*1e-9:.7f}GHz Tf={o["Tf"]:.7f}K '
                 f'P={o["P"]:.8f} CI95=[{lo:.8f},{hi:.8f}] fail={o["failures"]} '
                 f'Preform={o["Preform"]:.8f} coldReg=({o["coldRegX"]:.4f},{o["coldRegU"]:.4f}) '
                 f'xfinal={o["xf"]:+.6f}+-{o["sxf"]:.6f}')
            print(msg); print(f'::notice title=Experiment 03 strict CRN marginal::{msg}')
        # Adjacent and all-vs-.21200 paired comparisons.
        pairs=[]
        for x,y in zip(DELTAS[:-1],DELTAS[1:]): pairs.append((x,y))
        for y in DELTAS[1:]: pairs.append((DELTAS[0],y))
        seen=set()
        for x,y in pairs:
            if (x,y) in seen: continue
            seen.add((x,y)); n10,n01,diff,se,p=paired(outs[x]['labels'],outs[y]['labels'])
            msg=(f'area={area:g} pair delta {x:.5f}->{y:.5f}: dP={diff:+.8f} pairedSE={se:.8f} '
                 f'gain={n10} loss={n01} discord={n10+n01} McNemarExactP={p:.6g}')
            print(msg); print(f'::notice title=Experiment 03 strict CRN paired difference::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
