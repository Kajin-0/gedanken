# Experiment 03 — Capture-probability similarity theorem — 2026-08-15

## Status

**Exact theorem within the stated reduced lumped model. Not a claim about real devices and not novelty-audited.**

This strengthens `THERMAL_AREA_SIMILARITY_CLOSURE_2026-08-15.md` from a peak-temperature scaling into a statement about the *entire stochastic phase-capture problem*.

## 1. Assumptions

Assume:

1. graphene electronic heat capacity is
   \[
   C_e(T)=\gamma A T;
   \]
2. an absorbed photon deposits energy
   \[
   E_{\rm abs}=\eta_{\rm abs}(\lambda)hc/\lambda;
   \]
3. the normalized optical source shape/rise time is fixed and its amplitude is proportional to `E_abs/A`;
4. the subsequent lumped electronic cooling law has no additional explicit dependence on `lambda`, `A`, or `eta_abs` after division by area (the current clean-graphene `T^4` model has this property);
5. the Josephson CPR depends on the optical event only through the resulting electronic state, currently represented by `T_e(t)`;
6. the superconducting circuit and its bath/noise statistics are otherwise held fixed;
7. optical absorption efficiency enters only through the deposited energy, not through an additional wavelength-dependent dynamical channel.

## 2. Thermal reduction

With `u=T_e^2`, the current lumped energy equation can be written schematically as

\[
\dot u
=
\mathcal S(t)
\frac{\eta_{\rm abs}(\lambda)}{A\lambda}
-\mathcal C(u;T_0),
\]

where `S(t)` contains constants and the fixed normalized rise profile, and `C` is the fixed cooling law.

Therefore the full electronic-temperature history depends on optical wavelength, absorber area and absorption fraction only through

\[
\boxed{
 g_\gamma
 =\frac{\eta_{\rm abs}(\lambda)}{A\lambda}
}.
\]

If two optical cases satisfy

\[
\frac{\eta_1}{A_1\lambda_1}
=
\frac{\eta_2}{A_2\lambda_2},
\]

then uniqueness of the thermal ODE gives

\[
\boxed{T_{e,1}(t)=T_{e,2}(t)}
\]

for identical initial conditions and source shape.

## 3. Coupled phase dynamics

The phase/environment state `z` obeys a stochastic dynamical equation of the form

\[
\dot z
=F[z,T_e(t)] + \Xi(t),
\]

where `Xi(t)` is drawn from the same bath law in the two compared cases.

Equal `T_e(t)` therefore gives equal deterministic coefficients at every time. Coupling the two cases to the same realization of `Xi(t)` yields identical trajectories path-by-path:

\[
\boxed{z_1(t;\Xi)=z_2(t;\Xi)}.
\]

Hence every event functional of the trajectory has the same distribution, including the target-basin indicator.

Therefore

\[
\boxed{
P_{\rm cap}(\lambda,A,\eta_{\rm abs})
=\mathcal P\!\left(
\frac{\eta_{\rm abs}(\lambda)}{A\lambda}
\right)
}
\]

for fixed material, circuit, bath, rise profile and cooling model.

This remains true whether `Xi` is omitted, treated semiclassically, or replaced by a more rigorous open-system stochastic representation, **provided the bath model itself does not acquire additional explicit optical-wavelength/area dependence**.

## 4. Fidelity contours

For a fixed target probability `p`, any level set satisfying `P_cap=p` obeys

\[
\boxed{
\frac{A_p(\lambda)\lambda}
     {\eta_{\rm abs}(\lambda)}
=\mathcal C_p
}
\]

whenever the selected branch of `P(g_gamma)` is single-valued.

At fixed absorption efficiency,

\[
\boxed{A_p\lambda=\text{constant}.}
\]

Thus a calibrated threshold at one wavelength maps exactly to all other wavelengths **inside this reduced model** without rerunning the phase dynamics.

## 5. Current numerical illustration only

The current R80 / `alpha=.90` / 20-ps-rise symmetrized-FDT TWA screen places the 14-um `P~0.99` crossing between approximately `A=84` and `86 um^2`. The associated constant is therefore near

\[
\lambda A_{99}\sim1.2\times10^3\ \mu{\rm m}^3
\]

for constant `eta_abs`.

This number is provisional because the high-statistics threshold refinement is still in progress and, more importantly, the symmetrized-FDT TWA fraction is not exact physical quantum efficiency.

The similarity theorem itself does **not** depend on that numerical value.

## 6. What breaks the theorem in a real device

Any explicit wavelength/area dependence outside the scalar deposited-energy density breaks the symmetry. Important examples include:

- `eta_abs(lambda)` changing with antenna/cavity resonance, unless included explicitly in `g_gamma`;
- wavelength-dependent absorption location or spatial mode shape;
- nonthermal carrier distributions whose relaxation depends on photon energy;
- optical-phonon thresholds and energy-dependent carrier cascades;
- area-dependent diffusion length/path to the weak link;
- area-dependent electronic density of states, proximity spectrum or CPR;
- geometry-dependent parasitic capacitance/inductance changing the phase circuit when `A` changes;
- contact cooling that depends on geometry rather than only local `T_e`;
- saturation/nonlinearity in absorption;
- multi-photon statistics or optical backgrounds coupled to collection area.

These are not small-print caveats: they are exactly the physics that can create a *real* intrinsic long-wavelength limit even though the lumped calorimetric model has none.

## 7. Research use

The theorem is useful as a diagnostic separator:

```text
if two equal-g_gamma cases disagree in a more complete model,
then the disagreement identifies the non-scale-invariant physics.
```

That makes wavelength translation a controlled way to expose which missing physical mechanism actually sets the detector's spectral limit.

No priority or novelty claim is authorized.
