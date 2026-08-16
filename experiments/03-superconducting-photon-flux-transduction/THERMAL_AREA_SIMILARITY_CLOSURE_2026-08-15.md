# Experiment 03 — Thermal absorber-area similarity closure — 2026-08-15

## Status

**Derived within the lumped graphene calorimetric model. Not novelty-audited.**

This closure clarifies what the current `14 um, A=57.142857 um^2` similarity tests do and do not establish.

## 1. General absorbed-photon temperature scaling

For electronic heat capacity

\[
C_e=\gamma A T,
\]

the energy required to raise the electronic system from `T0` to `T` is

\[
\Delta E_e
=\frac{\gamma A}{2}(T^2-T_0^2).
\]

For one photon of wavelength `lambda` with absorbed fraction `eta_abs(lambda)`,

\[
E_{\rm abs}
=\eta_{\rm abs}(\lambda)\frac{hc}{\lambda}.
\]

The adiabatic peak scale is therefore

\[
\boxed{
T_{\rm pk}^2-T_0^2
=\frac{2\eta_{\rm abs}(\lambda)hc}
       {\gamma A\lambda}
}.
\]

With the current common cooling/rise model, cases having equal

\[
\boxed{
\frac{\eta_{\rm abs}(\lambda)}{A\lambda}
}
\]

have the same reduced electronic-temperature history `T_e(t)`.

If `eta_abs` is held fixed, the exact similarity variable is simply

\[
\boxed{A\lambda=\text{constant}}.
\]

This is why

```text
8 um  x 100 um^2
14 um x 57.142857 um^2
```

produce exactly the same thermal and phase trajectories in the present model.

More generally, preserving the thermal drive relative to a reference case requires

\[
\boxed{
A(\lambda)
=A_0\,
\frac{\eta_{\rm abs}(\lambda)}{\eta_{\rm abs}(\lambda_0)}
\frac{\lambda_0}{\lambda}
}.
\]

## 2. Trigger versus parent-gap confinement

Suppose successful write dynamics require

\[
T_{\rm pk}\ge T_{\rm trig},
\]

while thermal confinement by the parent superconductor requires

\[
T_{\rm pk}\le T_{\rm esc},
\]

where `T_esc` is an effective parent-gap/contact-escape temperature scale and
`T_esc > T_trig`.

The trigger gives an upper absorber-area bound

\[
\boxed{
A\le A_{\max}(\lambda)
=\frac{2\eta_{\rm abs}(\lambda)hc}
       {\gamma\lambda(T_{\rm trig}^2-T_0^2)}
},
\]

while confinement gives a lower bound

\[
\boxed{
A\ge A_{\min}(\lambda)
=\frac{2\eta_{\rm abs}(\lambda)hc}
       {\gamma\lambda(T_{\rm esc}^2-T_0^2)}
}.
\]

The relative width of the feasible area window is therefore

\[
\boxed{
\frac{A_{\max}}{A_{\min}}
=\frac{T_{\rm esc}^2-T_0^2}
       {T_{\rm trig}^2-T_0^2}
}.
\]

The wavelength and absorption efficiency cancel exactly.

## 3. Consequence

Within this ideal lumped model, a thermal trigger threshold plus a parent-gap
confinement threshold does **not** by itself create a fundamental longest photon
wavelength.  Increasing wavelength simply scales the entire allowed absorber-area
window as

\[
A_{\min},A_{\max}\propto\frac{\eta_{\rm abs}(\lambda)}{\lambda}.
\]

Thus a genuine long-wavelength cutoff must arise from a non-scale-invariant
constraint such as

- a minimum realizable heat capacity / absorber area;
- wavelength-dependent optical absorption or antenna/cavity coupling;
- finite thermalization or diffusion length/time;
- a change in electronic heat-capacity law;
- parent-gap/contact leakage beyond a single temperature threshold;
- nonlocal or nonequilibrium quasiparticle physics;
- breakdown of the assumed CPR-temperature map;
- circuit/readout constraints that cannot be rescaled with absorber geometry.

This changes the interpretation of `lambda_fold` tables: they are thresholds at
**fixed absorber geometry**, not intrinsic spectral limits of the architecture.

## 4. Maximum wavelength from a non-scaling minimum area

If some independent physics imposes `A >= A_phys,min`, then the trigger condition
becomes

\[
\lambda
\le
\frac{2\eta_{\rm abs}(\lambda)hc}
     {\gamma A_{\rm phys,min}(T_{\rm trig}^2-T_0^2)}.
\]

Only at this stage does a thermal long-wavelength ceiling emerge.

## 5. Discipline

The similarity law is exact only within the stated lumped model. Do not infer
that a real antenna-coupled graphene Josephson detector has wavelength-independent
absorption efficiency or can shrink indefinitely.

No novelty claim is authorized.
