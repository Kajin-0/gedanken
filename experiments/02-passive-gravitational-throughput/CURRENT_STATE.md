# Current State — Experiment 02

**Status:** **PASSIVE LINEAR-NETWORK THROUGHPUT THEOREM CLOSED FOR COMPACT QUADRUPOLE MATTER LINKS; GENERAL INTERACTING/NON-MARKOV EXTENSION OPEN**

## 1. Research question

Can the speed–efficiency tradeoff found in Experiment 01 be promoted to a broad passive gravitational throughput bound that cannot be evaded by arbitrarily high Q, many resonances, coherent mode mixing, or a different compact quadrupole orientation?

Current answer:

> **Yes for stable passive linear bosonic matter networks coupled through compact quadrupole radiation in the weak one-way wave zone.**

The present theorem no longer depends on the four-spoke source architecture. Experiment 01 / V7 remains frozen and is not modified by this branch.

---

## 2. Physical throughput metric

For the useful stationary source-to-receiver transfer matrix `T(omega)`, define

```math
\boxed{
\Gamma_{\rm coh}
=\frac1{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
}
```

`Gamma_coh` has units of inverse time. It is a frequency-integrated coherent-transfer / efficiency-bandwidth quantity, **not itself a quantum capacity**.

---

## 3. Passive linear-network cut-set theorem

For a stable passive endpoint

```math
A=-iH-\frac12K^\dagger K,
```

partition the channels into useful local, gravitational, and ordinary-loss ports. The passive identity

```math
A+A^\dagger=-K^\dagger K
```

makes the complete-channel controllability Gramian exactly the identity. For the source local-input to gravitational-output block,

```math
\boxed{
\|S_{g\leftarrow u}\|_2^2
\le
\operatorname{Tr}(K_g^\dagger K_g).
}
```

The receiver dual obeys the same bound.

Let the one-way gravitational propagation operator be `P_g(omega)` and define

```math
\eta_{\max}
=\sup_{\omega\in\mathcal B}
\|P_g(\omega)\|_{\rm op}^2.
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

This theorem permits arbitrary finite-dimensional passive coherent mode mixing and overlapping resonances. It assumes no direct feedthrough that converts a useful local channel into a gravitational channel without passing through the modeled material degrees of freedom; any such physical converter must be included as part of the endpoint resource accounting.

Canonical derivation: `PASSIVE_NETWORK_CUTSET_THEOREM.md`.

---

## 4. Material-response bridge — closed for passive linear bosonic matter

Diagonalize the isolated linear matter Hamiltonian into normal modes. The gravitational coupling matrix transforms unitarily, so

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}.
}
```

Each one-quantum quadrupole mode has

```math
\kappa_{g,n}
=
\frac{2G\omega_n^5}{5\hbar c^5}
Q_{ij}^{0n}Q_{ij}^{n0}.
```

For retained mode frequencies `0 < omega_n <= Omega`, the positive quadrupole EWSR gives the cumulative ceiling

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}
\langle I\rangle\Omega^4.
}
```

Therefore

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

Equivalently, with `L_j^2=<I_j>/M_j`,

```math
\boxed{
\Gamma_{\rm coh}
\le
\frac23\eta_{\max}\Omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

The microscopic EWSR assumes ordinary compact nonrelativistic matter with the standard coordinate-quadrupole commutator structure. It is not asserted for arbitrary relativistic fields or effective Hamiltonians with unaccounted velocity-dependent microscopic interactions.

Canonical derivations: `MATERIAL_RESPONSE_BRIDGE.md`, `SPECTRAL_GENERALIZATION.md`.

---

## 5. TT geometry — closed for compact quadrupole wave-zone channels

For arbitrary complex STF quadrupole `Q`, the TT projector `Lambda(n)` gives

```math
D_Q(\hat n)
=
\frac52
\frac{Q^*:\Lambda(\hat n):Q}{Q^*:Q}
\le\frac52.
```

A direct normalized one-graviton stationary-phase calculation gives the leading outgoing wave-zone transfer

```math
\boxed{
t_{BA}^{\rm TT}
=
-\frac{5i}{4kR}e^{ikR}
\frac{Q_B^*:\Lambda(\hat R):Q_A}
{\sqrt{Q_A^*:Q_A}\sqrt{Q_B^*:Q_B}}
+O((kR)^{-2}).
}
```

Since `||Lambda||_op=1`,

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le
\frac{25}{16[k(\omega)R]^2}
}
```

at leading wave-zone order. Equality is attained by matched source and receiver tensors lying in the line-of-sight TT subspace, including the V7 aligned plus mode.

Thus `25/16` is the maximum compact-quadrupole wave-zone singular-channel coefficient within this class, not a special assumption inherited from the four-spoke geometry.

Canonical derivation: `TT_PROPAGATION_BOUND.md`.

---

## 6. Closed narrowband compact-quadrupole theorem

For a narrow operating band centered at `omega`, with `k=omega/c` and `kR >> 1`, combine the material and geometry bounds:

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25}{16(kR)^2}
\frac{4G\omega^4}{3c^5}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

or

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25}{24(kR)^2}
\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

This is the current headline physical theorem.

For a finite broad band `[omega_-,omega_+]` entirely in the wave zone, keep the two edges distinct:

```math
\eta_{\max}
\lesssim
\frac{25c^2}{16R^2\omega_-^2},
```

while the cumulative EWSR uses `omega_+^4`. Hence a safe broad-band form is

```math
\boxed{
\Gamma_{\rm coh}(\mathcal B)
\lesssim
\frac{25G}{12c^3R^2}
\frac{\omega_+^4}{\omega_-^2}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right),
}
```

provided `omega_- R/c >> 1` and the compact quadrupole approximation remains valid throughout the band. This form is intentionally looser than the narrowband theorem.

---

## 7. Exact two-pole specialization

For one source and receiver pole with explicit local input/output ports,

```math
\boxed{
\Gamma_{\rm EBP}
=
\frac{
4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}
}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
}
```

For symmetric intrinsic gravitational linewidths and no internal loss, the integrated spectral-area optimum occurs at

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
```

with

```math
\boxed{
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
}
```

Canonical derivation: `TWO_PORT_SPECTRAL_BOUND.md`.

---

## 8. Pure-loss quantum-information corollaries

For a stationary vacuum pure-loss realization, each transmission eigenvalue obeys

```math
\tau_n(\omega)\le\eta_{\max}.
```

If

```math
\eta_{\max}\le1/2,
```

then the unassisted continuous-time pure-loss quantum capacity is

```math
\boxed{Q_1=0.}
```

For `eta_max < 1`, the two-way-assisted capacity obeys

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
}
```

These are operational corollaries of the physical response theorem, not the definition of `Gamma_coh` and not universal noisy-gravity capacity statements.

Canonical derivation: `CAPACITY_COROLLARIES.md`.

---

## 9. Band-local Markov scope

The network proof uses a Markov input-output realization. Gravitational quadrupole coupling varies strongly with frequency, so a single frequency-independent `K_g` should not be stretched across an arbitrarily broad spectrum.

For widely separated resonances, the controlled interpretation is a direct sum of sufficiently narrow Markov sectors, or ultimately a non-Markov susceptibility formulation. The cumulative EWSR then bounds the summed gravitational spectral resource across those sectors.

This does not affect the narrowband theorem or the finite-dimensional local-sector cut-set proof; it is the main formal issue in extending the result to a genuinely arbitrary broadband susceptibility.

---

## 10. Validation state

Automated branch regression covers three independent layers:

1. exact two-pole spectral integral and random passive rate sets;
2. random multi-mode passive Gramians, endpoint H2 bounds, and directly integrated cascades;
3. random complex STF quadrupoles, TT directivity, angular normalization, and `25/16` wave-zone coefficient.

GitHub Actions run `31310582891`, job `93237694140`, completed successfully with all three regression stages passing.

---

## 11. Novelty status

**Promising but unverified — no priority claim.**

A targeted current search found established work on generic continuous-time transducer capacity, passive efficiency-bandwidth limits, passive linear quantum-network formalism, microscopic graviton absorption, gravitational detector coupling limits, and propagating-gravity quantum-information channels. No inspected source yet combined the full chain

```text
passive material network
-> gravitational interface cut set
-> mass-quadrupole EWSR
-> compact TT propagation ceiling
-> end-to-end integrated coherent-transfer bound
-> pure-loss capacity corollary.
```

This remains a negative search result, not proof of priority.

See `INITIAL_NOVELTY_SWEEP.md` and `LITERATURE_MAP.md`.

---

## 12. Open problems

### Publication-critical before manuscript claim

1. independent adversarial audit of the passive-network proof and the direct TT stationary-phase normalization;
2. deeper collision search in passive H2/scattering-sum-rule and gravitational-antenna literature;
3. decide whether the cleanest paper claim should stop at passive linear bosonic matter or also derive a full susceptibility/dilation extension.

### Valuable later extensions

1. arbitrary interacting/non-Markov passive susceptibility theorem;
2. thermal/noisy channel capacities;
3. active/inverted and parametrically driven escape resources;
4. extended apertures, higher multipoles, and relativistic sources;
5. finite-time rather than asymptotic continuous-frequency communication.

### Forbidden for now

- “universal gravitational quantum capacity bound”;
- “all passive matter” without the stated linear/nonrelativistic assumptions;
- first/unique/unprecedented claims;
- claims that zero unassisted capacity means no entanglement survives;
- applying `25/16` to extended arrays, higher multipoles, or the near field;
- merging Experiment 02 into V7.
