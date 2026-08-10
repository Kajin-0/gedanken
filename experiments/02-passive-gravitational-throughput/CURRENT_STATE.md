# Current State — Experiment 02

**Checkpoint:** Stage A validated on real `main`.  
**Status:** **FINITE-DIMENSIONAL GENERIC PASSIVE CUT ESTABLISHED; GRAVITY-SPECIFIC RESOURCE AND FINAL INERTIA THEOREM UNVERIFIED; NO MANUSCRIPT.**

## 1. Project objective

This project studies whether a separated compact passive gravitational link has a frequency-integrated throughput ceiling controlled by endpoint inertia.

A previous conversation suggested the candidate relation

```math
\Gamma_{\rm coh}
\stackrel{?}{\lesssim}
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B),
```

but none of the previous conversation-only validation claims are inherited. Every load-bearing step is being rebuilt as a real repository artifact.

## 2. Stage A — passive selected-port cut

For a finite-dimensional passive Markov realization with

```math
A=-iH-\frac12K^\dagger K
```

and disjoint strictly proper selected port groups `i -> o`, the Stage-A derivation establishes

```math
\boxed{
\|H_{o\leftarrow i}\|_2^2
\le
\min\!\left[
\operatorname{Tr}(K_i^\dagger K_i),
\operatorname{Tr}(K_o^\dagger K_o)
\right].
}
```

The proof uses selected controllability/observability Gramians and the dissipativity identity. It is stored in

`PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`.

For a separated source/receiver pair with normalized propagation operator `P(omega)` satisfying

```math
\|P(\omega)\|_{\rm op}^2\le\eta_{\max},
```

the same argument gives

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

No gravitational inertia formula is used in this step.

### Stage-A scope

Established here:

- finite-dimensional passive Markov realizations;
- all physical loss channels retained in the passive dilation/dissipativity balance;
- stable strictly proper selected cross-port transfer;
- normalized propagation with a pointwise operator-norm ceiling.

Not yet established:

- countably infinite bounded-port sectors;
- unbounded PDE boundary ports;
- non-Markov continua;
- any gravity-specific expression for `Tr(K_g^dagger K_g)`.

### Stage-A prior art

The passive realization and frequency-axis contractivity/unitarity structure are established systems machinery. Primary sources checked during reconstruction include Guta–Yamamoto (arXiv:1303.3771) and Gough–Zhang (arXiv:1311.1375). Stage A is not a novelty claim.

## 3. Stage-A automated validation

Files:

- `numerics/verify_passive_selected_port_cut.py`
- `numerics/requirements.txt`
- `.github/workflows/experiment02-passive-cut.yml`

Canonical first run on `main`:

```text
run: 31391304791
job: 93463450929
PASS
```

Regression output:

```text
worst endpoint H2/resource ratio = 0.410127000961
largest full-scattering singular value = 1
worst two-ended Gamma/bound ratio = 0.089763188389
PASS: finite-dimensional passive selected-port cut
```

The regression generates random complex noncommuting passive realizations, checks the exact Lyapunov `H2` cut, verifies pointwise full-scattering contractivity, and numerically integrates random two-ended links against the structural bound.

The numerical regression supports but does not replace the analytic proof.

## 4. Current epistemic state

```text
spectral-area metric, finite stable cross block:      ESTABLISHED WITHIN MODEL
finite-dimensional passive selected-port cut:         ESTABLISHED WITHIN MODEL
finite-dimensional two-ended propagation cut:         ESTABLISHED WITHIN MODEL
cumulative gravitational inertia resource:            UNVERIFIED
25/16 TT propagation in this throughput normalization: UNVERIFIED
25/12 final coefficient:                               UNVERIFIED
countably infinite modal extension:                    OPEN
passive recurrence statement:                          UNVERIFIED
complete historical prior-art boundary:                OPEN
publication significance:                              UNKNOWN
manuscript:                                             NONE
```

## 5. Experiment 01 boundary

`../01-causal-quantum-branch-information/` remains the frozen V7 publication project.

Do not modify its physics while developing Experiment 02 unless an explicit cross-check reveals a concrete defect relevant to V7. Shared formulas may be compared, but Experiment 02 must reconstruct its own operational normalization.

## 6. Next action — Stage B

Derive the cumulative gravitational coupling resource

```math
\operatorname{Tr}(K_g^\dagger K_g)
```

from an explicit mass-weighted quadrupolar continuum/modal model and determine whether it can actually be bounded by a simple endpoint inertia functional.

Stage B must answer, independently:

1. what modal quadrupole variable couples to TT radiation;
2. how its gravitational linewidth/coupling rate is normalized;
3. whether completeness/Bessel arguments bound the sum over all passive modes;
4. what inertia functional appears;
5. whether the inherited `4/3` coefficient survives;
6. which parts are established gravitational-antenna/modal prior art.

Do not assume the inherited coefficient or the final `25/12` result.
