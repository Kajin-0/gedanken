# External Review Packet — Experiment 02

**Purpose:** obtain scrutiny that is independent of the internal AI research/audit pipeline before any further theorem broadening or final journal submission.

**Authoritative scientific snapshot:** `1ce596493073dbb49e6eb71f1a6df0566ff3c25b`.

The current repository may contain later editorial/submission files, but reviewers should evaluate the scientific claims against the frozen snapshot above.

## Review design: blind first, comparison second

The goal is not to ask a reviewer to confirm our derivation. The goal is to give them a fair chance to reproduce, weaken, or break the relevant claim before they see how the repository derived it.

### Pass 1 — independent reconstruction

1. Read only the relevant packet in this directory.
2. Do **not** read the repository derivation, manuscript, claim ledger, internal audits, numerical verification code, or prior review notes yet.
3. Starting from the stated assumptions and normalization, independently derive the strongest result you think is justified.
4. Record any counterexample, missing hypothesis, normalization ambiguity, or coefficient disagreement before seeing the repository proof.

### Pass 2 — hostile comparison

After completing Pass 1, inspect the specified frozen derivation files at scientific SHA `1ce596493073dbb49e6eb71f1a6df0566ff3c25b` and compare line by line against your independent result.

The desired output is not a general opinion. It is one of:

- **no concrete defect found**;
- **correct after adding/changing a stated hypothesis**;
- **coefficient/normalization defect**, with the corrected expression;
- **logical gap**, identifying the exact inference that fails;
- **counterexample**, with enough detail to reproduce it;
- **exact prior-art collision**, with a primary-source citation and the matching theorem/equations.

## Packets

### Stage A — passive selected-port cut

Use `STAGE_A_CONTROL_THEORY_PACKET.md`.

Ideal reviewer background: linear systems/control, passive scattering systems, `H_2` norms, dissipativity, Lyapunov/Gramian methods. No gravity background is needed.

### Stages B/C — gravitational endpoint resource and TT propagation

Use `STAGE_BC_GRAVITY_PACKET.md`.

Ideal reviewer background: linearized-gravity radiation, resonant-mass/gravitational-wave antenna theory, elastic normal modes, quadrupole normalization, TT polarization projection, and far-zone propagation.

## Independence standard

A useful external check should not merely rerun the repository scripts or ask another model to summarize the existing derivation. The strongest signal comes from an independent reconstruction performed before reading the proof.

If an AI system is used as an external checker, it should be a genuinely separate model/provider/session that has not been given the internal derivation before its Pass-1 result is frozen. Record the model/provider/version and prompt used so the provenance is explicit.

## What does and does not reopen the theorem

A concrete mathematical contradiction, normalization defect, missing hypothesis, or exact prior-art theorem collision reopens only the affected layer.

A request to make the theorem broader—for example to cover uncontrolled modes with `omega_n >> omega_0`—does not by itself constitute a defect in the current theorem, because those modes are explicitly outside the retained carrier-scale scope. Such extensions remain future work unless an external reviewer shows that the present scope statement is internally inconsistent.

## After external review

If Stage A and Stages B/C survive independent review, the remaining pre-submission work is editorial: one honest numerical scale example, final human sign-off, archival DOI/release, metadata, disclosure, and submission to the selected journal.
