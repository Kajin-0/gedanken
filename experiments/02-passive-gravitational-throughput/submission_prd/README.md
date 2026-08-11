# Physical Review D submission layer — Experiment 02

This directory is the journal-submission layer for Experiment 02.

**Frozen theorem/source checkpoint:** `1ce596493073dbb49e6eb71f1a6df0566ff3c25b`.

The PRD copy preserves the theorem, numerical coefficient, and declared scope of that checkpoint while allowing submission-specific exposition, physical interpretation, worked examples, metadata, and disclosure to improve in response to referee-style criticism.

## Target

- Journal: **Physical Review D**
- Article type: **Research Article**
- Current title: **An Inertia-Controlled Spectral-Area Bound for Passive Far-Zone Gravitational Transduction**
- Framing: classical passive-resource/no-go theorem in propagating linearized gravity
- Not framed as: detector sensitivity, information capacity, a practical near-term experiment, or a priority claim about gravity-mediated communication

## Current submission-layer clarifications

The PRD version now adds, without broadening the theorem:

- an operational interpretation of `Gamma_coh` as the band-limited `H2` / power-transmissivity spectral area;
- a physical justification of strict properness and complete retained gravitational port sets;
- an explicit quadrupole-power-to-linewidth normalization check;
- clarification that Bessel's inequality acts on the orthonormal mode basis, not on mutually orthogonal influence fields;
- a uniformity argument for the TT stationary-phase/operator-norm step;
- an explicit recurrence expansion showing that constructive returns first affect `O[(kR)^-4]`;
- a uniform-sphere scale example showing the extreme weakness of the far-zone macroscopic ceiling;
- consolidated prior-art language and a sharper statement of the near-field and high-frequency exclusions;
- a non-placeholder substantive-AI disclosure.

## Package contents

- `main.tex` — REVTeX 4.2 PRD manuscript wrapper and abstract/disclosure/data statements.
- `sections/` — PRD submission sections derived from the frozen theorem source, with exposition-only clarifications and the worked example above.
- `references.bib` — bibliography retained from the literature-corrected frozen source.
- `COVER_LETTER_DRAFT.md` — PRD cover-letter draft.
- `AI_DISCLOSURE_DRAFT.md` — disclosure/provenance working record.
- `DATA_AVAILABILITY_DRAFT.md` — Data Availability draft tied to immutable repository provenance.
- `SUBMISSION_METADATA.md` — author and journal metadata.
- `SIGNIFICANCE_POSITIONING.md` — editorial positioning and scale discipline.
- `HUMAN_SIGNOFF_CHECKLIST.md` — items requiring direct human responsibility before upload.

## Remaining blockers before actual submission

1. Complete the human line-by-line scientific and reference sign-off.
2. Confirm submission history / no concurrent submission.
3. Add ORCID if desired.
4. Preferably archive the exact submission source/code in a persistent repository and insert its DOI.
5. Add recommended/excluded referee names only if desired after deliberate human selection.
6. Compile and visually inspect the final PRD PDF generated from this exact revision.

No further theorem broadening is authorized merely for manuscript polish. A scientific reopen requires a concrete defect or external-review objection that cannot be resolved by clarification within the existing theorem.
