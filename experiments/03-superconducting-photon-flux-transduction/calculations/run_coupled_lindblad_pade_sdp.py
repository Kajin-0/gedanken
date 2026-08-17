#!/usr/bin/env python3
"""Launch the coupled-Lindblad Padé SDP probe with numerical PSD enforcement.

Three launch-only compatibility steps are applied without changing the published
SDP objective or physical bath parameters:

1. bind the canonical HBAR symbol used only by the detailed-balance diagnostic;
2. enforce the already requested PSD floors after conic-solver tolerance by a
   minimal positive identity shift;
3. put the exact bath correlation/spectrum into the *same dimensionless
   coupling convention* as the FP-HEOM Padé coefficients before comparing the
   physical coupled BCF to the exact bath.

The third item corrects reporting only.  `heom_fp_harmonic_oracle.harmonic_setup`
returns coefficients

    d_k = c_k (Phi_bar/hbar)^2 / omega_c^2,

so the exact comparison in tau=omega_c t units is

    C_exact,dim(tau) = C_exact(tau/omega_c)
                       (Phi_bar/hbar)^2 / omega_c^2,

and its dimensionless-frequency spectrum is

    S_exact,dim(x) = S_exact(omega_c x)
                     (Phi_bar/hbar)^2 / omega_c.

Earlier probe output compared these dimensionless quantities to C/(S0 omega_c)
and S/S0, creating a spurious ~56x normalization discrepancy even while the
coupled BCF differed from the Padé BCF by only ~1e-3.  The SDP itself was
unchanged.
"""
import numpy as np

from direct_port_bath_correlation import HBAR, BETA, G, corr_series
from quantum_initial_capture import PHI_BAR
import coupled_lindblad_pade_sdp as probe

probe.fp.HBAR = HBAR
_original_solve = probe.solve_sdp
_physical_exact_s_over_S0 = probe.exact_dimless


def solve_sdp_with_psd_floor(Lam, l, r):
    Y, status, obj, residual, rel, solver = _original_solve(Lam, l, r)
    Y = 0.5 * (Y + Y.conj().T)
    Q = 1j * (Y @ Lam - Lam.conj().T @ Y)
    Q = 0.5 * (Q + Q.conj().T)
    QI = 1j * (Lam - Lam.conj().T)
    QI = 0.5 * (QI + QI.conj().T)

    ymin = float(np.linalg.eigvalsh(Y).min())
    qmin = float(np.linalg.eigvalsh(Q).min())
    qimin = float(np.linalg.eigvalsh(QI).min())
    if qimin <= 0:
        raise RuntimeError(f"identity shift is not PSD-monotone: min Q(I)={qimin}")

    y_floor = 1.0e-9
    q_floor = 1.0e-12
    delta = max(0.0, y_floor - ymin, (q_floor - qmin) / qimin)
    if delta > 0:
        delta += 1.0e-12
        Y = Y + delta * np.eye(len(r))

    Q2 = 1j * (Y @ Lam - Lam.conj().T @ Y)
    Q2 = 0.5 * (Q2 + Q2.conj().T)
    ymin2 = float(np.linalg.eigvalsh(Y).min())
    qmin2 = float(np.linalg.eigvalsh(Q2).min())
    residual2 = float(np.linalg.norm(l - Y @ r))
    rel2 = residual2 / max(float(np.linalg.norm(l)), 1e-300)
    obj2 = residual2 * residual2

    print(
        f"PSD_ENFORCEMENT solver={solver} raw_Ymin={ymin:+.12e} "
        f"raw_Qmin={qmin:+.12e} QImin={qimin:+.12e} delta={delta:.12e} "
        f"final_Ymin={ymin2:+.12e} final_Qmin={qmin2:+.12e} "
        f"residual_before={residual:.12e} residual_after={residual2:.12e}",
        flush=True,
    )
    if ymin2 < 0.99 * y_floor or qmin2 < -1e-13:
        raise RuntimeError("post-shift SDP constraints remain numerically violated")
    return Y, status + "+PSD_SHIFT", obj2, residual2, rel2, solver


def exact_corr_same_convention(tau, wc):
    cscale = (PHI_BAR / HBAR) ** 2 / (wc * wc)
    return corr_series(float(tau) / wc, 10000) * cscale


def exact_s_same_convention(x):
    # omega_c is fixed by the physical harmonic operating point and does not
    # depend on Padé order.  Obtain it once from the same harmonic setup.
    wc = probe.fp.harmonic_setup(2, 4)[0]
    cscale = (PHI_BAR / HBAR) ** 2 / (wc * wc)
    S0 = 2 * G / BETA
    return _physical_exact_s_over_S0(x) * (S0 * cscale * wc)


probe.solve_sdp = solve_sdp_with_psd_floor
probe.exact_corr_norm = exact_corr_same_convention
probe.exact_dimless = exact_s_same_convention

if __name__ == "__main__":
    probe.main()
