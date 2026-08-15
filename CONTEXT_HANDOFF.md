# CONTEXT_HANDOFF.md — Live Agent Continuity Pointer

**Repository:** `Kajin-0/gedanken`  
**Active research experiment:** `experiments/03-superconducting-photon-flux-transduction/`  
**Updated:** 2026-08-15  
**Mode:** Experiment 03 exploratory theory / falsification-first

> **LIVE `main` ALWAYS WINS.** Other agents may edit concurrently. Before every write, fetch current HEAD, inspect relevant intervening commits, fetch the exact current target blob, and never write from a stale SHA.

## Recovery order

1. root `AGENTS.md` — repository-wide integrity and frozen-track rules;
2. `experiments/03-superconducting-photon-flux-transduction/AGENTS.md`;
3. `experiments/03-superconducting-photon-flux-transduction/CURRENT_STATE.md`;
4. `experiments/03-superconducting-photon-flux-transduction/DERIVATION_LOG.md`;
5. `experiments/03-superconducting-photon-flux-transduction/CLAIM_LEDGER.md`;
6. `experiments/03-superconducting-photon-flux-transduction/ASSUMPTIONS.md`;
7. `experiments/03-superconducting-photon-flux-transduction/LITERATURE_LEDGER.md`;
8. `experiments/03-superconducting-photon-flux-transduction/NOVELTY_GATES.md`.

## One-sentence current state

Experiment 03 asks whether a single absorbed LWIR photon can transiently modify a Josephson phase-escape landscape so that one direction is selected and the event is stored as a persistent superconducting fluxoid state, with ordinary Johnson noise absent from the ideal storage channel and false events instead governed by phase escape, MQT, quasiparticles, vortices, stray photons and readout/reset physics.

## Current strongest mathematical checkpoint

The provisional constant-barrier model produced the exploratory window

```math
\frac{\hbar\omega_p}{7.2}\ln\frac{\Gamma_0}{D}
<\Delta U<
k_BT_{\rm pk}\ln\left[\frac{\Gamma_0\tau}{-\ln(1-\eta)}\right],
```

but this is **not a theorem for the device**. Its prefactors and validity must be recomputed from the actual rf-SQUID/Josephson potential, damping regime, and time-dependent `T_e(t)`.

## Immediate next task

Replace constant barriers with the actual time-dependent model

```text
T_e(t)
 -> I_c[T_e(t)]
 -> U(phi,T_e)
 -> Delta U_+(t), Delta U_-(t), omega_p(t)
 -> competing escape hazards
 -> P_+, P_-, P_0 and dark-count channels.
```

Then map realistic `(L, C, I_c, A, T_0, lambda, bias)` to efficiency, directionality, dark rate, persistent signal and reset/readout constraints.

## Prior-art boundary already known

Do not claim novelty for:

- superconducting single-photon detection in the MIR/LWIR;
- graphene Josephson calorimetric single-photon switching;
- field-free Josephson/superconducting diode effects;
- electromagnetic-illumination-driven superconducting phase batteries, circulating supercurrent, or vorticity switching.

The exact single-LWIR-photon -> directional fluxoid capture -> persistent superconducting memory conjunction and any derived performance bound remain **un-audited**, not novel by default.

## Publication state

**NO manuscript yet.** `experiments/03-superconducting-photon-flux-transduction/NOVELTY_GATES.md` is the manuscript gate.

Experiments 01 and 02 remain frozen/submission tracks; do not modify their science while working Experiment 03.
