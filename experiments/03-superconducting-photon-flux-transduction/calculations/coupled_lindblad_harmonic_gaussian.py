#!/usr/bin/env python3
"""Exact Gaussian harmonic benchmark for the physical coupled-Lindblad bath.

The acceptance rule was frozen in
`COUPLED_LINDBLAD_HARMONIC_ACCEPTANCE_2026-08-17.md` before this calculation.

For each p12/p16 physical bath we construct the exact real-quadrature drift and
vacuum diffusion matrices of the enlarged harmonic system + coupled auxiliaries,
solve the continuous Lyapunov equation, and compare the reduced system Gaussian
state against the independently integrated exact direct-port FDT reference.

No auxiliary Fock truncation is used in this harmonic calculation.  This does
not waive explicit basis/Fock convergence for later nonlinear detector work.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov, svdvals

from qutip import destroy, thermal_dm, squeeze

import run_coupled_lindblad_pade_sdp as runner
import heom_harmonic_final_state_gate as finalgate
import heom_harmonic_pade_depth as base
from quantum_initial_capture import PHI_BAR

p = runner.probe

ORDERS = (12, 16)
REF_DIM = 16
EXPECTED_OMEGA_RATIO = 1.1310805656
TAUS = np.array([0.0, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0,
                 8.0, 12.0, 16.0, 20.0, 24.0])


def symplectic(n: int):
    I = np.eye(n)
    Z = np.zeros((n, n))
    return np.block([[Z, I], [-I, Z]])


def physical_bath(N: int):
    wc, _x, _u, _Hsys_truncated, d, z, _ref = p.fp.harmonic_setup(2, N)
    Lam = np.diag(-1j * z)
    l, r = p.balanced_lr(d)
    Y, status, _obj, residual, relsdp, solver = p.solve_sdp(Lam, l, r)
    K, g, H, Gamma, ey = p.reconstruct(Lam, r, Y)
    return dict(N=N, wc=wc, d=d, z=z, K=K, g=g, H=H, Gamma=Gamma,
                Y=Y, Yev=ey, status=status, residual=residual,
                relsdp=relsdp, solver=solver)


def aux_real_matrices(H: np.ndarray, Gamma: np.ndarray):
    """Return auxiliary real drift, diffusion, and symplectic form.

    Ordering is R_A=(q_1,...,q_K,p_1,...,p_K).
    The paper's K=H-i Gamma gives bdot=(-i H-Gamma)b.
    """
    Hr = np.asarray(H.real, float)
    Hi = np.asarray(H.imag, float)
    Gr = np.asarray(Gamma.real, float)
    Gi = np.asarray(Gamma.imag, float)
    Aham = np.block([[Hi, Hr], [-Hr, Hi]])
    Adamp = np.block([[-Gr, Gi], [-Gi, -Gr]])
    A = Aham + Adamp
    D = -Adamp
    Om = symplectic(H.shape[0])
    return A, D, Om


def bcf_from_real(tau: float, bath):
    A, _D, Om = aux_real_matrices(bath['H'], bath['Gamma'])
    g = bath['g']
    h = math.sqrt(2.0) * np.concatenate([g.real, g.imag])
    F0 = 0.5 * (np.eye(len(h)) + 1j * Om)
    return complex(h @ (expm(A * float(tau)) @ (F0 @ h)))


def enlarged_matrices(bath, sigma0: float):
    """Construct H=1/2 R^T G R, drift A, and diffusion D.

    Ordering is all q followed by all p:
      (q_s,q_1,...,q_K,p_s,p_1,...,p_K).
    """
    Kmode = len(bath['g'])
    n = Kmode + 1
    Om = symplectic(n)
    Gq = np.zeros((n, n), float)
    Gp = np.zeros((n, n), float)
    Gqp = np.zeros((n, n), float)  # q-block rows, p-block cols

    ct_phys = PHI_BAR**2 / base.HBAR * base.G * base.WD / (2.0 * math.sqrt(2.0))
    lam = ct_phys / bath['wc']
    Gq[0, 0] = 1.0 + 4.0 * lam * sigma0 * sigma0
    Gp[0, 0] = 1.0

    H = bath['H']
    Hr = np.asarray(H.real, float)
    Hi = np.asarray(H.imag, float)
    Gq[1:, 1:] = Hr
    Gp[1:, 1:] = Hr
    Gqp[1:, 1:] = -Hi

    # x*A = 2 sigma0 q_s [Re(g).q_A + Im(g).p_A].
    Gq[0, 1:] = 2.0 * sigma0 * bath['g'].real
    Gq[1:, 0] = Gq[0, 1:]
    Gqp[0, 1:] = 2.0 * sigma0 * bath['g'].imag

    Gmat = np.block([[Gq, Gqp], [Gqp.T, Gp]])
    if np.linalg.norm(Gmat - Gmat.T, ord='fro') > 1e-11:
        raise RuntimeError('quadratic Hamiltonian matrix is not symmetric')

    # Lindblad damping/noise acts only on auxiliaries.  Build its realification
    # in the same all-q/all-p ordering and embed around the system indices.
    Gr = np.asarray(bath['Gamma'].real, float)
    Gi = np.asarray(bath['Gamma'].imag, float)
    Ad_aux = np.block([[-Gr, Gi], [-Gi, -Gr]])
    D_aux = -Ad_aux

    Ad = np.zeros((2*n, 2*n), float)
    Diff = np.zeros((2*n, 2*n), float)
    idx = np.r_[np.arange(1, n), np.arange(n+1, 2*n)]
    Ad[np.ix_(idx, idx)] = Ad_aux
    Diff[np.ix_(idx, idx)] = D_aux

    A = Om @ Gmat + Ad
    return Gmat, A, Diff, Om, lam


def symplectic_nu(V: np.ndarray, Om: np.ndarray):
    vals = np.linalg.eigvals(1j * Om @ V)
    return np.sort(np.abs(vals))[::2]


def covariance_of_rho(rho, q, pp):
    mq = complex((rho*q).tr())
    mp = complex((rho*pp).tr())
    qq = float(np.real((rho*q*q).tr() - mq*mq))
    p2 = float(np.real((rho*pp*pp).tr() - mp*mp))
    qp = 0.5 * complex((rho*(q*pp + pp*q)).tr()) - mq*mp
    return np.array([[qq, float(np.real(qp))],
                     [float(np.real(qp)), p2]], float)


def gaussian_rho_from_cov(V: np.ndarray, dim: int):
    """Construct a zero-mean one-mode Gaussian density matrix from covariance."""
    V = 0.5 * (V + V.T)
    nu = math.sqrt(float(np.linalg.det(V)))
    if nu < 0.5 - 1e-9:
        raise RuntimeError(f'one-mode covariance violates uncertainty: nu={nu}')
    nbar = max(nu - 0.5, 0.0)
    ratio = float(np.trace(V) / (2.0 * nu))
    ratio = max(ratio, 1.0)
    rr = 0.5 * math.acosh(ratio)
    m = 0.5 * (V[0, 0] - V[1, 1] + 2j * V[0, 1])
    phi = 0.0 if abs(m) < 1e-15 else float(np.angle(-m))
    zeta = rr * np.exp(1j * phi)

    S = squeeze(dim, zeta)
    rho = S * thermal_dm(dim, nbar) * S.dag()
    a = destroy(dim)
    q = (a + a.dag()) / math.sqrt(2.0)
    pp = 1j * (a.dag() - a) / math.sqrt(2.0)
    Vrec = covariance_of_rho(rho, q, pp)
    recerr = float(np.linalg.norm(Vrec - V, ord='fro') /
                   max(np.linalg.norm(V, ord='fro'), 1e-300))
    return rho, dict(nu=nu, nbar=nbar, r=rr, phi=phi,
                     zeta=zeta, Vrec=Vrec, recerr=recerr)


def run_order(N: int, ref):
    bath = physical_bath(N)
    sigma0 = ref['sigma0']

    # Exact BCF mapping identity of the real auxiliary drift.
    bcferrs = []
    for tau in TAUS:
        c1 = bcf_from_real(float(tau), bath)
        c2 = p.cc(float(tau), bath['K'], bath['g'])
        bcferrs.append(abs(c1-c2) / max(abs(c2), 1e-14))
    bcferr = float(max(bcferrs))

    # Uncoupled auxiliary vacuum must be an exact fixed point.
    Aa, Da, _Oa = aux_real_matrices(bath['H'], bath['Gamma'])
    Vvac = 0.5 * np.eye(Aa.shape[0])
    rvac = Aa @ Vvac + Vvac @ Aa.T + Da
    vacres = float(np.linalg.norm(rvac, ord='fro') /
                   max(np.linalg.norm(Da, ord='fro'), 1.0))

    Gmat, A, Diff, Om, lam = enlarged_matrices(bath, sigma0)
    gqq = Gmat[0, 0]
    omega_iso = math.sqrt(gqq * Gmat[len(bath['g'])+1, len(bath['g'])+1])
    omega_relerr = abs(omega_iso / EXPECTED_OMEGA_RATIO - 1.0)

    evA = np.linalg.eigvals(A)
    maxRe = float(np.max(evA.real))
    if maxRe >= 0:
        # Still solve only if stable; an unstable result is already a hard fail.
        raise RuntimeError(f'p{N} enlarged Gaussian drift unstable: maxRe={maxRe}')

    V = solve_continuous_lyapunov(A, -Diff)
    V = np.asarray(np.real_if_close(V, tol=1000), float)
    V = 0.5 * (V + V.T)
    resid = A @ V + V @ A.T + Diff
    lyapres = float(np.linalg.norm(resid, ord='fro') /
                    max(np.linalg.norm(Diff, ord='fro'), 1.0))
    nus = symplectic_nu(V, Om)
    numin = float(nus.min())

    nm = len(bath['g']) + 1
    Vsys = np.array([[V[0, 0], V[0, nm]],
                     [V[nm, 0], V[nm, nm]]], float)
    sx = math.sqrt(max(2.0 * sigma0*sigma0 * Vsys[0, 0], 0.0))
    su = math.sqrt(max(2.0 * sigma0*sigma0 * Vsys[1, 1], 0.0))
    relx = sx/ref['target_x'] - 1.0
    relu = su/ref['target_u'] - 1.0
    maxwidth = max(abs(relx), abs(relu))
    crossnorm = abs(Vsys[0, 1]) / math.sqrt(Vsys[0, 0]*Vsys[1, 1])

    rho, grec = gaussian_rho_from_cov(Vsys, REF_DIM)
    ah = np.asarray(rho.full(), complex)
    ae = np.asarray(ref['rho'].full(), complex)
    nuclear = 0.5 * float(np.sum(svdvals(ah-ae)))
    frob = float(np.linalg.norm(ah-ae, ord='fro'))

    out = dict(N=N, bath=bath, bcferr=bcferr, vacres=vacres,
               omega_iso=omega_iso, omega_relerr=omega_relerr,
               maxRe=maxRe, lyapres=lyapres, numin=numin, V=V, Vsys=Vsys,
               sx=sx, su=su, relx=relx, relu=relu, maxwidth=maxwidth,
               crossnorm=crossnorm, nuclear=nuclear, frob=frob, grec=grec,
               lam=lam)

    print(f'GAUSSIAN_IMPL p{N} bcferr={bcferr:.12e} vacres={vacres:.12e} '
          f'omega_iso={omega_iso:.12e} omega_relerr={omega_relerr:.12e} '
          f'maxRe={maxRe:+.12e} lyapres={lyapres:.12e} numin={numin:.12e}',
          flush=True)
    print(f'GAUSSIAN_STATE p{N} sx={sx:.12e} relx={relx:+.12e} '
          f'su={su:.12e} relu={relu:+.12e} maxwidth={maxwidth:.12e} '
          f'Vqp={Vsys[0,1]:+.12e} crossnorm={crossnorm:.12e} '
          f'nu_sys={grec["nu"]:.12e} nbar_eff={grec["nbar"]:.12e} '
          f'r={grec["r"]:.12e} phi={grec["phi"]:+.12e} '
          f'rho_reconstruction={grec["recerr"]:.12e} '
          f'nuclear_half={nuclear:.12e} frob={frob:.12e}', flush=True)
    return out


def main():
    ref = finalgate.exact_reference(REF_DIM)
    print(f'EXACT_REFERENCE dim={REF_DIM} basis_err={ref["basis_err"]:.12e} '
          f'target_x={ref["target_x"]:.12e} target_u={ref["target_u"]:.12e} '
          f'sigma0={ref["sigma0"]:.12e} nbar={ref["nbar"]:.12e} r={ref["r"]:.12e}',
          flush=True)

    rows = [run_order(N, ref) for N in ORDERS]
    p12, p16 = rows

    mandatory = all(
        r['bcferr'] < 1e-10 and
        r['vacres'] < 1e-12 and
        r['omega_relerr'] < 2e-9 and
        r['maxRe'] < -1e-8 and
        r['lyapres'] < 1e-10 and
        r['numin'] >= 0.5 - 1e-9 and
        r['grec']['recerr'] < 1e-7
        for r in rows
    )
    trend = (p16['maxwidth'] < p12['maxwidth'] and
             p16['nuclear'] < p12['nuclear'])
    improvement25 = (max(p16['maxwidth'], p16['nuclear']) <
                     0.75 * max(p12['maxwidth'], p12['nuclear']))

    finalpass = (
        mandatory and trend and
        ref['basis_err'] < 1e-7 and
        p16['maxwidth'] < 1e-6 and
        p16['nuclear'] < 5e-6 and
        p16['crossnorm'] < 1e-5
    )
    authorize = mandatory and trend and improvement25 and not finalpass

    print(f'GAUSSIAN_ACCEPTANCE mandatory={int(mandatory)} trend={int(trend)} '
          f'improvement25={int(improvement25)} finalpass={int(finalpass)} '
          f'authorize_p24_p32={int(authorize)}', flush=True)
    if finalpass:
        print('COUPLED_LINDBLAD_HARMONIC_PASS', flush=True)
    elif authorize:
        print('COUPLED_LINDBLAD_HARMONIC_AUTHORIZE_P24_P32', flush=True)
    else:
        print('COUPLED_LINDBLAD_HARMONIC_FAIL', flush=True)


if __name__ == '__main__':
    main()
