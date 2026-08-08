# CONTEXT_HANDOFF.md — Live Agent Continuity File

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Research state included through:** `bee11bda2fcade8930a0ebca70539e6e7481247a`  
**Snapshot date:** 2026-08-07 23:59 EDT  

> **LIVE `main` ALWAYS WINS.** This repo may be edited by another agent. Before every write, fetch current HEAD, inspect intervening commits, re-fetch the exact target file, and never write from a stale blob SHA.

---

# 1. Project status in one sentence

The project now studies a **locally prepared, explicitly conserved quadrupolar gravity source whose branch-dependent radiative mode is propagated through retarded free space into a noisy quantum receiver**, asking when the downstream bosonic channel preserves source-reference entanglement.

The standalone Gaussian-channel theorem paper is **stopped**. The active publication candidate is the gravity-specific end-to-end construction.

---

# 2. Broad novelty claims that are dead

Do not resurrect any of these as headline discoveries.

## Gaussian collisions

- Mele–Lami–Giovannetti: finite Schmidt-rank-two Fock survival in the non-EB phase-insensitive Gaussian region.
- Filippov–Ziman (2014): all-finite binary coherent survival in substance, including the matched coherent scale/exponential factor.

Read:

- `STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
- `NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `THREE_ELEMENT_WITNESS_VS_FILIPPOV.md`

## Gravity collisions

Do not claim novelty for

- branch-conditioned coherent graviton radiation;
- $N_\Delta=\|\Delta\alpha\|^2$ as radiation-state distance;
- $\Gamma_{\rm vac}=N_\Delta/2$;
- coherent quantum gravitational radiation from a classical/semiclassical source;
- quantum GW → resonant quantum detector state transfer;
- gravitational communication framed by an EB/non-EB threshold;
- propagating gravitons causally generating distant matter entanglement after a distance-dependent delay.

The last item is explicitly occupied by Trenggana & Zen, arXiv:2606.12901 (2026).

Read:

- `NOVELTY_AUDIT_END_TO_END_GRAVITY_2026.md`
- `NOVELTY_COLLISION_TRENGGANA_ZEN_PROPAGATING_ENTANGLEMENT.md`
- `MATSUI_NDELTA_NORMALIZATION_CROSSCHECK.md`

---

# 3. Strongest defensible paper thesis

The remaining candidate contribution is a **source-resolved quantitative synthesis**:

> Construct a local branch preparation with a branch-common controller; realize it as an internally conserved finite-mass elastic quadrupole; normalize the emitted graviton difference mode; propagate it through retarded free space with an audited storage coefficient; load it into a noisy resonant receiver; and determine the finite spacetime region in which the downstream channel preserves source-reference entanglement, with controlled source, finite-size, feedback, and thermal errors.

The novelty, if it survives final review, is in the **complete explicit construction and normalization**, not any one conceptual ingredient.

---

# 4. Canonical conserved source

Use the four-spoke elastic plus mode.

Define

$$
q=\frac{\omega L}{c_s}.
$$

Exact spoke/end-mass boundary condition:

$$
\boxed{\frac{m_r}{\mu}=q\tan q.}
$$

Total branch-difference plus quadrupole:

$$
\boxed{
\Delta Q_{xx}=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx}.
}
$$

Generalized mode mass:

$$
\boxed{
M_{\rm eff}=4\mu A(q),
\qquad
A(q)=\frac12+\frac{q}{\sin2q}.
}
$$

One-phonon quadrupole matrix element:

$$
\boxed{
q_{01}
=4\mu L\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}\omega}}.
}
$$

Gravitational linewidth:

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\mathcal C_\kappa(q),
}
$$

$$
\boxed{
\mathcal C_\kappa(q)
=\frac{(\tan q/q)^2}{A(q)}
=1+\frac{q^2}{3}+\frac{q^4}{9}+\cdots.
}
$$

Main source file:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`

---

# 5. Graviton branch-distance normalization is externally verified

Use

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

Matsui 2026 independently gives the same coefficient and convention, with

$$
\boxed{\Gamma_{\rm vac}=N_\Delta/2.}
$$

No factor-of-two/four normalization discrepancy was found.

Matsui also explicitly notes that the quadrupole reduction requires the **complete conserved matter–apparatus source**, while setup-dependent apparatus terms are often left out of estimates. This is exactly where the explicit finite-spoke source is useful.

Read:

- `MATSUI_NDELTA_NORMALIZATION_CROSSCHECK.md`

---

# 6. Local source preparation is now explicit

Do not define the fundamental causal protocol by declaring a branch-displaced mechanical state at $t=0$.

Preferred physical preparation uses a degenerate internal source qubit/reference $R$, finite-spoke source mode $a$, and branch-common work mode $c$:

$$
\boxed{
H_{\rm enc}
=\hbar g\sigma_z(a^\dagger c+a c^\dagger).
}
$$

Lossless branch amplitudes:

$$
\alpha_s(t)=-is\beta\sin gt,
\qquad
\gamma_s(t)=\beta\cos gt.
$$

At a half swap,

$$
\boxed{gT=\pi/2,}
$$

controller $c$ is exactly vacuum and the mechanical source carries opposite coherent branches.

With source damping $\kappa_A$, define

$$
\Omega=\sqrt{g^2-\kappa_A^2/16}.
$$

There is an exact controller-empty time

$$
\boxed{
T_*
=\frac{\pi-\arctan(4\Omega/\kappa_A)}{\Omega},
}
$$

with

$$
\gamma(T_*)=0,
\qquad
\alpha_s(T_*)=-is\beta e^{-\kappa_AT_*/4}.
$$

For vacuum loss ports the controller is branch independent, vacuum, and factorized at the handoff.

Read:

- `EXACT_LOCAL_GAUSSIAN_SOURCE_ENCODER.md`
- `CHANNEL_INPUT_ROLE_AND_DARK_MEMORY_AUDIT.md`

Important conceptual role:

- the qubit is a **retained reference**, not the Gaussian channel input;
- the downstream bosonic source/gravitational mode → receiver map is the channel whose EB property is tested.

---

# 7. Continuum realization of the local encoder

The modal encoder can arise from a local elastic eigenstrain energy, not an unexplained external force.

For spoke sign $\epsilon_a=\pm1$,

$$
\boxed{
H_{{\rm el},a}
=\frac12EA\int_0^Ldx\,
[\partial_x\xi_a
-\epsilon_a\sigma_z\lambda X_c\chi(x)]^2.
}
$$

Projecting

$$
\xi_a=\epsilon_a u f_q(x)
$$

gives

$$
\boxed{
H_{\rm cross}
=-4EA\lambda\mathcal J\sigma_zX_cu,
}
$$

$$
\mathcal J=\int_0^L\chi(x)f_q'(x)dx.
$$

After quantization and RWA this is the sign-controlled beam-splitter encoder.

For mirrored branches, the ideal elastic energy density is pointwise branch even.

Read:

- `DISTRIBUTED_EIGENSTRAIN_ENCODER_REALIZATION.md`

Remaining scope: this is a continuum theoretical realization, not a detailed material device or fully relativistic active-material model.

---

# 8. Complete encoder + passive tail is one normalized output mode

The encoder necessarily emits a short precursor. Do not discard it.

For vacuum source-loss ports, define the complete source response $h(t)$ and normalized temporal mode

$$
\boxed{f_{\rm full}(t)=i\sqrt{\kappa_A}h(t),}
$$

with

$$
\boxed{
\int_0^\infty|f_{\rm full}(t)|^2dt=1.
}
$$

The precursor norm is

$$
\boxed{
\epsilon_{\rm pre}
=1-e^{-\kappa_AT_*/2}
\simeq\frac{\pi\kappa_A}{4g}
}
$$

for $g\gg\kappa_A$.

The full source output therefore includes both

1. encoding-stage radiation;
2. passive tail.

Read:

- `LOCAL_BOSONIC_INPUT_SWAP_CHANNEL.md`
- `LOCAL_PREPARATION_END_TO_END_NPT_PROTOCOL.md`

---

# 9. Source branching and receiver channel

Define source gravitational branching

$$
\boxed{
\eta_g=\frac{\kappa_{g,A}}{\kappa_A}.
}
$$

For vacuum ordinary source loss, the source stage is equivalent to pure loss

$$
\mathcal L_{\eta_g}
$$

on the virtual bosonic branch mode.

Receiver useful coupling:

$$
\boxed{
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B}.
}
$$

Receiver loading for the complete source temporal mode:

$$
\boxed{
\tau_{\rm full}(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
e^{-\kappa_B(t-s)/2}f_{\rm full}(s)
\right|^2.
}
$$

Receiver vacuum-output occupation:

$$
\boxed{
m_B(t)
=n_0e^{-\kappa_Bt}
+\frac{\Gamma_{{\rm th},B}}{\kappa_B}
(1-e^{-\kappa_Bt}).
}
$$

Complete vacuum-source effective channel:

$$
\boxed{
\Phi_{\rm eff}(t)
=\Phi_{\eta_g\tau_{\rm full}(t),m_B(t)}.
}
$$

For every finite nonzero coherent branch separation, the locally prepared source-reference/receiver state is NPT iff

$$
\boxed{
\eta_g\tau_{\rm full}(t)>m_B(t).
}
$$

The Gaussian sign theorem is prior art; the gravity construction is the application.

---

# 10. Free-space storage normalization

For aligned compact plus quadrupoles in the wave zone,

$$
\boxed{
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}.
}
$$

Do not use the old $25/[4(kR)^2]$ as coherent storage probability.

The $25/16$ coefficient survived the finite-spoke source normalization update.

Finite-size angular correction for the ideal slender-spoke source:

$$
\boxed{
\kappa_g(q,\beta)
=\kappa_g^{(Q)}(q)
\left[1-\frac{2a(q)}7\beta^2+O(\beta^4)\right],
}
$$

$$
a(q)=\frac12+\frac{\cot q}{q}-\frac1{q^2}.
$$

Endpoint limit:

$$
\boxed{
\kappa_g
=\kappa_g^{(Q)}
[1-\beta^2/21+\cdots].
}
$$

The on-axis planar Fraunhofer amplitude has no transverse $kL$ correction at this order.

Read:

- `STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`
- `FINITE_SIZE_FORM_FACTOR_COEFFICIENT.md`

---

# 11. Passive temporal optimization

For natural exponential source decay and constant receiver coupling, matched linewidths are the **global optimum** at fixed useful receiver fraction.

Let

$$
r=\kappa_B/\kappa_A,
\qquad
\beta_\Delta=\kappa_\Delta/\kappa_B.
$$

Exact peak:

$$
\boxed{
\tau_{\max}(r)
=4\beta_\Delta\frac1r r^{-2/(r-1)}.
}
$$

Unique maximum:

$$
\boxed{r=1.}
$$

Thus

$$
\boxed{
\tau_{\max}^{\rm passive}
=4e^{-2}\beta_\Delta.
}
$$

End-to-end passive ceiling:

$$
\boxed{
\tau_{\rm passive}^{\max}
=4e^{-2}
\beta_{g,A}\beta_{g,B}\eta_{\rm store}.
}
$$

Read:

- `OPTIMAL_PASSIVE_LINEWIDTH_MATCHING.md`

---

# 12. Nonlinear source geometry does not spoil the leading Gaussian branch mode

For the exact endpoint geometry

$$
X=L+u,
\qquad
Y=L-u,
$$

$$
\boxed{
Q_{xx}-Q_{yy}=8\mu Lu
}
$$

exactly. The $u^2$ terms cancel from the branch-carrying plus tensor.

The leading quadratic rest-mass tensor is parity even:

$$
\boxed{
Q_{ij}^{(2)}
\propto
u^2\operatorname{diag}(1,1,-2),
}
$$

and lies in the $0/2\omega$ sector.

Its two-phonon rate is suppressed by

$$
\boxed{
\frac{\Gamma_{2\to0}^{(2)}}
{\Gamma_{1\to0}^{(1)}}
=
\frac{16}{3}
\frac{A(q)^2}{(\tan q/q)^2}
\left(\frac{u_{\rm zpf}}L\right)^2.
}
$$

For perfectly mirrored coherent branches, the coherent $2\omega$ displacement difference vanishes at this order.

Read:

- `NONLINEAR_QUADRUPOLE_GAUSSIANITY_AUDIT.md`

---

# 13. Reciprocal receiver backaction is controlled

The exact reciprocal delayed source/receiver response differs from the one-way cascade by a round-trip factor

$$
\boxed{
\frac1{1+L(\nu)},
}
$$

$$
L(\nu)
=\Sigma_{AB}^R\Sigma_{BA}^R
\chi_A(\nu)\chi_B(\nu)e^{2i\nu R/c}.
$$

Uniform bound:

$$
\boxed{
|L(\nu)|
\le
4\eta_{\rm store}
\beta_{g,A}\beta_{g,B}.
}
$$

Wave-zone form:

$$
\boxed{
|L|
\le
\frac{25\mathcal O}{4(kR)^2}
\beta_{g,A}\beta_{g,B}.
}
$$

Thus

- relative transfer-amplitude correction is $O((kR)^{-2})$;
- absolute correction to the leading $O((kR)^{-2})$ forward transfer probability is $O((kR)^{-4})$;
- the first source-controlled feedback echo at the receiver follows the path $A\to B\to A\to B$ and cannot arrive before $3R/c$.

Read:

- `RECIPROCAL_FEEDBACK_CASCADE_AUDIT.md`

---

# 14. Finite source causality: use the operation worldtube

The theorem-level statement is

$$
\boxed{
\text{receiver source-dependence}=0
\quad\text{outside }J^+(\mathcal W_A),
}
$$

where $\mathcal W_A$ is the complete source-operation worldtube.

For an arbitrary simultaneous extended source operation,

$$
T_{\rm front}\ge D_{AB}/c,
$$

where $D_{AB}$ is support-to-support distance.

For a centrally triggered causal encoder, if source point $\mathbf x$ cannot respond before $|\mathbf x-\mathbf x_0|/c$, then the triangle inequality gives

$$
\boxed{T_{\rm front}\ge R/c}
$$

for a point receiver at distance $R$ from the local origin, regardless of source extent.

For the canonical planar four-spoke source viewed on axis, transverse path spread begins only at

$$
\boxed{
\Delta t\sim L^2/(2Rc),
}
$$

consistent with the Fresnel criterion $kL^2/R\ll1$.

Read:

- `FINITE_SOURCE_CAUSAL_SUPPORT_AUDIT.md`

---

# 15. Source thermal noise

Passive source thermal channel:

$$
\boxed{
m_A^{\rm passive}
=\eta_g\frac{\Gamma_{{\rm th},A}}{\kappa_A}.}
$$

Full passive source→receiver non-EB condition:

$$
\boxed{
\tau_f(t)
[\eta_g-m_A]
>m_B(t).
}
$$

Thermal noise injected specifically during the local encoder obeys

$$
\boxed{
\Delta N_{\rm enc}
\le\Gamma_{\rm enc}T_*}
$$

and gravitational-output penalty

$$
\boxed{
\delta m_A^{\rm enc}
\le\eta_g\Gamma_{\rm enc}T_*.
}
$$

For source-bath dominated noise,

$$
\boxed{
\frac{\delta m_A^{\rm enc}}
{m_A^{\rm passive}}
\lesssim
\kappa_AT_*
\simeq\frac{\pi\kappa_A}{2g}.
}
$$

Thus the hierarchy

$$
\boxed{\kappa_A\ll g\ll\omega}
$$

simultaneously controls precursor emission, encoder loss, thermal contamination, and RWA validity.

Read:

- `THERMAL_PASSIVE_SOURCE_CHANNEL.md`
- `THERMAL_LOCAL_ENCODER_BOUND.md`

---

# 16. Causal/NPT capability statement

Let the local encoder begin at source time zero and let receiver-local time after causal arrival be $\theta$.

For the vacuum-source benchmark,

$$
\boxed{
\rho_{RB}(\theta)\text{ NPT}
\iff
\eta_g\tau_{\rm full}(\theta)>m_B(\theta).
}
$$

Define

$$
\boxed{
T_{\rm NPT}(R)
=\frac Rc+
\inf\{\theta>0:
\eta_g\tau_{\rm full}(\theta)>m_B(\theta)\}
}
$$

only for the explicitly defined point-origin/aligned benchmark. The invariant theorem uses the causal future of the source-operation worldtube.

Do not revert to the old universal logarithmic “quantum cone” for one physical pulse.

---

# 17. Practical scale remains devastating

The project is a theoretical channel-structure result, not a near-term apparatus proposal.

Earlier aggressive kilogram/meter/MHz/$Q\sim10^{12}$/perfect-overlap benchmarks gave optimized passive negativity around

$$
10^{-22}.
$$

The new source closure does not remove the enormous weakness of gravity.

---

# 18. Current strongest remaining attacks

The model has now survived leading-order attacks on

- source conservation;
- actuator cancellation;
- controller branch records;
- unexplained initial branch state;
- finite spoke inertia;
- finite source size;
- nonlinear quadrupole terms;
- reciprocal source↔receiver feedback;
- encoder thermal noise;
- broad novelty overclaims.

Highest-value remaining work, in order:

1. **Final source-level novelty audit of the exact local-preparation + conserved-source + normalized-storage + noisy-receiver combination.** Search combinations, not individual ingredients.
2. **Exact thermal covariance of the full encoder-plus-tail temporal mode** if a submission needs an equality rather than the current rigorous fast-encoder bound.
3. **Microscopic implementation/error model for the sign-controlled eigenstrain coupler**, only if reviewers require more than the continuum existence construction.
4. **Final paper core rewrite** around the narrow end-to-end benchmark, with prior-art collisions stated prominently rather than hidden.
5. Recompute a representative absolute feasibility benchmark using all current correction factors to ensure no accumulated normalization drift.

---

# 19. Canonical recovery reading order

After refreshing live `main`:

1. `AGENTS.md`
2. `CONTEXT_HANDOFF.md`
3. all commits after the snapshot SHA above
4. `NOVELTY_AUDIT_END_TO_END_GRAVITY_2026.md`
5. `NOVELTY_COLLISION_TRENGGANA_ZEN_PROPAGATING_ENTANGLEMENT.md`
6. `MATSUI_NDELTA_NORMALIZATION_CROSSCHECK.md`
7. `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`
8. `EXACT_LOCAL_GAUSSIAN_SOURCE_ENCODER.md`
9. `DISTRIBUTED_EIGENSTRAIN_ENCODER_REALIZATION.md`
10. `LOCAL_PREPARATION_END_TO_END_NPT_PROTOCOL.md`
11. `STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`
12. `FINITE_SIZE_FORM_FACTOR_COEFFICIENT.md`
13. `NONLINEAR_QUADRUPOLE_GAUSSIANITY_AUDIT.md`
14. `RECIPROCAL_FEEDBACK_CASCADE_AUDIT.md`
15. `FINITE_SOURCE_CAUSAL_SUPPORT_AUDIT.md`
16. `THERMAL_PASSIVE_SOURCE_CHANNEL.md`
17. `THERMAL_LOCAL_ENCODER_BOUND.md`
18. `OPTIMAL_PASSIVE_LINEWIDTH_MATCHING.md`
19. paper-core/current-state files only after these technical notes are understood.

---

# 20. Working rule

Attack every attractive claim by

1. counterexample;
2. hidden assumption;
3. factor-of-two / convention error;
4. conservation failure;
5. omitted subsystem;
6. nonlinear correction;
7. feedback / reciprocity;
8. finite-support causality;
9. thermal/noise correction;
10. stronger prior art under different notation;
11. scope inflation.

If a claim dies, preserve correct mathematics but downgrade the novelty immediately.
