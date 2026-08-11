import numpy as np


def basis(n):
    ref=np.array([1.,0.,0.]) if abs(n[0])<.9 else np.array([0.,1.,0.])
    e1=ref-np.dot(ref,n)*n; e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
    return ((np.outer(e1,e1)-np.outer(e2,e2))/np.sqrt(2),
            (np.outer(e1,e2)+np.outer(e2,e1))/np.sqrt(2),
            (np.outer(e1,n)+np.outer(n,e1))/np.sqrt(2),
            (np.outer(e2,n)+np.outer(n,e2))/np.sqrt(2),
            (2*np.outer(n,n)-np.outer(e1,e1)-np.outer(e2,e2))/np.sqrt(6))


def modes(rng,m):
    d=3*len(m); q,_=np.linalg.qr(rng.normal(size=(d,d)))
    return (np.repeat(1/np.sqrt(m),3)[:,None]*q).T.reshape(d,len(m),3)


def quadrupoles(m,x,w):
    out=np.zeros((len(w),3,3)); eye=np.eye(3)
    for k,u in enumerate(w):
        for ma,xa,ua in zip(m,x,u):
            out[k]+=ma*(np.outer(ua,xa)+np.outer(xa,ua)-2*eye*np.dot(ua,xa)/3)
    return out


def main():
    rng=np.random.default_rng(20260810); worst=0.; sat=0.
    for _ in range(80):
        m=np.exp(rng.normal(size=rng.integers(3,9))); x=rng.normal(size=(len(m),3))
        x-=np.sum(m[:,None]*x,axis=0)/m.sum(); n=rng.normal(size=3); n/=np.linalg.norm(n)
        I2=np.sum(m*np.sum(x*x,axis=1)); Z=np.sum(m*(x@n)**2); J=I2-Z
        q=quadrupoles(m,x,modes(rng,m)); E=basis(n)
        s=np.array([sum(np.sum(np.einsum('nij,ij->n',q,e)**2) for e in E[:2]),
                    sum(np.sum(np.einsum('nij,ij->n',q,e)**2) for e in E[2:4]),
                    np.sum(np.einsum('nij,ij->n',q,E[4])**2)])
        expected=np.array([4*J,2*J+4*Z,2*J/3+8*Z/3])
        err=np.max(np.abs(s-expected)); worst=max(worst,err)
        if not np.allclose(s,expected,rtol=2e-12,atol=2e-12): raise AssertionError((s,expected))
        if not np.isclose(np.sum(q*q),(20/3)*I2,rtol=2e-12,atol=2e-12): raise AssertionError('20/3')
        # Far-zone source coefficient: (25/16)*(1/5)*sum |Pi_2 q|^2 = (5/4) J.
        lhs=(25/16)*s[0]/5; rhs=5*J/4; sat=max(sat,abs(lhs-rhs))
        if not np.isclose(lhs,rhs,rtol=2e-12,atol=2e-12): raise AssertionError('5/4')
    print(f'worst sector Parseval absolute error = {worst:.12g}')
    print(f'worst exact 5/4 saturation error = {sat:.12g}')
    print('PASS: scalar and STF-sector gravitational endpoint resources')


if __name__=='__main__': main()
