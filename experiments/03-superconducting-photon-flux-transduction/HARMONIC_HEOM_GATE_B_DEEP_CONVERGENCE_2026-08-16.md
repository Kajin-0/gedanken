# Experiment 03 — Harmonic Direct-Port HEOM Gate B Deep Convergence — 2026-08-16

## Status

**Method validation only. Not a detector-efficiency result.**

This checkpoint extends and supersedes the *active/pending* portions of
`HARMONIC_HEOM_GATE_B_2026-08-16.md`. The older file remains provenance for the
initial Matsubara hierarchy and staged-solver work.

Current gate disposition at this checkpoint:

```text
Gate A: direct-port bath correlation             PASS
Gate B: harmonic HEOM versus exact cold FDT      ACTIVE / NOT YET PASSED
Gate C: nonlinear cold/metastable HEOM           BLOCKED ON B
Gate D: finite-pulse nonlinear HEOM              BLOCKED
Gate E: exact/open versus N=8192 TWA             BLOCKED
```

Do not weaken Gate B merely because second moments agree. The controlling test
now includes reduced-state positivity and the full Gaussian equilibrium
eigenspectrum.

## 1. Fixed physical benchmark

Certified `.212` electrical point:

```text
delta       = .212
C           = 24.262211 pF
R           = 7.5308506 ohm
fc          = 1.984426698 GHz
alpha       = omega_D/omega_c = .90
```

Direct passive port:

```text
Re Y(omega) = (1/R) / [1 + (omega/omega_D)^4]
```

Exact harmonic cold-FDT widths:

```text
sigma_x = 3.9899698572e-2
sigma_u = 4.2646690208e-2
sigma0  = 4.01157261977e-2   # isolated oscillator vacuum width
```

The Caldeira-Leggett counterterm is retained. Its dimensionless coefficient is

```text
counterterm / omega_c = 43.395916715
```

The no-counterterm control misses the exact covariance by up to about 9.16%, so
the counterterm convention is physically discriminating and remains fixed.

## 2. N_Mats=16, depth-4 brute-force result

The first `N_Mats=16,d=4` time-domain job hit the default ZVODE internal-step
ceiling, not a physics failure. The exact same model was retried with a larger
integrator step budget.

```text
workflow: experiment03-heom-n16d4-retry.yml
run:      31980012630
job:      95245166232
```

Result, `dim=8`, `N_Mats=16`, `depth=4`, estimated 7315 ADOs:

```text
rel sigma_x     = +1.748247e-05
rel sigma_u     = +7.694695e-06
max width error = 1.748247e-05
min eig(rho)    = -6.707929e-05
top basis pop   = +2.406766e-06
runtime         = 657.680 s
```

Thus increasing hierarchy depth again improves the exact-FDT moments and reduces
the depth-3 `~1.15e-4` negativity, but does not restore positivity.

## 3. Omitted-Matsubara-tail terminator control

For the exact custom direct-port Matsubara coefficients, the omitted fast-tail
integral gives approximately

```text
Delta_8  = -6.683435593292e-03
Delta_16 = -9.183240118494e-04
```

A Markovian double-commutator tail correction was applied without changing the
physical spectral density.

Representative controls:

```text
N8,  d3 + tail: max width err = 4.818986e-05
                min eig       = -1.147857e-04

N16, d3 + tail: max width err = 4.737393e-05
                min eig       = -1.147797e-04
```

Conclusion:

```text
The omitted Matsubara correlation tail is not the primary source of the
finite-tier density-matrix negativity.
```

## 4. Matrix-free Schur hierarchy closure

A finite-hierarchy Schur-complement closure was implemented using the same
nearest-neighbor HEOM blocks as pinned QuTiP 5.3:

```text
calculations/heom_harmonic_schur_closure.py
.github/workflows/experiment03-heom-schur-closure.yml
run 31982711076
```

The key implementation validation is structural:

```text
Schur depth 1 ~= ordinary zero-tail depth 2
Schur depth 2 ~= ordinary zero-tail depth 3
```

including both covariance and the finite-tier negative eigenvalue. Example:

```text
N8 Schur d1: relx=-9.115944e-4, relu=-1.137475e-3,
             min eig=+2.044258e-4

N8 Schur d2: relx=+4.839629e-4, relu=+6.405060e-4,
             min eig=-1.332862e-4
```

Therefore the Schur implementation is behaving as a controlled one-tier
accelerator for this problem, but it is not by itself positivity preserving.
The residual defect cannot be dismissed as a sign error in the hierarchy
coupling.

## 5. Direct-port Bose-Pade bath compression

The thermal Matsubara ladder was replaced by the optimized Bose-Pade thermal
poles used in QuTiP's Padé environment decomposition, while keeping the exact
two circuit poles and the same physical `J(omega)`.

Canonical validation:

```text
calculations/direct_port_bath_pade.py
.github/workflows/experiment03-direct-port-pade.yml
```

Independent oscillatory quadrature versus the 10,000-term Matsubara reference:

```text
max relative disagreement = 2.445310e-09
```

Padé correlation convergence:

| N_Pade | max rel error, t>=20 ps |
|---:|---:|
| 1 | 6.970373e-2 |
| 2 | 2.566195e-3 |
| 3 | 6.329125e-4 |
| 4 | 1.955043e-4 |
| 5 | 2.620749e-5 |
| 6 | 3.808400e-6 |
| 8 | 8.099921e-7 |

For `N_Pade=8`, the maximum error for `t>=1 ps` is `3.880794e-5`.

Disposition:

```text
N_Pade=8 is the strict correlation-certified reference.
N_Pade=4--6 are controlled lower-order hierarchy-convergence candidates only.
```

No detector conclusion is inferred from bath compression itself.

## 6. Deep Padé HEOM hierarchy sweep

Canonical code/workflow:

```text
calculations/heom_harmonic_pade_depth.py
.github/workflows/experiment03-heom-pade-depth.yml
run 31982972155
```

All cases below use `dim=8`.

| case | N_Pade | depth | max FDT width err | min eig(rho) |
|---|---:|---:|---:|---:|
| p4d3 | 4 | 3 | 1.987765e-4 | -1.075005e-4 |
| p4d4 | 4 | 4 | ~1.5e-5 | -6.713646e-5 |
| p4d5 | 4 | 5 | 1.081598e-5 | -6.930681e-7 |
| p4d6 | 4 | 6 | 2.596516e-6 | -8.937236e-7 |
| p5d5 | 5 | 5 | 1.085068e-5 | -6.930622e-7 |
| p6d5 | 6 | 5 | 1.084984e-5 | -6.930612e-7 |
| p8d4 | 8 | 4 | 1.503996e-5 | -6.713646e-5 |

Key conclusions:

1. `N_Pade=4,5,6` at depth 5 agree in the minimum eigenvalue at approximately
   the `1e-12` level. The depth-5 residual is not a low-Padé-order artifact.
2. The strict `N_Pade=8,d=4` reference reproduces the `N_Pade=4,d=4` state.
3. Hierarchy depth is the dominant control of the large positivity defect.
4. The negativity collapses by about two orders of magnitude between depths 4
   and 5, but the depth-5/6 sign floor is non-monotonic.

## 7. Independent refinement axes

Canonical workflow:

```text
.github/workflows/experiment03-heom-pade-refine.yml
run 31983104350
```

### 7.1 100x tighter ODE tolerance

At `N_Pade=5,d=5,dim=8`, tightening the ODE tolerances by 100x gives

```text
min eig(rho) = -6.930623e-7
```

essentially unchanged from the standard-tolerance result.

Therefore the residual is not an ODE-integration tolerance artifact.

### 7.2 Larger oscillator basis

At `N_Pade=5,d=5,dim=10`:

```text
rel sigma_x     = +2.241183e-06
rel sigma_u     = +1.545972e-06
max width error = 2.241183e-06
min eig(rho)    = -9.125667e-07
top basis pop   = -1.070055e-07
```

Therefore the depth-5 sign defect is not simply the `dim=8` basis boundary.

### 7.3 Deeper hierarchy

At `N_Pade=4,d=7,dim=8`:

```text
rel sigma_x     = -2.504298e-07
rel sigma_u     = -6.558955e-07
max width error = 6.558955e-07
late drift      = 7.404220e-07
min eig(rho)    = -4.249847e-07
top basis pop   = +1.097560e-07
```

The covariance is now sub-ppm accurate. The remaining sign error is small but is
still not accepted as machine epsilon.

The observed sign sequence is approximately

```text
d3: -1.075e-4
d4: -6.714e-5
d5: -6.931e-7
d6: -8.937e-7
d7: -4.250e-7
```

so strict positivity has not yet shown a monotone convergence certificate.

## 8. Exact Gaussian eigenspectrum benchmark

For this exact linear one-mode equilibrium problem, the reduced state is
Gaussian. With the current `(x,u)` convention,

```text
symplectic ratio = sigma_x sigma_u / sigma0^2 = 1.057366700830
nbar             = 0.0286833504148
q                = 0.02788355659031
```

The exact density-operator eigenvalue ladder therefore begins

```text
p0 = 9.721164434097e-1
p1 = 2.710606386219e-2
p2 = 7.558134656418e-4
p3 = 2.107476754094e-5
p4 = 5.876394733555e-7
p5 = 1.638547851001e-8
p6 = 4.568854172931e-10
p7 = 1.273959038838e-11
```

Canonical workflow:

```text
calculations/heom_harmonic_eigenspectrum.py
.github/workflows/experiment03-heom-eigenspectrum.yml
run 31983321235
```

### 8.1 Depth-5, dim-10 result

At `N_Pade=5,d=5,dim=10`:

```text
negative mass     = 1.769743565910e-6
spectral L1       = 7.059141140120e-5
spectral TV       = 3.529570570060e-5
min eig           = -9.125666955350e-7
```

Critically, the exact `p3=2.10748e-5` weight is represented as only
`8.99578e-6`, a 57.3% relative error. Thus excellent covariance agreement at
this tier does not imply an accurate physical reduced state.

### 8.2 Depth-7, dim-8 result

At `N_Pade=4,d=7,dim=8`:

```text
negative mass     = 4.249847428170e-7
spectral L1       = 2.755914214558e-6
spectral TV       = 1.377957107279e-6
min eig           = -4.249847428170e-7
```

Leading exact versus HEOM eigenweights:

| rank | exact | HEOM | relative error |
|---:|---:|---:|---:|
| 0 | 9.721164434097e-1 | 9.721167740201e-1 | 3.40e-7 |
| 1 | 2.710606386219e-2 | 2.710567622159e-2 | 1.43e-5 |
| 2 | 7.558134656418e-4 | 7.553368837665e-4 | 6.31e-4 |
| 3 | 2.107476754094e-5 | 2.196825895427e-5 | 4.24e-2 |
| 4 | 5.876394733555e-7 | 4.989026900794e-7 | 1.51e-1 |

The full spectrum therefore improves dramatically between depths 5 and 7, but
the final dim-8 tail eigenvalue remains negative.

## 9. Final predeclared brute-force hierarchy matrix — RUNNING

The last raw-depth matrix is deliberately bounded at depth 9:

```text
calculations/heom_harmonic_pade_final_depth.py
.github/workflows/experiment03-heom-pade-final-depth.yml
run 31983405446

cases:
  N_Pade=4, depth=8, dim=8
  N_Pade=4, depth=9, dim=8
  N_Pade=5, depth=7, dim=8
```

Acceptance rule was fixed before reading these results:

```text
Require a stable approach to the exact positive Gaussian state across adjacent
hierarchy depths and Padé orders. Do not declare success from one accidentally
positive tier.
```

No raw depth greater than 9 is authorized by this checkpoint. If this final
matrix still gives an oscillatory `O(1e-7)` sign floor or an unconverged occupied
spectrum, Gate B remains open and the next method must be an independent
physical embedding / controlled alternate open-system solver rather than simply
adding more zero-tail hierarchy tiers.

If the sign does stabilize, perform one final full density-matrix comparison to
the exact squeezed thermal Gaussian state before promoting Gate B.

## 10. Current scientific conclusion

The direct-port bath mapping has survived increasingly severe checks:

- exact analytic correlation versus independent oscillatory quadrature;
- exact FDT covariance;
- decisive counterterm control;
- Matsubara-order and Padé-order convergence;
- omitted-correlation-tail control;
- hierarchy Schur-closure cross-check;
- Hilbert-basis refinement;
- ODE-tolerance refinement;
- full exact-Gaussian eigenspectrum comparison.

The remaining issue is narrow but real: finite-tier HEOM produces a small
nonpositive far-tail sector even after the physically occupied spectrum and FDT
moments have substantially converged.

Therefore, at this checkpoint:

```text
Gate B remains ACTIVE.
Gate C remains BLOCKED.
No nonlinear HEOM detector-efficiency claim is authorized.
```
