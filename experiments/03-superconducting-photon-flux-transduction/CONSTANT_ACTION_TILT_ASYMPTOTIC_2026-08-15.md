# Experiment 03 — Constant-dark-action critical-tilt asymptotic — 2026-08-15

## Status

**Derived model law / design asymptotic.**

This note records a generic saddle-node consequence of the current high-tilt + electrical-compensation strategy. It does **not** establish a physical detector optimum or novelty. It explains why the constant-zero-temperature-action spectral improvement cannot continue without bound as the cold metastable state approaches its fold.

## 1. Setup

Let

\[
\epsilon=\delta_c-\delta>0
\]

measure distance from the cold metastable saddle-node in the directional tilt coordinate. Near a generic one-dimensional fold, the potential can be reduced locally to the cubic normal form

\[
U(q;\epsilon)=U_c+a\epsilon q-\frac{b}{3}q^3+\cdots,
\qquad a,b>0.
\]

The minimum/saddle displacement scales as

\[
\Delta q\propto\epsilon^{1/2},
\]

the barrier as

\[
\boxed{\Delta U\propto\epsilon^{3/2}},
\]

and the cold curvature as

\[
U''_m\propto\epsilon^{1/2}.
\]

For fixed electrical mass `M \propto C`, therefore

\[
\boxed{\omega_{c,0}\propto\epsilon^{1/4}}.
\]

## 2. Unscaled bounce action

For the cubic metastable normal form, the zero-temperature bounce exponent scales as

\[
B_0\sim c_b\frac{\Delta U}{\hbar\omega_{c,0}},
\]

where `c_b` is an order-unity shape constant (7.2 for the textbook cubic-barrier formula under its own conventions). Hence at fixed base capacitance

\[
\boxed{B_0\propto\epsilon^{5/4}}.
\]

The exact numerical coefficient is model/environment dependent. The exponent is the generic saddle-node scaling so long as the passive normalized environment remains regular in this limit.

## 3. Enforce a fixed target dark action by electrical similarity

The Experiment-03 electrical similarity is exact at fixed static CPR potential and normalized two-pole environment:

\[
C\to r^2C,\qquad
R\to R/r,\qquad
\omega_D\to\omega_D/r,
\]

with

\[
B\to rB,\qquad
\omega_c\to\omega_c/r.
\]

To hold a prescribed zero-temperature action `B_*` while approaching the fold,

\[
r=\frac{B_*}{B_0}
\propto\epsilon^{-5/4}.
\]

Therefore

\[
\boxed{C_*\propto\epsilon^{-5/2}}
\]

and the compensated cold phase frequency obeys

\[
\omega_{c,*}
=\frac{\omega_{c,0}}{r}
\propto\epsilon^{1/4}\epsilon^{5/4}.
\]

Thus

\[
\boxed{\omega_{c,*}\propto\epsilon^{3/2}},
\qquad
\boxed{\tau_{c,*}\propto\epsilon^{-3/2}}.
\]

This is the critical-slowing penalty of holding the dark tunneling action fixed while biasing ever closer to the metastable fold.

## 4. Fixed physical photon-rise time

For a physical optical rise time `tau_rise`, define

\[
\rho_*=\omega_{c,*}\tau_{rise}.
\]

Then

\[
\boxed{\rho_*\propto\epsilon^{3/2}\to0}.
\]

The phase degree of freedom becomes arbitrarily slow relative to the fixed thermal write/recovery history. Therefore static threshold reduction near the fold cannot produce unlimited finite-time detector sensitivity at fixed dark action.

This provides a structural reason to expect an interior optimum of the current numerical objective

\[
A_{99}(\delta\mid B=B_*),
\]

or, at minimum, a finite-time constraint before the critical tilt is reached.

## 5. Cold zero-point localization under the same compensation

In the low-temperature harmonic approximation,

\[
\sigma_q^2=\frac{\hbar}{2M\omega_c}.
\]

Under the pure electrical similarity,

\[
M\to r^2M,
\qquad
\omega_c\to\omega_c/r,
\]

so

\[
\boxed{\sigma_q^2\to\sigma_q^2/r},
\qquad
\boxed{\sigma_q\to\sigma_q/\sqrt r}.
\]

Near the saddle-node, the unscaled harmonic width scales as

\[
\sigma_{q,0}^2\propto\epsilon^{-1/4}.
\]

After constant-action compensation,

\[
\sigma_{q,*}^2
\propto
\epsilon^{-1/4}\epsilon^{5/4}
=\epsilon,
\]

hence

\[
\boxed{\sigma_{q,*}\propto\epsilon^{1/2}}.
\]

But the minimum-to-saddle distance also scales as

\[
\Delta q\propto\epsilon^{1/2}.
\]

Therefore the **relative** cold quantum localization does not parametrically improve near the critical point:

\[
\boxed{
\frac{\sigma_{q,*}}{\Delta q}=O(1)
}
\]

under fixed-action saddle-node scaling. The absolute Wigner cloud narrows, but the metastable basin narrows at the same parametric rate.

This is consistent with the earlier localization/action closure

\[
\sigma_x^2 S
=\frac{u_b}{2\kappa_c}
\]

at low temperature, because near a fold `u_b \propto \epsilon^{3/2}` and `\kappa_c \propto \epsilon^{1/2}`, so the right-hand side scales as `epsilon`.

## 6. Design interpretation

The constant-action tilt strategy has four coupled effects:

1. higher tilt lowers the static thermal trigger/fold scale;
2. higher tilt strengthens directional basin preference;
3. electrical compensation narrows the absolute cold phase distribution;
4. electrical compensation slows the phase clock, asymptotically as `epsilon^{-3/2}` in response time near the fold.

Thus the current optimization should be treated as a Pareto problem in

\[
(\text{zero-T dark action},\ \text{spectral/energy reach},\ \text{write speed},\ \text{basin probability}).
\]

The present symmetrized-FDT TWA simulations are numerical/model-dependent realizations of that competition; this asymptotic law itself does not validate their absolute probabilities.

## 7. Scope / caveats

This derivation assumes:

- a generic one-coordinate saddle-node normal form;
- the relevant dissipative environment remains regular under the normalized electrical similarity;
- zero-temperature tunneling action is the constrained dark metric;
- the static CPR/tilt topology remains one-dimensional near the local fold.

It does **not** establish:

- equality of physical finite-temperature dark-count rates at equal `B`;
- a physical detector optimum;
- exact nonlinear quantum capture probabilities;
- immunity to flux noise, quasiparticles, vortices or stray photons;
- novelty.

The numerical high-tilt sweep must still locate the finite-time turnover and the final design must be rechecked with a detailed-balance-preserving open-quantum model.
