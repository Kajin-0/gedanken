#!/usr/bin/env python3
"""Provisional MQT capacitance compensation for increased external tilt.

This uses the retained cubic-barrier diagnostic ONLY:

    Gamma = omega/(2pi) exp[-alpha_Q DeltaU/(hbar omega)],
    omega=sqrt(kappa/(L C)), alpha_Q=7.2.

Rather than assuming an absolute dark target, use the current rDelta=.6,
`delta=.05`, `C=215 fF` point as the reference dark rate.  For each new tilt,
solve for the capacitance required to recover exactly that same provisional
Gamma.

This cleanly measures the dark-stability cost of directionality while avoiding
any ambiguity about which absolute D target originally generated the historical
Cmin,Q table.

The result is not exact dissipative rf-SQUID MQT because the causal environment
changes the bounce action/prefactor.  It is a relative diagnostic within the
same historical approximation.
"""

from __future__ import annotations

import math

from scipy.optimize import brentq

from full_dynamic_rfsquid import CASES, DynamicForce, T0
from finite_time_basin_slice import cold_phase_scale
from directional_recovery_barriers import directional_barriers, kelvin_scale
from tilt_directionality_pareto import with_tilt
from quantum_initial_capture import HBAR, KB

ALPHA_Q=7.2
CREF=215e-15
DREF=0.05


def log_rate(kappa: float,L: float,C: float,U: float) -> float:
    omega=math.sqrt(kappa/(L*C))
    return math.log(omega/(2*math.pi))-ALPHA_Q*U/(HBAR*omega)


def main() -> None:
    print('Experiment 03 tilt provisional-MQT compensation')
    base=DynamicForce(0.6,quick=False,Tmax=0.95)
    L,_,_=CASES[0.6]
    EK=kelvin_scale(0.6)

    mref=with_tilt(base,DREF)
    bref=directional_barriers(mref,T0)
    _,kref,wref=cold_phase_scale(mref,0.6)
    Uref=bref['b_left']*EK*KB
    lr0=log_rate(kref,L,CREF,Uref)
    tau0=1/wref

    print(
        f'reference: delta={DREF:.3f}, C={CREF*1e15:.1f} fF, '
        f'wc/2pi={wref/(2*math.pi)*1e-9:.4f} GHz, '
        f'U/(hbar wc)={Uref/(HBAR*wref):.4f}'
    )

    for delta in (0.025,0.05,0.06,0.07,0.075,0.08,0.09,0.10,0.11,0.125):
        m=with_tilt(base,delta)
        try:
            b=directional_barriers(m,T0)
            _,kappa,w_at_refC=cold_phase_scale(m,0.6)
        except Exception as exc:
            print(f'delta={delta:.3f}: no cold bistability ({exc})')
            continue
        U=b['b_left']*EK*KB
        lr_fixed=log_rate(kappa,L,CREF,U)
        penalty=math.exp(min(700.0,lr_fixed-lr0))

        def f(logC):
            C=math.exp(logC)
            return log_rate(kappa,L,C,U)-lr0
        # Increasing C suppresses the rate monotonically in the retained model.
        lo=math.log(1e-15); hi=math.log(100e-12)
        try:
            root=brentq(f,lo,hi,xtol=1e-12)
            Ccomp=math.exp(root)
            wcomp=math.sqrt(kappa/(L*Ccomp))
            phase_slow=(1/wcomp)/tau0
            msg=(
                f'delta={delta:.3f}: BL/kB={U/KB:.5f} K, '
                f'fixedC_rate_ratio={penalty:.3e}, '
                f'C_sameDark={Ccomp*1e15:.2f} fF ({Ccomp/CREF:.3f}x), '
                f'wc_sameDark/2pi={wcomp/(2*math.pi)*1e-9:.3f} GHz, '
                f'tau_phase_ratio={phase_slow:.3f}'
            )
        except ValueError:
            msg=(f'delta={delta:.3f}: BL/kB={U/KB:.5f} K, '
                 f'fixedC_rate_ratio={penalty:.3e}, no C root in bracket')
        print(msg)
        print(f'::notice title=Experiment 03 tilt MQT compensation::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
