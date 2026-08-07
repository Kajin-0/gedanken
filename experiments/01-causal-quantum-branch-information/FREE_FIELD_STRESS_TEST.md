# Free-Field Stress Test: Why Spatial Smearing Alone Does Not Give a Relativistic Receiver Ceiling

**Timestamp:** 2026-08-07 16:18 EDT  
**Status:** Active theoretical test for Experiment 01

This note applies the smeared stress-energy response framework to the simplest relativistic receiver: a free scalar quantum field. The result exposes a fundamental difference from the nonrelativistic quadrupole receiver.

---

## 1. Free scalar receiver

Take a free real scalar field in flat spacetime,

$$
H
=\frac12\int d^3x
\left[
\pi^2+(\nabla\phi)^2+m^2\phi^2
\right].
$$

A transverse-traceless gravitational perturbation couples to the anisotropic spatial stress. Choose a fixed STF/TT tensor $e^{ij}$ and a smooth spatial profile $f(\mathbf x)$, and define

$$
\boxed{
F_f
=\int d^3x\,
f(\mathbf x)
e^{ij}T_{ij}(\mathbf x).
}
$$

Because $e^{ij}$ is trace free, the isotropic $\delta_{ij}$ terms in $T_{ij}$ drop out, leaving schematically

$$
F_f
\sim
\int d^3x\,
f(\mathbf x)
e^{ij}\partial_i\phi\partial_j\phi.
$$

---

## 2. Pair-creation matrix element

At $t=0$,

$$
\phi(\mathbf x)
=\int\frac{d^3p}{(2\pi)^3}
\frac{1}{\sqrt{2\omega_p}}
\left(
a_{\mathbf p}e^{i\mathbf p\cdot\mathbf x}
+a_{\mathbf p}^\dagger e^{-i\mathbf p\cdot\mathbf x}
\right),
$$

with

$$
\omega_p=\sqrt{\mathbf p^2+m^2}
$$

in units $c=\hbar=1$ for this section.

The vacuum-to-two-particle matrix element has the structure

$$
\boxed{
\langle\mathbf p,\mathbf q|F_f|0\rangle
\propto
\frac{e^{ij}p_iq_j}
{\sqrt{\omega_p\omega_q}}
\widetilde f(\mathbf p+\mathbf q).
}
$$

The spatial profile therefore suppresses **total momentum**

$$
\mathbf p+\mathbf q,
$$

not the relative momentum.

---

## 3. The ultraviolet loophole

Consider back-to-back excitations,

$$
\mathbf q\simeq-\mathbf p.
$$

Then

$$
\mathbf p+\mathbf q\simeq0,
$$

so

$$
\widetilde f(\mathbf p+\mathbf q)
\simeq\widetilde f(0)
$$

no matter how large $|\mathbf p|$ becomes.

For $|\mathbf p|\gg m$,

$$
\frac{|e^{ij}p_ip_j|}
{\omega_p}
\sim |\mathbf p|.
$$

Thus a spatially smeared stress operator still couples to arbitrarily energetic back-to-back pairs.

This is the key result:

$$
\boxed{
\text{smooth spatial smearing does not by itself impose a UV energy cutoff on stress-energy response.}
}
$$

---

## 4. High-frequency spectral growth

In four spacetime dimensions the stress tensor has scaling dimension four. Correspondingly, zero/spatially-smeared stress-tensor spectral functions have a leading ultraviolet behavior of the form

$$
\boxed{
\chi_f''(\omega)
\sim C_f\,\omega^4
}
$$

up to theory-, tensor-, and smearing-dependent coefficients and subleading terms.

This $\omega^4$ UV behavior is familiar in relativistic stress-tensor spectral functions.

The energy-weighted moment therefore behaves schematically as

$$
\int^{\Lambda}d\omega\,
\omega\chi_f''(\omega)
\sim C_f\Lambda^6.
$$

Hence

$$
\boxed{
\int_0^\infty d\omega\,
\omega\chi_f''(\omega)
}
$$

is not a finite universal number for the ideal continuum field.

Equivalently, the naive equal-time quantity

$$
\langle[F_f,[H,F_f]]\rangle
$$

contains the UV/contact structure of the composite stress tensor and does not provide the simple finite geometric receiver budget obtained in nonrelativistic mechanics.

---

## 5. Why this does not invalidate the spectral framework

The failure is not in passivity.

For a passive state,

$$
\chi_f''(\omega)\ge0
\qquad(\omega>0)
$$

still holds.

What fails is the assumption that the total first spectral moment is finite without an additional physical scale.

Thus:

$$
\boxed{
\text{passivity gives positivity, not a universal finite UV budget in relativistic QFT.}
}
$$

---

## 6. A physical receiver must include time/bandwidth resolution

A real protocol interacts for a finite time with a smooth switching function $g(t)$. Define the spacetime-smeared observable

$$
\boxed{
F_{f,g}
=\int dt\,g(t)
\int d^3x\,f(\mathbf x)
T_{\mu\nu}(t,\mathbf x)e^{\mu\nu}.
}
$$

Its response/noise functionals contain the temporal filter

$$
|\widetilde g(\omega)|^2.
$$

For a smooth compactly supported $g$, $\widetilde g(\omega)$ decays faster than any power, so the filtered quantities

$$
\boxed{
\mathcal R[f,g]
=\int_0^\infty d\omega\,
|\widetilde g(\omega)|^2
\chi_f''(\omega)
}
$$

and the analogous noise functional can be finite even though the unfiltered first moment diverges.

Therefore the relativistic receiver has no protocol-independent oscillator-strength ceiling of the simple nonrelativistic form. Its usable response depends on

- spatial support;
- temporal bandwidth;
- microscopic/QFT structure;
- energy available in the receiver state.

---

## 7. Gaussian temporal resolution example

Take a temporal filter with characteristic duration $\tau$,

$$
|\widetilde g(\omega)|^2
\sim e^{-\omega^2\tau^2}.
$$

If

$$
\chi_f''(\omega)\sim C_f\omega^4,
$$

then the filtered response scales as

$$
\boxed{
\mathcal R[f,g]
\sim C_f\tau^{-5}
}
$$

up to numerical factors.

The energy-weighted filtered moment scales as

$$
\boxed{
\mathcal R_1[f,g]
\sim C_f\tau^{-6}.
}
$$

Shorter temporal resolution therefore opens access to rapidly increasing high-frequency stress-energy oscillator strength.

This is the QFT counterpart of leaving the nonrelativistic regime $\omega L/c\ll1$.

---

## 8. Physical interpretation

The nonrelativistic receiver bound said that a finite mass distribution has only a limited quadrupole oscillator-strength budget at fixed frequency.

The relativistic free field contains arbitrarily high-energy pair excitations. A smooth spatial profile cannot remove them because high relative momentum can coexist with small total momentum.

Therefore a relativistic field-theoretic receiver can evade the **global** nonrelativistic oscillator-strength ceiling, but only by accessing additional high-frequency degrees of freedom.

That does not automatically make it a good receiver for a narrowband source graviton mode. The source still supplies a specific frequency, angular pattern, and temporal wavepacket. Mode matching remains decisive.

---

## 9. Narrowband source rescues a useful bound

Suppose the source branch-difference mode occupies a finite frequency band

$$
\mathcal B
=[\omega_1,\omega_2].
$$

Then only the receiver spectral weight inside that band matters:

$$
\boxed{
\mathcal R_{u,\mathcal B}
=\int_{\omega_1}^{\omega_2}
d\omega\,
W_g(\omega)\chi_u''(\omega).
}
$$

This quantity is finite for a well-defined smeared operator even if the full UV moment diverges.

Thus the correct relativistic question is not

> How much total stress oscillator strength does the receiver possess?

but

> **How much passive stress-energy spectral weight lies in the exact causal graviton mode emitted by the source?**

This returns the problem to the source-mode overlap framework rather than a universal material sum rule.

---

## 10. Consequence for the receiver phase diagram

The nonrelativistic two-resource phase diagram used

$$
\mathfrak R_B
\times
\mathcal O_{SB}.
$$

In relativistic QFT, replace the finite global oscillator-strength variable $\mathfrak R_B$ by a **band-limited source-mode response functional**

$$
\boxed{
\mathfrak R_{u,\mathcal B}
\equiv
\frac{\mathcal R_{u,\mathcal B}}
{\text{receiver decoherence/noise scale}}.
}
$$

The mode-matching and causal-front logic survives, but the compactness ceiling is replaced by a theory- and protocol-dependent spectral ratio.

---

## 11. Novelty discipline

UV growth of stress-tensor spectral functions, composite-operator contact terms, and the need for smearing/renormalization are established QFT facts. In particular, stress-tensor spectral functions are known to carry an $\omega^4$ ultraviolet contribution in four-dimensional relativistic theories.

No novelty is claimed for that behavior.

The important correction to Experiment 01 is conceptual:

$$
\boxed{
\text{the passive compactness ceiling is a nonrelativistic receiver theorem, not a universal QFT theorem.}
}
$$

A relativistic receiver must instead be characterized by its **band-limited stress-energy response in the source-matched graviton mode**.

---

## 12. Immediate next step

Construct the relativistic source-mode figure of merit explicitly:

$$
\mathcal C_u
=
\frac{\text{source-mode absorptive stress spectral weight}}
{\text{complementary + internal noise spectral weight}}.
$$

Then determine whether passivity/KMS conditions impose a universal bound on $\mathcal C_u$ at finite temperature, even though they do not impose a finite UV-integrated oscillator-strength ceiling.