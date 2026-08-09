# Exact Two-Port Spectral Throughput Bound

## 1. Motivation

The provisional quantity `Gamma_kappa = min(kappa_A,kappa_B) tau_*` closes the high-Q loophole but still contains a bandwidth convention.

A stronger formulation is to add explicit local input/output ports and derive the continuous-frequency transduction efficiency. The resulting efficiency-bandwidth integral is unambiguous:

```math
\Gamma_{\rm EBP}
\equiv
\frac{1}{2\pi}
\int_{-\infty}^{\infty}
\tau(\Omega)\,d\Omega.
```

This is the natural quantity to compare with ordinary quantum-transducer efficiency-bandwidth products. It has units of inverse time.

---

## 2. Minimal cascaded model

Let source resonator `A` have

```math
\kappa_A
=
\kappa_{\rm in}
+\kappa_{g,A}
+\kappa_{i,A},
```

where

- `kappa_in` is the local signal-input coupling;
- `kappa_g,A` is the gravitational radiative coupling;
- `kappa_i,A` is other passive loss.

Let receiver resonator `B` have

```math
\kappa_B
=
\kappa_{g,B}
+\kappa_{\rm out}
+\kappa_{i,B},
```

where `kappa_out` is the useful local output/readout coupling.

Assume weak one-way propagation through a selected gravitational channel with amplitude transmissivity `sqrt(eta_prop)` and negligible reciprocal feedback at the retained order.

Using the standard resonator susceptibilities

```math
\chi_A(\Omega)
=
\frac{1}{\kappa_A/2-i\Omega},
\qquad
\chi_B(\Omega)
=
\frac{1}{\kappa_B/2-i\Omega},
```

the source-input to receiver-output scattering amplitude is

```math
\boxed{
S_{BA}(\Omega)
=
\sqrt{
\eta_{\rm prop}
\kappa_{\rm in}
\kappa_{g,A}
\kappa_{g,B}
\kappa_{\rm out}}
\;\chi_A(\Omega)\chi_B(\Omega)
\,e^{i\phi(\Omega)}.
}
```

The propagation phase drops out of the one-way power/coherent-transfer efficiency,

```math
\boxed{
\tau(\Omega)
=
\frac{
\eta_{\rm prop}
\kappa_{\rm in}
\kappa_{g,A}
\kappa_{g,B}
\kappa_{\rm out}
}
{
[\Omega^2+(\kappa_A/2)^2]
[\Omega^2+(\kappa_B/2)^2]
}.
}
```

This model is a stationary continuous-input extension of the V7 source/memory interface bookkeeping. It is not the same protocol as one-shot local preparation, but it is the appropriate object for an efficiency-bandwidth theorem.

---

## 3. Exact efficiency-bandwidth integral

Use

```math
\int_{-\infty}^{\infty}
\frac{d\Omega}
{(\Omega^2+a^2)(\Omega^2+b^2)}
=
\frac{\pi}{ab(a+b)}
```

for positive `a,b`. With

```math
a=\kappa_A/2,
\qquad
b=\kappa_B/2,
```

we obtain

```math
\boxed{
\Gamma_{\rm EBP}
=
\frac{
4\eta_{\rm prop}
\kappa_{\rm in}
\kappa_{g,A}
\kappa_{g,B}
\kappa_{\rm out}
}
{
\kappa_A\kappa_B(\kappa_A+\kappa_B)
}.
}
```

No FWHM convention or factor-of-`2 pi` ambiguity remains.

---

## 4. Theorem

### Proposition — two-port passive gravitational EBP ceiling

For

```math
\kappa_A
\ge
\kappa_{\rm in}+\kappa_{g,A},
\qquad
\kappa_B
\ge
\kappa_{g,B}+\kappa_{\rm out},
```

with all rates nonnegative,

```math
\boxed{
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}
\min(\kappa_{g,A},\kappa_{g,B}).
}
```

### Proof — source-side bound

Divide the exact integral by `eta_prop kappa_g,A`:

```math
\frac{\Gamma_{\rm EBP}}
{\eta_{\rm prop}\kappa_{g,A}}
=
\frac{
4\kappa_{\rm in}\kappa_{g,B}\kappa_{\rm out}
}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}.
```

Since

```math
4\kappa_{g,B}\kappa_{\rm out}
\le
(\kappa_{g,B}+\kappa_{\rm out})^2
\le
\kappa_B^2
```

and `kappa_in <= kappa_A`,

```math
4\kappa_{\rm in}\kappa_{g,B}\kappa_{\rm out}
\le
\kappa_A\kappa_B^2.
```

Therefore

```math
\frac{\Gamma_{\rm EBP}}
{\eta_{\rm prop}\kappa_{g,A}}
\le
\frac{\kappa_B}{\kappa_A+\kappa_B}
\le1.
```

Hence

```math
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}\kappa_{g,A}.
```

### Proof — receiver-side bound

Similarly,

```math
4\kappa_{\rm in}\kappa_{g,A}
\le
(\kappa_{\rm in}+\kappa_{g,A})^2
\le
\kappa_A^2,
```

and `kappa_out <= kappa_B`, so

```math
\frac{\Gamma_{\rm EBP}}
{\eta_{\rm prop}\kappa_{g,B}}
\le
\frac{\kappa_A}{\kappa_A+\kappa_B}
\le1.
```

Thus

```math
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}\kappa_{g,B}.
```

Combining the two inequalities proves the proposition.

QED.

---

## 5. Why this is stronger than `B_kappa tau`

The bound is now attached to an actual continuous-frequency scattering channel:

```math
\Gamma_{\rm EBP}
=\frac{1}{2\pi}\int\tau(\Omega)d\Omega.
```

The high-Q tradeoff appears automatically. Narrowing the resonators can raise on-resonance conversion, but it narrows the Lorentzian area. Broadening them increases spectral width but reduces interface matching to the intrinsically weak gravitational port.

The integrated area cannot exceed the slower gravitational interface rate times the propagation fraction.

---

## 6. Symmetric endpoint optimum

For a useful reference case, take

```math
\kappa_{g,A}=\kappa_{g,B}\equiv\kappa_g,
```

no internal loss, and symmetric external couplings

```math
\kappa_{\rm in}=\kappa_{\rm out}=x\kappa_g.
```

Then

```math
\Gamma_{\rm EBP}
=
\eta_{\rm prop}\kappa_g
\frac{2x^2}{(1+x)^3}.
```

Differentiation gives

```math
\frac{d}{dx}
\frac{2x^2}{(1+x)^3}=0
\quad\Longrightarrow\quad
x=2.
```

Thus the efficiency-bandwidth optimum is **overcoupled**, not critically coupled:

```math
\boxed{
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
}
```

with

```math
\boxed{
\Gamma_{\rm EBP}^{\rm sym,max}
=
\frac{8}{27}
\eta_{\rm prop}\kappa_g.
}
```

This is an important distinction:

- critical coupling maximizes peak interface conversion;
- overcoupling by a factor of two maximizes the **integrated efficiency-bandwidth area** in the symmetric two-resonator model.

---

## 7. Sharpness of the universal coefficient

The coefficient `1` in

```math
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B})
```

cannot be reduced uniformly over all gravitational linewidth ratios.

When one gravitational interface is parametrically slower than the other, the fast endpoint can be broadened while the slow endpoint remains near its optimal matching condition. The optimized EBP approaches

```math
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B})
```

in the extreme linewidth-asymmetry limit.

For comparable endpoints the tighter optimum is below the cut-set ceiling; the symmetric value is `8/27` of it.

A closed-form optimum for arbitrary linewidth ratio is a useful but nonessential next calculation.

---

## 8. Passive-matter corollary

If each gravitational linewidth obeys the passive narrowband sum-rule ceiling

```math
\kappa_{g,j}
\lesssim
\frac23\omega\mathcal C_j\beta_j^3,
```

then

```math
\boxed{
\Gamma_{\rm EBP}
\lesssim
\frac23\eta_{\rm prop}\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

For the aligned plus-quadrupole wave-zone propagation channel,

```math
\eta_{\rm prop}
=\frac{25\mathcal O}{16(kR)^2},
```

so

```math
\boxed{
\Gamma_{\rm EBP}
\lesssim
\frac{25\mathcal O}{24(kR)^2}
\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

This is now a genuine efficiency-bandwidth integral bound for the minimal two-port gravitational transducer, not merely a product of peak efficiency with a chosen bandwidth.

---

## 9. Information-theory relation

For this pure-loss stationary model, the frequency-dependent transmissivity `tau(Omega)` can be inserted directly into established continuous-time transducer-capacity formulas.

The EBP itself is not equal to one-way quantum capacity. In the weak-link regime, however, the two-way-assisted pure-loss capacity density satisfies

```math
q_2(\Omega)
=-\log_2[1-\tau(\Omega)]
=
\frac{\tau(\Omega)}{\ln2}
+O(\tau^2).
```

Therefore

```math
Q_2
=
\frac{1}{2\pi}
\int q_2(\Omega)d\Omega
=
\frac{\Gamma_{\rm EBP}}{\ln2}
+O\!\left(\int\tau^2d\Omega\right).
```

A controlled bound on the quadratic remainder would convert the physical EBP theorem into a weak-link two-way entanglement-distribution-rate theorem.

---

## 10. Remaining scope

This theorem still assumes:

- two single-pole passive resonators;
- one selected one-way gravitational propagation channel;
- linear time-invariant Markov dynamics;
- no active gain;
- no reciprocal multiple-scattering correction at leading order.

The next task is to prove that an arbitrary passive susceptibility network obeys an analogous integrated cut-set bound whose endpoint resources are controlled by the cumulative quadrupole EWSR.
