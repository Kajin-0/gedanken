#!/usr/bin/env python3
"""Nonlinear stationary-bath TWA screen for dark-compensated external tilt.

Directionality can improve write capture but reduces the occupied-state cold
barrier.  `tilt_mqt_compensation.py` used the historical cubic MQT diagnostic
to determine the capacitance required to restore the SAME provisional dark rate
as the retained reference point

    delta=0.05, C=215 fF.

This script tests whether that dark-compensated tilt improves nonlinear
semiclassical capture.  For each tilt, the full force table is shifted exactly
by the load-line tilt change and the shared rDelta=.6 circuit capacitance is
patched to its same-dark value before calling the established nonlinear
causal-FDT TWA/GLE solver.

The compensation is only as physical as the retained cubic MQT diagnostic.  A
real device must recompute dissipative MQT with the same causal Y(omega).
Reported capture fractions are likewise TWA/GLE screening numbers, not exact
quantum efficiencies.
"""

from __future__ import annotations

import argparse
import math

from full_dynamic_rfsquid import CASES, DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson
from tilt_directionality_pareto import with_tilt

# Same-dark C values from experiment03-tilt-mqt-compensation run 31914613147.
COMP = {
    0.050: 215.00e-15,
    0.060: 242.84e-15,
    0.070: 275.94e-15,
    0.075: 294.88e-15,
    0.080: 315.67e-15,
}


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--delta',type=float,required=True)
    ap.add_argument('--ntraj',type=int,default=512)
    ap.add_argument('--dt-ps',type=float,default=0.5)
    ap.add_argument('--seed',type=int,default=97531)
    args=ap.parse_args()

    delta=round(args.delta,3)
    if delta not in COMP:
        raise SystemExit(f'unsupported compensated tilt {delta}; choose {sorted(COMP)}')

    # CASES is a shared mutable dictionary imported by the established solver
    # stack.  Patch only rDelta=.6 for this isolated process.
    L,Cold,Tf=CASES[0.6]
    Cnew=COMP[delta]
    CASES[0.6]=(L,Cnew,Tf)

    print('Experiment 03 nonlinear FDT dark-compensated tilt scan')
    print(
        f'delta={delta:.3f}, C={Cnew*1e15:.2f} fF '
        f'({Cnew/Cold:.3f}x historical), N={args.ntraj}, dt={args.dt_ps} ps'
    )
    print('C chosen to preserve historical cubic-MQT reference rate; not exact dissipative MQT')

    base=DynamicForce(0.6,quick=False,Tmax=0.95)
    model=with_tilt(base,delta)

    # Focus first on the strongest energy-density lobe.  Include 10/11-um
    # equivalents to detect any phase-lobe relocation caused by C/tilt changes.
    for alpha in (0.45,0.50,0.55,0.60,0.65,0.70,0.80):
        for lam in (8.0,10.0,11.0):
            o=run_case(
                model,lam,alpha=alpha,R=250.0,ntraj=args.ntraj,
                dt_ps=args.dt_ps,seed=args.seed,
            )
            n=int(o['ntraj']); k=int(o['n_right_final'])
            lo,hi=wilson(k,n)
            msg=(
                f'delta={delta:.3f}, C={Cnew*1e15:.2f} fF, alpha={alpha:.2f}, '
                f'lambdaEq={lam:.1f} um: coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
                f'P_reform={o["P_xright_reform"]:.5f}, '
                f'P_final={o["P_right_final"]:.5f} CI95=[{lo:.5f},{hi:.5f}], '
                f'xR={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
                f'uR={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}, '
                f'rho={o["rho_xu_reform"]:+.3f}, '
                f'tauCold={o["tau_cold_ns"]:.3f} ns'
            )
            print(msg)
            print(f'::notice title=Experiment 03 compensated-tilt TWA::{msg}')

    print('PASS')


if __name__=='__main__':
    main()
