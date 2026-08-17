#!/usr/bin/env python3
"""Export frozen Ns=16/24 metastable-window system matrices for Gate C.1."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import eigsh
import full_dynamic_rfsquid as fd
import phase_dvr_basis_convergence as dvr
import direct_port_bath_correlation as bc
from quantum_initial_capture import KB, PHI_BAR

DELTA=.21200; RSC=dvr.ROOTS[DELTA]; L=dvr.L0; C=dvr.C0*RSC*RSC; T0=fd.T0

def embed(x0,p,x):
    q=np.interp(x,x0,np.real(p),left=0,right=0)+1j*np.interp(x,x0,np.imag(p),left=0,right=0)
    dx=x[1]-x[0]; return q/math.sqrt(float(np.sum(abs(q)**2)*dx))

def build(nmax=24,xmax=4.2,ngrid=2600,nleft=12):
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA; fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02); roots=model.roots(T0)
        mins=[(x,k) for x,k in roots if k>0]; saddles=[(x,k) for x,k in roots if k<0]
        xm=max(x for x,k in mins if x<0); xs=min(saddles,key=lambda z:abs(z[0]))[0]
        km=float(np.asarray(model.spline.ev(T0,xm,dx=0,dy=1)).reshape(-1)[0]); wc=math.sqrt(km/(L*C))
        xl,_,el,vl,_=dvr.spectrum(model,T0,C,-3.8,xs,2200,nleft)
        p=np.exp(-(el-el[0])/(KB*T0)); p/=p.sum()
        x=np.linspace(-xmax,xmax,ngrid+2)[1:-1]; U,_=dvr.potential_J(model,T0,x); H,_=dvr.hamiltonian(U,x,C); dx=x[1]-x[0]
        Uleft=float(np.interp(xm,x,U)); target=Uleft+float(el[0])
        ev,v=eigsh(H,k=nmax,sigma=target,which='LM',tol=2e-12,maxiter=200000); ii=np.argsort(abs(ev-target)); ev=ev[ii]; v=v[:,ii]/math.sqrt(dx)
        y=x-xm; Y=v.conj().T@(y[:,None]*v)*dx; Y2=v.conj().T@((y*y)[:,None]*v)*dx; PL=v.conj().T@(((x<xs).astype(float))[:,None]*v)*dx
        Y=(Y+Y.conj().T)/2; Y2=(Y2+Y2.conj().T)/2; PL=(PL+PL.conj().T)/2
        psi=np.column_stack([embed(xl,vl[:,j],x) for j in range(nleft)]); coeff=v.conj().T@psi*dx
        lam=(PHI_BAR**2/bc.HBAR)*bc.G*bc.WD/(2*math.sqrt(2))/wc
        out={}
        meta=dict(delta=DELTA,r=RSC,C_F=C,xm=xm,xs=xs,wc_rad_s=wc,target_energy_J=target,counterterm_lambda=lam,left_weights=p.tolist())
        for n in (16,24):
            c=coeff[:n]; rho=(c*p[None,:])@c.conj().T; rho=(rho+rho.conj().T)/2; rho/=np.trace(rho)
            H0=np.diag((ev[:n]-target)/(bc.HBAR*wc)).astype(complex)
            Hsys=H0+lam*Y2[:n,:n]
            out[f'H0_{n}']=H0; out[f'Hsys_{n}']=Hsys; out[f'Y_{n}']=Y[:n,:n]; out[f'Y2_{n}']=Y2[:n,:n]; out[f'PL_{n}']=PL[:n,:n]; out[f'rhoL_{n}']=rho
            meta[str(n)]=dict(trace=float(np.trace(rho).real),PL=float(np.trace(rho@PL[:n,:n]).real),mean_y=float(np.trace(rho@Y[:n,:n]).real),sigma_y=float(np.sqrt(max((np.trace(rho@Y2[:n,:n]).real)-(np.trace(rho@Y[:n,:n]).real)**2,0))),Hsys_herm_rel=float(np.linalg.norm(Hsys-Hsys.conj().T)/max(np.linalg.norm(Hsys),1e-300)))
        out.update(wc=np.array(wc),xm=np.array(xm),xs=np.array(xs),target=np.array(target),counterterm_lambda=np.array(lam),energies=ev)
        return out,meta
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--npz',default='variable_pole_c1_system.npz'); ap.add_argument('--json',default='variable_pole_c1_system.json'); a=ap.parse_args()
    out,meta=build(); np.savez_compressed(a.npz,**out); Path(a.json).write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
    print(f'C1_SYSTEM_EXPORT Ns16_PL={meta["16"]["PL"]:.12e} Ns24_PL={meta["24"]["PL"]:.12e} lambda={meta["counterterm_lambda"]:.12e}')
    if max(meta['16']['Hsys_herm_rel'],meta['24']['Hsys_herm_rel'])>=1e-12: raise RuntimeError('system Hamiltonian non-Hermitian')
    print('VARIABLE_POLE_C1_SYSTEM_EXPORT_PASS')
if __name__=='__main__': main()
