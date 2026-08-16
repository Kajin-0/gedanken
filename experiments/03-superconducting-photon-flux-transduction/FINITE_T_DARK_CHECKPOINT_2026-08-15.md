# Experiment 03 — Finite-temperature dark-action checkpoint — 2026-08-15

## Status

**Canonical dark-physics checkpoint.**

The previous optimization manifold that held the **zero-temperature** nonlocal bounce action at `B=37.61` is no longer the correct dark constraint at the actual bath temperature `T0=20 mK`.

A finite-period, same-environment nonlocal Euclidean solver has now been implemented and converged. The accepted reduced-model constraint is

\[
\boxed{B_{20\,\mathrm{mK}}=37.61}
\]

for the metastable dark state, subject to the still-unresolved fluctuation prefactor and competing dark channels.

The number `37.61` remains a **provisional target exponent**, inherited from the earlier crude attempt-frequency screen. It is not yet a calibrated physical DCR requirement.

---

## 1. Finite-period nonlocal Euclidean problem

At bath temperature `T`, Euclidean time is periodic with physical period

\[
\beta\hbar=\frac{\hbar}{k_BT}.
\]

Using normalized time `s=omega_c tau`, the period is

\[
\boxed{P_s=\frac{\hbar\omega_c}{k_BT}}.
\]

The even periodic path is represented as

\[
y(s)=a_0+\sum_{n=1}^{N}a_n\cos\!\left(\frac{2\pi ns}{P_s}\right),
\]

with `y=x-x_m`.

The reduced Euclidean action contains:

1. phase inertia;
2. the exact non-sinusoidal cold CPR potential;
3. the exact Matsubara kernel of the same passive two-pole environment.

For mode `n>0`,

\[
K_{\rm env,nn}
=
\frac{\bar\Phi^2}{\hbar}
\frac{P_s}{2}
 k_nY_L(\omega_ck_n).
\]

The constant mode has no dissipative contribution.

The solver explicitly checks the number of negative even modes. The physical periodic instanton below crossover has exactly one.

Implementation:

```text
calculations/finiteT_nonlocal_periodic_bounce.py
calculations/finiteT_nonlocal_periodic_bounce_v2.py
```

The `v2` wrapper exists because the first workflow exposed a pure SciPy/NumPy scalar-conversion bug before finite-T physics was evaluated. It changes only scalarization and reuses the same action equations and continuation.

---

## 2. Exact sphaleron regression

The static saddle/sphaleron has the exact action

\[
\boxed{B_{\rm sph}(T)=\frac{\Delta U}{k_BT}}.
\]

The periodic solver reproduces this identity numerically at approximately `1e-8` relative error in the high-tilt tests.

This is an important independent normalization check on the finite-period action.

---

## 3. Exact dissipative quantum-to-thermal crossover

The first nonzero Matsubara mode of the static sphaleron has the quadratic eigenvalue

\[
\boxed{
\Lambda_1(T)
=
C\nu_1^2+\nu_1Y_L(\nu_1)+\frac{F'_s}{L},
\qquad
\nu_1=\frac{2\pi k_BT}{\hbar}.
}
\]

The exact reduced-model crossover solves

\[
\Lambda_1(T_\times)=0.
\]

For the earlier designs scaled so that `B(T=0)=37.61`, the corrected crossovers are:

| delta | exact Tx [K] |
|---:|---:|
| .050 | .58145 |
| .140 | .16983 |
| .160 | .11893 |
| .180 | .073542 |
| .190 | .054225 |
| .200 | .037984 |
| .210 | .028440 |
| .220 | .021792 |

Thus the previous heuristic `hbar*omega_c/(2*pi*kB)` crossover was substantially too pessimistic because it ignored the actual saddle curvature and full environment.

At `T0=.020 K`, even the old zero-T-compensated `.22` point is still just on the periodic-instanton side of this exact linear bifurcation.

Implementation:

```text
calculations/finiteT_exact_sphaleron_crossover.py
```

---

## 4. Finite temperature lowers the action before the crossover

The important correction is not merely whether `T0` is above or below `Tx`.

At the old `B(T=0)=37.61` scales, the actual 20-mK periodic actions are:

| delta | old r | fc [GHz] | Tx [K] | B20mK |
|---:|---:|---:|---:|---:|
| .180 | 4.9562 | 4.6616 | .07354 | 36.82827 |
| .190 | 5.7634 | 3.9148 | .05423 | 36.48792 |
| .200 | 6.8126 | 3.2217 | .03798 | 35.86042 |
| .210 | 8.2333 | 2.5794 | .02844 | 34.54548 |

All four physical paths are nonstatic one-negative-mode periodic instantons.

Therefore

\[
\boxed{
B_{T=0}=37.61
\ \not\Rightarrow\
B_{20\,\mathrm{mK}}=37.61.
}
\]

The discrepancy grows rapidly as the electrical compensation slows the phase mode and moves the system closer to the finite-T sphaleron bifurcation.

---

## 5. Corrected electrical scales for B20mK=37.61

The finite-period solver was inverted to solve

\[
\boxed{B_{20\,\mathrm{mK}}(\delta,r)=37.61}
\]

under the exact electrical similarity family

\[
C=r^2C_0,
\qquad
R=R_0/r,
\qquad
\alpha=.90.
\]

The corrected scales are:

| delta | r20 | C [fF] | R [ohm] | fc [GHz] | Tx [K] | saddle |
|---:|---:|---:|---:|---:|---:|---|
| .180 | 5.065859 | 5517.53 | 15.792 | 4.56068 | .071950 | periodic |
| .190 | 5.954157 | 7622.18 | 13.436 | 3.78932 | .052487 | periodic |
| .200 | 7.191672 | 11119.83 | 11.124 | 3.05185 | .035982 | periodic |
| .210 | 9.235496 | 18338.29 | 8.662 | 2.29952 | .025354 | periodic |

The final 48-mode/6144-grid actions are all within roughly `1e-5` of 37.61.

---

## 6. Spectral convergence is extremely strong

A basis/grid convergence test was run at the corrected `.18`, `.20`, and `.21` scales:

```text
N=32 / 4096 grid
N=40 / 5120
N=48 / 6144
N=64 / 8192.
```

Representative 48->64 relative action changes:

```text
delta=.18 : 4.7e-7
delta=.20 : 1.7e-8
delta=.21 : 3.6e-10.
```

Each converged periodic saddle has exactly one negative even mode and gradient residuals far below `1e-8`.

Thus numerical spectral truncation is no longer a meaningful uncertainty in the reduced finite-T exponent. Model completeness and the prefactor dominate.

Workflow:

```text
experiment03-finiteT-periodic-convergence.yml
run 31923048864
```

---

## 7. Exact finite-temperature action ceiling in tilt

At fixed bath temperature, no electrical mass/damping compensation can make the physical escape exponent exceed the static sphaleron action

\[
B_{\rm sph}=\frac{\Delta U}{k_BT_0}.
\]

Therefore a target `Bstar` is possible only if

\[
\frac{\Delta U(\delta)}{k_BT_0}\ge B_\star.
\]

For `T0=.020 K` and `Bstar=37.61`, the exact static-potential solve gives

\[
\boxed{\delta_{\rm ceiling}=0.2150240395}.
\]

At this tilt,

\[
\frac{\Delta U}{k_B}=0.752200000~\mathrm K,
\qquad
B_{\rm sph}=37.61.
\]

Nearby values:

```text
delta=.210 -> Bsph=43.70888
delta=.212 -> 41.24478
delta=.214 -> 38.82848
delta=.2150240395 -> 37.61000
delta=.216 -> 36.46065
delta=.218 -> 34.14209
delta=.220 -> 31.87374.
```

Hence

\[
\boxed{
\delta>0.2150240395
\quad\text{cannot satisfy}\quad
B_{20\,\mathrm{mK}}\ge37.61
}
\]

within the reduced model, regardless of capacitance.

This finite-temperature action ceiling is the relevant high-tilt termination, well before the cold static double-well fold near `.26-.27`.

---

## 8. Finite-temperature electrical similarity

The pure electrical similarity extends to finite temperature. Under

\[
C\to r^2C,
\quad R\to R/r,
\quad\omega_D\to\omega_D/r,
\]

and Euclidean time `tau=r u`, the finite-period problem maps to the unscaled problem at the higher effective temperature `rT`:

\[
\boxed{B(T;r)=r\,B_0(rT)}.
\]

Consequently

\[
\boxed{T_\times(r)=T_\times(1)/r}.
\]

A numerical full-periodic-saddle regression of this identity is running in

```text
experiment03-finiteT-electrical-similarity.yml
```

so this statement should be treated as a derived exact model symmetry pending that numerical regression.

An important implication follows near the finite-T action ceiling: the required electrical scale does **not** diverge as the ceiling is approached. Instead it approaches the finite crossover scale

\[
r_\times=\frac{T_\times(1)}{T_0}.
\]

For a regular supercritical first periodic-instanton bifurcation,

\[
B_{\rm sph}-B_{\rm per}\propto(r_\times-r)^2,
\]

so for fixed target

\[
\boxed{
r_\times-r_\star
\propto
\sqrt{B_{\rm sph}-B_\star}.
}
\]

This supersedes the earlier provisional intuition that the compensation scale must diverge at the finite-temperature action ceiling.

---

## 9. Corrected capture frontier is running

The earlier high-tilt capture results were obtained on the obsolete `B(T=0)=37.61` manifold. They remain useful trajectory diagnostics but are not the accepted constant-dark-action frontier.

A matched 14-um / 20-ps capture screen is now running at the corrected `B20mK=37.61` scales for

```text
delta=.18,.19,.20,.21.
```

Workflow:

```text
experiment03-finiteT-corrected-capture.yml
run 31923038900
```

Do not infer its outcome from the old zero-T-compensated capture runs.

---

## 10. What this does and does not establish

### Established within the reduced Euclidean model

- the actual non-sinusoidal cold potential must be used;
- the full passive two-pole environment can be included nonlocally;
- the finite-period periodic instanton is numerically converged;
- the exact dissipative crossover can be obtained from the sphaleron Matsubara Hessian;
- finite temperature materially lowers the escape action before crossover;
- the high-tilt design is bounded by a finite-T sphaleron action ceiling near `delta=.215`;
- the correct dark-constrained optimization variable is now
  \[
  A_{99}(\delta\mid B_{20\mathrm{mK}}=37.61).
  \]

### Not established

- a physical DCR;
- the fluctuation determinant / collective-coordinate prefactor;
- finite-frequency/environmental renormalizations outside the retained linear network;
- dark switching from flux noise, quasiparticles, vortices or stray photons;
- exact nonlinear quantum capture efficiency;
- physical long-wavelength cutoff after realistic absorptance and spatial thermalization are restored.

---

## 11. Next gates

1. finish the corrected `B20mK=37.61` capture frontier;
2. numerically verify the exact finite-T electrical similarity;
3. refine the optimum below `delta_ceiling` if the capture frontier still rises through `.21`;
4. derive/compute the finite-T nonlocal fluctuation prefactor;
5. replace the provisional exponent target with a calibrated physical dark-rate constraint;
6. only then reopen absolute detector-performance claims.

**Verdict: GO for continued theory; NO-GO for manuscript.**
