# CONTEXT_HANDOFF.md — Live Agent Continuity File

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Research state included through:** `4a7119081f5c3baa2d7ee7b54a4f8d1025bee820`  
**Snapshot date:** 2026-08-07 23:12 EDT  
**Purpose:** let a fresh agent recover the current research state quickly after another agent reaches its context limit.

> **This is a snapshot, not authority over live `main`. The repository is being edited concurrently. Before doing any work, fetch the current `main` head and compare it with the SHA above. If `main` has advanced, read the intervening commits and changed files first. Newer live `main` always wins.**

---

## 0. Mandatory concurrency protocol

Before **every write**:

1. Fetch current `main` HEAD.
2. Compare it with the HEAD you last read.
3. If it changed, inspect intervening commits and all relevant changed files.
4. Re-fetch the exact target file immediately before updating it.
5. Never overwrite using an old blob SHA.
6. Prefer a new narrowly scoped note over rewriting a live coordination file unless synchronization is required.
7. If another agent changed the research direction, follow the newer state.

This repository really is being edited concurrently. During creation of this file another agent landed the conserved source-plus-actuator result between head checks. Treat races as normal.

---

# 1. Project in one sentence

The project asks when a branch-dependent gravitational signal can propagate causally into a distant quantum receiver **while preserving quantum branch coherence**, rather than merely creating a classical branch record.

The current publication center is the **gravity application**, with explicit causality, source-mode quantization, retarded propagation, noisy receiver dynamics, and now an explicit conserved source-plus-actuator model.

---

# 2. Standalone Gaussian paper: STOP

The Gaussian work produced correct compact mathematics, but the broad novelty claims collided with prior art.

Read:

- `AGENTS.md`
- `experiments/01-causal-quantum-branch-information/STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
- `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `experiments/01-causal-quantum-branch-information/THREE_ELEMENT_WITNESS_VS_FILIPPOV.md`

## Mele–Lami–Giovannetti collision

The repository independently derived the finite Schmidt-rank-two Fock result

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}},
$$

with

$$
\det M_s
=\frac{s^2}{(1+s^2)^2}\frac{m-\tau}{(m+1)^3}.
$$

The output is NPT iff $\tau>m$, but the substantive finite-Fock-pair survival result already exists in Mele–Lami–Giovannetti.

**Do not resurrect Schmidt-rank-two sufficiency as a new standalone result.**

## Filippov–Ziman collision

The repository independently proved that every finite nontrivial binary coherent hybrid probe survives with NPT output exactly in the non-EB phase-insensitive region.

A one-sided specialization of Filippov–Ziman's 2014 coherent-state witness plus an invertible local filter on the untouched two-dimensional coherent support already implies that survival result.

Their witness also contains the same matched scale. With

$$
1-\lambda=\frac{m}{\sqrt\tau},
$$

the one-sided witness contains

$$
1-\exp\left[\frac{4a^2}{m}(\tau-m)\right]
$$

and the same matched coherent displacement

$$
v_*=\frac{2\sqrt\tau a}{m}.
$$

Do **not** claim as new:

- all-finite binary coherent survival;
- the matched displacement $v_*$;
- the exponential sign factor;
- generic small-coherent-alphabet access to the Gaussian EB boundary.

Retain the repository proofs only as compact lemmas / quantitative tools for the gravity receiver analysis.

---

# 3. Gaussian formulas still worth carrying forward

The phase-insensitive convention is

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp\left[-\frac{2m+1-\tau}{2}|\xi|^2\right],
$$

with

$$
\boxed{\Phi_{\tau,m}\text{ EB}\iff m\ge\tau.}
$$

For

$$
|\Phi_2\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
$$

the selected PT block has

$$
\boxed{\det M_{01}=\frac{m-\tau}{4(m+1)^3}}
$$

and negative eigenvalue

$$
\boxed{\mu_- = \frac{m-\tau}{2(m+1)^2}}.
$$

Therefore

$$
\boxed{\mathcal N_{\rm out}\ge\frac{[\tau-m]_+}{2(m+1)^2}.}
$$

For symmetric coherent branches $|\pm a\rangle$,

$$
\boxed{v_*=\frac{2\sqrt\tau a}{m}},
$$

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

The selected block gives the negativity lower bound

$$
G(v)=\frac12\max\left\{0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}-(p_0+p_v)
\right\}.
$$

Weak-link optimization gives

$$
G_{\rm abs}^{\rm opt}
=\frac{W(e^{-1})}{2}(\tau-m)+O(\tau^2),
$$

with

$$
\frac{W(e^{-1})}{2}\simeq0.1392322714,
\qquad
a_*\simeq0.565346\sqrt\tau.
$$

Treat these as retained tools / possible quantitative corollaries, not the basis of the stopped theorem paper.

---

# 4. Gravity architecture

The active chain is

$$
\boxed{
\text{source qubit}
\to
\text{closed branch-dependent mechanical quadrupole}
\to
\text{graviton difference mode}
\to
\text{retarded propagation}
\to
\text{noisy quantum receiver}
\to
\text{accessible register}.
}
$$

The relevant question is not merely whether a classical gravitational waveform arrives. It is whether the complete source-controlled receiver channel becomes non-entanglement-breaking after causal contact.

---

# 5. Causality statement to preserve

Do **not** claim that all source-receiver entanglement must vanish outside the light cone. Vacuum correlations and entanglement harvesting make that too broad.

Use the controlled-channel theorem.

Define

$$
\mathcal A_{R,t}:
\text{controllable incoming branch mode}
\to
\text{accessible receiver register at time }t.
$$

Before causal contact,

$$
\boxed{
\mathcal A_{R,t}(\rho)
=\sigma_{R,t}\operatorname{Tr}\rho,
\qquad t<R/c,
}
$$

so the source-controlled map is a replacer channel and therefore EB.

Read:

- `GENERAL_CAUSAL_QUANTUM_CHANNEL_FRONT.md`
- `MICROCAUSAL_REPLACER_THEOREM.md`
- `ACCESSIBLE_RECEIVER_CASCADE_THEOREM.md`

---

# 6. NEW CURRENT SOURCE RESULT: explicit conserved four-spoke architecture

The former strongest source-side vulnerability was real: prescribed accelerated endpoint masses alone satisfy

$$
\partial_\mu T^{\mu\nu}_{\rm endpoints}\neq0,
$$

so an unspecified actuator could in principle carry compensating branch-dependent stress-energy.

That leading-order loophole is now closed for one explicit elastic-spoke architecture in

- `experiments/01-causal-quantum-branch-information/CONSERVED_SOURCE_ACTUATOR_AUDIT.md`

Its status is:

> **LEADING-ORDER ACTUATOR LOOPHOLE CLOSED FOR AN EXPLICIT ELASTIC-SPOKE ARCHITECTURE.**

The complete source is

$$
T^{\mu\nu}_{\rm tot}
=T^{\mu\nu}_{\rm end}
+T^{\mu\nu}_{\rm spokes}
+T^{\mu\nu}_{\rm hub}
+T^{\mu\nu}_{\rm ctrl},
$$

with

$$
\boxed{\partial_\mu T^{\mu\nu}_{\rm tot}=0.}
$$

For

$$
I_{ij}
=\frac1{c^2}\int d^3x\,T^{00}_{\rm tot}x_i x_j,
$$

conservation gives

$$
\boxed{\ddot I_{ij}=2\int d^3x\,T^{ij}_{\rm tot}.}
$$

Thus internal stresses are not an extra independent leading TT source to append to a point-mass quadrupole. In a conserved compact source, the stress representation and total-energy-quadrupole representation are equivalent. Any true cancellation must appear in the total energy quadrupole itself.

## 6.1 Exact finite-spoke mode

Use a central hub, four identical longitudinal elastic spokes, endpoint mass $\mu$, spoke mass $m_r$, spoke length $L$, and longitudinal sound speed $c_s$.

Define

$$
\boxed{q\equiv\frac{\omega L}{c_s}.}
$$

The exact endpoint traction condition gives

$$
\boxed{\frac{m_r}{\mu}=q\tan q.}
$$

For the endpoint-dominated fundamental mode, $q\ll1$ and

$$
\frac{m_r}{\mu}=q^2+\frac{q^4}{3}+O(q^6).
$$

No massless support is required.

## 6.2 Total branch quadrupole

Including endpoint masses and spoke rest mass,

$$
\boxed{
\Delta Q_{xx}
=8\mu L u_c\frac{\tan q}{q},
}
$$

$$
\boxed{
\Delta Q_{yy}
=-8\mu L u_c\frac{\tan q}{q}.
}
$$

For $0<q<\pi/2$,

$$
\frac{\tan q}{q}>1,
$$

so the support does **not** cancel the endpoint quadrupole. It reinforces it.

For $q\ll1$,

$$
\boxed{
\frac{\tan q}{q}
=1+\frac{q^2}{3}+\frac{2q^4}{15}+O(q^6).
}
$$

The endpoint-only source is therefore the controlled $q\to0$ limit.

## 6.3 Correct mode mass and quantum matrix element

The generalized mode mass is

$$
\boxed{
M_{\rm eff}(q)
=4\mu\left[
\frac12+\frac{q}{\sin2q}
\right].
}
$$

Define

$$
A(q)=\frac12+\frac{q}{\sin2q}.
$$

Then

$$
A(q)=1+\frac{q^2}{3}+\frac{7q^4}{45}+O(q^6).
$$

The corrected transition matrix element is

$$
\boxed{
q_{01}^{\rm tot}(q)
=4\mu L\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}(q)\omega}}.
}
$$

Relative to the endpoint-only expression,

$$
\boxed{
\mathcal C_Q(q)
=\frac{\tan q/q}{\sqrt{A(q)}}
=1+\frac{q^2}{6}+O(q^4).
}
$$

## 6.4 Correct finite-spoke graviton linewidth

For the plus mode,

$$
\kappa_g
=\frac{4G\omega^5}{5\hbar c^5}|q_{01}|^2.
$$

Hence

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}{A(q)}.
}
$$

For $q\ll1$,

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\left[1+\frac{q^2}{3}+O(q^4)\right].
}
$$

The repository's previous endpoint-only linewidth is the controlled $q\to0$ limit.

## 6.5 Controller branch record

The new source note also gives an autonomous controller form

$$
H=H_m+H_c-\sigma_z g(q_c)u.
$$

A controlled mechanical-parity transformation removes the source-qubit label from the nongravitational source/controller dynamics. This is the argument that the work reservoir need not acquire a hidden which-branch record before gravitational coupling is included.

### Scope

This is a controlled nonrelativistic/weak-field model, not a complete covariant hyperelastic material realization. Relevant small parameters include

$$
|u_c|/L\ll1,
\qquad
q=\omega L/c_s\ll1,
\qquad
\beta=\omega L/c\ll1,
\qquad
\mathcal C\ll1.
$$

Do not inflate the scope beyond that.

### Presentation note

The initial version of `CONSERVED_SOURCE_ACTUATOR_AUDIT.md` contains a few apparent LaTeX transcription typos such as `\rac` where `\frac` is intended. Re-fetch before fixing; another agent may already have corrected them.

---

# 7. Gravitational difference mode

The branch coherent-state distance is

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

For a narrow-band plus quadrupole,

$$
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}{5\hbar c^5}.
$$

Keep separate:

- source branch strength $N_\Delta$;
- free-space / mode overlap;
- intrinsic receiver coupling.

The immediate task is to propagate the corrected finite-spoke matrix element into $N_\Delta$ and verify that previous source scalings survive with controlled $O(q^2)$ corrections.

---

# 8. Retarded source→receiver map

For aligned plus quadrupoles,

$$
\boxed{
\Sigma_{AB}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
\qquad
\epsilon=\omega R/c,
}
$$

with

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

The storage amplitude is

$$
\boxed{
t_{BA}^{\rm store}
=\frac{-i\Sigma_{BA}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}.
}
$$

In the wave zone,

$$
\boxed{
\eta_{\rm store}(R)
\simeq\frac{25\mathcal O}{16(kR)^2}.
}
$$

The $25/16$ coefficient has independent checks from

1. retarded Green/input-output normalization;
2. plus-quadrupole power pattern × critical $l=2$ absorption cross section;
3. electromagnetic dipole control giving $9/[16(kR)^2]$.

Do **not** use the old $25/[4(kR)^2]$ as coherent storage efficiency; that corresponds to the larger scattering/extinction normalization.

Read:

- `DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md`
- `NORMALIZED_GRAVITATIONAL_CROSS_RESPONSE.md`
- `INDEPENDENT_CROSS_RESPONSE_CHECK.md`
- `STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`

---

# 9. Receiver bookkeeping

The intrinsic receiver linewidth is

$$
\boxed{
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}Q_{ij}^{10}Q_{ij}^{01}.
}
$$

Range does **not** reduce this intrinsic linewidth. Range reduces only the selected source-mode coupling:

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g.
}
$$

---

# 10. Fixed physical waveform correction

The old logarithmic "quantum reception cone" is an **optimized protocol envelope**, not the trajectory of a single physical emitted pulse.

For fixed normalized waveform $f(t)$,

$$
\boxed{
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t e^{-\kappa(t-s)/2}f(s)\,ds
\right|^2.
}
$$

The receiver's branch-independent occupation is

$$
m(t)
=\bar n_0e^{-\kappa t}
+\frac{\Gamma_{\rm th}}{\kappa}(1-e^{-\kappa t}).
$$

The instantaneous non-EB condition is

$$
\boxed{\tau_f(t)>m(t).}
$$

Do not re-promote the waveform-optimized front as a universal physical prediction.

---

# 11. Preferred finite pulse and quantum window

For the mechanically closed $\sin^4$ source pulse, the receiver can exhibit

$$
\boxed{
\mathrm{EB}\to\mathrm{non\!-\!EB}\to\mathrm{EB}.
}
$$

The dimensionless loading maximum is

$$
H_*\simeq0.8136763,
$$

so a non-EB interval requires

$$
\boxed{
\kappa_\Delta>1.22899\,\Gamma_{\rm th}.
}
$$

This finite capability bubble/window is the physical replacement for the old indefinitely expanding logarithmic cone.

Read:

- `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`
- `SIN4_MECHANICAL_SOURCE_QUANTUM_WINDOW.md`

---

# 12. Passive receiver bounds: keep scope narrow

For passive nonrelativistic receivers,

$$
\boxed{
\frac{\kappa_g}{\omega}
\lesssim\frac23\mathcal C\beta^3,
}
$$

with

$$
\mathcal C=\frac{r_s}{L},
\qquad
\beta=\frac{\omega L}{c}.
$$

Do not call the older $\beta^5$ scaling universal; the extra $\beta^2$ came from a literal geometric-aperture assumption.

Do not extrapolate the passive nonrelativistic sum-rule ceiling to arbitrary relativistic QFT receivers, active/inverted systems, or strongly self-gravitating objects.

---

# 13. Accessibility is separate from absorption

For Gaussian capture $(\tau_c,m_c)$ followed by readout $(\tau_r,m_r)$,

$$
\tau_{\rm tot}=\tau_c\tau_r,
\qquad
m_{\rm tot}=\tau_rm_c+m_r.
$$

The accessible output remains quantum-capable iff

$$
\boxed{\tau_r(\tau_c-m_c)>m_r.}
$$

This separates capture, retained coherence, and operational readout.

---

# 14. Practical scale

The gravity work is presently a **theoretical channel-structure result**, not a near-term experimental proposal.

The repo's deliberately aggressive kilogram/meter/MHz/$Q\sim10^{12}$/perfect-overlap benchmark still produces optimized passive source-receiver negativity only around

$$
\sim10^{-22}.
$$

Do not market the present architecture as experimentally imminent.

---

# 15. Highest-value next work

The source-conservation loophole is no longer the unresolved starting point. It has an explicit controlled solution. The next task is to **propagate and attack that solution through the full gravity chain**.

Unless live `main` has advanced further, proceed in this order.

## A. Update canonical source formulas

Insert

$$
q=\omega L/c_s
$$

and replace endpoint-only quantities by either the exact four-spoke factors or expressions explicitly labeled as the $q\ll1$ limit.

## B. Recompute emitted branch mode

Use

$$
q_{01}^{\rm tot}(q)
$$

to recompute the emitted coherent-graviton norm $N_\Delta$ and determine the exact finite-$q$ correction.

## C. Re-audit source→receiver normalization

Insert the corrected source transition into $\Sigma_{AB}^R$ and the normalized source output. Verify rather than assume that the dimensionless far-zone storage factor

$$
25/[16(kR)^2]
$$

remains unchanged after source normalization cancels.

## D. Re-audit the $\sin^4$ capability window

Determine whether finite-spoke corrections affect only source/linewidth strength or alter any normalized waveform quantity entering the EB→non-EB→EB window.

## E. Attack the new source model

Check for:

- missing controller momentum flux;
- boundary-condition sign errors;
- misuse of the conserved quadrupole identity;
- branch-odd elastic/internal-energy terms at the same order;
- errors in $M_{\rm eff}$, $q_{01}^{\rm tot}$, or $\kappa_g(q)$;
- finite hub/controller branch dependence;
- inconsistent simultaneous assumptions $q\ll1$ and $\beta\ll1$;
- endpoint-only expressions still used elsewhere without a $q\to0$ label.

## F. Only then rebuild the gravity paper core

The paper should distinguish

- causal signal arrival;
- quantum-channel capability;
- finite certification strength;
- source conservation;
- receiver accessibility;
- practical feasibility.

---

# 16. Superseded / killed claims not to resurrect

Unless newer evidence explicitly reopens them:

- standalone novelty of Schmidt-rank-two Gaussian EB testing;
- standalone novelty of all-finite binary coherent survival;
- standalone novelty of the matched coherent displacement $v_*$;
- generic novelty of coherent-state Gaussian EB benchmarking;
- old universal logarithmic quantum cone for one physical pulse;
- $25/[4(kR)^2]$ as coherent storage efficiency;
- universal $\beta^5$ passive-receiver suppression;
- universal Planck-area absorption/linewidth bound for all gravitational receivers;
- stronger source amplitude automatically improving channel quality;
- all source-receiver entanglement vanishing outside the light cone;
- the statement that actuator stress-energy is still completely unspecified.

---

# 17. Numerical support

Committed checks exist for

- thermal attenuation;
- thermal amplification;
- additive Gaussian noise;
- near-boundary convergence.

Read:

- `experiments/01-causal-quantum-branch-information/numerics/README.md`
- `NUMERICAL_AUDIT_AMPLIFIER_ADDITIVE_NOISE.md`
- `NUMERICAL_NEAR_BOUNDARY_STRESS_RESULTS.md`

These are regression/supporting checks, not the origin of the analytic sign results.

---

# 18. Recovery reading order

After refreshing live `main`:

1. `AGENTS.md` — authoritative active recovery note.
2. `CONTEXT_HANDOFF.md` — compact continuity snapshot.
3. latest commits after the snapshot SHA at the top.
4. `README.md`.
5. `experiments/01-causal-quantum-branch-information/CONSERVED_SOURCE_ACTUATOR_AUDIT.md`.
6. `experiments/01-causal-quantum-branch-information/STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`.
7. `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`.
8. `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`.
9. current state / claim ledger files.
10. `QUANTIZED_PLUS_MODE_SOURCE.md`.
11. `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`.
12. `EXPLICIT_FOUR_MASS_SOURCE_RECEIVER_LINK.md`.
13. `DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md`.
14. `STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`.
15. `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`.
16. `SIN4_MECHANICAL_SOURCE_QUANTUM_WINDOW.md`.
17. passive/QFT receiver notes only as needed.

Do not reread every historical checkpoint unless reconstructing a correction. Many checkpoint claims were superseded later the same day.

---

# 19. Research method

Work adversarially rather than accumulatively.

For every strong result, attack in this order:

1. counterexample;
2. hidden assumption;
3. normalization / factor-of-two / convention error;
4. singular limit;
5. conservation-law failure;
6. stronger theorem making the result a corollary;
7. prior art under different notation;
8. numerical truncation artifact;
9. omitted subsystem of a supposedly closed physical model;
10. scope inflation.

When a headline claim dies, preserve correct mathematics but downgrade novelty immediately.

---

# 20. Maintaining this handoff

When approaching context exhaustion or after a major state transition:

1. fetch newest `main` HEAD;
2. compare it with the snapshot SHA at the top;
3. read intervening relevant changes;
4. re-fetch this exact file and update only from its current blob SHA;
5. refresh snapshot SHA/date;
6. update **STOP**, **current strongest result**, and **highest-value next work** first;
7. preserve killed claims so later agents do not rediscover and re-promote them;
8. keep canonical equations needed to prevent convention drift;
9. prefer file paths over duplicating full derivations;
10. if this file conflicts with a newer committed technical note, **newer live `main` wins**.
