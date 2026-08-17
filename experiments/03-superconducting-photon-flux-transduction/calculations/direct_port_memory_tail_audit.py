#!/usr/bin/env python3
"""Analytic direct-port bath memory-tail audit for TEMPO planning.

For the validated exponential correlation

    C(tau)=sum_k d_k exp(-z_k tau), tau>=0,

the omitted integrated tail beyond a TEMPO memory cutoff tcut is exact:

    I_tail(tcut)=sum_k d_k exp(-z_k tcut)/z_k.

This script reports:
  * |C(tcut)|/|C(0)|;
  * |I_tail|/|I_total|, which includes physical complex cancellation;
  * sum |I_tail,k| / sum |I_total,k|, a conservative no-cancellation bound.

The tail metric is a memory-planning diagnostic only.  It is not a bound on the
reduced-state trace distance and does not replace explicit tcut convergence.
"""
from __future__ import annotations

import numpy as np

import heom_fp_harmonic_oracle as fp


def audit(npade):
    wc,_x,_u,_H,d,z,_ref=fp.harmonic_setup(2,npade)
    C0=np.sum(d)
    I0=np.sum(d/z)
    absI0=np.sum(np.abs(d/z))
    print(f"ORDER p{npade} modes={len(d)} C0=({C0.real:+.12e}{C0.imag:+.12e}j) "
          f"I0=({I0.real:+.12e}{I0.imag:+.12e}j) absI0={absI0:.12e}",flush=True)
    for t in (4,6,8,10,12,14,16,18,20,22,24):
        Ct=np.sum(d*np.exp(-z*t))
        tails=d*np.exp(-z*t)/z
        It=np.sum(tails)
        absIt=np.sum(np.abs(tails))
        print(f"TAIL p{npade} tcut={t:02d} corr_frac={abs(Ct)/abs(C0):.12e} "
              f"signed_int_frac={abs(It)/abs(I0):.12e} "
              f"absolute_int_frac={absIt/absI0:.12e} "
              f"Itail=({It.real:+.12e}{It.imag:+.12e}j)",flush=True)


def main():
    audit(4); audit(5)
    print('PASS_DIRECT_PORT_MEMORY_TAIL_AUDIT')

if __name__=='__main__': main()
