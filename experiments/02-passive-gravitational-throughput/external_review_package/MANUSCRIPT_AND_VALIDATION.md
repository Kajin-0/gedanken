# Manuscript and Validation Handoff

## Manuscript to review

Title:

**Passive Throughput Bounds for Propagating Gravitational Transduction**

Canonical source on the parent theorem branch:

`../manuscript_v1/`

The external-review branch does **not** alter the theorem manuscript. It adds only reviewer-facing material.

## Validated manuscript artifact

The manuscript was compiled and checked after the strongest-route theorem changes and the Lobo/Tobar historical attributions.

```text
GitHub Actions run: 31346901851
job:               93330404771
artifact:          experiment02-manuscript-v1
artifact id:       9047633369
artifact digest:   sha256:d46658b4e763799c320da35ccae83e653dde201cd72f47f6127d40c938bbd0ca
```

Validation status:

```text
LaTeX compilation:                   PASS
unresolved citation/reference scan: PASS
PDF artifact upload:                PASS
```

The compiled PDF contains 20 pages.

## Physics validation

The six-layer regression suite passed after the strongest-route closure:

```text
run: 31347058681
job: 93330821747
PASS
```

The six layers are:

1. exact two-port spectral bound;
2. passive selected-port `H2` cut set;
3. classical modal resource / `20/3` and `40/3` identities;
4. recurrent passive two-endpoint scattering;
5. compact TT propagation;
6. microscopic gravitational-port factorization.

The theorem-source branch subsequently received documentation-only synchronization commits. Its actual final documentation head also triggered and passed the full physics workflow:

```text
run: 31347305552
PASS
```

## What a reviewer should read

For a first contact, send only:

- compiled manuscript PDF;
- `TECHNICAL_SUMMARY.md`;
- `NOVELTY_AND_SCOPE.md`.

If the reviewer agrees to inspect a specific theorem step, add:

- `AUDIT_EQUATIONS_AND_ASSUMPTIONS.md`;
- the relevant audit file from the parent Experiment 02 directory.

Do not send the full internal audit archive unless requested; it obscures the small number of load-bearing questions.

## Version discipline

Any external criticism must be recorded against an explicit manuscript version or commit. Do not silently repair the manuscript while several specialists are reviewing different versions.

Recommended protocol:

```text
1. freeze the PDF + source commit being reviewed;
2. collect reviewer objections;
3. classify each objection as technical / priority / significance / scope;
4. reopen the derivation only for a concrete technical or priority objection;
5. issue one synchronized revision after the first review wave.
```
