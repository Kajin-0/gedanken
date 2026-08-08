# Audit of the Wave-Zone Storage Coefficient $25/16$

**Timestamp:** 2026-08-07 20:12 EDT  
**Status:** Independent normalization audit of the aligned plus-quadrupole wave-zone storage coefficient. The result supports

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25}{16(kR)^2}
}
$$

for ideal polarization/tensor/temporal matching, rather than the four-times-larger unitary scattering coefficient.

---

## 1. The normalization question

The retarded gravitational Green-function calculation gives, for two aligned resonant plus-type quadrupole transitions,

$$
\Sigma_{AB}^{R}
\simeq
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_{g,A}\kappa_{g,B}}
$$

in the wave zone.

The source-output $\to$ receiver-input state-storage identification used in Experiment 01 is

$$
\boxed{
t_{AB}^{\rm store}
=-i\frac{\Sigma_{AB}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}},
}
$$

so

$$
\boxed{
|t_{AB}^{\rm store}|^2
=\frac{25}{16(kR)^2}.
}
$$

A factor-of-two ambiguity in amplitude can arise if one confuses the reciprocal self-energy with the full scattering/extinction amplitude. This note checks the coefficient by a completely different power-flow / partial-wave route.

---

## 2. Plus-quadrupole radiation pattern

For the plus STF quadrupole

$$
Q_{xx}=q,
\qquad
Q_{yy}=-q,
\qquad
Q_{zz}=0,
$$

the polarization-summed angular radiation weight can be written

$$
\boxed{
\mathcal F(\theta,\phi)
=2\cos^2\theta
+\frac12\sin^4\theta\cos^2(2\phi).
}
$$

On the $z$ axis,

$$
\boxed{
\mathcal F(0,\phi)=2.
}
$$

The exact full-sphere integral is

$$
\int d\Omega\,\mathcal F
=\frac{16\pi}{5}.
$$

Therefore the on-axis fraction of total radiated power per steradian is

$$
\boxed{
\frac1P\frac{dP}{d\Omega}\bigg|_{z}
=\frac{2}{16\pi/5}
=\frac{5}{8\pi}.
}
$$

At distance $R$, the on-axis incident intensity from a source radiating total power $P$ is therefore

$$
\boxed{
I_z(R)
=\frac{5}{8\pi}
\frac{P}{R^2}.
}
$$

---

## 3. One-channel partial-wave absorption limit

For a single spherical partial-wave channel with angular momentum $l$, the standard critical-coupling maximum absorption cross section per electric/magnetic-type channel is

$$
\boxed{
\sigma_{\rm abs,max}^{(l)}
=\frac{(2l+1)\pi}{2k^2}.
}
$$

The corresponding unitary scattering maximum is four times larger,

$$
\boxed{
\sigma_{\rm sca,max}^{(l)}
=\frac{2(2l+1)\pi}{k^2}.
}
$$

For the quadrupole channel $l=2$,

$$
\boxed{
\sigma_{\rm abs,max}^{(2)}
=\frac{5\pi}{2k^2},
}
$$

while

$$
\boxed{
\sigma_{\rm sca,max}^{(2)}
=\frac{10\pi}{k^2}.
}
$$

The factor of four is exactly the distinction that previously caused the storage/scattering ambiguity.

Experiment 01 requires coherent **capture/storage** into a receiver mode, so the absorption/critical-coupling cross section is the relevant one.

---

## 4. Power-flow derivation of the gravitational storage fraction

The maximum power stored/absorbed by a perfectly aligned resonant quadrupole receiver is

$$
P_{\rm abs,max}
=I_z(R)\,
\sigma_{\rm abs,max}^{(2)}.
$$

Substitute

$$
I_z(R)
=\frac{5}{8\pi}\frac{P}{R^2}
$$

and

$$
\sigma_{\rm abs,max}^{(2)}
=\frac{5\pi}{2k^2}.
$$

Then

$$
P_{\rm abs,max}
=
P
\left(
\frac{5}{8\pi R^2}
\right)
\left(
\frac{5\pi}{2k^2}
\right).
$$

Therefore

$$
\boxed{
\frac{P_{\rm abs,max}}{P}
=\frac{25}{16(kR)^2}.
}
$$

Thus

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25}{16(kR)^2}
}
$$

is independently reproduced without using the retarded self-energy normalization.

For imperfect tensor/polarization/temporal matching,

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2},
\qquad
0\le\mathcal O\le1.
}
$$

---

## 5. Electromagnetic dipole control case

The same reasoning can be checked in a theory whose normalization is standard.

Consider an electric dipole radiating transverse to the source-receiver axis.

Its normalized on-axis power fraction is

$$
\boxed{
\frac1P\frac{dP}{d\Omega}\bigg|_{\perp}
=\frac{3}{8\pi}.
}
$$

For one critically coupled electric-dipole channel,

$$
\boxed{
\sigma_{\rm abs,max}^{(l=1)}
=\frac{3\pi}{2k^2}.
}
$$

Therefore

$$
\boxed{
\eta_{\rm dip}^{\rm store}
=\frac{3}{8\pi R^2}
\frac{3\pi}{2k^2}
=\frac{9}{16(kR)^2}.
}
$$

This is exactly what the far-zone quantized electromagnetic dyadic Green tensor gives when its reciprocal source-receiver self-energy is normalized by the individual spontaneous-emission rates:

$$
\boxed{
\Sigma_{AB}^{R,\rm EM}
\simeq
\frac34
\frac{e^{ikR}}{kR}
\sqrt{\gamma_A\gamma_B}
}
$$

for the maximally coupled transverse geometry, so

$$
\left|
\frac{\Sigma_{AB}^{R,\rm EM}}
{\sqrt{\gamma_A\gamma_B}}
\right|^2
=\frac{9}{16(kR)^2}.
$$

This provides a direct control for the gravitational identification

$$
t_{AB}^{\rm store}
\propto
\Sigma_{AB}^{R}/\sqrt{\kappa_A\kappa_B}.
$$

---

## 6. Lehmberg control

Lehmberg's quantized-electromagnetic treatment of spatially separated two-level atoms derives the coupled source/receiver equations from a common continuum of quantized electromagnetic modes.

The standard cross-damping/coherent-exchange kernels contain the same far-zone dyadic-Green structure used in the control calculation above.

The electromagnetic result is important because it separates three quantities that can otherwise be confused:

1. reciprocal retarded self-energy;
2. collective damping/scattering amplitude;
3. one-way coherent state-storage/input amplitude.

The gravitational calculation follows the same open-system architecture with dipole $\to$ quadrupole and spin-1 $\to$ spin-2 angular structure.

---

## 7. Why the four-times-larger value is not storage

If one doubles the reciprocal self-energy amplitude before squaring, one obtains

$$
4\eta_{\rm store}
=\frac{25}{4(kR)^2}.
$$

Combining the on-axis gravitational intensity with this number implies

$$
\sigma
=\frac{10\pi}{k^2},
$$

which is precisely the **unitary scattering** cross section for one $l=2$ channel, not the critical-coupling absorption/storage cross section.

Thus the factor-of-four discrepancy has a clean physical interpretation:

$$
\boxed{
\text{storage/absorption}
=\frac14\times
\text{unitary scattering maximum}.
}
$$

The state-transfer problem must use the former.

---

## 8. Three independent checks now agree

The coefficient $25/16$ is supported by:

### Check 1 — retarded gravitational Green function

$$
\Sigma_{AB}^{R}
\to
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
$$

### Check 2 — gravitational angular power × $l=2$ critical absorption area

$$
\frac{5}{8\pi}
\times
\frac{5\pi}{2k^2}
=
\frac{25}{16k^2}.
$$

### Check 3 — electromagnetic $l=1$ control

$$
\frac{3}{8\pi}
\times
\frac{3\pi}{2k^2}
=
\frac{9}{16k^2},
$$

matching the normalized far-zone electromagnetic Green coupling.

These checks are independent enough that a hidden factor-of-two error in the storage interpretation is now substantially less likely.

---

## 9. Literature anchors

### Quantized electromagnetic common-bath control

R. H. Lehmberg, **Radiation from an N-Atom System. I. General Formalism**, Phys. Rev. A 2, 883 (1970).

This is the canonical quantized-field derivation of coupled radiating atoms / harmonic oscillators through a shared electromagnetic continuum.

### Absorption/scattering upper bounds

J.-P. Hugonin, M. Besbes, P. Ben-Abdallah, **Fundamental limits for light absorption and scattering induced by cooperative electromagnetic interactions**, Phys. Rev. B 91, 180202(R) (2015).

This provides a primary modern reference for critical absorption/scattering limits of radiative channels.

### Gravitational retarded quadrupole control

Y. Hu, J. Hu, H. Yu, P. Wu, **Resonance interaction between two entangled gravitational polarizable objects**, Eur. Phys. J. C 80, 792 (2020), arXiv:2001.05116.

Their linearized-quantum-gravity quadrupole resonance interaction independently exhibits the same $R^{-5}\to R^{-1}$ near/far crossover as the retarded gravitational kernel used here.

---

## 10. Remaining caveat

This audit validates the **far-zone aligned single-channel normalization**.

It does not by itself replace a full second derivation of the gravitational input-output map from canonically normalized TT graviton modes.

Before submission, the strongest remaining normalization check would be:

1. start from the canonical TT field expansion;
2. derive the receiver quadrupole coupling constants $g_{\mathbf k\lambda}$;
3. normalize them by the spontaneous graviton linewidth $\kappa_g$;
4. explicitly construct the source emission mode and receiver absorption mode;
5. evaluate their far-zone overlap.

The expected result is now tightly constrained to reproduce $25/16$.