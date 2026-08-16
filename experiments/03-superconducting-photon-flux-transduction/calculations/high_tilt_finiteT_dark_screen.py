#!/usr/bin/env python3
"""Finite-temperature dark-side diagnostic along the equal-action high-tilt family.

This is NOT a physical dark-count-rate calculation.  It tabulates quantities
needed to decide whether the zero-temperature Euclidean-action optimization is
approaching a thermal-activation/crossover problem:

- cold directional barrier DeltaU/kB,
- equal-action electrical scale r=B_target/B_diss,
- compensated cold phase frequency,
- barrier ratio DeltaU/(kB*T0),
- harmonic quantum/classical crossover diagnostic hbar*omega_c/(2*pi*kB),
- crude Arrhenius scale f_c exp[-DeltaU/(kB*T0)] only as an order-of-magnitude
  falsification screen.

The latter is not a Kramers rate and must never be quoted as a physical DCR.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
from finite_time_basin_slice import cold_phase_scale
from directional_recovery_barriers import directional_barriers
from quantum_initial_capture import HBAR, KB, PHI_BAR

B_TARGET=37.61
B_DISS={
 .050:29.7656361,.055:28.4189359,.060:27.1429682,.065:25.9301238,
 .070:24.7742334,.075:23.6696502,.080:22.6112773,.085:21.5947909,
}
C0=215e-15


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    L=fd.CASES[.6][0]
    EL=PHI_BAR**2/L
    try:
        fd.BETA_COLD=.80
        print(f'T0={fd.T0:.6f} K')
        for delta,B in B_DISS.items():
            fd.DELTA_TILT=delta
            model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
            _,_,wc0=cold_phase_scale(model,.6)
            bd=directional_barriers(model,fd.T0)
            barrierK=bd['b_left']*EL/KB
            r=B_TARGET/B
            wc=wc0/r
            fc=wc/(2*math.pi)
            thermal_exp=barrierK/fd.T0
            Tx=HBAR*wc/(2*math.pi*KB)
            log10_arr=math.log10(fc)-thermal_exp/math.log(10)
            msg=(f'delta={delta:.3f}: barrier={barrierK:.6f}K B0={B:.6f} r={r:.6f} '
                 f'fc_scaled={fc*1e-9:.5f}GHz DeltaU/kBT0={thermal_exp:.2f} '
                 f'Tcross_diag={Tx:.5f}K log10[f_c exp(-DeltaU/kBT0)]={log10_arr:.2f}')
            print(msg); print(f'::notice title=Experiment 03 high-tilt finiteT dark screen::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')

if __name__=='__main__': main()
