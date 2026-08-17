# Experiment 03 — dim2 TEMPO reference and memory audit

Date: 2026-08-17

## Scope

This checkpoint closes two reference-side questions in the direct-TEMPO method-recovery program:

1. is the finite dim=2 conventional-HEOM stationary state used for the TEMPO mapping comparison itself converged in hierarchy depth and bath Padé order?
2. how much of the validated direct-port correlation is omitted by the currently tested TEMPO memory cutoffs?

Neither result promotes nonlinear Gate C.1.

## 1. Dim=2 conventional-HEOM stationary reference convergence

Scripts:

- `calculations/heom_dim2_stationary_reference.py`
- `calculations/heom_dim2_stationary_reference_table.py`

Workflow runs:

- matrix `32004136501`
- compact table `32004264709`

The finite system is the exact same dim=2 harmonic truncation used in the direct-TEMPO-vs-HEOM mapping test.  All physical parameters and the counterterm are unchanged.

Compact stationary table:

```text
case   nADO   pop1
p4d4    210   0.03376039427782657
p4d5    462   0.03372570884753459
p4d6    924   0.03372933952687725
p4d7   1716   0.03372954547252102
p4d8   3003   0.03372953139051186
p4d9   5005   0.03372953070668817

p5d6   1716   0.03372959938112182
p5d7   3432   0.03372980532865586
p5d8   6435   0.03372979124640112
```

All stationary coherences are zero to displayed precision and all reduced states are positive.

Depth differences relative to p4d9:

```text
p4d4  +3.0863571e-5
p4d5  -3.8218592e-6
p4d6  -1.9117981e-7
p4d7  +1.4765833e-8
p4d8  +6.8382369e-10
p4d9   0
```

Padé-order control:

```text
p4d9 pop1 = 0.03372953070668817
p5d8 pop1 = 0.03372979124640112
difference = +2.6053971e-7
```

Therefore the dim=2 HEOM stationary comparison state is converged far below the ~`1.6e-3` direct-TEMPO half-distance observed at `tcut=8, tend=32`.

**Conclusion:** underconvergence of the dim=2 HEOM reference is not a viable explanation of the current TEMPO offset.

For subsequent mapping diagnostics, p4d9 may be treated as the canonical finite-system HEOM stationary reference:

```text
rho_ref = diag(0.9662704692933118,
               0.03372953070668817)
```

with p5-order uncertainty at the few-`1e-7` population level.

## 2. Exact direct-port memory-tail audit

Script:

`calculations/direct_port_memory_tail_audit.py`

Workflow run `32004188463`, job `95310256579`.

For the validated exponential representation

```text
C(tau)=sum_k d_k exp(-z_k tau), tau>=0,
```

the exact omitted integrated tail is

```text
I_tail(tcut)=sum_k d_k exp(-z_k tcut)/z_k.
```

The audit reports both the signed complex tail and a conservative no-cancellation absolute sum.  p4 and p5 agree at displayed precision over the relevant tail because the slow circuit poles dominate.

### p4 results

```text
tcut  |C(tcut)|/|C(0)|  |I_tail|/|I_total|  abs-tail fraction
4      1.22712e-1        8.55475e-2          6.70410e-2
6      3.45995e-2        2.59313e-2          1.86252e-2
8      1.00108e-2        6.67319e-3          5.20528e-3
10     2.58972e-3        1.96619e-3          1.45697e-3
12     7.95684e-4        5.52458e-4          4.07968e-4
14     2.07096e-4        1.46330e-4          1.14247e-4
16     5.98737e-5        4.46652e-5          3.19944e-5
18     1.71477e-5        1.14456e-5          8.95996e-6
20     4.47502e-6        3.41131e-6          2.50922e-6
22     1.37305e-6        9.44633e-7          7.02704e-7
24     3.54507e-7        2.53454e-7          1.96791e-7
```

The p5 table is numerically the same at the shown precision.

These are **bath-memory diagnostics, not reduced-state error bounds**.  They nevertheless establish that:

- `tcut=8` discards a non-negligible ~`6.7e-3` signed integrated correlation tail;
- `tcut=12` reduces that by ~12x but still leaves ~`5.5e-4`;
- `tcut=16` leaves ~`4.5e-5`;
- `tcut=20` leaves ~`3.4e-6`, finally on the same order as the frozen full-state TEMPO acceptance scale.

Therefore, if the `tcut=12` direct-TEMPO mapping improves substantially but remains visibly biased, `tcut≈20` is the next principled memory window.  Do not choose a larger memory cutoff arbitrarily and do not infer a state-error bound directly from the correlation-tail fraction.

## Predeclared memory-bias diagnostic

See `TEMPO_DIM2_MEMORY_PREDICTION_2026-08-17.md`, committed before the `tcut=12` state was read.

Using the current `tcut=8` late-distance fit and linear tail scaling only as a falsification heuristic, it predicts roughly

```text
tcut=12  half-distance ~1.27e-4
tcut=16                ~1.03e-5
tcut=20                ~7.8e-7
```

These are not acceptance thresholds.

## Pending direct-TEMPO controls at this checkpoint

```text
long64: tcut=8,  tend=64, run 32003044791, job 95306962896
mem64:  tcut=12, tend=64, run 32003044791, job 95306963004
mem32:  tcut=12, tend=32, run 32004405379, job 95310884194
```

All were still in progress when this checkpoint was written.

## Method status

- dim2 HEOM reference uncertainty: CLOSED / negligible at current TEMPO offset scale
- direct-port memory cutoff: ACTIVE / likely material
- direct TEMPO finite-system mapping: NOT YET PASSED
- PT-TEMPO reusable route: REJECTED separately
- nonlinear TEMPO: NOT AUTHORIZED
- Gate C.1: ACTIVE / method recovery
- Gate C.2, D, E: BLOCKED
- Publication: NO-GO
