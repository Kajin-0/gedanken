# Current State — Experiment 02

**Checkpoint:** Stage B independently derived on real `main`; endpoint-resource validation pending.  
**Status:** **STAGE A ESTABLISHED; GRAVITY-SPECIFIC ENDPOINT RESOURCE RE-DERIVED WITH `4/3` COEFFICIENT, VALIDATION PENDING; TT PROPAGATION AND FINAL TWO-ENDED THEOREM UNVERIFIED; NO MANUSCRIPT.**

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

Canonical derivation:

`PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`

Canonical first validation:

```text
run: 31391304791
job: 93463450929
PASS
```

Stage A is generic passive-systems mathematics and is not a novelty claim.

## 3. Stage B — independent gravitational endpoint derivation

For mass-orthogonal displacement modes

```math
\langle w_n,w_m\rangle_\rho=\mu_n\delta_{nm},
```

define the linear STF modal quadrupole

```math
q_{n,ij}
=\int\rho\left(
 w_{n,i}x_j+w_{n,j}x_i
-\frac23\delta_{ij}\,w_n\cdot x
\right)d^3x.
```

The standard quadrupole radiation power gives the modal gravitational energy-decay rate

```math
\boxed{
\kappa_{g,n}
=\frac{G\omega_n^4}{5c^5}
\frac{q_n:q_n}{\mu_n}.
}
```

Introduce vector influence fields

```math
(g^{ij})_k
=\delta_{ik}x_j+\delta_{jk}x_i
-\frac23\delta_{ij}x_k.
```

Direct contraction gives

```math
\boxed{
\sum_{ijk}|(g^{ij})_k|^2
=\frac{20}{3}r^2.
}
```

Bessel's inequality then yields

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I_2,
\qquad
I_2\equiv\int\rho r^2d^3x.
}
```

For retained modes satisfying `omega_n <= Omega`,

```math
\boxed{
\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}I_2\Omega^4.
}
```

Thus the inherited `4/3` coefficient has re-emerged from an independent derivation rather than being assumed.

Canonical derivation:

`GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`

### Important notation

`I_2 = int rho r^2 dV` is the scalar second mass moment about the center of mass. It is not a moment of inertia about one chosen axis. The trace of the conventional inertia tensor is `2 I_2`.

## 4. Stage-B historical boundary

Primary literature checked so far establishes that broad ingredients are historical:

- Hirakawa, Narihara, and Fujimoto (JPSJ 41, 1093, 1976) treat gravitational antenna emission/reception using an eigenmode system and structure symmetry.
- Lobo (Phys. Rev. D 52, 591, 1995; arXiv:gr-qc/0006102) develops a general response formalism for an arbitrary solid elastic body, including multimode transfer and absorption cross sections.

Therefore eigenmode gravitational-antenna response and arbitrary-body multimode coupling are **not** novelty claims.

The exact historical status of the `20/3` and `4/3` cumulative inequalities is still open. See:

`STAGE_B_PRIOR_ART_BOUNDARY.md`

## 5. Stage-B numerical adversary

Added:

- `numerics/verify_gravitational_endpoint_resource.py`
- `.github/workflows/experiment02-endpoint-resource.yml`

The regression is designed to test:

1. the pointwise `20/3` tensor identity for random positions;
2. exact Parseval saturation for complete discrete mass-weighted displacement bases;
3. Bessel inequality for random truncated modal subspaces;
4. invariance of total quadrupole strength under random orthogonal modal mixing;
5. the cumulative `4/3` linewidth bound for random mode frequencies below `Omega`.

The Stage-B result remains `DERIVED / VALIDATION PENDING` until this workflow passes on the actual `main` commit and the run/job IDs are recorded.

## 6. Current epistemic state

```text
spectral-area metric, finite stable cross block:      ESTABLISHED WITHIN MODEL
finite-dimensional passive selected-port cut:         ESTABLISHED WITHIN MODEL
finite-dimensional two-ended propagation cut:         ESTABLISHED WITHIN MODEL
20/3 modal quadrupole Bessel bound:                    DERIVED / VALIDATION PENDING
4/3 cumulative gravitational endpoint resource:        DERIVED / VALIDATION PENDING
Markov trace = sum gravitational energy linewidths:    DERIVED / VALIDATION PENDING
25/16 TT propagation in this throughput normalization: UNVERIFIED
25/12 final coefficient:                               UNVERIFIED
countably infinite modal extension:                    OPEN
passive recurrence statement:                          UNVERIFIED
complete historical prior-art boundary:                OPEN
publication significance:                              UNKNOWN
manuscript:                                             NONE
```

## 7. Experiment 01 boundary

`../01-causal-quantum-branch-information/` remains the frozen V7 publication project. Experiment 02 must not silently import V7's operational `25/16` normalization; Stage C will reconstruct the relevant TT propagation normalization independently.

## 8. Next action

1. Push the Stage-B derivation/regression to `main` and record the real CI result.
2. If Stage B passes, perform a second normalization audit of `Tr(K_g^dagger K_g)=sum kappa_g,n` and the literature collision search for the cumulative coefficient.
3. Only then begin Stage C: independently derive the normalized compact TT propagation operator for the Experiment-02 spectral-throughput metric.
