# Gravitational Difference-Mode Amplitude from a Conserved Quadrupole History

**Timestamp:** 2026-08-07 17:12 EDT  
**Status:** Linearized-gravity source mapping using the propagating TT sector.

## 1. Purpose

The exact binary-coherent channel theorem tells us **when** the receiver channel can carry NPT entanglement, but the magnitude of the entanglement/witness depends on the coherent branch separation in the incoming gravitational difference mode.

This note maps a physical branch-dependent quadrupole history onto

$$
N_\Delta
=\|\Delta\alpha\|^2,
$$

the squared phase-space distance between the two outgoing branch-conditioned graviton coherent states.

---

## 2. Exact linearized-gravity displacement

For a conserved semiclassical branch stress tensor $T_b^{\mu\nu}$, the TT graviton field is driven linearly. With the standard linearized-gravity normalization,

$$
\alpha_{b,s}(\mathbf k)
=
\frac{i\kappa}{2\sqrt{2\omega_k}}
\epsilon_{ij}^{s*}(\hat{\mathbf k})
\widetilde T_b^{ij}(\omega_k,\mathbf k),
\qquad
\kappa=\sqrt{32\pi G}
$$

in $\hbar=c=1$ units.

Define

$$
\Delta\alpha_s(\mathbf k)
=\alpha_{L,s}(\mathbf k)-\alpha_{R,s}(\mathbf k).
$$

Then

$$
\boxed{
N_\Delta
=\sum_s\int\frac{d^3k}{(2\pi)^3}
|\Delta\alpha_s(\mathbf k)|^2.
}
$$

This is the mean graviton number of the auxiliary coherent field sourced by the **difference stress tensor** $\Delta T^{\mu\nu}$, equivalently the squared coherent-state distance between the two branch radiation histories.

Vacuum which-path decoherence is

$$
\Gamma_{\rm vac}=N_\Delta/2.
$$

---

## 3. Nonrelativistic quadrupole reduction

For a compact, slowly moving closed source, define the STF mass quadrupole difference

$$
\Delta Q_{ij}(t).
$$

Using stress-energy conservation and the angular TT projection, the radiative difference-mode norm becomes

$$
\boxed{
N_\Delta
=
\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
\Delta\widetilde Q_{ij}(\omega)
\Delta\widetilde Q_{ij}^*(\omega).
}
$$

Equivalently,

$$
\boxed{
\Gamma_{\rm vac}
=
\frac{G}{10\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

This is consistent with the exact linearized-gravity branch-displacement result and with the ordinary quadrupole radiation formula divided mode-by-mode by $\hbar\omega$.

---

## 4. Plus-type quadrupole

For the same branch geometry used throughout Experiment 01,

$$
\Delta Q_{xx}(t)=q(t),
\qquad
\Delta Q_{yy}(t)=-q(t),
$$

with all other components zero,

$$
\Delta Q_{ij}\Delta Q_{ij}^*=2|q|^2.
$$

Therefore

$$
\boxed{
N_\Delta
=
\frac{2G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5|\widetilde q(\omega)|^2.
}
$$

---

## 5. Narrow-band source pulse

Let

$$
q(t)=q_0 f(t)\cos(\omega_0t),
$$

where the real envelope varies slowly compared with $\omega_0^{-1}$ and define

$$
T_f=\int_{-\infty}^{\infty}dt\,|f(t)|^2.
$$

In the narrow-band limit,

$$
\int_0^\infty d\omega\,
|\widetilde q(\omega)|^2
\simeq
\frac{\pi q_0^2}{2}T_f.
$$

Hence

$$
\boxed{
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5}{5\hbar c^5}
T_f.
}
$$

The branch-difference graviton production rate is therefore

$$
\boxed{
\dot N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5}{5\hbar c^5}.
}
$$

This agrees with the classical quadrupole power

$$
P_G=\frac{Gq_0^2\omega_0^6}{5c^5}
$$

divided by the graviton energy $\hbar\omega_0$.

---

## 6. Mapping to the binary coherent theorem

After compressing the outgoing radiation into the normalized difference mode, the two branches can be written as

$$
|\pm a\rangle,
$$

with

$$
\boxed{|a|^2=N_\Delta/4.}
$$

Thus for the narrow-band plus quadrupole,

$$
\boxed{
|a|^2
\simeq
\frac{Gq_0^2\omega_0^5T_f}
{20\hbar c^5}.
}
$$

The exact NPT **sign boundary** of the receiver channel is independent of this quantity as long as $N_\Delta>0$ is finite, but every practical entanglement/witness magnitude scales with it.

---

## 7. Smooth matter-wave trajectory consistency check

For the smooth Gaussian source trajectory studied in recent graviton-decoherence work,

$$
\Gamma_{\rm vac}
=\frac{8}{15}
\frac{Gm^2d^4}{\hbar c^5\tau_s^4}.
$$

Therefore

$$
\boxed{
N_\Delta
=\frac{16}{15}
\frac{Gm^2d^4}{\hbar c^5\tau_s^4},
}
$$

and the equivalent single difference-mode branch amplitude is

$$
\boxed{
|a|^2
=\frac{4}{15}
\frac{Gm^2d^4}{\hbar c^5\tau_s^4}.
}
$$

This makes explicit why radiative branch amplitudes from laboratory matter-wave motion are fantastically small even though the exact NPT threshold is mathematically amplitude independent.

---

## 8. Conceptual consequence

There are now two independent source/receiver quantities:

### Channel quality

$$
\tau-m
$$

or, for the passive gravitational receiver,

$$
\kappa_\Delta-\Gamma_{\rm th}.
$$

This determines whether source-receiver entanglement is possible at all.

### Source branch strength

$$
N_\Delta.
$$

This determines how much branch coherence/entanglement is available to transfer and how strongly any exact witness can be violated.

A larger source cannot make an EB receiver quantum, but once the receiver is non-EB it can increase the measurable quantum signal.

---

## 9. Next step

Insert $N_\Delta$ into the exact three-element witness and derive a **finite-strength certification front**: the earliest time at which the witness violation exceeds a chosen nonzero margin, rather than merely becoming infinitesimally negative.
