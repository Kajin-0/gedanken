# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** none; do not create one until `NOVELTY_GATES.md` is passed.

## Recovery order

Read, in order:

1. `CURRENT_STATE.md`
2. `DERIVATION_LOG.md`
3. `CLAIM_LEDGER.md`
4. `ASSUMPTIONS.md`
5. `LITERATURE_LEDGER.md`
6. `NOVELTY_GATES.md`
7. `README.md`

Conversation history is not authoritative when it conflicts with repository state.

## Current objective

Determine whether a single absorbed LWIR photon can be mapped with high probability to a persistent, directionally selected superconducting fluxoid state while keeping intrinsic false-switch probability extremely low.

The current minimal model is an rf-SQUID-like loop with a photon-sensitive Josephson element. Generation A may use external flux bias. Generation B seeks intrinsic directionality through a phi0 / Josephson-diode / inversion-breaking element.

## Mandatory discipline

1. Separate established background from derived model results, numerical extrapolations, and novelty hypotheses.
2. Update `CLAIM_LEDGER.md` whenever a claim is strengthened, weakened, falsified, or collision-tested.
3. Update `DERIVATION_LOG.md` after each important logical step, including failed paths and why they failed.
4. Update `CURRENT_STATE.md` when the preferred architecture, governing equations, or next decisive test changes.
5. Add primary literature to `LITERATURE_LEDGER.md`; do not rely on uncited conversation memory for state-of-the-art claims.
6. Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority language before a dedicated collision audit.
7. Do not equate zero DC resistance with zero total fluctuations or zero dark counts.
8. Do not treat the provisional Kramers/MQT prefactors as exact for the proposed device. Recompute escape actions from the actual potential and damping model.
9. Do not call the architecture photovoltaic as a settled classification until the zero-bias energy/charge/phase conversion mechanism is explicit.
10. Do not create a manuscript because a parameter window looks promising. Survive the novelty and falsification gates first.

## Immediate work queue

1. Derive the exact rf-SQUID potential for the chosen weak link and bias configuration.
2. Define a physically consistent `I_c(T_e)` or nonequilibrium Josephson relation for the photon pulse.
3. Solve `T_e(t)` including realistic electronic heat capacity and electron-phonon cooling.
4. Compute `Delta U_+(t)`, `Delta U_-(t)`, attempt frequencies, damping regime and escape actions.
5. Integrate competing hazards to obtain `P_+`, `P_-`, `P_0` per absorbed photon.
6. Compute independent dark channels: thermal activation, MQT, residual quasiparticles, vortices, stray photons and readout backaction.
7. Map `(L,C,I_c,A,T_0,lambda,bias)` to efficiency, DCR, directionality, recovery and stored-signal magnitude.
8. Only after a realistic nonempty region survives, perform a hostile architecture/theorem collision audit.

## Stop conditions

Stop or reformulate the branch if any of the following is shown robustly:

- the photon-induced perturbation required for reliable flux capture necessarily destroys the metastable storage state;
- the exact MQT/thermal action closes the apparent photon/dark-rate window for all plausible parameters;
- reset/readout necessarily reintroduces a noise/dissipation penalty eliminating the claimed operating distinction;
- prior art already contains substantially the same single-photon-to-persistent-directional-flux architecture and no independent theorem/performance result survives;
- realistic LWIR optical coupling and heat capacity make the required hot-state excursion incompatible with the superconducting/Josephson operating regime.

A negative result can itself be valuable if it yields a clean bound. Record it rather than forcing the original concept to survive.
