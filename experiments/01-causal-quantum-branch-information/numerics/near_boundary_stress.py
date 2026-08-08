"""Near-boundary stress harness for independent Gaussian-channel simulations.

The analytic coherent theorem predicts NPT iff

    delta := tau - m > 0.

This script approaches delta=0 from both sides using the committed independent
implementations for

1. unit-gain additive Gaussian noise;
2. thermal amplification.

The purpose is not to decide the theorem numerically.  It is to expose when the
finite Fock/quadrature approximation stops resolving the analytic witness gap.
A correct audit should show stable negative PT eigenvalues on the non-EB side
until numerical resolution is exhausted, and resolution-dependent residuals
approaching zero on the EB side.
"""

from __future__ import annotations

import argparse

import numpy as np

from additive_noise_cat_scan import cat_pt_spectrum as additive_pt_spectrum
from amplifier_cat_scan import (
    cat_pt_spectrum as amplifier_pt_spectrum,
    two_mode_squeezer_unitary,
)


def summarize(eigvals: np.ndarray) -> tuple[float, float]:
    return float(eigvals[0]), float(-eigvals[eigvals < 0.0].sum())


def additive_scan(
    epsilons: list[float],
    amplitude: float,
    dims: list[int],
    orders: list[int],
) -> None:
    print("\n=== additive Gaussian noise: tau=1, m=1-delta ===")
    for sign in (+1.0, -1.0):
        side = "non-EB" if sign > 0 else "EB"
        print(f"\n-- {side} side --")
        for eps in epsilons:
            delta = sign * eps
            noise = 1.0 - delta
            print(f"delta=tau-m={delta:+.3e}; m={noise:.12g}")
            for dim in dims:
                for order in orders:
                    eigvals, trace = additive_pt_spectrum(
                        noise=noise,
                        amplitude=amplitude,
                        dim=dim,
                        order=order,
                    )
                    lam_min, neg = summarize(eigvals)
                    print(
                        f"  N={dim:3d}  order={order:3d}  "
                        f"lambda_min={lam_min:+.8e}  "
                        f"neg={neg:.8e}  trace={trace:.12f}"
                    )


def amplifier_scan(
    gain: float,
    epsilons: list[float],
    amplitude: float,
    cutoffs: list[int],
) -> None:
    if gain <= 1.0:
        raise ValueError("gain must be > 1 for the thermal-amplifier stress test")

    print(
        "\n=== thermal amplifier: tau=G, "
        "n_env=(1-delta)/(G-1), so m=G-delta ==="
    )

    for sign in (+1.0, -1.0):
        side = "non-EB" if sign > 0 else "EB"
        print(f"\n-- {side} side --")
        for eps in epsilons:
            delta = sign * eps
            n_env = (1.0 - delta) / (gain - 1.0)
            if n_env < 0.0:
                continue

            print(
                f"delta=tau-m={delta:+.3e}; "
                f"G={gain:.8g}; n_env={n_env:.12g}"
            )
            for dim in cutoffs:
                unitary = two_mode_squeezer_unitary(gain, dim)
                eigvals, trace, env_tail = amplifier_pt_spectrum(
                    gain=gain,
                    n_env=n_env,
                    amplitude=amplitude,
                    dim=dim,
                    unitary=unitary,
                )
                lam_min, neg = summarize(eigvals)
                print(
                    f"  N={dim:3d}  lambda_min={lam_min:+.8e}  "
                    f"neg={neg:.8e}  trace={trace:.12f}  "
                    f"env_tail={env_tail:.3e}"
                )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--channel",
        choices=("additive", "amplifier", "both"),
        default="additive",
        help="Amplifier scans are substantially more expensive.",
    )
    parser.add_argument(
        "--eps",
        type=float,
        nargs="+",
        default=[1e-1, 1e-2, 1e-3, 1e-4],
        help="Absolute offsets |tau-m| from the EB boundary.",
    )
    parser.add_argument("--amplitude", type=float, default=0.35)
    parser.add_argument(
        "--additive-dims",
        type=int,
        nargs="+",
        default=[16, 18, 20],
        help="Fock cutoffs for additive-noise convergence.",
    )
    parser.add_argument("--orders", type=int, nargs="+", default=[16, 20, 24])
    parser.add_argument("--gain", type=float, default=1.5)
    parser.add_argument("--cutoffs", type=int, nargs="+", default=[10, 12, 14, 16])
    args = parser.parse_args()

    epsilons = sorted({abs(x) for x in args.eps if x > 0.0}, reverse=True)

    if args.channel in ("additive", "both"):
        additive_scan(
            epsilons,
            amplitude=args.amplitude,
            dims=args.additive_dims,
            orders=args.orders,
        )

    if args.channel in ("amplifier", "both"):
        amplifier_scan(
            gain=args.gain,
            epsilons=epsilons,
            amplitude=args.amplitude,
            cutoffs=args.cutoffs,
        )


if __name__ == "__main__":
    main()
