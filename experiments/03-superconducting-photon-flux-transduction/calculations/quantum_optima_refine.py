#!/usr/bin/env python3
"""Refine probability-optimal scalar-R points with nested x-grid integration."""
from full_dynamic_rfsquid import DynamicForce
from quantum_basin_xgrid import integrate_case


def run(model,r,rise,R):
    results,stats,tail=integrate_case(
        model,r,float(R),float(rise),
        nxs=[9,17,33],zmax_x=4.5,zmax_u=5.5,nscan_u=65,
    )
    vals={n:p for n,p in results}
    p=vals[33]
    msg=(f"rDelta={r:.1f}, rise={rise:g} ps, R={R:g} ohm; "
         f"nx9={vals[9]:.6f}, nx17={vals[17]:.6f}, nx33={p:.6f}; "
         f"tail_interval=[{p:.6f},{min(1,p+tail):.6f}]; "
         f"edge_count={int(stats['min_edges'])}..{int(stats['max_edges'])}; "
         f"max_neighbor_dP={stats['max_dp_neighbor']:.3f}")
    print(msg)
    print(f"::notice title=Experiment 03 optimum refinement::{msg}")


def main():
    m06=DynamicForce(0.6,quick=False)
    m08=DynamicForce(0.8,quick=False)
    for R in (160,250,400): run(m06,0.6,20.0,R)
    for R in (400,600): run(m08,0.8,5.0,R)
    print("PASS")

if __name__=="__main__": main()
