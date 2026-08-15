#!/usr/bin/env python3
"""Causal-cutoff robustness scan of favorable energy-density lobes.

The wavelength tangent scan found unusually large phase-only reformation margins
near alpha=omega_D/omega_c~0.5 for several stronger pulse-energy densities.
This script tests whether those points form broad design plateaus or narrow
phase-matching resonances.

It uses the same deterministic full-CPR tangent diagnostic as
initial_quantum_tangent_scan.py.  It is not a physical capture probability and
does not include full stationary bath history.
"""

from __future__ import annotations

from full_dynamic_rfsquid import DynamicForce
from initial_quantum_tangent_scan import tangent_case


def main() -> None:
    print('Experiment 03 tangent alpha robustness scan')
    print('rDelta=.6, R=250 ohm, rise=20 ps, full CPR Tmax=.95 K')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    alphas=[0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.80]
    for lam in (8.0,9.0,10.0,11.0,12.0):
        print(f'\nlambda={lam:.1f} um equivalent energy density')
        for alpha in alphas:
            o=tangent_case(model,250.0,alpha,lam)
            if not o['fold_removed']:
                msg=f'lambda={lam:.1f} alpha={alpha:.2f}: fold not removed'
            else:
                msg=(
                    f'lambda={lam:.1f} alpha={alpha:.2f}: '
                    f'x={o["x"]:+.5f}, u={o["u"]:+.5f}, dx={o["dx"]:+.5f}, '
                    f'Aphase={o["A_phase"]:.4f}, sigma_phase={o["sigma_xf_phase"]:.5f}, '
                    f'margin_phase={o["x_margin_phase_sigma"]:.4f}, '
                    f'treform={o["tf"]*1e12:.2f} ps'
                )
            print(msg)
            print(f'::notice title=Experiment 03 alpha robustness::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
