#!/usr/bin/env python3
"""Extend finite-temperature dark diagnostic along constant-B high-tilt family.

Not a physical DCR calculation. Reports actual cold barrier, compensated phase
frequency and a deliberately crude Arrhenius falsification scale through delta=.22.
The purpose is to identify where equal zero-temperature tunneling action ceases
to imply even plausibly comparable finite-temperature dark stability.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
from finite_time_basin_slice import cold_phase_scale
from directional_recovery_barriers import directional_barriers
from quantum_initial_capture import HBAR, KB, PHI_BAR

B_TARGET=37.61
B_DISS={
 .050:29.76563577,.080:22.6112773,.100:18.76503780,.120:15.4275357,
 .140:12.49903278,.150:11.16332163,.160:9.90315950,.180:7.58847202,
 .200:5.52063400,.220:3.65877364,
}


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    L=fd.CASES[.6][0]; EL=PHI_BAR**2/L
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
            wc=wc0/r; fc=wc/(2*math.pi)
            theta=barrierK/fd.T0
            Tx=HBAR*wc/(2*math.pi*KB)
            log10arr=math.log10(fc)-theta/math.log(10)
            # Thermal exponent needed for a nominal 1e-6/s scale if the prefactor
            # were f_c; diagnostic only, not a Kramers prefactor.
            theta_req=math.log(fc/1e-6)
            margin=theta-theta_req
            msg=(f'delta={delta:.3f}: barrier={barrierK:.6f}K Bq={B:.6f} r={r:.6f} '
                 f'fc_scaled={fc*1e-9:.5f}GHz DeltaU/kBT0={theta:.2f} '
                 f'theta_req_fc_for_1e-6={theta_req:.2f} thermal_margin={margin:+.2f} '
                 f'Tcross_diag={Tx:.5f}K log10_crude_arr={log10arr:.2f}')
            print(msg); print(f'::notice title=Experiment 03 extended finiteT dark::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')

if __name__=='__main__': main()
