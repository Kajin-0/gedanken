# Manuscript V7 — Adversarial Referee Audit

**Date:** 2026-08-08  
**Status:** ACTIVE PRE-SUBMISSION AUDIT  
**Target:** `manuscript_v7/main.tex`

## 1. Executive verdict

The V7 architecture is internally much stronger than V6.

The main chain is now

$$
\boxed{
\text{equal-charge local code}
\to
\text{fixed virtual-mode handoff}
\to
\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f
\to
\Delta_{\rm mem}
\to
\Delta_{\rm acc}.}
$$

No fatal inconsistency has been found in this audit.

The paper is potentially publishable as a **source-resolved normalization / synthesis paper**, provided the remaining medium-risk claims are kept narrowly scoped and the derivations stay visible.

The strongest remaining risks are not the Gaussian channel algebra. They are

1. how fully the explicit elastic/control model earns the phrase "conserved source";
2. whether the equal-charge gravitational-dressing argument is stated no more strongly than first-order gravitational splitting supports;
3. the normalization and literature positioning of the passive quadrupole sum-rule ceiling;
4. the novelty/value proposition for the complete serial link normalization.

---

# 2. Claim-by-claim risk table

| Claim | Current status | Referee risk | Required discipline |
|---|---|---:|---|
| finite-spoke support does not cancel plus quadrupole | analytically derived | low-medium | state linear-elastic/weak-field scope |
| local encoder returns work mode to common vacuum | exact in linear damped model | low | retain coherent/vacuum-port assumption |
| two branches have equal Poincare charges | symmetry argument | medium | keep "to working order" and include controller assumptions |
| common asymptotic dressing is available | supported by Donnelly--Giddings first-order splitting | medium | do not claim exact locality or exact subsystem factorization |
| causal receiver response starts no earlier than source worldtube light cone | retarded conserved source + triangle inequality | low-medium | formulate using physical receiver observables / difference stress tensor |
| fixed virtual bosonic mode exists after $T_*$ | exact coherent-state mode rotation | low | distinguish encoder interval from post-handoff channel |
| source gravitational branching is $\kappa_g/\kappa_A$ | exact in narrowband Markov amplitude damping | low | keep frequency-dependent and dephasing caveats |
| $\eta_{\rm store}=25\mathcal O/[16(kR)^2]$ | checked by Green function, critical-coupling area, EM control, Friis form | medium | present as normalized bridge, not new cross section |
| four-factor product has no double counting | independently reproduced by bosonic cascade | low | retain separate stage definitions |
| memory non-EB iff $\Delta_{\rm mem}>0$ | standard phase-insensitive Gaussian channel result | low | do not claim novelty |
| readout gives $\Delta_{\rm acc}=\tau_r\Delta_{\rm mem}-m_r$ | exact Gaussian composition | low | keep memory/readout distinction |
| exact pure-loss negativity | exact two-dimensional receiver-support reduction | low | derivation now in appendix |
| $\mathcal N_{\max}\sim\eta$ | numerical and asymptotic checks agree | low | distinguish vacuum pure-loss result from thermal case |
| passive $\kappa_g/\omega\lesssim(2/3)\mathcal C\beta^3$ | double-commutator/EWSR derivation | medium | passive nonrelativistic class only; continue literature audit |
| active $N^2$ collectivity removes fixed internal loss but saturates at mode selectivity | rate-level argument + prior collective model | medium | do not imply universal active-channel theorem |
| ordinary/ordinary benchmark is $O(10^{-42})$ | arithmetic checked | low | label parameter set deliberately aggressive, not realistic design |

---

# 3. Independent checks completed in this audit

## 3.1 Benchmark arithmetic

Using

$$
\beta_g=1.09386\times10^{-20},
$$

and

$$
\eta_{\rm store}=\frac{25}{16(10)^2}=0.015625,
$$

one obtains

$$
\boxed{
\eta_Q^{\rm link}
=\beta_g^2\eta_{\rm store}
=1.86958\times10^{-42}.}
$$

For a matched passive exponential,

$$
4e^{-2}\eta_Q^{\rm link}
=1.01208\times10^{-42}.
$$

With one ideal gravitational interface,

$$
\eta_{\rm store}\beta_g
=1.70916\times10^{-22}.
$$

These reproduce the manuscript values.

For

$$
\kappa_g=6.87\times10^{-26}\,\mathrm{s}^{-1},
$$

the corresponding lifetime is

$$
\boxed{\kappa_g^{-1}=4.61\times10^{17}\,\mathrm{yr}.}
$$

## 3.2 Exact pure-loss negativity asymptotics

Numerical optimization of

$$
\mathcal N(\eta,A)
=
\frac{
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
}{4}
$$

was repeated for

$$
10^{-2}\ge\eta\ge10^{-6}.
$$

The optimizer satisfies

$$
\boxed{
\frac{A_{\rm opt}^2}{\sqrt\eta}\to1,}
$$

and the optimized negativity converges to

$$
\boxed{
\mathcal N_{\max}
=\eta-2\eta^{3/2}
+\frac{13}{3}\eta^2
+O(\eta^{5/2}).}
$$

Example:

$$
\eta=10^{-4}:
$$

$$
A_{\rm opt}^2=9.8354\times10^{-3},
$$

$$
\mathcal N_{\rm exact}=9.8042430\times10^{-5},
$$

while the truncated asymptotic expression gives

$$
9.8043333\times10^{-5}.
$$

Thus the linear-in-link conclusion is numerically stable.

## 3.3 Passive sum-rule coefficient

For an orthonormal STF basis $E^A_{ij}$,

$$
\sum_A E^A_{kj}E^A_{kl}
=\frac53\delta_{jl}.
$$

For one particle,

$$
Q_A=mE^A_{ij}x_ix_j,
$$

so

$$
\sum_A|\nabla Q_A|^2
=\frac{20}{3}m^2r^2.
$$

Using

$$
\frac12[Q,[p^2/(2m),Q]]
=\frac{\hbar^2}{2m}|\nabla Q|^2
$$

gives

$$
\boxed{
\sum_A\frac12[Q_A,[H,Q_A]]
=\frac{10}{3}\hbar^2mr^2.}
$$

Summing particles reproduces the manuscript coefficient

$$
\frac{10}{3}\hbar^2 I.
$$

This independently checks the normalization behind the passive EWSR bound.

---

# 4. Precursor / handoff issue

This was the largest conceptual ambiguity in the first V7 draft and is now corrected.

Radiation emitted during the encoder is not discarded.

At sufficiently small separation the receiver can begin responding to that precursor before

$$
T_*.
$$

Therefore:

- for $t<T_*$, the physical process is controlled qubit-to-multimode state generation;
- the receiver entanglement can be evaluated from the instantaneous coherent branch state;
- the response normalized to the eventual code norm is not yet called a fixed-input channel transmissivity;
- at $T_*$, the total branch-distance norm is fixed;
- for receiver states evaluated after $T_*$, the fixed virtual mode includes precursor modes already emitted/in flight, and the complete waveform $f$ includes their contribution.

This distinction is now explicit in `manuscript_v7/main.tex`.

---

# 5. Gravitational-dressing risk

Donnelly--Giddings establishes two facts relevant here:

1. gauge-invariant gravitational observables do not obey ordinary compact local-QFT subsystem structure;
2. at first perturbative order, a gravitational splitting can make exterior observables insensitive to internal information except through total Poincare charges.

V7 uses only the second, restricted statement.

The source branches are designed so that

$$
\Delta P^\mu=0,
\qquad
\Delta M^{\mu\nu}=0
$$

to the working order.

The manuscript must continue to say

- "common first-order asymptotic dressing";
- "equal-charge encoded subspace";
- "to the working perturbative order";

and must avoid

- "exactly local gravitational qubit";
- "exact tensor factorization";
- "all outside observables commute";
- any claim covering states with different ADM/Poincare charges.

Current V7 wording satisfies this requirement.

---

# 6. Source-conservation risk

The finite-spoke model is a meaningful improvement over prescribed accelerated point masses because it supplies

- finite support mass;
- internal elastic stress;
- a central hub;
- an internal eigenstrain actuator architecture;
- total momentum/torque cancellation by symmetry.

However it remains a **linear-elastic effective model**.

The paper should not claim a fully covariant microscopic hyperelastic material stress tensor.

Recommended phrasing:

> The complete source is conserved to the working order of the nonrelativistic elastic model; a microscopic relativistic material completion is outside the present scope.

This is already close to the current main-text wording.

---

# 7. Passive sum-rule risk

The algebraic normalization has been independently checked, but the literature novelty boundary remains less mature than for the main link budget.

Recommended publication strategy:

- keep the bound as a **derived passive-class corollary**, not as the title/abstract claim;
- retain the derivation in an appendix;
- explicitly restrict to stationary passive nonrelativistic coordinate-quadrupole matter;
- do not apply to active/inverted states or relativistic QFT;
- perform one final source-level literature search for quadrupole energy-weighted sum rules in gravitational/nuclear transition literature before submission.

If a close prior statement is found, cite it and keep the present derivation as an application.

---

# 8. Novelty verdict

The literature audits already show that the following are occupied individually:

- coherent graviton radiation;
- closed/conserved branch sources;
- propagating-graviton entanglement;
- quantum GW reception;
- graviton transduction;
- gravitational communication benchmarks;
- Gaussian EB criteria;
- critical-coupling $l=2$ absorption;
- collective gravitational transition enhancement.

The manuscript should therefore make one novelty claim only:

> **A locally initialized, equal-charge, conserved source-to-accessible-receiver weak-gravity construction in which source branching, free-space mode capture, receiver branching, temporal loading, noise, and readout are normalized in one end-to-end calculation.**

The novelty risk is **medium**, because the contribution is primarily synthesis plus normalization rather than a new fundamental theorem.

That is acceptable if the paper makes clear what the synthesis resolves:

1. receiver-local calculations hide the source gravitational branching penalty;
2. ``incoming graviton mode'' descriptions do not specify local source preparation;
3. memory capture is not accessible quantum readout;
4. gravitational locality requires an equal-charge dressing-aware formulation;
5. the $10^{-22}$ receiver-local scale becomes $10^{-42}$ in the ordinary/ordinary end-to-end benchmark.

---

# 9. Current strongest paper claims

The safest high-value claims are:

### A. Physical local initialization

An explicit branch-common work mode can create mirrored coherent source branches and return to the same vacuum state at a finite handoff time.

### B. Dressing-aware code

The two source branches share total Poincare charges to the working order, allowing common first-order asymptotic dressing rather than an assumed exactly local gravitational subsystem.

### C. Fixed virtual mode

At handoff the complete coherent branch-distance norm is fixed and all branch dependence can be compressed into one virtual bosonic mode.

### D. Four-factor memory link

$$
\boxed{
\tau_c
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f.}
$$

### E. Accessible quantum excess

$$
\boxed{
\Delta_{\rm acc}
=\tau_r(\tau_c-m_c)-m_r.}
$$

### F. Quantitative weak-link entanglement

$$
\boxed{
\mathcal N_{\max}
=\eta-2\eta^{3/2}+O(\eta^2).}
$$

### G. Ordinary-matter hierarchy

The aggressive ordinary/ordinary benchmark is

$$
O(10^{-42}),
$$

whereas idealizing one matter--gravity interface raises it to

$$
O(10^{-22}).
$$

---

# 10. Remaining pre-submission tasks

Priority order:

1. **Final literature audit of the passive quadrupole EWSR application.**
2. **Explicit charge table** for endpoints + spokes + hub + work/controller showing why every Poincare charge is branch common at the required order.
3. **LaTeX compile/type-setting pass** in an environment with TeX access; current connector environment cannot compile the repository directly.
4. Build one main conceptual figure only after text is stable:
   $$
   S\to\text{encoder}\to\beta_{g,A}\to\eta_{\rm store}\to\beta_{g,B}\to\mathcal T_f\to\Delta_{\rm mem}\to\text{readout}.
   $$
5. Build one benchmark figure/table showing
   $$
   10^{-42}\to10^{-22}\to10^{-2}
   $$
   as the two matter interfaces are idealized.
6. Tighten the introduction/abstract after figures, not before.

No further standalone Gaussian theorem work is currently justified for this paper.
