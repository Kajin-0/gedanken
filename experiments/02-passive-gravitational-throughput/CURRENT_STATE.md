# Current State — Experiment 02

**Checkpoint:** Stage B validated on real `main`; Stage C next.  
**Status:** **STAGE A PASSIVE CUT ESTABLISHED; STAGE B GRAVITATIONAL ENDPOINT RESOURCE ESTABLISHED WITHIN FINITE QUADRUPOLE/MODAL MODEL; TT PROPAGATION AND FINAL TWO-ENDED THEOREM UNVERIFIED; NO MANUSCRIPT.**

## 1. Project objective

This project studies whether a separated compact passive gravitational link has a frequency-integrated throughput ceiling controlled by endpoint inertia.

The provisional conversation-origin target remains

```math
\Gamma_{\rm coh}
\stackrel{?}{\lesssim}
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B),
```

but no final coefficient is inherited from conversation history. Every load-bearing step is being reconstructed as a real repository artifact.

## 2. Stage A — established finite-dimensional passive cut

For finite-dimensional passive Markov realizations,

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

Canonical derivation: `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`.

Canonical first validation:

```text
run: 31391304791
job: 93463450929
PASS
```

Stage A is generic passive-systems mathematics and is not a novelty claim.

## 3. Stage B — established gravitational endpoint resource within model

For mass-orthogonal displacement modes,

```math
q_{n,ij}
=\int\rho\left(
 w_{n,i}x_j+w_{n,j}x_i
-\frac23\delta_{ij}\,w_n\cdot x
\right)d^3x,
```

and the standard quadrupole radiation power gives

```math
\boxed{
\kappa_{g,n}
=\frac{G\omega_n^4}{5c^5}
\frac{q_n:q_n}{\mu_n}.
}
```

The STF influence-field identity

```math
\boxed{
\sum_{ijk}|(g^{ij})_k|^2
=\frac{20}{3}r^2
}
```

plus Bessel's inequality yields

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I_2,
\qquad
I_2\equiv\int\rho r^2d^3x.
}
```

For retained modes `omega_n <= Omega`,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}I_2\Omega^4.
}
```

The inherited `4/3` coefficient therefore re-emerged independently and has now survived the repository regression.

Canonical derivation: `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`.

### Stage-B validation

```text
workflow: .github/workflows/experiment02-endpoint-resource.yml
run:      31392339989
job:      93466817164
result:   PASS
```

Regression output:

```text
worst 20/3 tensor absolute error = 2.84217094304e-14
worst truncated Bessel ratio = 1
worst full-basis Parseval absolute error = 1.70530256582e-13
worst modal-mixing invariance absolute error = 5.68434188608e-14
worst cumulative linewidth/(4 I2/3) ratio = 0.381072504534
PASS: gravitational endpoint quadrupole resource
```

The regression independently checks the tensor contraction, Parseval/Bessel structure, modal-mixing invariance, and cumulative linewidth ceiling.

### Important notation

`I_2 = int rho r^2 dV` is the scalar second mass moment about the center of mass, not a moment of inertia about one chosen axis. The trace of the conventional inertia tensor is `2 I_2`.

## 4. Historical boundary

Primary literature already makes broad ingredients historical:

- Hirakawa, Narihara, and Fujimoto (JPSJ 41, 1093, 1976) treat gravitational antenna emission/reception using eigenmodes and structure symmetry.
- Lobo (Phys. Rev. D 52, 591, 1995; arXiv:gr-qc/0006102) develops a general arbitrary-solid-elastic-body GW response formalism with multimode transfer and absorption cross sections.

Therefore eigenmode gravitational-antenna response and arbitrary-body multimode coupling are not novelty claims.

The exact historical status of the `20/3` and `4/3` cumulative inequalities remains open. See `STAGE_B_PRIOR_ART_BOUNDARY.md`.

## 5. Current epistemic state

```text
spectral-area metric, finite stable cross block:      ESTABLISHED WITHIN MODEL
finite-dimensional passive selected-port cut:         ESTABLISHED WITHIN MODEL
finite-dimensional two-ended propagation cut:         ESTABLISHED WITHIN MODEL
20/3 modal quadrupole Bessel bound:                    ESTABLISHED WITHIN MODEL
4/3 cumulative gravitational endpoint resource:        ESTABLISHED WITHIN MODEL
Markov trace = sum gravitational energy linewidths:    ESTABLISHED WITHIN MODEL
passive internal modal mixing trace invariance:        ESTABLISHED WITHIN MODEL
25/16 TT propagation in this throughput normalization: UNVERIFIED
25/12 final coefficient:                               UNVERIFIED
countably infinite modal extension:                    OPEN
passive recurrence statement:                          UNVERIFIED
complete historical prior-art boundary:                OPEN
publication significance:                              UNKNOWN
manuscript:                                             NONE
```

## 6. Experiment 01 boundary

`../01-causal-quantum-branch-information/` remains the frozen V7 publication project. Experiment 02 must not silently import V7's operational `25/16` normalization.

## 7. Next action — Stage C

Independently derive the compact TT propagation operator normalization appropriate to the Experiment-02 throughput metric.

Required checks:

1. derive the STF TT angular radiation pattern and its integrated normalization;
2. obtain the maximum compact quadrupole directivity without assuming `5/2`;
3. derive the reciprocal effective-area/Friis propagation coefficient for a normalized gravitational mode;
4. show whether the pointwise operator norm satisfies `eta_max <= 25/[16(kR)^2]` at leading wave-zone order;
5. cross-check only afterward against the independent V7 one-graviton result;
6. add a numerical tensor/directivity regression and record real CI.

Only if Stage C closes may the candidate `25/12` two-ended coefficient be assembled and tested.
