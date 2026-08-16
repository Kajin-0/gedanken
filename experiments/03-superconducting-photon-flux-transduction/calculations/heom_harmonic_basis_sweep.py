#!/usr/bin/env python3
"""Hilbert-basis convergence sweep for Experiment 03 harmonic HEOM Gate B.

Fixed bath/hierarchy point: N_Mats=8, hierarchy depth=3, counterterm ON.
Only the oscillator Hilbert dimension changes.  The purpose is to determine
whether the small negative eigenvalue seen in the reduced density matrix at
low Hilbert dimension is a basis-truncation artifact while monitoring the exact
FDT covariance error at the same time.
"""
from __future__ import annotations

import argparse
import heom_harmonic_port_probe as probe


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dim", type=int, choices=(8, 10, 12), required=True)
    args = ap.parse_args()
    name = f"basis{args.dim}_n8_d3"
    probe.CASES[name] = dict(dim=args.dim, nmats=8, depth=3, counterterm=True)
    probe.run_case(name)


if __name__ == "__main__":
    main()
