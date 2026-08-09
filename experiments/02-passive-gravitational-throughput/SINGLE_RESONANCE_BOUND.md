# Single-Resonance Linewidth-Weighted Bound

## 1. Setup

Consider a source mode `A` and receiver memory mode `B` in the same weak one-way narrowband Markov class used by V7. Let

```math
\kappa_A\ge\kappa_{g,A}>0,
\qquad
\kappa_B\ge\kappa_{g,B}>0
```

be total and gravitational linewidths, respectively. Let the selected gravitational propagation/capture fraction satisfy

```math
0\le\eta_{\rm prop}\le1,
```

and let the normalized temporal loading obey

```math
0\le\mathcal T_f(t)\le1.
```

The source-to-memory coherent transfer fraction is

```math
\tau_c(t)
=
\eta_{\rm prop}
\frac{\kappa_{g,A}}{\kappa_A}
\frac{\kappa_{g,B}}{\kappa_B}
\mathcal T_f(t).
```

Define

```math
\tau_*\equiv\sup_t\tau_c(t)
```

and the purely linewidth-defined scale

```math
B_\kappa\equiv\min(\kappa_A,\kappa_B).
```

Then define

```math
\boxed{
\Gamma_\kappa\equiv B_\kappa\tau_*.
}
```

`Gamma_kappa` has units of inverse time. At this stage it is a linewidth-weighted coherent-transfer scale, not a Shannon or quantum capacity.

---

## 2. Theorem

### Proposition — passive-port speed–efficiency no-free-lunch bound

For any positive linewidths satisfying

```math
0<\kappa_{g,A}\le\kappa_A,
\qquad
0<\kappa_{g,B}\le\kappa_B,
```

and any `0 <= T_f <= 1`,

```math
\boxed{
\Gamma_\kappa
\le
\eta_{\rm prop}
\min(\kappa_{g,A},\kappa_{g,B}).
}
```

### Proof

Since `T_f <= 1`,

```math
\Gamma_\kappa
\le
\eta_{\rm prop}
\min(\kappa_A,\kappa_B)
\frac{\kappa_{g,A}\kappa_{g,B}}
{\kappa_A\kappa_B}.
```

Because `min(kappa_A,kappa_B) <= kappa_A`,

```math
\min(\kappa_A,\kappa_B)
\frac{\kappa_{g,A}\kappa_{g,B}}
{\kappa_A\kappa_B}
\le
\kappa_{g,A}
\frac{\kappa_{g,B}}{\kappa_B}
\le
\kappa_{g,A}.
```

Likewise, using `min(kappa_A,kappa_B) <= kappa_B`,

```math
\min(\kappa_A,\kappa_B)
\frac{\kappa_{g,A}\kappa_{g,B}}
{\kappa_A\kappa_B}
\le
\kappa_{g,B}
\frac{\kappa_{g,A}}{\kappa_A}
\le
\kappa_{g,B}.
```

Therefore the same quantity is bounded by both gravitational linewidths, proving

```math
\Gamma_\kappa
\le
\eta_{\rm prop}
\min(\kappa_{g,A},\kappa_{g,B}).
```

QED.

---

## 3. Exact piecewise form before the final relaxation

The proof contains a useful sharper expression. If

```math
\kappa_A\le\kappa_B,
```

then

```math
\Gamma_\kappa
\le
\eta_{\rm prop}
\kappa_{g,A}
\frac{\kappa_{g,B}}{\kappa_B}
=
\eta_{\rm prop}\kappa_{g,A}\beta_{g,B}.
```

If

```math
\kappa_B\le\kappa_A,
```

then

```math
\Gamma_\kappa
\le
\eta_{\rm prop}
\kappa_{g,B}
\frac{\kappa_{g,A}}{\kappa_A}
=
\eta_{\rm prop}\kappa_{g,B}\beta_{g,A}.
```

Thus making one endpoint fast does not remove the other endpoint's gravitational branching penalty.

---

## 4. Tightness

The inequality is algebraically tight with respect to the linewidth/branching variables.

Take the ideal passive limit with no nongravitational damping:

```math
\kappa_A=\kappa_{g,A},
\qquad
\kappa_B=\kappa_{g,B}.
```

Then

```math
\beta_{g,A}=\beta_{g,B}=1
```

and

```math
B_\kappa=\min(\kappa_{g,A},\kappa_{g,B}).
```

If temporal loading approaches unity, then

```math
\Gamma_\kappa
\to
\eta_{\rm prop}
\min(\kappa_{g,A},\kappa_{g,B}).
```

Hence arbitrarily high gravitational branching does not evade the bound; it reaches the bound by making the usable linewidth gravitationally slow.

Temporal saturation is a separate waveform-realizability issue. The inequality itself does not assume it.

---

## 5. Passive nonrelativistic matter corollary

For each endpoint in the passive compact nonrelativistic class, V7 established for a selected narrow band

```math
\kappa_{g,j}
\lesssim
\frac23\omega\mathcal C_j\beta_j^3,
```

where

```math
\mathcal C_j=\frac{2GM_j}{c^2L_j},
\qquad
\beta_j=\frac{\omega L_j}{c}.
```

For matched source and receiver carrier frequency,

```math
\boxed{
\Gamma_\kappa
\lesssim
\frac23\eta_{\rm prop}\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

For the aligned plus-quadrupole wave-zone specialization,

```math
\eta_{\rm prop}
=
\frac{25\mathcal O}{16(kR)^2},
```

so

```math
\boxed{
\Gamma_\kappa
\lesssim
\frac{25\mathcal O}{24(kR)^2}
\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

This is the first candidate gravity-specific speed–efficiency bound.

---

## 6. Benchmark inherited from V7

For

```math
\kappa_g\simeq6.87\times10^{-26}\;\mathrm{s}^{-1},
\qquad
\eta_{\rm prop}=0.015625,
```

the gravitationally limited linewidth-weighted scale is

```math
\eta_{\rm prop}\kappa_g
\simeq1.0734\times10^{-27}\;\mathrm{s}^{-1}.
```

Its inverse is

```math
\simeq9.32\times10^{26}\;\mathrm{s}
\simeq2.95\times10^{19}\;\mathrm{yr}.
```

Do **not** call this “one qubit every `2.95e19 yr`.” It is an inverse coherent-transfer rate scale. An information-rate interpretation requires a defined continuous-time channel capacity or entanglement-rate functional.

---

## 7. What this theorem does and does not establish

It establishes, inside the two-resonator V7 link class, that the usual high-Q escape route cannot make both coherent transfer and linewidth arbitrarily favorable. The intrinsic gravitational linewidth remains as the limiting rate scale.

It does **not** yet establish:

- an architecture-independent many-mode bound;
- a frequency-integrated efficiency-bandwidth theorem;
- a bound on one-way quantum capacity;
- a bound for active/inverted or relativistic matter;
- a universal propagation coefficient.

Those are the next research steps.
