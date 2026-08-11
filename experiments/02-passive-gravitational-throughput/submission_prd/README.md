# Physical Review D submission layer — Experiment 02

This directory contains the journal-submission manuscript.

**Validated sector-resolved science/manuscript checkpoint:** `3bf26c7535919597d711fdcd781e6098b76b5d68`.

The current PRD copy incorporates the reviewer-driven sector decomposition, finite-band propagation treatment, and tightened separation-axis inertia theorem while preserving the declared passive compact-quadrupole retained-modal scope.

## Target

- Journal: **Physical Review D**
- Article type: **Research Article**
- Title: **An Inertia-Controlled Spectral-Area Bound for Passive Far-Zone Gravitational Transduction**
- Framing: classical passive-resource theorem for propagating linearized gravity
- Not framed as: detector sensitivity, information capacity, practical near-term feasibility, or a priority claim about gravity-mediated communication

## Current theorem layer

The strongest finite-band statement keeps the exact outgoing compact-TT `m=0,|m|=1,|m|=2` propagation weights over the measured frequency band and closes them against sector-resolved endpoint completeness resources.

The rigorous leading far-zone statement is

```math
limsup_{R->infty} R^2 Gamma_coh
<= [5 G Omega^4/(4 c^3 omega_-^2)]
min(I_Rhat,A,I_Rhat,B),
```

where `I_Rhat` is the conventional moment of inertia about the source-receiver axis. For a carrier-scale narrow band,

```math
Gamma_coh lesssim
[5 G omega_0^2/(4 c^3 R^2)]
min(I_Rhat,A,I_Rhat,B).
```

This supersedes the former scalar `25/12 * min(I_2A,I_2B)` closure.

## Submission-layer clarifications now included

- operational meaning of `Gamma_coh` as a band-limited `H2` / power-transmissivity spectral area;
- weighted passive-Gramian cut with frequency-dependent propagation retained across the measured band;
- sector-resolved endpoint Parseval/Bessel resources about the propagation axis;
- exact finite-`kR` outgoing compact-TT sector singular values;
- explicit distinction between the on-shell modal gravitational linewidth and far-detuned frequency response;
- explanation of why completeness alone cannot control an unrestricted fourth modal-frequency moment;
- Fano broadband-matching and Chu--Harrington gain-bandwidth/size context without treating generic passive gain-bandwidth tradeoffs as the gravitational contribution;
- uniform-sphere and slender-bar scale/tightness checks;
- exact recurrence resolvent showing same-endpoint passive returns do not alter the leading `R^-2` coefficient;
- substantive AI-use disclosure and data-availability statement.

## Package contents

- `main.tex` — REVTeX 4.2 PRD wrapper, abstract, disclosure, and data statement.
- `sections/` — scientific manuscript sections and appendices.
- `references.bib` — cited primary and review literature.
- `COVER_LETTER_DRAFT.md` — cover-letter draft.
- `AI_DISCLOSURE_DRAFT.md` — disclosure working record.
- `DATA_AVAILABILITY_DRAFT.md` — data-availability working record.
- `SUBMISSION_METADATA.md` — author and journal metadata.
- `SIGNIFICANCE_POSITIONING.md` — editorial positioning and scale discipline.
- `HUMAN_SIGNOFF_CHECKLIST.md` — items requiring direct human responsibility before submission.

## Remaining human blockers before submission

1. Complete line-by-line scientific and reference sign-off.
2. Confirm submission history and absence of concurrent submission.
3. Add ORCID if desired.
4. Add recommended/excluded referee names only if desired after deliberate selection.
5. Perform final human visual inspection of the compiled submission PDF.

No further theorem broadening is authorized merely for manuscript polish. Reopen the science only for a concrete technical defect, direct literature collision, or substantive external-review objection.
