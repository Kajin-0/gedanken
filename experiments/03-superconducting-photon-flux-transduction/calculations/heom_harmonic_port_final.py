#!/usr/bin/env python3
"""Final combined convergence point for Experiment 03 harmonic HEOM Gate B.

This intentionally reuses the staged time-domain probe implementation while
raising oscillator basis, Matsubara count and hierarchy depth simultaneously.
It exists separately so the completed staged matrix is not needlessly rerun.
"""
import heom_harmonic_port_probe as probe

probe.CASES["final"] = dict(dim=8, nmats=8, depth=3, counterterm=True)

if __name__ == "__main__":
    probe.run_case("final")
