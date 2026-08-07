# Normalized Gravitational Cross Response

**Timestamp:** 2026-08-07 17:25 EDT  
**Status:** Exact for the aligned plus-quadrupole geometry in linearized gravity; provides the bridge between local resonant reception and geometric wave-zone propagation.

## 1. Purpose

A previous finite-aperture construction assumed that coherent collection was bounded by literal physical area. That is not universal for a resonant quantum absorber: effective quantum cross-sections can exceed geometric area.

A cleaner comparison uses quantities already fixed by quantum gravity itself:

1. the retarded source-to-receiver tidal response;
2. the spontaneous graviton linewidth of each quadrupole transition.

The ratio is dimensionless and does not require assigning a geometric aperture by hand.

---

## 2. Source and receiver quadrupoles

Take two resonant plus-type STF quadrupole transitions $A$ and $B$,

$$
Q_{xx}^{(j)}=q_j,
\qquad
Q_{yy}^{(j)}=-q_j,
\qquad
j=A,B.
$$

Place $B$ on the $z$ axis of $A$ and align their plus axes.

For harmonic time dependence $e^{-i\omega t}$, the exact retarded electric-Weyl response from $A$ is

$$
\boxed{
\mathcal E_{xx}^{A}(\omega,R)
=-\frac{Gq_A}{R^5}
P(\epsilon)e^{i\epsilon},
}
$$

where

$$
\epsilon=\frac{\omega R}{c}
$$

and

$$
\boxed{
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
}
$$

---

## 3. Receiver interaction energy

For an external tidal field, the quadrupole interaction is

$$
H_I=-\frac12Q_B^{ij}\mathcal E_{ij}.
$$

For the aligned plus tensors on the symmetry axis,

$$
\mathcal E_{yy}=-\mathcal E_{xx},
$$

so

$$
-\frac12Q_B^{ij}\mathcal E_{ij}
=-q_B\mathcal E_{xx}.
$$

Hence the complex retarded source-receiver frequency coefficient, in frequency units, is

$$
\boxed{
\Sigma_{AB}^{R}(\omega,R)
=\frac{Gq_Aq_B}{\hbar R^5}
P(\epsilon)e^{i\epsilon}
}
$$

up to the overall retarded-sign convention.

Its real and imaginary parts encode the dispersive/coherent and radiative/collective-damping pieces of the common-field interaction; the full complex object is the convention-safe quantity to retain.

---

## 4. Express in spontaneous graviton linewidths

For a plus-type quadrupole transition,

$$
Q_{ij}^{10}Q_{ij}^{01}=2|q|^2.
$$

The spontaneous quadrupole graviton linewidth is

$$
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01},
$$

so

$$
\boxed{
\kappa_g
=\frac{4G\omega^5}{5\hbar c^5}|q|^2.
}
$$

Therefore

$$
|q_j|^2
=\frac{5\hbar c^5}{4G\omega^5}
\kappa_{g,j}.
$$

For resonant $A$ and $B$,

$$
q_Aq_B
\rightarrow
\frac{5\hbar c^5}{4G\omega^5}
\sqrt{\kappa_{g,A}\kappa_{g,B}}
$$

in magnitude, with any quadrupole transition phases absorbed into the orientation overlap.

Substitution yields the exact normalized response

$$
\boxed{
\Sigma_{AB}^{R}(\omega,R)
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}
{\epsilon^5}.
}
$$

This is the central result of this note.

---

## 5. Static/near-zone limit

For

$$
\epsilon\ll1,
$$

$$
P(\epsilon)=3+O(\epsilon),
$$

so

$$
\boxed{
\Sigma_{AB}^{R}
\simeq
\frac{15}{4}
\frac{\sqrt{\kappa_{g,A}\kappa_{g,B}}}
{\epsilon^5}.
}
$$

The enormous factor relative to spontaneous radiative linewidth reflects the reactive near field: coherent tidal coupling can be much stronger than radiative graviton emission.

This is the quantum-channel form of the earlier near-field/radiation separation.

---

## 6. Wave-zone limit

For

$$
\epsilon\gg1,
$$

$$
P(\epsilon)\simeq\epsilon^4,
$$

and hence

$$
\boxed{
\Sigma_{AB}^{R}
\simeq
\frac54
\frac{e^{i\epsilon}}{\epsilon}
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

Thus the resonant source-receiver **amplitude** decays as

$$
\frac1{kR},
$$

and any weak single-pass transfer probability built from this amplitude scales as

$$
\boxed{
\propto\frac1{(kR)^2}.
}
$$

This is the resonant quantum-receiver analogue of an effective absorption/scattering area of order the wavelength squared.

It does **not** contain the extra factor $(L_B/R)^2$ unless a separate geometric-aperture restriction is imposed.

---

## 7. Relation to earlier local-receiver result

The earlier exact local history cooperativity had wave-zone scaling

$$
\mathcal C_{\rm hist}^{(G)}
\propto
\nu_G\epsilon^{-2}.
$$

The normalized cross response explains that scaling directly:

$$
|\Sigma_{AB}^{R}|^2
\propto
\kappa_{g,A}\kappa_{g,B}\epsilon^{-2}.
$$

Thus the local resonant receiver and the propagating-wave picture are consistent once the receiver is characterized by its **quantum transition linewidth/effective cross-section**, not literal geometric area.

---

## 8. Distinction from the enclosing-cap model

The spherical-cap receiver in `FINITE_APERTURE_WAVEZONE_FRONT.md` is a different Gedanken architecture:

- it physically occupies a fraction of a sphere centered on the source;
- it is assumed to coherently absorb the field crossing that cap;
- its accessible mode fraction is therefore geometric.

A compact resonant receiver instead samples the field locally but can have an effective resonant area controlled by wavelength and transition strength.

Neither model should be substituted for the other without an explicit scattering/input-output derivation.

---

## 9. Next calculation

The remaining task is to derive the **actual source-mode overlap/transmission coefficient** $\tau_{A\to B}$ for a finite emitted wavepacket from the complex cross kernel $\Sigma_{AB}^{R}$, including

- source linewidth $\kappa_{g,A}$;
- receiver linewidth $\kappa_{g,B}$ and internal loss;
- retardation;
- the collective radiative damping part of the same Green tensor;
- optimized source pulse shaping.

That will replace the heuristic geometric $\mathcal O_{SB}(R)$ by a genuine free-space gravitational quantum transfer channel.