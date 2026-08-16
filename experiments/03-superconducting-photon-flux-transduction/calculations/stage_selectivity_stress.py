#!/usr/bin/env python3
"""Cross-parameter stress test of the stage-selective damping hypothesis.

Hypothesis under test
---------------------
The sharp R80/alpha=.9, 14-um area-margin loss happened close to

    A_select = H_eff,L^2 / H_eff,C^2 = 1,

where H_eff^2 = int w^2 dt / int v^2 dt in the two passive-network stages

    launch: 0 -> first favored-side x=0 crossing
    capture: crossing -> cooling-side well reformation.

This script deliberately varies R, cutoff alpha and photon energy density to ask
whether A_select~1 is a robust organizing boundary or merely an accidental
feature of one scan.  For each point it reports

- thermal headroom Tadiab/Tfold;
- launch and capture durations in units of the cold phase period;
- A_select;
- pre-cross resistor-loss fraction relative to pre+capture;
- symmetrized-FDT TWA screening P_final (N=1024).

The stochastic fractions remain harsh semiclassical screening values, NOT exact
quantum efficiencies.  A_select is a deterministic trajectory diagnostic, NOT
a theorem.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.stats import spearmanr

from causal_two_pole_environment import filter_components
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import CASES, DynamicForce, T0, TAU0_CONDITIONAL, adiabatic_photon_temperature
from quantum_initial_capture import PHI_BAR
from nonlinear_fdt_twa_screen import run_case


def deterministic_features(model,R,alpha,A,lam=14.,rise_ps=20.,tend_ns=.35):
    L,C,_=CASES[.6]; xc,_,wc=cold_phase_scale(model,.6); Tf=model.fold_temperature()
    wd=alpha*wc; Lf,Cf=filter_components(R,wd)
    Tad=adiabatic_photon_temperature(lam,A)
    u0=T0*T0; du=Tad*Tad-u0; cool=1/(2*TAU0_CONDITIONAL*u0); tr=rise_ps*1e-12
    def src(t): return du/tr*math.exp(-t/tr)
    def rhs(t,y):
        x,v,u,d,w=y; u=max(float(u),u0); T=math.sqrt(u)
        return np.array([v,-(d+model.force(T,x))/(L*C),src(t)-cool*(u*u-u0*u0),
                         (L/Lf)*(v-w),d/(L*Cf)-w/(R*Cf)])
    tf=tend_ns*1e-9
    sol=solve_ivp(rhs,(0,tf),np.array([xc,0,u0,0,0],float),method='DOP853',rtol=3e-8,
                  atol=np.array([1e-10,2e2,1e-13,1e-10,2e2]),max_step=.08e-12,dense_output=True)
    ts=np.linspace(0,tf,16001); y=sol.sol(ts); x=y[0]; T=np.sqrt(np.maximum(y[2],u0))
    ip=int(np.argmax(T)); post=np.where(T[ip:]<Tf)[0]
    if not len(post): return {'valid':False,'reason':'no_reform','Tad':Tad,'Tf':Tf}
    trf=float(ts[ip+int(post[0])])
    ids=np.where(x[:-1]*x[1:]<0)[0]
    if not len(ids):
        return {'valid':False,'reason':'no_cross','Tad':Tad,'Tf':Tf,'trf':trf,'wc':wc}
    i=int(ids[0]); tc=brentq(lambda t:float(sol.sol(t)[0]),float(ts[i]),float(ts[i+1]))
    if tc>=trf:
        return {'valid':False,'reason':'cross_after_reform','Tad':Tad,'Tf':Tf,'tc':tc,'trf':trf,'wc':wc}

    def ints(ta,tb):
        tt=np.linspace(ta,tb,5001); yy=sol.sol(tt); v=yy[1]; w=yy[4]
        iv=float(np.trapezoid(v*v,tt)); iw=float(np.trapezoid(w*w,tt))
        q=PHI_BAR**2/R*iw
        return iv,iw,iw/iv,q
    _,_,hL,qL=ints(0,tc); _,_,hC,qC=ints(tc,trf)
    P0=2*math.pi/wc
    return {'valid':True,'Tad':Tad,'Tf':Tf,'wc':wc,'tc':tc,'trf':trf,
            'cyclesL':tc/P0,'cyclesC':(trf-tc)/P0,'Aselect':hL/hC,
            'fpre':qL/(qL+qC),'qratio':qL/qC,'hL':hL,'hC':hC}


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    # Chosen to cross both strong-capture and marginal regions without making
    # this first falsification sweep prohibitively expensive.
    points=[]
    for R in (40.,80.,150.):
        for alpha in (.6,.9,1.2):
            for A in (80.,86.,92.):
                points.append((R,alpha,A))

    rows=[]
    print('Experiment 03 stage-selectivity cross-parameter stress')
    for R,alpha,A in points:
        d=deterministic_features(model,R,alpha,A)
        o=run_case(model,14.,R=R,alpha=alpha,ntraj=1024,dt_ps=.25,seed=808080,
                   area_um2=A,rise_ps=20.)
        p=float(o['P_right_final'])
        if d['valid']:
            msg=(f'R={R:g} alpha={alpha:.2f} A={A:g}: P={p:.6f}; '
                 f'Thead={d["Tad"]/d["Tf"]:.4f}; '
                 f'cyclesL={d["cyclesL"]:.4f} cyclesC={d["cyclesC"]:.4f}; '
                 f'Aselect={d["Aselect"]:.5f} fpre={d["fpre"]:.5f} qpre/qcap={d["qratio"]:.5f}')
            rows.append((p,d['Aselect'],d['fpre'],d['cyclesC'],d['Tad']/d['Tf']))
        else:
            msg=(f'R={R:g} alpha={alpha:.2f} A={A:g}: P={p:.6f}; '
                 f'deterministic_stage={d["reason"]}; Thead={d["Tad"]/d["Tf"]:.4f}')
        print(msg); print(f'::notice title=Experiment 03 stage-selectivity stress::{msg}')

    if len(rows)>=5:
        arr=np.asarray(rows,float); fail=1-arr[:,0]
        # Rank correlations are used only as descriptive diagnostics; saturation
        # and shared-noise pairing violate naive independent-sample regression assumptions.
        for name,col in [('Aselect',1),('fpre',2),('cyclesC',3),('Thead',4)]:
            rho,pv=spearmanr(arr[:,col],fail)
            print(f'Spearman({name}, failure) rho={rho:+.4f}, nominal_p={pv:.3g}')
    print('PASS')

if __name__=='__main__': main()
