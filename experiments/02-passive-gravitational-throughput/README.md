# Experiment 02 — Passive Gravitational Throughput

**Status:** internally frozen theorem and literature-corrected manuscript; external specialist/journal review pending.  
**Authoritative validated science/manuscript SHA:** `1ce596493073dbb49e6eb71f1a6df0566ff3c25b`.  
**Current submission target:** Physical Review D Research Article.

## Result

For two separated compact passive nonrelativistic linear-harmonic matter systems in weak leading mass-quadrupole gravity, define

```math
\Gamma_{\rm coh}
=\frac{1}{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

Within the declared retained-sector model,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
}
```

with

```math
I_2=\int\rho r^2\,d^3x.
```

`Gamma_coh` has units `s^-1`. It is a coherent-transfer spectral area, not an information capacity, bit rate, or detector strain-noise spectral density.

## Physical interpretation

The theorem is a passive resource/no-go statement. Resonances, high `Q`, additional retained modes, passive unitary mode mixing, endpoint matching, and repeated passive returns can reshape the transfer spectrum, but they cannot raise its leading integrated ceiling beyond the smaller endpoint gravitational resource and the compact transverse-traceless propagation channel.

The intended significance is conceptual rather than near-term experimental. For ordinary macroscopic mechanical frequencies, simultaneously satisfying compact endpoints and `k_0R >> 1` can require very large separations, while the resulting gravitational transfer is extremely weak. The manuscript therefore does **not** present the theorem as a practical detector-sensitivity result or a near-term measurement proposal.

Do not interpret `1/Gamma_coh` as a waiting time for one bit; no information-capacity theorem or signaling protocol has been derived here.

## Scope

The established theorem requires

```text
B/omega_0 << 1
k_0 a_A, k_0 a_B << 1
k_0 R >> 1
omega_n <= Omega = omega_0[1+O(B/omega_0)]
finite or countably infinite bounded-port Markov retained modal sectors
```

It explicitly excludes uncontrolled high-frequency off-resonant sectors, broad absolute-frequency operation represented by one carrier coefficient, active gain/pumping/feedback, extended phased apertures, added gravitational relays or external cavities, reactive near-field exchange, arbitrary unbounded PDE boundary ports, genuinely non-Markov continua, and relativistic/nonlinear/higher-multipole-dominated regimes.

## Validation status

The theorem/manuscript SHA above passed the six dedicated physics regressions and the manuscript build on that exact head. The repository also contains hostile prior-art, normalization, recurrence, infinite-modal, and manuscript-scope audits.

This is **internal validation**, not external verification. The next epistemic step is specialist/journal peer review. A clean internal pipeline cannot establish priority or substitute for independent expert review.

## Start here

1. `INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md` — frozen theorem/manuscript checkpoint and exact-head validation.
2. `CURRENT_STATE.md` — current theorem, proof spine, exclusions, and research stop condition.
3. `CLAIM_LEDGER.md` — established, failed, historical, and open claims.
4. `RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md` — recent gravity-communication near-collision audit.
5. `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md` — broader historical collision audit.
6. `META_REFEREE_SIGNIFICANCE_AUDIT.md` — significance/referee-risk analysis.
7. `manuscript_v1/` — authoritative frozen manuscript source.
8. `SUBMISSION_STRATEGY_2026-08-10.md` — journal-fit and submission strategy.
9. `submission_prd/` — PRD-specific submission copy and submission materials.
10. `external_review/` — blind-first Stage-A and Stage-B/C packets for independent scrutiny.
11. `AGENTS.md` — repository recovery and freeze protocol.

`QUESTION.md`, `HYPOTHESES.md`, and early derivation files preserve the research history. Their provisional language should not be mistaken for the current claim state.

## Provenance

Conversation history is not repository evidence. Only files, commits, workflow results, and primary literature actually verified against the repository/remote count as provenance.

The complete two-ended closure is the only plausible publication contribution. No exact equivalent was found in the inspected literature, but that negative search is not proof of priority.
