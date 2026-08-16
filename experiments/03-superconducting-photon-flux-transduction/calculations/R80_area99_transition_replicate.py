#!/usr/bin/env python3
"""Independent replication at the two current R80 P~.99 transition points.

Adds a third high-statistics seed only at A=86.5 and 87.0 um^2 so the threshold
can be combined with the existing independent N=8192 runs without spending
more trajectories far from the transition.

Fractions are symmetrized-FDT TWA screening values, not exact quantum efficiencies.
"""
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    N=8192
    for A in (86.5,87.0):
        o=run_case(model,14.,R=80.,alpha=.90,ntraj=N,dt_ps=.125,seed=848484,
                   area_um2=A,rise_ps=20.)
        k=int(o['n_right_final']); lo,hi=wilson(k,N)
        msg=(f'A={A:.1f} N={N} P_final={o["P_right_final"]:.7f} '
             f'CI95=[{lo:.7f},{hi:.7f}] fail={N-k} '
             f'P_reform={o["P_xright_reform"]:.7f}')
        print(msg); print(f'::notice title=Experiment 03 R80 transition replicate::{msg}')
    print('PASS')
if __name__=='__main__': main()
