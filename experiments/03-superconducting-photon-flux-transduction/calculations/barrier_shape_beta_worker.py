#!/usr/bin/env python3
"""Parallel worker for the live barrier-shape rescue scan."""
from __future__ import annotations
import argparse
import full_dynamic_rfsquid as fd
from barrier_shape_action_fast import metrics, BASE_ACTION


def main():
    p=argparse.ArgumentParser(); p.add_argument('--beta',type=float,required=True); a=p.parse_args()
    beta=float(a.beta); ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        for tilt in (.035,.050,.065):
            fd.BETA_COLD=beta; fd.DELTA_TILT=tilt
            try:
                q=metrics(fd.DynamicForce(.6,quick=False,Tmax=.96),nx=45001)
                msg=(f'beta={beta:.2f} tilt={tilt:.3f}: B0={q["B"]:.6f} '
                     f'DeltaB={q["B"]-BASE_ACTION:+.6f} betaU={q["betaU"]:.4f} '
                     f'barrier={q["barrierK"]:.4f}K bias={q["biasK"]:.4f}K '
                     f'fold={q["fold"]:.4f}K fc={q["fc"]*1e-9:.3f}GHz sep={q["sep"]:.4f}')
                if abs(beta-.8)<1e-12 and abs(tilt-.05)<1e-12:
                    rel=q['B']/BASE_ACTION-1
                    msg += f' baseline_relerr={rel:+.3e}'
                    if abs(rel)>.003: raise RuntimeError('baseline action regression failed')
            except Exception as e:
                msg=f'beta={beta:.2f} tilt={tilt:.3f}: INVALID {type(e).__name__}: {e}'
            print(msg); print(f'::notice title=Experiment 03 barrier beta worker::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')
if __name__=='__main__': main()
