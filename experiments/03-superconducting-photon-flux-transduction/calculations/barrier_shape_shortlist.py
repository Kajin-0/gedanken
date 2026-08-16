#!/usr/bin/env python3
"""Small live-baseline barrier-shape shortlist for rapid rescue comparison.

Uses the validated metrics() routine from barrier_shape_action_fast.py but only
checks a neighborhood of the current `(beta=.80, tilt=.05)` point.  The purpose
is to answer quickly whether static shape tuning can plausibly buy ~8 action
units, comparable to the successful electrical r~1.26 rescue, before spending
more computation on a broad scan.
"""
from __future__ import annotations
import full_dynamic_rfsquid as fd
from barrier_shape_action_fast import metrics, BASE_ACTION


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    print('Experiment 03 live barrier-shape SHORTLIST')
    try:
        for beta in (.80,.85,.90,.95,1.00):
            for tilt in (.035,.050,.065):
                fd.BETA_COLD=beta; fd.DELTA_TILT=tilt
                try:
                    q=metrics(fd.DynamicForce(.6,quick=False,Tmax=.96),nx=45001)
                    gain=q['B']-BASE_ACTION
                    msg=(f'beta={beta:.2f} tilt={tilt:.3f}: B0={q["B"]:.6f} '
                         f'DeltaB_vs_live={gain:+.6f} betaU={q["betaU"]:.4f} '
                         f'barrier={q["barrierK"]:.4f}K bias={q["biasK"]:.4f}K '
                         f'fold={q["fold"]:.4f}K fc={q["fc"]*1e-9:.3f}GHz sep={q["sep"]:.4f}')
                except Exception as e:
                    msg=f'beta={beta:.2f} tilt={tilt:.3f}: INVALID {type(e).__name__}: {e}'
                print(msg); print(f'::notice title=Experiment 03 barrier shortlist::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')
if __name__=='__main__': main()
