#!/usr/bin/env python3
"""Finite-temperature periodic nonlocal Euclidean bounce for Experiment 03.

This upgrades the zero-temperature spectral bounce to the actual bath temperature.
The cold rf-SQUID potential is fixed at T0, while the Euclidean time interval has
physical period beta*hbar.  In normalized time s=omega_c*tau,

    P = hbar*omega_c/(k_B*T).

Use an even periodic cosine basis including the constant mode,

    y(s)=a_0 + sum_{n=1}^N a_n cos(2*pi*n*s/P),

with y=x-x_m.  Translation is fixed by even parity.  The action is

    B = Ak/2 int y'^2 ds
        + Av int [u(x_m+y)-u(x_m)] ds
        + 1/2 a^T Kenv a,

where

    Ak = C Phi_bar^2 omega_c / hbar,
    Av = (Phi_bar^2/L)/(hbar omega_c).

For cosine mode n>0, exact periodic Matsubara normalization gives

    Kenv_nn = (Phi_bar^2/hbar)*(P/2)*k_n*Y_L(omega_c*k_n),

while the constant mode has no environmental term.

The static sphaleron is an exact stationary solution with action

    B_sph = DeltaU/(k_B*T).

Its first nonzero Matsubara mode changes sign at the dissipative crossover.
Below that crossover a one-negative-mode periodic saddle is continued down from
the first bifurcation.  Above it the static sphaleron is the one-negative-mode
thermal saddle.

This computes only the exponent/saddle structure.  It does NOT compute the
fluctuation determinant/prefactor or a physical dark-count rate.
"""
from __future__ import annotations

import argparse
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq, root

import full_dynamic_rfsquid as fd
from directional_recovery_barriers import directional_barriers
from R80_dissipative_bounce_screen import Y_laplace
from quantum_initial_capture import HBAR, KB, PHI_BAR

B_TARGET=37.61
ALPHA=.90
C0=215e-15
R0=80.0
L0=111.5e-12
B_BASE={
    .050:29.76563577,
    .180:7.58847205,
    .190:6.52571286,
    .200:5.52063406,
    .210:4.56802352,
    .220:3.65877371,
}


def design(delta:float):
    if delta not in B_BASE:
        raise ValueError(f'no exact base action for delta={delta}')
    r=B_TARGET/B_BASE[delta]
    C=C0*r*r
    R=R0/r
    return r,C,R


def static_model(delta:float,C:float,R:float):
    fd.BETA_COLD=.80
    fd.DELTA_TILT=float(delta)
    model=fd.DynamicForce(.6,quick=False,Tmax=.98)
    roots=model.roots(fd.T0)
    xm=max(x for x,kap in roots if x<0 and kap>0)
    xs=min((x for x,kap in roots if kap<0 and x>xm), key=lambda z:z-xm)
    xr=min((x for x,kap in roots if x>xs and kap>0), key=lambda z:z-xs)
    km=float(model.spline.ev(fd.T0,xm,dx=0,dy=1))
    Fs=float(model.spline.ev(fd.T0,xs,dx=0,dy=1))
    wc=math.sqrt(km/(L0*C))
    wd=ALPHA*wc
    b=directional_barriers(model,fd.T0)
    barrierK=b['b_left']*(PHI_BAR**2/L0)/KB

    xlo=max(float(model.xgrid[0]),xm-.25)
    xhi=min(float(model.xgrid[-1]),xr+.45)
    xgrid=np.linspace(xlo,xhi,70001)
    Fgrid=np.array([model.force(fd.T0,float(x)) for x in xgrid])
    Ugrid=cumulative_trapezoid(Fgrid,xgrid,initial=0.0)
    Ugrid-=float(np.interp(xm,xgrid,Ugrid))
    dFgrid=np.gradient(Fgrid,xgrid)
    Fv=lambda x:np.interp(x,xgrid,Fgrid,left=Fgrid[0],right=Fgrid[-1])
    Uv=lambda x:np.interp(x,xgrid,Ugrid,left=Ugrid[0],right=Ugrid[-1])
    dFv=lambda x:np.interp(x,xgrid,dFgrid,left=dFgrid[0],right=dFgrid[-1])
    return dict(model=model,xm=xm,xs=xs,xr=xr,km=km,Fs=Fs,wc=wc,wd=wd,
                barrierK=barrierK,Fv=Fv,Uv=Uv,dFv=dFv,C=C,R=R)


def exact_crossover(st):
    C,R,wc,wd,Fs=st['C'],st['R'],st['wc'],st['wd'],st['Fs']
    def lam(T):
        nu=2*math.pi*KB*T/HBAR
        return C*nu*nu + nu*float(Y_laplace(nu,R,wd)) + Fs/L0
    Tx=brentq(lam,1e-6,.5,xtol=2e-14,rtol=2e-13,maxiter=400)
    return Tx,lam


def periodic_system(st,T:float,nbasis:int=48,ngrid:int=6144):
    wc=st['wc']; C=st['C']; R=st['R']; wd=st['wd']; xm=st['xm']
    P=HBAR*wc/(KB*T)
    s=np.linspace(-P/2,P/2,ngrid,endpoint=False)
    ds=float(s[1]-s[0])
    n=np.arange(nbasis+1)
    k=2*math.pi*n/P
    B=np.empty((ngrid,nbasis+1))
    B[:,0]=1.0
    if nbasis:
        B[:,1:]=np.cos(np.outer(s,k[1:]))
    norms=np.full(nbasis+1,P/2); norms[0]=P

    Ak=C*PHI_BAR**2*wc/HBAR
    Av=(PHI_BAR**2/L0)/(HBAR*wc)
    Kkin=np.zeros(nbasis+1)
    Kkin[1:]=Ak*norms[1:]*k[1:]**2
    Kenv=np.zeros(nbasis+1)
    if nbasis:
        nu=wc*k[1:]
        Y=np.asarray(Y_laplace(nu,R,wd),dtype=float)
        Kenv[1:]=(PHI_BAR**2/HBAR)*norms[1:]*k[1:]*Y
    Kdiag=Kkin+Kenv

    Fv,Uv,dFv=st['Fv'],st['Uv'],st['dFv']
    def grad(a):
        x=xm+B@a
        return Kdiag*a + Av*(B.T@Fv(x))*ds
    def jac(a):
        x=xm+B@a
        W=dFv(x)
        return np.diag(Kdiag)+Av*(B.T@(W[:,None]*B))*ds
    def action(a):
        x=xm+B@a
        K=.5*float(np.sum(Kkin*a*a))
        E=.5*float(np.sum(Kenv*a*a))
        V=Av*float(np.sum(Uv(x))*ds)
        return K+E+V,K,E,V
    return dict(P=P,s=s,ds=ds,k=k,B=B,norms=norms,grad=grad,jac=jac,action=action,
                Av=Av,Kkin=Kkin,Kenv=Kenv)


def solve_stationary(sys,a0,maxfev=8000):
    sol=root(sys['grad'],np.asarray(a0,dtype=float),jac=sys['jac'],method='hybr',tol=2e-10,
             options={'xtol':2e-10,'maxfev':maxfev})
    a=np.asarray(sol.x,dtype=float)
    act,K,E,V=sys['action'](a)
    H=sys['jac'](a)
    ev=np.linalg.eigvalsh(H)
    return dict(a=a,B=act,K=K,E=E,V=V,success=bool(sol.success),
                grad=float(np.linalg.norm(sys['grad'](a),ord=np.inf)),ev=ev)


def sphaleron(st,T,nbasis=48,ngrid=6144):
    sys=periodic_system(st,T,nbasis,ngrid)
    a=np.zeros(nbasis+1); a[0]=st['xs']-st['xm']
    o=solve_stationary(sys,a)
    exact=st['barrierK']/T
    return sys,o,exact


def seed_periodic_branch(st,Tx,nbasis,ngrid):
    # Slightly below the bifurcation, where the static sphaleron has acquired a
    # second negative even mode and the first periodic branch should be nearby.
    Tseed=.94*Tx
    sys=periodic_system(st,Tseed,nbasis,ngrid)
    ys=st['xs']-st['xm']
    scale=max(st['xr']-st['xs'],st['xs']-st['xm'])
    candidates=[]
    for frac in (.015,.03,.06,.10,.16,.24,.34,.48):
        a=np.zeros(nbasis+1); a[0]=ys; a[1]=frac*scale
        o=solve_stationary(sys,a)
        nneg=int(np.sum(o['ev']<0))
        amp=float(np.max(np.abs(o['a'][1:])))
        if o['success'] and o['grad']<3e-7 and nneg==1 and amp>1e-5:
            candidates.append(o)
    if not candidates:
        raise RuntimeError('failed to seed one-negative-mode periodic branch below crossover')
    # The physical first-bounce branch has the lowest action among accepted
    # one-negative-mode stationary solutions near the bifurcation.
    best=min(candidates,key=lambda z:z['B'])
    return Tseed,sys,best


def project_coeffs(oldsys,olda,newsys):
    # Reconstruct the previous even periodic path in physical normalized s and
    # project it onto the new period.  Periodic evaluation avoids an artificial
    # discontinuity when the period changes during continuation.
    sold=oldsys['s']; Pold=oldsys['P']; Bold=oldsys['B']; yold=Bold@olda
    snew=newsys['s']
    sw=((snew+Pold/2)%Pold)-Pold/2
    order=np.argsort(sold)
    y=np.interp(sw,sold[order],yold[order],period=Pold)
    Bnew=newsys['B']; ds=newsys['ds']; norms=newsys['norms']
    return (Bnew.T@y)*ds/norms


def finiteT_bounce(st,Ttarget,Tx,nbasis=48,ngrid=6144):
    if Ttarget>=Tx:
        sys,o,exact=sphaleron(st,Ttarget,nbasis,ngrid)
        return dict(kind='sphaleron',T=Ttarget,Tx=Tx,sys=sys,o=o,Bsph_exact=exact,history=[])

    Tcur,sys,o=seed_periodic_branch(st,Tx,nbasis,ngrid)
    hist=[(Tcur,o['B'],int(np.sum(o['ev']<0)),o['grad'])]
    # Continue downward with enough steps that basis-period changes are gentle.
    nstep=max(8,int(math.ceil((Tcur-Ttarget)/max(.0015,.08*Ttarget))))
    temps=np.linspace(Tcur,Ttarget,nstep+1)[1:]
    for T in temps:
        newsys=periodic_system(st,float(T),nbasis,ngrid)
        a0=project_coeffs(sys,o['a'],newsys)
        no=solve_stationary(newsys,a0)
        nneg=int(np.sum(no['ev']<0))
        if (not no['success']) or no['grad']>1e-6 or nneg!=1:
            raise RuntimeError(f'periodic continuation failed at T={T:.6g}: success={no["success"]} grad={no["grad"]:.3e} nneg={nneg}')
        sys,o=newsys,no
        hist.append((float(T),o['B'],nneg,o['grad']))
    exact=st['barrierK']/Ttarget
    return dict(kind='periodic',T=Ttarget,Tx=Tx,sys=sys,o=o,Bsph_exact=exact,history=hist)


def run_delta(delta,nbasis,ngrid):
    r,C,R=design(delta)
    st=static_model(delta,C,R)
    Tx,lam=exact_crossover(st)
    # Exact sphaleron regression at the actual bath temperature, whether or not
    # it is the physical one-negative-mode escape saddle there.
    ssys,so,sexact=sphaleron(st,fd.T0,nbasis,ngrid)
    sph_rel=so['B']/sexact-1
    sph_nneg=int(np.sum(so['ev']<0))
    out=finiteT_bounce(st,fd.T0,Tx,nbasis,ngrid)
    o=out['o']; nneg=int(np.sum(o['ev']<0))
    center=st['xm']+float(np.sum(o['a'])) # cos(0)=1 for all modes
    msg=(f'delta={delta:.3f}: r={r:.7f} C={C*1e15:.3f}fF R={R:.4f}ohm '
         f'fc={st["wc"]/(2*math.pi)*1e-9:.5f}GHz Tx={Tx:.6f}K T0/Tx={fd.T0/Tx:.5f}; '
         f'sph_Bgrid={so["B"]:.7f} sph_exact={sexact:.7f} sph_rel={sph_rel:+.3e} sph_nneg={sph_nneg}; '
         f'physical={out["kind"]} B_T0={o["B"]:.7f} nneg={nneg} grad={o["grad"]:.2e} '
         f'center={center:+.6f} B_T0/B_zeroTarget={o["B"]/B_TARGET:.6f}')
    print(msg); print(f'::notice title=Experiment 03 finiteT periodic bounce::{msg}')
    if abs(sph_rel)>2e-3:
        raise RuntimeError('sphaleron action regression failed')
    if nneg!=1:
        raise RuntimeError('physical finite-T saddle does not have one negative even mode')
    if out['kind']=='periodic' and not (o['B']<sexact):
        raise RuntimeError('periodic saddle below crossover should lie below sphaleron action')
    if out['history']:
        print('  continuation: '+', '.join(f'T={T:.5f}:B={B:.5f}:nneg={nn}' for T,B,nn,g in out['history']))
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--delta',type=float,required=True)
    ap.add_argument('--nbasis',type=int,default=48)
    ap.add_argument('--ngrid',type=int,default=6144)
    a=ap.parse_args(); delta=round(a.delta,3)
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        run_delta(delta,a.nbasis,a.ngrid)
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
