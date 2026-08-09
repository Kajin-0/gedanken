# Spectral Generalization

## 1. Why the single-mode theorem is not enough

The bound

```math
\Gamma_\kappa
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B})
```

closes the high-Q loophole for one source resonance and one receiver resonance. It is not yet architecture independent because a passive device may contain many resonances in parallel.

The next object must therefore bound the **total positive gravitational spectral weight available inside a finite operating band**.

---

## 2. Positive passive quadrupole spectral measure

Let a stationary passive nonrelativistic system have

```math
\rho=\sum_m p_m|m\rangle\langle m|,
\qquad
p_m\ge p_n\quad\text{when }E_m<E_n.
```

Let `Q_a`, `a=1,...,5`, be an orthonormal basis of symmetric trace-free mass-quadrupole components. Define positive transition frequencies

```math
\omega_{nm}=\frac{E_n-E_m}{\hbar}>0
```

and the positive passive quadrupole spectral measure

```math
\boxed{
d\mu_Q(\omega)
=
\sum_{m<n,a}
(p_m-p_n)
|Q^a_{mn}|^2
\delta(\omega-\omega_{nm})\,d\omega.
}
```

Passivity guarantees `d mu_Q >= 0`.

The energy-weighted sum rule inherited from V7 is

```math
\boxed{
\int_0^\infty \omega\,d\mu_Q(\omega)
=
\frac{10}{3}\hbar\langle I\rangle_\rho,
}
```

with

```math
I=\sum_a m_a r_a^2.
```

---

## 3. Band-limited gravitational spectral-weight theorem

The quadrupole graviton transition rate is

```math
\gamma_{nm}^{(g)}
=
\frac{2G\omega_{nm}^5}{5\hbar c^5}
Q_{ij}^{nm}Q_{ij}^{mn}.
```

Using the orthonormal STF basis, define the cumulative passive gravitational transition-rate weight below angular frequency `Omega` by

```math
\boxed{
K_g(\Omega)
\equiv
\frac{2G}{5\hbar c^5}
\int_0^\Omega \omega^5\,d\mu_Q(\omega).
}
```

Because `d mu_Q >= 0` and, for `0 <= omega <= Omega`,

```math
\omega^5\le\Omega^4\omega,
```

we obtain

```math
K_g(\Omega)
\le
\frac{2G\Omega^4}{5\hbar c^5}
\int_0^\Omega\omega\,d\mu_Q(\omega)
\le
\frac{2G\Omega^4}{5\hbar c^5}
\int_0^\infty\omega\,d\mu_Q(\omega).
```

Therefore

```math
\boxed{
K_g(\Omega)
\le
\frac{4G}{3c^5}
\langle I\rangle_\rho\,\Omega^4.
}
```

### Interpretation

This is a cumulative finite-band statement. It does **not** require assuming that the material spectrum literally terminates at `Omega`. It says that no matter how the passive quadrupole oscillator strength is distributed among arbitrarily many lines below `Omega`, their total gravitational transition-rate spectral weight is bounded by the inertia moment and the top of the selected band.

For a narrow band concentrated near `omega`, the statement reduces to the V7 narrowband linewidth ceiling

```math
\kappa_{g,\rm net}
\lesssim
\frac{4G}{3c^5}\langle I\rangle\omega^4.
```

Writing `I = M L^2` gives

```math
\frac{K_g(\Omega)}{\Omega}
\le
\frac23\mathcal C\left(\frac{\Omega L}{c}\right)^3,
```

with

```math
\mathcal C=\frac{2GM}{c^2L}.
```

Thus the compactness/velocity scaling survives the many-line generalization.

---

## 4. Independent parallel-resonance corollary

Suppose an end-to-end passive link decomposes into independent narrow resonant channels indexed by `n`. Let each channel satisfy the single-resonance theorem

```math
\Gamma_n
\le
\eta_n\min(\kappa_{g,A,n},\kappa_{g,B,n}),
\qquad
0\le\eta_n\le1.
```

Then

```math
\Gamma_{\rm tot}
\equiv\sum_n\Gamma_n
\le
\sum_n\min(\kappa_{g,A,n},\kappa_{g,B,n}).
```

For nonnegative sequences,

```math
\sum_n\min(a_n,b_n)
\le
\min\!\left(\sum_n a_n,\sum_n b_n\right).
```

Therefore

```math
\boxed{
\Gamma_{\rm tot}
\le
\min\!\left(
\sum_n\kappa_{g,A,n},
\sum_n\kappa_{g,B,n}
\right).
}
```

For ground-state passive endpoints, or more generally when the channel linewidth sums are identified with the positive net spectral weights entering linear response, the cumulative EWSR gives the candidate band-limited interface bound

```math
\boxed{
\Gamma_{\rm tot}(\Omega)
\le
\frac{4G\Omega^4}{3c^5}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

This is deliberately written **without** a propagation factor. Free-space propagation and tensor mode mismatch can only reduce an already passive end-to-end transfer, so the expression is an interface cut-set ceiling for the independent-channel class.

If every channel additionally obeys `eta_n <= eta_max`, then

```math
\boxed{
\Gamma_{\rm tot}(\Omega)
\le
\eta_{\max}
\frac{4G\Omega^4}{3c^5}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

The usefulness of this stronger form depends on obtaining a physically meaningful `eta_max` over the declared propagation band.

---

## 5. What has actually been proved here

The following pieces are algebraically controlled:

1. the cumulative EWSR-to-gravitational-weight inequality `K_g(Omega)`;
2. the sum-of-minima inequality for independent parallel channels;
3. the resulting many-line cut-set ceiling **if** the channel gravitational linewidths are the same positive spectral weights appearing in the passive response measure.

The last identification is automatic for simple ground-state normal modes but must be formulated carefully for a general interacting finite-temperature susceptibility.

---

## 6. Next step — susceptibility / scattering formulation

The architecture-independent target is to replace the explicit resonance index by matrix-valued quadrupole susceptibilities

```math
\chi_A^{ab}(\omega),
\qquad
\chi_B^{ab}(\omega),
```

with positive absorptive parts for passive systems, and to write the separated source-to-receiver transfer through a TT propagation operator

```math
G_{\rm TT}^{ab}(\mathbf R,\omega).
```

The desired structure is schematically

```math
\text{source response}
\;\longrightarrow\;
G_{\rm TT}
\;\longrightarrow\;
\text{receiver response},
```

with a frequency-dependent contraction whose singular values define the useful coherent channels.

The key research problem is then to prove a trace/singular-value inequality that converts the EWSR bounds on `Im chi_A` and `Im chi_B` into an integral bound on end-to-end coherent transmission.

---

## 7. Preferred broadband metric

To avoid arbitrary definitions of bandwidth, target

```math
\boxed{
\Gamma_{\rm coh}
=\frac{1}{2\pi}
\int_{\mathcal B}\tau(\omega)\,d\omega,
}
```

or, for multiple tensor channels,

```math
\Gamma_{\rm coh}
=\frac{1}{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]\,d\omega.
```

This has units of inverse time and is the gravitational analogue of an efficiency-bandwidth integral. Whether the trace or another singular-value functional is the correct operational quantity must be derived from the scattering normalization, not assumed.

---

## 8. Capacity mapping comes later

For a frequency-dependent pure-loss channel with transmissivity `tau(omega)`, established transducer theory defines continuous-time capacities by integrating the per-frequency capacity over `d omega / 2 pi`.

In particular, the unassisted one-way pure-loss capacity is zero whenever `tau <= 1/2`, whereas the two-way-assisted pure-loss capacity remains positive for every `tau > 0`. Therefore the physical response theorem should be independent of which capacity notion is later chosen.

In the weak-link limit, the two-way-assisted per-mode capacity obeys

```math
-\log_2(1-\tau)
=
\frac{\tau}{\ln2}+O(\tau^2),
```

so a rigorous bound on the integrated `tau(omega)` would immediately generate a weak-link entanglement-distribution-rate corollary.

That corollary is not yet claimed as a theorem because the general gravitational `tau(omega)` has not yet been derived.
