# Resonant Free-Space Gravitational Quantum Reception Cone

**Updated:** 2026-08-07 17:36 EDT  
**Status:** Far-zone aligned-plus-quadrupole result. The retarded cross Green function is independently checked against Hu et al. and its collective-decay part is reproduced by an explicit angular common-bath integral. This corrects an earlier factor-of-four error in the propagation efficiency.

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

## 2. Exact common-bath angular check

For the plus quadrupole, the polarization-summed on-shell angular weight is

$$
\mathcal F(\theta,\phi)
=2\cos^2\theta
+\frac12\sin^4\theta\cos^2(2\phi).
$$

After azimuthal integration,

$$
\int_0^{2\pi}d\phi\,\mathcal F
=\frac\pi2(1+6u^2+u^4),
\qquad
u=\cos\theta.
$$

The normalized common-bath overlap is therefore

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

But

$$
\operatorname{Im}[P(\epsilon)e^{i\epsilon}]
=(\epsilon^4-3\epsilon^2+3)\sin\epsilon
+(2\epsilon^3-3\epsilon)\cos\epsilon.
$$

Hence

$$
\boxed{
\mu(\epsilon)
=\frac{5}{2\epsilon^5}
\operatorname{Im}[P(\epsilon)e^{i\epsilon}].
}
$$

The cross damping is

$$
\Gamma_{AB}
=\sqrt{\kappa_{g,A}\kappa_{g,B}}\,\mu(\epsilon),
$$

so the exact retarded self-energy obeys

$$
\boxed{
\Gamma_{AB}
=2\operatorname{Im}\Sigma_{AB}^{R}
}
$$

up to the overall retarded-sign convention.

This is the standard open-system relation and fixes the factor relating the reciprocal retarded self-energy to a one-way cascaded propagation amplitude.

---

## 3. Correct one-way far-field propagation efficiency

For a directional/cascaded channel with propagation amplitude $t_{AB}$, the corresponding reciprocal retarded self-energy has magnitude

$$
|\Sigma_{AB}^{R}|
=\frac12|t_{AB}|
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
$$

Therefore, in the wave zone,

$$
|t_{AB}|
=\frac{2|\Sigma_{AB}^{R}|}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}
\simeq
\frac{5}{2kR}.
$$

The ideal aligned source-to-receiver propagation efficiency is thus

$$
\boxed{
\eta_{\rm ff}(R)
=|t_{AB}|^2
=\frac{25}{4(kR)^2}.
}
$$

This supersedes the earlier provisional value $25/[16(kR)^2]$.

For general tensor/polarization/temporal mismatch,

$$
\boxed{
\eta_{\rm ff}(R)
=\frac{25\mathcal O}{4(kR)^2},
\qquad
0\le\mathcal O\le1.
}
$$

The interpretation is restricted to

$$
kR\gg1,
$$

where this is safely below unity. The near-zone Green response contains reactive interactions and cannot be treated as a pure propagating transmissivity.

---

## 4. Resonant cross-section consistency check

The plus-quadrupole source radiates most strongly along its $z$ axis. Its on-axis angular power fraction is

$$
\boxed{
\frac{1}{P_G}
\frac{dP_G}{d\Omega}\bigg|_{z}
=\frac{5}{8\pi}.
}
$$

If a receiver of resonant cross-section $\sigma_{\rm res}$ sits on this axis, the captured power fraction is

$$
\eta_{\rm ff}
=\frac{5}{8\pi}
\frac{\sigma_{\rm res}}{R^2}.
$$

Using the common-bath result

$$
\eta_{\rm ff}
=\frac{25}{4k^2R^2}
$$

gives

$$
\boxed{
\sigma_{\rm res}
=\frac{10\pi}{k^2}.
}
$$

This is the expected unitary-scale cross-section for an $l=2$ resonant partial wave, providing an independent physical consistency check on the factor of four.

The relevant cross-section is set by wavelength and transition strength, not necessarily by the literal material area of a subwavelength receiver.

---

## 5. Receiver bath decomposition

The receiver's total spontaneous graviton linewidth

$$
\kappa_{g,B}
$$

is intrinsic and distance independent.

The incoming source branch mode occupies only a fraction of that gravitational bath:

$$
\boxed{
\kappa_\Delta(R)
=\eta_{\rm ff}(R)\kappa_{g,B}.
}
$$

All orthogonal gravitational vacuum modes contribute the remaining damping

$$
\kappa_{g,\perp}
=\kappa_{g,B}-\kappa_\Delta.
$$

Therefore

$$
\boxed{
\kappa_{\rm tot}
=\kappa_{g,B}+\kappa_i+\cdots
}
$$

is independent of source distance.

Only occupied uncontrolled baths contribute to

$$
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a.
$$

---

## 6. Exact finite-cat NPT range

For a stationary thermal receiver, every finite nontrivial binary coherent source encoding becomes NPT iff

$$
\kappa_\Delta(R)>\Gamma_{\rm th}.
$$

Thus

$$
\frac{25\mathcal O}{4(kR)^2}
\kappa_{g,B}
>\Gamma_{\rm th}.
$$

Define

$$
\boxed{
R_Q^{\rm res}
=\frac{5}{2k}
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

is the exact thermal NPT-capability range within the far-zone resonant model.

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

The matched time-reversed receiver ringdown saturates the ceiling.

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

while still satisfying the wave-zone condition,

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
\simeq
\frac1{\kappa_{\rm tot}}
\left(\frac{R}{R_Q^{\rm res}}\right)^2.
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

The logarithmic vertical asymptote survives unchanged.

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
\frac{25\mathcal O}{4}
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
\frac{4}{25\mathcal O}\zeta^2.
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
\frac{25\mathcal O}{6}
\frac{Q_B\mathcal C_B\beta_B^3}
{\bar n_B}
>\zeta^2.
}
$$

This is the corrected resonant passive wave-zone criterion.

It is still extremely restrictive for ordinary matter because

$$
\mathcal C_B\ll1,
\qquad
\beta_B\ll1,
$$

but there is no universal extra $\beta_B^2$ geometric penalty.

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

Keep two distinct models separate.

### Compact resonant receiver

$$
\eta_{\rm ff}\sim(kR)^{-2},
$$

with effective resonant cross-section of order $k^{-2}$.

### Literal enclosing/absorbing cap

$$
\eta_{\rm cap}\sim(a_R/R)^2,
$$

set by physical angular coverage around the source.

The cap model remains a legitimate Gedanken architecture but is not a universal bound on resonant matter.

---

## 13. Current remaining caveat

The common-bath angular calculation and classical cross-section consistency strongly support the corrected coefficient. A fully explicit delayed two-system input-output derivation would still be valuable for separating reciprocal coherent exchange, collective damping, and strictly one-way state-transfer conventions in one notation.
