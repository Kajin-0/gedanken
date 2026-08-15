#!/usr/bin/env python3
"""Robust cold-bistable / hot-fold window for Experiment 03.

For a CPR uncertainty set, let B0_max be the largest cold normalized fold
threshold.  Guaranteed cold bistability requires

    beta_cold > B0_max.

At the hot state, if the critical-current amplitude has fallen by a factor

g = Ic_hot / Ic_cold

and the hot CPR uncertainty set has minimum normalized fold Bhot_min, guaranteed
loss of the metastable well requires

    beta_cold * g < Bhot_min.

Therefore a nonempty robust write window exists if

    B0_max < beta_cold < Bhot_min/g,

or equivalently

    g < Bhot_min/B0_max.

This script uses the three-harmonic equal-skewness envelope from
cpr_skewness_envelope.py to quantify how interface/CPR uncertainty shifts the
preferred beta.  It also reports cold-barrier and provisional MQT-capacitance
envelopes at selected beta.
"""

from __future__ import annotations

import numpy as np

from cpr_skewness_envelope import envelope


def fold_bounds(S):
    rows = envelope(S, beta_cold=1.0)
    folds = np.asarray([r["beta_fold"] for r in rows])
    return float(folds.min()), float(folds.max()), len(rows)


def cold_metrics_bounds(S, beta):
    rows = envelope(S, beta_cold=beta)
    stable = [r for r in rows if r["cold"] is not None]
    if not stable:
        return None
    barrier = np.asarray([r["cold"]["barrier_K"] for r in stable])
    cmin = np.asarray([r["cold"]["Cmin_F"] for r in stable])
    dphi = np.asarray([r["cold"]["delta_flux_phi0"] for r in stable])
    return {
        "nstable": len(stable),
        "ntotal": len(rows),
        "barrier_min": float(barrier.min()),
        "barrier_max": float(barrier.max()),
        "cmin_min": float(cmin.min()),
        "cmin_max": float(cmin.max()),
        "dphi_min": float(dphi.min()),
        "dphi_max": float(dphi.max()),
    }


def robust_window(Bcold_max, Bhot_min, g):
    lo = Bcold_max
    hi = Bhot_min / g
    return lo, hi, hi > lo


def main():
    print("Experiment 03 robust CPR write-window checkpoint")
    print("delta=0.05; equal-skewness 3-harmonic cold/hot envelopes")

    for S in (0.10, 0.15, 0.23, 0.27):
        bmin, bmax, n = fold_bounds(S)
        print(f"S={S:.2f}: beta_fold in [{bmin:.4f}, {bmax:.4f}] from {n} CPRs")

    print("\nCold robustness at selected beta:")
    for S in (0.15, 0.27):
        for beta in (0.8, 0.9, 1.0, 1.1, 1.2):
            m = cold_metrics_bounds(S, beta)
            if m is None:
                print(f"S={S:.2f}, beta={beta:.2f}: no accepted CPR is bistable")
                continue
            print(
                f"S={S:.2f}, beta={beta:.2f}: stable {m['nstable']}/{m['ntotal']}; "
                f"barrier=[{m['barrier_min']:.3g},{m['barrier_max']:.3g}] K; "
                f"Cmin_Q=[{m['cmin_min']*1e15:.3g},{m['cmin_max']*1e15:.3g}] fF"
            )

    # Experimentally reported high-T CPR is approximately sinusoidal by 4.2 K.
    Bhot_sine = 1.1471219433332678  # exact sinusoidal delta=0.05 fold

    print("\nRobust write window if the hot CPR is approximately sinusoidal:")
    for Scold in (0.15, 0.23, 0.27):
        _, Bcold_max, _ = fold_bounds(Scold)
        gcrit = Bhot_sine / Bcold_max
        print(
            f"cold S={Scold:.2f}: Bcold,max={Bcold_max:.4f}; "
            f"nonempty if g < {gcrit:.4f}"
        )
        for g in (1.0, 0.95, 0.90, 0.70):
            lo, hi, ok = robust_window(Bcold_max, Bhot_sine, g)
            print(
                f"  g={g:.2f}: beta in ({lo:.4f}, {hi:.4f}) "
                f"{'OPEN' if ok else 'CLOSED'}"
            )

    print("\nExample beta_cold=1.20 with sinusoidal hot CPR:")
    g_needed = Bhot_sine / 1.20
    print(f"hot amplitude must satisfy g < {g_needed:.5f}")
    print(f"equivalent Ic suppression > {(1-g_needed)*100:.3f} %")

    print("\nImportant limitation:")
    print("Skewness alone does not define the hot uncertainty set either.  If the")
    print("trigger occurs before the CPR has become genuinely sinusoidal, Bhot_min")
    print("must be obtained from measured/microscopic tail slopes at that temperature.")


if __name__ == "__main__":
    main()
