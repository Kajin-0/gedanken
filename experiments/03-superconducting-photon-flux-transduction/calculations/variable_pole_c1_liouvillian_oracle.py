#!/usr/bin/env python3
"""Dense finite-mode implementation oracle for the C.1 coupled-Lindblad generator."""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.sparse.linalg import expm_multiply


def destroy(d):
    a=np.zeros((d,d),complex)
    for n in range(1,d): a[n-1,n]=np.sqrt(n)
    return a

def kron_all(xs):
    z=np.array([[1.+0j]])
    for x in xs: z=np.kron(z,x)
    return z

def embed(op,site,dims):
    return kron_all([op if j==site else np.eye(d, dtype=complex) for j,d in enumerate(dims)])

def comm(H,rho): return -1j*(H@rho-rho@H)

def dissipator(c,rho):
    n=c.conj().T@c
    return c@rho@c.conj().T-.5*(n@rho+rho@n)

def liouvillian_from_collapses(H,cs):
    D=H.shape[0]; I=np.eye(D,dtype=complex)
    L=-1j*(np.kron(I,H)-np.kron(H.T,I))
    for c in cs:
        n=c.conj().T@c
        L += np.kron(c.conj(),c)-.5*np.kron(I,n)-.5*np.kron(n.T,I)
    return L

def master_rhs(H,cs,rho):
    z=comm(H,rho)
    for c in cs: z+=dissipator(c,rho)
    return z

def direct_kossakowski(Gamma,bs,rho):
    z=np.zeros_like(rho)
    K=len(bs)
    for j in range(K):
        for k in range(K):
            q=bs[j].conj().T@bs[k]
            z += 2*Gamma[j,k]*(bs[k]@rho@bs[j].conj().T-.5*(q@rho+rho@q))
    return z

def adjoint_dissipator(c,O):
    n=c.conj().T@c
    return c.conj().T@O@c-.5*(n@O+O@n)

def rel(a,b): return float(np.linalg.norm(a-b)/max(np.linalg.norm(b),1e-300))

def main():
    # Deterministic two-mode physical realization with complex damping mixing.
    Hb=np.array([[.73,.21-.08j],[.21+.08j,1.31]],complex)
    Lc=np.array([[.37,0],[.09+.04j,.28]],complex)
    Gamma=Lc@Lc.conj().T
    d=4; dims_aux=[d,d]; bs=[embed(destroy(d),j,dims_aux) for j in range(2)]
    Haux=sum(Hb[j,k]*bs[j].conj().T@bs[k] for j in range(2) for k in range(2))
    cs=[]
    for mu in range(2):
        cs.append(np.sqrt(2.)*sum(np.conj(Lc[j,mu])*bs[j] for j in range(2)))

    # 1) Collective collapses vs direct dense Kossakowski action on a fixed rho.
    rng=np.random.default_rng(20260817)
    X=rng.normal(size=(d*d,d*d))+1j*rng.normal(size=(d*d,d*d)); rho=X@X.conj().T; rho/=np.trace(rho)
    dc=sum(dissipator(c,rho) for c in cs); dk=direct_kossakowski(Gamma,bs,rho)
    kerr=rel(dc,dk)

    # 2) Adjoint first-moment drift on the interior Fock subspace.  Truncation of
    # b at n=d-1 modifies the operator identity only on the top boundary, so
    # project all modes onto n<=d-2 before comparison.
    P1=np.diag([1.]*(d-1)+[0.]); P=kron_all([P1,P1])
    drift=-1j*Hb-Gamma; derr=0.
    for j,bj in enumerate(bs):
        got=1j*(Haux@bj-bj@Haux)+sum(adjoint_dissipator(c,bj) for c in cs)
        want=sum(drift[j,k]*bs[k] for k in range(2))
        derr=max(derr,rel(P@got@P,P@want@P))

    # 3) Column-major vectorization oracle on a small coupled system+two-mode model.
    ds=2; dims=[ds,d,d]
    sx=np.array([[0,1],[1,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
    Sx=embed(sx,0,dims); Sz=embed(sz,0,dims)
    B=[embed(destroy(d),j+1,dims) for j in range(2)]
    H=.41*Sz
    H+=sum(Hb[j,k]*B[j].conj().T@B[k] for j in range(2) for k in range(2))
    g=np.array([.17+.03j,-.06+.02j])
    A=sum(g[j]*B[j].conj().T+np.conj(g[j])*B[j] for j in range(2)); H+=Sx@A
    Cfull=[np.sqrt(2.)*sum(np.conj(Lc[j,mu])*B[j] for j in range(2)) for mu in range(2)]
    Lv=liouvillian_from_collapses(H,Cfull)
    psi=np.zeros(np.prod(dims),complex); psi[0]=1.; rho0=np.outer(psi,psi.conj())
    v0=rho0.reshape(-1,order='F')
    times=(.03,.11,.37); maxprop=0.; maxtr=0.; maxanti=0.
    for t in times:
        vv=expm_multiply(Lv*t,v0); rv=vv.reshape(rho0.shape,order='F')
        def rhs(_t,v):
            r=v.reshape(rho0.shape,order='F'); return master_rhs(H,Cfull,r).reshape(-1,order='F')
        sol=solve_ivp(rhs,(0,t),v0,t_eval=[t],method='DOP853',rtol=2e-12,atol=2e-14)
        rd=sol.y[:,-1].reshape(rho0.shape,order='F')
        maxprop=max(maxprop,rel(rv,rd)); maxtr=max(maxtr,abs(np.trace(rv)-1)); maxanti=max(maxanti,np.linalg.norm(rv-rv.conj().T,'fro'))

    print(f'C1_LIOUVILLIAN_ORACLE kossakowski_rel={kerr:.12e} first_moment_rel={derr:.12e} propagation_rel={maxprop:.12e} trace_err={maxtr:.12e} antiherm={maxanti:.12e}',flush=True)
    if kerr>=1e-12: raise RuntimeError('collective collapse / Kossakowski mismatch')
    if derr>=1e-12: raise RuntimeError('first-moment drift mismatch')
    if maxprop>=1e-11: raise RuntimeError('vectorization propagation mismatch')
    if maxtr>=1e-11 or maxanti>=1e-11: raise RuntimeError('dense propagation physicality mismatch')
    print('VARIABLE_POLE_C1_LIOUVILLIAN_ORACLE_PASS')
if __name__=='__main__': main()
