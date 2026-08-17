#!/usr/bin/env python3
"""Predeclared high-order coupled-Lindblad bath audit for Experiment 03.

Acceptance criteria were frozen in
`COUPLED_LINDBLAD_HIGH_ORDER_ACCEPTANCE_2026-08-17.md` before this calculation.

This script applies exactly the same published Huang et al. SDP, deterministic
post-solver PSD enforcement, and direct-port normalization as
`run_coupled_lindblad_pade_sdp.py`, then evaluates p8/p12/p16 on the additional
system-band metrics required by the frozen rule.

Bath-level test only: no system dynamics and no nonlinear detector claim.
"""
from __future__ import annotations

import math
import numpy as np

# Importing the wrapper applies the canonical HBAR binding, PSD enforcement,
# and corrected exact-bath normalization to the underlying probe module.
import run_coupled_lindblad_pade_sdp as runner

p = runner.probe

TAUS = np.array([0.0, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0,
                 8.0, 12.0, 16.0, 20.0, 24.0])
DB_X = np.array([0.5, 1.0, 1.13, 1.5, 2.0])


def build_order(N: int):
    wc, _x, _u, _H, d, z, _ref = p.fp.harmonic_setup(2, N)
    Lam = np.diag(-1j * z)
    l, r = p.balanced_lr(d)
    Y, status, obj, residual, relsdp, solver = p.solve_sdp(Lam, l, r)
    K, g, H, Gamma, ey = p.reconstruct(Lam, r, Y)
    eg = np.linalg.eigvalsh(Gamma)

    # Time-domain exact-correlation audit on the frozen grid.
    relc = []
    absc = []
    for tau in TAUS:
        cv = p.cc(float(tau), K, g)
        ex = p.exact_corr_norm(float(tau), wc)
        relc.append(abs(cv - ex) / max(abs(ex), 1e-14))
        absc.append(abs(cv - ex))
    c0 = p.cc(0.0, K, g)
    c0ex = p.exact_corr_norm(0.0, wc)
    c0rel = abs(c0 - c0ex) / abs(c0ex)

    # Detailed balance in the system-frequency band.
    db = {}
    for x in DB_X:
        sp = p.sexp(float(x), K, g)
        sm = p.sexp(float(-x), K, g)
        ratio = sm / sp if sp > 0.0 and sm > 0.0 else 0.0
        exact_ratio = math.exp(-runner.BETA * runner.HBAR * wc * float(x))
        err = (abs(math.log(ratio) - math.log(exact_ratio))
               if ratio > 0.0 else math.inf)
        db[float(x)] = (ratio, exact_ratio, err)

    # Spectrum metrics requested by the frozen acceptance rule.
    xcore = np.linspace(-4.0, 6.0, 4001)
    sc = np.array([p.sexp(float(x), K, g) for x in xcore])
    se = np.asarray(p.exact_dimless(xcore), float)
    s0 = float(np.asarray(p.exact_dimless(np.array([0.0])), float)[0])
    err = sc - se
    spec_maxabs_s0 = float(np.max(np.abs(err)) / s0)
    spec_rms_s0 = float(np.sqrt(np.mean(err * err)) / s0)
    mask = se >= 1.0e-3 * s0
    spec_maxrel_1e3 = float(np.max(np.abs(err[mask]) / se[mask]))

    # Wide positivity scan.  This is a numerical scan in addition to the
    # analytic Gamma >= 0 generator condition.
    wings = np.concatenate([
        -np.geomspace(1.0e4, 4.001, 1800),
        xcore,
        np.geomspace(6.001, 1.0e4, 1800),
    ])
    sw = np.array([p.sexp(float(x), K, g) for x in wings])
    minsw = float(sw.min())
    xmin = float(wings[np.argmin(sw)])

    out = {
        "N": N,
        "nmode": len(d),
        "solver": solver,
        "status": status,
        "relSDP": float(relsdp),
        "Ymin": float(ey.min()),
        "Ymax": float(ey.max()),
        "condY": float(ey.max() / ey.min()),
        "GammaMin": float(eg.min()),
        "GammaMax": float(eg.max()),
        "minSwide": minsw,
        "xminS": xmin,
        "maxrelC": float(max(relc)),
        "maxabsC": float(max(absc)),
        "C0rel": float(c0rel),
        "specMaxAbsS0": spec_maxabs_s0,
        "specRmsS0": spec_rms_s0,
        "specMaxRel1e3": spec_maxrel_1e3,
        "db": db,
    }

    print(
        f"HIGH_ORDER p{N} n={len(d)} status={status} relSDP={out['relSDP']:.12e} "
        f"Ymin={out['Ymin']:+.12e} condY={out['condY']:.6e} "
        f"GammaMin={out['GammaMin']:+.12e} minSwide={out['minSwide']:+.12e} "
        f"xminS={out['xminS']:+.6e} maxrelC={out['maxrelC']:.12e} "
        f"C0rel={out['C0rel']:.12e} specMaxAbsS0={out['specMaxAbsS0']:.12e} "
        f"specRmsS0={out['specRmsS0']:.12e} specMaxRel1e3={out['specMaxRel1e3']:.12e}",
        flush=True,
    )
    for x in DB_X:
        ratio, rex, e = db[float(x)]
        print(
            f"HIGH_ORDER_DB p{N} x={x:.2f} ratio={ratio:.12e} "
            f"exact={rex:.12e} logerr={e:.12e}", flush=True
        )
    return out


def strictly_decreasing(rows, key):
    vals = [r[key] for r in rows]
    return all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))


def db_decreasing(rows, x):
    vals = [r['db'][float(x)][2] for r in rows]
    return all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))


def main():
    rows = [build_order(N) for N in (8, 12, 16)]
    p8, p12, p16 = rows

    physical = all(
        r['Ymin'] > 0.0 and
        r['GammaMin'] >= -1.0e-12 and
        r['minSwide'] >= -1.0e-10 and
        r['condY'] < 10.0 * p8['condY']
        for r in rows[1:]
    )
    monotone_core = (
        strictly_decreasing(rows, 'relSDP') and
        strictly_decreasing(rows, 'maxrelC') and
        strictly_decreasing(rows, 'specMaxAbsS0') and
        strictly_decreasing(rows, 'specRmsS0') and
        strictly_decreasing(rows, 'specMaxRel1e3') and
        db_decreasing(rows, 1.0) and
        db_decreasing(rows, 1.13) and
        db_decreasing(rows, 2.0)
    )
    p16_targets = (
        p16['maxrelC'] < 1.0e-3 and
        p16['C0rel'] < 1.0e-3 and
        p16['db'][1.0][2] < 2.0e-2 and
        p16['db'][1.13][2] < 3.0e-2
    )
    passed = physical and monotone_core and p16_targets

    print(
        f"HIGH_ORDER_ACCEPTANCE physical={int(physical)} monotone={int(monotone_core)} "
        f"p16targets={int(p16_targets)} pass={int(passed)}",
        flush=True,
    )
    print(
        "COUPLED_LINDBLAD_HIGH_ORDER_PASS"
        if passed else "COUPLED_LINDBLAD_HIGH_ORDER_FAIL",
        flush=True,
    )


if __name__ == '__main__':
    main()
