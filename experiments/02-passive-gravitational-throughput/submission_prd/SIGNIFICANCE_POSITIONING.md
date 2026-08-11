# Significance Positioning — PRD

## Strongest defensible framing

Experiment 02 is a **conceptual passive-resource/no-go theorem** for propagating linearized gravity. Its value is not near-term experimental accessibility; it removes a large class of passive engineering degrees of freedom from the leading frequency-integrated ceiling.

Within the theorem class, high quality factor, additional retained resonances, passive mode hybridization, endpoint asymmetry, and same-two-endpoint recurrence can reshape spectral transfer but cannot raise the leading far-zone ceiling beyond

```math
\Gamma_{\rm coh}
\lesssim
\frac{5G\omega_0^2}{4c^3R^2}
\min(I_{\hat R,A},I_{\hat R,B})
```

for a retained carrier-scale narrow band. The earlier scalar `25/12 * I_2` result remains a valid looser corollary and should be described as such, not as an error.

## What `Gamma_coh` means

`Gamma_coh` is the band-limited squared `H2` norm of the selected transfer block: the integral of power transmissivity over envelope detuning. With energy-normalized ports and a spectrally flat input PSD `S_in` across the retained band, the corresponding transmitted output power is `S_in Gamma_coh`.

It has units `s^-1`, but it is **not** an information rate, bit rate, detector sensitivity, waiting time, or strain-noise PSD. It becomes an information-theoretic quantity only after adding a noise model and signaling protocol.

## Concrete scale

For a uniform sphere,

```math
I_{\hat R}=2Ma^2/5,
\qquad
Z_{\hat R}=Ma^2/5,
```

so for equal endpoints

```math
\Gamma_{\rm coh}
\lesssim
\frac{G\omega_0^2Ma^2}{2c^3R^2}.
```

For `M=1000 kg`, `a=1 m`, `f_0=1 kHz`, and `k_0R=100`, one has `R≈4.77e6 m` and

```text
Gamma_coh ≲ 2.15e-39 s^-1.
```

This is not a one-event or one-bit waiting-time estimate. It demonstrates that the macroscopic mechanical far-zone ceiling is extraordinarily weak and reinforces the structural, rather than experimental, significance claim.

## Why the sector refinement matters

The old scalar proof multiplied the full endpoint quadrupole resource by an independently optimized TT propagation ceiling. The current proof resolves the endpoint quadrupole resource into propagation-defined STF sectors before closing the passive trace. Only `|m|=2` survives at leading `R^-2` power order, so the leading resource becomes the conventional separation-axis inertia `I_Rhat` and the coefficient tightens from the scalar `25/12` form to `5/4`.

This refinement has been checked against the older theorem with an explicit cross-version regression. The older bound remains the fallback if a future defect is found specifically in the sector-weighted step.

## Dominant referee risk

The most likely substantive publication objection is significance:

> Once historical resonant-mass response, arbitrary-body modal theory, material sum rules, generic passive `H2`, antenna/matching limits, and wave-propagation bounds are credited, is the residual complete two-ended closure sufficiently nontrivial to merit publication?

The response should emphasize the elimination accomplished by the final theorem: passive internal architecture at **both** endpoints collapses to geometry-resolved inertia resources while the separated TT link supplies the propagation cut.

## Scope discipline

Do not broaden beyond compact, retained-modal, separated-wave, passive weak-field assumptions. In particular:

- higher-frequency off-resonant sectors require separate frequency-dependent control;
- `omega R/c` outside the wave-zone regime is outside the propagation theorem;
- active systems, relays, external cavities, and extended phased apertures are outside scope;
- reduced non-Markovianity alone is not an exclusion if an admissible enlarged passive realization exists;
- arbitrary hereditary/singular continuum models and unbounded distributed ports remain unproved until the needed realization, admissibility, and gravitational finite-trace conditions are established.

## What to emphasize

The result is a clean gravity-specific cut/resource law: within the declared class, passive resonant engineering can reshape the spectrum but cannot manufacture additional cumulative endpoint quadrupole resource or evade the smaller two-ended separation-axis resource.
