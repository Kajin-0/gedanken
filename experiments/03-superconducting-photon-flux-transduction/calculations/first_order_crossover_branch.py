#!/usr/bin/env python3
"""Continue the finite-amplitude periodic instanton through the local sphaleron crossover.

The earlier solver treated the first Matsubara instability temperature T_x as
the physical quantum-to-thermal crossover.  Direct normal-form tests falsified
that assumption: as T -> T_x^- the lowest-action one-negative-mode periodic
saddle retains finite amplitude and remains lower in action than the sphaleron.
This is the characteristic topology of a first-order escape-rate crossover.

Here we continue that *same finite-amplitude periodic branch* upward through
T_x.  The physical exponential crossover is the action intersection

    B_per(T_c) = B_sph(T_c) = DeltaU/(k_B T_c),

provided the periodic saddle still has exactly one negative mode there.  If the
branch folds before an action crossing, that fold is reported instead.

The calculation is done at the unscaled electrical reference C0,R0.  Exact
electrical similarity then maps temperatures to the physical T0=20 mK design
family via

    r = T/T0,
    B(T0;r) = r B_base(r T0).

Thus r_c=T_c/T0 is the true first-order crossover scale along the electrical
similarity family, replacing the local-instability scale r_x=T_x/T0.
"""
from __future__ import annotations

import argparse, math
import numpy as np

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2

C0=215e-15; R0=80.0


def amp_norm(sys,a):
    # L2 norm of nonconstant harmonics on one period.
    return math.sqrt(float(np.sum((a[1:]**2)*sys['norms'][1:])))


def continue_branch(delta,nbasis=48,ngrid=6144):
    st=ft2.static_model(delta,C0,R0)
    Tx,_=ft2.exact_crossover(st)
    # Get a clean one-negative finite-amplitude point below the local bifurcation.
    Tstart=.90*Tx
    out=ft.finiteT_bounce(st,Tstart,Tx,nbasis,ngrid)
    if out['kind']!='periodic': raise RuntimeError('failed to obtain starting periodic branch')
    sys=out['sys']; o=out['o']
    rows=[]

    # Small steps resolve a possible subcritical branch fold above Tx.
    fracs=np.concatenate([
        np.linspace(.90,.99,10,endpoint=True),
        np.linspace(.995,1.05,23,endpoint=True),
        np.linspace(1.06,1.35,30,endpoint=True),
    ])
    fracs=np.unique(np.round(fracs,7))
    # Start from the exact Tstart solution and march only upward.
    for frac in fracs:
        T=float(frac*Tx)
        if abs(T-Tstart)<1e-12:
            no=o; newsys=sys
        elif T<Tstart:
            continue
        else:
            newsys=ft.periodic_system(st,T,nbasis,ngrid)
            a0=ft.project_coeffs(sys,o['a'],newsys)
            no=ft.solve_stationary(newsys,a0,maxfev=12000)
            nneg=int(np.sum(no['ev']<0))
            amp=amp_norm(newsys,no['a'])
            # A Newton collapse to the static sphaleron is not continuation of
            # the finite-amplitude branch.  Stop and report the last valid row.
            if (not no['success']) or no['grad']>3e-6 or nneg!=1 or amp<1e-4:
                print(f'BRANCH_STOP T/Tx={frac:.7f} success={no["success"]} grad={no["grad"]:.3e} '
                      f'nneg={nneg} amp={amp:.6e}')
                break
        amp=amp_norm(newsys,no['a'])
        Bs=st['barrierK']/T
        diff=float(no['B']-Bs)
        center=st['xm']+float(np.sum(no['a']))
        rows.append(dict(frac=frac,T=T,B=float(no['B']),Bs=Bs,diff=diff,
                         amp=amp,nneg=int(np.sum(no['ev']<0)),grad=no['grad'],center=center))
        print(f'T/Tx={frac:.7f} T={T:.9f}K Bper={no["B"]:.9f} Bsph={Bs:.9f} '
              f'Bper-Bsph={diff:+.9e} amp={amp:.9e} nneg={int(np.sum(no["ev"]<0))} '
              f'center={center:+.7f} grad={no["grad"]:.2e}')
        sys,o=newsys,no

    if len(rows)<4: raise RuntimeError('periodic branch continuation too short')
    # Find first action crossing from periodic-dominant (diff<0) to thermal-dominant (diff>0).
    cross=None
    for a,b in zip(rows[:-1],rows[1:]):
        if a['diff']<=0 and b['diff']>=0:
            # Linear interpolation is only a locator; report bracket explicitly.
            w=-a['diff']/(b['diff']-a['diff']) if b['diff']!=a['diff'] else .5
            Tc=a['T']+w*(b['T']-a['T'])
            cross=(a,b,Tc)
            break
    if cross:
        a,b,Tc=cross
        rc=Tc/fd.T0
        msg=(f'delta={delta:.3f}: FIRST_ORDER_ACTION_CROSSING '
             f'Tc~{Tc:.9f}K Tc/Tx~{Tc/Tx:.7f} r_c~{rc:.8f}; '
             f'bracket=[{a["frac"]:.7f},{b["frac"]:.7f}] '
             f'amps=[{a["amp"]:.6e},{b["amp"]:.6e}]')
    else:
        last=rows[-1]
        msg=(f'delta={delta:.3f}: NO_ACTION_CROSSING_BEFORE_BRANCH_STOP_OR_SCAN_END; '
             f'last_T/Tx={last["frac"]:.7f} last_diff={last["diff"]:+.6e} '
             f'last_amp={last["amp"]:.6e}')
    print(msg); print(f'::notice title=Experiment 03 first-order crossover branch::{msg}')
    print(f'local_linear_scale: Tx={Tx:.9f}K r_x={Tx/fd.T0:.8f}')
    print('PASS')
    return rows,cross


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in (.212,.213,.214,.215): raise SystemExit('supported: .212-.215')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        continue_branch(d)
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
