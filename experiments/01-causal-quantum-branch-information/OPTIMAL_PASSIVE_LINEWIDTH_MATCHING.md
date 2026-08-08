# Global Optimality of Passive Source–Receiver Linewidth Matching

**Date:** 2026-08-07  
**Status:** **EXACT PASSIVE OPTIMIZATION — MATCHED LINEWIDTHS MAXIMIZE CONSTANT-COUPLING STORAGE AT FIXED USEFUL RECEIVER FRACTION**

## 1. Purpose

The passive exponential source calculations often specialize to

$$
\kappa_A=\kappa_B.
$$

This is not merely an algebraic convenience.

For the natural normalized exponential source waveform and a passive receiver with time-independent damping, matched source and receiver linewidths are the **global optimum** at fixed useful receiver coupling fraction

$$
\boxed{
\beta_\Delta
\equiv
\frac{\kappa_\Delta}{\kappa_B}.
}
$$

The exact maximum is

$$
\boxed{
\tau_{\max}
=4e^{-2}\beta_\Delta.
}
$$

---

# 2. Exponential source and passive receiver

Let

$$
\boxed{
f_A(t)
=\sqrt{\kappa_A}e^{-\kappa_A t/2},
\qquad t\ge0.
}
$$

The receiver amplitude kernel is

$$
I(t)
=
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}f_A(s).
$$

For

$$
\kappa_A\ne\kappa_B,
$$

$$
\boxed{
I(t)
=
\frac{2\sqrt{\kappa_A}}
{\kappa_B-\kappa_A}
\left(
 e^{-\kappa_A t/2}
-e^{-\kappa_B t/2}
\right).
}
$$

The coherent transfer parameter is

$$
\boxed{
\tau(t)=\kappa_\Delta|I(t)|^2.
}
$$

---

# 3. Dimensionless linewidth ratio

Define

$$
\boxed{
r=\frac{\kappa_B}{\kappa_A}>0,}
$$

and

$$
x=\kappa_A t.
$$

Then

$$
\boxed{
\tau(x)
=
\frac{4\kappa_\Delta}{\kappa_A}
\frac{
\left(e^{-x/2}-e^{-rx/2}\right)^2
}{(r-1)^2}.
}
$$

For fixed useful receiver fraction

$$
\beta_\Delta=\kappa_\Delta/\kappa_B,
$$

$$
\kappa_\Delta
=\beta_\Delta r\kappa_A.
$$

Hence

$$
\boxed{
\tau(x)
=4\beta_\Delta r
\frac{
\left(e^{-x/2}-e^{-rx/2}\right)^2
}{(r-1)^2}.
}
$$

---

# 4. Exact optimal time for fixed $r$

Differentiate the amplitude difference:

$$
\frac{d}{dx}
\left(
 e^{-x/2}-e^{-rx/2}
\right)
=
-\frac12e^{-x/2}
+\frac r2e^{-rx/2}.
$$

The interior maximum satisfies

$$
\boxed{
r e^{-rx_*/2}
=e^{-x_*/2}.}
$$

Therefore

$$
\boxed{
 e^{-(r-1)x_*/2}=\frac1r,
}
$$

and for

$$
r\ne1,
$$

$$
\boxed{
x_*(r)
=\frac{2\ln r}{r-1}.}
$$

This is positive for every

$$
r>0,
\qquad r\ne1.
$$

The matched limit is

$$
\lim_{r\to1}x_*(r)=2.
$$

Thus

$$
\boxed{t_*\to2/\kappa_A}
$$

when the linewidths match.

---

# 5. Exact peak transfer for fixed $r$

At the optimum,

$$
 e^{-rx_*/2}
=\frac1r e^{-x_*/2}.
$$

Therefore

$$
 e^{-x_*/2}-e^{-rx_*/2}
=
\frac{r-1}{r}e^{-x_*/2}.
$$

Substituting gives

$$
\boxed{
\tau_{\max}(r)
=
4\beta_\Delta
\frac1r
\exp\left[
-\frac{2\ln r}{r-1}
\right].
}
$$

Equivalently,

$$
\boxed{
\tau_{\max}(r)
=
4\beta_\Delta
\frac1r
r^{-2/(r-1)}.
}
$$

Define

$$
\boxed{
F(r)
\equiv
\frac{\tau_{\max}(r)}{\beta_\Delta}
=
4r^{-1-2/(r-1)}.
}
$$

---

# 6. Global optimization over linewidth mismatch

Take the logarithm:

$$
\ln\frac{F(r)}4
=-\ln r
-\frac{2\ln r}{r-1}.
$$

Differentiate:

$$
\boxed{
\frac{d}{dr}\ln F(r)
=
-\frac{
 r^2-2r\ln r-1
}{
 r(r-1)^2
}.
}
$$

Write

$$
r=e^y.
$$

Then

$$
r^2-2r\ln r-1
=2r(\sinh y-y).
$$

For

$$
y>0,
$$

$$
\sinh y>y,
$$

while for

$$
y<0,
$$

$$
\sinh y<y.
$$

Therefore

$$
\frac{dF}{dr}>0
\qquad(0<r<1),
$$

and

$$
\frac{dF}{dr}<0
\qquad(r>1).
$$

The unique global maximum is

$$
\boxed{r=1.}
$$

Hence

$$
\boxed{
\kappa_B=\kappa_A
}
$$

is globally optimal.

---

# 7. Matched maximum

Taking the limit

$$
r\to1,
$$

$$
\boxed{
F(1)=4e^{-2}.}
$$

Thus

$$
\boxed{
\tau_{\max}^{\rm passive}
=4e^{-2}\beta_\Delta
=4e^{-2}
\frac{\kappa_\Delta}{\kappa_B}.
}
$$

Numerically,

$$
\boxed{
4e^{-2}
\simeq0.5413411329.
}
$$

This is the largest peak storage obtainable from the natural exponentially decaying source waveform using a passive receiver with constant coupling and a fixed useful coupling fraction.

---

# 8. Physical interpretation

If

$$
\kappa_B\gg\kappa_A,
$$

the receiver forgets amplitude faster than the source supplies it.

If

$$
\kappa_B\ll\kappa_A,
$$

the source pulse passes before the receiver can accumulate it efficiently.

The exact optimum occurs when the two exponential time scales coincide.

The remaining factor

$$
4e^{-2}<1
$$

is the penalty for driving a passive cavity/oscillator with its **natural decaying exponential** rather than the time-reversed rising exponential that would achieve unit loading in an ideal single-port system.

---

# 9. Relation to the waveform-optimized front

The old waveform-optimized causal envelope effectively chose a different incident waveform to maximize loading at each target time.

The present result concerns one fixed physical source waveform:

$$
f_A(t)=\sqrt{\kappa_A}e^{-\kappa_A t/2}.
$$

Even after optimizing the receiver linewidth, its peak constant-coupling capture is only

$$
4e^{-2}\beta_\Delta.
$$

This gives another precise way to distinguish

- waveform-optimized protocol bounds; from
- source-fixed physical trajectories.

---

# 10. End-to-end source branching

For vacuum source loss, the complete passive source→receiver coherent transfer is

$$
\tau_{A\to B}
=\eta_g\tau,
$$

with

$$
\eta_g=\kappa_{g,A}/\kappa_A.
$$

Therefore the globally optimized passive end-to-end maximum at fixed

$$
\eta_g
$$

and

$$
\beta_\Delta
$$

is

$$
\boxed{
\tau_{A\to B}^{\max}
=4e^{-2}\eta_g\beta_\Delta.
}
$$

For a stationary thermal receiver, a necessary and sufficient condition for a non-EB interval in this optimized passive family is

$$
\boxed{
 n_{\rm th,B}
<4e^{-2}\eta_g\beta_\Delta
}
$$

in the vacuum-source-loss model.

---

# 11. Geometric specialization

For the gravitational receiver,

$$
\boxed{
\beta_\Delta
=\frac{\kappa_\Delta}{\kappa_B}
=\eta_{\rm store}
\frac{\kappa_{g,B}}{\kappa_B}.
}
$$

Hence

$$
\boxed{
\tau_{A\to B}^{\max}
=4e^{-2}
\left(
\frac{\kappa_{g,A}}{\kappa_A}
\right)
\eta_{\rm store}
\left(
\frac{\kappa_{g,B}}{\kappa_B}
\right).
}
$$

At leading compact-source wave-zone order,

$$
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}.
$$

Therefore

$$
\boxed{
\tau_{A\to B}^{\max}
=
\frac{25e^{-2}}{4}
\frac{\mathcal O}{(kR)^2}
\left(
\frac{\kappa_{g,A}}{\kappa_A}
\right)
\left(
\frac{\kappa_{g,B}}{\kappa_B}
\right).
}
$$

This factorization cleanly separates

1. source gravitational branching;
2. free-space mode overlap;
3. receiver gravitational branching;
4. the unavoidable $4e^{-2}$ passive temporal-mode penalty.

---

# 12. Strongest passive no-free-lunch formula

Define

$$
\boxed{
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A},
\qquad
\beta_{g,B}=\frac{\kappa_{g,B}}{\kappa_B}.
}
$$

Then the best possible constant-coupling passive exponential-link transmissivity in the aligned wave-zone model is

$$
\boxed{
\tau_{\rm passive}^{\max}
=4e^{-2}
\beta_{g,A}
\beta_{g,B}
\eta_{\rm store}.
}
$$

Thus every non-gravitational source or receiver loss reduces the link multiplicatively.

For ideal source and receiver branching,

$$
\beta_{g,A}=\beta_{g,B}=1,
$$

$$
\boxed{
\tau_{\rm passive}^{\max}
=4e^{-2}\eta_{\rm store}.
}
$$

This is the cleanest passive end-to-end ceiling currently available in the repository.

---

# 13. Scope

The optimization is over

- constant receiver linewidth $\kappa_B$;
- fixed normalized exponential source waveform generated by free source decay;
- fixed useful receiver fraction $\beta_\Delta$.

It does not include

- time-dependent receiver coupling;
- active coherent capture;
- shaped time-reversal loading;
- non-Markov receiver memory;
- multimode adaptive protocols.

Those can exceed the $4e^{-2}$ temporal factor but correspond to a different receiver architecture.

---

# 14. Adversarial verdict

The matched-linewidth assumption used repeatedly in the passive source calculations is now justified by an exact global optimization.

For the natural decaying exponential source,

$$
\boxed{
\kappa_A=\kappa_B
}
$$

is the unique global optimum at fixed useful receiver branching fraction.

The resulting passive ceiling

$$
\boxed{
4e^{-2}
\beta_{g,A}
\beta_{g,B}
\eta_{\rm store}
}
$$

provides a compact end-to-end benchmark against which any active or shaped protocol must be compared.
