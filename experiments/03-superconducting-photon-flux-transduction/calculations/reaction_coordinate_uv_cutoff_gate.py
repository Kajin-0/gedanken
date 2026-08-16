#!/usr/bin/env python3
"""Diagnose the residual-Ohmic UV boundary of the reaction-coordinate bridge.

The two-pole network makes the *phase* noise finite because ReY_port~omega^-4.
After lifting the network to an explicit filter coordinate, however, the physical
resistor is still ideal Ohmic. The filter-capacitor voltage / conjugate-momentum
variance is therefore expected to carry the logarithmic zero-point UV divergence
of an Ohmic quantum Brownian oscillator unless a microscopic resistor cutoff is
specified.

This script varies the upper frequency cutoff in the exact quantum-FDT covariance
while keeping the low-frequency bound fixed. It transforms [x,u,d,s] to
[x,y=psi/Phi_bar,u,s] and tests which moments converge.
"""
from __future__ import annotations
import math
import numpy as np

import full_dynamic_rfsquid as fd
from causal_two_pole_environment import filter_components
from finite_time_basin_slice import cold_phase_scale
from two_pole_joint_covariance import covariance_matrix

L=111.5e-12; C=24.262211e-12; R=7.5308506; DELTA=.212; ALPHA=.90


def transform(M,Lf):
    a=Lf/L
    T=np.array([[1,0,0,0],[1,0,-a,0],[0,1,0,0],[0,0,0,1]],float)
    return T@M@T.T


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA; fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        _,_,wc=cold_phase_scale(model,.6); wd=ALPHA*wc; Lf,Cf=filter_components(R,wd)
        ymaxs=(8.,10.,12.,14.,16.,18.,20.,22.,24.)
        rows=[]
        print(f'delta=.212 wc/2pi={wc/(2*math.pi)*1e-9:.7f}GHz Lf={Lf*1e9:.6f}nH Cf={Cf*1e12:.6f}pF')
        for ym in ymaxs:
            M=transform(covariance_matrix(model,.6,R,ALPHA,y_min=-22,y_max=ym),Lf)
            row=(ym,math.sqrt(M[0,0]),math.sqrt(M[1,1]),math.sqrt(M[2,2]),math.sqrt(M[3,3]))
            rows.append(row)
            cutoff=math.exp(ym)*wc/(2*math.pi)
            print(f'ymax={ym:4.1f} fmax={cutoff:.6e}Hz '
                  f'sigx={row[1]:.9e} sigy={row[2]:.9e} sigu={row[3]:.9e} sigs={row[4]:.9e}')

        arr=np.array(rows)
        # Relative changes over the final four e-fold increments.
        for col,name in [(1,'sigx'),(2,'sigy'),(3,'sigu')]:
            rel=abs(arr[-1,col]-arr[-3,col])/arr[-1,col]
            print(f'{name} relative change ymax20->24 = {rel:.6e}')
        # For a logarithmically divergent variance, sigma_s^2 should grow linearly
        # with y_max. Fit the high-cutoff tail.
        yy=arr[-5:,0]; var_s=arr[-5:,4]**2
        slope,inter=np.polyfit(yy,var_s,1)
        fit=slope*yy+inter
        ss_res=np.max(np.abs(var_s-fit))/max(np.ptp(var_s),1e-30)
        print(f's_variance_tail_slope_per_logomega={slope:.9e} '
              f'linear_tail_relative_residual={ss_res:.6e} '
              f'sigma_s_growth_16to24={arr[-1,4]/arr[-5,4]:.6f}x')
        msg=(f'delta=.212: phase/filter-coordinate moments converge, but filter velocity variance '
             f'has linear-in-log-cutoff tail slope={slope:.3e}; '
             f'sigma_s(24)/sigma_s(16)={arr[-1,4]/arr[-5,4]:.3f}; '
             f'tail_fit_residual={ss_res:.3e}')
        print(msg); print(f'::notice title=Experiment 03 reaction-coordinate UV gate::{msg}')
        if abs(arr[-1,1]-arr[-3,1])/arr[-1,1] > 2e-4: raise RuntimeError('phase position covariance not UV converged')
        if abs(arr[-1,2]-arr[-3,2])/arr[-1,2] > 2e-4: raise RuntimeError('filter coordinate covariance not UV converged')
        if abs(arr[-1,3]-arr[-3,3])/arr[-1,3] > 2e-4: raise RuntimeError('phase velocity covariance not UV converged')
        if slope<=0 or ss_res>.03: raise RuntimeError('expected logarithmic s-variance tail not resolved')
        print('PASS: explicit reaction-coordinate momentum requires a physical residual-bath UV cutoff.')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original

if __name__=='__main__': main()
