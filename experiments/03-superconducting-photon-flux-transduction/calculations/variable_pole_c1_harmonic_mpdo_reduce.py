#!/usr/bin/env python3
"""Deterministic H0/H1/H2 external-convergence reducer.

Runs only after the three frozen finite-bosonic rank-16 harmonic MPDO cases. It
performs no propagation and cannot alter any case setting.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.linalg import svdvals


def read_rho(path: Path):
    a=np.genfromtxt(path,delimiter=",",names=True)
    n=int(max(a["i"].max(),a["j"].max()))
    z=np.zeros((n,n),complex)
    for r in a:
        z[int(r["i"])-1,int(r["j"])-1]=r["real"]+1j*r["imag"]
    return z


def embed(a,n):
    z=np.zeros((n,n),complex); z[:a.shape[0],:a.shape[1]]=a; return z


def halftrace(a,b):
    n=max(a.shape[0],b.shape[0]); return 0.5*float(np.sum(svdvals(embed(a,n)-embed(b,n))))


def widthdiff(a,b):
    return max(abs(a["final_sx"]/b["final_sx"]-1),abs(a["final_su"]/b["final_su"]-1))


def load(root,name):
    d=Path(root)/name
    return json.loads((d/"metrics.json").read_text()),read_rho(d/"rho_final.csv")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("root")
    args=ap.parse_args()
    m0,r0=load(args.root,"H0"); m1,r1=load(args.root,"H1"); m2,r2=load(args.root,"H2")
    h01=halftrace(r0,r1); w01=widthdiff(m1,m0)
    h12=halftrace(r1,r2); w12=widthdiff(m2,m1)
    tensor_ok=h01<5e-5 and w01<1e-5
    fock_ok=h12<5e-5 and w12<1e-5
    cases_ok=all(m["physical"] and m["fdt"] and m["stationary"] for m in (m0,m1,m2))
    print(f"C1_HARMONIC_MPDO_CROSS H0_H1_half={h01:.12e} H0_H1_width={w01:.12e} tensor_ok={int(tensor_ok)}")
    print(f"C1_HARMONIC_MPDO_CROSS H1_H2_half={h12:.12e} H1_H2_width={w12:.12e} fock_ok={int(fock_ok)}")
    print(f"C1_HARMONIC_MPDO_MATRIX cases_ok={int(cases_ok)} tensor_ok={int(tensor_ok)} fock_ok={int(fock_ok)}")
    out=dict(cases_ok=cases_ok,tensor_ok=tensor_ok,fock_ok=fock_ok,
             H0_H1_half_trace=h01,H0_H1_width=w01,H1_H2_half_trace=h12,H1_H2_width=w12,
             cases={"H0":m0,"H1":m1,"H2":m2})
    Path(args.root,"matrix_summary.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    if not (cases_ok and tensor_ok and fock_ok): raise RuntimeError("finite-bosonic harmonic matrix failed frozen acceptance")
    print("VARIABLE_POLE_C1_FINITE_BOSONIC_HARMONIC_PASS")

if __name__=="__main__": main()
