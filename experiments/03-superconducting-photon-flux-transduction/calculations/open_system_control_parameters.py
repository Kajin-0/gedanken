#!/usr/bin/env python3
"""Control parameters for selecting the Experiment-03 quantum open-system method.

The purpose is to prevent an uncontrolled jump from the validated reaction-
coordinate circuit to a convenient local/secular Lindblad equation.

At the certified delta=.212 point this script computes:

1. exact two-pole filter Lf,Cf and its bare damping ratio;
2. low-amplitude phase damping inferred directly from ReY(omega_c);
3. normal modes of the *coupled cold harmonic phase+filter Hamiltonian*;
4. resistor damping participation of those normal modes;
5. normal-mode splitting versus damping, as a secular-approximation diagnostic;
6. optical-rise and fold-free interval relative to coherent/dissipative times.

These are approximation-control diagnostics, not detector-performance metrics.
"""
from __future__ import annotations
import math
import numpy as np

import full_dynamic_rfsquid as fd
from causal_two_pole_environment import filter_components, re_y_ratio
from finite_time_basin_slice import cold_phase_scale
from time_dependent_unitary_phase import thermal_history, crossings

L=111.5e-12
C=24.262211e-12
R=7.5308506
DELTA=.212
ALPHA=.90
RISE_PS=20.
AREA=490.


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA; fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        xc,kappa,wc=cold_phase_scale(model,.6)
        wd=ALPHA*wc
        Lf,Cf=filter_components(R,wd)

        # For fixed phase coordinate, the filter obeys
        #   psi_ddot + [1/(R Cf)] psi_dot + wd^2 psi = 0.
        kappa_f=1/(R*Cf)
        zeta_f=kappa_f/(2*wd)
        Qf=wd/kappa_f
        tau_filter_amp=2/kappa_f

        rey_ratio=re_y_ratio(wc,wd)
        G_eff=(1/R)*rey_ratio
        gamma_phase_amp=G_eff/(2*C)
        tau_phase_amp=1/gamma_phase_amp
        tau_phase_energy=1/(2*gamma_phase_amp)

        # Coupled quadratic Hamiltonian in coordinates [x, y=psi/Phi_bar].
        # V/Phi_bar^2 = .5*(kappa/L)x^2 + .5*(x-y)^2/Lf.
        K=np.array([[kappa/L+1/Lf,-1/Lf],[-1/Lf,1/Lf]],float)
        M=np.diag([C,Cf])
        Minv2=np.diag(1/np.sqrt(np.diag(M)))
        A=Minv2@K@Minv2
        eigval,E=np.linalg.eigh(A)
        wn=np.sqrt(eigval)

        # Classical velocity damping matrix D=diag(0,1/R). In mass-weighted
        # normal coordinates, diagonal participation gives the isolated-mode
        # viscous coefficient d_j. If a weak-coupling modal picture were valid,
        # the amplitude decay would be d_j/2.
        D=np.diag([0.,1/R])
        Dm=Minv2@D@Minv2
        d=np.array([E[:,j].T@Dm@E[:,j] for j in range(2)])
        gam=d/2
        split=wn[1]-wn[0]
        secular_ratio=split/float(np.sum(gam))

        Tf=model.fold_temperature(hi=.98)
        Tof,Tad,ts,TT=thermal_history(14.,AREA,RISE_PS,1000.)
        cc=crossings(ts,TT,Tf)
        tup,tdown=cc[0],cc[-1]
        absent=tdown-tup

        print(f'delta={DELTA:.5f} C={C*1e12:.6f}pF R={R:.7f}ohm '
              f'fc={wc/(2*math.pi)*1e-9:.7f}GHz wd/2pi={wd/(2*math.pi)*1e-9:.7f}GHz')
        print(f'filter Lf={Lf*1e9:.9f}nH Cf={Cf*1e12:.9f}pF '
              f'kappa_f={kappa_f*1e-9:.7f}GHz(rad/s units e9) zeta={zeta_f:.9f} Q={Qf:.9f} '
              f'tau_filter_amp={tau_filter_amp*1e12:.3f}ps')
        print(f'phase ReY(wc)/(1/R)={rey_ratio:.9f} G_eff={G_eff:.9e}S '
              f'gamma_amp/wc={gamma_phase_amp/wc:.9f} tau_phase_amp={tau_phase_amp*1e9:.6f}ns '
              f'tau_phase_energy={tau_phase_energy*1e9:.6f}ns')
        for j in range(2):
            print(f'normal{j+1}: f={wn[j]/(2*math.pi)*1e-9:.8f}GHz '
                  f'gamma_amp={gam[j]*1e-9:.8f}e9/s gamma/omega={gam[j]/wn[j]:.8f} '
                  f'phase_mass_component={E[0,j]:+.8f} filter_mass_component={E[1,j]:+.8f}')
        print(f'normal splitting/2pi={split/(2*math.pi)*1e-9:.8f}GHz '
              f'split/(gamma1+gamma2)={secular_ratio:.8f}')
        print(f'drive omega_c*tau_r={wc*RISE_PS*1e-12:.8f} '
              f'tau_r/Tphase={RISE_PS*1e-12/(2*math.pi/wc):.8f} '
              f'fold_absent={absent*1e12:.3f}ps '
              f'fold_absent/tau_filter_amp={absent/tau_filter_amp:.5f} '
              f'fold_absent/tau_phase_energy={absent/tau_phase_energy:.5f}')

        msg=(f'delta=.212: filter_zeta={zeta_f:.4f} Qf={Qf:.4f}; '
             f'phase_gamma_over_omega={gamma_phase_amp/wc:.4f}; '
             f'normal_gamma_over_omega=({gam[0]/wn[0]:.4f},{gam[1]/wn[1]:.4f}); '
             f'secular_split_over_sumgamma={secular_ratio:.4f}; '
             f'omega_tau_r={wc*RISE_PS*1e-12:.4f}; '
             f'fold_absent_ps={absent*1e12:.2f}')
        print(msg); print(f'::notice title=Experiment 03 open-system control parameters::{msg}')

        # These are intentionally qualitative validity gates. A secular weak-
        # coupling treatment would require ratios parametrically much smaller/
        # larger than unity, not merely passing a tuned numerical threshold.
        if not (0 < zeta_f < 1.5): raise RuntimeError('unexpected filter damping regime')
        if not (0 < wn[0] < wn[1]): raise RuntimeError('normal-mode solve failed')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original

if __name__=='__main__': main()
