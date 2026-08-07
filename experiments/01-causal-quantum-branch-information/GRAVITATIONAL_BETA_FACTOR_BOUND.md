# Gravitational Beta-Factor Bound

**Timestamp:** 2026-08-07 17:52 EDT  
**Status:** General linear-mode statement; useful for separating collective oscillator strength from source-mode matching.

## 1. Receiver coupling as a continuum vector

Let a receiver transition couple linearly to normalized graviton continuum labels $\lambda$ through amplitudes

$$
g_B(\lambda).
$$

Here $\lambda$ can include

- frequency;
- propagation direction;
- polarization;
- any other normalized wavepacket channel label.

At the receiver resonance, the total spontaneous gravitational linewidth is proportional to the squared norm of this coupling vector,

$$
\boxed{
\kappa_g
=2\pi\int d\lambda\,|g_B(\lambda)|^2
}
$$

within the usual Markov normalization.

Now let the incoming source branch-difference mode have normalized profile

$$
f_S(\lambda),
$$

with

$$
\int d\lambda\,|f_S(\lambda)|^2=1.
$$

The receiver coupling amplitude to that one source mode is

$$
g_\Delta
=\int d\lambda\,g_B(\lambda)f_S^*(\lambda).
$$

Define

$$
\boxed{
\kappa_\Delta
=2\pi|g_\Delta|^2.
}
$$

---

## 2. Cauchy-Schwarz bound

Cauchy-Schwarz gives

$$
|g_\Delta|^2
\le
\left(\int d\lambda\,|g_B(\lambda)|^2\right)
\left(\int d\lambda\,|f_S(\lambda)|^2\right).
$$

Since the source mode is normalized,

$$
\boxed{
\kappa_\Delta\le\kappa_g.
}
$$

Define the gravitational source-mode beta factor

$$
\boxed{
\beta_\Delta
\equiv
\frac{\kappa_\Delta}{\kappa_g}.
}
$$

Then

$$
\boxed{0\le\beta_\Delta\le1.}
$$

Equality occurs exactly when the receiver's normalized gravitational emission/absorption mode is proportional to the time-reversed source difference mode on the relevant support.

This is the clean abstract version of source-receiver mode matching.

---

## 3. Relation to the existing overlap notation

The project has written

$$
\kappa_\Delta
=\mathcal O_{SB}\kappa_g.
$$

The present derivation identifies

$$
\boxed{
\mathcal O_{SB}=\beta_\Delta
=\frac{|\langle g_B,f_S\rangle|^2}
{\|g_B\|^2}
}
$$

for a normalized source mode.

Thus tensor orientation, aperture/directivity, temporal/spectral mode shape, and polarization are all components of one normalized Hilbert-space overlap.

They can never produce

$$
\mathcal O_{SB}>1.
$$

---

## 4. What a distributed array can do

A coherent array changes the receiver coupling vector itself,

$$
g_B(\lambda)
\rightarrow
g_B^{(N)}(\lambda).
$$

There are two distinct benefits.

### A. Increase total gravitational oscillator strength

A passive collective bright mode can increase

$$
\|g_B^{(N)}\|^2
$$

and therefore increase the total

$$
\kappa_g^{(N)}.
$$

For $N$ identical subwavelength elements in a normalized symmetric single-excitation bright state, the familiar coherent scaling is generically

$$
\kappa_g^{(N)}\sim N\kappa_g^{(1)}
$$

rather than an unlimited $N^2$ single-excitation rate.

Higher Dicke manifolds or active/inverted states can display $N^2$ transition rates, but these are active resources and carry corresponding spontaneous-transition dynamics.

### B. Improve source-mode overlap/directivity

A spatially extended phased array can reshape the angular coupling pattern so that

$$
\beta_\Delta^{(N)}
=\frac{\kappa_\Delta^{(N)}}{\kappa_g^{(N)}}
$$

approaches unity for one selected incoming source mode.

This is a **directivity/mode-matching** improvement, not an additional oscillator-strength factor.

---

## 5. What an array cannot do

No linear array can obtain

$$
\kappa_\Delta>\kappa_g
$$

for a normalized incoming source mode.

Therefore one must not multiply a collective total-rate enhancement and a directional array gain as though they were independent unbounded factors. Once the full collective receiver mode is normalized, the correct decomposition is always

$$
\boxed{
\kappa_\Delta
=\beta_\Delta\kappa_g,
\qquad
0\le\beta_\Delta\le1.
}
$$

Any architecture must improve one or both of

1. total gravitational branching strength $\kappa_g/\kappa_{\rm tot}$;
2. mode overlap $\beta_\Delta$.

Neither can exceed unity as a branching fraction.

---

## 6. Internal loss of a passive bright mode

For $N$ identical receiver elements with independent local internal loss rate $\kappa_i$, define the normalized bright single-excitation mode

$$
C
=\frac1{\sqrt N}
\sum_{j=1}^N e^{-i\phi_j}c_j.
$$

Independent local damping gives

$$
\dot C\big|_{\rm int}
=-\frac{\kappa_i}{2}C+\text{normalized bright bath noise},
$$

so the bright mode's internal decay rate remains

$$
\boxed{\kappa_i}
$$

rather than $N\kappa_i$.

If the elements are subwavelength and gravitationally superradiant in the bright mode,

$$
\kappa_g^{(N)}\sim N\kappa_g^{(1)},
$$

so the gravitational branching ratio can improve approximately linearly with $N$.

This is not a loophole in the passive oscillator-strength bound: total mass/oscillator strength has also increased by $N$.

---

## 7. Large phased arrays

When the array size is comparable to or larger than the gravitational wavelength, cross terms in the **integrated** spontaneous rate need not all add coherently. The array can instead produce a narrow directional lobe.

Then

- total $\kappa_g$ may grow much more slowly than $N$;
- coupling density into the matched direction can be strongly enhanced;
- the lobe solid angle shrinks correspondingly;
- the integrated beta-factor bound remains
  $$
  \beta_\Delta\le1.
  $$

Thus directivity redistributes gravitational oscillator strength in mode space rather than creating it from nothing.

---

## 8. Consequence for Experiment 01

The receiver problem has a clean two-factor decomposition:

$$
\boxed{
\eta_Q
=\beta_{\rm prop}
\times
\beta_\Delta
\times
\frac{\kappa_g}{\kappa_{\rm tot}}
}
$$

where

- $\beta_{\rm prop}$ is free-space source-to-receiver propagation/access;
- $\beta_\Delta$ is normalized receiver/source mode matching;
- $\kappa_g/\kappa_{\rm tot}$ is the gravitational branching ratio of the receiver memory.

Depending on how the free-space mode is normalized, $\beta_{\rm prop}$ and $\beta_\Delta$ can be combined into the single source-to-receiver storage coefficient derived in `DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md`. The invariant statement is that useful coupling cannot exceed total gravitational coupling.

A distributed array can be valuable, but it does not invalidate the basic conclusion that **quantum reception requires both large gravitational oscillator strength and excellent source-mode matching**.

---

## 9. Strongest next question

The remaining major passive loophole is not ordinary array gain. It is whether a **relativistic field-theoretic collective receiver** can possess a gravitational branching ratio near unity without paying an equivalent KMS/vacuum-noise cost. That requires a QFT receiver model rather than the nonrelativistic quadrupole sum rule.