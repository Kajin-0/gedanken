#!/usr/bin/env python3
"""Focused rDelta=0.6 initial-state probability damping scout."""
from full_dynamic_rfsquid import DynamicForce
from quantum_basin_integral import integrated_probability

m=DynamicForce(0.6,quick=False)
rows=[]
for R in (90,120,160,250,400,700,1000):
    p,cov,details=integrated_probability(m,0.6,float(R),20.0,order_x=5,zmax=5.0,nscan=49)
    rows.append((R,p,max(d[2] for d in details)))
    msg=f"rDelta=0.6, rise=20 ps, R={R} ohm; P_R_scout={p:.6f}; max_edges={rows[-1][2]}"
    print(msg)
    print(f"::notice title=Experiment 03 rDelta 0.6 probability scan::{msg}")
b=max(rows,key=lambda r:r[1])
print(f"BEST R={b[0]} P={b[1]:.6f}")
print("PASS")
