#!/usr/bin/env python3
"""Static metastable-energy-window basis preflight for variable-pole Gate C.1."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import eigsh
import full_dynamic_rfsquid as fd
import phase_dvr_basis_convergence as dvr
from quantum_initial_capture import KB

DELTA=.21200; RSC=dvr.ROOTS[DELTA]; L=dvr.L0; C=dvr.C0*RSC*RSC; T0=fd.T0
CANDIDATES=(8,12,16,24,32,48,64,80,96,128)

def embed(x0,p,x):
    q=np.interp(x,x0,np.real(p),left=0,right=0)+1j*np.interp(x,x0,np.imag(p),left=0,right=0)
    dx=x[1]-x[0]; q/=math.sqrt(float(np.sum(abs(q)**2)*dx)); return q

def boltz(e):
    p=np.exp(-(e-e[0])/(KB*T0)); return p/p.sum()

def project(v,f,dx): return v.conj().T@f*dx
def retained(c,p,n): return float(np.dot(p,np.sum(abs(c[:n])**2,axis=0)))

def run(kmax,xmax,ngrid,nleft):
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA; fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        roots=model.roots(T0); mins=[(x,k) for x,k in roots if k>0]; saddles=[(x,k) for x,k in roots if k<0]
        xm=max(x for x,k in mins if x<0); xr=min(x for x,k in mins if x>0); xs=min(saddles,key=lambda z:abs(z[0]))[0]
        km=float(np.asarray(model.spline.ev(T0,xm,dx=0,dy=1)).reshape(-1)[0]); wc=math.sqrt(km/(L*C))
        xl,_,el,vl,resl=dvr.spectrum(model,T0,C,-3.8,xs,2200,nleft); p=boltz(el)
        x=np.linspace(-xmax,xmax,ngrid+2)[1:-1]; U,_=dvr.potential_J(model,T0,x); H,_=dvr.hamiltonian(U,x,C); dx=x[1]-x[0]
        Uleft=float(np.interp(xm,x,U)); target=Uleft+float(el[0])
        ev,v=eigsh(H,k=kmax,sigma=target,which='LM',tol=2e-12,maxiter=200000)
        ii=np.argsort(abs(ev-target)); ev=ev[ii]; v=v[:,ii]
        res=np.array([np.linalg.norm(H@v[:,j]-ev[j]*v[:,j])/KB for j in range(kmax)]); v=v/math.sqrt(dx)
        psi=np.column_stack([embed(xl,vl[:,j],x) for j in range(nleft)]); y=x-xm
        fs=(psi,y[:,None]*psi,(y*y)[:,None]*psi); cs=tuple(project(v,f,dx) for f in fs)
        exact=tuple(float(np.dot(p,np.sum(abs(f)**2,axis=0)*dx)) for f in fs)
        Y=v.conj().T@(y[:,None]*v)*dx; Y2=v.conj().T@((y*y)[:,None]*v)*dx; PL=v.conj().T@(((x<xs).astype(float))[:,None]*v)*dx
        Y=(Y+Y.conj().T)/2; Y2=(Y2+Y2.conj().T)/2; PL=(PL+PL.conj().T)/2
        rows=[]
        for n in CANDIDATES:
            if n>kmax: continue
            c=cs[0][:n]; rho=(c*p[None,:])@c.conj().T; tr=float(np.trace(rho).real); rho=(rho+rho.conj().T)/(2*tr)
            r0=tr/exact[0]; r1=retained(cs[1],p,n)/exact[1]; r2=retained(cs[2],p,n)/exact[2]
            pl=float(np.trace(rho@PL[:n,:n]).real); my=float(np.trace(rho@Y[:n,:n]).real); my2=float(np.trace(rho@Y2[:n,:n]).real); sy=math.sqrt(max(my2-my*my,0)); top=float(rho[-1,-1].real)
            rows.append(dict(basis_dim=n,prep_loss=max(0.,1-r0),y_loss=max(0.,1-r1),y2_loss=max(0.,1-r2),left_basin=pl,mean_y=my,sigma_y=sy,top_population=top,energy_span_K=float((max(ev[:n])-min(ev[:n]))/KB),max_target_detuning_K=float(max(abs(ev[:n]-target))/KB)))
            print(f'C1_RESONANT_BASIS dim={n} prepLoss={1-r0:.12e} yLoss={1-r1:.12e} y2Loss={1-r2:.12e} PL={pl:.12e} sigmaY={sy:.12e} topPop={top:.12e} spanK={(max(ev[:n])-min(ev[:n]))/KB:.6e}',flush=True)
        return dict(purpose='metastable-window static basis preflight',nonlinear_open_dynamics_used=False,delta=DELTA,r=RSC,xm=xm,xs=xs,xr=xr,wc_rad_s=wc,target_energy_K=target/KB,left_min_offset_K=Uleft/KB,left_ground_local_K=el[0]/KB,left_weights=p.tolist(),max_left_residual_K=float(max(resl)),max_full_residual_K=float(max(res)),target_eigen_energies_K=(ev/KB).tolist(),rows=rows)
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--kmax',type=int,default=128); ap.add_argument('--xmax',type=float,default=4.2); ap.add_argument('--ngrid',type=int,default=2600); ap.add_argument('--left-states',type=int,default=12); ap.add_argument('--json',default='variable_pole_c1_resonant_basis_preflight.json'); a=ap.parse_args()
    out=run(a.kmax,a.xmax,a.ngrid,a.left_states); Path(a.json).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    if max(out['max_left_residual_K'],out['max_full_residual_K'])>2e-7: raise RuntimeError('eigen residual regression')
    print(f'C1_RESONANT_BASIS_JSON={a.json}'); print('VARIABLE_POLE_C1_RESONANT_BASIS_PREFLIGHT_PASS')
if __name__=='__main__': main()
