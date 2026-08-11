# Recovery Index — Experiment 02

**Purpose:** single-entry handoff for any new agent resuming this research track. Read this before older audits or derivation notes.

## 1. Canonical state

Current validated **science/manuscript** checkpoint:

```text
bfae23af41aefb3104d639099299b3432b4a14fe
```

Later commits may change tests, audits, or recovery documentation without changing the manuscript checkpoint. Always fetch the live `main` head and distinguish documentation/test commits from a validated science/manuscript SHA.

Submission theorem status: **GO / frozen unless a concrete technical defect, direct prior-art collision, or substantive external objection reopens it.**

The physics article must never mention source-control infrastructure, commit hashes, internal experiment labels, CI, or project bookkeeping.

## 2. Current result

Operational quantity:

```math
Gamma_coh=(1/2pi) int_B Tr[T^dag T] dnu
```

It is a coherent-transfer spectral area with units `s^-1`, not capacity, bit rate, waiting time, detector sensitivity, or a noise PSD.

Define the source-receiver axis `Rhat` and

```math
I_Rhat = int rho [r^2-(Rhat.x)^2] d^3x,
Z_Rhat = int rho (Rhat.x)^2 d^3x,
I_2 = I_Rhat+Z_Rhat.
```

For the retained passive endpoint realization and compact outgoing quadrupolar TT propagation model, the strongest finite-band closure is

```math
Gamma_coh <= [G Omega^4/(5 c^5)] min[G_A(R),G_B(R)]
```

with exact STF-sector propagation weights. In the far zone only the `|m|=2` sector survives at order `R^-2`, giving

```math
limsup_{R->infty} R^2 Gamma_coh
<= [5 G Omega^4/(4 c^3 omega_-^2)]
min(I_Rhat,A,I_Rhat,B).
```

For a carrier-scale narrow retained band,

```math
Gamma_coh lesssim
[5 G omega_0^2/(4 c^3 R^2)]
min(I_Rhat,A,I_Rhat,B).
```

The former scalar headline remains a **valid looser corollary**:

```math
Gamma_coh lesssim
(25/12) [G omega_0^2/(c^3R^2)] min(I_2,A,I_2,B).
```

It is superseded only as the strongest current leading closure. Do not call the scalar result false, and do not restore it as the strongest theorem unless the sector-resolved refinement fails a future audit.

## 3. Proof chain that has been independently checked

1. **Passive selected-port cut.** Stable strictly proper passive cross-port blocks obey the `H2` Gramian bound. Weighted form permits angular-sector weighting before taking the endpoint trace.
2. **Endpoint gravitational resource.** On-shell modal linewidth is

```math
kappa_g,n=[G omega_n^4/(5c^5)](q_n:q_n)/mu_n.
```

3. **Sector completeness.** Relative to `Rhat`,

```math
sum Q_2^2/mu <= 4 I_Rhat,
sum Q_1^2/mu <= 2 I_Rhat+4 Z_Rhat,
sum Q_0^2/mu <= (2/3)I_Rhat+(8/3)Z_Rhat.
```

These recover `(20/3) I_2` when summed.
4. **Compact TT propagation.** Exact outgoing sector powers `eta_2,eta_1,eta_0` are known; their leading far-zone orders are `R^-2`, `R^-4`, `R^-6` in power.
5. **Two-ended closure.** The source and receiver cuts combine through the minimum endpoint resource.
6. **Infinite-dimensional extension.** Countably infinite separable passive modal realizations are covered when the required operators are well posed/admissible and the retained gravitational observation is finite-trace/Hilbert-Schmidt.
7. **Same-endpoint recurrence.** Passive repeated reflections cannot modify the leading `R^-2` coefficient because each round trip contains two small propagation factors.

## 4. Chronology of major objections and what happened

### A. Generic passive-system / novelty concern

**Angle tried:** Is the result merely Bode-Fano / Chu-Harrington / generic `H2` theory in gravitational notation?

**Disposition:** generic passivity, gain-bandwidth, antenna size-bandwidth, directivity, and infinite-dimensional `H2` machinery are historical and are **not** claimed as novelty. The publication candidate is the gravity-specific two-ended endpoint-resource + STF-sector + compact-TT closure.

Relevant files:
- `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `META_REFEREE_SIGNIFICANCE_AUDIT.md`
- `RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`

### B. Reviewer arithmetic / physics claims that were rejected

The following hostile-review claims were independently checked and rejected:

- using a second rather than third time derivative in the gravitational quadrupole power;
- a claimed Paik-Wagoner `1/Q` integrated-response scaling;
- a bar-radiation example placing the receiver on the longitudinal bar axis, where the ideal quadrupole actually has a null;
- several visual/source complaints that were artifacts of rendered line breaks rather than manuscript errors.

Relevant file:
- `CRITICAL_REVIEW_AUDIT_2026-08-10.md`

### C. Asymptotic theorem wording

**Concern:** the earlier headline used `lesssim` while the propagation result was a far-zone `limsup`.

**Accepted.** The rigorous theorem is now stated as an asymptotic coefficient, while the carrier form is explicitly a leading narrowband expression. Exact compact-TT finite-`kR` sector corrections were derived instead of inventing a universal remainder.

Relevant file:
- `SECOND_CRITICAL_REVIEW_AUDIT_2026-08-10.md`

### D. Carrier-frozen propagation

**Concern:** freezing the propagator at `omega_0` left an unquantified `O(B/omega_0)` band error.

**Accepted and removed.** The propagation operator is retained across the actual measured physical-frequency band through sectorwise band suprema.

### E. Independent endpoint/directivity maximization

**Concern:** multiplying a scalar endpoint quadrupole ceiling by an independently optimized TT directivity ceiling was unnecessarily loose.

**Accepted and materially strengthened.** Resolving STF quadrupole space into `m=0`, `|m|=1`, `|m|=2` before closing the passive trace produced the stronger leading `5/4 * I_Rhat` result while retaining the old `25/12 * I_2` result as a looser scalar corollary.

This is the most important theorem improvement triggered by adversarial review and, because it changed a longstanding constant after a context handoff, it is also subject to the dedicated cross-version audit in item L below.

Relevant files:
- `SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md`
- `CONSTANT_REGRESSION_AUDIT_2026-08-10.md`

### F. Tightness / resonant-bar comparison

**Concern:** the endpoint completeness bound might be so loose as to be physically meaningless.

**Checked.** For the ideal slender free-free bar fundamental in its maximum-radiation transverse direction, the single mode uses

```math
48/pi^4 ~= 0.493
```

of the complete leading `|m|=2` endpoint resource. Thus the projection/completeness step is not loose by many orders of magnitude, although a complete two-ended device can still sit far below the ceiling because of matching, loss, accessibility, the second endpoint, etc.

The earlier scalar-resource comparison `~0.394` is superseded by the more relevant sector-resolved `~0.493` comparison.

### G. Historical cross-section comparison

**Angle tried:** directly equate `Gamma_coh` to Weber/Paik/Wagoner-style absorption cross sections.

**Not adopted.** Their normalizations and observables are not identical. The manuscript uses a self-contained bar-resource comparison rather than asserting a questionable numerical identity.

### H. High-frequency off-resonant modes / retained modal ceiling

**Concern:** completeness alone does not control arbitrarily high physical modal frequencies.

**Real and still open.** The on-shell `omega_n^4` linewidth must not be copied unchanged into a far-detuned low-frequency tail. But unweighted completeness also cannot control the unrestricted fourth modal-frequency moment. Removing `omega_n<=Omega` from the inertia-controlled theorem requires additional constitutive/elastic regularity, microscopic cutoff information, or a different frequency-domain sum rule.

This is currently the strongest unresolved mathematical frontier.

### I. Non-Markovian / continuum objection

**Concern:** real crystals or continuum elasticity might be excluded because reduced dynamics can have memory.

**Reviewer framing was too broad.** A finite crystal is not automatically a frequency continuum, and a memory kernel can arise by eliminating passive degrees of freedom from a larger local-in-time system. Reduced non-Markovianity is therefore not itself an escape from the theorem.

What remains unproved is universality for arbitrary hereditary media, singular continuum baths, or unbounded boundary-control/observation systems unless an admissible passive realization and finite gravitational-trace/resource closure are established.

Relevant files:
- `NON_MARKOVIAN_CONTINUUM_SCOPE_AUDIT_2026-08-10.md`
- `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`

### J. Same-endpoint recurrence

**Concern:** near-unit endpoint reflectivity might make repeated reflections invalidate the leading coefficient.

**Rejected.** The loop contains two propagation factors. In the separated far zone the round-trip norm remains parametrically small even if endpoint reflection blocks have unit norm. The resolvent inequality is exact in its stated domain; the Taylor expansion only identifies correction order.

Relevant file:
- `PASSIVE_TWO_ENDPOINT_RECURRENCE.md`

### K. Quantum-communication framing

**Concern:** opening with gravity-as-communication literature invited a capacity/information-theoretic interpretation that the paper does not deliver.

**Accepted as presentation issue.** The introduction was narrowed toward passive resonant transduction, integrated response, and gain-bandwidth structure. Quantum-information papers remain only as contextual prior work; their criteria are not used in the proof.

### L. Context-window continuity / theorem-constant regression audit

**Concern:** the longstanding `25/12` coefficient changed to `5/4` soon after a new session resumed the project, raising the possibility of churn or an unnoticed normalization regression.

**Concern accepted as a change-control issue and re-audited from the pre-change theorem.** The audit found one real process defect: when the sector-resolved theorem was introduced, shorter new sector regressions replaced some broader inherited randomized end-to-end and scalar-resource tests. That loss of coverage was not acceptable.

The mathematical transition was then re-tested independently rather than trusted from the current derivation. The new self-contained regression checks both theorem generations: the original randomized `25/12` end-to-end link, scalar and sector Parseval/Bessel identities, modal mixing, weighted linewidth, TT kernels from direct projector integration, outgoing overlap formulas, and a randomized five-sector end-to-end passive link.

**Disposition:** no scientific contradiction in `5/4` was found. The `25/12 * I_2` inequality still passes as a valid scalar fallback, while `5/4 * I_Rhat` survives as the tighter directional refinement. The important correction was to validation discipline: new theorem tests must accumulate on top of inherited regressions rather than replace them.

Permanent infrastructure:
- `CONSTANT_REGRESSION_AUDIT_2026-08-10.md`
- `numerics/verify_constant_regression.py`
- `.github/workflows/experiment02-constant-regression.yml`

The dedicated cross-version workflow passed on documentation/test head `968718c0c96934e1eee44bdd09576ecd35b62c9b` as run `31455758548`. This does **not** create a new manuscript/science checkpoint; the validated manuscript remains `bfae23af...`.

## 5. Open questions — do not pretend these are solved

1. **Whole-spectrum inertia closure:** remove the retained modal ceiling without an uncontrolled fourth-frequency moment.
2. **Constitutive realizability/tightness:** determine how closely realistic elastic bodies can approach abstract sector-Parseval saturation while respecting material mechanics.
3. **Continuum/admissibility extension:** prove the passive cut plus gravitational finite-trace closure for broader unbounded distributed models where needed.
4. **Engineering relevance:** the passive gravitational scale is extraordinarily small; the theorem is primarily structural, not a near-term detector-design ceiling.
5. **Noise/information theory:** no thermodynamic or quantum noise model is part of `Gamma_coh`; capacity/bit-rate questions remain separate.

## 6. Dead ends / claims not to resurrect

Do not reintroduce any of the following as established claims:

- generic passive `H2` mathematics as the novelty;
- the former `25/12 * I_2` bound as the strongest theorem **or** describe it as invalid; it remains the scalar fallback;
- carrier-frozen propagation as the preferred derivation;
- an unrestricted all-frequency inertia bound from completeness alone;
- the on-shell `omega_n^4` linewidth applied unchanged to far-detuned tails;
- a blanket statement that all non-Markovian reduced dynamics or all continuum elasticity lie outside the theorem;
- a numerical identification of `Gamma_coh` with historical absorption cross sections without normalization derivation;
- a capacity, bit-rate, waiting-time, or noise interpretation of `Gamma_coh`;
- near-unit endpoint reflectivity as a loophole in the separated far-zone recurrence proof;
- priority language such as `first`, `unique`, `unprecedented`, or equivalent;
- replacement of inherited regressions with narrower tests tailored only to a new decomposition.

## 7. Validation record for current manuscript checkpoint

Science/manuscript SHA:

```text
bfae23af41aefb3104d639099299b3432b4a14fe
```

Passed:

```text
TT propagation     run 31454245214
endpoint resource  run 31454245215
PRD manuscript     run 31454245216
infinite modal     run 31454245221
recurrence         run 31454245237
combined bound     run 31454245240
passive cut        run 31454245251
```

Compiled artifact:

```text
experiment02-prd-submission
artifact ID 9087453835
SHA256 5ef8720af89dd76d515adb852df951aa72d9bb439935638556b4ba4516df2e81
```

The exact-head PDF was visually preflighted as 9 pages with embedded fonts and no unresolved references/citations.

Post-checkpoint validation infrastructure additionally includes the cross-version theorem-constant regression. On documentation/test head `968718c0c96934e1eee44bdd09576ecd35b62c9b`, all seven triggered physics/test workflows completed without failure, including cross-version run `31455758548`. These later test/documentation commits do not alter the manuscript PDF.

## 8. Recovery reading order

After this file, read:

1. `CURRENT_STATE.md` — concise canonical theorem and current research mode.
2. `CLAIM_LEDGER.md` — established / failed / historical / open claims.
3. `CONSTANT_REGRESSION_AUDIT_2026-08-10.md` — mandatory cross-version audit of the `25/12 -> 5/4` transition and permanent theorem change-control rules.
4. `NON_MARKOVIAN_CONTINUUM_SCOPE_AUDIT_2026-08-10.md` — latest scope correction.
5. `SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md` — derivation transition from scalar to sector-resolved theorem. Its recorded SHA is a historical checkpoint, not the current manuscript SHA.
6. `SECOND_CRITICAL_REVIEW_AUDIT_2026-08-10.md` and `CRITICAL_REVIEW_AUDIT_2026-08-10.md` — reviewer objections and independent dispositions.
7. `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`, `RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`, `META_REFEREE_SIGNIFICANCE_AUDIT.md` — novelty/significance boundaries.
8. `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`, `PASSIVE_TWO_ENDPOINT_RECURRENCE.md`, and the endpoint/TT derivation files for proof detail.
9. `submission_prd/README.md` and `submission_prd/HUMAN_SIGNOFF_CHECKLIST.md` for submission-only status.

## 9. Operating rule for the next agent

Before changing science, identify the exact current objection and check whether it already appears in this index or the claim ledger. Do not repeat a dead-end path merely because an older derivation file predates the current theorem.

Any proposed change to a coefficient, normalization, endpoint resource, asymptotic order, or headline inequality must first preserve and pass inherited regressions, add an independent regression for the new step, include an end-to-end test for an end-to-end theorem, and document its exact relationship to the old theorem. A context reset or new reviewer prompt is not evidence that a validated result needs changing.

If a new objection survives independent derivation/literature checking, update this index together with the relevant audit, claim ledger, current state, and manuscript checkpoint so handoff remains lossless.
