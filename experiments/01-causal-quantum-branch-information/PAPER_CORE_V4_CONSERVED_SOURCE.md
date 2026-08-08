# Paper Core V4 — Conserved Quantum Quadrupole Source to Noisy Gravitational Receiver

**Date:** 2026-08-07  
**Status:** Current gravity-paper architecture after adversarial prior-art and source-conservation audits.  
**Novelty:** unverified; generic Gaussian-channel and gravity-as-quantum-channel claims are explicitly excluded from the novelty claim.

## Working title

**Causal Quantum-Channel Transfer from a Conserved Quadrupole Source to a Noisy Gravitational Receiver**

Alternative:

**An Explicit Conserved Source–Field–Receiver Model for Causal Gravitational Quantum Information**

---

## Abstract — working architecture

Whether gravity can mediate entanglement or act as a non-entanglement-breaking quantum channel is already established as a theoretical question. We instead construct an explicit source-resolved benchmark in which the full chain from a conserved branch-dependent mechanical source to a distant noisy quantum receiver can be followed analytically. The source is a finite-mass four-spoke elastic plus mode controlled by an internal two-level system. Its total stress-energy is conserved, its mass dipole vanishes, and the actuator/support contribution to the leading branch quadrupole can be integrated explicitly. If $q=\omega L/c_s$, the branch-difference quadrupole is

$$
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx},
$$

so finite support reinforces rather than cancels the endpoint quadrupole and the endpoint model is recovered as $q\to0$. Quantization gives a corrected gravitational linewidth

$$
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}
{\frac12+q/\sin2q}.
$$

A smooth closed source trajectory emits a normalized branch-dependent graviton mode with coherent distance

$$
N_\Delta
\simeq
\frac72
\frac{G\mu^2L^2u_0^2\omega^5T}
{\hbar c^5}
\left(\frac{\tan q}{q}\right)^2.
$$

Retarded free-space propagation couples that normalized mode to a distant resonant plus-mode receiver. In the wave zone the leading state-storage fraction remains

$$
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2},
$$

while the absolute loading rate uses the receiver's corrected $\kappa_g(q_B)$. The resulting one-mode Gaussian receiver is non-entanglement-breaking precisely when its useful coherent transfer exceeds its vacuum-output occupation. For a fixed emitted waveform this defines a retarded finite capability interval rather than an instantaneous Newtonian interaction. We give explicit error controls for elastic support inertia, finite-source retardation, finite controller extent, and weak self-gravity. The objective is not to re-prove known Gaussian-channel or gravity-mediated-entanglement results, but to exhibit a closed conserved source→field→receiver model in which source preparation, causal propagation, noise, and certification can be placed in one quantitative framework.

---

# 1. Prior-art boundary

Do **not** claim novelty for

- gravity-mediated entanglement;
- local/retarded gravity-mediated entanglement;
- gravity as a quantum-information channel;
- gravitational non-EB channel thresholds;
- coherent-state gravitational channel benchmarks;
- quantum gravitational-wave modes coupled to resonant quantum detectors;
- relativistic sender→receiver no-signalling;
- finite-rank Gaussian EB probes;
- all-finite binary coherent survival through phase-insensitive Gaussian channels.

The Gaussian rank-two and binary-coherent theorem branches were independently rediscovered in this project but collided with prior work. They remain useful lemmas only.

Canonical audit files:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`

The possible paper contribution is the **explicit conserved source-resolved end-to-end construction and its controlled source/receiver scaling**, not the generic channel theory.

---

# 2. Complete conserved source

Use a total stress-energy tensor

$$
T^{\mu\nu}_{\rm tot}
=T^{\mu\nu}_{\rm end}
+T^{\mu\nu}_{\rm spokes}
+T^{\mu\nu}_{\rm hub}
+T^{\mu\nu}_{\rm ctrl}
$$

satisfying

$$
\boxed{\partial_\mu T^{\mu\nu}_{\rm tot}=0.}
$$

Define

$$
I_{ij}(t)
=\frac1{c^2}\int d^3x\,
T^{00}_{\rm tot}(t,\mathbf x)x_ix_j.
$$

For a compact conserved source,

$$
\boxed{
\ddot I_{ij}
=2\int d^3x\,T^{ij}_{\rm tot}.
}
$$

Thus the internal stresses required to accelerate the endpoint masses are already part of the same conserved quadrupole source. Any cancellation must appear in the total $T^{00}$ quadrupole.

---

# 3. Four-spoke plus mode

Use four endpoint masses $\mu$ on four identical longitudinal elastic spokes of reference length $L$.

Define

$$
\boxed{q=\omega L/c_s.}
$$

The exact longitudinal shape normalized to the endpoint displacement is

$$
\boxed{
f_q(x)=\frac{\sin(qx/L)}{\sin q}.}
$$

The endpoint traction condition gives

$$
\boxed{
\frac{m_r}{\mu}=q\tan q.
}
$$

For branch $s=\pm1$,

$$
\xi_x^{(s)}=suf_q(x),
$$

$$
\xi_y^{(s)}=-suf_q(x).
$$

The total branch-difference plus quadrupole is

$$
\boxed{
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
}
$$

$$
\boxed{
\Delta Q_{yy}
=-8\mu Lu\frac{\tan q}{q}.
}
$$

For the endpoint-dominated fundamental mode,

$$
\boxed{
\frac{\tan q}{q}
=1+\frac{q^2}{3}+O(q^4).
}
$$

This is the first source-level result that must appear prominently: the support needed for conservation does not remove the radiative quadrupole.

---

# 4. Mode inertia and quantization

Define

$$
\boxed{
A(q)=\frac12+\frac{q}{\sin2q}.
}
$$

The exact generalized mode mass is

$$
\boxed{
M_{\rm eff}=4\mu A(q).
}
$$

Quantize

$$
u
=u_{\rm zpf}(a+a^\dagger),
$$

with

$$
\boxed{
u_{\rm zpf}
=\sqrt{\frac{\hbar}{2M_{\rm eff}\omega}}.
}
$$

The plus-quadrupole transition matrix element is

$$
\boxed{
q_{01}(q)
=4\mu L\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}\omega}}.
}
$$

The spontaneous gravitational linewidth is

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\mathcal C_\kappa(q),
}
$$

where

$$
\boxed{
\mathcal C_\kappa(q)
=\frac{(\tan q/q)^2}{A(q)}.
}
$$

For $q\ll1$,

$$
\boxed{
\mathcal C_\kappa(q)
=1+\frac{q^2}{3}+\frac{q^4}{9}+O(q^6).
}
$$

---

# 5. Autonomous coherent branch control

Use an internal source qubit and controller coordinate:

$$
\boxed{
H
=H_m(u,p_u)+H_c(q_c,p_c)-\sigma_zg(q_c)u.
}
$$

For branch $s$, the plus coordinate follows the mirrored trajectory

$$
u_s=s u_c.
$$

A controlled mechanical parity transformation

$$
U_P
=|+\rangle\langle+|\otimes I
+|-\rangle\langle-|\otimes P_u
$$

satisfies

$$
\boxed{
U_P^\dagger H U_P
=H_m+H_c-g(q_c)u.
}
$$

Thus the controller/work reservoir can be branch common before gravitational coupling. The branch label need not be copied into an uncontrolled classical actuator record.

---

# 6. Smooth closed source history

Use

$$
\boxed{
u_c(t)
=u_0
\sin^4\left(\frac{\pi t}{T}\right)
\cos\omega t,
\qquad0<t<T.
}
$$

The source returns to the same local phase-space point after the pulse.

For the narrowband mode, the branch quadrupole amplitude is

$$
q_0(q)
=8\mu Lu_0\frac{\tan q}{q}.
$$

The emitted coherent gravitational branch distance is

$$
\boxed{
N_\Delta(q_A)
\simeq
\frac72
\frac{G\mu_A^2L_A^2u_0^2\omega^5T}
{\hbar c^5}
\left(\frac{\tan q_A}{q_A}\right)^2.
}
$$

The same result follows from

$$
N_\Delta
=\kappa_{g,A}(q_A)
\int dt\,|\Delta\alpha_m(t)|^2.
$$

This provides a nontrivial normalization cross-check between the classical conserved quadrupole and quantized input-output descriptions.

---

# 7. Retarded free-space propagation

For source and receiver plus modes, the leading wave-zone retarded cross response is

$$
\boxed{
\Sigma_{AB}^R
\simeq
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_{g,A}\kappa_{g,B}}
}
$$

for ideal tensor alignment.

The normalized storage amplitude is

$$
\boxed{
t_{AB}^{\rm store}
=-i\frac{\Sigma_{AB}^R}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}.
}
$$

Hence

$$
\boxed{
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}
}
$$

at leading quadrupole order.

The finite-spoke quadrupole factors cancel exactly in this normalized ratio.

Read:

- `FINITE_SPOKE_STORAGE_INVARIANCE.md`

---

# 8. Absolute receiver loading

Although the normalized storage fraction is unchanged, the absolute receiver loading rate depends on the receiver linewidth:

$$
\boxed{
\kappa_\Delta(R,q_B)
=\eta_{\rm store}\kappa_{g,B}(q_B).
}
$$

For receiver endpoint mass

$$
M_{e,B}=4\mu_B,
$$

$$
\boxed{
\kappa_\Delta
=
\frac{5\mathcal O}{8}
\frac{GM_{e,B}L_B^2\omega^2}
{c^3R^2}
\mathcal C_\kappa(q_B).
}
$$

At

$$
kR=\zeta,
$$

with

$$
\kappa\simeq\omega/Q_B,
$$

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=
\frac{5\mathcal O}{16\zeta^2}
Q_B\mathcal C_{e,B}\beta_B^3
\mathcal C_\kappa(q_B),
}
$$

where

$$
\mathcal C_{e,B}=\frac{2GM_{e,B}}{c^2L_B},
$$

$$
\beta_B=\frac{\omega L_B}{c}.
$$

The qualitative receiver scaling remains

$$
\boxed{Q\mathcal C\beta^3.}
$$

---

# 9. Fixed-waveform noisy receiver channel

For normalized incoming waveform $f(t)$,

$$
\int_0^\infty|f(t)|^2dt=1,
$$

and receiver equation

$$
\dot c
=-\frac\kappa2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_a\sqrt{\kappa_a}\,b_a^{\rm in},
$$

the coherent transfer parameter is

$$
\boxed{
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
 e^{-\kappa(t-s)/2}f(s)
\right|^2.
}
$$

For initial receiver occupation $n_0$ and thermal injection

$$
\Gamma_{\rm th}
=\sum_a\kappa_a\bar n_a,
$$

$$
\boxed{
m(t)
=n_0e^{-\kappa t}
+\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-\kappa t}).
}
$$

The known phase-insensitive Gaussian EB condition gives

$$
\boxed{
\tau_f(t)>m(t)
}
$$

for the receiver to be non-entanglement-breaking.

No novelty should be claimed for this generic Gaussian condition.

---

# 10. Retarded capability interval

Restore propagation delay:

$$
\boxed{
T_{\rm cap}(R;f)
=\frac Rc
+\inf\{t>0:\tau_f(t)>m(t)\}.
}
$$

For a finite pulse, the receiver can enter and later leave the non-EB region, producing a finite causal capability interval rather than a permanently open channel.

For the normalized $\sin^4$ source mode,

$$
\boxed{
f_4(t)
=\sqrt{\frac{128}{35T}}
\sin^4(\pi t/T),
}
$$

the existing source-specific optimization should be retained, but all absolute loading parameters must use the corrected $\kappa_\Delta(q_B)$.

---

# 11. Certification

The repository's compact Gaussian derivations can be used as certification lemmas without claiming them as discoveries.

For the binary coherent source-replacement state, a selected $2\times2$ PT block gives

$$
|z_v|^2>p_0p_v.
$$

At the matched coherent analysis state the sign boundary coincides with

$$
\tau_f(t)>m(t).
$$

This provides a finite joint witness for the receiver state, but its broad underlying survival theorem is prior art in substance.

The paper should cite the appropriate Gaussian/coherent-state literature and use the finite witness only as a convenient explicit diagnostic.

---

# 12. Source error budget

The source model has independent controlled parameters.

### Elastic support inertia

$$
\boxed{q=\omega L/c_s\ll1.}
$$

Explicit coefficient known:

$$
\mathcal C_\kappa(q)=1+q^2/3+O(q^4).
$$

### Gravitational finite-source retardation

$$
\boxed{\beta=\omega L/c\ll1.}
$$

Inversion symmetry removes the $O(\beta)$ term, so generic field corrections start at

$$
O(\beta^2).
$$

Because

$$
c_s\le c,
$$

$$
q\ge\beta.
$$

Thus $q\ll1$ automatically implies the gravitational compact-source regime.

### Hub/controller contamination

For branch-asymmetric controller energy supported within radius $r_h$,

$$
\boxed{
|\Delta Q^{\rm ctrl}_{ij}|
\le
\frac{r_h^2}{c^2}
E_{\rm TV}^{\rm ctrl}.
}
$$

For the ideal controlled-parity controller,

$$
\Delta T^{00}_{\rm ctrl}=0
$$

and the direct controller quadrupole vanishes.

### Weak self-gravity

$$
\boxed{
\mathcal C=2GM/(c^2L)\ll1.
}
$$

Nonlinear gravitational self-energy corrections are $O(\mathcal C)$.

---

# 13. Conservative final scaling statement

The end-to-end observables should be presented as

$$
\boxed{
\text{observable}
=
\text{leading conserved-source result}
\left[
1+O(q_A^2)+O(q_B^2)
+O(\beta_A^2)+O(\beta_B^2)
+O(\epsilon_Q^{\rm ctrl})
+O(\mathcal C)
\right].
}
$$

The explicit $q^2$ coefficients are known. The finite-size $\beta^2$ coefficients remain optional refinements.

---

# 14. Candidate paper contribution

If novelty survives a dedicated gravity-specific literature audit, the paper should claim only the combination actually constructed here:

> **An explicit conserved branch-dependent quadrupole source, its normalized quantum gravitational output mode, retarded free-space storage into a noisy resonant quantum receiver, and the resulting finite causal non-entanglement-breaking interval, all with source/actuator error controls.**

This is a source-resolved end-to-end benchmark.

It is not a new proof that gravity can mediate entanglement, a new Gaussian EB theorem, or a new general causality principle.

---

# 15. Remaining submission-critical checks

1. Perform a fresh literature audit specifically for **explicit conserved source→quantized gravitational wavepacket→noisy receiver** models, not generic gravity-mediated entanglement.
2. Decide whether the finite-source $O(\beta^2)$ coefficient needs explicit calculation or can remain in the controlled error budget.
3. Verify every downstream numerical coefficient after replacing endpoint-only $\kappa_g$ by $\kappa_g(q)$.
4. Ensure all mass-based compactness parameters specify whether they use endpoint mass, moving mechanical mass, or full source rest mass.
5. Keep the controller/hub error parameter visible in all claimed source normalizations.
6. Only then convert this core into a conventional manuscript with references, figures, and appendices.
