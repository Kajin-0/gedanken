# Passive Selected-Port Spectral-Area Cut — Independent Derivation

**Stage:** A  
**Status:** finite-dimensional passive Markov result derived; infinite-dimensional extension not addressed here.

## 1. Objective

Derive the strongest selected-port spectral-area inequality available from passivity alone, without assuming the desired gravitational inertia formula.

The result in this file is generic passive-systems mathematics. It is not a gravity-specific novelty claim.

## 2. Passive realization

Let the energy-normalized internal modal amplitude be `x in C^n`. Collect every physical loss/radiation channel into a port-coupling matrix

```math
K=\begin{bmatrix}K_1\\K_2\\\cdots\end{bmatrix}.
```

Take

```math
A=-iH-\frac12K^\dagger K,
\qquad H=H^\dagger,
```

or, more generally,

```math
A+A^\dagger\le -K^\dagger K.
```

For two disjoint port groups `i` and `o` with no direct cross-feedthrough, the strictly proper cross-transfer block is

```math
H_{o\leftarrow i}(\omega)
=-K_o(i\omega I-A)^{-1}K_i^\dagger.
```

The sign does not affect any norm below.

This realization is standard for passive linear input-output systems. For example, Guta and Yamamoto, arXiv:1303.3771, Eqs. (12)–(16), use

```math
A=-i\Omega-\frac12C^\dagger C,
\qquad
\Xi(s)=I-C(sI-A)^{-1}C^\dagger,
```

and note that the passive transfer matrix is unitary on the frequency axis when all channels are retained. Gough and Zhang, arXiv:1311.1375, likewise relate passive minimal realizations to Hurwitz stability and lossless-bounded-real transfer functions.

The derivation below is self-contained and uses only the dissipativity identity.

## 3. Frequency-integrated metric

For a stable strictly proper cross block, define the two-sided `H2` spectral area

```math
\|H_{o\leftarrow i}\|_2^2
\equiv
\frac1{2\pi}\int_{-\infty}^{\infty}
\operatorname{Tr}
\left[H_{o\leftarrow i}^\dagger(\omega)
H_{o\leftarrow i}(\omega)\right]d\omega.
```

Its impulse response is

```math
h_{o\leftarrow i}(t)
=-K_o e^{At}K_i^\dagger\,\Theta(t),
```

so Plancherel gives

```math
\|H_{o\leftarrow i}\|_2^2
=
\int_0^\infty
\|K_oe^{At}K_i^\dagger\|_F^2dt.
```

For a finite physical band `B`, the same nonnegative integrand immediately gives

```math
\frac1{2\pi}\int_B
\operatorname{Tr}(H^\dagger H)d\omega
\le \|H\|_2^2.
```

A one-sided physical-spectrum convention must be converted explicitly before numerical coefficients are imported later. Stage A therefore keeps the two-sided convention exact.

## 4. Input Gramian bound

Define the selected-input controllability Gramian

```math
P_i(\tau)
=
\int_0^\tau
e^{At}K_i^\dagger K_i e^{A^\dagger t}dt.
```

Since

```math
K_i^\dagger K_i\le K^\dagger K\le -(A+A^\dagger),
```

we have

```math
P_i(\tau)
\le
-\int_0^\tau
e^{At}(A+A^\dagger)e^{A^\dagger t}dt.
```

But

```math
\frac{d}{dt}
\left(e^{At}e^{A^\dagger t}\right)
=
e^{At}(A+A^\dagger)e^{A^\dagger t},
```

therefore

```math
\boxed{
0\le P_i(\tau)
\le I-e^{A\tau}e^{A^\dagger\tau}
\le I.
}
```

For a Hurwitz realization the exponential term vanishes as `tau -> infinity`, giving

```math
0\le P_i\le I.
```

Now

```math
\|H_{o\leftarrow i}\|_2^2
=
\operatorname{Tr}(K_oP_iK_o^\dagger),
```

so

```math
\boxed{
\|H_{o\leftarrow i}\|_2^2
\le
\operatorname{Tr}(K_o^\dagger K_o).
}
```

## 5. Output Gramian bound

Similarly define

```math
Q_o(\tau)
=
\int_0^\tau
e^{A^\dagger t}K_o^\dagger K_o e^{At}dt.
```

Using

```math
\frac{d}{dt}
\left(e^{A^\dagger t}e^{At}\right)
=
e^{A^\dagger t}(A^\dagger+A)e^{At},
```

gives

```math
0\le Q_o\le I.
```

The same `H2` norm can be written

```math
\|H_{o\leftarrow i}\|_2^2
=
\operatorname{Tr}(K_iQ_oK_i^\dagger),
```

hence

```math
\boxed{
\|H_{o\leftarrow i}\|_2^2
\le
\operatorname{Tr}(K_i^\dagger K_i).
}
```

Combining both sides,

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

This is the finite-dimensional selected-port cut.

## 6. Two-ended separated link

Let

- `H_A(omega)` map selected local source inputs to source gravitational output channels;
- `P(omega)` be separated propagation between normalized gravitational channel spaces;
- `H_B(omega)` map receiver gravitational inputs to selected local receiver outputs.

Then

```math
T(\omega)=H_B(\omega)P(\omega)H_A(\omega).
```

Because the full endpoint scattering matrices are contractive for passive systems with all loss ports retained, every cross block obeys

```math
\|H_A(\omega)\|_{\rm op}\le1,
\qquad
\|H_B(\omega)\|_{\rm op}\le1.
```

Suppose over the retained band

```math
\|P(\omega)\|_{\rm op}^2\le\eta_{\max}.
```

Using `||XYZ||_F <= ||X||_op ||Y||_op ||Z||_F`,

```math
\|T(\omega)\|_F^2
\le
\eta_{\max}\|H_A(\omega)\|_F^2.
```

Integrating over any band gives

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
```

where the source-side `H2` cut used the gravitational output resource.

Cutting from the receiver side instead gives

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B}).
```

Therefore

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

This is the desired Stage-A structural cut. No gravitational inertia relation has been used.

## 7. Dimensions

With energy-normalized internal amplitudes, each coupling matrix element has units `s^{-1/2}`. Thus

```math
\operatorname{Tr}(K_g^\dagger K_g)
```

has units `s^{-1}`.

Because `T(omega)` is dimensionless and `d omega` has units `s^{-1}`, the spectral area `Gamma_coh` also has units `s^{-1}`. Stage A is dimensionally consistent.

## 8. Scope and failure modes

The derivation currently requires:

- a finite-dimensional passive Markov realization, or a reduction to a stable controllable/observable finite sector;
- all dissipative channels included in the passive dilation or represented by the dissipativity inequality;
- no direct feedthrough between the selected disjoint cross-port groups when the full-line `H2` integral is used;
- a normalized propagation operator with a valid pointwise operator-norm ceiling.

Not yet established:

- countably infinite bounded-port sectors;
- unbounded PDE boundary ports;
- non-Markov continua;
- gravitational normalization of `K_g`;
- any inertia bound on `Tr(K_g^dagger K_g)`;
- the proposed `25/16` or `25/12` gravitational coefficients.

## 9. Numerical adversary

`numerics/verify_passive_selected_port_cut.py` generates random complex, noncommuting finite-dimensional passive systems, checks the exact Lyapunov `H2` identity and both endpoint trace cuts, verifies pointwise contractivity of the full scattering matrix, and numerically integrates random two-ended links against the cut above.

The test is deliberately generic: passing it supports this Stage-A algebra only; it says nothing yet about the gravitational resource or final inertia hypothesis.
