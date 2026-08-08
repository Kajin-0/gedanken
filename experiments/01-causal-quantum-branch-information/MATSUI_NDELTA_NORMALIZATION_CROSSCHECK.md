# Matsui 2026 Cross-Check of the Graviton Difference-Mode Normalization

**Date:** 2026-08-07  
**Status:** **EXTERNAL NORMALIZATION CHECK PASSED — REPOSITORY $N_\Delta$ COEFFICIENT MATCHES MATSUI EXACTLY**

## 1. Purpose

The absolute branch-radiation normalization is load-bearing because it enters

- the branch-conditioned gravitational coherent-state distance;
- radiative which-branch decoherence;
- source-strength estimates;
- finite entanglement / witness amplitudes downstream.

A factor-of-two or polarization-normalization error here would contaminate essentially every absolute source prediction.

Hiroki Matsui, *Graviton-induced which-path decoherence in matter-wave interferometry*, arXiv:2607.20867 (2026), provides an independent conserved-source derivation using the same linearized-gravity problem.

The comparison is exact.

---

## 2. Field and polarization conventions

Matsui uses

$$
\kappa=\sqrt{32\pi G}
$$

in $\hbar=c=1$ units and the TT interaction

$$
H_{\rm int}(t)
=-\frac{\kappa}{2}
\int d^3x\,
\hat h^{TT}_{ij}(t,\mathbf x)
T^{ij}(t,\mathbf x).
$$

The graviton mode expansion uses polarization tensors normalized as

$$
\boxed{
\epsilon^s_{ij}\epsilon^{s'*}_{ij}
=\delta_{ss'}.
}
$$

The repository uses the same unit-normalized polarization convention.

For source branch $b$, Matsui obtains

$$
\boxed{
\alpha_{b,s}(\mathbf k)
=
\frac{i\kappa}{2\sqrt{2\omega_k}}
\epsilon^{s*}_{ij}(\hat{\mathbf k})
\widetilde T_b^{ij}(\omega_k,\mathbf k).
}
$$

This is exactly the starting expression in

- `GRAVITATIONAL_DIFFERENCE_MODE_AMPLITUDE.md`.

No convention conversion is required.

---

## 3. Difference displacement

Define

$$
\Delta\alpha_s(\mathbf k)
=\alpha_{1,s}(\mathbf k)-\alpha_{2,s}(\mathbf k).
$$

Both Matsui and the repository define

$$
\boxed{
N_\Delta
=\sum_s\int\frac{d^3k}{(2\pi)^3}
|\Delta\alpha_s(\mathbf k)|^2.
}
$$

Matsui explicitly identifies this as

1. the mean graviton number of the auxiliary coherent field sourced by the difference stress tensor $\Delta T^{\mu\nu}$; and
2. the squared phase-space distance between the two branch-conditioned radiation states.

Therefore the repository's normalized one-mode compression is a reduction of this already-standard multimode norm, not a new underlying radiation principle.

---

## 4. Vacuum decoherence

For vacuum gravitons,

$$
\langle0|D[\Delta\alpha]|0\rangle
=\exp(-N_\Delta/2).
$$

Matsui therefore obtains

$$
\boxed{
\Gamma_{\rm vac}=\frac12N_\Delta.
}
$$

This is exactly the relation used in the repository.

---

## 5. Quadrupole reduction

For a compact slowly moving **complete conserved source**, Matsui defines the STF quadrupole $Q_{ij}$ and uses

$$
\int d^3x\,T^{ij}
=\frac12\ddot I^{ij}.
$$

With the same Fourier convention as the repository,

$$
\widetilde f(\omega)
=\int dt\,e^{i\omega t}f(t),
$$

Matsui derives

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

Therefore

$$
\boxed{
\frac{dN_\Delta}{d\omega}
=
\frac{G}{5\pi\hbar c^5}
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

Integrating,

$$
\boxed{
N_\Delta
=
\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

This is **identical** to the repository formula.

There is no factor-of-two, factor-of-four, positive/negative-frequency, or polarization-normalization mismatch.

---

## 6. Plus quadrupole

For

$$
\Delta Q_{xx}=q(t),
\qquad
\Delta Q_{yy}=-q(t),
$$

with all other components zero,

$$
|\Delta\widetilde Q_{ij}|^2
=2|\widetilde q|^2.
$$

Hence

$$
\boxed{
N_\Delta
=
\frac{2G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5|\widetilde q(\omega)|^2.
}
$$

This matches `GRAVITATIONAL_DIFFERENCE_MODE_AMPLITUDE.md` exactly.

---

## 7. Narrowband pulse cross-check

Let

$$
q(t)=q_0f(t)\cos\omega_0t,
$$

with slowly varying real envelope and

$$
T_f=\int dt\,|f(t)|^2.
$$

For a narrowband positive-frequency lobe,

$$
\int_0^\infty d\omega\,
|\widetilde q(\omega)|^2
\simeq
\frac{\pi q_0^2}{2}T_f.
$$

Therefore

$$
\boxed{
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5}{5\hbar c^5}T_f.
}
$$

Again this is exactly the repository coefficient.

The corresponding diagnostic difference-source energy is

$$
E_\Delta
\simeq
\hbar\omega_0N_\Delta,
$$

consistent with the Einstein quadrupole power normalization.

---

## 8. Symmetric one-mode branch amplitude

Compress the multimode displacement difference into one normalized bosonic mode and represent the two branch radiation states as

$$
|+a\rangle,
\qquad
|-a\rangle.
$$

Their phase-space separation is

$$
|(+a)-(-a)|^2=4|a|^2.
$$

Therefore

$$
\boxed{|a|^2=N_\Delta/4.}
$$

This is a geometric identity, not a separate gravitational normalization assumption.

---

## 9. Important source-model distinction

Matsui states explicitly that the quadrupole reduction applies to the **complete conserved matter–apparatus source**.

However, for the numerical matter-wave estimate, the paper then neglects setup-dependent branch contributions from the apparatus and keeps only the matter quadrupole, aside from a recoil estimate.

This is exactly where the current repository source construction goes beyond that treatment.

Experiment 01 now supplies an explicit finite-mass mechanical conservation completion:

- four endpoint masses;
- four elastic spokes;
- central hub/controller sector;
- exact finite-spoke normal mode;
- explicit support rest-mass contribution to the branch quadrupole;
- compact controller residual bound.

For that architecture,

$$
\boxed{
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
}
$$

and the support contribution reinforces rather than cancels the endpoint term.

Thus the external Matsui comparison does two things simultaneously:

1. **validates the repository's $N_\Delta$ normalization**;
2. **sharpens the possible source-level contribution** to the explicit treatment of the apparatus stress-energy that the generic conserved-source formula requires but source estimates often leave setup dependent.

---

## 10. Novelty consequence

Do not claim as new

- $N_\Delta$ as the graviton difference displacement norm;
- $\Gamma_{\rm vac}=N_\Delta/2$;
- the quadrupole spectral formula for $N_\Delta$;
- closed conserved branch histories driving coherent graviton displacements.

A defensible source-specific claim, subject to further literature audit, is instead:

> an explicit finite-mass elastic source-plus-support architecture for which the complete conserved branch quadrupole can be calculated analytically and shown not to be canceled by the actuator/support completion.

---

## 11. Audit verdict

### Normalization

$$
\boxed{\text{PASS}}
$$

The repository coefficient

$$
\boxed{
N_\Delta
=
\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}|^2
}
$$

matches Matsui 2026 exactly under the same Fourier and polarization conventions.

### Novelty

$$
\boxed{\text{NARROWED}}
$$

The branch-difference graviton formalism is prior art. The explicit apparatus/conservation completion remains the stronger project-specific candidate.

---

## Primary comparison source

H. Matsui, *Graviton-induced which-path decoherence in matter-wave interferometry*, arXiv:2607.20867 (2026), especially Eqs. (17), (27), (31)–(40) and the discussion following Eq. (40).
