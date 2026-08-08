# V7 manuscript

Current source-resolved gravitational quantum-link manuscript.

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The repository workflow `.github/workflows/latex-v7.yml` runs the same compile path and fails on unresolved references or citations.

## Layout

- `main.tex` — preamble, abstract, section driver
- `sections/01_introduction.tex` — literature boundary and paper scope
- `sections/02_source_encoding.tex` — conserved four-spoke source, local encoder, equal-Poincare-charge code, causal handoff
- `sections/03_virtual_link.tex` — virtual difference mode, gravitational branching, propagation, four-factor coherent link
- `sections/04_noise_negativity.tex` — memory noise, accessible readout, exact pure-loss negativity
- `sections/05_bounds_benchmark.tex` — passive-matter bound, active loopholes, benchmark
- `sections/06_discussion_conclusion.tex` — controlled limitations and interpretation
- `sections/appendices.tex` — handoff norm, full-system charge audit, exact PT block, passive EWSR derivation, broadening no-go
- `references.bib` — bibliography

Canonical research recovery point remains `../CURRENT_STATE_LINK_BUDGET_V7.md` together with the more recent audit notes committed after it.
