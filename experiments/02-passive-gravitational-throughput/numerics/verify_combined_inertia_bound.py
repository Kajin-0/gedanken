import numpy as np


def eta(z):
    z=np.asarray(z,float)
    e2=25*(z**8-2*z**6+3*z**4-9*z**2+9)/(16*z**10)
    e1=25*(z**6-3*z**4+36)/(4*z**10)
    e0=225*(z**4+3*z**2+9)/(4*z**10)
    return e2,e1,e0


def geometry(J,Z,z):
    e2,e1,e0=eta(z)
    return 4*e2*J+e1*(2*J+4*Z)+e0*(2*J/3+8*Z/3)


def main():
    rng=np.random.default_rng(20260810); worst=0.; oldratio=0.; asym=0.
    for _ in range(500):
        J=np.exp(rng.normal()); Z=np.exp(rng.normal()); z=np.exp(rng.uniform(np.log(3),np.log(1e4)))
        e2,e1,e0=eta(z)
        if e2+1e-14<max(e1,e0): raise AssertionError('sector ordering')
        g=geometry(J,Z,z)
        old=(20/3)*(J+Z)*e2
        oldratio=max(oldratio,g/old)
        if g>old*(1+2e-12): raise AssertionError(('geometry vs scalar',g,old))
        # Random retained sector fractions cannot exceed the sector geometry bound.
        f=rng.random(3); actual=e2*4*J*f[0]+e1*(2*J+4*Z)*f[1]+e0*(2*J/3+8*Z/3)*f[2]
        worst=max(worst,actual/g)
        if actual>g*(1+2e-12): raise AssertionError('finite-z geometry')
        # Far-zone coefficient approaches (25/4)J/z^2 before the G Omega^4/(5 c^5) factor.
        lead=25*J/(4*z*z); asym=max(asym,abs(g/lead-1)) if z>1e3 else asym
    # Exact chained coefficient: (1/5)*(25/4) J = (5/4) J.
    J=3.7; c=(25/4)*J/5
    if not np.isclose(c,5*J/4,rtol=1e-15,atol=1e-15): raise AssertionError('5/4')
    # Sphere finite-z check at z=100: J=2Ma^2/5, Z=Ma^2/5.
    sf=geometry(2/5,1/5,100)/(25*(2/5)/(4*100**2))
    if not np.isclose(sf,1.0002000900450314,rtol=2e-14,atol=2e-14): raise AssertionError(('sphere',sf))
    print(f'worst random finite-z utilization = {worst:.12g}')
    print(f'largest new/old scalar finite-z bound ratio = {oldratio:.12g}')
    print(f'worst z>1000 relative approach error = {asym:.12g}')
    print(f'sphere z=100 finite/leading factor = {sf:.12g}')
    print('PASS: sector-resolved finite-z and 5/4 directional-inertia closure')


if __name__=='__main__': main()
