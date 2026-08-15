#!/usr/bin/env python3
"""External-tilt directionality versus dark-stability Pareto screen.

Experiment 03 Generation A currently uses a small normalized external tilt
`delta=0.05`.  The one-sided-fold analysis shows that directionality is a real
lever: stronger tilt should move the deterministic write trajectory and deepen
the favored state, but it also lowers the occupied metastable cold barrier.

This script changes only the load-line tilt in the already computed rDelta=.6
full-CPR force table.  Since

    F(x,T;delta) = x-delta-I(x,T),

changing delta is exactly a constant force-table shift; the expensive CPR does
not need to be recomputed.

For each tilt it reports:
- cold left/write barrier and favored right/return barrier;
- cold phase frequency and action-like barrier ratio DeltaU/(hbar omega_c);
- cooling-side fold temperature and 100-um2 quasistatic fold wavelength;
- deterministic causal-filter reformation state for the favorable 8-um-
  equivalent energy density at alpha=.5 and .7.

This is a design/falsification screen, not a dark-count prediction.  Exact
quantum escape must use the same causal environment.
"""

from __future__ import annotations

import copy
import math

import numpy as np
from scipy.interpolate import RectBivariateSpline

from causal_two_pole_environment import simulate_filtered
from directional_recovery_barriers import directional_barriers, kelvin_scale
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import (
    DynamicForce,
    DELTA_TILT,
    T0,
)
from quantum_initial_capture import HBAR, KB


def with_tilt(base: DynamicForce, delta: float) -> DynamicForce:
    m=copy.copy(base)
    m.Ftab=np.asarray(base.Ftab,dtype=float)-(float(delta)-DELTA_TILT)
    m.spline=RectBivariateSpline(m.Tgrid,m.xgrid,m.Ftab,kx=3,ky=3)
    return m


def fold_lambda(Tf: float) -> float:
    return 1.55*(2.5**2-T0**2)/(Tf**2-T0**2)


def main() -> None:
    print('Experiment 03 tilt directionality/dark-barrier Pareto')
    print('rDelta=.6, beta=.8 retained; changing normalized external tilt only')
    base=DynamicForce(0.6,quick=False,Tmax=0.95)
    EK=kelvin_scale(0.6)

    for delta in (0.00,0.025,0.05,0.075,0.10,0.125,0.15,0.175,0.20,0.225,0.25):
        m=with_tilt(base,delta)
        try:
            b=directional_barriers(m,T0)
            x_c,kappa,wc=cold_phase_scale(m,0.6)
            Tf=m.fold_temperature(hi=0.90)
        except Exception as exc:
            print(f'delta={delta:.3f}: no retained cold bistable-left state ({exc})')
            continue

        BL=b['b_left']*EK
        BR=b['b_right']*EK
        action=(BL*KB)/(HBAR*wc)
        parts=[]
        for alpha in (0.50,0.70):
            try:
                o=simulate_filtered(m,0.6,250.0,alpha,lambda_um=8.0,
                                    rise_ps=20.0,tend_ns=0.5)
                parts.append(
                    f'a{alpha:.2f}:{o["basin"]},xf={float(o["x_final"]):+.3f}'
                )
            except Exception as exc:
                parts.append(f'a{alpha:.2f}:ERR')
        msg=(
            f'delta={delta:.3f}: BL/kB={BL:.5f} K, BR/kB={BR:.5f} K, '
            f'BR/BL={BR/BL:.3f}, wc/2pi={wc/(2*math.pi)*1e-9:.3f} GHz, '
            f'BL/(hbar wc)={action:.3f}, Tf={Tf:.5f} K, '
            f'lambda_fold={fold_lambda(Tf):.2f} um, ' + ', '.join(parts)
        )
        print(msg)
        print(f'::notice title=Experiment 03 tilt Pareto::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
