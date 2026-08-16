#!/usr/bin/env python3
"""Persist exact deterministic resistor-dissipation partition for candidate points."""
from __future__ import annotations
import math
from pathlib import Path
from full_dynamic_rfsquid import DynamicForce
from candidate_dissipation_partition import trajectory, first_cross, integrate_q
from causal_energetic_lock import trace_lock

OUT=Path('../RESULTS_DISSIPATION_PARTITION_2026-08-15.md')
MEV=1.602176634e-22

def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    lines=['# Experiment 03 — Deterministic Dissipation Partition — 2026-08-15','',
           'Exact resistor loss of the passive two-pole environment, partitioned by write stage.','',
           '```text']
    for R,alpha in [(150.,.70),(150.,.80),(100.,.80),(80.,.70),(80.,.90),(80.,1.0),(40.,.90),(30.,1.0),(20.,.90),(20.,1.0)]:
        sol,wc=trajectory(model,R,alpha)
        tc=first_cross(sol,.5e-9)
        lock=trace_lock(model,R,alpha,lambda_um=8.,rise_ps=20.,tend_ns=.5)
        trf=lock['t_reform'];tl=lock['t_lock'];tf=.5e-9
        q=[integrate_q(sol,R,a,b) for a,b in [(0,tc),(tc,trf),(trf,tl),(tl,tf)]]
        qt=sum(v for v in q if math.isfinite(v))
        frac=[v/qt for v in q]
        lines.append(f'R={R:g} ohm; alpha={alpha:.2f}; tcross={tc*1e12:.4f} ps; '
                     f'treform={trf*1e12:.4f} ps; tlock={tl*1e12:.4f} ps; '
                     f'Qpre={q[0]/MEV:.8f} meV; Qcross_reform={q[1]/MEV:.8f} meV; '
                     f'Qreform_lock={q[2]/MEV:.8f} meV; Qpost_lock={q[3]/MEV:.8f} meV; '
                     f'Qtotal={qt/MEV:.8f} meV; '
                     f'fractions=[{frac[0]:.6f},{frac[1]:.6f},{frac[2]:.6f},{frac[3]:.6f}]')
    lines += ['```','',
              'This is deterministic energy accounting, not a stochastic capture probability.']
    OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'wrote {OUT}')
if __name__=='__main__':main()
