# Gravitational Friis Form of the Aligned Quadrupole Link

**Date:** 2026-08-08  
**Status:** **INTERPRETIVE NORMALIZATION RESULT — STANDARD ANTENNA STRUCTURE, NOT A NOVELTY CLAIM**

## 1. Purpose

The V6 wave-zone source→receiver storage factor is

$$
\boxed{
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}.}
$$

The numerical coefficient can look gravitationally peculiar when written only in retarded Green-function language.

For the aligned plus-quadrupole channel it has a simpler interpretation:

> **The coefficient is exactly the ordinary reciprocal far-field antenna transmission factor for a transmitter and receiver that each have directional gain \(5/2\), multiplied by the residual normalized mode-overlap factor.**

Thus the propagation part of V6 is a spin-2/quadrupole analogue of an ordinary Friis link.

This is an interpretation and consistency check, not a claim that the Friis equation or gravitational antenna reciprocity is new.

---

# 2. Source directivity

For the plus STF quadrupole

$$
Q_{ij}=q\,\operatorname{diag}(1,-1,0),
$$

the on-axis radiation fraction is

$$
\boxed{
\frac1{P_G}
\frac{dP_G}{d\Omega}\bigg|_{z}
=\frac{5}{8\pi}.}
$$

Define the usual dimensionless transmitting directivity/gain relative to isotropic radiation:

$$
\boxed{
G_A
=4\pi
\frac1{P_G}
\frac{dP_G}{d\Omega}\bigg|_z.}
$$

Therefore

$$
\boxed{G_A=\frac52.}
$$

This is simply the directional gain of the chosen plus-quadrupole radiation pattern along its symmetry axis.

---

# 3. Receiver effective area and reciprocal gain

The maximum useful absorptive/storage cross section of one critically coupled \(l=2\) channel is

$$
\boxed{
A_{e,B}
\equiv
\sigma_{{\rm abs},l=2}^{\max}
=\frac{5\pi}{2k^2}.}
$$

Using

$$
\lambda=\frac{2\pi}{k},
$$

this becomes

$$
\boxed{
A_{e,B}
=\frac{5\lambda^2}{8\pi}.}
$$

For a reciprocal far-field antenna/channel the effective area and receiving gain are related by

$$
A_e
=\frac{G\lambda^2}{4\pi}.
$$

Hence the receiver gain corresponding to the \(l=2\) critical-coupling area is

$$
\boxed{
G_B
=\frac{4\pi A_{e,B}}{\lambda^2}
=\frac52.}
$$

Thus the matched plus-quadrupole source and receiver have the same reciprocal directional gain,

$$
\boxed{G_A=G_B=\frac52.}
$$

---

# 4. Friis reconstruction

The ordinary far-field reciprocal-antenna power-transfer relation is

$$
\frac{P_B}{P_A}
=G_AG_B
\left(
\frac{\lambda}{4\pi R}
\right)^2
$$

for aligned, polarization-matched antennas in free space.

Insert

$$
G_A=G_B=\frac52.
$$

Then

$$
\frac{P_B}{P_A}
=\frac{25}{4}
\frac{\lambda^2}{16\pi^2R^2}.
$$

Since

$$
\frac{\lambda^2}{4\pi^2}
=\frac1{k^2},
$$

we obtain

$$
\boxed{
\frac{P_B}{P_A}
=\frac{25}{16(kR)^2}.}
$$

Including residual normalized tensor/polarization/spatial/spectral mismatch gives

$$
\boxed{
\eta_{\rm store}
=\mathcal O\,
G_AG_B
\left(
\frac{\lambda}{4\pi R}
\right)^2
=\frac{25\mathcal O}{16(kR)^2}.}
$$

This is exactly the storage factor already obtained from the retarded self-energy/input-output derivation.

---

# 5. Quantum link-budget form

The complete V6 vacuum-source link can therefore be written as

$$
\boxed{
\tau_{A\to B}(t)
=
\beta_{g,A}
G_AG_B
\left(
\frac{\lambda}{4\pi R}
\right)^2
\mathcal O
\beta_{g,B}
\mathcal T_f(t).}
$$

For the aligned plus-quadrupole channel,

$$
G_A=G_B=5/2.
$$

This gives a direct analogy with a conventional link budget:

### transmitting-interface efficiency

$$
\beta_{g,A};
$$

### transmitting antenna gain

$$
G_A;
$$

### free-space path factor

$$
\left(\frac{\lambda}{4\pi R}\right)^2;
$$

### receiving antenna gain / source-mode alignment

$$
G_B\mathcal O;
$$

### receiver gravitational interface efficiency

$$
\beta_{g,B};
$$

### temporal impedance/mode matching

$$
\mathcal T_f.
$$

Thus

$$
\boxed{
\text{gravitational quantum link}
=
\text{matter--gravity source efficiency}
\times
\text{ordinary far-field antenna transfer}
\times
\text{matter--gravity receiver efficiency}
\times
\text{temporal loading}.}
$$

---

# 6. Why this is useful

The Friis form makes three points immediate.

## 6.1 The \(R^{-2}\) factor is not a mysterious quantum penalty

It is the ordinary far-field transmission factor between finite-gain reciprocal wave channels.

The severe quantum weakness of ordinary matter lies primarily in

$$
\beta_{g,A}
\quad\text{and}\quad
\beta_{g,B},
$$

not in a new quantum-gravity propagation loss.

## 6.2 The \(25/16\) coefficient is geometry, not new dynamics

It is simply

$$
\boxed{
G_AG_B
=\left(\frac52\right)^2
=\frac{25}{4}}
$$

combined with the standard

$$
(\lambda/4\pi R)^2
$$

path factor.

This further supports the novelty downgrade in

`STORAGE_25_OVER_16_PRIOR_ART_SCOPE.md`.

## 6.3 The quantum part of the link budget is at the interfaces and in noise

The propagation stage is unitary free-field propagation followed by a geometrical/mode projection.

The specifically quantum capability question arises because

- source branch information can leak into nongravitational ports;
- receiver coupling can leak into uncontrolled ports;
- occupied environments add noise;
- the resulting channel may become entanglement breaking.

The antenna propagation factor itself is classical/quantum agnostic.

---

# 7. Relation to the retarded self-energy result

The field-theory/input-output derivation gives

$$
\Sigma_{BA}^R
\simeq
\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{e^{ikR}}{kR}.
$$

Therefore

$$
\left|
\frac{-i\Sigma_{BA}^R}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}
\right|^2
=\frac{25}{16(kR)^2}.
$$

The Friis reconstruction shows that the same dimensionless amplitude has the expected reciprocal-antenna interpretation.

Thus there are now three equivalent views of the same coefficient:

1. retarded Green-function self-energy;
2. source directivity × critical receiver absorption area;
3. reciprocal Friis gain × path factor.

This is a strong normalization consistency check.

---

# 8. Scope

The simple Friis form assumes

- far-field/wave-zone propagation;
- reciprocal source and receiver modes;
- a single selected polarization/tensor channel with normalized overlap;
- no intervening scattering or cavity environment;
- compact antennas relative to the propagation distance.

Near-zone gravitational interaction should continue to be treated through the full retarded Green tensor/self-energy rather than through a Friis interpretation.

Likewise a large distributed receiving array or enclosing collector should be treated through its actual coherent mode overlap rather than by extrapolating the pointlike \(G_B=5/2\) receiver indefinitely.

---

# 9. Manuscript recommendation

The main paper can replace one paragraph of storage-normalization discussion with the compact statement

> For the aligned plus-quadrupole channel, the source directivity is \(G_A=5/2\). The critical \(l=2\) absorptive area corresponds by reciprocity to \(G_B=5/2\). Hence the retarded storage factor is exactly the standard far-field link factor \(G_AG_B(\lambda/4\pi R)^2=25/[16(kR)^2]\), up to residual normalized mode overlap \(\mathcal O\).

This makes the propagation part immediately legible to readers from antenna, scattering, and quantum-network backgrounds without making a novelty claim about the coefficient itself.
