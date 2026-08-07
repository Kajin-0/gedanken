# Current State — Experiment 01

**Last updated:** 2026-08-07 18:00 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the canonical compact recovery point. Detailed derivations, corrections, novelty checks, and numerical audits are preserved in the experiment directory and timestamped `checkpoints/`.

---

## 1. Central question

Can gravity carry information about a coherent source alternative to a distant quantum receiver **causally**, while preserving enough coherence that source and receiver become entangled rather than merely classically correlated?

The operational source-receiver state is

$$
\rho_{AB}
=\begin{pmatrix}
p\rho_L&\Xi\\
\Xi^\dagger&(1-p)\rho_R
\end{pmatrix}.
$$

The off-diagonal block $\Xi$ is the conditional-history coherence. For pure conditional global histories,

$$
\|\Xi\|_1=F(\rho_E^L,\rho_E^R),
$$

so it measures how indistinguishable the unobserved complementary branch records remain.

Do not formulate the final paper by assuming a fundamental source–gravity–receiver tensor factorization; gravitational dressing/gauge constraints make that split nontrivial. Keep the final statements operational in source/receiver channel variables.

---

## 2. Causal hierarchy

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

The current hierarchy is

1. **signal front** — first causal gravitational response;
2. **internal NPT front** — first entanglement between source and gravitationally active receiver mode;
3. **exact matched-witness front**;
4. **finite-certification front**;
5. **accessible NPT front** — first entanglement between source and a controllable/readable output register.

Thus

$$
\boxed{
R/c
\neq
\text{quantum build time}
\neq
\text{accessible quantum readout time}.
}
$$

---

## 3. Gravitational branch-difference mode

Linearized quantum gravity driven by two conserved branch stress histories produces branch-conditioned TT coherent states. Define

$$
\boxed{
N_\Delta
=\sum_s\int\frac{d^3k}{(2\pi)^3}
|\Delta\alpha_s(\mathbf k)|^2.
}
$$

After subtracting the branch-common coherent displacement, all coherent branch distinguishability can be compressed into one normalized bosonic **difference mode**, with branch states equivalent to

$$
|\pm\sqrt{N_\Delta}/2\rangle.
$$

Vacuum radiative decoherence is

$$
\Gamma_{\rm vac}=N_\Delta/2.
$$

For a compact nonrelativistic quadrupole difference,

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

For a narrow-band plus quadrupole,

$$
\boxed{
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}{5\hbar c^5}.
}
$$

---

## 4. Exact binary coherent Gaussian-channel theorem

Take any nontrivial finite binary coherent hybrid state

$$
|\Psi\rangle
=\sqrt p\,|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}\,|1\rangle|\beta\rangle,
$$

with $0<p<1$ and $\alpha\neq\beta$.

For a one-mode gauge-covariant phase-insensitive Gaussian channel $\Phi_{\tau,m}$,

$$
\chi_{\Phi(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp[-(2m+1-\tau)|\xi|^2/2],
$$

where $\tau$ is intensity transmission/gain and $m$ is vacuum-output occupation, the channel is EB iff

$$
m\ge\tau.
$$

The current analytic result is

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
m<\tau.
}
$$

Thus every nontrivial finite binary coherent hybrid input is a complete EB probe for thermal attenuation, thermal amplification, and additive Gaussian noise.

The exact sign parameter is

$$
\boxed{
q=
\exp\left[
\frac{|\alpha-\beta|^2}{2m}(\tau-m)
\right].
}
$$

The thermal attenuator special case was independently checked by direct beam-splitter dilation and its infinite-dimensional proof was strengthened with an explicit normalizable negative vector.

Main files:

- `PHASE_INSENSITIVE_GAUSSIAN_BINARY_PROBE_THEOREM.md`
- `BINARY_COHERENT_EB_PROBE_THEOREM.md`
- `EXACT_FINITE_CAT_THERMAL_THEOREM.md`

---

## 5. Exact three-element witness

For symmetric branch states $|\pm a\rangle$, choose

$$
\boxed{
v_*=\frac{2\sqrt\tau\,a}{m}.
}
$$

Measure

$$
p_0=\langle0,0|\rho|0,0\rangle,
$$

$$
p_v=\langle1,v_*|\rho|1,v_*\rangle,
$$

and

$$
z_v=\langle1,0|\rho|0,v_*\rangle.
$$

Every separable state obeys

$$
|z_v|^2\le p_0p_v.
$$

For the binary coherent Gaussian-channel output,

$$
\boxed{
\frac{|z_v|^2}{p_0p_v}
=\exp\left[
\frac{N_\Delta}{m}(\tau-m)
\right].
}
$$

Therefore

$$
\boxed{
|z_v|^2>p_0p_v
\iff
\tau>m
\iff
\rho\text{ is NPT}.
}
$$

Define the finite-strength margin

$$
\boxed{
\Lambda
=\ln\frac{|z_v|^2}{p_0p_v}
=\frac{N_\Delta}{m}(\tau-m).
}
$$

The NPT sign is independent of finite cat size; finite measurable certification is not.

---

## 6. Exact passive causal-front theorem

For a stationary passive Markov receiver,

$$
\dot c
=-\frac{\kappa_{\rm tot}}2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_a\sqrt{\kappa_a}\,b_a^{\rm in},
$$

with thermal injection

$$
\boxed{
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a,
}
$$

any normalized incoming branch-mode waveform obeys

$$
\tau_f(\Delta t)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\Delta t}),
\qquad
\Delta t=t-R/c.
$$

The time-reversed receiver ringdown saturates the bound.

If

$$
\boxed{\kappa_\Delta\le\Gamma_{\rm th},}
$$

no finite binary coherent source encoding produces an NPT front in the model.

If

$$
\kappa_\Delta>\Gamma_{\rm th},
$$

$$
\boxed{
T_{\rm NPT}^{\min}
=\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right].
}
$$

---

## 7. Intrinsic graviton linewidth and passive matter ceiling

For a quadrupole transition,

$$
\boxed{
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

For a plus transition,

$$
\boxed{
\kappa_g
=\frac{4G\omega^5|q|^2}{5\hbar c^5}.
}
$$

For stationary passive nonrelativistic matter, the quadrupole energy-weighted sum rule gives

$$
\boxed{
\kappa_g
\le\frac{4G}{3c^5}I\omega^4,
}
$$

or

$$
\boxed{
\frac{\kappa_g}{\omega}
\le
\frac23\mathcal C_B\beta_B^3,
}
$$

with

$$
\mathcal C_B=r_s/L_B,
\qquad
\beta_B=\omega L_B/c.
$$

This ceiling is not universal to relativistic QFT or strongly self-gravitating systems.

---

## 8. Exact normalized retarded source-receiver coupling

For resonant aligned plus quadrupoles,

$$
\boxed{
\Sigma_{AB}^{R}(\omega,R)
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
\qquad
\epsilon=\omega R/c.
}
$$

Wave zone:

$$
\boxed{
\Sigma_{AB}^{R}
\simeq
\frac54
\frac{e^{i\epsilon}}{\epsilon}
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

Independent checks:

1. Hu et al.'s vacuum-graviton quadrupole resonance tensor reproduces the real part of $P(\epsilon)e^{i\epsilon}$ with the same normalization;
2. direct angular common-bath integration gives
   $$
   \Gamma_{AB}=2\operatorname{Im}\Sigma_{AB}^{R}
   $$
   in the chosen retarded convention.

---

## 9. Delayed gravitational input-output map — storage normalization settled

Eliminating the graviton continuum gives

$$
\dot a_B(t)|_A
=-i\Sigma_{BA}^{R}a_A(t-R/c).
$$

Since

$$
b_{\rm out,A}^{(S)}
=\sqrt{\kappa_{g,A}}a_A,
$$

and

$$
b_{\rm in,B}^{(S)}
=t_{BA}^{\rm store}
 b_{\rm out,A}^{(S)}(t-R/c),
$$

comparison with the receiver input drive gives

$$
\boxed{
t_{BA}^{\rm store}
=\frac{-i\Sigma_{BA}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}
}
$$

up to a global phase convention.

For aligned plus quadrupoles,

$$
\boxed{
t_{BA}^{\rm store}(\epsilon)
=-\frac{5i}{4}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5}.
}
$$

Wave zone:

$$
\boxed{
\eta_{\rm store}(R)
=|t|^2
\simeq
\frac{25\mathcal O}{16(kR)^2}.
}
$$

The factor of two in cross damping belongs to scattering/decay bookkeeping and does not double the stored amplitude.

For one $l=2$ partial-wave channel,

$$
\boxed{
\sigma_{\rm abs,max}
=\frac{5\pi}{2k^2},
}
$$

while the unitary scattering scale is

$$
\boxed{
\sigma_{\rm sca,max}
=\frac{10\pi}{k^2}.
}
$$

Files:

- `DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md`
- `RESONANT_FREE_SPACE_RECEPTION_CONE.md`

---

## 10. Correct compact-resonant reception cone

The receiver's total graviton linewidth is intrinsic and range independent:

$$
\boxed{
\kappa_{\rm tot}
=\kappa_{g,B}+\kappa_i+\cdots.
}
$$

Range affects only the desired source-mode fraction,

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}
\kappa_{g,B}.
}
$$

For stationary thermal injection, define

$$
\boxed{
R_Q^{\rm res}
=\frac{5}{4k}
\sqrt{
\frac{\mathcal O\kappa_{g,B}}
{\Gamma_{\rm th}}
}.
}
$$

Then

$$
\boxed{
T_{\rm NPT}^{\min}(R)
=\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln[1-(R/R_Q^{\rm res})^2],
\qquad R<R_Q^{\rm res}.
}
$$

Within range and in the wave zone,

$$
T_{\rm NPT}^{\min}-R/c\propto R^2.
$$

As $R\to R_Q^{\rm res-}$ the NPT front diverges logarithmically.

For finite witness margin $\Lambda_{\rm req}$,

$$
\boxed{
R_\Lambda^{\rm res}
=\frac{R_Q^{\rm res}}
{\sqrt{1+\Lambda_{\rm req}/N_\Delta}}.
}
$$

---

## 11. Vacuum passive wave-zone entanglement ceiling

At exactly zero thermal occupation, pure loss is non-EB at every nonzero transmission, so the mathematical NPT range is unbounded. The physically stronger quantity is maximum transferable entanglement.

Total asymptotic storage efficiency is

$$
\boxed{
\eta_Q(R)
=\frac{25\mathcal O}{16(kR)^2}
\frac{\kappa_g}{\kappa_{\rm tot}}.
}
$$

For $\eta_Q\ll1$, optimizing source branch strength gives

$$
N_\Delta^{\rm opt}=4\sqrt{\eta_Q}+O(\eta_Q),
$$

$$
\boxed{
\mathcal N_{\max}
=\eta_Q-2\eta_Q^{3/2}+O(\eta_Q^2)
\simeq\eta_Q.
}
$$

For passive nonrelativistic matter with $\kappa_{\rm tot}\simeq\omega/Q_B$,

$$
\boxed{
\mathcal N_{\max}(R)
\lesssim
\frac{25\mathcal O}{24(kR)^2}
Q_B\mathcal C_B\beta_B^3.
}
$$

At wave-zone radius $kR\ge\zeta$,

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\lesssim
\mathfrak V_B
\equiv
\frac{25\mathcal O}{24\zeta^2}
Q_B\mathcal C_B\beta_B^3.
}
$$

This is the current strongest passive laboratory-matter feasibility statement. It remains severe even in perfect vacuum.

File: `VACUUM_PASSIVE_ENTANGLEMENT_CEILING.md`.

---

## 12. Gravitational beta-factor bound and arrays

For receiver continuum coupling vector $g_B(\lambda)$ and normalized source mode $f_S(\lambda)$,

$$
\kappa_g=2\pi\int d\lambda|g_B(\lambda)|^2,
$$

$$
\kappa_\Delta=2\pi|\langle g_B,f_S\rangle|^2.
$$

Therefore

$$
\boxed{
\kappa_\Delta\le\kappa_g.
}
$$

Define

$$
\boxed{
\beta_\Delta=\kappa_\Delta/\kappa_g\le1.
}
$$

A coherent array can

1. increase total gravitational oscillator strength $\kappa_g$;
2. improve source-mode overlap/directivity $\beta_\Delta$;

but these are separate resources. Directivity cannot create oscillator strength from nothing.

File: `GRAVITATIONAL_BETA_FACTOR_BOUND.md`.

---

## 13. Planck-area absorption reconciled with resonant storage

Weak gravitationally bound-state calculations give a Planckian absorption strength,

$$
\boxed{
\sigma_{\rm GR}
=\frac{\Gamma_g}{\omega^3}
=\tilde\kappa\ell_P^2
}
$$

in $c=1$ conventions.

Thus

$$
\boxed{
\frac{\Gamma_g}{\omega}
=\tilde\kappa(k\ell_P)^2.
}
$$

The wavelength-scale peak resonant storage area

$$
\sigma_{\rm peak}=\frac{5\pi}{2k^2}
$$

is therefore consistent with Planckian broadband/frequency-averaged strength because

$$
\boxed{
\sigma_{\rm GR}
=\frac{2}{5\pi}
\sigma_{\rm peak}
\frac{\Gamma_g}{\omega}
}
$$

in the stated conventions.

Robustly,

$$
\boxed{
\text{Planck-scale oscillator strength}
\sim
\text{wavelength-scale peak area}
\times
\text{Planck-suppressed fractional bandwidth}.
}
$$

The coherent loading time is

$$
\boxed{
T_{\rm load}
\sim\Gamma_g^{-1}
\sim
[\omega(k\ell_P)^2]^{-1}
}
$$

up to the bound-state matrix-element coefficient.

Thus weakly gravitating bound states can have a large **peak** resonant cross section only at the cost of an absurdly narrow line and enormous coherent loading time.

Files:

- `PLANCK_AREA_RESONANT_RECONCILIATION.md`
- `PLANCK_BANDWIDTH_LOADING_LIMIT.md`

---

## 14. Strong self-gravity is the real escape route

The Planck-suppressed fractional linewidth is not universal to gravity.

For the fundamental Schwarzschild $l=2$ gravitational quasinormal mode,

$$
M\omega\simeq0.3737-0.0890i,
$$

so

$$
Q_{\rm BH}\sim2.1.
$$

Strongly self-gravitating systems can therefore have order-unity gravitational bandwidth/coupling.

Neutron-star-like modes occupy an intermediate regime with much stronger gravitational damping than laboratory matter but enormous realistic thermal occupation.

This creates a receiver tradeoff:

### Laboratory matter

- weak gravitational capture;
- potentially good quantum coherence/control/accessibility.

### Compact-star modes

- much stronger gravitational capture;
- huge thermal/internal environment;
- poor microscopic accessibility.

### Black-hole-like modes

- strong gravitational coupling/bandwidth;
- absorber/horizon degrees of freedom are not obviously an accessible coherent quantum register.

The remaining general problem is therefore a **capture–coherence–accessibility tradeoff**, not a universal Planck-area bound.

File: `COMPACT_OBJECT_RECEIVER_TRADEOFF.md`.

---

## 15. Accessible receiver cascade theorem — latest abstraction

Model reception as

$$
\boxed{
\text{gravitational capture}
\to
\text{accessible readout register}.
}
$$

Let capture be a phase-insensitive Gaussian channel

$$
\Phi_c=\Phi_{\tau_c,m_c},
$$

and readout be

$$
\Phi_r=\Phi_{\tau_r,m_r}.
$$

The composition is

$$
\boxed{
\tau_{\rm tot}=\tau_c\tau_r,
}
$$

$$
\boxed{
m_{\rm tot}=\tau_rm_c+m_r.
}
$$

Define capture quantum excess

$$
\boxed{
\Delta_c=\tau_c-m_c.
}
$$

Then the source and **accessible register** are NPT for every nontrivial finite binary coherent input iff

$$
\boxed{
\tau_r\Delta_c>m_r.
}
$$

Equivalently,

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_c-m_r>0.
}
$$

This formalizes accessibility:

> strong gravitational absorption is insufficient if the stored branch information cannot pass through a second channel into a controllable register without becoming entanglement breaking.

For an $N$-stage phase-insensitive Gaussian chain,

$$
\tau_{1:N}=\prod_j\tau_j,
$$

and downstream stages transmit upstream noise while adding their own.

File: `ACCESSIBLE_RECEIVER_CASCADE_THEOREM.md`.

---

## 16. Receiver-theory limits and open loopholes

Closed or largely closed within the present model:

- phase-insensitive amplifier gain does not help for free because spontaneous gain noise enters the EB budget;
- deterministic Gaussian squeezing cannot alter EB status, though it can improve matching/readout;
- linear array gain cannot make $\kappa_\Delta>\kappa_g$.

Open:

- relativistic field-theoretic receiver with large gravitational branching and low accessible noise;
- strongly self-gravitating receiver with an explicit coherent readout channel;
- genuinely non-Gaussian/heralded receiver operations;
- a non-Gaussian/channel-theoretic generalization of the accessible quantum-excess cascade.

---

## 17. Novelty boundary

Established prior art includes:

- two-coherent-state effective-entanglement channel tests;
- the same symmetric hybrid coherent/qubit state through thermal attenuation;
- phase-insensitive Gaussian EB thresholds;
- nonzero entanglement-distribution capacity for every non-EB phase-insensitive Gaussian channel using other protocols;
- finite free-space quantum ranges caused by loss/background noise;
- retarded gravity-mediated entanglement;
- graviton quadrupole radiation, resonance interaction, and Planck-area bound-state absorption;
- standard input-output/cascaded-system theory.

Closest hybrid predecessor: **Kreis & van Loock, PRA 85, 032307 (2012)** study the same symmetric hybrid state and thermal attenuator but use a sufficient moment witness and explicitly note that it can fail below the EB boundary.

Current targeted searches have not located:

1. the theorem that every nontrivial finite binary coherent hybrid input is NPT iff a gauge-covariant phase-insensitive Gaussian channel is non-EB;
2. the exact three-element matched witness saturating that boundary;
3. the exact retarded gravitational earliest-NPT/certification fronts built from that theorem;
4. the combined delayed gravitational Green-function storage map and source-receiver front;
5. the passive vacuum entanglement ceiling in the present receiver interpretation;
6. the capture→accessible-readout Gaussian cascade used to formalize the strong-gravity accessibility problem.

Novelty remains **promising but unverified**. Do not claim originality until broader citation-forward review and independent mathematical scrutiny are complete.

---

## 18. Strongest next path

The next research target is no longer another weak receiver example. It is the general receiver tradeoff.

1. **Generalize accessibility beyond Gaussian channels.** Seek a channel-theoretic quantity that captures
   $$
   \text{capture strength}
   +
   \text{coherence preservation}
   +
   \text{readout accessibility}
   $$
   without assuming phase-insensitive Gaussian dynamics.
2. Test that abstraction on an idealized strong-gravity receiver/readout chain rather than guessing black-hole parameters.
3. Search for a covariant/passive response bound on the combined peak-coupling × bandwidth × accessible-coherence resource, not on cross section alone.
4. If no structural failure appears, reorganize Experiment 01 around:
   - binary coherent Gaussian-channel completeness;
   - retarded gravitational difference mode;
   - exact matched witness;
   - causal NPT and finite-certification fronts;
   - delayed gravitational storage map;
   - passive vacuum ceiling;
   - capture→accessibility cascade.

## Current Einstein/Feynman compression

> **A gravitational signal can arrive without quantum information becoming usable. Relativity permits the branch-dependent field to reach the receiver after $R/c$. Quantum mechanics then asks whether the receiver stores that branch mode coherently faster than its uncontrolled environment creates an ordinary record. Even successful internal capture is not the end: the stored state must still reach a controllable readout register without being classicalized. Weak laboratory matter can be coherent and accessible but couples fantastically weakly to gravity. Strongly gravitating systems can absorb gravity efficiently but may hide the information in inaccessible or strongly scrambling degrees of freedom. The real receiver problem is therefore not simply “how strongly does it absorb gravitons?” but “how much branch coherence can be captured, preserved, and made accessible?”**