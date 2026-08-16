#!/usr/bin/env python3
"""Same-environment cold dark-stability screen for the current R80 candidate.

This is deliberately conservative in claim scope.  It reports:

1. the exact static cold barrier/curvature of the current rDelta=.6 CPR model;
2. the passive two-pole admittance and local Q at the cold phase frequency for
   R=80 ohm, alpha=.90;
3. the *existing provisional isolated cubic-barrier MQT diagnostic* used
   elsewhere in Experiment 03;
4. the corresponding C_min for a diagnostic 1e-6 /s dark-rate target.

It does NOT solve dissipative tunneling in the frequency-dependent two-pole
bath.  Therefore neither the isolated MQT rate nor any local-Q correction is a
physical dark-count prediction.  The purpose is only to determine whether the
strong capture candidate is parametrically near or hopelessly far from the
previous cold-stability target.
"""
from __future__ import annotations

import math

from full_dynamic_rfsquid import CASES, DynamicForce, T0
from finite_time_basin_slice import cold_phase_scale
from directional_recovery_barriers import directional_barriers, kelvin_scale
from causal_two_pole_environment import filter_components
from capacitance_stability_window import cmin_mqt, ALPHA_Q, D_TARGET, HBAR, KB


def main():
    r=.6; R=80.; alpha=.90
    model=DynamicForce(r,quick=False)
    L,C,_=CASES[r]
    xc,kappa,wc=cold_phase_scale(model,r)
    b=directional_barriers(model,T0)
    EK=kelvin_scale(r)
    barrierK=b['b_left']*EK
    barrierJ=barrierK*KB
    action_ratio=barrierJ/(HBAR*wc)

    wd=alpha*wc
    Lf,Cf=filter_components(R,wd)
    reY=(1/R)/(1+(wc/wd)**4)
    Reff=1/reY
    Qc=wc*C/reY

    gamma_iso=wc/(2*math.pi)*math.exp(-ALPHA_Q*action_ratio)
    Cmin=cmin_mqt(L,barrierK,kappa,D_TARGET,ALPHA_Q)

    print('Experiment 03 R80 same-environment cold-stability SCREEN')
    print('WARNING: frequency-dependent dissipative tunneling is NOT solved here')
    print(f'rDelta={r:.1f}, L={L*1e12:.4f} pH, C={C*1e15:.3f} fF')
    print(f'cold x={xc:+.6f}, curvature={kappa:.6f}, fc={wc/(2*math.pi)*1e-9:.6f} GHz')
    print(f'cold left barrier/kB={barrierK:.6f} K, DeltaU/(hbar wc)={action_ratio:.6f}')
    print(f'two-pole R={R:g} ohm alpha={alpha:.2f}: ReY(wc)={reY:.8e} S, Reff={Reff:.3f} ohm, Qc={Qc:.6f}')
    print(f'filter Lf={Lf*1e12:.5f} pH, Cf={Cf*1e15:.5f} fF')
    print(f'provisional ISOLATED cubic-MQT diagnostic Gamma={gamma_iso:.6e} s^-1')
    print(f'provisional C_min(D={D_TARGET:.1e}/s)={Cmin*1e15:.3f} fF; actual/Cmin={C/Cmin:.5f}')
    print('Interpretation: isolated-MQT numbers are scale diagnostics only; the selected passive Y(omega) must enter the tunneling action and prefactor consistently before any physical DCR statement.')
    print('PASS')

if __name__=='__main__': main()
