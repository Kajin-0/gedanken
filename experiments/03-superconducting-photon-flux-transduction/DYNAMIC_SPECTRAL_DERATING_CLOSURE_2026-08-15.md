# Experiment 03 — Dynamic spectral derating closure — 2026-08-15

## Status

**Exact consequence of the reduced-model optical similarity theorem once a target-fidelity headroom `chi_p` is defined. The numerical `chi_p` values are model/screen dependent and are not exact quantum efficiencies. Not novelty-audited.**

## 1. Static fold wavelength

For fixed absorber geometry, absorption efficiency and material parameters, define `lambda_fold` as the wavelength at which one absorbed photon provides exactly the calorimetric energy density needed to reach the static rf-SQUID fold temperature:

\[
\chi_E
\equiv
\frac{T_{\rm ad}^2-T_0^2}
     {T_f^2-T_0^2}
=1.
\]

Because the reduced lumped model gives

\[
T_{\rm ad}^2-T_0^2
\propto
\frac{\eta_{\rm abs}}{A\lambda},
\]

at fixed `A` and `eta_abs` we have

\[
\chi_E(\lambda)
=\frac{\lambda_{\rm fold}}{\lambda}.
\]

## 2. Dynamic target-fidelity headroom

Let `chi_p` denote the optical energy-density headroom required by the *full reduced dynamical model* to reach a chosen capture probability `p`, with circuit, bath, rise and cooling parameters held fixed:

\[
P_{\rm cap}(\chi_p)=p.
\]

The corresponding target-fidelity wavelength `lambda_p` obeys

\[
\chi_p
=\frac{\lambda_{\rm fold}}{\lambda_p}.
\]

Therefore

\[
\boxed{
\frac{\lambda_p}{\lambda_{\rm fold}}
=\frac{1}{\chi_p}
}
\]

or

\[
\boxed{
\lambda_p
=\frac{\lambda_{\rm fold}}{\chi_p}.
}
\]

This is an exact reduced-model identity, not an empirical fit.

## 3. Interpretation

`lambda_fold` measures a **static thermal/topological reach**: can the photon suppress the metastable well at all?

`lambda_p` measures a **dynamic fidelity reach**: does the same finite-energy pulse drive the phase into the target basin with probability `p` after finite rise, inertia, causal-environment dynamics and the selected stochastic approximation are included?

The factor

\[
\boxed{D_p\equiv1/\chi_p}
\]

is therefore a dynamic spectral derating factor.

A perfect quasistatic deterministic latch would have `chi_p -> 1` for a threshold-like target and `D_p -> 1`. Any need for extra dynamical margin gives `chi_p>1` and shifts high-fidelity spectral reach to shorter wavelength than the static fold estimate.

## 4. Current numerical illustration

For the current `rDelta=.6`, passive two-pole `R=80 ohm`, `alpha=.90`, 20-ps-rise, symmetrized-FDT TWA screen, the high-statistics 14-um area study establishes `P_final>0.99` through `A=86 um^2`, while the earlier `A=88 um^2` result is below 0.99. The final 86–88 refinement is still running.

These points correspond approximately to

\[
1.63\lesssim\chi_{99}\lesssim1.67,
\]

hence

\[
\boxed{
0.60\lesssim D_{99}\lesssim0.61.
}
\]

The same `rDelta=.6`, `A=100 um^2` static fold-only scale is around `20 um` in the current model, so the predicted dynamic 99%-screening reach is around

\[
\lambda_{99}\sim12.0-12.3\ \mu{\rm m},
\]

consistent with the independent `lambda*A_p=const` translation of the 14-um area threshold.

Again, `P=0.99` here means the present harsh **symmetrized-FDT TWA screening fraction**, not exact physical quantum efficiency. The identity `lambda_p/lambda_fold=1/chi_p` survives a more rigorous bath treatment provided the reduced optical similarity remains valid; only the calibrated value of `chi_p` changes.

## 5. General form with wavelength-dependent absorption

If absorption efficiency changes with wavelength, then

\[
\chi_E(\lambda)
=\frac{\eta_{\rm abs}(\lambda)}{\eta_{\rm abs}(\lambda_{\rm fold})}
\frac{\lambda_{\rm fold}}{\lambda}.
\]

The target condition becomes

\[
\boxed{
\frac{\lambda_p}{\lambda_{\rm fold}}
=
\frac{1}{\chi_p}
\frac{\eta_{\rm abs}(\lambda_p)}
     {\eta_{\rm abs}(\lambda_{\rm fold})}
}
\]

and is implicit if `eta_abs(lambda)` is not known analytically.

This makes optical coupling a clean symmetry-breaking correction to the simple derating law rather than something to hide inside an effective wavelength cutoff.

## 6. Research implication

The useful theoretical target is now not merely `what wavelength can reach the fold?`, but

\[
\boxed{
\text{what determines or bounds }\chi_p
\text{ for a passive metastable flux latch?}
}
\]

The current work suggests `chi_p` depends on the dimensionless thermal rise/cooling groups, normalized CPR topology, and the finite launch/capture dissipation exposures of the causal environment.

No novelty claim is authorized.
