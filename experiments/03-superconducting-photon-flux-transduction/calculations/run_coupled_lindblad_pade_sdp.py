#!/usr/bin/env python3
"""Launch the coupled-Lindblad Padé SDP probe with numerical PSD enforcement.

Two launch-only compatibility steps are applied without changing the published
SDP objective or physical bath parameters:

1. bind the canonical HBAR symbol used only by the detailed-balance diagnostic;
2. after the conic solver returns, enforce the *already requested* strict PSD
   floors by a minimal positive identity shift if solver tolerance leaves tiny
   negative eigenvalues.

For Lambda_k=-i z_k with Re z_k>0,

    Q(Y)=i(Y Lambda-Lambda^dag Y),
    Q(Y+delta I)=Q(Y)+delta i(Lambda-Lambda^dag),

and

    i(Lambda-Lambda^dag)=2 diag(Re z_k) > 0.

Therefore delta I monotonically improves both Y>0 and Q>=0.  The shift is
chosen from rigorous minimum-eigenvalue lower bounds, is reported explicitly,
and the SDP residual/objective are recomputed after the shift.  This is a
numerical enforcement of the original constraints, not a relaxation.
"""
import numpy as np

from direct_port_bath_correlation import HBAR
import coupled_lindblad_pade_sdp as probe

probe.fp.HBAR = HBAR
_original_solve = probe.solve_sdp


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
    # Add a tiny guard above the mathematical lower bound so a subsequent
    # eigensolve cannot fall back below the floor through roundoff.
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


probe.solve_sdp = solve_sdp_with_psd_floor

if __name__ == "__main__":
    probe.main()
