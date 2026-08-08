# PRD Pre-Submission Checklist — V7

**Manuscript:** `manuscript_v7/`

## A. Scientific gates — COMPLETE

- [x] Conserved finite-support source specified to working elastic order.
- [x] Internal controller architecture explicit.
- [x] Controller propagation made local through finite-speed bus field.
- [x] Controller clearing/handoff distinguished from modal idealization.
- [x] Full encoded system audited for equal Poincare charges.
- [x] Gravitational dressing statement restricted to first-order equal-charge code.
- [x] Encoder precursor retained rather than reset at handoff.
- [x] Fixed post-handoff virtual bosonic mode derived.
- [x] Four-factor link independently checked against cascaded bosonic network.
- [x] $25/16$ propagation normalization checked by retarded-field, reciprocal-absorption, and canonical TT one-graviton routes.
- [x] Source dephasing separated from energy branching.
- [x] Memory channel separated from accessible readout.
- [x] Exact pure-loss reference-receiver negativity derived.
- [x] Weak-link asymptotic checked numerically.
- [x] Passive EWSR coefficient independently checked.
- [x] EWSR and graviton-absorption prior art cited.
- [x] Active/collective loophole scoped.
- [x] Finite hub/controller residuals bounded.
- [x] Approximation/error budget centralized in the manuscript.
- [x] Benchmark arithmetic independently checked.
- [x] Final integrated prior-art sweep completed with restrained novelty claims.

## B. Manuscript build — COMPLETE / AUTOMATED

- [x] Manuscript split into modular section files.
- [x] GitHub Actions LaTeX workflow added.
- [x] `latexmk` compilation automated.
- [x] Undefined reference/citation check automated.
- [x] Compiled PDF uploaded as CI artifact.
- [x] Full manuscript PDF rendered for visual QA.
- [x] Overwide introduction equation corrected.
- [x] Link figure redesigned and visually approved.
- [x] Approximation table visually approved.
- [x] TT-normalization appendix visually approved.

## C. Figures

### Figure 1 — serial link architecture

- [x] Equal-charge source/code shown.
- [x] Graviton-mode stage shown.
- [x] Receiver memory separated from accessible readout.
- [x] Link backbone equation shown cleanly below diagram.
- [x] Caption states source branching, propagation, receiver branching, loading, and readout roles.
- [x] Caption states precursor remains in complete waveform.
- [x] Final visual QA passed at full-page scale.

### Figure 2 — conserved four-spoke source

- [x] Four endpoints and finite spokes shown.
- [x] Plus-mode sign pattern visible.
- [x] Hub included.
- [x] Caption states opposite branch reverses arrows.
- [x] Visual QA passed in rendered PDF.

## D. Bibliography

- [x] Holevo EB source included.
- [x] Filippov-Ziman attenuation/amplification source included.
- [x] Donnelly-Giddings dressing/locality sources included.
- [x] Matsui conserved-source radiation included.
- [x] Laga-Suyama coherent radiation included.
- [x] Toccacelo et al. quantum GW receiver included.
- [x] Trenggana-Zen propagating-graviton entanglement included.
- [x] Mari et al. gravitational channel benchmark included.
- [x] Toccacelo-Andersen-Brask communication benchmark included.
- [x] Miki-Li-Chen thermal/entanglement bound included.
- [x] Graviton transducer literature included.
- [x] E2/EWSR literature included.
- [x] Atomic/bound-state graviton absorption literature included.
- [x] Public project repository citation added for Data Availability.
- [x] Final publication/DOI metadata pass completed for entries with verified publisher records; recent unverified 2026 works remain arXiv-only rather than receiving speculative metadata.

## E. Editorial preflight — COMPLETE EXCEPT AUTHOR METADATA

- [x] Complete prose copyedit for repeated caveats and scope inflation.
- [x] Claim-language scan for `first`, `new`, `exact`, `universal`, and `optimal`; retained mathematical uses are scoped.
- [x] Approximation qualifiers checked against strongest claims.
- [x] Symbol consistency reviewed, including the controller-strain $u f_q'$ correction and $A_s/\mathcal A/W_c$ cleanup.
- [x] Remove direct source-handoff/receiver-local clock comparison from the link proposition.
- [x] Replace unqualified ``exact controller-empty handoff'' wording with local-controller-safe handoff wording.
- [x] Remove orphaned $\sin^4$ loading example from the general link section.
- [x] Retain passive-broadening appendix because it directly supports the source speed--efficiency conclusion.
- [x] Add Data Availability statement.
- [x] Tighten the conclusion so the $10^{-42}$ source/receiver comparison is explicitly the symmetric benchmark rather than a universal claim.
- [ ] Add acknowledgments/funding/conflict statements as appropriate for the actual author.
- [ ] Replace `Anonymous` with actual author/affiliation/contact metadata in the submission copy.

## F. PRD initial-submission format

- [x] Current APS guidance checked: PDF is sufficient for initial peer review; REVTeX source is preferred but not an initial-review gate.
- [x] Current article-style manuscript therefore remains an acceptable initial-review source path.
- [x] Cover letter finalized around the narrow source-resolved normalization claim.
- [ ] Optional: prepare/test a REVTeX branch for production convenience or if requested by the journal.
- [ ] If REVTeX is adopted, recheck figure/table placement and long equations in two-column format.
- [ ] Replace author metadata and complete the journal submission form.

## G. Reproducibility / submission package

- [x] Pinned active numerical environment: Python 3.12.13, NumPy 2.5.1, SciPy 1.18.0.
- [x] TT normalization regression in CI.
- [x] Broader scientific regression CI covering representative thermal/amplifier/additive, near-boundary, finite-spoke, benchmark, and weak-negativity checks.
- [x] `SUBMISSION_MANIFEST.txt` defines the journal source set.
- [x] Submission-package workflow copies only manifest-defined manuscript files into an isolated directory.
- [x] Submission-package workflow runs semantic guards and clean-directory LaTeX compilation.
- [x] Research scratch notes are excluded from the source archive.
- [ ] Rebuild and download the clean archive from the final editorial head.
- [ ] Record final submission commit SHA.
- [ ] Create and push final annotated Git tag.

## H. Post-submission fallback order

If PRD declines on scope/significance rather than a substantive technical defect:

1. Classical and Quantum Gravity.
2. Physical Review Research.
3. Reconsider Quantum Science and Technology only if substantially reframed around general transduction/quantum-technology implications.

See `SUBMISSION_STRATEGY_V7.md`.
