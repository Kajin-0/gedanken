# Resonant Free-Space Gravitational Quantum Reception Cone

**Updated:** 2026-08-07 17:38 EDT  
**Status:** Far-zone aligned-plus-quadrupole state-transfer model. The retarded Green kernel is independently cross-checked against a vacuum-graviton resonance calculation and a common-bath angular integral. This version explicitly distinguishes **coherent storage/absorption** from reciprocal scattering/extinction and restores the correct storage efficiency.

## 1. Exact normalized retarded cross response

For resonant aligned plus-type quadrupole transitions $A$ and $B$,

$$
\boxed{
\Sigma_{AB}^{R}(\omega,R)
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
}
$$

where

$$
\epsilon=kR=\frac{\omega R}{c},
$$

and

$$
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

In the wave zone,

$$
\boxed{
\Sigma_{AB}^{R}
\simeq
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

See `NORMALIZED_GRAVITATIONAL_CROSS_RESPONSE.md` and `INDEPENDENT_CROSS_RESPONSE_CHECK.md`.

---

## 2. Common-bath consistency check

For the plus quadrupole, the normalized on-shell common-bath overlap is

$$
\mu(\epsilon)
=\frac{5}{32}
\int_{-1}^{1}du\,
(1+6u^2+u^4)e^{i\epsilon u}.
$$

Direct integration gives

$$
\boxed{
\mu(\epsilon)
=\frac{5}{2\epsilon^5}
\left[
(\epsilon^4-3\epsilon^2+3)\sin\epsilon
+(2\epsilon^3-3\epsilon)\cos\epsilon
\right].
}
$$

Since the bracket is

$$
\operatorname{Im}[P(\epsilon)e^{i\epsilon}],
$$

$$
\boxed{
\Gamma_{AB}
=2\operatorname{Im}\Sigma_{AB}^{R}
}
$$

up to the retarded-sign convention.

This relation concerns the reciprocal common-bath self-energy and cross damping. It should **not** be interpreted as saying that the coherent field amplitude stored by $B$ is $2\Sigma_{AB}^{R}$.

---

## 3. Storage/state-transfer normalization

The relevant comparison for coherent quantum-memory transfer is the ordinary input-output one.

Let the source mode amplitude be $a_A$. Its outgoing normalized gravitational field amplitude is

$$
\boxed{
b_{\rm out,A}
=\sqrt{\kappa_{g,A}}\,a_A.
}
$$

Let the propagating source mode arrive at $B$ as

$$
b_{\rm in,B}=t_{AB}b_{\rm out,A}.
$$

The receiver equation contains the input drive

$$
\sqrt{\kappa_{g,B}}\,b_{\rm in,B}
=t_{AB}
\sqrt{\kappa_{g,A}\kappa_{g,B}}\,a_A.
$$

But the same retarded source drive is, by definition,

$$
\Sigma_{AB}^{R}a_A.
$$

Therefore the **coherent storage propagation amplitude** is

$$
\boxed{
t_{AB}^{\rm store}
=\frac{\Sigma_{AB}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}.
}
$$

In the wave zone,

$$
\boxed{
t_{AB}^{\rm store}
\simeq
\frac54\frac{e^{ikR}}{kR}.
}
$$

Hence the ideal aligned source-to-receiver **storage efficiency** is

$$
\boxed{
\eta_{\rm ff}^{\rm store}(R)
=|t_{AB}^{\rm store}|^2
=\frac{25}{16(kR)^2}.
}
$$

For general tensor/polarization/temporal mismatch,

$$
\boxed{
\eta_{\rm ff}^{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2},
\qquad
0\le\mathcal O\le1.
}
$$

This is the coefficient relevant to the source-to-memory quantum channel used in the causal-front theorem.

---

## 4. Why the factor-four scattering coefficient is different

The reciprocal common-bath relation

$$
\Gamma_{AB}=2\operatorname{Im}\Sigma_{AB}^{R}
$$

naturally introduces a factor of two in scattering/extinction amplitudes. Squaring that factor produces a cross-section four times larger than the maximal absorptive/storage cross-section.

For the aligned plus quadrupole, the source's on-axis power fraction is

$$
\frac1{P_G}\frac{dP_G}{d\Omega}\bigg|_z
=\frac{5}{8\pi}.
$$

Using the **storage** efficiency

$$
\eta_{\rm ff}^{\rm store}
=\frac{25}{16k^2R^2}
$$

corresponds to

$$
\boxed{
\sigma_{\rm abs,max}^{(l=2)}
=\frac{5\pi}{2k^2}.
}
$$

This is the critical-coupling absorption scale for one quadrupolar partial-wave channel.

By contrast, the factor-four larger quantity

$$
\frac{25}{4k^2R^2}
$$

corresponds to

$$
\boxed{
\sigma_{\rm sca,max}^{(l=2)}
=\frac{10\pi}{k^2},
}
$$

the unitary scattering/extinction scale.

For Experiment 01 the receiver is intended to **store the incoming branch mode coherently**, so the absorption/storage coefficient $25/16$ is the relevant one.

This distinction is analogous to the familiar difference between maximal dipole absorption and maximal dipole scattering cross-sections.

---

## 5. Receiver bath decomposition

The receiver's total spontaneous graviton linewidth

$$
\kappa_{g,B}
$$

is intrinsic and does not depend on source distance.

Distance changes only the fraction of the gravitational bath occupied by the selected source mode:

$$
\boxed{
\kappa_\Delta(R)
=\eta_{\rm ff}^{\rm store}(R)\kappa_{g,B}.
}
$$

The orthogonal gravitational vacuum channels contribute

$$
\kappa_{g,\perp}
=\kappa_{g,B}-\kappa_\Delta.
$$

Hence

$$
\boxed{
\kappa_{\rm tot}
=\kappa_{g,B}+\kappa_i+\cdots
}
$$

is distance independent.

Vacuum gravitational ports broaden the receiver but do not contribute to the thermal occupation budget

$$
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a
$$

when their occupation is zero.

---

## 6. Exact finite-cat NPT range

For a stationary thermal receiver, every nontrivial finite binary coherent source encoding becomes NPT iff

$$
\kappa_\Delta(R)>\Gamma_{\rm th}.
$$

Thus

$$
\frac{25\mathcal O}{16(kR)^2}
\kappa_{g,B}
>\Gamma_{\rm th}.
$$

Define

$$
\boxed{
R_Q^{\rm res}
=\frac{5}{4k}
\sqrt{
\frac{\mathcal O\kappa_{g,B}}
{\Gamma_{\rm th}}
}.
}
$$

Then

$$
\boxed{R<R_Q^{\rm res}}
$$

is the exact stationary-thermal NPT-capability range within the resonant far-zone model.

At zero thermal injection the mathematical NPT range is unbounded, as expected for pure loss.

---

## 7. Exact waveform-optimal spacetime front

For any normalized incoming source waveform,

$$
\tau_f(t)
\le
\frac{\kappa_\Delta(R)}{\kappa_{\rm tot}}
\left(1-e^{-\kappa_{\rm tot}(t-R/c)}\right).
$$

The matched time-reversed receiver ringdown saturates this ceiling.

Since

$$
\frac{\Gamma_{\rm th}}
{\kappa_\Delta(R)}
=\left(\frac{R}{R_Q^{\rm res}}\right)^2,
$$

the exact optimal NPT front is

$$
\boxed{
T_{\rm NPT}^{\min}(R)
=\frac Rc
-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-\left(\frac{R}{R_Q^{\rm res}}\right)^2
\right],
\qquad
R<R_Q^{\rm res}.
}
$$

No finite-cat NPT front exists for

$$
R\ge R_Q^{\rm res}
$$

at nonzero stationary thermal injection.

---

## 8. Front asymptotics

For

$$
R\ll R_Q^{\rm res}
$$

while remaining in the wave zone,

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
\simeq
\frac1{\kappa_{\rm tot}}
\left(\frac{R}{R_Q^{\rm res}}ight)^2.
}
$$

Thus the resonant post-light-cone quantum-build delay scales as

$$
\boxed{R^2}.
$$

Near the quantum range,

$$
R=R_Q^{\rm res}(1-\epsilon),
$$

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
\simeq
\frac1{\kappa_{\rm tot}}
\ln\frac1{2\epsilon}.
}
$$

The logarithmic vertical asymptote survives.

---

## 9. Wave-zone existence condition

Demand

$$
kR\ge\zeta.
$$

A nonempty resonant wave-zone NPT region requires

$$
kR_Q^{\rm res}>\zeta,
$$

or

$$
\boxed{
\frac{25\mathcal O}{16}
\frac{\kappa_{g,B}}
{\Gamma_{\rm th}}
>\zeta^2.
}
$$

Equivalently,

$$
\boxed{
\frac{\kappa_{g,B}}
{\Gamma_{\rm th}}
>
\frac{16}{25\mathcal O}\zeta^2.
}
$$

---

## 10. Passive nonrelativistic necessary condition

For one dominant thermal internal bath,

$$
\Gamma_{\rm th}
=\bar n_B\frac{\omega_B}{Q_B}.
$$

The passive nonrelativistic quadrupole sum-rule ceiling gives

$$
\frac{\kappa_{g,B}}
{\Gamma_{\rm th}}
\le
\frac23
\frac{Q_B\mathcal C_B\beta_B^3}
{\bar n_B}.
$$

Therefore a necessary condition for a passive nonrelativistic **resonant** wave-zone receiver is

$$
\boxed{
\frac{25\mathcal O}{24}
\frac{Q_B\mathcal C_B\beta_B^3}
{\bar n_B}
>\zeta^2.
}
$$

This is the robust resonant passive wave-zone criterion within the stated nonrelativistic sum-rule assumptions.

The earlier $\beta_B^5$ result applies only to a literal geometric-aperture-limited receiver and is not a universal passive bound.

---

## 11. Finite-strength certification range

For exact witness margin $\Lambda_{\rm req}>0$ and source difference-mode strength $N_\Delta$,

$$
\boxed{
R_\Lambda^{\rm res}
=
\frac{R_Q^{\rm res}}
{\sqrt{1+\Lambda_{\rm req}/N_\Delta}}.
}
$$

The finite-certification front is

$$
\boxed{
T_\Lambda^{\min}(R)
=
\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-\left(\frac{R}{R_\Lambda^{\rm res}}\right)^2
\right],
\qquad
R<R_\Lambda^{\rm res}.
}
$$

---

## 12. Receiver architectures

Keep two receiver classes distinct.

### Compact resonant receiver

$$
\eta_{\rm store}\sim(kR)^{-2},
$$

with effective maximal absorption area of order $k^{-2}$.

### Literal enclosing/absorbing cap

$$
\eta_{\rm cap}\sim(a_R/R)^2,
$$

set by physical angular coverage.

The cap architecture remains a valid Gedanken receiver but should not be used as a universal upper bound on a compact resonant absorber.

---

## 13. Remaining derivation target

The next clean step is to write the fully delayed source–field–receiver input-output equations in one notation and derive

$$
t_{AB}^{\rm store}
=\Sigma_{AB}^{R}/\sqrt{\kappa_{g,A}\kappa_{g,B}}
$$

directly from the propagating field elimination, including the distinction between

- coherent storage;
- collective damping;
- reciprocal scattering/extinction;
- time-reversed matched absorption.

That will make the storage normalization independent of cross-section analogy.