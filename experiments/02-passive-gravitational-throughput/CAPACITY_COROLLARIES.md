# Pure-Loss Capacity Corollaries

## 1. Scope

The passive-network theorem bounds the integrated coherent transfer

```math
\Gamma_{\rm coh}
=
\frac1{2\pi}
\int d\omega\,
\operatorname{Tr}[T^\dagger(\omega)T(\omega)].
```

This quantity is **not** itself a quantum capacity.

For a stationary pure-loss bosonic channel, however, the singular values of `T(omega)` define independent pure-loss eigenchannels. This allows established per-frequency capacity formulas to convert the physical response bound into rigorous capacity corollaries.

The statements below assume all unobserved ports are in vacuum. Thermal or active noise requires separate channel bounds.

---

## 2. Transmission eigenvalues

Let

```math
\tau_n(\omega)
```

be the eigenvalues of

```math
T^\dagger(\omega)T(\omega).
```

Then

```math
0\le\tau_n(\omega)\le1
```

and

```math
\sum_n\tau_n(\omega)
=
\operatorname{Tr}[T^\dagger T].
```

Because the source and receiver passive scattering subblocks are contractions and the propagation operator satisfies

```math
\|P_g(\omega)\|_{\rm op}^2\le\eta_{\max},
```

the full transfer obeys

```math
\boxed{
\tau_n(\omega)\le\eta_{\max}
}
```

for every frequency and transmission eigenchannel.

---

## 3. Unassisted one-way quantum capacity

For a pure-loss bosonic eigenchannel with transmissivity `tau`, the unassisted quantum capacity per mode is

```math
q_1(\tau)
=
\max\!\left\{
\log_2\frac{\tau}{1-\tau},0
\right\}.
```

Therefore, if

```math
\boxed{
\eta_{\max}\le\frac12,
}
```

then every transmission eigenchannel satisfies `tau_n <= 1/2`, and hence

```math
\boxed{
Q_1=0.
}
```

This is a propagation-level zero-capacity corollary for the stationary pure-loss model. It does **not** mean that no reference–receiver entanglement can survive a single use; pure-loss channels below `1/2` can remain non-entanglement-breaking while having zero unassisted asymptotic quantum capacity.

---

## 4. Two-way-assisted capacity

For pure loss, the two-way-assisted quantum/entanglement-distribution capacity per eigenchannel is

```math
q_2(\tau)
=-\log_2(1-\tau).
```

For `0 <= tau <= eta_max < 1`, use

```math
-\ln(1-\tau)
=\int_0^\tau\frac{dx}{1-x}
\le
\frac{\tau}{1-\eta_{\max}}.
```

Thus

```math
\boxed{
q_2(\tau)
\le
\frac{\tau}
{\ln2\,(1-\eta_{\max})}.
}
```

Summing transmission eigenchannels and integrating frequency gives

```math
Q_2
\le
\frac{1}{\ln2\,(1-\eta_{\max})}
\frac1{2\pi}
\int d\omega\sum_n\tau_n(\omega).
```

Therefore

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
}
```

Applying the passive-network cut-set theorem,

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

This is a genuine operational capacity upper bound within the stationary pure-loss passive-network model.

---

## 5. Weak-propagation limit

When

```math
\eta_{\max}\ll1,
```

the prefactor becomes

```math
\frac{1}{1-\eta_{\max}}
=1+O(\eta_{\max}).
```

Hence

```math
\boxed{
Q_2
\lesssim
\frac{\Gamma_{\rm coh}}{\ln2}
}
```

up to a controlled relative correction of order `eta_max`.

The lower Taylor inequality

```math
-\ln(1-\tau)\ge\tau
```

also shows that, for a *known actual transfer function*,

```math
Q_2\ge\frac{\Gamma_{\rm coh}}{\ln2}.
```

Thus `Gamma_coh / ln 2` is the leading weak-link two-way entanglement-distribution rate, while the passive theorem supplies its architecture-level upper envelope.

---

## 6. Material-response corollary

For passive linear matter networks whose total gravitational coupling trace below operating ceiling `Omega` is controlled by the cumulative quadrupole sum rule,

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4,
```

the pure-loss two-way-assisted rate obeys

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

This is the current strongest candidate **gravitational quantum throughput bound** in the project, with a clearly defined operational quantity.

Its material generality is exactly the same as the material-response bridge in `PASSIVE_NETWORK_CUTSET_THEOREM.md`: passive linear Markov matter networks whose gravitational coupling trace resolves the positive quadrupole spectral weight entering the EWSR.

---

## 7. Aligned wave-zone specialization

For a single aligned plus-quadrupole propagation channel with

```math
\eta_{\max}
=\frac{25\mathcal O}{16(kR)^2}
```

inside the declared wave-zone regime, the capacity corollary becomes explicit after inserting the endpoint passive-matter spectral bound.

At `kR=10` and `O=1`,

```math
\eta_{\max}=0.015625<1/2,
```

so the stationary pure-loss **unassisted** quantum capacity is zero, while the two-way-assisted rate remains nonzero but is bounded by the gravitational spectral resource above.

Do not confuse this zero one-way capacity statement with the V7 result that finite reference–receiver negativity survives for every nonzero pure-loss transmissivity.

---

## 8. What changes with noise

Thermal occupation, active gain, pump noise, dephasing, or non-Gaussian noise changes the channel class. The pure-loss formulas above no longer apply directly.

The physical passive-network EBP/cut-set theorem remains the primary result because it constrains coherent transmission before a particular information metric is chosen. Noisy capacity bounds should be developed only after a specific gravitational noise model is declared.

---

## 9. Claim discipline

Allowed statement:

> In the stationary vacuum pure-loss realization, the passive gravitational response bound implies an explicit upper bound on continuous-time two-way-assisted quantum/entanglement-distribution capacity; if the propagation singular value squared never exceeds one half, the unassisted quantum capacity is identically zero.

Not yet allowed:

- a universal quantum-capacity bound for arbitrary gravitational noise;
- a claim that gravity itself has zero quantum capacity;
- a claim that zero one-way capacity means no entanglement transmission in a single use;
- a claim that the result applies to active, relativistic, or nonlinear transducers.
