# Current State — Experiment 02

**Status:** **PASSIVE LINEAR-NETWORK CUT-SET THEOREM PROVED; MATERIAL-RESPONSE BRIDGE PARTLY CLOSED; GENERAL NON-MARKOV SUSCEPTIBILITY EXTENSION OPEN**

## 1. Research question

Can the speed–efficiency tradeoff found in Experiment 01 be promoted to a broad passive gravitational throughput bound that cannot be evaded by arbitrarily high Q, multiple resonances, or coherent mode mixing?

Current answer:

> **Yes for stable finite-dimensional passive linear Markov endpoint networks.**

The remaining question is how far the material-response step can be extended beyond that class without introducing hidden assumptions.

Experiment 01 / V7 remains frozen and is not modified by this branch.

---

## 2. Exact two-port spectral result

For the stationary two-resonator transducer extension,

```math
\Gamma_{\rm EBP}
\equiv
\frac1{2\pi}
\int_{-\infty}^{\infty}\tau(\Omega)d\Omega
```

has the exact form

```math
\boxed{
\Gamma_{\rm EBP}
=
\frac{
4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}
}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}.
}
```

Passivity implies

```math
\boxed{
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}
\min(\kappa_{g,A},\kappa_{g,B}).
}
```

This removes arbitrary bandwidth conventions. The high-Q escape route is replaced by an exact area law: raising peak conversion by reducing ordinary loss narrows the usable spectral response so that the integrated area remains gravitationally limited.

For symmetric intrinsic gravitational rates with no internal loss, the optimal external coupling is

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
```

and

```math
\boxed{
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
}
```

---

## 3. Passive linear-network theorem

For a stable passive endpoint

```math
A=-iH-\frac12K^\dagger K,
```

so

```math
A+A^\dagger=-K^\dagger K.
```

Partition the channels into useful local, gravitational, and ordinary loss channels. For the source cross transfer from local input to gravitational output,

```math
S_{g\leftarrow u}(s)
=-K_g(sI-A)^{-1}K_u^\dagger.
```

The selected-input Gramian satisfies

```math
0\le P_u\le I
```

because the complete-channel Gramian is exactly `I`. Hence

```math
\boxed{
\|S_{g\leftarrow u}\|_2^2
\le
\operatorname{Tr}(K_g^\dagger K_g).
}
```

The reciprocal receiver cross block obeys the same bound.

Let the one-way gravitational propagation operator satisfy

```math
\eta_{\max}
=\sup_{\omega\in\mathcal B}
\|P_g(\omega)\|_{\rm op}^2
\le1.
```

For

```math
T(\omega)
=
S_{v\leftarrow g}^{(B)}
P_g
S_{g\leftarrow u}^{(A)},
```

define

```math
\boxed{
\Gamma_{\rm coh}
=
\frac1{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger T]d\omega.
}
```

Then

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

This permits arbitrary passive coherent mode mixing and overlapping resonances inside both endpoints. It does not require independent scalar channels.

Canonical derivation:

`PASSIVE_NETWORK_CUTSET_THEOREM.md`

---

## 4. Cumulative material spectral-weight bound

For a stationary passive nonrelativistic matter system, define the positive quadrupole spectral measure

```math
d\mu_Q(\omega)
=
\sum_{m<n,a}
(p_m-p_n)|Q^a_{mn}|^2
\delta(\omega-\omega_{nm})d\omega.
```

The EWSR gives

```math
\int_0^\infty\omega\,d\mu_Q(\omega)
=
\frac{10}{3}\hbar\langle I\rangle.
```

The cumulative gravitational transition-rate weight below operating ceiling `Omega` therefore obeys

```math
\boxed{
K_g(\Omega)
\le
\frac{4G}{3c^5}
\langle I\rangle\Omega^4.
}
```

This controls arbitrarily many passive quadrupole transition lines inside a finite operating band.

For passive linear mode networks whose gravitational Markov coupling trace resolves these positive transition rates,

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le K_g(\Omega),
```

so the current strongest material-level coherent-transfer theorem is

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

This statement is currently restricted to the passive linear Markov realization for which the coupling-trace / positive-spectral-weight identification is controlled.

---

## 5. Quantum-information corollaries

`Gamma_coh` is a physical coherent-transfer integral, not itself a capacity.

For the stationary vacuum pure-loss realization, let `tau_n(omega)` be the transmission eigenvalues. Passivity and propagation imply

```math
\tau_n(\omega)\le\eta_{\max}.
```

Therefore:

### Unassisted capacity

If

```math
\eta_{\max}\le1/2,
```

then every pure-loss eigenchannel lies below the degradability threshold and

```math
\boxed{Q_1=0.}
```

### Two-way-assisted capacity

For `eta_max < 1`,

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
}
```

Combining with the network theorem gives

```math
\boxed{
Q_2
\le
\frac{\eta_{\max}}
{\ln2\,(1-\eta_{\max})}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

And with the controlled material-response bridge,

```math
\boxed{
Q_2
\le
\frac{\eta_{\max}}
{\ln2\,(1-\eta_{\max})}
\frac{4G\Omega^4}{3c^5}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

These capacity statements are **pure-loss stationary corollaries**, not universal noisy-gravity capacity theorems.

Canonical derivation:

`CAPACITY_COROLLARIES.md`

---

## 6. Relation to V7 aligned quadrupole benchmark

For the V7 aligned wave-zone single channel,

```math
\eta_{\rm prop}
=\frac{25\mathcal O}{16(kR)^2}.
```

At `kR=10`, `O=1`,

```math
\eta_{\rm prop}=0.015625<1/2.
```

Thus the corresponding stationary pure-loss transducer has zero unassisted asymptotic quantum capacity, even though V7 correctly shows that finite reference–receiver negativity survives for any nonzero pure-loss transmissivity.

For the inherited benchmark gravitational linewidth,

```math
\eta_{\rm prop}\kappa_g
=1.0734375\times10^{-27}\;\mathrm{s}^{-1},
```

with inverse scale approximately

```math
2.95\times10^{19}\;\mathrm{yr}.
```

This remains a coherent-transfer/cut-set timescale, not literally “one qubit every `2.95e19` years.”

---

## 7. Validation state

Two numerical regression scripts now exist:

- `numerics/verify_two_port_bound.py`
- `numerics/verify_passive_network_cutset.py`

Independent exploratory checks performed during development found:

- direct quadrature agrees with the exact two-pole EBP formula;
- 200,000 random passive two-pole rate sets showed no bound violation;
- the symmetric optimum is `8/27` at external coupling `2 kappa_g`;
- random passive multi-mode Gramians satisfy `0 <= P <= I`;
- random multi-mode endpoint H2 norms remain below the gravitational coupling trace;
- direct quadrature of random low-dimensional cascades remains below the network cut-set ceiling.

Branch-only automated regression should be added before any manuscript-level claim.

---

## 8. Primary formalism cross-check

The passive linear quantum input-output form used here is standard: passive systems have

```math
A=-i\Omega-\frac12C^\dagger C
```

and transfer matrix

```math
\Xi(s)=I-C(sI-A)^{-1}C^\dagger,
```

with `Xi(i omega)` unitary for real frequency when all channels are included. The branch derivation uses these identities plus standard Lyapunov/Gramian relations; it does not assume a new passive-system formalism.

Relevant primary literature is tracked in `LITERATURE_MAP.md`.

---

## 9. Open physics problem

The deepest remaining issue is no longer the high-Q loophole or parallel resonances. It is:

> **Can the coupling-trace resource in the passive Markov theorem be replaced directly by a general matrix-valued quadrupole susceptibility/spectral measure for arbitrary interacting passive matter, while preserving a rigorous end-to-end TT propagation bound?**

That requires connecting

```math
\operatorname{Im}\chi_{QQ}(\omega)
```

to a physically normalized set of gravitational scattering channels without assuming a finite-dimensional Markov realization.

A successful proof would produce the broad architecture-independent gravitational response theorem originally sought.

---

## 10. Current claim boundary

### Proved within stated assumptions

1. exact two-pole gravitational efficiency-bandwidth integral;
2. passive two-pole EBP ceiling;
3. stable passive linear-network cut-set theorem;
4. cumulative finite-band passive quadrupole gravitational spectral-weight bound;
5. pure-loss continuous-time capacity corollaries;
6. passive material bound for linear Markov mode networks whose gravitational coupling trace resolves the EWSR transition weight.

### Open

1. arbitrary non-Markov/interacting susceptibility theorem;
2. full TT operator normalization over arbitrary source/receiver tensor channels;
3. thermal/noisy capacity theorem;
4. active-resource escape classification;
5. dedicated gravity-specific novelty audit.

### Forbidden for now

- “universal gravitational quantum capacity bound”;
- “all passive matter” without the linear-response realization qualifier;
- first/unique/unprecedented claims;
- claims that zero unassisted capacity means no entanglement survives;
- merging Experiment 02 into V7.
