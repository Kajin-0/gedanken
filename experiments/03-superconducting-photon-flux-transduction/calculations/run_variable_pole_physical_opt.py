#!/usr/bin/env python3
"""Launch the frozen variable-pole optimization with exact-C0 initializer normalization.

The deterministic normalization is specified in
`VARIABLE_POLE_INITIALIZER_CLARIFICATION_2026-08-17.md`, committed before any
variable-pole optimization result.
"""
from __future__ import annotations

import math
import numpy as np

import variable_pole_physical_opt as opt

_original_baseline = opt.baseline_physical


def baseline_physical_exact_c0(rank, samples):
    model, sdp, phys = _original_baseline(rank, samples)
    c0 = float(np.real(samples[0]))
    old = float(np.real(np.vdot(phys['g'], phys['g'])))
    if c0 <= 0 or old <= 0:
        raise RuntimeError(f'invalid C0 normalization c0={c0} old={old}')
    scale = math.sqrt(c0 / old)
    out = dict(phys)
    out['g'] = np.asarray(phys['g'], complex) * scale
    new = float(np.real(np.vdot(out['g'], out['g'])))
    rel = abs(new-c0)/c0
    print(f'VARIABLE_C0_NORMALIZE rank={rank} oldC0={old:.12e} exactC0={c0:.12e} '
          f'scale={scale:.12e} newC0={new:.12e} rel={rel:.12e}', flush=True)
    if rel > 2e-15:
        raise RuntimeError('exact-C0 initializer normalization failed')
    return model, sdp, out


opt.baseline_physical = baseline_physical_exact_c0

if __name__ == '__main__':
    opt.main()
