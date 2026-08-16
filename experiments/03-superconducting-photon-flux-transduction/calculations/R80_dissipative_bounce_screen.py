#!/usr/bin/env python3
"""Frequency-dependent Euclidean bounce screen for the current R80 candidate.

This is the next dark-stability level beyond the old isolated cubic-barrier MQT
formula.  It uses the actual non-sinusoidal cold rf-SQUID potential and the same
passive two-pole environment selected by the photon-capture calculation.

For q=Phi_bar*x, integrating a linear passive environment gives the zero-T
Euclidean quadratic kernel

    S_env = (Phi_bar^2/2) int dω/(2π) [ |ω| Y_L(|ω|) ] |y(ω)|^2,

where y=x-x_m and Y_L(s) is the positive-real Laplace admittance seen at the
phase port.  For the passive two-pole network

    Z(s)=s Lf + R/(1+s R Cf),
    Y_L(s)=1/Z(s).

The script computes:

1. the exact *isolated* zero-energy bounce of the actual CPR potential;
2. its exact isolated Euclidean action B0=S0/hbar;
3. the first-order environmental action correction Benv evaluated on that
   isolated bounce;
4. a restricted time-rescaling variational diagnostic

       x_a(tau)=x_0(tau/a)

   to estimate how strongly the frequency-dependent environment tries to alter
   the bounce duration.

What this is NOT
----------------
- not the full nonlocal dissipative bounce solution;
- not the fluctuation-determinant/prefactor calculation;
- not a physical DCR prediction;
- not a replacement for a systematic Caldeira-Leggett / ImF treatment.

Its purpose is to determine whether the selected environment changes the MQT
exponent by <<1, O(1), or many units.  If the correction is large, the earlier
isolated diagnostic is demonstrably not the right dark-stability model.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar

from full_dynamic_rfsquid import CASES, DynamicForce, T0
from finite_time_basin_slice import cold_phase_scale
from directional_recovery_barriers import directional_barriers
from causal_two_pole_environment import filter_components
from quantum_initial_capture import HBAR, PHI_BAR, KB


def potential_delta(model: DynamicForce, xm: float, x: float) -> float:
    """Dimensionless U(x)-U(xm), with dU/dx=F."""
    return float(quad(lambda xx:model.force(T0,xx),xm,x,
                      epsabs=2e-12,epsrel=2e-10,limit=250)[0])


def turning_point(model: DynamicForce,xm: float,xs: float,xr: float) -> float:
    f=lambda x: potential_delta(model,xm,x)
    # At the saddle f>0; in the favored right well it must become negative for
    # the left metastable bounce to have a finite zero-energy turning point.
    fs=f(xs); fr=f(xr)
    if not (fs>0 and fr<0):
        raise RuntimeError(f'turning bracket failed: U_s={fs}, U_right={fr}')
    return float(brentq(f,xs,xr,xtol=2e-13,rtol=2e-13,maxiter=200))


def isolated_bounce(model: DynamicForce,nfft: int=65536,tail_eps: float=2e-9):
    L,C,_=CASES[.6]
    xm,kappa,wc=cold_phase_scale(model,.6)
    b=directional_barriers(model,T0)
    xs=b['saddle']; xr=b['right']
    xt=turning_point(model,xm,xs,xr)

    # Euclidean normalized-time equation: d2x/ds2=F/kappa, s=wc*tau.
    # Start exactly at the zero-energy turning point with zero velocity.
    def rhs(s,y): return np.array([y[1],model.force(T0,float(y[0]))/kappa])
    def event_tail(s,y): return float(y[0]-xm-tail_eps)
    event_tail.terminal=True; event_tail.direction=-1
    sol=solve_ivp(rhs,(0,40),np.array([xt,0.0]),events=event_tail,
                  method='DOP853',rtol=2e-11,atol=np.array([2e-12,2e-12]),
                  max_step=.01,dense_output=True)
    if not len(sol.t_events[0]):
        raise RuntimeError('isolated bounce did not reach tail threshold')
    Shalf=float(sol.t_events[0][0])

    # Symmetric zero-padded interval. Choose period 4*Shalf so the two tails are
    # separated by a large exact-zero region and periodic FFT wraparound is tiny.
    Sbox=2.0*Shalf
    s=np.linspace(-Sbox,Sbox,nfft,endpoint=False)
    y=np.zeros_like(s); p=np.zeros_like(s)
    mask=np.abs(s)<=Shalf
    vals=sol.sol(np.abs(s[mask]))
    y[mask]=vals[0]-xm
    # derivative of symmetric x(|s|): odd sign.
    ptmp=vals[1]
    p[mask]=np.where(s[mask]>=0,ptmp,-ptmp)

    # Isolated action directly in normalized s.
    EL=PHI_BAR**2/L
    M=C*PHI_BAR**2
    u=np.zeros_like(s)
    # Avoid many adaptive quads: integrate F once over sorted x table, then interp.
    xlo=xm; xhi=xt
    xgrid=np.linspace(xlo,xhi,16001)
    Fgrid=np.array([model.force(T0,float(xx)) for xx in xgrid])
    # cumulative trapezoid manually so this file has no extra import dependency.
    dx=xgrid[1]-xgrid[0]
    Ugrid=np.concatenate(([0.0],np.cumsum(0.5*(Fgrid[:-1]+Fgrid[1:])*dx)))
    u[mask]=np.interp(xm+y[mask],xgrid,Ugrid)
    ds=s[1]-s[0]
    K=(M*wc/2.0)*float(np.sum(p*p)*ds)/HBAR
    V=(EL/wc)*float(np.sum(u)*ds)/HBAR
    Btime=K+V

    # Independent exact 1D WKB/bounce integral.
    def integrand(x):
        uu=max(potential_delta(model,xm,float(x)),0.0)
        return math.sqrt(2.0*M*EL*uu)
    Bquad=2.0/HBAR*quad(integrand,xm,xt,epsabs=1e-33,epsrel=2e-9,limit=300)[0]

    # FFT convention approximates integral ds exp(-i Omega s)y(s).
    Y=np.fft.fft(y)*ds
    Om=2*math.pi*np.fft.fftfreq(nfft,d=ds)
    dOm=2*math.pi/(nfft*ds)
    return {
        'L':L,'C':C,'xm':xm,'xs':xs,'xr':xr,'xt':xt,'kappa':kappa,'wc':wc,
        'Shalf':Shalf,'s':s,'y':y,'p':p,'u':u,'Om':Om,'Y':Y,'dOm':dOm,
        'K':K,'V':V,'Btime':Btime,'Bquad':Bquad,
        'barrierK':b['b_left']*(EL/KB),
    }


def Y_laplace(s: np.ndarray,R: float,wd: float) -> np.ndarray:
    """Positive-real Laplace admittance of series Lf + (R || Cf)."""
    Lf,Cf=filter_components(R,wd)
    return (1.0+s*R*Cf)/(R+s*Lf+s*s*Lf*R*Cf)


def env_action_on_scaled_bounce(dat,R: float,alpha: float,a: float=1.0) -> float:
    """B_env=S_env/hbar for y_a(s)=y_0(s/a), using fixed bounce FFT.

    After changing integration variable z=a*Omega, the explicit time-scaling
    factors cancel and only the admittance argument shifts:
        Benv(a) = Phi_bar^2/(2 hbar) int dz/(2pi)
                  |z| Y_L(wc |z|/a) |Y0(z)|^2.
    """
    Om=np.abs(dat['Om']); wd=alpha*dat['wc']
    YY=np.abs(dat['Y'])**2
    YL=Y_laplace(dat['wc']*Om/a,R,wd)
    val=float(np.sum(Om*YL*YY)*dat['dOm']/(2*math.pi))
    return PHI_BAR**2/(2*HBAR)*val


def main():
    print('Experiment 03 R80 frequency-dependent dissipative bounce SCREEN')
    dat=isolated_bounce(DynamicForce(.6,quick=False),nfft=65536)
    print(f'cold xm={dat["xm"]:+.7f}, saddle={dat["xs"]:+.7f}, right={dat["xr"]:+.7f}, turning={dat["xt"]:+.7f}')
    print(f'fc={dat["wc"]/(2*math.pi)*1e-9:.6f} GHz, barrier/kB={dat["barrierK"]:.6f} K')
    print(f'isolated half-bounce extent s={dat["Shalf"]:.4f}')
    print(f'isolated action: K={dat["K"]:.6f}, V={dat["V"]:.6f}, K/V={dat["K"]/dat["V"]:.6f}')
    print(f'isolated B time-grid={dat["Btime"]:.6f}, exact quadrature={dat["Bquad"]:.6f}, relerr={(dat["Btime"]/dat["Bquad"]-1):+.3e}')
    cubic=7.2*(dat['barrierK']*KB)/(HBAR*dat['wc'])
    print(f'old cubic exponent 7.2*DeltaU/(hbar wc)={cubic:.6f}; exact-isolated/cubic={dat["Bquad"]/cubic:.6f}')

    for R,alpha in [(80.,.90),(80.,.70),(150.,.80),(360.,3.0)]:
        b1=env_action_on_scaled_bounce(dat,R,alpha,1.0)
        def obj(loga):
            a=math.exp(loga)
            Biso=0.5*dat['Bquad']*(a+1/a)
            return Biso+env_action_on_scaled_bounce(dat,R,alpha,a)
        opt=minimize_scalar(obj,bounds=(math.log(.35),math.log(3.0)),method='bounded',
                            options={'xatol':2e-5})
        aopt=math.exp(float(opt.x)); Bvar=float(opt.fun)
        msg=(f'R={R:g} alpha={alpha:.2f}: Benv[isolated]={b1:.6f}; '
             f'B_first={dat["Bquad"]+b1:.6f}; '
             f'time-scale aopt={aopt:.5f}, B_var={Bvar:.6f}, '
             f'DeltaB_var={Bvar-dat["Bquad"]:.6f}, exp(-DeltaB)={math.exp(-(Bvar-dat["Bquad"])):.3e}')
        print(msg); print(f'::notice title=Experiment 03 dissipative bounce::{msg}')

    print('Interpretation: B_first is first-order in the environmental action on the isolated bounce; B_var is a restricted time-scale ansatz, not the exact nonlocal bounce. Large DeltaB means the old isolated MQT screen is not self-consistent for that environment.')
    print('PASS')

if __name__=='__main__': main()
