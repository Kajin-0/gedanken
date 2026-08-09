# AGENTS.md — Experiment 02

## Scope

This branch investigates passive gravitational coherent-transfer throughput bounds. It is deliberately separate from Experiment 01 / V7.

Do not modify V7 from this branch unless a concrete technical defect is found. V7 is an inherited source of already-audited lemmas, not an active derivation target.

## Canonical question

Can the V7 speed–efficiency tradeoff be promoted from a two-resonator statement to an integrated spectral bound for arbitrary compact passive nonrelativistic matter coupled through propagating linearized gravity?

## Mandatory order of attack

1. Prove and stress-test the single-resonance linewidth-weighted bound.
2. Derive the actual frequency-domain transfer function for a minimal passive source–propagation–receiver model.
3. Define an unambiguous integrated coherent-transfer metric using `d omega / 2 pi`.
4. Replace single poles by positive quadrupole spectral measures / susceptibilities.
5. Use passivity + EWSR + TT propagation to seek a total spectral bound.
6. Only then map the physical bound to quantum-capacity or entanglement-rate quantities.

Do not skip directly to a capacity theorem.

## Claim discipline

Until proved otherwise:

- `Gamma_kappa` is a linewidth-weighted coherent-transfer scale, **not** a communication capacity.
- `25/16` belongs only to the aligned plus-quadrupole wave-zone specialization.
- The EWSR controls the first positive frequency moment of quadrupole spectral weight; it does not by itself bound an unrestricted `omega^5` gravitational spectrum.
- A broadband theorem must address multiple parallel resonances explicitly.
- Any ultraviolet cutoff must be derived from the declared physical regime or stated as an assumption.
- No priority claim is allowed before a dedicated current literature sweep.

## Research stopping rules

Stop and document rather than hand-wave if any of the following occurs:

- the proposed rate metric depends on an arbitrary bandwidth convention;
- the general bound requires an unphysical hard cutoff with no regime justification;
- a many-mode counterexample exceeds the proposed single-mode ceiling while remaining passive and nonrelativistic;
- the TT propagation map cannot be normalized consistently for arbitrary tensor channels;
- an existing paper already proves the same gravity-specific theorem.

## Concurrency protocol

Before every write:

1. fetch current `main`;
2. confirm V7 has not changed unexpectedly;
3. fetch the current experiment-02 target blob if updating a file;
4. never write with a stale blob SHA;
5. keep writes on `experiment-02-passive-gravitational-throughput` until the research state is mature enough to merge.

## Canonical files

- `README.md` — research program and current headline target.
- `CURRENT_STATE.md` — live result/status ledger.
- `SINGLE_RESONANCE_BOUND.md` — exact first theorem and assumptions.
- `SPECTRAL_GENERALIZATION.md` — arbitrary-response route and known obstacles.
- `LITERATURE_MAP.md` — nearest prior art and collision risks.

## Inherited V7 inputs

Use only the following V7 results unless a new need is demonstrated:

```math
\tau_c(t)=\eta_{\rm prop}\beta_{g,A}\beta_{g,B}\mathcal T_f(t),
\qquad
\beta_{g,j}=\kappa_{g,j}/\kappa_j,
\qquad
0\le\mathcal T_f\le1,
```

and, for passive nonrelativistic matter in the selected narrow band,

```math
\frac{\kappa_{g,j}}{\omega}
\lesssim
\frac23\mathcal C_j\beta_j^3.
```

Everything beyond those inherited inputs should be rederived cleanly for Experiment 02.
