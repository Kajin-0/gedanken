# Stages B/C External Review Packet — Endpoint Resource and TT Propagation

**Scientific snapshot:** `1ce596493073dbb49e6eb71f1a6df0566ff3c25b`

**Reviewer expertise:** linearized-gravity radiation, resonant-mass/GW antenna theory, elastic normal modes, quadrupole normalization, TT projection, far-zone propagation.

Do **not** read `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`, `TT_PROPAGATION_BOUND_DERIVATION.md`, the manuscript, or the prior-art audits before completing the blind pass below.

## Declared physical class

Assume weak leading mass-quadrupole gravity, nonrelativistic linear-harmonic matter, compact endpoints, separated wave-zone propagation, and a retained modal sector with physical modal frequencies bounded by

```math
\omega_n\le \Omega.
```

The eventual narrowband carrier replacement uses

```math
\Omega=\omega_0[1+O(B/\omega_0)],
\qquad B/\omega_0\ll1.
```

Uncontrolled modes with `omega_n >> omega_0` are **not** part of the simple carrier-scale theorem and should not be silently folded into it.

## Stage B blind-pass problem — endpoint resource

For each elastic normal mode `n`, let `mu_n` be its modal mass and `q_n` its symmetric trace-free mass-quadrupole overlap tensor under the repository's standard linearized mass-quadrupole convention.

The claimed completeness/resource chain is

```math
\boxed{
\sum_n \frac{q_n:q_n}{\mu_n}
\le \frac{20}{3}I_2,
\qquad
I_2=\int \rho r^2\,d^3x
}
```

and, after converting modal quadrupole radiation damping into normalized gravitational port coupling,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}I_2\Omega^4.
}
```

### Independently test

1. Re-derive the relevant tensor/completeness identity from the displacement-field normal-mode expansion.
2. Check the numerical factor `20/3` from first principles.
3. Check the gravitational quadrupole-radiation normalization and the resulting `4/3` coefficient.
4. Check whether the use of a common upper bound `Omega^4` is valid exactly under `omega_n <= Omega`.
5. Identify any hidden assumptions on completeness, boundary conditions, center-of-mass removal, rigid translations/rotations, mode normalization, degeneracy, or continuum limits.
6. Check whether passive unitary mixing inside the retained sector can change the total coupling trace.
7. Check all one-sided/two-sided, amplitude/power, and angular-frequency conventions for factors of 2 or `2pi`.

If the exact constants differ, provide the corrected constants and the normalization convention that produces them.

## Stage C blind-pass problem — compact TT propagation

For a compact trace-free quadrupole source in the radiation zone, independently derive the largest normalized directional power gain/directivity and the corresponding source-to-receiver compact TT propagation ceiling.

The claimed results are

```math
D_{\max}=\frac52
```

and

```math
\boxed{
\limsup_{kR\to\infty}(kR)^2\|P_g\|_{\rm op}^2
\le \frac{25}{16}.
}
```

### Independently test

1. Re-derive the TT angular radiation pattern and sphere normalization.
2. Check whether `D_max=5/2` is truly the global maximum over trace-free quadrupoles and viewing directions.
3. Derive the far-zone receiver coupling without assuming the desired `25/16` coefficient.
4. Check the stationary-phase/effective-area/Friis normalization, including amplitude versus power and polarization conventions.
5. Check reciprocity assumptions and whether the receiver normalization matches the source normalization.
6. Check whether the `limsup` statement is the correct asymptotic form and whether any `O[(kR)^{-3}]` or phase effects can contaminate the leading coefficient.
7. Identify any geometry or orientation class that could exceed the claimed operator-norm ceiling.

## Assembly check

Only after independently validating Stages B and C, combine them with a generic passive cut of the form

```math
\Gamma_{\rm coh}
\le
\eta_{\max}\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

Check whether the leading compact narrowband result is in fact

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
}
```

with `Gamma_coh` having units `s^-1`.

## Prior-art collision pass

Do this **after** the blind mathematics pass so literature familiarity does not substitute for checking the constants.

Search primary sources for an exact theorem containing the same complete two-ended closure: both passive endpoints reduced to `I_2`, the smaller-endpoint cut, frequency-integrated coherent transfer, and the compact far-zone TT coefficient.

Near-collisions are expected and should be distinguished from exact equivalence. In particular, inspect the resonant-mass/GW-antenna lineage and modern gravity-mediated communication/state-transfer work. If you find an exact collision, provide the exact theorem/equations and bibliographic source.

## Comparison pass

Only after freezing the blind result, read at the exact scientific snapshot:

- `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`
- `TT_PROPAGATION_BOUND_DERIVATION.md`
- `FINITE_TWO_ENDED_INERTIA_BOUND.md`

Then, if assessing literature priority, read:

- `STAGE_B_PRIOR_ART_BOUNDARY.md`
- `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`

Numerical scripts may be used only as secondary diagnostics after the analytic review.

## Requested response format

```text
STAGE B VERDICT:
[NO CONCRETE DEFECT FOUND / HYPOTHESIS CHANGE / COEFFICIENT DEFECT / LOGICAL GAP / COUNTEREXAMPLE]

BLIND STAGE-B DERIVATION SUMMARY:
...

STAGE C VERDICT:
[NO CONCRETE DEFECT FOUND / HYPOTHESIS CHANGE / COEFFICIENT DEFECT / LOGICAL GAP / COUNTEREXAMPLE]

BLIND STAGE-C DERIVATION SUMMARY:
...

ASSEMBLED 25/12 VERDICT:
...

EXACT ISSUE(S), IF ANY:
...

EXACT PRIOR-ART COLLISION, IF ANY:
primary source + theorem/equations
...

MINIMAL CORRECTION:
...

CONFIDENCE / REMAINING UNCERTAINTY:
...
```
