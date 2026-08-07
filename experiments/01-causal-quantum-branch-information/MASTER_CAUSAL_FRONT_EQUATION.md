# Master Causal Quantum-Reception Front

**Timestamp:** 2026-08-07 18:15 EDT  
**Status:** Closed-form wave-zone result for the aligned resonant linearized-gravity + stationary phase-insensitive Gaussian receiver model. This is the current central quantitative prediction of Experiment 01.

## 1. Ingredients

The result combines four independently derived pieces.

### A. Retarded propagation

No source-controlled signal reaches the receiver before

$$
t=R/c.
$$

### B. Far-zone gravitational storage coefficient

For aligned plus-type source and receiver quadrupoles,

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2},
}
$$

where

$$
k=\omega/c
$$

and $\mathcal O\le1$ collects tensor/polarization/temporal mode mismatch.

Therefore the useful source branch-mode loading rate is

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g,
}
$$

where $\kappa_g$ is the receiver's intrinsic graviton linewidth.

### C. Stationary receiver noise

Let

$$
\boxed{
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a
}
$$

be the thermal occupation-injection rate from uncontrolled receiver ports, and let

$$
\kappa_{\rm tot}
$$

be the receiver's full distance-independent linewidth, including gravitational vacuum damping and ordinary losses.

### D. Exact binary coherent certification law

For gravitational branch-mode coherent-state distance $N_\Delta$, define the matched exact witness margin

$$
\Lambda
=\ln\frac{|z_v|^2}{p_0p_v}.
$$

A target finite margin $\Lambda_{\rm req}>0$ is reached optimally when

$$
\kappa_\Delta
(1-e^{-\kappa_{\rm tot}\Delta t})
=\Gamma_{\rm th}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right),
$$

where

$$
\Delta t=t-R/c.
$$

---

## 2. Master finite-certification front

Substitute the gravitational loading rate into the exact receiver result.

The earliest possible source-to-receiver certification time is

$$
\boxed{
T_\Lambda^{\min}(R)
=
\frac Rc
-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right)
\right].
}
$$

This is the current **master causal quantum-reception front** for the wave-zone resonant Gaussian model.

It is valid when the logarithm argument lies strictly between zero and one.

---

## 3. Existence condition

A finite certification front exists iff

$$
\boxed{
\frac{25\mathcal O\kappa_g}
{16(kR)^2\Gamma_{\rm th}}
>
1+\frac{\Lambda_{\rm req}}{N_\Delta}.
}
$$

Define the dimensionless local gravitational quantum-reception ratio

$$
\boxed{
\mathfrak Q_G(R)
\equiv
\frac{25\mathcal O\kappa_g}
{16(kR)^2\Gamma_{\rm th}}.
}
$$

Then

$$
\boxed{
\text{finite certificate exists}
\iff
\mathfrak Q_G(R)
>
1+\frac{\Lambda_{\rm req}}{N_\Delta}.
}
$$

This separates three physical resources:

- **receiver channel quality:** $\mathfrak Q_G$;
- **source branch strength:** $N_\Delta$;
- **required experimental confidence/margin:** $\Lambda_{\rm req}$.

---

## 4. Bare NPT/capability front

Set

$$
\Lambda_{\rm req}=0.
$$

Then

$$
\boxed{
\mathfrak Q_G(R)>1
}
$$

is exactly the receiver non-entanglement-breaking condition for the binary coherent gravitational branch mode.

The earliest NPT/capability front is

$$
\boxed{
T_{\rm cap}(R)
=T_{\rm NPT}^{\min}(R)
=
\frac Rc
-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
\right].
}
$$

Within the covered Gaussian receiver family, every nontrivial finite binary coherent source encoding is front faithful, so the channel-capability and source-cat NPT fronts coincide.

---

## 5. Maximum thermal quantum range

The mathematical NPT front exists only while

$$
\mathfrak Q_G(R)>1.
$$

Thus

$$
\boxed{
R<R_Q
=
\frac{5}{4k}
\sqrt{
\frac{\mathcal O\kappa_g}
{\Gamma_{\rm th}}
}.
}
$$

For a finite witness requirement,

$$
\boxed{
R<R_\Lambda
=
\frac{R_Q}
{\sqrt{1+\Lambda_{\rm req}/N_\Delta}}.
}
$$

Therefore

$$
\boxed{
R_\Lambda<R_Q
}
$$

for every finite nonzero certification margin.

The classical gravitational wave continues beyond these radii; these are receiver quantum-capability/certification limits, not propagation limits.

---

## 6. Source branch strength in gravitational variables

For a conserved nonrelativistic source quadrupole difference,

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

For the narrow-band plus-type branch motion

$$
\Delta Q_{xx}
=q_0f(t)\cos\omega_0t,
$$

$$
\Delta Q_{yy}
=-\Delta Q_{xx},
$$

$$
\boxed{
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}
{5\hbar c^5},
\qquad
T_f=\int dt\,|f(t)|^2.
}
$$

The finite-certification front can therefore be written entirely in terms of a physical source trajectory and receiver parameters.

---

## 7. Receiver graviton linewidth

For a plus-type receiver quadrupole transition,

$$
\boxed{
\kappa_g
=\frac{4G\omega^5|q_B|^2}
{5\hbar c^5}.
}
$$

More generally,

$$
\boxed{
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

Thus the master front can be expressed entirely in source and receiver quadrupole matrix elements without an abstract gravitational coupling constant.

---

## 8. Fully quadrupolar form

Using the general receiver linewidth,

$$
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
=
\frac{8\hbar c^5(kR)^2\Gamma_{\rm th}}
{5\mathcal O G\omega^5Q_{ij}^{10}Q_{ij}^{01}}.
$$

Since

$$
kR=\omega R/c,
$$

this becomes

$$
\boxed{
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
=
\frac{8\hbar c^3R^2\Gamma_{\rm th}}
{5\mathcal O G\omega^3Q_{ij}^{10}Q_{ij}^{01}}.
}
$$

Hence

$$
\boxed{
T_\Lambda^{\min}(R)
=
\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{8\hbar c^3R^2\Gamma_{\rm th}}
{5\mathcal O G\omega^3Q_{ij}^{10}Q_{ij}^{01}}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right)
\right].
}
$$

This form displays the physical scaling directly:

$$
\boxed{
\text{quantum-build penalty}
\propto
\frac{R^2\Gamma_{\rm th}}
{\omega^3|Q_B|^2}.
}
$$

---

## 9. Near-capability asymptotic

Define

$$
\epsilon_Q(R)
=1-
\frac{1+\Lambda_{\rm req}/N_\Delta}
{\mathfrak Q_G(R)}.
$$

Then

$$
\boxed{
T_\Lambda^{\min}-R/c
=-\frac{\ln\epsilon_Q}{\kappa_{\rm tot}}.
}
$$

As

$$
\epsilon_Q\to0^+,
$$

the certification front diverges logarithmically.

Thus approaching the quantum/classical receiver boundary produces a universal critical slowing in this Markov Gaussian model.

---

## 10. Well-inside-range asymptotic

If

$$
\frac{1+\Lambda_{\rm req}/N_\Delta}
{\mathfrak Q_G(R)}
\ll1,
$$

then

$$
-\ln(1-x)\simeq x,
$$

and

$$
\boxed{
T_\Lambda^{\min}-R/c
\simeq
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g\kappa_{\rm tot}}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right).
}
$$

Therefore the far-zone post-light-cone build delay scales as

$$
\boxed{R^2}
$$

for a compact resonant receiver with fixed intrinsic linewidth.

---

## 11. Zero-temperature limit

The finite-margin variable $\Lambda$ above is normalized by the vacuum-output occupation $m$ and becomes singular as the receiver approaches an ideal pure-loss channel with

$$
\Gamma_{\rm th}\to0.
$$

Therefore the thermal front formula should not be naively evaluated by setting $\Gamma_{\rm th}=0$ inside $\Lambda$.

In vacuum the correct feasibility object is the maximum transferable negativity. For weak total capture,

$$
\boxed{
\mathcal N_{\max}
\simeq
\eta_Q
=
\frac{25\mathcal O}{16(kR)^2}
\frac{\kappa_g}{\kappa_{\rm tot}}.
}
$$

Thus thermal and vacuum receiver limitations should remain conceptually distinct.

---

## 12. Passive nonrelativistic specialization

For a passive nonrelativistic receiver,

$$
\frac{\kappa_g}{\omega}
\le
\frac23\mathcal C_B\beta_B^3.
$$

With one thermal internal bath,

$$
\Gamma_{\rm th}
=\bar n_B\omega/Q_B.
$$

A wave-zone NPT region with

$$
kR\ge\zeta
$$

requires

$$
\boxed{
\frac{25\mathcal O}{24}
\frac{Q_B\mathcal C_B\beta_B^3}
{\bar n_B}
>\zeta^2.
}
$$

In vacuum, the optimized source-receiver negativity obeys

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\lesssim
\frac{25\mathcal O}{24\zeta^2}
Q_B\mathcal C_B\beta_B^3
}
$$

in the weak-capture regime.

---

## 13. What is actually predicted

The model predicts a nested causal structure:

### Light cone

$$
T=R/c.
$$

### Quantum-capability/NPT front

$$
T_{\rm cap}=T_{\rm NPT}^{\min}.
$$

### Finite-certification front

$$
T_\Lambda^{\min}>T_{\rm cap}.
$$

At nonzero thermal noise the latter two terminate at finite radii,

$$
R_Q,
\qquad
R_\Lambda<R_Q,
$$

and diverge logarithmically as those ranges are approached from below.

This is not a modification of the relativistic light cone. It is a **quantum-information cone inside the ordinary causal cone**, set by receiver channel quality.

---

## 14. Central Feynman-level statement

> **Einstein tells us when the gravitational branch signal is allowed to arrive. The receiver then needs time to turn that arriving field into a quantum record faster than its own environment turns the same information into a classical record. The source determines how much branch information is available, the Green function determines how much reaches the receiver, and the receiver linewidths determine whether that information remains quantum. Those ingredients combine into one front in spacetime.**

---

## 15. Strongest next step

The model now has a single central prediction. The strongest remaining tasks are therefore validation rather than adding more mechanisms:

1. independent mathematical review of the binary coherent Gaussian theorem;
2. broader prior-art/citation-forward novelty check;
3. check the gravitational storage coefficient in a second fully explicit field quantization convention;
4. then reorganize the main Experiment 01 paper around this master equation and its general channel-capability interpretation.