#!/usr/bin/env python3
"""Deep x-grid refinement of the candidate rDelta=0.6 scalar-R optimum.

This exists because the previous nx=17 -> 33 shift at R=250 ohm was still
large enough to straddle the 99% capture threshold.  It is intentionally
narrow: only the candidate optimum and nearby bracketing points are evaluated.
"""
from full_dynamic_rfsquid import DynamicForce
from quantum_basin_xgrid import integrate_case


def run(model, R):
    nxs=[17,33,65]
    results,stats,tail=integrate_case(
        model,0.6,float(R),20.0,
        nxs=nxs,zmax_x=4.75,zmax_u=5.75,nscan_u=81,
    )
    vals={n:p for n,p in results}
    p=vals[65]
    d17_33=vals[33]-vals[17]
    d33_65=vals[65]-vals[33]
    msg=(f"rDelta=0.6, rise=20 ps, R={R:g} ohm; "
         f"nx17={vals[17]:.7f}, nx33={vals[33]:.7f}, nx65={vals[65]:.7f}; "
         f"d17_33={d17_33:+.7f}, d33_65={d33_65:+.7f}; "
         f"Gaussian_tail<={tail:.3e}; "
         f"edge_count={int(stats['min_edges'])}..{int(stats['max_edges'])}; "
         f"max_neighbor_dP={stats['max_dp_neighbor']:.3f}")
    print(msg)
    print(f"::notice title=Experiment 03 deep optimum refinement::{msg}")


def main():
    model=DynamicForce(0.6,quick=False)
    for R in (200,225,250,275,300):
        run(model,R)
    print("PASS")

if __name__=="__main__":
    main()
