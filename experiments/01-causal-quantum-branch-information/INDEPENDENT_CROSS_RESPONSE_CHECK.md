# Independent Check of the Normalized Quadrupole Cross Response

**Timestamp:** 2026-08-07 17:25 EDT  
**Status:** Independent consistency check of `NORMALIZED_GRAVITATIONAL_CROSS_RESPONSE.md`.

## 1. Result being checked

For two resonant aligned plus quadrupole transitions,

$$
Q_{xx}^{(j)}=q_j,
\qquad
Q_{yy}^{(j)}=-q_j,
$$

with $B$ on the $z$ axis of $A$, the project derived

$$
\Sigma_{AB}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
$$

where

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
\qquad
\epsilon=\omega R/c.
$$

The wave-zone limit is

$$
\Sigma_{AB}^{R}
\simeq
\frac54
\frac{e^{i\epsilon}}{\epsilon}
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
$$

Two independent checks support this normalization.

---

## 2. Check A — Hu et al. resonance interaction

Yongshun Hu, Jiawei Hu, Hongwei Yu, and Puxun Wu,
“Resonance interaction between two entangled gravitational polarizable objects,” *Eur. Phys. J. C* **80**, 792 (2020), arXiv:2001.05116.

They calculate the resonance interaction energy of two entangled gravitationally polarizable objects in linearized quantum gravity.

Their general result has the form

$$
\delta E
=\pm\frac{1}{64\pi R^5}
\sum_{ijkl}
D_{ijkl}(\omega R)
q_A^{ij}q_B^{kl}
$$

in units

$$
\hbar=c=16\pi G=1.
$$

For separation along $z$, their listed tensor components include

$$
D_{1111}
=-x^4\cos x+2x^3\sin x+5x^2\cos x-9x\sin x-9\cos x,
$$

and

$$
D_{1122}
=x^4\cos x-2x^3\sin x-x^2\cos x-3x\sin x-3\cos x.
$$

For aligned plus quadrupoles,

$$
q^{11}=q,
\qquad
q^{22}=-q,
$$

so the contraction is

$$
2(D_{1111}-D_{1122})q_Aq_B.
$$

Direct simplification gives

$$
2(D_{1111}-D_{1122})
=-4\left[
(x^4-3x^2+3)\cos x
+(3x-2x^3)\sin x
\right].
$$

But

$$
\operatorname{Re}[P(x)e^{ix}]
=(x^4-3x^2+3)\cos x
+(3x-2x^3)\sin x.
$$

Therefore their resonance energy reduces to

$$
\delta E
=\mp\frac{q_Aq_B}{16\pi R^5}
\operatorname{Re}[P(x)e^{ix}].
$$

Restoring $16\pi G=1$ gives

$$
\boxed{
\delta E
=\mp\frac{Gq_Aq_B}{R^5}
\operatorname{Re}[P(\epsilon)e^{i\epsilon}].
}
$$

This is exactly the real/dispersive part of the retarded cross coefficient used in the project, up to the branch-state sign convention.

Hu et al. also explicitly report the same asymptotic behavior:

$$
R^{-5}\quad\text{near zone},
$$

and oscillatory

$$
R^{-1}\quad\text{far zone}.
$$

Thus the polynomial and overall interaction normalization are independently reproduced by a vacuum-graviton calculation.

---

## 3. Check B — spontaneous linewidth from classical correspondence

For a plus-type harmonic quadrupole

$$
Q_{xx}(t)=q_0\cos\omega t,
\qquad
Q_{yy}(t)=-q_0\cos\omega t,
$$

the Einstein quadrupole formula gives

$$
P_G
=\frac{G}{5c^5}
\left\langle
\dddot Q_{ij}\dddot Q_{ij}
\right\rangle.
$$

There are two equal STF components, and time averaging gives

$$
\left\langle
\dddot Q_{ij}\dddot Q_{ij}
\right\rangle
=\omega^6q_0^2.
$$

Hence

$$
\boxed{
P_G
=\frac{G\omega^6q_0^2}{5c^5}.
}
$$

Now quantize the quadrupole transition as

$$
\hat q=q_{10}(a+a^\dagger).
$$

For a large coherent state $|\alpha\rangle$, the classical oscillation amplitude is

$$
q_0=2q_{10}|\alpha|.
$$

Therefore classical gravitational power is

$$
P_G
=\frac{4G\omega^6q_{10}^2}{5c^5}|\alpha|^2.
$$

If one quantum is lost at rate $\kappa_g$, a coherent state with occupation $|\alpha|^2$ loses energy at

$$
P_Q=\hbar\omega\kappa_g|\alpha|^2.
$$

Equating the correspondence-limit powers gives

$$
\boxed{
\kappa_g
=\frac{4G\omega^5q_{10}^2}{5\hbar c^5}.
}
$$

Since

$$
Q_{ij}^{10}Q_{ij}^{01}=2q_{10}^2,
$$

this is equivalent to

$$
\boxed{
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

Thus the spontaneous-rate normalization used to express the cross response in units of $\sqrt{\kappa_{g,A}\kappa_{g,B}}$ follows directly from the classical quadrupole formula.

---

## 4. Recover the $5/4$ coefficient

The retarded interaction coefficient is

$$
\Sigma_{AB}^{R}
=\frac{Gq_Aq_B}{\hbar R^5}
P(\epsilon)e^{i\epsilon}.
$$

Using

$$
q_j^2
=\frac{5\hbar c^5}{4G\omega^5}
\kappa_{g,j},
$$

we obtain

$$
\boxed{
\Sigma_{AB}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5}.
}
$$

The coefficient is therefore fixed by independently verified interaction and radiation normalizations.

---

## 5. What remains unverified

The above checks validate

- the exact retarded cross polynomial;
- its interaction normalization;
- the single-system spontaneous linewidth;
- the normalized $5/4$ cross-response coefficient.

The additional identification

$$
\eta_{\rm ff}
=\frac{25}{16(kR)^2}
$$

uses the standard far-zone **one-way cascaded input-output matching**

$$
|\Sigma_{AB}^{R}|
=\sqrt{\eta_{\rm ff}\kappa_{g,A}\kappa_{g,B}}.
$$

That propagation-channel interpretation is physically natural but should still be independently checked against a full common-bath master equation or explicit single-graviton scattering calculation before being called exact.

Thus the $5/4$ retarded Green coefficient is well cross-checked; the $25/16$ transmissivity coefficient remains one layer more model dependent.
