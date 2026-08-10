# Experiment 02 manuscript v1

**Title:** *An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction*

This is the active short specialist manuscript source for Experiment 02 on `main`.

## Scientific status

The manuscript is organized around one result:

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
```

The theorem is established only within its declared compact narrowband retained-sector class. The manuscript does not claim novelty for gravitational-antenna eigenmode theory, integrated resonant-mass response, arbitrary-body modal projection, response sum rules, generic passive `H2` mathematics, generic wave-channel bounds, directivity, or multiple-scattering composition.

The historical/prior-art and manuscript-audit boundaries are maintained in:

- `../HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `../CLAIM_LEDGER.md`
- `../META_REFEREE_SIGNIFICANCE_AUDIT.md`
- `../MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Dedicated GitHub Actions workflow:

`.github/workflows/latex-experiment02.yml`

It compiles the manuscript, fails on unresolved references/citations, and uploads the PDF artifact.

## Scope

Use

```text
omega_0   absolute carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
a_A,a_B   characteristic endpoint radii
R         endpoint separation
Omega     upper physical frequency of retained endpoint modal sector
```

Required asymptotic/model conditions:

```text
k_0 a_A, k_0 a_B << 1
k_0 R >> 1
Omega = omega_0[1+O(B/omega_0)]
finite or countably infinite bounded-port Markov retained modal sectors
```

The simple `omega_0^4` endpoint resource does **not** automatically include uncontrolled higher-frequency modes `omega_n >> omega_0` merely because their off-resonant tails enter a narrow measured band. Such sectors require a separate bound.

Explicitly outside the current theorem:

- broad absolute-frequency operation without retaining frequency-dependent resources;
- uncontrolled higher-frequency off-resonant endpoint sectors;
- arbitrary unbounded PDE boundary ports;
- genuinely non-Markov continua;
- active gain/pumping/feedback;
- extended phased apertures;
- added relays or external gravitational cavities;
- reactive near-field exchange;
- relativistic/nonlinear matter and higher-multipole-dominated regimes.

## Current checkpoint

The first manuscript adversarial scope audit found no `25/12` coefficient failure. It required three clarifications now incorporated in the source:

1. the retained carrier-scale modal-sector condition;
2. explicit `k_0 a << 1` and `k_0R >> 1` geometry conditions;
3. explicit use of positivity to bound the band-limited metric by the full-line `H2` cut.

Fresh CI on the exact scope-hardening head is required before this checkpoint is frozen.

The public manuscript remains `Anonymous`; private author/submission metadata should be added only at the external submission boundary.
