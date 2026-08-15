# AGENTS.md — Canonical Repository Recovery Protocol

**Repository:** `Kajin-0/gedanken`

This is the first operational file a new automated contributor should read.

## 1. Research tracks

### Experiment 01 — frozen publication track

`experiments/01-causal-quantum-branch-information/`

Paper: **A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Status: V7 physics is frozen. Work is limited to submission/editorial tasks unless a concrete technical defect appears.

Canonical recovery files:

1. `experiments/01-causal-quantum-branch-information/CURRENT_STATE_REVIEW_CLOSED_V7.md`
2. `experiments/01-causal-quantum-branch-information/CLAIM_LEDGER.md`
3. `experiments/01-causal-quantum-branch-information/manuscript_v7/README.md`
4. `experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md`

Do not reopen closed V7 physics without a concrete contradiction.

### Experiment 02 — frozen theorem / submission-ready track

`experiments/02-passive-gravitational-throughput/`

Underlying validated science/theorem checkpoint:

```text
bfae23af41aefb3104d639099299b3432b4a14fe
```

Validated final submission-manuscript checkpoint:

```text
6f7a60b3b05dea9f288b1b07e6f2e55acaf34e83
```

Status: **GO / submission ready after human sign-off.** Preserve the theorem unless a concrete technical defect, direct prior-art collision, or substantive specialist/journal objection appears.

Canonical recovery order:

1. `experiments/02-passive-gravitational-throughput/FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md`
2. `experiments/02-passive-gravitational-throughput/AGENTS.md`
3. `experiments/02-passive-gravitational-throughput/CURRENT_STATE.md`
4. `experiments/02-passive-gravitational-throughput/CLAIM_LEDGER.md`
5. relevant theorem/collision audits linked there.

The Experiment-02 theorem is explicitly a compact narrowband retained-sector result. Do not drop

```text
B/omega_0 << 1
k_0 a_A, k_0 a_B << 1
k_0 R >> 1
omega_n <= Omega = omega_0[1+O(B/omega_0)]
finite or countably infinite bounded-port Markov retained modal sectors
```

or silently extend the carrier-scale endpoint resource to uncontrolled higher-frequency off-resonant modes.

### Experiment 03 — active exploratory theory track

`experiments/03-superconducting-photon-flux-transduction/`

Working title: **Superconducting Photon-to-Flux Transduction**

Status: **GO for continued theory; NO-GO for manuscript.**

Canonical recovery order:

1. `experiments/03-superconducting-photon-flux-transduction/AGENTS.md`
2. `experiments/03-superconducting-photon-flux-transduction/CURRENT_STATE.md`
3. `experiments/03-superconducting-photon-flux-transduction/DERIVATION_LOG.md`
4. `experiments/03-superconducting-photon-flux-transduction/CLAIM_LEDGER.md`
5. `experiments/03-superconducting-photon-flux-transduction/ASSUMPTIONS.md`
6. `experiments/03-superconducting-photon-flux-transduction/LITERATURE_LEDGER.md`
7. `experiments/03-superconducting-photon-flux-transduction/NOVELTY_GATES.md`

Current question: can a single absorbed LWIR photon transiently modify a Josephson phase-escape landscape so that one direction is selected and the event is stored as a persistent superconducting fluxoid state, with very low intrinsic false switching?

Do not claim novelty for superconducting MIR/LWIR single-photon detection, graphene Josephson calorimetric photon switching, superconducting/Josephson diode behavior, or illumination-driven superconducting phase batteries/vorticity switching; those broad ingredients already have prior art.

The current provisional photon-efficiency/MQT inequality is only an exploratory constant-barrier result. It must be rederived from the exact time-dependent rf-SQUID/Josephson potential and damping model before being treated as a detector bound.

For Experiment 03, every important advance, failed path, architecture change, or literature collision must be recorded in `DERIVATION_LOG.md`; claim status must be synchronized to `CLAIM_LEDGER.md`; the preferred model and immediate next test must be synchronized to `CURRENT_STATE.md`.

Do not create `manuscript_v1/` until `NOVELTY_GATES.md` is passed.

## 2. Mandatory repository-integrity protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch latest `main`;
2. compare with the last-seen head;
3. inspect relevant intervening commits;
4. fetch the exact current target blob immediately before replacing a file;
5. never force a write against a stale blob SHA;
6. if `main` changes during a long task, recheck before writing;
7. preserve concurrent work and prefer narrowly scoped edits;
8. after any important write, fetch the resulting commit and affected files from the actual remote to verify persistence;
9. require fresh CI on the exact resulting science/manuscript head before reporting a validated scientific checkpoint when CI exists.

**Live `main` always overrides conversation history, connector caches, and state snapshots.**

A later documentation-only commit does not replace an explicitly recorded validated science/manuscript SHA.

## 3. Scientific boundaries

### Experiment 01

The publication claim is the source-resolved physical normalization/capability chain, not a new Gaussian-channel theorem. Its standalone Gaussian novelty route is stopped.

### Experiment 02

`Gamma_coh` is a frequency-integrated coherent-transfer spectral area with units `s^-1`; it is not an information capacity.

Generic passive-system mathematics, gravitational-antenna eigenmode theory, integrated resonant-mass response, material sum rules, directivity, generic wave-channel bounds, and multiple-scattering composition are not novelty claims.

Modern gravity-as-communication results are also explicit prior art. The only plausible Experiment-02 publication contribution is the gravity-specific passive far-zone two-ended inertia/sector closure recorded in its canonical files. Do not broaden it to active systems, extended apertures, added relays/cavities, near-field transfer, arbitrary unbounded PDE ports, genuinely non-Markov continua, or uncontrolled high-frequency sectors.

### Experiment 03

Zero DC resistance is not equivalent to zero total fluctuations or zero dark counts. Keep Johnson noise, thermal escape, MQT, quasiparticles, vortices, photon statistics, stray photons, readout and reset physics conceptually separate.

Do not require dissipationless LWIR absorption: the current architecture permits a brief nonequilibrium write event followed by persistent superconducting storage.

Do not classify the device as photovoltaic by default. That terminology is earned only if the final zero-bias directional optical-to-electrical/phase mechanism warrants it.

A negative result is acceptable if it yields a clean bound or falsifies the architecture. Do not force the original idea to survive.

## 4. Reproducibility and provenance

- Conversation-only descriptions of branches, commits, calculations, files, workflow runs or literature results are not repository provenance.
- Numerical checkpoints must record assumptions and units.
- If a calculation becomes load-bearing, add a reproducible script/test rather than leaving only hand arithmetic.
- Literature claims should be tied to primary sources in the experiment's ledger.
- Never report a scientific checkpoint as validated before its actual remote state and relevant tests are verified.

## 5. Global prohibitions

Do not:

- invent branches, commits, workflow runs, files, citations or validation states;
- use `first`, `new`, `unique`, `unprecedented`, or similar priority language without dedicated evidence;
- modify frozen Experiment-01 or Experiment-02 science merely to align with Experiment 03;
- silently broaden a theorem's scope;
- let an important new result live only in conversation history;
- create a manuscript for Experiment 03 before the quantitative and novelty gates are passed.
