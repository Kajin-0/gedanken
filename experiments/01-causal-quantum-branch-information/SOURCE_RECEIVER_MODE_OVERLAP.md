# Source–Receiver Graviton Mode Overlap

**Timestamp:** 2026-08-07 16:10 EDT  
**Status:** Active derivation for Experiment 01

This note completes the mode-matching step for the wave-zone Gedankenexperiment. The receiver's useful gravitational coupling is determined not only by its total graviton linewidth but by the overlap between the source's branch-difference graviton wavepacket and the time-reversed spontaneous-emission mode of the receiver.

---

## 1. Far-zone quadrupolar graviton mode

For a localized STF quadrupole tensor $Q_{ij}$, the far-zone graviton amplitude into direction $\mathbf n$ and polarization $\lambda$ is proportional to

$$
A_\lambda(\mathbf n)
=e_{ij}^{(\lambda)}(\mathbf n)Q_{ij},
$$

where $e_{ij}^{(\lambda)}$ is a transverse-traceless polarization tensor.

For two quadrupoles $Q^S_{ij}$ and $Q^B_{ij}$, define the angular/polarization inner product

$$
\langle Q_B,Q_S\rangle_{\rm rad}
\equiv
\int d\Omega\sum_\lambda
A^B_\lambda(\mathbf n)^*
A^S_\lambda(\mathbf n).
$$

Rotational invariance implies this bilinear form must be proportional to the unique STF scalar contraction

$$
Q_B^{ij*}Q^S_{ij}.
$$

With the polarization normalization used in the rest of Experiment 01,

$$
\boxed{
\int d\Omega\sum_\lambda
A^B_\lambda{}^*A^S_\lambda
=
\frac{16\pi}{5}
Q_B^{ij*}Q^S_{ij}.
}
$$

The overall constant cancels from normalized mode overlaps.

---

## 2. Invariant quadrupole mode overlap

The normalized full-$4\pi$ spatial/polarization overlap is therefore

$$
\boxed{
\mathcal O_Q
=
\frac{|Q_B^{ij*}Q^S_{ij}|^2}
{(Q_B^{ij*}Q^B_{ij})
 (Q_S^{ij*}Q^S_{ij})}.
}
$$

This obeys

$$
0\le\mathcal O_Q\le1.
$$

Equality $\mathcal O_Q=1$ means the source and receiver quadrupole tensors define the same normalized spin-2 radiation mode up to phase/sign.

Orthogonal STF tensors give

$$
\mathcal O_Q=0.
$$

Thus the wave-zone quantum matching condition is fundamentally a **tensor-mode matching problem**, not merely a question of placing the receiver at the right point in space.

---

## 3. Spin-2 orientation law

Take the source plus quadrupole

$$
Q_S=q\,\operatorname{diag}(1,-1,0).
$$

Rotate an otherwise identical receiver quadrupole by angle $\psi$ around the common $z$ axis.

The normalized amplitude overlap is

$$
\frac{Q_B^{ij}Q^S_{ij}}
{\sqrt{(Q_B:Q_B)(Q_S:Q_S)}}
=\cos2\psi.
$$

Therefore

$$
\boxed{
\mathcal O_Q(\psi)=\cos^2(2\psi).
}
$$

Consequences:

- $\psi=0$: perfect overlap;
- $\psi=\pi/4$: zero overlap;
- $\psi=\pi/2$: unit overlap again, with an overall sign/phase reversal.

This is the expected spin-2 orientation structure.

---

## 4. Random orientation benchmark

The STF quadrupole representation is five-dimensional. For a fixed normalized source quadrupole and a uniformly random receiver orientation in the irreducible $l=2$ representation,

$$
\boxed{
\langle\mathcal O_Q\rangle_{\rm orientation}
=\frac15.
}
$$

This gives a useful baseline: an unaligned quadrupolar receiver typically accesses only an order-$20\%$ mode-overlap fraction even before aperture and temporal mismatch are included.

---

## 5. Finite angular access

Full-$4\pi$ overlap assumes complete access to the source radiation mode. If only a region $\mathcal A$ of solid angle is controlled, define

$$
\mathcal O_{Q,\mathcal A}
=
\frac{
\left|
\int_{\mathcal A}d\Omega\sum_\lambda
A^B_\lambda{}^*A^S_\lambda
\right|^2
}
{
\left(
\int_{\mathcal A}d\Omega\sum_\lambda|A^B_\lambda|^2
\right)
\left(
\int_{4\pi}d\Omega\sum_\lambda|A^S_\lambda|^2
\right)
}.
$$

For a perfectly matched receiver mode restricted only by aperture, this reduces to the accessible power fraction derived in `GRAVITATIONAL_BETA_FACTOR.md`.

For the plus quadrupole and one polar cap $0\le\theta\le\theta_0$, $u_0=\cos\theta_0$,

$$
\boxed{
\beta_{\rm cap}
=\frac12-
\frac{u_0^5+10u_0^3+5u_0}{32}.
}
$$

One ideal hemisphere therefore gives exactly

$$
\beta_{\rm cap}=1/2.
$$

---

## 6. Temporal / spectral mode overlap

Spatial and polarization matching are not sufficient. The source and receiver wavepackets must also match temporally.

For normalized exponentially decaying one-boson emission modes

$$
f_S(t)
=\sqrt{\kappa_S}\,
e^{-\kappa_St/2}e^{-i\omega_St}\Theta(t),
$$

$$
f_B(t)
=\sqrt{\kappa_B}\,
e^{-\kappa_Bt/2}e^{-i\omega_Bt}\Theta(t),
$$

the normalized spectral/temporal overlap is

$$
\langle f_B|f_S\rangle
=
\frac{\sqrt{\kappa_S\kappa_B}}
{(\kappa_S+\kappa_B)/2-i\Delta},
$$

where

$$
\Delta=\omega_B-\omega_S.
$$

Hence

$$
\boxed{
\mathcal O_t
=
\frac{4\kappa_S\kappa_B}
{(\kappa_S+\kappa_B)^2+4\Delta^2}.
}
$$

Perfect temporal/spectral overlap requires

$$
\kappa_S=\kappa_B,
\qquad
\Delta=0.
$$

For coherent absorption the receiver must couple to the **time-reversed** version of its spontaneous-emission mode. The expression above is therefore best interpreted as the intrinsic spectral compatibility of the two radiative modes; an actual static receiver may require temporal control to realize the corresponding time-reversed absorption waveform.

---

## 7. Factorized total source–receiver overlap

When angular/polarization and temporal dependences factorize, define

$$
\boxed{
\mathcal O_{SB}
=\beta_{\rm access}
\,\mathcal O_Q
\,\mathcal O_t
\,\mathcal O_{\rm other},
}
$$

where $\mathcal O_{\rm other}$ may include radial-mode, phase-front, or other geometric mismatch factors.

Then

$$
0\le\mathcal O_{SB}\le1.
$$

The receiver's total gravitational radiative linewidth $\kappa_g$ decomposes relative to the source difference mode as

$$
\boxed{
\kappa_\Delta
=\mathcal O_{SB}\,\kappa_g,
}
$$

$$
\boxed{
\kappa_\perp
=(1-\mathcal O_{SB})\kappa_g,
}
$$

within the one-frequency Markov decomposition used here.

This is the precise source–receiver version of the gravitational beta factor.

---

## 8. Mode-overlap corrected thermal NPT condition

The matched receiver's total damping is

$$
\kappa_{\rm tot}
=\kappa_\Delta+\kappa_\perp+\kappa_i
=\kappa_g+\kappa_i.
$$

The orthogonal gravitational channels are vacuum in the present model; they reduce useful capture efficiency but do not add thermal quanta.

For a stationary receiver, the thermal occupation is

$$
m_*
=\frac{\kappa_i\bar n_i}{\kappa_{\rm tot}}.
$$

The maximum useful source-mode capture accumulated by time $\tau=t-R/c$ is

$$
\eta_\Delta(\tau)
=
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau}).
$$

The weak-cat NPT condition

$$
\eta_\Delta>m_*
$$

therefore becomes

$$
\boxed{
\kappa_\Delta>\bar n_i\kappa_i.
}
$$

Using $\kappa_\Delta=\mathcal O_{SB}\kappa_g$,

$$
\boxed{
\mathcal O_{SB}\kappa_g
>\bar n_i\kappa_i.
}
$$

This is a clean result: **vacuum gravitational coupling to orthogonal modes reduces the amount of transferable entanglement but does not move the weak-cat entanglement-breaking boundary; thermal record formation does.**

---

## 9. Mode-overlap corrected global-history threshold

The global fidelity-history witness requires

$$
\eta_\Delta>m_*+\frac12.
$$

Substituting the stationary receiver quantities gives

$$
2\kappa_\Delta
>
\kappa_{\rm tot}+2\bar n_i\kappa_i.
$$

Since

$$
\kappa_{\rm tot}
=\kappa_\Delta+\kappa_\perp+\kappa_i,
$$

this becomes

$$
\boxed{
\kappa_\Delta
>
\kappa_\perp+(2\bar n_i+1)\kappa_i.
}
$$

In terms of $\mathcal O_{SB}$,

$$
\boxed{
(2\mathcal O_{SB}-1)\kappa_g
>(2\bar n_i+1)\kappa_i.
}
$$

Thus the simple global history witness has an irreducible geometric requirement

$$
\boxed{
\mathcal O_{SB}>1/2
}
$$

even when internal loss vanishes.

This is the mode-matching version of the earlier $50\%$ capture threshold.

---

## 10. Mode-overlap corrected causal front

If

$$
\kappa_\Delta>\bar n_i\kappa_i,
$$

the optimized weak-cat NPT front is

$$
\boxed{
T_{\rm NPT}(R)
=
\frac{R}{c}
+
\frac{1}{\kappa_g+\kappa_i}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\bar n_i\kappa_i}
\right].
}
$$

Equivalently,

$$
\boxed{
T_{\rm NPT}(R)
=
\frac{R}{c}
+
\frac{1}{\kappa_g+\kappa_i}
\ln\left[
\frac{\mathcal O_{SB}\kappa_g}
{\mathcal O_{SB}\kappa_g-\bar n_i\kappa_i}
\right].
}
$$

Thus orientation, aperture, frequency mismatch, and temporal mismatch do not alter the light-cone delay $R/c$; they alter the **post-light-cone quantum build time** through the useful-mode rate.

---

## 11. Orientation as a causal quantum control knob

For the rotated plus-quadrupole example,

$$
\mathcal O_Q=\cos^22\psi.
$$

Ignoring other mismatch factors, the weak-cat thermal condition is

$$
\boxed{
\cos^22\psi\,\kappa_g
>\bar n_i\kappa_i.
}
$$

So simply rotating the receiver through $45^\circ$ can continuously close the causal quantum channel while leaving many gross classical properties of the receiver unchanged.

This suggests a particularly clean Gedanken control experiment: compare otherwise identical receivers at mode-matched and quadrupole-orthogonal orientations.

---

## 12. Current Einstein/Feynman interpretation

> **A gravitational quantum receiver must not merely be sensitive to gravity. It must radiate, and therefore absorb, the same spin-2 mode that the source branch difference creates. The overlap is set by an invariant contraction of the two quadrupole tensors, by how much of the radiation pattern is physically accessible, and by temporal/frequency matching. Misaligned or inaccessible gravitational modes still carry branch information, but they do not help the intended receiver. They become part of the unobserved record. The causal entanglement front is therefore controlled by the useful matched-mode rate $\kappa_\Delta$, not by the receiver's total gravitational transition rate.**

---

## 13. Novelty discipline

TT projection, quadrupole radiation patterns, spin-2 orientation dependence, matched temporal modes, and input-output mode decompositions are standard ingredients.

Potentially distinctive is their assembly into a causal gravitational branch-information transfer law,

$$
\boxed{
\mathcal O_{SB}\kappa_g>\bar n_i\kappa_i,
}
$$

with a directly calculable post-light-cone entanglement-front time.

No novelty claim should be made until the exact source-receiver mode-overlap formulation is checked against current graviton absorption/state-transfer literature.

---

## 14. Immediate next step

The next task is to optimize the full useful-mode rate

$$
\kappa_\Delta
=\mathcal O_{SB}\kappa_g
$$

under the passive receiver sum-rule ceiling and finite aperture. This will show whether increasing total gravitational oscillator strength or improving mode matching is the more valuable resource in each regime.