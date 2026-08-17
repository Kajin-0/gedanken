#!/usr/bin/env python3
"""Nonlinear restricted-left-well HEOM convergence pilot for Experiment 03.

This is a Gate-C calibration run, NOT an acceptance calculation and NOT a
photon-capture calculation.

The purpose is to take the already validated phase-DVR metastable-well basis and
the already validated Gate-B direct-port Padé HEOM bath, combine them without
changing the physical environment, and measure the numerical scales that should
set the prospective Gate-C.1 acceptance thresholds.

Physical/model choices
----------------------
* delta = .212 certified reduced operating point.
* cold T = 20 mK.
* restricted left-well Hamiltonian has a Dirichlet wall at the cold saddle,
  exactly as in phase_dvr_basis_convergence.py.
* the bath is the same direct-port two-pole spectral density and Padé
  decomposition used in harmonic Gate B.
* coupling coordinate is y=x-x_m.  A constant coordinate offset is a bath
  displacement and does not alter reduced phase dynamics; using y makes the
  counterterm consistent with the local harmonic Gate-B convention.
* the physical Caldeira-Leggett counterterm is retained.

The pilot varies hierarchy depth, Padé order, phase basis dimension, and the
left box boundary.  Only gross per-job sanity guards are enforced.  Cross-case
acceptance tolerances must be fixed in a separate checkpoint AFTER this pilot
and BEFORE any deeper decisive run.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np
from scipy.linalg import svdvals

import full_dynamic_rfsquid as fd
import phase_dvr_basis_convergence as dvr
import heom_harmonic_pade_depth as bathbase
from quantum_initial_capture import HBAR, KB, PHI_BAR

from qutip import Qobj, expect
from qutip.solver.heom import BosonicBath, HEOMSolver


DELTA = .21200
RSC = dvr.ROOTS[DELTA]
L = dvr.L0
C = dvr.C0 * RSC * RSC
T0 = fd.T0

# Pilot-only matrix.  These are calibration points, not a pass/fail frontier.
CASES = {
    "large_dim8_p4d4": dict(xmin=-3.8, ngrid=2200, dim=8, npade=4, depth=4),
    "large_dim8_p4d5": dict(xmin=-3.8, ngrid=2200, dim=8, npade=4, depth=5),
    "large_dim8_p5d5": dict(xmin=-3.8, ngrid=2200, dim=8, npade=5, depth=5),
    "large_dim10_p4d5": dict(xmin=-3.8, ngrid=2200, dim=10, npade=4, depth=5),
    "medium_dim8_p4d5": dict(xmin=-3.2, ngrid=1800, dim=8, npade=4, depth=5),
}


def projected_operator(x: np.ndarray, vec: np.ndarray, values: np.ndarray) -> Qobj:
    """Project a multiplicative DVR operator into the retained eigenbasis."""
    dx = float(x[1]-x[0])
    mat = vec.conj().T @ (values[:, None] * vec) * dx
    mat = 0.5*(mat + mat.conj().T)
    return Qobj(mat)


def bare_gibbs(e: np.ndarray) -> Qobj:
    de = np.asarray(e-e[0], dtype=float)
    z = np.exp(-de/(KB*T0))
    z /= z.sum()
    return Qobj(np.diag(z.astype(complex)))


def nonlinear_system(cfg):
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    original = fd.CASES[.6]
    try:
        fd.BETA_COLD = .80
        fd.DELTA_TILT = DELTA
        fd.CASES[.6] = (L, C, original[2])
        model = fd.DynamicForce(.6, quick=False, Tmax=1.02)
        roots = model.roots(T0)
        mins = [(x,k) for x,k in roots if k > 0]
        saddles = [(x,k) for x,k in roots if k < 0]
        xm = max(x for x,k in mins if x < 0)
        xs = min(saddles, key=lambda z: abs(z[0]))[0]
        km = float(np.asarray(model.spline.ev(T0, xm, dx=0, dy=1)).reshape(-1)[0])
        wc = math.sqrt(km/(L*C))

        x, U, e, vec, residuals = dvr.spectrum(
            model, T0, C, cfg["xmin"], xs, cfg["ngrid"], cfg["dim"]
        )
        y = x-xm
        yop = projected_operator(x, vec, y)
        y2_direct = projected_operator(x, vec, y*y)
        # Projection and squaring do not commute in a truncated basis.  The CL
        # counterterm is the projected physical y^2 operator, not (P y P)^2.
        h0 = Qobj(np.diag(((e-e[0])/(HBAR*wc)).astype(complex)))
        ct_phys = PHI_BAR**2/HBAR * bathbase.G*bathbase.WD/(2*math.sqrt(2))
        hsys = h0 + (ct_phys/wc)*y2_direct
        rho0 = bare_gibbs(e)
        return model, xm, xs, wc, e, yop, y2_direct, h0, hsys, rho0, residuals
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot
        fd.CASES[.6] = original


def state_metrics(rho, yop, y2op, h0, rho_gibbs):
    a = np.asarray(rho.full(), dtype=complex)
    tr = complex(np.trace(a))
    anti = np.linalg.norm(a-a.conj().T, ord="fro")/max(np.linalg.norm(a, ord="fro"),1e-300)
    ev = np.linalg.eigvalsh(0.5*(a+a.conj().T))
    neg = float(np.sum(np.maximum(-ev,0.0)))
    ymin = float(np.real(expect(yop,rho)))
    y2 = float(np.real(expect(y2op,rho)))
    sig = math.sqrt(max(y2-ymin*ymin,0.0))
    energy = float(np.real(expect(h0,rho)))
    top = float(np.real(a[-1,-1]))
    dg = a-np.asarray(rho_gibbs.full(),dtype=complex)
    gibbs_half = 0.5*float(np.sum(svdvals(dg)))
    return dict(trace=tr, anti=anti, eigmin=float(ev.min()), neg=neg,
                mean=ymin, sigma=sig, energy=energy, top=top,
                gibbs_half=gibbs_half)


def run_case(name: str):
    cfg = CASES[name]
    model,xm,xs,wc,e,yop,y2op,h0,hsys,rho0,residuals = nonlinear_system(cfg)
    cr,vr,ci,vi = bathbase.pade_bath_expansion(wc,cfg["npade"])
    bath = BosonicBath(yop,cr,vr,ci,vi,combine=True,tag="direct-port-pade-nonlinear")
    nexp = len(bath.exponents)
    nado = math.comb(nexp+cfg["depth"],cfg["depth"])
    print(f"CASE={name} delta={DELTA:.5f} r={RSC:.10f} C={C*1e12:.6f}pF",flush=True)
    print(f"xmin={cfg['xmin']:+.3f} Ngrid={cfg['ngrid']} dim={cfg['dim']} "
          f"Npade={cfg['npade']} depth={cfg['depth']} nexp={nexp} nado_est={nado}",flush=True)
    print(f"xm={xm:+.10f} xs={xs:+.10f} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz "
          f"max_DVR_residual_K={float(np.max(residuals)):.3e}",flush=True)
    print("transitions_K="+",".join(f"{q:.9e}" for q in (e[:min(8,len(e))]-e[0])/KB),flush=True)

    tlist = np.array([0.,10.,20.,40.,80.,120.,160.])
    solver = HEOMSolver(
        hsys,bath,max_depth=cfg["depth"],
        options={
            "progress_bar":"",
            "store_states":True,
            "method":"bdf",
            "rtol":2e-7,
            "atol":2e-9,
            "nsteps":250000,
        },
    )
    t0=time.perf_counter()
    result=solver.run(rho0,tlist,e_ops=[yop,y2op,h0])
    runtime=time.perf_counter()-t0

    rows=[]
    for i,tau in enumerate(tlist):
        rho=result.states[i]
        m=state_metrics(rho,yop,y2op,h0,rho0); rows.append(m)
        print(f"tau={tau:7.2f} mean_y={m['mean']:+.10e} sigma_y={m['sigma']:.10e} "
              f"E0_units={m['energy']:.10e} eigmin={m['eigmin']:+.6e} "
              f"negmass={m['neg']:.6e}",flush=True)

    f=rows[-1]; p=rows[-2]
    late=max(abs(f["mean"]-p["mean"]),abs(f["sigma"]-p["sigma"]),
             abs(f["energy"]-p["energy"]))
    msg=(f"CASE={name} FINAL trace=({f['trace'].real:.12e}{f['trace'].imag:+.2e}j) "
         f"antiherm={f['anti']:.3e} eigmin={f['eigmin']:+.6e} negmass={f['neg']:.6e} "
         f"mean_y={f['mean']:+.10e} sigma_y={f['sigma']:.10e} E0_units={f['energy']:.10e} "
         f"topPop={f['top']:+.6e} bareGibbs_nuclear_half={f['gibbs_half']:.6e} "
         f"late_abs_drift={late:.6e} runtime_s={runtime:.3f}")
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 nonlinear left-well HEOM pilot::{msg}",flush=True)

    # Gross pilot guards only.  Do not reinterpret these as Gate-C thresholds.
    if abs(f["trace"]-1)>5e-6: raise RuntimeError("gross trace failure")
    if f["anti"]>1e-7: raise RuntimeError("gross Hermiticity failure")
    if f["neg"]>1e-3: raise RuntimeError("gross negativity")
    if abs(f["top"])>1e-2: raise RuntimeError("gross phase-basis truncation")
    if late>5e-3: raise RuntimeError("gross failure to settle")
    print("PASS_PILOT",flush=True)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--case",choices=sorted(CASES),required=True)
    args=ap.parse_args()
    run_case(args.case)


if __name__ == "__main__":
    main()
