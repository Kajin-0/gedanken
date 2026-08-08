# Finite-Spoke Invariance of the $25/16$ Storage Coefficient

**Date:** 2026-08-07  
**Status:** **NORMALIZATION AUDIT PASSED — CONSERVED-SOURCE CORRECTIONS CANCEL FROM THE NORMALIZED LEADING QUADRUPOLE STORAGE COEFFICIENT**

## 1. Question

The conserved finite-spoke source changes the quadrupole transition matrix element and spontaneous graviton linewidth:

$$
q_{01}
\to
q_{01}^{\rm end}\mathcal C_Q(q),
$$

$$
\kappa_g
\to
\kappa_g^{\rm end}\mathcal C_\kappa(q),
$$

where

$$
\mathcal C_\kappa(q)=\mathcal C_Q^2(q).
$$

Does this alter the previously audited wave-zone normalized storage coefficient

$$
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}?
$$

At leading compact-source quadrupole order, it does not.

---

## 2. Corrected transition matrix elements

For source $A$ and receiver $B$,

$$
q_{01,A}
=q_{01,A}^{\rm end}\mathcal C_Q(q_A),
$$

$$
q_{01,B}
=q_{01,B}^{\rm end}\mathcal C_Q(q_B).
$$

Their spontaneous gravitational linewidths satisfy

$$
\boxed{
\kappa_{g,A}
=K_A|q_{01,A}|^2,
}
$$

$$
\boxed{
\kappa_{g,B}
=K_B|q_{01,B}|^2,
}
$$

with the standard quadrupole frequency factors contained in $K_A,K_B$.

At equal resonance frequency,

$$
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\propto
|q_{01,A}q_{01,B}|.
$$

Thus finite-spoke corrections multiply the geometric mean linewidth by

$$
\boxed{
\mathcal C_Q(q_A)\mathcal C_Q(q_B).
}
$$

---

## 3. Cross response has the same matrix-element factors

At leading long-wavelength quadrupole order, the retarded source–receiver self-energy is bilinear in the transition quadrupoles:

$$
\Sigma_{AB}^R
\propto
q_{01,A}q_{01,B}
\,G_{QQ}^R(R,\omega).
$$

Therefore the finite-spoke corrections enter as

$$
\boxed{
\Sigma_{AB}^R
\to
\Sigma_{AB}^{R,{\rm end}}
\mathcal C_Q(q_A)\mathcal C_Q(q_B).
}
$$

For aligned plus modes the wave-zone form remains

$$
\boxed{
\Sigma_{AB}^{R}
\simeq
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_{g,A}\kappa_{g,B}},
}
$$

up to the same tensor/mode overlap and compact-source higher-multipole corrections as before.

The coefficient $5/4$ comes from the normalized leading $l=2$ tensor Green function, not from the absolute size of either quadrupole matrix element.

---

## 4. Normalized storage amplitude

Define

$$
\boxed{
t_{AB}^{\rm store}
=-i
\frac{\Sigma_{AB}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}.
}
$$

The factors

$$
\mathcal C_Q(q_A)\mathcal C_Q(q_B)
$$

cancel exactly between numerator and denominator.

Therefore

$$
\boxed{
t_{AB}^{\rm store}
\simeq
-i\frac54
\frac{e^{ikR}}{kR}
}
$$

for ideal aligned plus modes, and

$$
\boxed{
\eta_{\rm store}
=|t_{AB}^{\rm store}|^2
=\frac{25}{16(kR)^2}.
}
$$

With imperfect mode/tensor matching,

$$
\boxed{
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}.
}
$$

Thus the finite-spoke conservation correction does **not** renormalize the dimensionless state-storage coefficient.

---

## 5. Physical interpretation

There are two distinct quantities:

### Absolute source strength

The number/coherent distance emitted into the normalized gravitational mode depends on the total source quadrupole:

$$
N_\Delta(q_A)
\propto
\left(\frac{\tan q_A}{q_A}\right)^2.
$$

### Fraction of that normalized mode captured by the receiver

The geometric free-space storage fraction depends on

$$
\frac{|\Sigma_{AB}|^2}
{\kappa_{g,A}\kappa_{g,B}},
$$

so the absolute transition matrix elements cancel.

The receiver's **rate** of loading from the normalized incident mode still depends on its absolute linewidth:

$$
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B}.
$$

Hence

$$
\kappa_\Delta
\propto
\mathcal C_\kappa(q_B),
$$

while

$$
\eta_{\rm store}
$$

itself is invariant.

This separation prevents double counting the source correction.

---

## 6. Power-flow interpretation is unchanged

The independent power-flow derivation in `STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md` uses

1. the normalized angular distribution of an $l=2$ plus quadrupole;
2. the single-channel critical-coupling absorption cross section.

Multiplying the source quadrupole by any finite factor changes both the directional intensity and total radiated power by the same squared factor, so the normalized angular fraction is unchanged.

Likewise the critical-coupling cross section is a normalized one-channel statement, not an absolute quadrupole-strength statement.

Therefore the power-flow route also predicts no finite-spoke renormalization of $25/16$ at leading $l=2$ order.

---

## 7. What can still change the coefficient

The invariance applies within the same compact-source leading-quadrupole model.

Corrections can arise from

- finite-size retardation inside source/receiver;
- higher multipoles;
- tensor/polarization mismatch;
- temporal-mode mismatch;
- near-zone rather than wave-zone propagation;
- departures from a single isolated resonant $l=2$ receiver channel.

These are represented schematically by

$$
\mathcal O
$$

and controlled powers of

$$
\beta_A=kL_A,
\qquad
\beta_B=kL_B.
$$

They are conceptually distinct from the finite spoke-inertia parameter

$$
q=\omega L/c_s.
$$

---

## 8. Adversarial verdict

The conserved-source correction does **not** reopen the earlier factor-of-four storage-normalization ambiguity.

At leading quadrupole order,

$$
\boxed{
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}
}
$$

is invariant under the finite-spoke renormalization of source and receiver quadrupole matrix elements.

The absolute receiver loading rate should nevertheless use the corrected

$$
\kappa_{g,B}(q_B).
$$

---

## 9. Next check

The remaining propagation audit is not the $25/16$ normalization itself. It is the **finite-size field correction** at nonzero

$$
\beta=kL,
$$

for an extended elastic source/receiver.

The next useful question is whether the first nonvanishing source-size correction to the aligned plus-mode cross response is indeed $O(\beta^2)$ and how it compares numerically with the independent support-inertia correction $O(q^2)$.
