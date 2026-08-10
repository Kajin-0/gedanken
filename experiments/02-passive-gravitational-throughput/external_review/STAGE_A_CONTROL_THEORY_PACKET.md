# Stage A External Review Packet — Passive Selected-Port Cut

**Scientific snapshot:** `1ce596493073dbb49e6eb71f1a6df0566ff3c25b`

**Reviewer expertise:** finite-dimensional linear systems/control, passive scattering, `H_2` norms, dissipativity, Lyapunov/Gramian methods.

Do **not** read `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md` before completing the blind pass below.

## Blind-pass problem

Let a stable finite-dimensional passive Markov realization have internal state `x in C^n` and total port coupling matrix `K`, with

```math
A+A^\dagger \le -K^\dagger K.
```

Let `i` and `o` be disjoint selected port groups with no direct cross-feedthrough. Define the strictly proper cross-transfer block

```math
H_{o\leftarrow i}(\omega)
=-K_o(i\omega I-A)^{-1}K_i^\dagger.
```

Use the two-sided convention

```math
\|H_{o\leftarrow i}\|_2^2
=\frac1{2\pi}\int_{-\infty}^{\infty}
\operatorname{Tr}[H^\dagger(\omega)H(\omega)]\,d\omega.
```

### Claim to independently test

Does passivity alone imply

```math
\boxed{
\|H_{o\leftarrow i}\|_2^2
\le
\min\!
\left[
\operatorname{Tr}(K_i^\dagger K_i),
\operatorname{Tr}(K_o^\dagger K_o)
\right]?
}
```

If yes, derive it independently. If not, give the weakest correction or a counterexample.

Then consider a separated two-ended passive link

```math
T(\omega)=H_B(\omega)P(\omega)H_A(\omega),
```

where the endpoint scattering systems are passive and all physical loss ports are retained, and where over the retained band

```math
\|P(\omega)\|_{\rm op}^2\le \eta_{\max}.
```

Does it follow that

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right]
}
```

for

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}\operatorname{Tr}[T^\dagger T]\,d\omega?
```

## Specific failure modes to test

Please actively test, rather than assume away:

1. whether the Gramian inequality survives nonnormal/noncommuting `A` and `K^\dagger K`;
2. whether stability/Hurwitz assumptions are sufficient as stated;
3. whether any hidden minimality, controllability, or observability assumption is needed;
4. whether direct feedthrough or overlapping selected port groups would spoil the full-line `H_2` argument;
5. whether the trace dimensions and normalization are consistent;
6. whether the receiver-side cut follows independently of the source-side cut;
7. whether pointwise contractivity of passive scattering blocks is being used in a valid way in the separated-link step;
8. whether the result changes for dissipativity inequality versus exact lossless dilation `A+A^\dagger=-K^\dagger K`.

## Freeze your blind-pass result

Before reading the repository derivation, record:

- verdict: valid / valid with added hypothesis / invalid;
- your derivation or counterexample;
- any coefficient or normalization change;
- the minimal assumptions you believe are actually necessary.

## Comparison pass

Only after the blind result is fixed, read at the exact scientific snapshot:

- `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`
- optionally `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md` only if you want to assess the later bounded-port extension separately.

Do not use the numerical scripts as proof. They may be consulted only after the analytic comparison.

## Requested response format

```text
STAGE A VERDICT:
[NO CONCRETE DEFECT FOUND / HYPOTHESIS CHANGE / COEFFICIENT DEFECT / LOGICAL GAP / COUNTEREXAMPLE]

BLIND DERIVATION SUMMARY:
...

EXACT ISSUE, IF ANY:
file/section/equation or inference
...

MINIMAL CORRECTION:
...

CONFIDENCE / REMAINING UNCERTAINTY:
...
```
