#!/usr/bin/env python3
"""Coarse probability-optimal scalar-R scan for Experiment 03.

Uses geometry-aware conditional velocity integration with modest x quadrature to
locate candidate maxima of initial-state target-basin probability. This is a
scouting calculation, not the final convergence result.
"""

from __future__ import annotations

from full_dynamic_rfsquid import DynamicForce
from quantum_basin_integral import integrated_probability


def scan_family(model, r_delta, rise_ps, Rs):
    rows=[]
    for R in Rs:
        p,cov,details=integrated_probability(
            model,r_delta,float(R),rise_ps,
            order_x=5,zmax=5.0,nscan=49,
        )
        max_edges=max(d[2] for d in details)
        rows.append((R,p,max_edges))
        msg=(f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps, R={R:g} ohm; "
             f"P_R_scout={p:.6f}; max_edges_at_xnodes={max_edges}")
        print(msg)
        print(f"::notice title=Experiment 03 probability R scan::{msg}")
    best=max(rows,key=lambda r:r[1])
    print(f"BEST rDelta={r_delta:.1f}: R={best[0]:g} ohm, P_R_scout={best[1]:.6f}")
    return rows


def main():
    print("Experiment 03 probability-optimal scalar-R scouting scan")
    m08=DynamicForce(0.8,quick=False)
    m06=DynamicForce(0.6,quick=False)
    scan_family(m08,0.8,5.0,[170,185,220,260,300,400,600,900])
    scan_family(m06,0.6,20.0,[66,75,90,120,160,250,400,700,1000])
    print("PASS")

if __name__=="__main__":
    main()
