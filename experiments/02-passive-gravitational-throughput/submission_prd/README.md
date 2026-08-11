# Physical Review D submission layer — Experiment 02

This directory contains the current journal-submission manuscript.

**Underlying validated science/theorem checkpoint:** `bfae23af41aefb3104d639099299b3432b4a14fe`.  
**Validated submission-manuscript checkpoint after final APS-policy alignment:** `6f7a60b3b05dea9f288b1b07e6f2e55acaf34e83`.

The later checkpoint changes only the article's Acknowledgments/Data Availability layer and submission-support documentation. The theorem, equations, scientific sections, appendices, bibliography, and numerical regressions are unchanged from the underlying science checkpoint.

The PRD copy incorporates the sector-resolved endpoint resource, exact finite-band outgoing compact-TT propagation weights, reduced-memory/continuum scope clarification, and the tightened separation-axis inertia theorem.

## Target

- Journal: **Physical Review D**
- Article type: **Research Article**
- Title: **An Inertia-Controlled Spectral-Area Bound for Passive Far-Zone Gravitational Transduction**
- Framing: classical passive-resource theorem for propagating linearized gravity
- Not framed as: detector sensitivity, information capacity, practical near-term feasibility, or a priority claim about gravity-mediated communication

## Current theorem layer

The strongest finite-band statement is

```math
\Gamma_{\rm coh}
\le
\frac{G\Omega^4}{5c^5}
\min[\mathcal G_A(R),\mathcal G_B(R)],
```

where `mathcal G_X` retains the exact measured-band `m=0,|m|=1,|m|=2` outgoing compact-TT power weights and the corresponding endpoint sector resources.

The rigorous far-zone statement is

```math
\limsup_{R\to\infty} R^2 \Gamma_{\rm coh}
\le
\frac{5G\Omega^4}{4c^3\omega_-^2}
\min(I_{\hat R,A},I_{\hat R,B}),
```

where `I_Rhat` is the conventional moment of inertia about the source-receiver axis. For a retained carrier-scale narrow band,

```math
\Gamma_{\rm coh}
\lesssim
\frac{5G\omega_0^2}{4c^3R^2}
\min(I_{\hat R,A},I_{\hat R,B}).
```

The earlier scalar closure

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
```

remains a valid looser corollary. It is not the strongest current headline.

## Submission-layer clarifications included

- `Gamma_coh` is a band-limited squared `H2` / power-transmissivity spectral area, not capacity or bit rate;
- the weighted passive-Gramian cut retains frequency-dependent propagation across the measured band;
- endpoint Parseval/Bessel resources are resolved into STF sectors about the propagation axis;
- exact finite-`kR` outgoing compact-TT sector singular values are used;
- the on-shell modal gravitational linewidth is distinguished from far-detuned frequency response;
- completeness alone cannot control an unrestricted fourth modal-frequency moment;
- reduced non-Markovianity alone is not an escape if an admissible enlarged passive realization exists;
- arbitrary hereditary/singular continuum or unbounded distributed models still require separate realization/admissibility/trace proof;
- Fano, Chu--Harrington, resonant-mass, material-response, channel, and multiple-scattering precedents are credited without treating their generic ingredients as the contribution;
- uniform-sphere and slender-bar scale/tightness checks are included;
- same-two-endpoint passive recurrence is shown not to alter the leading `R^-2` coefficient;
- substantive AI use is disclosed under Acknowledgments;
- the Data Availability statement explicitly addresses the numerical verification code supporting Appendix D.

## Final-preflight validation

At submission checkpoint `6f7a60b...`, the PRD compile and all seven physics/regression workflows passed, including the cross-version constant regression. The exact-head PDF is 9 pages with embedded fonts and no unresolved references or internal project terminology.

A pixel comparison with the prior validated PDF found pages 1-8 identical; only page 9 changed in the Acknowledgments/Data Availability region. See `../FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md` for the complete audit, run IDs, artifact digest, PDF digest, and human blockers.

## Package contents

- `main.tex` — REVTeX 4.2 PRD wrapper, abstract, Acknowledgments, and Data Availability statement.
- `sections/` — scientific manuscript sections and appendices.
- `references.bib` — cited primary and review literature.
- `COVER_LETTER_DRAFT.md` — cover-letter draft synchronized to the current theorem.
- `AI_DISCLOSURE_DRAFT.md` — disclosure working record.
- `DATA_AVAILABILITY_DRAFT.md` — article data/software-availability wording.
- `SUBMISSION_METADATA.md` — internal author/journal metadata.
- `SIGNIFICANCE_POSITIONING.md` — current editorial positioning and scale discipline.
- `HUMAN_SIGNOFF_CHECKLIST.md` — items requiring direct human responsibility before submission.

## Remaining human blockers before submission

1. Complete line-by-line scientific and reference sign-off.
2. Provide/authenticate the corresponding-author ORCID in the APS system.
3. Confirm submission history, preprint history, and absence of concurrent submission.
4. Finalize/read the cover letter and any recommended/excluded referee choices.
5. Perform final human visual inspection of the exact compiled submission PDF.

## Style boundary

The submitted physics article must not mention repository infrastructure, GitHub, commit hashes, source control, CI, internal experiment labels, or project bookkeeping. The article's Data Availability statement states only the scientific availability facts: no experimental data were created or analyzed, and the numerical verification code supporting Appendix D is available from the author upon reasonable request.

No further theorem broadening is authorized merely for manuscript polish. Reopen the science only for a concrete technical defect, direct literature collision, or substantive external-review objection.
