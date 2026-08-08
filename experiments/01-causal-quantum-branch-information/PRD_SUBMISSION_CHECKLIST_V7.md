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
- [x] $25/16$ propagation normalization cross-checked and demoted from novelty claim.
- [x] Source dephasing separated from energy branching.
- [x] Memory channel separated from accessible readout.
- [x] Exact pure-loss reference-receiver negativity derived.
- [x] Weak-link asymptotic checked numerically.
- [x] Passive EWSR coefficient independently checked.
- [x] EWSR and graviton-absorption prior art cited.
- [x] Active/collective loophole scoped.
- [x] Benchmark arithmetic independently checked.

## B. Manuscript build — COMPLETE / AUTOMATED

- [x] Manuscript split into modular section files.
- [x] GitHub Actions LaTeX workflow added.
- [x] `latexmk` compilation automated.
- [x] Undefined reference/citation check automated.
- [x] Compiled PDF uploaded as CI artifact.
- [x] At least one full manuscript PDF rendered page-by-page for visual QA.
- [x] Initial overwide introduction equation corrected.
- [x] Initial undersized/overlapping link figure redesigned.
- [ ] Final current-head page-2 render visually approved after last figure-label edit.

## C. Figures

### Figure 1 — serial link architecture

- [x] Equal-charge source/code shown.
- [x] Graviton-mode stage shown.
- [x] Receiver memory separated from accessible readout.
- [x] Link factors shown.
- [x] Caption states precursor remains in complete waveform.
- [ ] Final current-head visual QA.

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
- [ ] Final DOI/journal metadata pass for every entry immediately before submission.

## E. Required editorial preflight

- [ ] Final current-head PDF visual QA.
- [ ] One complete prose copyedit for repeated caveats and overly long sentences.
- [ ] Check every use of `first`, `new`, `exact`, `universal`, and `optimal`.
- [ ] Verify all approximation qualifiers appear before, not after, strongest claims.
- [ ] Check symbol consistency: $S,a,w,\Phi$, $\beta$, $\beta_g$, $q$, $q_c$, $\mathcal C$, $\mathcal O$.
- [ ] Check source-time versus receiver-local-time notation one final time.
- [ ] Decide whether $\sin^4$ numerical value belongs in main text or appendix.
- [ ] Decide whether passive broadening appendix is necessary for first submission.
- [ ] Add acknowledgments/funding statement as appropriate.
- [ ] Add data/code availability statement.
- [ ] Replace `Anonymous` with author metadata only in the actual submission copy.

## F. PRD formatting

- [ ] Convert article-style source to a PRD/REVTeX submission branch or confirm journal accepts current source for initial submission.
- [ ] Verify title/abstract under current PRD submission requirements.
- [ ] Confirm figure and table placement in REVTeX/two-column rendering if adopted.
- [ ] Recheck long equations in two-column format; break where needed.
- [ ] Verify bibliography style and APS reference formatting.

## G. Submission package

- [x] Cover-letter draft exists: `PRD_COVER_LETTER_DRAFT_V7.md`.
- [ ] Finalize cover letter after final manuscript copyedit.
- [ ] Prepare source archive containing only manuscript-required files.
- [ ] Exclude research scratch notes from submission archive.
- [ ] Verify source archive compiles from a clean directory.
- [ ] Save final submission commit SHA/tag.

## H. Post-submission fallback order

If PRD declines on scope/significance rather than a technical defect:

1. Classical and Quantum Gravity.
2. Physical Review Research.
3. Reconsider Quantum Science and Technology only if substantially reframed around general transduction/quantum-technology implications.

See `SUBMISSION_STRATEGY_V7.md`.
