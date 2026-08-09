# Passive Linear-Network Cut-Set Theorem

## 1. Objective

The two-port theorem still assumes one source pole and one receiver pole. This note removes that restriction for **arbitrary stable finite-dimensional passive linear Markov endpoint networks**, including internal mode mixing and multiple overlapping resonances.

The result is a network theorem first. Its conversion into a material theorem requires a second step relating the endpoint gravitational coupling trace to the positive mass-quadrupole spectral weight.

---

## 2. Passive endpoint model

Let an endpoint contain a vector of bosonic internal modes

```math
\mathbf a=(a_1,\ldots,a_N)^T.
```

In a rotating frame, write the passive input-output equations as

```math
\dot{\mathbf a}
=A\mathbf a-K^\dagger\mathbf b_{\rm in},
```

```math
\mathbf b_{\rm out}
=\mathbf b_{\rm in}+K\mathbf a,
```

with

```math
\boxed{
A=-iH-\frac12K^\dagger K,
\qquad H=H^\dagger.
}
```

Hence

```math
\boxed{
A+A^\dagger=-K^\dagger K.
}
```

Partition the external channels into physically distinct sets. For a source endpoint, in particular,

```math
K=
\begin{pmatrix}
K_u\\
K_g\\
K_\ell
\end{pmatrix},
```

where

- `u` denotes useful local input channels;
- `g` denotes gravitational radiation channels;
- `ell` denotes all other passive loss channels.

Assume `A` is Hurwitz so all transients decay.

The cross transfer from local input to gravitational output has no direct feedthrough term and is

```math
\boxed{
S_{g\leftarrow u}(s)
=-K_g(sI-A)^{-1}K_u^\dagger.
}
```

The sign convention is irrelevant to all norm bounds below.

---

## 3. Spectral coherent-transfer norm

For a matrix transfer `S(i omega)`, define

```math
\boxed{
\|S\|_2^2
\equiv
\frac1{2\pi}
\int_{-\infty}^{\infty}
\operatorname{Tr}\!\left[
S^\dagger(i\omega)S(i\omega)
\right]d\omega.
}
```

This is the matrix generalization of the scalar efficiency-bandwidth integral used in the two-port calculation. It has units of inverse time because the input/output traveling fields have the standard white-noise normalization.

---

## 4. Endpoint gravitational-output lemma

### Lemma

For any stable passive endpoint of the form above,

```math
\boxed{
\|S_{g\leftarrow u}\|_2^2
\le
\operatorname{Tr}(K_g^\dagger K_g).
}
```

### Proof

Let the controllability Gramian generated only by the useful input channels be

```math
P_u
=\int_0^\infty
e^{At}K_u^\dagger K_u e^{A^\dagger t}\,dt.
```

It solves

```math
AP_u+P_uA^\dagger+K_u^\dagger K_u=0.
```

For the **complete** set of passive channels,

```math
P_{\rm all}
=\int_0^\infty
e^{At}K^\dagger K e^{A^\dagger t}\,dt.
```

Using

```math
A+A^\dagger=-K^\dagger K,
```

we have

```math
A I+I A^\dagger+K^\dagger K=0.
```

Stability makes the Lyapunov solution unique, hence

```math
\boxed{P_{\rm all}=I.}
```

Since

```math
0\le K_u^\dagger K_u\le K^\dagger K,
```

positivity of the integral representation gives

```math
\boxed{0\le P_u\le I.}
```

The standard frequency-domain/Gramian identity gives

```math
\|S_{g\leftarrow u}\|_2^2
=
\operatorname{Tr}(K_gP_uK_g^\dagger).
```

Therefore

```math
\|S_{g\leftarrow u}\|_2^2
\le
\operatorname{Tr}(K_gK_g^\dagger)
=
\operatorname{Tr}(K_g^\dagger K_g).
```

QED.

---

## 5. Dual receiver lemma

For a receiver endpoint, partition the channels into gravitational input/output channels `g`, useful local output channels `v`, and other losses. The cross transfer

```math
S_{v\leftarrow g}(s)
=-K_v(sI-A)^{-1}K_g^\dagger
```

obeys

```math
\boxed{
\|S_{v\leftarrow g}\|_2^2
\le
\operatorname{Tr}(K_g^\dagger K_g).
}
```

The proof is identical after exchanging the selected input and output channel sets, or equivalently by using the observability Gramian.

---

## 6. Pointwise contraction of passive scattering

When **all** passive channels are retained, the full frequency-domain scattering matrix of the endpoint is unitary on the real frequency axis. Any subblock is therefore contractive:

```math
\boxed{
\|S_{X\leftarrow Y}(i\omega)\|_{\rm op}\le1.
}
```

This property is what permits one endpoint to be placed downstream of another without increasing the upstream spectral-transfer norm.

---

## 7. Propagating gravitational channel

Let

```math
P_g(\omega)
```

map the source gravitational outgoing channel basis to the receiver gravitational incoming channel basis. Assume one-way propagation in the retained approximation and define

```math
\boxed{
\eta_{\max}
\equiv
\sup_{\omega\in\mathcal B}
\|P_g(\omega)\|_{\rm op}^2
\le1.
}
```

The full useful transfer is

```math
\boxed{
T(\omega)
=
S_{v\leftarrow g}^{(B)}(i\omega)
P_g(\omega)
S_{g\leftarrow u}^{(A)}(i\omega).
}
```

Define the integrated coherent-transfer throughput

```math
\boxed{
\Gamma_{\rm coh}
\equiv
\frac1{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
}
```

---

## 8. Passive-network cut-set theorem

### Theorem

For two stable finite-dimensional passive linear Markov endpoint networks connected by a one-way contractive gravitational propagation operator,

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

### Source-side proof

Using the Frobenius/operator-norm inequality,

```math
\|XYZ\|_F
\le
\|X\|_{\rm op}\|Y\|_{\rm op}\|Z\|_F,
```

pointwise in frequency,

```math
\|T(\omega)\|_F^2
\le
\|S_{v\leftarrow g}^{(B)}\|_{\rm op}^2
\|P_g\|_{\rm op}^2
\|S_{g\leftarrow u}^{(A)}\|_F^2.
```

Passivity gives the first factor at most unity and propagation gives the second at most `eta_max`. Integrating,

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\|S_{g\leftarrow u}^{(A)}\|_2^2
\le
\eta_{\max}
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}).
```

### Receiver-side proof

Instead use

```math
\|XYZ\|_F
\le
\|X\|_F\|Y\|_{\rm op}\|Z\|_{\rm op}.
```

The source cross scattering block is contractive, so

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\|S_{v\leftarrow g}^{(B)}\|_2^2
\le
\eta_{\max}
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B}).
```

Combining both cut-set bounds proves the theorem.

QED.

---

## 9. What this removes

The theorem does **not** require

- a single resonance;
- diagonal internal normal modes;
- nonoverlapping resonances;
- independent parallel channels;
- critical coupling;
- identical source and receiver linewidths.

Arbitrary coherent mode mixing inside each endpoint is allowed as long as the endpoint remains finite-dimensional, stable, linear, time invariant, Markovian, and passive.

This is the first genuinely architecture-independent result within that passive linear-network class.

---

## 10. Connection to the two-pole theorem

For one internal source mode and one internal receiver mode,

```math
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A})=\kappa_{g,A},
```

```math
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})=\kappa_{g,B}.
```

If the propagation operator is a scalar with

```math
|P_g|^2=\eta_{\rm prop},
```

the general theorem reduces immediately to

```math
\Gamma_{\rm coh}
\le
\eta_{\rm prop}
\min(\kappa_{g,A},\kappa_{g,B}),
```

which is exactly the two-port EBP ceiling.

---

## 11. Material-response bridge

The remaining physics step is to relate

```math
\operatorname{Tr}(K_g^\dagger K_g)
```

to a microscopic passive mass-quadrupole spectral resource.

For a set of weakly damped ground-state normal modes below an operating ceiling `Omega`, the diagonal entries of `K_g^\dagger K_g` are the corresponding gravitational decay rates, so

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_{n\in\mathcal B}\kappa_{g,n}
\le K_g(\Omega),
```

and the cumulative EWSR gives

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
}
```

Under that identification, the network theorem yields

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\frac{4G\Omega^4}{3c^5}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

This is already valid for arbitrary **passive linear mode networks** whose gravitational Markov coupling matrices resolve the same positive transition weights entering the EWSR.

The extension to a completely general interacting finite-temperature susceptibility should be stated only after the relation between the Markov coupling trace and the net positive absorptive spectral measure is derived carefully.

---

## 12. Important limitation: propagation geometry

The scalar V7 factor

```math
25/[16(kR)^2]
```

is not inserted into the general theorem. The correct general propagation resource is

```math
\eta_{\max}(\omega)
=\|P_g(\omega)\|_{\rm op}^2,
```

whose singular channels depend on frequency, orientation, tensor polarization, source/receiver geometry, and the wave-zone approximation.

The V7 aligned plus-quadrupole result is a single-channel specialization of this operator statement.

---

## 13. Current strongest claim boundary

What is now proved, conditional on standard passive input-output normalization, is:

> A stable passive linear source/receiver network cannot increase the frequency-integrated coherent transmission through a contractive gravitational link beyond the smaller total gravitational coupling rate available at its two material interfaces.

What is **not** yet proved is the same statement for arbitrary nonlinear/interacting matter outside a linear Markov realization, nor a universal quantum-capacity theorem.
