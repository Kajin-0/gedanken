# Experiment 03 — Electrical dark-action similarity closure — 2026-08-15

## Status

**Exact scaling statement for the zero-temperature electrical Euclidean action of the current reduced passive-network model. Capture compatibility with an unscaled physical thermal pulse is a separate question. Not novelty-audited.**

## 1. Electrical scaling

Hold fixed

- loop inductance `L`;
- the static CPR / rf-SQUID potential `U(x)`;
- the normalized two-pole bath cutoff `alpha=omega_D/omega_c`;
- the normalized dissipative control `g=1/(R C omega_c)`.

Apply

\[
\boxed{
C' = r^2 C,
\qquad
R'=R/r,
\qquad
\omega_D'=\omega_D/r
}
\]

with `r>0`.

Since

\[
\omega_c^2=\frac{\kappa_c}{LC},
\]

we have

\[
\boxed{\omega_c'=\omega_c/r.}
\]

Therefore

\[
g'=rac{1}{R'C'\omega_c'}=g,
\qquad
\alpha'=\frac{\omega_D'}{\omega_c'}=\alpha.
\]

For the critically parameterized passive two-pole network

\[
L_f=\frac{\sqrt2R}{\omega_D},
\qquad
C_f=\frac{1}{\sqrt2R\omega_D},
\]

this gives

\[
\boxed{L_f'=L_f,\qquad C_f'=r^2C_f.}
\]

Thus all electrical capacitances scale as `r^2`, all selected resistances as `1/r`, and the relevant electrical frequencies as `1/r`, while inductances remain fixed.

## 2. Euclidean action scaling

Write the zero-temperature electrical Euclidean action after integrating the linear passive environment as

\[
S_E[x]
=\int d\tau\left[
\frac12 C\bar\Phi^2\dot x^2+U_{\rm phys}(x)
\right]
+
\frac{\bar\Phi^2}{2}
\int\frac{d\omega}{2\pi}
|\omega|Y_L(|\omega|)|x(\omega)|^2,
\]

where `Y_L(s)` is the positive-real Laplace admittance of the selected passive network.

Under the electrical scaling above and the time change

\[
\tau'=r\tau,
\qquad
x'(\tau')=x(\tau'/r),
\]

- the capacitive kinetic term scales by `r`;
- the static-potential term scales by `r`;
- the two-pole Laplace admittance scales as
  \[
  Y_L'(s)=rY_L(rs),
  \]
  which makes the environmental quadratic term also scale by `r`.

Therefore

\[
\boxed{
S_E'[x']=rS_E[x]
}
\]

for every path related by the scaling.

Consequently the stationary dissipative bounce maps onto itself in normalized time and

\[
\boxed{B'=S_B'/\hbar=rB.}
\]

This statement is stronger than the old cubic-barrier `C_min` rule: it applies to the **full static CPR potential plus the chosen linear two-pole environment**, independent of whether the bounce is cubic.

## 3. What does not scale

The persistent-current state separation remains

\[
\Delta I=\zeta\Phi_0/L,
\]

so it is unchanged because `L` is fixed.

The physical electrical time scale grows as

\[
\boxed{\tau_{\rm elec}'=r\tau_{\rm elec}.}
\]

Thus the scaling improves the dark tunneling exponent without reducing the persistent current signal, but it **slows the phase dynamics**.

## 4. Dark-rate scaling with a similarity-preserving prefactor assumption

If the fluctuation determinant/prefactor has the same dimensionless form under this electrical similarity, its characteristic frequency scale changes as `1/r`. A screening form is then

\[
\Gamma'(r)
\sim
\frac{\Omega_0}{r}
\mathcal A_{\rm dimless}
\exp(-rB_0).
\]

The exponential scaling is exact at the action level. The prefactor expression is conditional until the actual dissipative fluctuation determinant is calculated.

For a target `D`, the corresponding screening equation is

\[
\boxed{
rB_0+\ln r
\gtrsim
\ln\frac{\Omega_0\mathcal A_{\rm dimless}}{D}.}
\]

## 5. Current R80 numerical scale

The exact non-sinusoidal isolated bounce gives

\[
B_{\rm iso}=25.03,
\]

while the restricted two-parameter dissipative saddle for `R=80 ohm, alpha=.90, C=215 fF` gives

\[
B_{\rm 2D}\approx30.06.
\]

Using the same rough `f_c exp(-B)` normalization only to estimate the required scaling for `D=10^{-6}/s` gives

\[
r\approx1.25.
\]

That corresponds approximately to

\[
C'\sim337\ \mathrm{fF},
\qquad
R'\sim64\ \Omega,
\qquad
f_c'\sim21.8\ \mathrm{GHz},
\]

with the same `alpha=.90` and unchanged `Delta I`.

**These are not a recommended device point.** They only locate the scale of the electrical redesign suggested by the current restricted-action model.

## 6. Capture tradeoff

The photon thermal history does not automatically transform as `t->r t`. If the physical graphene rise/cooling laws are left unchanged while the electrical phase circuit slows, then the full photon-capture problem is no longer similar.

Therefore the relevant combined condition is not merely `B -> rB`, but

```text
increase r enough for dark stability
while remaining inside the finite-time photon-capture basin.
```

The workflow `electrical_dark_rescue_capture.py` tests exactly this conflict by applying the electrical scaling while leaving the physical thermal pulse unchanged.

## 7. Research implication

This scaling exposes a clean detector-level competition:

\[
\boxed{
\text{dark tunneling exponent} \uparrow
\Longleftrightarrow
\text{electrical response time} \uparrow
}
\]

at fixed persistent-current signal and normalized electrical topology.

If a finite thermal capture window imposes a maximum allowable `r`, then it also imposes a maximum action reachable by pure electrical rescaling. That combined dark-stability/write-time bound is a natural next analytical target after the rescue-capture workflow is evaluated.

No novelty claim is authorized.
