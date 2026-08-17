#!/usr/bin/env python3
"""Final predeclared p16/p24/p32 coupled-Lindblad harmonic matrix.

Authorization and final thresholds were frozen in
`COUPLED_LINDBLAD_HARMONIC_ACCEPTANCE_2026-08-17.md` before the p12/p16 result.
No p20/p28/post-hoc Padé-order scanning is permitted.
"""
from __future__ import annotations

import coupled_lindblad_harmonic_gaussian as h

ORDERS = (16, 24, 32)


def main():
    ref = h.finalgate.exact_reference(h.REF_DIM)
    print(f'FINAL_EXACT_REFERENCE dim={h.REF_DIM} basis_err={ref["basis_err"]:.12e} '
          f'target_x={ref["target_x"]:.12e} target_u={ref["target_u"]:.12e}',
          flush=True)

    rows = [h.run_order(N, ref) for N in ORDERS]
    p16, p24, p32 = rows

    mandatory = all(
        r['bcferr'] < 1e-10 and
        r['vacres'] < 1e-12 and
        r['omega_relerr'] < 2e-9 and
        r['maxRe'] < -1e-8 and
        r['lyapres'] < 1e-10 and
        r['numin'] >= 0.5 - 1e-9 and
        r['grec']['recerr'] < 1e-7 and
        r['bath']['Yev'].min() > 0.0 and
        r['bath']['relsdp'] >= 0.0
        for r in rows
    )

    monotone_state = (
        p24['maxwidth'] < p16['maxwidth'] and
        p32['maxwidth'] < p24['maxwidth'] and
        p24['nuclear'] < p16['nuclear'] and
        p32['nuclear'] < p24['nuclear']
    )

    # Bath correction itself is a supporting convergence diagnostic.  It was
    # not a new post-hoc threshold in the harmonic acceptance rule, but a
    # reversal is reported explicitly because it would weaken interpretation.
    monotone_bath = (
        p24['bath']['relsdp'] < p16['bath']['relsdp'] and
        p32['bath']['relsdp'] < p24['bath']['relsdp']
    )

    finalpass = (
        mandatory and monotone_state and
        ref['basis_err'] < 1e-7 and
        p32['maxwidth'] < 1e-6 and
        p32['nuclear'] < 5e-6 and
        p32['crossnorm'] < 1e-5
    )

    for r in rows:
        print(f'FINAL_ORDER p{r["N"]} relSDP={r["bath"]["relsdp"]:.12e} '
              f'maxwidth={r["maxwidth"]:.12e} nuclear={r["nuclear"]:.12e} '
              f'crossnorm={r["crossnorm"]:.12e} maxRe={r["maxRe"]:+.12e} '
              f'numin={r["numin"]:.12e}', flush=True)

    print(f'FINAL_COUPLED_GAUSSIAN_ACCEPTANCE mandatory={int(mandatory)} '
          f'monotone_state={int(monotone_state)} monotone_bath={int(monotone_bath)} '
          f'finalpass={int(finalpass)}', flush=True)

    if finalpass:
        print('COUPLED_LINDBLAD_HARMONIC_FINAL_PASS', flush=True)
    else:
        print('COUPLED_LINDBLAD_HARMONIC_FINAL_FAIL', flush=True)
        print('PADE_COORDINATE_COUPLED_ROUTE_CLOSED_IF_NO_IMPLEMENTATION_FAILURE',
              flush=True)


if __name__ == '__main__':
    main()
