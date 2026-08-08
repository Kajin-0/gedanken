# V7 manuscript

Current manuscript:

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

This directory is the active publication source. The project is in submission-preflight mode; older paper cores elsewhere in the experiment directory are historical unless a current audit cites them explicitly.

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Automated checks:

- `.github/workflows/latex-v7.yml` — manuscript compile, unresolved-reference/citation check, PDF artifact;
- `.github/workflows/submission-package.yml` — manifest-defined isolated source copy, semantic guards, clean-directory compile, clean source ZIP.

## Layout

- `main.tex` — preamble, title/abstract, section driver
- `sections/01_introduction.tex` — literature boundary and paper scope
- `sections/02_source_encoding.tex` — conserved four-spoke source, finite-speed local controller, equal-Poincare-charge code, causal handoff
- `sections/03_virtual_link.tex` — virtual difference mode, source branching, free-space capture, receiver branching, temporal loading
- `sections/04_noise_negativity.tex` — memory noise, accessible readout, exact pure-loss negativity
- `sections/05_bounds_benchmark.tex` — passive-matter response bound, active loopholes, numerical benchmark
- `sections/05b_approximation_budget.tex` — centralized approximation and error budget
- `sections/06_discussion_conclusion.tex` — controlled limitations, interpretation, conclusion, Data Availability
- `sections/appendices.tex` — handoff norm, full-system charge audit, exact PT block, passive EWSR derivation, passive broadening result
- `sections/tt_normalization_appendix.tex` — independent canonical TT one-graviton derivation of the free-space normalization
- `figures/` — source geometry and serial link architecture
- `references.bib` — scientific bibliography
- `data.bib` — repository/Data Availability citation
- `SUBMISSION_MANIFEST.txt` — exact manuscript-source file set used by the isolated packaging workflow

## Canonical state

Read:

1. `../CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`
2. `../PRD_SUBMISSION_CHECKLIST_V7.md`
3. `../EXTERNAL_REVIEW_RESPONSE_V7.md`
4. `../ARCHIVE_STATUS.md`

Current internal verdict:

> No known publication-critical structural physics gap remains from the external review within the manuscript's declared weak-field, nonrelativistic, narrowband linear regime.

This is a submission-readiness statement, not a guarantee of peer-review acceptance.

## Public versus private submission metadata

The public repository intentionally keeps `\author{Anonymous}`. Author name, affiliation, correspondence address, acknowledgments, funding, and conflict statements should be added to the private submission copy as appropriate rather than committed publicly unless the author explicitly chooses otherwise.
