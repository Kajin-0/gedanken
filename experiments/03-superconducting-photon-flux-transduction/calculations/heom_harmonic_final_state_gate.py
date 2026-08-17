#!/usr/bin/env python3
"""Final full-density-matrix gate for Experiment-03 harmonic direct-port HEOM.

This calculation is authorized only because the predeclared raw hierarchy test
continued toward positivity through N_Pade=4, depth=9.  It reruns that exact
physical/method point, captures the unmodified HEOM reduced state, and compares
it against the exact finite-dimensional squeezed thermal Gaussian equilibrium
state implied by the independently integrated FDT covariance.

Acceptance thresholds were fixed before the depth-9 result was known in
HARMONIC_HEOM_GATE_B_FINAL_ACCEPTANCE_2026-08-16.md:

    exact-reference finite-basis width error  < 1e-7
    HEOM max relative FDT width error          < 1e-6
    0.5 * nuclear norm(rho_HEOM-rho_exact)     < 5e-6
    total negative eigenvalue mass             < 5e-8

The HEOM state is never clipped, projected, or positivity-repaired.  Because a
tiny negative tail may remain, the 0.5 nuclear norm is called a
"nuclear-norm discrepancy", not a trace distance.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.linalg import svdvals

import full_dynamic_rfsquid as fd
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import PHI_BAR
from two_pole_joint_covariance import covariance_matrix
import heom_harmonic_pade_depth as base

from qutip import destroy, thermal_dm, squeeze


CASE = "p4d9_full"
CFG = dict(dim=8, npade=4, depth=9)

# Predeclared thresholds; do not relax post hoc.
REF_BASIS_MAXERR = 1.0e-7
HEOM_FDT_MAXERR = 1.0e-6
NUCLEAR_HALF_MAX = 5.0e-6
NEG_MASS_MAX = 5.0e-8

# The already-read raw depth trend.  These are provenance diagnostics, not
# adjustable tolerances.  Depth 9 must not reverse depth 8 in min-eigenvalue
# magnitude; the raw run already showed that it did not.
D8_EIGMIN = -1.504870e-8
D9_RAW_EIGMIN = -9.172453e-9


_BaseSolver = base.HEOMSolver


class CaptureSolver(_BaseSolver):
    last_result = None

    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)
        CaptureSolver.last_result = result
        return result


def moments(rho, op):
    m = complex((rho * op).tr())
    m2 = complex((rho * op * op).tr())
    var = float(np.real(m2 - m*m))
    return float(np.real(m)), math.sqrt(max(var, 0.0))


def exact_reference(dim: int):
    """Construct exact finite-basis squeezed thermal FDT reference."""
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    original = fd.CASES[.6]
    try:
        fd.BETA_COLD = .80
        fd.DELTA_TILT = base.DELTA
        fd.CASES[.6] = (base.L, base.C, original[2])
        model = fd.DynamicForce(.6, quick=False, Tmax=1.02)
        V = covariance_matrix(model, .6, base.R, base.ALPHA,
                              y_min=-22, y_max=22)
        target_x = math.sqrt(V[0, 0])
        target_u = math.sqrt(V[1, 1])
        _xc, _kap, wc = cold_phase_scale(model, .6)
        sigma0 = math.sqrt(base.HBAR/(2*base.C*PHI_BAR**2*wc))

        # In the present equilibrium convention <{x,u}>/2 = 0.  The symplectic
        # ratio fixes nbar and the variance ratio fixes the real squeeze r.
        nu = target_x*target_u/(sigma0*sigma0)
        nbar = 0.5*(nu - 1.0)
        r = 0.5*math.log(target_u/target_x)

        a = destroy(dim)
        xop = sigma0*(a + a.dag())
        uop = 1j*sigma0*(a.dag() - a)
        S = squeeze(dim, r)
        rho_th = thermal_dm(dim, nbar)
        rho_exact = S * rho_th * S.dag()

        _mx, sx = moments(rho_exact, xop)
        _mu, su = moments(rho_exact, uop)
        basis_err = max(abs(sx/target_x - 1.0),
                        abs(su/target_u - 1.0))
        return dict(
            rho=rho_exact, xop=xop, uop=uop,
            target_x=target_x, target_u=target_u,
            sigma0=sigma0, nbar=nbar, r=r,
            sx=sx, su=su, basis_err=basis_err,
        )
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot
        fd.CASES[.6] = original


def main():
    base.CASES[CASE] = CFG
    base.HEOMSolver = CaptureSolver
    base.run_case(CASE)
    if CaptureSolver.last_result is None:
        raise RuntimeError("failed to capture HEOM result")

    rho_h = CaptureSolver.last_result.states[-1]
    ref = exact_reference(CFG["dim"])
    rho_e = ref["rho"]

    _mxh, sxh = moments(rho_h, ref["xop"])
    _muh, suh = moments(rho_h, ref["uop"])
    heom_fdt_err = max(abs(sxh/ref["target_x"] - 1.0),
                       abs(suh/ref["target_u"] - 1.0))

    ah = np.asarray(rho_h.full(), dtype=complex)
    ae = np.asarray(rho_e.full(), dtype=complex)
    antiherm = np.linalg.norm(ah-ah.conj().T, ord="fro") / max(
        np.linalg.norm(ah, ord="fro"), 1e-300)
    tr_h = complex(np.trace(ah))
    tr_e = complex(np.trace(ae))

    # Diagnostics are computed on the raw HEOM matrix.  eigvalsh is appropriate
    # after separately verifying Hermiticity to high precision; no projection is
    # applied to the state used in the norm comparison.
    eig_h = np.linalg.eigvalsh(ah)
    eig_e = np.linalg.eigvalsh(ae)
    neg_mass = float(np.sum(np.maximum(-eig_h, 0.0)))
    eigmin = float(eig_h.min())
    delta = ah-ae
    nuclear_half = 0.5*float(np.sum(svdvals(delta)))
    frob = float(np.linalg.norm(delta, ord="fro"))

    # Basis-independent sorted spectrum comparison is supplemental to the full
    # matrix norm because eigenvectors/squeezing matter too.
    sh = np.sort(eig_h)[::-1]
    se = np.sort(eig_e)[::-1]
    spectral_l1 = float(np.sum(np.abs(sh-se)))

    print("EXACT FINITE-BASIS REFERENCE")
    print(f"sigma0={ref['sigma0']:.12e} nbar={ref['nbar']:.12e} "
          f"r={ref['r']:.12e}")
    print(f"sigma_x={ref['sx']:.12e} target_x={ref['target_x']:.12e} "
          f"relx={ref['sx']/ref['target_x']-1:+.12e}")
    print(f"sigma_u={ref['su']:.12e} target_u={ref['target_u']:.12e} "
          f"relu={ref['su']/ref['target_u']-1:+.12e}")
    print(f"basis_max_width_error={ref['basis_err']:.12e}")

    print("RAW HEOM FULL-STATE COMPARISON")
    print(f"sigma_x={sxh:.12e} relx={sxh/ref['target_x']-1:+.12e}")
    print(f"sigma_u={suh:.12e} relu={suh/ref['target_u']-1:+.12e}")
    print(f"heom_max_FDT_width_error={heom_fdt_err:.12e}")
    print(f"trace_HEOM=({tr_h.real:.12e}{tr_h.imag:+.12e}j) "
          f"trace_exact=({tr_e.real:.12e}{tr_e.imag:+.12e}j)")
    print(f"antihermitian_relative_frobenius={antiherm:.12e}")
    print(f"eigmin_HEOM={eigmin:.12e} negative_mass={neg_mass:.12e}")
    print(f"nuclear_norm_discrepancy_half={nuclear_half:.12e} "
          f"frobenius_error={frob:.12e} spectral_L1={spectral_l1:.12e}")
    print(f"depth_trend d8_eigmin={D8_EIGMIN:.12e} "
          f"d9_raw_eigmin={D9_RAW_EIGMIN:.12e}")

    print("rank exact_eig heom_eig abs_error")
    for i,(ee,eh) in enumerate(zip(se,sh)):
        print(f"{i:2d} {ee:.12e} {eh:+.12e} {abs(eh-ee):.12e}")

    passes = {
        "reference_basis": ref["basis_err"] < REF_BASIS_MAXERR,
        "heom_fdt": heom_fdt_err < HEOM_FDT_MAXERR,
        "nuclear_half": nuclear_half < NUCLEAR_HALF_MAX,
        "negative_mass": neg_mass < NEG_MASS_MAX,
        "depth9_no_reversal": D9_RAW_EIGMIN >= D8_EIGMIN,
        "trace": abs(tr_h-1.0) < 5e-7,
        "hermiticity": antiherm < 1e-8,
    }
    for key,val in passes.items():
        print(f"GATE {key}={'PASS' if val else 'FAIL'}")

    msg=(f"FINAL_GATE basis_err={ref['basis_err']:.6e} "
         f"heom_fdt_err={heom_fdt_err:.6e} "
         f"nuclear_half={nuclear_half:.6e} neg_mass={neg_mass:.6e} "
         f"eigmin={eigmin:.6e} antiherm={antiherm:.3e} "
         f"all_pass={all(passes.values())}")
    print(msg)
    print(f"::notice title=Experiment 03 harmonic HEOM Gate B full state::{msg}")

    if not all(passes.values()):
        failed=[k for k,v in passes.items() if not v]
        raise RuntimeError("Gate B full-state acceptance failed: " + ", ".join(failed))
    print("PASS_GATE_B_HARMONIC")


if __name__ == "__main__":
    main()
