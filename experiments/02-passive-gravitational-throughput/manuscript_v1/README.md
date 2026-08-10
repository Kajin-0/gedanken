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

The theorem is established only within its declared compact narrowband retained-sector class. The manuscript does not claim novelty for gravitational-antenna eigenmode theory, integrated resonant-mass response, arbitrary-body modal projection, response sum rules, generic passive `H2` mathematics, generic wave-channel bounds, directivity, multiple-scattering composition, or gravity-mediated communication/state-transfer bounds in general.

The historical/prior-art and manuscript-audit boundaries are maintained in:

- `../RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`
- `../HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `../CLAIM_LEDGER.md`
- `../META_REFEREE_SIGNIFICANCE_AUDIT.md`
- `../MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`
- `../MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md`

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

## Recent literature-framing correction

A post-freeze audit identified an omission in the novelty review: the manuscript had not directly engaged the recent gravity-as-communication line represented by Kafri--Milburn--Taylor (2015), Lami--Pedernales--Plenio (2024), Toccacelo--Andersen--Brask (2025), and Mari--Zippilli--Vitali (2026).

The current source now cites those papers explicitly and states that gravity-mediated communication, communication/classicality bounds, and state-transfer benchmarks are historical. The remaining candidate contribution is only the passive separated-TT frequency-integrated two-ended `I_2` closure.

This patch does not alter the theorem derivation. Fresh exact-head CI is required before the manuscript freeze is restored.

The public manuscript remains `Anonymous`; private author/submission metadata should be added only at the external submission boundary.
