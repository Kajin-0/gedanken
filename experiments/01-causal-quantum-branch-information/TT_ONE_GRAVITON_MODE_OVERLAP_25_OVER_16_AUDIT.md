# Canonical TT One-Graviton Mode-Overlap Audit of the $25/16$ Storage Coefficient

**Date:** 2026-08-08  
**Status:** **THIRD INDEPENDENT NORMALIZATION ROUTE — CANONICAL TT QUANTIZATION / RECIPROCAL ONE-GRAVITON MODE OVERLAP**

## 1. Purpose

The V7 gravitational link uses the aligned plus-quadrupole wave-zone storage factor

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2}.
}
$$

Because normalization is one of the paper's main contributions, this coefficient should survive a derivation that does **not** begin from either

1. the previously derived retarded source--receiver self-energy/cross response; or
2. the critical-coupling/Friis absorption-area argument.

This note supplies that third route.

The calculation starts directly from

- canonical TT plane-wave quantization;
- the one-graviton angular emission mode of a plus quadrupole;
- microscopic emission/absorption reciprocity;
- translation of that normalized one-graviton mode from source to receiver.

No gravitational Green-function self-energy and no absorption cross section are used as inputs.

The result is stronger than a far-zone coefficient check: the causal outgoing part of the translated TT mode overlap reproduces the complete polynomial

$$
P(z)=3-3iz-3z^2+2iz^3+z^4
$$

that appeared independently in the retarded field calculation.

---

# 2. Canonical TT normalization

A convenient normalization is the one used by Boughn and Rothman, *Class. Quantum Grav.* **23**, 5839 (2006), arXiv:gr-qc/0605052.

They box-normalize the linearized TT field as

$$
h_{ij}(\mathbf x,t)
=\frac{1}{c\sqrt V}
\sum_{\mathbf k,\lambda}
\sqrt{\frac{16\pi G\hbar}{\omega_k}}
\left[
 a_{\mathbf k\lambda}
 \epsilon^{(\lambda)}_{ij}(\hat{\mathbf k})
 e^{i(\mathbf k\cdot\mathbf x-\omega_k t)}
+\text{h.c.}
\right],
$$

with

$$
\epsilon^{(\lambda)}_{ij}
\epsilon^{(\lambda')}_{ij}
=\delta_{\lambda\lambda'}.
$$

The same field-theoretic treatment uses the gauge-safe local-inertial quadrupole interaction. For a localized transition quadrupole $Q_{ij}$ at resonant frequency $\omega$,

$$
H_I
=\frac{\omega^2}{4}h_{ij}Q_{ij}
$$

for the transition matrix element, with the trace part irrelevant because the TT polarization is traceless.

For emission of one graviton into $(\hat{\mathbf n},\lambda)$,

$$
|M_\lambda|^2
=
\frac{\pi G\hbar\omega^3}{c^2V}
\left|
Q_{ij}\epsilon^{(\lambda)}_{ij}(\hat{\mathbf n})
\right|^2.
$$

The box-normalized density of one-graviton states per solid angle and per energy is

$$
\rho_E
=\frac{V\omega^2}{(2\pi)^3\hbar c^3}.
$$

Fermi's golden rule therefore gives

$$
\boxed{
\frac{d\kappa_g}{d\Omega}
=\frac{G\omega^5}{4\pi\hbar c^5}
\sum_\lambda
\left|
Q_{ij}\epsilon^{(\lambda)}_{ij}
\right|^2.
}
$$

This absolute normalization is fixed before the source--receiver calculation begins.

---

# 3. Plus-quadrupole one-graviton angular mode

Take

$$
Q_{ij}
=q\,\operatorname{diag}(1,-1,0).
$$

For propagation direction

$$
\hat{\mathbf n}
=(\sin\theta\cos\phi,
  \sin\theta\sin\phi,
  \cos\theta),
$$

define the orthonormal transverse vectors

$$
\mathbf e_\theta
=(\cos\theta\cos\phi,
  \cos\theta\sin\phi,
 -\sin\theta),
$$

$$
\mathbf e_\phi
=(-\sin\phi,\cos\phi,0).
$$

Use unit-normalized TT polarizations

$$
\epsilon^+
=\frac{1}{\sqrt2}
(\mathbf e_\theta\mathbf e_\theta
-\mathbf e_\phi\mathbf e_\phi),
$$

$$
\epsilon^\times
=\frac{1}{\sqrt2}
(\mathbf e_\theta\mathbf e_\phi
+\mathbf e_\phi\mathbf e_\theta).
$$

Their contractions with the plus quadrupole are

$$
\boxed{
Q:\epsilon^+
=\frac{q}{\sqrt2}
(1+\cos^2\theta)\cos2\phi,
}
$$

$$
\boxed{
Q:\epsilon^\times
=-\sqrt2\,q\cos\theta\sin2\phi.
}
$$

Therefore

$$
\sum_\lambda|Q:\epsilon^\lambda|^2
=q^2\mathcal F(\theta,\phi),
$$

where

$$
\boxed{
\mathcal F(\theta,\phi)
=2\cos^2\theta
+\frac12\sin^4\theta\cos^22\phi.
}
$$

The full-sphere integral is

$$
\boxed{
\int d\Omega\,\mathcal F
=\frac{16\pi}{5}.
}
$$

Hence the total spontaneous graviton linewidth is

$$
\kappa_g
=\frac{G\omega^5}{4\pi\hbar c^5}
q^2\frac{16\pi}{5},
$$

or

$$
\boxed{
\kappa_g
=\frac{4G\omega^5q^2}{5\hbar c^5},
}
$$

exactly the plus-mode linewidth normalization used throughout V7.

Now define the **normalized one-graviton angular emission mode**

$$
\boxed{
u_\lambda(\hat{\mathbf n})
=\sqrt{\frac{5}{16\pi}}
\frac{Q:\epsilon^\lambda(\hat{\mathbf n})}{q}.
}
$$

Then

$$
\sum_\lambda\int d\Omega\,
|u_\lambda|^2=1.
$$

The corresponding normalized angular probability density is

$$
\boxed{
\sum_\lambda|u_\lambda|^2
=\frac{5}{16\pi}\mathcal F(\theta,\phi).
}
$$

On the $+z$ axis,

$$
\mathcal F(0,\phi)=2,
$$

so

$$
\boxed{
\sum_\lambda|u_\lambda(\hat z)|^2
=\frac{5}{8\pi}.
}
$$

This value has been obtained here directly from the normalized quantum emission mode, not from a classical antenna gain.

---

# 4. Reciprocal receiver mode

Take an identical aligned plus receiver $B$ centered at

$$
\mathbf R=R\hat z.
$$

The same Hermitian quadrupole interaction that produces spontaneous emission also governs absorption. Therefore, after normalization by the receiver's intrinsic gravitational linewidth, its reciprocal one-graviton acceptance mode has the same angular tensor amplitude $u_\lambda$ up to complex conjugation and an irrelevant overall phase.

A plane-wave component translated from the source origin to the receiver acquires

$$
e^{i\mathbf k\cdot\mathbf R}
=e^{iz\mu},
$$

where

$$
z=kR,
\qquad
\mu=\cos\theta.
$$

Thus the normalized fixed-frequency source/receiver spatial mode overlap is

$$
\boxed{
S(z)
=\sum_\lambda\int d\Omega\,
|u_\lambda(\hat{\mathbf n})|^2
 e^{iz\mu}.
}
$$

Substituting the plus-mode pattern,

$$
S(z)
=\frac{5}{16\pi}
\int d\Omega\,
\mathcal F(\theta,\phi)e^{iz\cos\theta}.
$$

The azimuthal integral is elementary:

$$
\int_0^{2\pi}d\phi\,\mathcal F
=\frac{\pi}{2}
\left(1+6\mu^2+\mu^4\right).
$$

Therefore

$$
\boxed{
S(z)
=\frac{5}{32}
\int_{-1}^{1}d\mu\,
(1+6\mu^2+\mu^4)e^{iz\mu}.
}
$$

This is the central integral of the independent audit.

---

# 5. Exact evaluation

Direct integration gives

$$
\boxed{
S(z)
=\frac{5}{4z^5}
\left[
2z^4\sin z
+4z^3\cos z
-6z^2\sin z
-6z\cos z
+6\sin z
\right].
}
$$

The result is real because this full fixed-frequency overlap contains both propagation directions.

Rewrite the trigonometric functions as exponentials. Then

$$
\boxed{
S(z)=S_+(z)+S_-(z),
}
$$

with

$$
\boxed{
S_+(z)
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5},
}
$$

$$
\boxed{
S_-(z)
=+\frac{5i}{4}
\frac{P(-z)e^{-iz}}{z^5},
}
$$

where

$$
\boxed{
P(z)=3-3iz-3z^2+2iz^3+z^4.
}
$$

This polynomial was **not inserted** into the calculation. It emerged from the translated normalized TT one-graviton mode.

It is exactly the same polynomial obtained independently from the retarded electric-Weyl/Green-function calculation in `NORMALIZED_GRAVITATIONAL_CROSS_RESPONSE.md`.

---

# 6. Why $S_+$ is the retarded source-to-receiver amplitude

A physical emitted wavepacket contains a radial frequency envelope $\xi(\omega)$ and time dependence

$$
e^{-i\omega t}.
$$

The two pieces above therefore carry phases

$$
S_+:
\qquad
 e^{ikR-i\omega t}
=e^{-i\omega(t-R/c)},
$$

and

$$
S_-:
\qquad
 e^{-ikR-i\omega t}
=e^{-i\omega(t+R/c)}.
$$

For a source launched at the origin and a receiver observed at positive retarded time near

$$
t=R/c,
$$

the first term is the outgoing source-to-receiver component. The second is the time-reversed/advanced component of the full fixed-frequency standing-wave overlap.

Thus the normalized causal one-way TT transfer amplitude is

$$
\boxed{
t_{BA}^{\rm TT}(z)
=S_+(z)
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5}.
}
$$

This identification is made through wavepacket time direction, not by importing a retarded Green function.

A useful subtlety follows. The **full** overlap $S(z)$ is a bounded overlap of two normalized fixed-frequency angular states. The separated outgoing component $S_+$ can become large in the near zone because the outgoing/advanced decomposition is not a decomposition into orthogonal normalized channels there. Consequently $|S_+|^2$ should not be interpreted as a single-pass storage probability in the reactive near zone.

The storage interpretation is the weak one-way wave-zone limit used by V7.

---

# 7. Wave-zone limit and the $25/16$ coefficient

For

$$
z=kR\gg1,
$$

$$
P(z)
=z^4\left[
1+\frac{2i}{z}
-\frac{3}{z^2}
-\frac{3i}{z^3}
+\frac{3}{z^4}
\right].
$$

Hence

$$
\boxed{
t_{BA}^{\rm TT}(z)
=-\frac{5i}{4}
\frac{e^{iz}}{z}
\left[1+O(z^{-1})\right].
}
$$

Therefore the weak one-way coherent storage probability is

$$
\boxed{
\eta_{\rm store}(R)
=|t_{BA}^{\rm TT}|^2
=\frac{25}{16(kR)^2}
\left[1+O((kR)^{-1})\right].
}
$$

At leading wave-zone order,

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25}{16(kR)^2}.
}
$$

Residual temporal, polarization, tensor, and orientation mismatch is represented as usual by

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2},
\qquad
0\le\mathcal O\le1.
}
$$

---

# 8. Stationary-phase interpretation

The leading coefficient can also be read directly from the same normalized TT mode.

At positive retarded time, the far-zone angular integral is dominated by the north-pole stationary point

$$
\hat{\mathbf n}=+\hat z.
$$

For a smooth normalized angular density $w(\hat{\mathbf n})$,

$$
\int d\Omega\,
w(\hat{\mathbf n})e^{iz\cos\theta}
\sim
\frac{2\pi}{iz}
w(+\hat z)e^{iz}
$$

for the outgoing contribution.

Here

$$
w(+\hat z)
=\frac{5}{8\pi}.
$$

Therefore

$$
\boxed{
S_+(z)
\sim
\frac{2\pi}{iz}
\frac{5}{8\pi}e^{iz}
=-\frac{5i}{4}
\frac{e^{iz}}{z}.
}
$$

This gives the $5/4$ amplitude coefficient without any cross-section argument.

---

# 9. Independence from the previous two routes

The three principal normalization routes are now:

## Route A — retarded conserved-source field

`NORMALIZED_GRAVITATIONAL_CROSS_RESPONSE.md`

Starts from the retarded electric-Weyl field and the receiver tidal Hamiltonian, then normalizes by spontaneous graviton linewidths.

Result:

$$
t_{BA}
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5}.
$$

## Route B — power flow / critical absorption / Friis

`STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`

Starts from the normalized quadrupole radiation pattern and the independent critical-coupling $l=2$ absorption area.

Result:

$$
\eta_{\rm store}
=\frac{25}{16z^2}.
$$

## Route C — canonical TT one-graviton mode overlap

**This note.**

Starts from canonical TT quantization and the normalized one-graviton emission/absorption mode, translates that mode to the receiver, and isolates the positive-retarded-time component.

Result:

$$
\boxed{
t_{BA}^{\rm TT}
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5},
}
$$

and hence

$$
\boxed{
\eta_{\rm store}
\to\frac{25}{16z^2}.
}
$$

Route C neither assumes the retarded source--receiver self-energy nor a resonant absorption cross section.

---

# 10. Primary-source normalization anchor

The canonical TT normalization and one-graviton golden-rule construction used above are consistent with

Stephen Boughn and Tony Rothman,
**“Aspects of Graviton Detection: Graviton Emission and Absorption by Atomic Hydrogen,”**
*Classical and Quantum Gravity* **23**, 5839--5852 (2006),
arXiv:gr-qc/0605052,
DOI: 10.1088/0264-9381/23/20/006.

Their field-theoretic calculation explicitly provides

- box-normalized TT plane-wave quantization;
- polarization normalization;
- the local-inertial quadrupole interaction;
- one-graviton density of states;
- differential spontaneous-emission rate;
- agreement of the resulting total rate with the classical quadrupole formula.

That source is particularly useful here because it discusses the gauge subtleties of naively using the linearized interaction Hamiltonian and verifies the rate in a local-inertial formulation.

---

# 11. Referee-level verdict

The reviewer's requested third independent check is now available:

$$
\boxed{
\text{canonical TT quantization}
\to
\text{normalized one-graviton angular mode}
\to
\text{translated reciprocal receiver mode}
\to
\frac{5}{4kR}
\to
\frac{25}{16(kR)^2}.
}
$$

More strongly, the TT overlap independently regenerates

$$
\boxed{
P(z)=3-3iz-3z^2+2iz^3+z^4,
}
$$

which is the complete retarded radial polynomial previously obtained from the gravitational field calculation.

Within the narrowband linearized-gravity conventions of V7, the $25/16$ normalization vulnerability should therefore be regarded as **closed at the same working order as the manuscript**.
