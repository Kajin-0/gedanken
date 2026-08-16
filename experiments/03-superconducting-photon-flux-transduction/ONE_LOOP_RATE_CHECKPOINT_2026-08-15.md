# Experiment 03 — Calibrated one-loop dark-rate checkpoint — 2026-08-15

## Status

**Canonical dark-rate checkpoint.**

The earlier provisional design constraints

```text
B(T=0)=37.61
```

and then

```text
B(20 mK)=37.61
```

have both been superseded as the preferred reduced-model dark constraint.

The finite-period periodic-instanton action is now combined with a UV-converged fluctuation determinant and an independently calibrated collective-coordinate normalization.  The current reduced-model dark constraint is therefore

\[
\boxed{
\Gamma_{1\ell}(T_0=20\,\mathrm{mK};\delta,r)=10^{-6}\ \mathrm{s^{-1}}
}
\]

where

\[
\Gamma_{1\ell}=A_{1\ell}e^{-B_{20\mathrm{mK}}}.
\]

This is still **not a final physical DCR** because the soft-mode crossover very near `Tx`, competing dark channels, and possible environment/model omissions remain unresolved.  It is nevertheless a materially stronger and internally normalized constraint than an arbitrary GHz attempt frequency.

---

## 1. Finite-T periodic instanton and determinant status

The finite-period, same-environment Euclidean action is solved in an even Matsubara basis with the actual non-sinusoidal CPR potential and exact positive-real two-pole environmental kernel.

Accepted regressions:

- static sphaleron action reproduces
  \[
  B_{\rm sph}=\Delta U/(k_BT)
  \]
  to roughly `1e-8` relative;
- physical periodic instantons have exactly one negative even mode;
- the odd translation zero mode has unit overlap with `dx_b/ds`;
- 48->64 basis changes in `B20` are `<=5e-7` and much smaller near crossover.

The exponent is numerically converged well beyond the accuracy justified by the physical model.

---

## 2. Raw determinant and UV-tail correction

The full real Hessian was constructed in an orthonormal basis:

- even sector: constant + cosine modes;
- odd sector: sine modes;
- one negative even mode;
- one odd translation zero mode.

The raw log determinant converges only as `O(1/N)` because the omitted high-Matsubara modes contribute `O(1/n^2)`.

The asymptotic correction uses the exact diagonal high-frequency operator

\[
\lambda_n^{(m)}
=
A_k k_n^2
+
\frac{\bar\Phi^2}{\hbar}k_nY_L(\omega_ck_n)
+
A_v\kappa_m
\]

and the leading average-curvature difference between the metastable well and periodic bounce.

At `delta=.20`, for example,

```text
raw logD, N=80 -> 3.908787
raw logD, N=96 -> 3.913990? before correction comparison basis
```

while the UV-corrected values converge to approximately

\[
\boxed{\log D_{raw,corr}(.20)=3.91399054}
\]

with an `N=80 -> 96` change of only `~5e-6`, an improvement by about `970x` over the raw truncation.

Representative converged corrected values:

\[
\log D_{raw,corr}
\approx
\begin{cases}
3.76856,&\delta=.18,\\
3.91399,&\delta=.20,\\
4.12568,&\delta=.21.
\end{cases}
\]

Thus UV regularization/convergence is no longer the dominant prefactor uncertainty.

---

## 3. Absolute determinant normalization — cubic calibration

A separate local cubic metastable problem was solved numerically:

\[
V(z)=\frac{M\omega^2q_0^2}{2}z^2(1-z),
\qquad
z_b(s)=\operatorname{sech}^2(s/2).
\]

For this canonical problem,

\[
B=\frac{8A}{15},
\qquad
A=\frac{M\omega q_0^2}{\hbar},
\]

and the exact operator determinant is

\[
\boxed{
\sqrt{\frac{\det L_m}{|\det' L_b|}}=\sqrt{60}.
}
\]

Hessians of the **dimensionless action** `B=S/hbar` contain one unmatched factor `sqrt(A)` after the zero mode is removed. Therefore

\[
\boxed{D_{op}=D_{raw}/\sqrt{A_k}}
\]

for the Experiment-03 determinant, with

\[
A_k=C\bar\Phi^2\omega_c/\hbar.
\]

Numerical cubic calibration at highest retained resolution gives

\[
D_{op}=7.74565249
\]

versus

\[
\sqrt{60}=7.74596669,
\]

a relative error of only about

\[
4.1\times10^{-5}.
\]

Changing the overall action scale by `16x` leaves `D_op` invariant to numerical precision while `D_raw` scales as `sqrt(A)`.

The same normalization reproduces the canonical cubic MQT one-loop prefactor to the same `~4e-5` level.

Therefore the determinant/collective-coordinate normalization is no longer an arbitrary convention.

---

## 4. Calibrated one-loop prefactor

For the periodic saddle define

\[
I_s=\int_0^{P_s}\left(\frac{dx_b}{ds}\right)^2ds.
\]

The translation collective coordinate contributes

\[
\sqrt{\frac{A_kI_s}{2\pi}}.
\]

Using the calibrated operator determinant,

\[
D_{op}=D_{raw,corr}/\sqrt{A_k},
\]

the one-loop prefactor simplifies to

\[
\boxed{
A_{1\ell}
=
\omega_c
\sqrt{\frac{I_s}{2\pi}}
D_{raw,corr}.
}
\]

Hence

\[
\boxed{
\Gamma_{1\ell}=A_{1\ell}e^{-B_{20\mathrm{mK}}}.
}
\]

This normalization is cubic-calibrated.  A uniform soft-mode treatment is still required asymptotically close to `T=Tx`.

---

## 5. One-loop rate at the old B20=37.61 designs

At the previously corrected `B20=37.61` scales:

### delta=.18

```text
B20 = 37.61000084
A1  = 2.271547e11 /s
Gamma1 = 1.0505e-5 /s
```

A fixed-prefactor estimate would require about `+2.35` additional action units.

### delta=.20

```text
B20 = 37.60999912
A1  = 1.462686e11 /s
Gamma1 = 6.7594e-6 /s
```

Fixed-prefactor diagnostic: about `+1.91` action units.

### delta=.21

```text
B20 = 37.61002026
A1  = 1.092254e11 /s
Gamma1 = 5.05e-6 /s
```

Fixed-prefactor diagnostic: about `+1.5–1.6` action units.

Therefore a universal exponent `37.61` is demonstrably not equivalent to a universal `1e-6/s` one-loop dark rate.

---

## 6. Self-consistent one-loop rate manifold

The exact finite-period action and calibrated prefactor were jointly solved for

\[
\Gamma_{1\ell}(\delta,r)=10^{-6}\ \mathrm{s^{-1}}.
\]

Accepted high-resolution roots include:

| delta | r_rate | C [fF] | R [ohm] | fc [GHz] | B20 | A1 [1/s] | T0/Tx |
|---:|---:|---:|---:|---:|---:|---:|---:|
| .2000 | 7.609686 | 12449 | 10.513 | 2.884 | 39.482 | 1.40e11 | .576 |
| .2050 | 8.549475 | 15714 | 9.358 | 2.507 | 39.327 | 1.19e11 | .688 |
| .2075 | 9.096703 | 17791 | 8.795 | 2.355 | 39.269 | 1.14e11 | .754 |
| .2100 | 9.825702 | 20757 | 8.142 | 2.161 | 39.184 | 1.04e11 | .839 |

Representative exact root values:

### delta=.20

\[
\boxed{r_{rate}=7.609686269}
\]

with

```text
C = 12.449 pF
R = 10.513 ohm
fc = 2.884 GHz
B20 = 39.4821
A1 = 1.400e11 /s
Gamma1 = 1.0001e-6 /s.
```

### delta=.21

\[
\boxed{r_{rate}=9.825701561}
\]

with

```text
C = 20.757 pF
R = 8.142 ohm
fc = 2.161 GHz
B20 = 39.1844
A1 = 1.041e11 /s
Gamma1 = 1.00005e-6 /s
T0/Tx = .839.
```

Thus the calibrated prefactor increases the required electrical scale by only about `6%` relative to the old `B20=37.61` scale in the `.20-.21` region.

The `.21` solution remains below the immediate soft-mode crossover; it is not yet in the region flagged by the current `T0/Tx>.92` caution criterion.

---

## 7. Exact finite-T electrical similarity extends to the prefactor

The finite-period action satisfies the exact model identity

\[
\boxed{B(T;r)=rB_0(rT)}.
\]

The periodic path at `(T,r)` is the unscaled dimensionless path at effective temperature `rT`, so

\[
I_s(T;r)=I_{s,0}(rT).
\]

Because the dimensionless Hessian scales by `r` and one zero mode is removed,

\[
D_{raw}(T;r)=\sqrt r\,D_{raw,0}(rT).
\]

Therefore the calibrated one-loop prefactor obeys

\[
\boxed{
A_{1\ell}(T;r)
=r^{-1/2}A_{1\ell,0}(rT)
}
\]

and

\[
\boxed{
\Gamma_{1\ell}(T;r)
=r^{-1/2}A_0(rT)e^{-rB_0(rT)}.
}
\]

This provides a compact exact similarity representation of the entire one-loop dark-rate family away from the soft-mode-uniformization region.

---

## 8. Capture constraint at the old B20 manifold

A matched 2-ns sym-FDT TWA sweep on the old `B20=37.61` manifold found:

```text
delta=.2000: A~425 um2 gives P~.9902
delta=.2025: A430 -> .9951; A445 -> .9863
delta=.2050: A455 -> .9912; A470 -> .9873
delta=.2075: A465 -> .9932; A480 -> .9873
delta=.2100: A470 -> 1.0000; A480 -> .9951
```

So the 2-ns capture frontier continued to rise through `.21` at equal **exponent**.

The exact thermal action ceiling probe at `delta=0.215024` instead gives only

```text
A420 -> P~.995
A500 -> P~.933
```

under the old 0.5-ns horizon, showing that the high-fidelity capture frontier eventually turns before or at the thermal ceiling.

---

## 9. Active decisive calculation

The correct final reduced-model comparison is now running:

```text
experiment03-one-loop-rate-capture.yml
```

It evaluates the 14-um / 20-ps capture frontier with a **2-ns post-pulse horizon** at the self-consistent one-loop `Gamma=1e-6/s` scales for

```text
delta=.2000, .2050, .2075, .2100.
```

Do not infer its result from the old B20=37.61 capture frontier.

A separate high-tilt rate-boundary workflow is probing

```text
delta=.211,.212,.213,.214
```

to locate where the ordinary Gaussian one-loop rate root either enters the soft-mode crossover region or ceases to be trustworthy.

---

## 10. Current interpretation

The design problem has now become

\[
\boxed{
\max_{\delta,r,A}\ A_{99}
}
\]

subject to

\[
\boxed{
\Gamma_{1\ell}(T_0;\delta,r)\le10^{-6}\ \mathrm{s^{-1}}
}
\]

plus the separate 2-ns capture-settling condition.

This is substantially stronger than all previous `B=constant` rescue formulations.

The likely optimum is in the high-tilt `.20-.21` region, but it is **not yet accepted** until the one-loop-rate-constrained capture matrix and high-tilt soft-mode boundary complete.

---

## 11. Remaining blockers

Even after the present optimum is located, no physical detector-performance claim is authorized without:

1. soft-mode-uniform finite-T rate treatment near `T~Tx`;
2. detailed-balance-preserving nonlinear quantum capture;
3. flux-noise sensitivity versus directional tilt;
4. quasiparticle/vortex/stray-photon dark channels;
5. realistic wavelength-dependent absorption/coupling;
6. spatial nonequilibrium thermalization;
7. readout/reset loading;
8. narrow prior-art/patent collision audit.

**Verdict: GO for continued theory; NO-GO for manuscript.**
