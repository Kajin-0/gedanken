# Theorem-Constant Cross-Version Regression Audit — 2026-08-10

## Trigger

A continuity concern was raised after the Experiment 02 headline coefficient changed soon after a context-window handoff. The previous scalar coefficient

```math
(25/12) min(I_2,A,I_2,B)
```

had survived many iterations before the sector-resolved revision replaced the leading resource by

```math
(5/4) min(I_Rhat,A,I_Rhat,B).
```

Because a long-lived coefficient changed immediately after a new agent/session resumed the project, the transition was treated as a potential regression rather than accepted from current documentation alone.

## Baselines audited

Pre-sector validated manuscript state:

```text
986d8e5e81172482605e5e244d8759005b94ed0b
```

Sector-resolved theorem transition:

```text
3bf26c7535919597d711fdcd781e6098b76b5d68
```

Current validated science/manuscript checkpoint remains:

```text
bfae23af41aefb3104d639099299b3432b4a14fe
```

No manuscript theorem change was authorized by this audit unless a contradiction was found.

## 1. Process regression found

The `3bf26c...` transition replaced two broad inherited regression programs with shorter sector-specific checks.

The old combined regression generated random finite-dimensional passive endpoints, constructed gravitational couplings under the scalar endpoint budget, numerically integrated the complete end-to-end transfer over frequency, and checked the `25/12` result directly.

The new combined regression checked the sector geometry, exact finite-distance `eta_m` formulas, ordering, the `5/4` arithmetic, and a sphere check, but no longer exercised the complete randomized passive endpoint + frequency-integration chain.

Likewise, the endpoint regression retained the new sector Parseval identities but dropped some inherited scalar checks such as truncated scalar Bessel, modal-mixing invariance, and the randomized fourth-frequency linewidth check.

This is a genuine **validation-process regression** even if the new theorem is correct. A stronger theorem must not obtain apparent confidence by deleting broader tests that an older theorem already passed.

## 2. Mathematical compatibility of the constants

The old coefficient remains valid. It follows by discarding STF-sector information:

```math
sum_n (q_n:q_n)/mu_n <= (20/3) I_2
```

and applying the worst compact-TT far-zone power singular value

```math
eta_max ~ 25/(16 z^2).
```

Including the gravitational linewidth factor `1/5` gives

```math
(1/5)(20/3)(25/16) = 25/12.
```

The sector-resolved proof does not contradict that inequality. It decomposes the same scalar Parseval resource into

```math
|m|=2:  4 I_Rhat
|m|=1:  2 I_Rhat + 4 Z_Rhat
m=0:    (2/3) I_Rhat + (8/3) Z_Rhat
```

whose sum is exactly `(20/3) I_2`.

In the far zone only the `|m|=2` propagation sector survives at order `R^-2`. Combining its resource with the same TT normalization gives

```math
(1/5)(4)(25/16) = 5/4.
```

Therefore the intended logical relation is:

```text
25/12 * I_2  = valid looser scalar corollary
5/4  * I_Rhat = stronger directional leading closure
```

A failure of the new sector argument would require reverting to the scalar theorem, not declaring the old theorem false.

## 3. Independent cross-version regression

A new self-contained regression, `numerics/verify_constant_regression.py`, was written without importing the current theorem regression modules. It deliberately re-tests both generations of the result.

It checks:

1. the original randomized `25/12` end-to-end passive link using full numerical frequency integration;
2. complete and truncated scalar Parseval/Bessel relations;
3. retained-mode mixing invariance and the old randomized `omega_n^4` linewidth inequality;
4. complete and truncated STF-sector Parseval/Bessel relations and exact recovery of the scalar resource;
5. the TT angular kernels by direct numerical application of the TT projector, rather than assuming the manuscript kernels;
6. the outgoing overlap/`eta_m` formulas by independent numerical integration;
7. a five-sector randomized passive end-to-end link with numerical frequency integration against the weighted sector trace and geometry bounds;
8. compatibility that the sector-resolved finite-distance geometry bound does not exceed the old scalar bound in the separated `z>=3` branch;
9. the exact leading algebra `(1/5)(25/16)(4)=5/4`.

Local pre-commit execution gave:

```text
legacy 25/12 end-to-end worst ratio = 0.0795603296478
truncated scalar Bessel worst ratio = 1
truncated sector Bessel worst ratio = 1
modal-mixing worst absolute error = 5.68434188608e-14
independent TT-kernel worst absolute error = 3.33066907388e-16
sector end-to-end Gamma/weighted-trace worst ratio = 0.0208442040097
sector end-to-end Gamma/geometry worst ratio = 0.0139210706778
largest new-geometry/old-scalar bound ratio = 0.705587022046
PASS: cross-version constant regression; 25/12 preserved, 5/4 refinement survives
```

These values are diagnostic rather than tightness estimates. The purpose is falsification of normalization, degeneracy, projection, and end-to-end composition errors.

## 4. Independent algebraic checks

The audit separately re-derived:

- orthonormality of the five real STF basis tensors;
- `q:E = <w,2 E x>_rho` for traceless symmetric `E`;
- the pointwise sector influence sums

```math
4(x^2+y^2),
2(x^2+y^2)+4z^2,
(2/3)(x^2+y^2)+(8/3)z^2,
```

which sum to `(20/3)r^2`;
- direct TT-projector azimuthal integration yielding

```math
K_2(mu)=5/32 (1+6mu^2+mu^4),
K_1(mu)=5/8 (1-mu^2)(1+mu^2),
K_0(mu)=15/16 (1-mu^2)^2.
```

No missing two-fold degeneracy, STF normalization mismatch, or extra factor of two was found.

## 5. Disposition

**No scientific regression in the `5/4` coefficient has been found.** The old `25/12` theorem survives as a valid looser scalar corollary, while the sector-resolved argument currently survives as a stricter directional refinement.

The confidence level is nevertheless changed in one important way: `5/4` is not to be protected merely because current documentation calls it canonical. Any future contradiction in the weighted sector cut, gravitational sector trace, or TT normalization reopens the transition and must fall back to the last independently validated compatible result.

## 6. Permanent change-control rule

For Experiment 02, any future change to a theorem coefficient, normalization, resource definition, asymptotic order, or headline inequality must satisfy all of the following before the old result is superseded:

1. preserve and rerun inherited regressions from the previous theorem state;
2. add an independent regression targeted at the new mathematical step;
3. include at least one end-to-end numerical composition test when the theorem is end-to-end;
4. show explicitly how the new result relates to the previous result: refinement, incompatible replacement, or correction;
5. perform a normalization/units/degeneracy audit independent of the implementation being tested;
6. record the exact pre-change and post-change science states in a dedicated audit;
7. do not delete older regression coverage merely because the new theorem has a different internal decomposition;
8. do not modify the manuscript headline until these gates pass.

This rule is specifically intended to prevent context-window/session churn from masquerading as scientific progress.

## 7. Current action

The manuscript remains at the validated `bfae23af...` science checkpoint. This audit adds validation infrastructure and documentation; it does not itself change the physics manuscript or the `5/4` theorem.
