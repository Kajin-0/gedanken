# Planckian Bandwidth and Gravitational Quantum Loading Time

**Timestamp:** 2026-08-07 18:00 EDT  
**Status:** Consequence of combining the bound-state Planck-area absorption relation with the resonant storage picture. Intended as a scaling/normalization bridge, not yet a universal theorem for all possible relativistic receivers.

## 1. Exact convention-level reconciliation

Palessandro & Sloth's bound-state QFT calculation gives, in $c=1$ units,

$$
\boxed{
\sigma_{\rm GR}
=\frac{\Gamma_g}{\omega^3},
}
$$

with

$$
\sigma_{\rm GR}
=\tilde\kappa\ell_P^2.
$$

For the aligned $l=2$ critical-coupling absorption/storage line used in Experiment 01,

$$
\boxed{
\sigma_{\rm peak}
=\frac{5\pi}{2\omega^2}
}
$$

in the same $c=1$ convention.

Therefore

$$
\boxed{
\sigma_{\rm GR}
=
\frac{2}{5\pi}
\sigma_{\rm peak}
\frac{\Gamma_g}{\omega}.
}
$$

Thus the Planck-area Golden-Rule/frequency-averaged strength is directly proportional to

$$
\boxed{
\text{peak resonant area}
\times
\text{fractional gravitational linewidth}.
}
$$

The coefficient $2/(5\pi)$ is specific to the aligned one-channel $l=2$ peak-area convention used here; the time-bandwidth interpretation is the robust point.

---

## 2. Fractional linewidth

Since

$$
\frac{\Gamma_g}{\omega^3}
=\tilde\kappa\ell_P^2,
$$

we have

$$
\boxed{
\frac{\Gamma_g}{\omega}
=\tilde\kappa(\omega\ell_P)^2
}
$$

in $c=1$ units, or

$$
\boxed{
\frac{\Gamma_g}{\omega}
=\tilde\kappa(k\ell_P)^2
}
$$

with

$$
k=\omega/c.
$$

Therefore the quality factor associated with gravitational radiation alone is

$$
\boxed{
Q_g
\equiv
\frac{\omega}{\Gamma_g}
\sim
\frac1{\tilde\kappa(k\ell_P)^2}.
}
$$

At laboratory wavelengths this number is enormous.

---

## 3. Minimum coherent loading time

A time-reversed spontaneous-emission wavepacket that coherently loads the gravitational transition has characteristic bandwidth

$$
\Delta\omega\sim\Gamma_g
$$

and therefore characteristic duration

$$
\boxed{
T_{\rm load}
\sim\Gamma_g^{-1}.
}
$$

Using the Planckian linewidth,

$$
\boxed{
T_{\rm load}
\sim
\frac1{\tilde\kappa\omega(k\ell_P)^2}.
}
$$

Equivalently,

$$
\boxed{
\omega T_{\rm load}
\sim
\frac1{\tilde\kappa(k\ell_P)^2}.
}
$$

The receiver must remain phase coherent for approximately

$$
N_{\rm cyc}\sim Q_g
$$

carrier cycles to exploit the wavelength-scale resonant storage area.

---

## 4. Numerical scale

Take $\tilde\kappa=1$ only as an order-unity illustration.

### $f=1\,\mathrm{kHz}$

$$
k\simeq2.10\times10^{-5}\,\mathrm{m^{-1}},
$$

$$
(k\ell_P)^2\simeq1.15\times10^{-79}.
$$

Then

$$
\boxed{
\Gamma_g
\sim7\times10^{-76}\,\mathrm{s^{-1}},
}
$$

and

$$
\boxed{
T_{\rm load}
\sim10^{75}\,\mathrm s.
}
$$

### $f=1\,\mathrm{GHz}$

$$
k\simeq20.96\,\mathrm{m^{-1}},
$$

$$
(k\ell_P)^2\simeq1.15\times10^{-67}.
$$

Then

$$
\boxed{
\Gamma_g
\sim7\times10^{-58}\,\mathrm{s^{-1}},
}
$$

and

$$
\boxed{
T_{\rm load}
\sim10^{57}\,\mathrm s.
}
$$

The exact coefficient depends on the bound-state matrix element through $\tilde\kappa$, but no order-unity factor changes the conclusion.

---

## 5. Connection to the source-receiver entanglement rate

For a cold pure-loss receiver with very small total coherent storage fraction $\eta_Q$, the optimized source-cat negativity obeys

$$
\mathcal N_{\max}
\simeq\eta_Q.
$$

For a perfectly source-mode-matched receiver being loaded from zero at short times,

$$
\eta_Q(t)
\simeq
\beta_{\rm prop}\Gamma_g t,
$$

where $\beta_{\rm prop}\le1$ is the free-space source-to-receiver propagation/mode factor.

Therefore

$$
\boxed{
\mathcal N_{\max}(t)
\lesssim
\beta_{\rm prop}\Gamma_g t
}
$$

in the initial weak-capture regime.

To reach a target small negativity $\mathcal N_*$ therefore requires at least

$$
\boxed{
t_*
\gtrsim
\frac{\mathcal N_*}
{\beta_{\rm prop}\Gamma_g}.
}
$$

For a gravity-dominated bound receiver,

$$
\boxed{
t_*
\gtrsim
\frac{\mathcal N_*}
{\beta_{\rm prop}\tilde\kappa\omega(k\ell_P)^2}.
}
$$

This is a **Planckian quantum-loading latency**: the wavelength-scale peak cross section cannot be exploited quickly because the oscillator strength is concentrated into an ultra-narrow line.

---

## 6. Far-zone source penalty

For the aligned resonant source-receiver geometry,

$$
\beta_{\rm prop}(R)
\simeq
\frac{25\mathcal O}{16(kR)^2}
$$

in the wave zone.

Thus, for small target entanglement,

$$
\boxed{
 t_*(R)
\gtrsim
\frac{16(kR)^2}{25\mathcal O}
\frac{\mathcal N_*}{\Gamma_g}.
}
$$

At the wave-zone edge $kR\sim O(1)$, the dominant difficulty is still the minute gravitational linewidth itself. Farther away an additional $R^2$ propagation penalty appears.

---

## 7. Why a large peak cross section is not paradoxical

A resonance can have a large peak cross section even when its coupling constant is tiny because the same tiny coupling makes the resonance extraordinarily narrow and long lived.

This is familiar from weakly coupled resonant scattering generally:

$$
\boxed{
\text{weak coupling}
\Rightarrow
\text{narrow line}
\Rightarrow
\text{large coherent build-up time}.
}
$$

The gravitational case is extreme because the fractional linewidth is Planck suppressed.

The receiver can, in principle, accumulate a coherent amplitude over an enormous number of cycles and reach a unitarity/critical-coupling peak cross section. But a broadband graviton or a finite-duration experiment sees the tiny integrated oscillator strength instead.

---

## 8. Relation to the passive nonrelativistic receiver bound

The Planckian bound-state result and the nonrelativistic passive sum-rule result describe different receiver classes.

### Bound-state Planckian scaling

For the bound systems treated in the Planck-area literature,

$$
\Gamma_g/\omega
\sim(k\ell_P)^2.
$$

### Generic passive nonrelativistic material receiver

The project derived the broader ceiling

$$
\frac{\kappa_g}{\omega}
\le
\frac23\mathcal C_B\beta_B^3.
$$

Electromagnetic/material binding can therefore produce gravitational oscillator strengths parametrically different from a purely gravitational atom. The Planck-area relation should not be imposed universally on all material resonators.

The common lesson is the same:

> **The relevant figure is not peak cross section alone, but peak area together with linewidth/loading time.**

---

## 9. Consequence for exotic receiver loopholes

A proposed relativistic or gravity-only receiver should now be evaluated using at least two independent quantities:

1. peak source-mode absorption/storage cross section;
2. gravitational linewidth or equivalent coherent loading time.

A large peak area is not enough if

$$
\Gamma_g/\omega\ll1.
$$

The strongest exotic-receiver question becomes:

> **Can any passive relativistic receiver simultaneously obtain a large gravitational branching ratio and a non-Planck-suppressed bandwidth?**

That is more precise than asking only whether it can have a large graviton absorption cross section.

---

## 10. Next strongest path

1. Search for relativistic/passive systems with parametrically larger $\Gamma_g/\omega$ than $(k\ell_P)^2$ while retaining gravitational branching ratio near unity.
2. Derive a covariant or KMS-based bound on the product
   $$
   \sigma_{\rm peak}\,\Gamma_g/\omega
   $$
   for general passive stress-energy receivers.
3. Use that result to decide whether the passive vacuum entanglement ceiling can be extended beyond the nonrelativistic receiver class.
