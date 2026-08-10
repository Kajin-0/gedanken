# Countably Infinite Bounded-Port Passive Extension

**Stage:** E  
**Status:** operator derivation; truncation stress test pending.  
**Scope:** separable modal Hilbert spaces with bounded Markov port operators and Hilbert–Schmidt gravitational port. This is not a theorem for arbitrary unbounded PDE boundary ports.

## 1. Why this step is needed

The finite-dimensional Stage-A proof uses controllability/observability Gramians. A physical elastic body can have countably many normal modes, so finite matrix dimension should not be a hidden resource constraint.

The correct question is not whether large finite truncations pass. It is whether the passive cut can be stated directly on a separable Hilbert space.

## 2. Passive Hilbert-space model

Let the internal modal state space `X` be a separable Hilbert space and the total port space `Y` another Hilbert space. Let

```math
K:X\to Y
```

be bounded, with selected port blocks `K_u`, `K_y`, and gravitational block `K_g` obtained by orthogonal projections in `Y`.

Let `H` be self-adjoint (possibly unbounded on its natural domain) and suppose

```math
A=-iH-\frac12K^\dagger K
```

generates the passive contraction semigroup

```math
\mathcal T(t)=e^{At}.
```

The only semigroup property used below is the passive energy inequality, understood in weak/operator-form sense,

```math
\boxed{
\mathcal T(\tau)\mathcal T^\dagger(\tau)
+
\int_0^\tau
\mathcal T(t)K^\dagger K\mathcal T^\dagger(t)dt
\le I,
}
```

and its dual ordering

```math
\boxed{
\mathcal T^\dagger(\tau)\mathcal T(\tau)
+
\int_0^\tau
\mathcal T^\dagger(t)K^\dagger K\mathcal T(t)dt
\le I.
}
```

For the lossless Markov dilation equality holds; the inequality form also permits additional passive dissipation already absorbed into the generator.

This is the declared bounded-port passive Markov class. Arbitrary boundary-control PDEs with unbounded control/observation maps require separate admissibility theory and are not silently included.

## 3. Selected-input Gramian

Define the finite-time positive operator

```math
P_u(\tau)
=\int_0^\tau
\mathcal T(t)K_u^\dagger K_u\mathcal T^\dagger(t)dt.
```

Because

```math
0\le K_u^\dagger K_u\le K^\dagger K,
```

passivity immediately gives

```math
\boxed{
0\le P_u(\tau)
\le I-\mathcal T(\tau)\mathcal T^\dagger(\tau)
\le I.
}
```

`P_u(tau)` is monotone increasing in the positive-operator order and uniformly bounded by `I`. Therefore it has a strong operator limit

```math
P_u=\operatorname{s-lim}_{\tau\to\infty}P_u(\tau),
```

with

```math
\boxed{0\le P_u\le I.}
```

No finite matrix dimension and no asymptotic decay of every dark internal mode is required for this inequality.

## 4. Gravitational port regularity from Stage B

The source gravitational impulse response is

```math
h_{g\leftarrow u}(t)
=K_g\mathcal T(t)K_u^\dagger.
```

To take an operator-valued `H2` norm, `K_g` must carry enough compactness that the relevant trace is finite.

Stage B provides exactly that resource. In a countable mass-orthogonal quadrupolar modal sector with retained frequencies below `Omega`,

```math
\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}I_2\Omega^4<\infty.
```

In energy-normalized modal coordinates,

```math
\|K_g\|_{\rm HS}^2
=\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}.
```

Therefore

```math
\boxed{K_g\ \text{is Hilbert--Schmidt}.}
```

This conclusion is not an extra modal-count assumption; it follows from the inertia resource itself.

## 5. Infinite-dimensional source-side H2 cut

Because `K_g` is Hilbert–Schmidt and `K_u` and `T(t)` are bounded, the impulse operator `h(t)` is Hilbert–Schmidt. Its squared Hilbert–Schmidt norm integrates as

```math
\begin{aligned}
\int_0^\infty
\|K_g\mathcal T(t)K_u^\dagger\|_{\rm HS}^2dt
&=
\operatorname{Tr}
\left(K_gP_uK_g^\dagger\right)\\
&\le
\operatorname{Tr}(K_gK_g^\dagger).
\end{aligned}
```

Hence

```math
\boxed{
\int_0^\infty
\|h_{g\leftarrow u}(t)\|_{\rm HS}^2dt
\le
\operatorname{Tr}(K_g^\dagger K_g).
}
```

The space of Hilbert–Schmidt operators is itself a Hilbert space. Hilbert-space Plancherel therefore gives an `L2` frequency-domain boundary function and

```math
\boxed{
\|H_{g\leftarrow u}\|_2^2
\le
\operatorname{Tr}(K_g^\dagger K_g).
}
```

This is the direct countably infinite source-side version of the Stage-A cut.

## 6. Receiver-side dual cut

Define

```math
Q_y(\tau)
=\int_0^\tau
\mathcal T^\dagger(t)K_y^\dagger K_y\mathcal T(t)dt.
```

The dual passive energy inequality gives

```math
0\le Q_y\le I.
```

For gravitational input and selected local output,

```math
h_{y\leftarrow g}(t)
=K_y\mathcal T(t)K_g^\dagger,
```

so

```math
\int_0^\infty
\|K_y\mathcal T(t)K_g^\dagger\|_{\rm HS}^2dt
=
\operatorname{Tr}(K_gQ_yK_g^\dagger)
\le
\operatorname{Tr}(K_g^\dagger K_g).
```

Thus the receiver gravitational-input cut has the same resource ceiling.

## 7. Two-ended consequence

The pointwise separated propagation contraction from Stage C can be inserted exactly as in finite dimension because bounded left/right multiplication preserves the Hilbert–Schmidt ideal:

```math
\|AXB\|_{\rm HS}
\le\|A\|_{\rm op}\,\|X\|_{\rm HS}\,\|B\|_{\rm op}.
```

Therefore the Stage-A structural cut extends to the declared separable bounded-port modal class:

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

Combining with Stages B and C gives the same narrowband leading theorem

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
}
```

for finite **or countably infinite bounded-port Markov modal sectors**.

## 8. Why this does not prove an arbitrary PDE theorem

Infinite-dimensional control theory distinguishes bounded internal/port operators from unbounded boundary control and observation operators. The latter require admissibility hypotheses and can have domain subtleties not present above.

Experiment 02 therefore does **not** infer from this proof that arbitrary elastic PDE boundary ports, singular point couplings, or genuinely non-Markov continua obey the same theorem without further analysis.

Historical systems references for the broader mathematical setting include:

- J. S. Baras and R. W. Brockett, *H2-Functions and Infinite-Dimensional Realization Theory*, SIAM Journal on Control **13**, 221–241 (1975), DOI `10.1137/0313013`.
- M. R. Opmeer, T. Reis, and W. Wollner, *Finite-Rank ADI Iteration for Operator Lyapunov Equations*, SIAM Journal on Control and Optimization **51**, 4084–4117 (2013), DOI `10.1137/120885310`.

These references establish that infinite-dimensional `H2` realizations and operator Lyapunov/Gramian machinery are historical. No novelty is claimed for that mathematics.

## 9. Numerical truncation stress test

`numerics/verify_infinite_modal_truncations.py` should construct a fixed square-summable gravitational-port sequence and bounded local/hidden ports, increase the modal truncation dimension, and check:

1. `lambda_max(P_u) <= 1` for every truncation;
2. the H2/resource ratio never exceeds unity;
3. the gravitational trace approaches a finite limit as mode count grows;
4. random unitary mixing of the retained modal space does not change the gravitational trace or violate the cut.

This is a consistency/stability check only. The operator argument above is the actual infinite-dimensional proof.
