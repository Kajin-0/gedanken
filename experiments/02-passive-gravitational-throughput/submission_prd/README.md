# Physical Review D submission layer — Experiment 02

This directory is a submission/editorial layer derived from the internally frozen Experiment 02 science/manuscript source.

**Authoritative scientific source:** `1ce596493073dbb49e6eb71f1a6df0566ff3c25b`.

The theorem, numerical coefficients, proof assumptions, and literature boundary are not to be altered here absent a concrete technical defect or external-review objection.

## Target

- Journal: **Physical Review D**
- Article type: **Research Article**
- Framing: classical passive-resource/no-go theorem in propagating linearized gravity
- Not framed as: detector sensitivity, information capacity, a practical near-term experiment, or the first gravity-mediated communication bound

## Package contents

- `main.tex` — REVTeX 4.2 PRD wrapper around an exact copy of the frozen scientific sections.
- `sections/` — scientific section files copied byte-for-byte from the frozen science SHA.
- `references.bib` — bibliography copied from the frozen science SHA.
- `COVER_LETTER_DRAFT.md` — PRD cover-letter draft.
- `AI_DISCLOSURE_DRAFT.md` — APS substantive-AI disclosure template; actual tool/model versions must be filled from project records before submission.
- `DATA_AVAILABILITY_DRAFT.md` — APS Data Availability draft tied to immutable repository provenance.
- `SUBMISSION_METADATA.md` — remaining author/reviewer/submission fields.
- `SIGNIFICANCE_POSITIONING.md` — editorial positioning, including the wave-zone/mechanical-frequency practical limitation.
- `HUMAN_SIGNOFF_CHECKLIST.md` — items that require direct human verification before submission.

## Remaining blockers before actual submission

1. Replace author, affiliation, email, and optional ORCID placeholders.
2. Fill the exact AI tool/model/version record; do not guess.
3. Complete human line-by-line scientific and reference sign-off.
4. Preferably archive the exact submission source/code in Zenodo or another persistent repository and insert its DOI into the Data Availability statement.
5. Add recommended/excluded referee names only after deliberate human selection.
6. Compile and inspect the PRD PDF generated from this directory.

The package may be edited for journal formatting, metadata, disclosure, and clarity, but its scientific content is pinned to the frozen source unless the repository's reopen conditions are met.
