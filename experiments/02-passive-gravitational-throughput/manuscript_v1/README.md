# Experiment 02 manuscript v1

**Title:** *An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction*

This is the first real manuscript source for Experiment 02 on `main`.

## Scientific status

The manuscript is intentionally short and is organized around one result:

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
```

It does not claim novelty for gravitational-antenna eigenmode theory, integrated resonant-mass response, arbitrary-body modal projection, response sum rules, generic passive `H2` mathematics, generic wave-channel bounds, or multiple-scattering composition.

The historical/prior-art boundary is maintained in:

- `../HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `../CLAIM_LEDGER.md`
- `../META_REFEREE_SIGNIFICANCE_AUDIT.md`

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The dedicated GitHub Actions workflow is `.github/workflows/latex-experiment02.yml`.

## Scope

The theorem is a narrowband complex-envelope, leading-wave-zone result for separated compact passive nonrelativistic linear-harmonic endpoints with finite or countably infinite bounded-port Markov modal sectors.

Explicitly outside the current theorem:

- broad absolute-frequency operation without retaining frequency-dependent resources;
- arbitrary unbounded PDE boundary ports;
- genuinely non-Markov continua;
- active gain/pumping/feedback;
- extended phased apertures;
- added relays or external gravitational cavities;
- reactive near-field exchange;
- relativistic/nonlinear matter and higher-multipole-dominated regimes.

The public manuscript remains `Anonymous`; private submission metadata should be added only when the paper reaches the external submission boundary.
