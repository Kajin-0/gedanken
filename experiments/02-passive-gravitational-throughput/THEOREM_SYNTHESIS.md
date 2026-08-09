# Theorem Synthesis — Passive Compact-Quadrupole Gravitational Throughput

## 1. Headline result

For a narrowband link between two compact passive nonrelativistic **linear bosonic matter networks**, coupled through propagating linearized gravity in the weak one-way wave zone, define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}
\int
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
```

Under the assumptions listed below,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

This is the simplest form of the current Experiment 02 theorem.

It contains:

- no quality factor `Q`;
- no branching fraction;
- no four-spoke geometry parameter;
- no assumed number of internal modes;
- no critical-coupling assumption.

The only endpoint material resource remaining is the smaller mass inertia moment available to the two passive compact quadrupole interfaces, at the stated operating frequency.

---

## 2. Assumptions

The theorem currently requires all of the following.

### Gravity

- weak linearized gravity;
- leading mass-quadrupole coupling;
- source and receiver compact relative to the wavelength;
- weak one-way wave-zone propagation;
- no near-field/reactive storage used as a communication channel;
- no extended phased aperture or higher-multipole beaming.

### Matter endpoints

- ordinary nonrelativistic matter with the coordinate-quadrupole EWSR used in Experiment 01;
- linearized bosonic endpoint dynamics about a stationary operating point;
- stable passive time-invariant input-output realization in each narrow Markov sector;
- no active gain, inversion, parametric pumping, or unaccounted direct local-to-gravity feedthrough;
- gravitational vacuum coupling represented by the microscopic quadrupole transition rates.

### Band

- narrow enough that one carrier `omega` and the leading wave-zone propagation factor are meaningful;
- compactness `omega L_j / c << 1` and wave-zone separation `omega R / c >> 1` hold simultaneously.

---

## 3. Proof dependency chain

The headline theorem is the product of three independent inequalities.

### A. Passive-network cut set

For each endpoint,

```math
A=-iH-\frac12K^\dagger K
```

and passivity implies

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

Source: `PASSIVE_NETWORK_CUTSET_THEOREM.md`.

### B. Passive quadrupole spectral resource

For a linear bosonic matter endpoint with retained quadrupole-active modes below `omega`,

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
```

and the quadrupole EWSR gives

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\lesssim
\frac{4G\omega^4}{3c^5}\langle I\rangle.
}
```

Source: `MATERIAL_RESPONSE_BRIDGE.md`.

### C. Compact TT propagation

The normalized one-graviton propagation map between compact STF quadrupole channel spaces obeys

```math
\boxed{
\eta_{\max}
=\|P_g\|_{\rm op}^2
\lesssim
\frac{25}{16(kR)^2}.
}
```

Source: `TT_PROPAGATION_BOUND.md`.

Multiplying B and C into A gives

```math
\Gamma_{\rm coh}
\lesssim
\frac{25}{16(kR)^2}
\frac{4G\omega^4}{3c^5}
\min(\langle I_A\rangle,\langle I_B\rangle).
```

Since `k=omega/c`,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

---

## 4. Physical interpretation

Increasing endpoint Q can improve gravitational branching because ordinary loss is removed. But the same operation narrows the endpoint's usable spectral response toward its tiny intrinsic gravitational coupling rate.

The integrated transfer area is therefore limited by the gravitational oscillator strength itself:

```math
\text{large peak efficiency}
\Longleftrightarrow
\text{small usable linewidth}
```

inside the passive class.

Adding additional passive resonances does not remove the ceiling because the quadrupole EWSR limits the total positive gravitational spectral weight that can be distributed among them. Coherent internal mode mixing does not remove it because the passive-network theorem depends only on the basis-invariant coupling trace.

Changing the compact quadrupole orientation does not remove it because the TT projector limits every compact quadrupole's directivity to `5/2`.

Thus three obvious passive escape routes are simultaneously closed:

```text
high Q
many modes
better compact quadrupole orientation
```

---

## 5. Pure-loss capacity consequences

For a stationary vacuum pure-loss realization, every transfer eigenvalue satisfies

```math
\tau_n(\omega)\le\eta_{\max}.
```

In the wave zone `kR >> 1`, the compact-quadrupole propagation ceiling is automatically far below `1/2`. Hence the unassisted asymptotic pure-loss quantum capacity is

```math
\boxed{Q_1=0}
```

for this far-field compact-quadrupole channel class.

This does **not** imply that no finite-use entanglement survives.

With unlimited two-way classical assistance,

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
```

Thus the material throughput theorem becomes an explicit upper bound on two-way entanglement-distribution rate in the vacuum pure-loss model.

---

## 6. Broad-band safe form

For a finite operating band

```math
\mathcal B=[\omega_-,\omega_+]
```

with the entire band in the wave zone and compact-quadrupole regime, use separate frequency edges:

```math
\eta_{\max}
\lesssim
\frac{25c^2}{16R^2\omega_-^2},
```

while the cumulative EWSR gives

```math
\operatorname{Tr}(K_g^\dagger K_g)
\lesssim
\frac{4G}{3c^5}\langle I\rangle\omega_+^4.
```

Therefore

```math
\boxed{
\Gamma_{\rm coh}(\mathcal B)
\lesssim
\frac{25G}{12c^3R^2}
\frac{\omega_+^4}{\omega_-^2}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

This is deliberately looser than the narrowband result. A sharper genuinely broadband theorem should keep the frequency dependence inside the spectral integral rather than taking separate suprema.

---

## 7. Benchmark connection

For the V7 benchmark, the simple endpoint cut-set scale was

```math
\eta_{\rm prop}\kappa_g
\simeq1.07\times10^{-27}\;\mathrm{s}^{-1},
```

whose inverse is about

```math
2.95\times10^{19}\;\mathrm{yr}.
```

The new theorem explains why this is not merely a poor choice of Q: in the passive class the integrated response remains tied to the same microscopic gravitational oscillator-strength scale.

Do not interpret the inverse directly as a universal “time per qubit.”

---

## 8. What would evade the theorem

The theorem itself identifies the resources that must be changed to escape it:

- **active / inverted matter** — breaks the positive passive spectral-weight argument;
- **parametric/time-dependent driving** — leaves the passive time-invariant network class;
- **extended phased apertures** — evade the compact quadrupole directivity ceiling by using spatial phase across a large aperture;
- **higher multipoles or relativistic sources** — leave the leading compact nonrelativistic quadrupole approximation;
- **near-field coupling** — leaves the propagating one-way wave-zone channel;
- **nonlinear many-body response** — may require a response theorem beyond the linear bosonic realization.

A useful follow-up program is therefore not “increase Q,” but rather:

> What additional nonpassive or noncompact physical resource is required to beat the passive compact-quadrupole gravitational throughput ceiling?

---

## 9. Strongest defensible current claim

> For compact passive nonrelativistic linear bosonic source and receiver networks coupled by propagating quadrupolar linearized gravity, the frequency-integrated coherent transfer is bounded by the smaller endpoint quadrupole oscillator-strength resource and by the TT propagation singular value. In the narrowband wave zone this gives `Gamma_coh <= 25 G omega^2 min(I_A,I_B)/(12 c^3 R^2)` at the retained order, independent of endpoint Q, the number of passive internal modes, and compact quadrupole orientation.

This statement remains subject to independent adversarial audit and deeper prior-art collision checking before manuscript submission.
