# Novelty and Scope — Reviewer Sheet

## The one claim being tested

The manuscript's candidate contribution is **not** any individual gravitational-antenna, sum-rule, passive-network, or wave-propagation ingredient.

It is the complete gravity-specific two-ended closure

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B),
}
```

which eliminates passive device-specific variables and bounds the frequency-integrated coherent source-to-receiver transfer only by frequency, separation, and the smaller endpoint inertia resource.

## Explicitly NOT claimed as new

The manuscript treats all of the following as prior art / established methodology:

- gravitational generator--receiver calculations;
- resonant-mass gravitational antenna eigenmodes;
- gravitational emission/reception reciprocity;
- quadrupole-controlled oscillator strength;
- quality-factor-independent integrated or short-pulse antenna response;
- compact quadrupole directivity and the `D = 5/2` maximum;
- gravitational absorption / susceptibility / response sum-rule methods;
- STF tidal-force projection onto elastic modes;
- modal participation and equivalent modal mass completeness;
- finite- or infinite-dimensional passive `H2` / Gramian machinery;
- singular source--receiver wave channels;
- two-body material-response + Green-operator transfer bounds;
- Redheffer / multiple-scattering composition;
- generic efficiency--bandwidth tradeoffs;
- quantum mechanics as the origin of the headline ceiling.

The exact `sum_n M A_Gn <= 40 I / 3` form was not found explicitly in the inspected literature, but it is intentionally **not** positioned as the paper's principal novelty because its derivation is a short gravitational specialization of historical tidal-mode formalism plus standard completeness.

## What appears not to have been found

No inspected primary source has been found to state the complete chain

```text
passive selected-port spectral-area cut
-> source gravitational coupling trace
-> receiver gravitational coupling trace
-> inertia closure of BOTH endpoint traces
-> normalized compact TT propagation
-> explicit two-ended inertia-only spectral-area ceiling.
```

A targeted search also did not find a historical result with the same final dimensional fingerprint

```math
\Gamma \sim \frac{G\omega^2 I}{c^3R^2}
```

after eliminating antenna-specific `Q`, effective masses, oscillator strengths, mode count, and matching parameters.

This is a **negative search result, not a priority claim**.

## Included physical class

The theorem is restricted to:

- weak linearized gravity;
- separated compact endpoints;
- nonrelativistic linear-harmonic matter;
- leading mass-quadrupole coupling;
- passive time-invariant endpoint dynamics;
- direct propagating TT wave-zone transfer;
- finite or countably infinite bounded-port Markov modal sectors;
- arbitrary coherent passive mode mixing;
- passive reciprocal returns between the same two endpoints at the retained leading wave-zone order.

## Excluded architectures

The theorem does not cover:

- active gain, inversion, or parametric/time-dependent drive;
- extended phased gravitational apertures;
- added relays, mirrors, repeaters, or engineered external cavities;
- reactive near-field gravitational exchange;
- higher-multipole or relativistically beamed sources;
- strongly self-gravitating systems;
- materially nonlinear motion;
- arbitrary unbounded PDE boundary-control ports without admissibility analysis;
- genuinely non-Markov matter continua;
- curved-background focusing/lensing;
- a universal gravitational quantum-capacity theorem.

## What the reviewer should decide

The useful external judgment is one of the following:

1. **Incorrect:** a concrete theorem step fails or a counterexample exists inside the stated class.
2. **Already known:** a primary source contains the same complete inertia-closed two-ended result, possibly in older notation.
3. **Correct but incremental:** the closure follows so immediately from known ingredients that it does not constitute a meaningful specialist result.
4. **Legitimate specialist contribution:** the ingredients are known but their closed gravitational consequence is both previously unstated and physically informative.
