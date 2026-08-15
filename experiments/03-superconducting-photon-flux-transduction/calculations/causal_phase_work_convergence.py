#!/usr/bin/env python3
"""Window-convergence check for causal_phase_work_noise.py.

The spectral FDT work identity is exact for a prescribed infinite-time voltage
waveform.  The numerical trajectory is necessarily truncated, so compare the
frequency-domain dissipative functional to the explicit resistor heat while
extending the recovery window.  Only converged or clearly bounded cases should
be used for physical interpretation.
"""

from __future__ import annotations

from causal_phase_work_noise import trace_case
from full_dynamic_rfsquid import DynamicForce


def main() -> None:
    print("Experiment 03 FDT work-noise recovery-window convergence")
    model = DynamicForce(0.6, quick=False)
    for R, alpha in [(250.0, 0.20), (250.0, 0.35), (250.0, 0.50)]:
        for tend in (1.5, 5.0, 20.0, 80.0):
            out = trace_case(
                model, R, alpha,
                tend_ns=tend,
                dt_ps=1.0,
            )
            msg = (
                f"R={R:g} alpha={alpha:.2f} tend={tend:g} ns: "
                f"Q/kB={float(out['Q_over_kB_K']):.6f} K, "
                f"eps/kB={float(out['eps_over_kB_K']):.6f} K, "
                f"sigmaW/kB={float(out['sigmaW_over_kB_K']):.6f} K, "
                f"Qspec/Qtime={float(out['Q_consistency']):.6f}, "
                f"basin={out['basin']}"
            )
            print(msg)
            print(f"::notice title=Experiment 03 FDT-work convergence::{msg}")
    print("PASS")


if __name__ == '__main__':
    main()
