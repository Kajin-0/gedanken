#!/usr/bin/env python3
"""Staged time-domain HEOM probe for Experiment 03 Gate B.

The original all-in-one harmonic HEOM gate used HEOMSolver.steady_state() for
several increasingly large hierarchies.  GitHub Actions run 31973895654 spent
its full 45-minute budget inside the first steady-state solve and was cancelled
without a physical result.  This probe preserves the same direct-port bath,
counterterm and exact-FDT target, but reaches equilibrium by HEOM time evolution
and separates convergence axes into independent CI jobs.

This is a numerical-method gate, not a detector-efficiency calculation.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np

import full_dynamic_rfsquid as fd
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import PHI_BAR
from two_pole_joint_covariance import covariance_matrix
from heom_harmonic_port_validation import (
    HBAR, R, G, WD, L, C, DELTA, ALPHA, bath_expansion,
)

from qutip import destroy, qeye, fock_dm
from qutip.solver.heom import BosonicBath, HEOMSolver


CASES = {
    # Reference low-cost point.
    "base":  dict(dim=6, nmats=4, depth=2, counterterm=True),
    # Hierarchy convergence at fixed bath truncation.
    "depth": dict(dim=6, nmats=4, depth=3, counterterm=True),
    # Matsubara convergence at fixed hierarchy depth.
    "mats":  dict(dim=6, nmats=8, depth=2, counterterm=True),
    # Oscillator-basis convergence.
    "basis": dict(dim=8, nmats=4, depth=2, counterterm=True),
    # Physical control: omit the Caldeira-Leggett counterterm.
    "noct":  dict(dim=6, nmats=4, depth=2, counterterm=False),
    # Strongest staged point; if this is expensive the other jobs remain useful.
    "deep":  dict(dim=6, nmats=8, depth=3, counterterm=True),
}


def widths_from_expect(expect_rows, i: int) -> tuple[float, float]:
    x, x2, u, u2 = (float(np.real(v[i])) for v in expect_rows)
    sx = math.sqrt(max(x2 - x*x, 0.0))
    su = math.sqrt(max(u2 - u*u, 0.0))
    return sx, su


def run_case(name: str) -> None:
    cfg = CASES[name]
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    original = fd.CASES[.6]
    try:
        fd.BETA_COLD = .80
        fd.DELTA_TILT = DELTA
        fd.CASES[.6] = (L, C, original[2])
        model = fd.DynamicForce(.6, quick=False, Tmax=1.02)

        M = covariance_matrix(model, .6, R, ALPHA, y_min=-22, y_max=22)
        target_x = math.sqrt(M[0, 0])
        target_u = math.sqrt(M[1, 1])
        _xc, _kappa, wc = cold_phase_scale(model, .6)

        dim = cfg["dim"]
        nmats = cfg["nmats"]
        depth = cfg["depth"]
        with_ct = cfg["counterterm"]

        sigma0 = math.sqrt(HBAR/(2*C*PHI_BAR**2*wc))
        a = destroy(dim)
        n = a.dag()*a
        xop = sigma0*(a+a.dag())
        uop = 1j*sigma0*(a.dag()-a)
        H = n + 0.5*qeye(dim)

        ct_phys = PHI_BAR**2/HBAR * G*WD/(2*math.sqrt(2))
        ct_scaled = ct_phys/wc
        if with_ct:
            H = H + ct_scaled*(xop*xop)

        cr, vr, ci, vi = bath_expansion(wc, nmats)
        bath = BosonicBath(xop, cr, vr, ci, vi, combine=True,
                           tag="direct-port")
        nexp = len(bath.exponents)
        nado_est = math.comb(nexp + depth, depth)

        print(
            f"CASE={name} dim={dim} nmats={nmats} depth={depth} "
            f"counterterm={int(with_ct)} nexp={nexp} nado_est={nado_est}",
            flush=True,
        )
        print(
            f"wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz "
            f"target_sigma_x={target_x:.10e} target_sigma_u={target_u:.10e} "
            f"ct/wc={ct_scaled:.10e}",
            flush=True,
        )

        # Cold phase amplitude decay time is ~11.5 in these wc-scaled units.
        # t=120 therefore spans >10 amplitude-decay times.  The final two
        # samples provide an explicit residual-equilibration diagnostic.
        tlist = np.array([0., 10., 20., 40., 60., 80., 100., 120.])
        solver = HEOMSolver(
            H, bath, max_depth=depth,
            options={
                "progress_bar": "",
                "store_states": True,
                "method": "bdf",
                "rtol": 2e-7,
                "atol": 2e-9,
            },
        )
        rho0 = fock_dm(dim, 0)
        t0 = time.perf_counter()
        result = solver.run(
            rho0, tlist,
            e_ops=[xop, xop*xop, uop, uop*uop],
        )
        runtime = time.perf_counter() - t0

        sx = []
        su = []
        for i, tau in enumerate(tlist):
            sxi, sui = widths_from_expect(result.expect, i)
            sx.append(sxi)
            su.append(sui)
            print(
                f"tau={tau:7.2f} sigma_x={sxi:.10e} "
                f"relx={sxi/target_x-1:+.6e} sigma_u={sui:.10e} "
                f"relu={sui/target_u-1:+.6e}",
                flush=True,
            )

        rho = result.states[-1]
        tr = float(np.real(rho.tr()))
        eigmin = float(np.linalg.eigvalsh(rho.full()).min())
        top = float(np.real(rho.diag()[-1]))
        relx = sx[-1]/target_x - 1
        relu = su[-1]/target_u - 1
        final_err = max(abs(relx), abs(relu))
        drift = max(abs(sx[-1]-sx[-2])/target_x,
                    abs(su[-1]-su[-2])/target_u)

        msg = (
            f"CASE={name} FINAL relx={relx:+.6e} relu={relu:+.6e} "
            f"max_cov_error={final_err:.6e} late_drift={drift:.6e} "
            f"trace={tr:.12f} eigmin={eigmin:.6e} topPop={top:.6e} "
            f"runtime_s={runtime:.3f}"
        )
        print(msg, flush=True)
        print(f"::notice title=Experiment 03 harmonic HEOM probe::{msg}", flush=True)

        # Per-job guards are deliberately only gross physical/numerical guards.
        # Cross-case Gate-B tolerances are evaluated only after all matrix jobs
        # complete; lower-order probe points must remain visible even if not yet
        # quantitatively converged.
        if abs(tr - 1.0) > 5e-6:
            raise RuntimeError("HEOM time evolution trace failure")
        if eigmin < -2e-4:
            raise RuntimeError("HEOM probe has material density-matrix negativity")
        if drift > .03:
            raise RuntimeError("HEOM probe has not equilibrated by tau=120")
        print("PASS_PROBE", flush=True)
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot
        fd.CASES[.6] = original


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=sorted(CASES), required=True)
    args = ap.parse_args()
    run_case(args.case)


if __name__ == "__main__":
    main()
