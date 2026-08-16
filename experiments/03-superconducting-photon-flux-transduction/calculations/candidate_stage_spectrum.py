#!/usr/bin/env python3
"""Stage-resolved spectral diagnostic for the passive two-pole candidate.

The frequency-selective damping lemma is only relevant to Experiment 03 if the
actual nonlinear phase dynamics provide distinct spectral content during launch
and capture/reformation.  This script tests that assumption.

For deterministic candidate trajectories it evaluates, separately on

    launch:   0 -> first favored-side x=0 crossing
    capture:  first crossing -> cooling-side well reformation

1. duration and phase displacement;
2. RMS phase velocity;
3. time-domain filter attenuation

       H_eff^2 = integral w^2 dt / integral v^2 dt,

   where w is the resistor-capacitor node voltage in phase-rate units and the
   exact resistor loss is proportional to integral w^2/R dt;
4. Hann-window spectral centroids and 50/90% power frequencies of v(t);
5. the same quantiles after weighting the phase-velocity spectrum by the exact
   quartic dissipative admittance ReY(omega).

The finite segments are nonstationary and the filter carries memory across the
segment boundary, so the FFT quantities are diagnostics, not exact segmented
energy identities.  The time-domain dissipation partition remains the exact
energy accounting.
"""
from __future__ import annotations

import math
import numpy as np

from candidate_dissipation_partition import trajectory, first_cross
from causal_energetic_lock import trace_lock
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import DynamicForce


def quantiles(freq,power,qs=(.5,.9)):
    power=np.maximum(np.asarray(power,float),0.0)
    total=float(np.sum(power))
    if total<=0: return [math.nan for _ in qs]
    c=np.cumsum(power)/total
    return [float(np.interp(q,c,freq)) for q in qs]


def segment_diag(sol,wc,R,alpha,ta,tb,label):
    # Fine uniform sampling; enough points that FFT-grid error is small compared
    # with the short-segment spectral resolution itself.
    duration=tb-ta
    n=max(2049,int(math.ceil(duration/0.02e-12))+1)
    if n%2==0: n+=1
    t=np.linspace(ta,tb,n)
    y=sol.sol(t)
    x,v,w=y[0],y[1],y[4]
    dt=float(t[1]-t[0])
    iv=float(np.trapezoid(v*v,t)); iw=float(np.trapezoid(w*w,t))
    heff2=iw/iv if iv>0 else math.nan
    dx=float(x[-1]-x[0])
    vrms=math.sqrt(iv/duration)
    wrms=math.sqrt(iw/duration)

    # Window the raw velocity after subtracting its segment mean.  The omitted
    # drift/DC component is reported separately through dx/duration.
    win=np.hanning(n)
    vp=(v-np.mean(v))*win
    V=np.fft.rfft(vp)
    f=np.fft.rfftfreq(n,dt)
    pv=np.abs(V)**2
    if len(pv): pv[0]=0.0
    cent=float(np.sum(f*pv)/np.sum(pv)) if np.sum(pv)>0 else math.nan
    f50,f90=quantiles(f,pv)

    omega=2*math.pi*f
    wd=alpha*wc
    reY=(1/R)/(1+(omega/wd)**4)
    pd=pv*reY
    dcent=float(np.sum(f*pd)/np.sum(pd)) if np.sum(pd)>0 else math.nan
    df50,df90=quantiles(f,pd)

    return {
        'label':label,'duration_ps':duration*1e12,'dx':dx,
        'drift_rate_GHz':(dx/duration)/(2*math.pi)*1e-9,
        'vrms':vrms,'wrms':wrms,'heff2':heff2,
        'cent_GHz':cent*1e-9,'f50_GHz':f50*1e-9,'f90_GHz':f90*1e-9,
        'dcent_GHz':dcent*1e-9,'df50_GHz':df50*1e-9,'df90_GHz':df90*1e-9,
    }


def main():
    print('Experiment 03 stage-resolved two-pole spectral diagnostic')
    model=DynamicForce(.6,quick=False,Tmax=.95)
    for R,alpha in [(150.,.8),(80.,.7),(80.,.9),(80.,1.0),(40.,.9),(20.,.9)]:
        sol,wc=trajectory(model,R,alpha,lambda_um=8.0,rise_ps=20.0,tend_ns=.5)
        tc=first_cross(sol,.5e-9)
        lock=trace_lock(model,R,alpha,lambda_um=8.0,rise_ps=20.0,tend_ns=.5)
        trf=lock['t_reform']
        a=segment_diag(sol,wc,R,alpha,0.0,tc,'launch')
        b=segment_diag(sol,wc,R,alpha,tc,trf,'capture')
        print(f'\nR={R:g} alpha={alpha:.2f} wc/2pi={wc/(2*math.pi)*1e-9:.3f} GHz')
        for z in (a,b):
            msg=(f'{z["label"]}: dt={z["duration_ps"]:.2f}ps dx={z["dx"]:+.4f} '
                 f'drift={z["drift_rate_GHz"]:.3f}GHz vrms={z["vrms"]:.3e} '
                 f'wrms={z["wrms"]:.3e} Heff2={z["heff2"]:.5f}; '
                 f'vSpec centroid/f50/f90={z["cent_GHz"]:.2f}/{z["f50_GHz"]:.2f}/{z["f90_GHz"]:.2f}GHz; '
                 f'dissWeighted centroid/f50/f90={z["dcent_GHz"]:.2f}/{z["df50_GHz"]:.2f}/{z["df90_GHz"]:.2f}GHz')
            print(msg)
            print(f'::notice title=Experiment 03 stage spectrum::{msg}')
        ratio=(a['f50_GHz']/b['f50_GHz']) if b['f50_GHz']>0 else math.nan
        aratio=(a['heff2']/b['heff2']) if b['heff2']>0 else math.nan
        print(f'launch/capture f50 ratio={ratio:.3f}; Heff2 ratio={aratio:.3f}')
    print('PASS')

if __name__=='__main__': main()
