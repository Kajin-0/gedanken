# Experiment 03 — variable-pole initializer clarification

Date: 2026-08-17

This clarification is committed **before the variable-pole optimization is run**.
It resolves one normalization ambiguity in
`VARIABLE_POLE_PHYSICAL_ACCEPTANCE_2026-08-17.md`; it does not change any rank,
objective, grid, optimizer, physicality condition, harmonic threshold, or
stopping rule.

## Ambiguity

The accepted coefficient-projection physical initializer has a small BCF
amplitude error, so its coupling vector generally satisfies

```text
||g_initializer||^2 != C_exact(0)
```

by the same small amount.

The new variable-pole parameterization, however, explicitly freezes

```text
g = sqrt(C_exact(0)) e1
```

so that exact equal-time bath variance is structural throughout optimization.

## Deterministic resolution

Immediately after reconstructing the coefficient-projection physical model and
**before** Hermitian Lanczos, rescale only its coupling vector:

```text
s_C0 = sqrt(C_exact(0) / (g_initializer^dag g_initializer)),
g_normalized = s_C0 g_initializer.
```

Keep `H` and `Gamma` unchanged.

This is not an optimized parameter and no choice is made from the result.  It is
the unique positive scalar normalization required by the already-frozen exact
`C(0)` condition.

The scale factor must be reported for every tested rank.

All Lanczos gauge checks then refer to this normalized physical initializer:

```text
U^dag g_normalized = sqrt(C_exact(0)) e1.
```

The gauge-invariance BCF audit compares the normalized model before and after
Lanczos.  The separately reported historical coefficient-projection baseline
remains unchanged in its existing checkpoints.

## Status

All other conditions in `VARIABLE_POLE_PHYSICAL_ACCEPTANCE_2026-08-17.md`
remain exactly unchanged.
