# Canonical Transverse-Traceless One-Graviton Mode-Overlap Audit of the $25/16$ Storage Coefficient

**Date:** 2026-08-08  
**Status:** **THIRD INDEPENDENT NORMALIZATION ROUTE — CANONICAL GRAVITON QUANTIZATION / RECIPROCAL ONE-GRAVITON MODE OVERLAP**

## 1. Purpose

The V7 gravitational link uses the aligned plus-quadrupole wave-zone storage factor

```math
\boxed{
\eta_{\rm store}(R)=\frac{25\mathcal O}{16(kR)^2}.
}
```

This note derives the coefficient without starting from either the retarded source-to-receiver field calculation or the reciprocal absorption-area argument.

The derivation starts from canonical transverse-traceless graviton modes, normalizes the one-graviton angular state of a plus quadrupole, translates that state from source to receiver, and isolates the outgoing causal component.

It reproduces the complete radial polynomial

```math
P(z)=3-3iz-3z^2+2iz^3+z^4,
\qquad z=kR,
```

not only the far-field coefficient.

---

## 2. Canonical graviton normalization

Use the transverse-traceless field convention

```math
h_{ij}(\mathbf x,t)=
\frac{1}{c\sqrt V}
\sum_{\mathbf k,\lambda}
\sqrt{\frac{16\pi G\hbar}{\omega_k}}
\left[
a_{\mathbf k\lambda}
\epsilon^{(\lambda)}_{ij}
 e^{i(\mathbf k\cdot\mathbf x-\omega_k t)}
+\mathrm{h.c.}
\right],
```

with unit-normalized polarizations

```math
\epsilon^{(\lambda)}_{ij}\epsilon^{(\lambda')}_{ij}
=\delta_{\lambda\lambda'}.
```

For a localized quadrupole transition at angular frequency $\omega$, the local-inertial interaction is

```math
H_I=\frac{\omega^2}{4}h_{ij}Q_{ij}.
```

The resulting one-graviton angular emission rate is

```math
\boxed{
\frac{d\kappa_g}{d\Omega}
=\frac{G\omega^5}{4\pi\hbar c^5}
\sum_\lambda
\left|Q_{ij}\epsilon^{(\lambda)}_{ij}\right|^2.
}
```

This fixes the absolute normalization before any source-to-receiver calculation is performed.

---

## 3. Plus-quadrupole angular state

Take

```math
Q_{ij}=q\,\mathrm{diag}(1,-1,0).
```

Here $q$ denotes the quadrupole matrix-element amplitude in this audit; it is unrelated to the elastic parameter $\omega L/c_s$ used elsewhere in V7.

For propagation direction $(\theta,\phi)$, the two transverse-traceless polarization contractions give

```math
\boxed{
Q:\epsilon^+
=\frac{q}{\sqrt2}(1+\cos^2\theta)\cos2\phi,
}
```

```math
\boxed{
Q:\epsilon^\times
=-\sqrt2\,q\cos\theta\sin2\phi.
}
```

Therefore

```math
\sum_\lambda|Q:\epsilon^\lambda|^2
=q^2\mathcal F(\theta,\phi),
```

with

```math
\boxed{
\mathcal F(\theta,\phi)
=2\cos^2\theta
+\frac12\sin^4\theta\cos^22\phi.
}
```

The full-sphere normalization is

```math
\boxed{
\int d\Omega\,\mathcal F=\frac{16\pi}{5}.
}
```

Hence

```math
\boxed{
\kappa_g=\frac{4G\omega^5q^2}{5\hbar c^5}.
}
```

Define the normalized one-graviton angular mode

```math
\boxed{
u_\lambda(\hat{\mathbf n})
=\sqrt{\frac{5}{16\pi}}
\frac{Q:\epsilon^\lambda(\hat{\mathbf n})}{q}.
}
```

Then

```math
\sum_\lambda\int d\Omega\,|u_\lambda|^2=1.
```

The corresponding angular probability density is

```math
\sum_\lambda|u_\lambda|^2
=\frac{5}{16\pi}\mathcal F(\theta,\phi).
```

On the forward axis,

```math
\boxed{
\sum_\lambda|u_\lambda(\hat z)|^2=\frac{5}{8\pi}.
}
```

---

## 4. Reciprocal receiver overlap

Place an identical aligned receiver at

```math
\mathbf R=R\hat z.
```

Emission and absorption are governed by the same Hermitian quadrupole interaction, so the normalized receiver acceptance mode is the reciprocal of the source emission mode.

A plane-wave component translated from source to receiver acquires phase

```math
e^{i\mathbf k\cdot\mathbf R}=e^{iz\mu},
\qquad
z=kR,
\qquad
\mu=\cos\theta.
```

The normalized fixed-frequency overlap is therefore

```math
\boxed{
S(z)=
\sum_\lambda\int d\Omega\,
|u_\lambda(\hat{\mathbf n})|^2e^{iz\mu}.
}
```

After the azimuthal integral,

```math
\boxed{
S(z)=
\frac{5}{32}
\int_{-1}^{1}
(1+6\mu^2+\mu^4)e^{iz\mu}\,d\mu.
}
```

This integral contains no source-to-receiver Green-function normalization and no absorption cross section.

---

## 5. Exact evaluation

Direct integration gives

```math
\boxed{
S(z)=
\frac{5}{4z^5}
\left[
2z^4\sin z
+4z^3\cos z
-6z^2\sin z
-6z\cos z
+6\sin z
\right].
}
```

Writing the trigonometric functions as exponentials gives

```math
S(z)=S_+(z)+S_-(z),
```

where

```math
\boxed{
S_+(z)=
-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5},
}
```

```math
\boxed{
S_-(z)=
+\frac{5i}{4}
\frac{P(-z)e^{-iz}}{z^5},
}
```

and

```math
\boxed{
P(z)=3-3iz-3z^2+2iz^3+z^4.
}
```

The same polynomial appears independently in the retarded electric-Weyl calculation.

---

## 6. Causal outgoing component

With time dependence $e^{-i\omega t}$,

```math
S_+\propto e^{ikR-i\omega t}
=e^{-i\omega(t-R/c)},
```

while

```math
S_-\propto e^{-ikR-i\omega t}
=e^{-i\omega(t+R/c)}.
```

For a source launched at the origin and a receiver observed near positive retarded time $t\simeq R/c$, $S_+$ is the outgoing source-to-receiver component.

Thus

```math
\boxed{
t_{BA}^{\rm TT}(z)=
-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5}.
}
```

The full $S(z)$ is a bounded overlap of normalized fixed-frequency angular states. The separated $S_+$ piece is not itself a normalized channel in the reactive near zone, so $|S_+|^2$ is interpreted as a storage probability only in the weak one-way wave-zone regime used by V7.

---

## 7. Wave-zone coefficient

For $z\gg1$,

```math
P(z)=z^4\left[
1+\frac{2i}{z}
-\frac{3}{z^2}
-\frac{3i}{z^3}
+\frac{3}{z^4}
\right].
```

Therefore

```math
\boxed{
t_{BA}^{\rm TT}(z)
\sim
-\frac{5i}{4}\frac{e^{iz}}{z}.
}
```

Hence

```math
\boxed{
\eta_{\rm store}(R)
\to
\frac{25}{16(kR)^2}.
}
```

Including imperfect temporal, tensor, polarization, or orientation overlap gives

```math
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2},
\qquad
0\le\mathcal O\le1.
}
```

The exact finite-distance probability from the same outgoing amplitude is

```math
\boxed{
|t_{BA}^{\rm TT}|^2=
\frac{25}{16z^2}
\left(
1-\frac{2}{z^2}
+\frac{3}{z^4}
-\frac{9}{z^6}
+\frac{9}{z^8}
\right).
}
```

At $z=10$, the leading $25/(16z^2)$ expression is about $1.97\%$ high.

---

## 8. Stationary-phase check

The forward angular density is

```math
w(+\hat z)=\frac{5}{8\pi}.
```

The outgoing stationary-phase contribution is

```math
S_+(z)
\sim
\frac{2\pi}{iz}w(+\hat z)e^{iz}
=-\frac{5i}{4}\frac{e^{iz}}{z}.
```

This independently reproduces the $5/4$ amplitude coefficient within the same normalized one-graviton picture.

---

## 9. Independence of the three normalization routes

The V7 coefficient is now supported by three conceptually distinct calculations:

1. **Retarded conserved-source field:** normalize the receiver response to the gravitational radiation field generated by the source.
2. **Reciprocal radiation/absorption:** combine the normalized quadrupole radiation pattern with the reciprocal critically coupled receiver area.
3. **Canonical one-graviton overlap:** normalize the emitted one-graviton angular state and translate it directly to the reciprocal receiver mode.

All three give the same wave-zone result

```math
\boxed{
\eta_{\rm store}(R)=\frac{25}{16(kR)^2}
}
```

for ideal alignment, before the residual overlap factor $\mathcal O$ is included.

---

## 10. Verdict

The canonical one-graviton calculation reproduces both the complete radial polynomial and the far-field coefficient without importing either of the previous normalization routes.

```math
\boxed{
\text{canonical graviton mode overlap}
\Longrightarrow
t_{BA}\sim-\frac{5i}{4}\frac{e^{ikR}}{kR}
\Longrightarrow
\eta_{\rm store}\sim\frac{25}{16(kR)^2}.
}
```

This closes the independent-normalization requirement at the stated weak-field, one-way, wave-zone order.
