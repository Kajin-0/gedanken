# CONTEXT_HANDOFF.md — Live Agent Continuity File

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Snapshot base:** `9a5934fc803b840c2e90e9aabecabeace8e373fc`  
**Snapshot date:** 2026-08-07 23:08 EDT  
**Purpose:** allow a new agent to recover the current research state quickly when another agent reaches its context limit.

> **This file is a snapshot, not authority over live `main`. The repository is being edited concurrently. Before doing any work, fetch the current `main` head and compare it with the snapshot SHA above. If `main` has advanced, read the intervening commits and changed files before trusting anything below.**

---

## 0. Mandatory concurrency protocol

This repository may have another agent editing it at the same time.

Before **every write**:

1. Fetch the current `main` HEAD.
2. Compare it with the HEAD you last read.
3. If HEAD changed, inspect all changed files relevant to your intended edit.
4. Re-fetch the exact target file immediately before updating it.
5. Never overwrite a file from an old blob SHA.
6. Prefer adding a new narrowly scoped file over rewriting a live coordination file unless the existing file clearly requires synchronization.
7. If another agent has changed the research direction, follow the newer state rather than this snapshot.

After a material discovery, update the claim ledger / state documentation in the same research pass so future agents do not resurrect dead claims.

---

# 1. Project in one sentence

The project asks when a branch-dependent gravitational signal can propagate causally into a distant quantum receiver **while preserving quantum branch coherence**, rather than merely creating a classical branch record.

The work evolved through quantum-information channel theory, exact Gaussian entanglement witnesses, linearized-gravity input-output theory, source/receiver mode matching, and explicit finite source-waveform dynamics.

The current publication focus has returned to the **gravity application** after two major prior-art collisions killed the standalone Gaussian-theorem paper.

---

# 2. Current top-level decision

## STOP: standalone Gaussian theorem paper

As of snapshot HEAD `9a5934fc...`, the repository explicitly records:

> **STOP AS A STANDALONE THEOREM PAPER; RETAIN AS LEMMAS/TOOLS FOR THE GRAVITY APPLICATION.**

Read first:

- `AGENTS.md`
- `experiments/01-causal-quantum-branch-information/STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
- `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `experiments/01-causal-quantum-branch-information/THREE_ELEMENT_WITNESS_VS_FILIPPOV.md`

### Why the paper was stopped

Two independent headline novelty claims collided with prior art.

### Collision A — Mele–Lami–Giovannetti

The repository independently found that a Schmidt-rank-two Fock probe

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}}
$$

has a partial-transpose block determinant

$$
\det M_s
=\frac{s^2}{(1+s^2)^2}
\frac{m-\tau}{(m+1)^3},
$$

so for a phase-insensitive Gaussian channel the output is NPT iff

$$
\tau>m.
$$

The mathematics is useful, but the finite-Fock-pair survival structure was already present in Mele–Lami–Giovannetti. Do **not** revive the claim that Schmidt rank two detecting the non-EB phase-insensitive region is new.

### Collision B — Filippov–Ziman (2014)

The repository also independently proved that every finite nontrivial binary coherent hybrid probe survives with NPT output exactly in the non-EB phase-insensitive region.

Filippov–Ziman's weighted coherent-state witness, after one-sided specialization plus an invertible local filter on the untouched two-dimensional coherent support, already implies that survival result.

More strongly, the latest audit found that the repository's matched coherent scale and exponential sign factor are algebraically encoded in the Filippov–Ziman witness family.

With their parameter chosen so that

$$
1-\lambda=t=\frac{m}{\sqrt\tau},
$$

their witness contains

$$
1-
\exp\left[
\frac{|\gamma|^2}{m}(\tau-m)
\right],
$$

and for $|\gamma|=2a$ this is

$$
1-
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
$$

Their coherent-kernel mapping gives the same matched displacement

$$
v_*=\frac{2\sqrt\tau a}{m}.
$$

Therefore do **not** claim the all-finite-binary-coherent survival theorem, the matched displacement, or the exponential sign structure as a new standalone theorem.

---

# 3. Gaussian mathematics that remains valid and useful

The novelty loss does **not** mean the derivations are wrong. They are valuable as compact tools for the gravity calculation.

## 3.1 Phase-insensitive convention

The repository uses

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=
\chi_O(\sqrt\tau\xi)
\exp\left[-\frac{2m+1-\tau}{2}|\xi|^2\right].
$$

The entanglement-breaking boundary is

$$
\boxed{m\ge\tau}.
$$

Non-EB region:

$$
\boxed{\tau>m}.
$$

## 3.2 Fixed rank-two Fock test

For the symmetric state

$$
|\Phi_2\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
$$

the relevant process elements are

$$
A_{11}=\frac{m}{(m+1)^2},
$$

$$
B_{00}=\frac{m+1-\tau}{(m+1)^2},
$$

$$
X_{01}=\frac{\sqrt\tau}{(m+1)^2}.
$$

The selected PT block has

$$
\det M_{01}
=\frac{m-\tau}{4(m+1)^3}.
$$

The negative eigenvalue simplifies to

$$
\mu_-=
\frac{m-\tau}{2(m+1)^2},
$$

so the full output negativity obeys

$$
\mathcal N_{\rm out}
\ge
\frac{[\tau-m]_+}{2(m+1)^2}.
$$

Treat this as a compact independent proof / quantitative lemma, not the basis of a novelty claim.

## 3.3 Binary coherent principal minor

For symmetric branches $|\pm a\rangle$ and $m>0$, choose

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m}}.
$$

The selected principal-minor ratio is

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

Hence the block is negative iff $\tau>m$.

The selected block's negative eigenvalue gives the rigorous lower bound

$$
G(v)=\frac12
\max\left\{0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
$$

In the weak-link regime, the repository derives

$$
G_{\rm abs}^{\rm opt}
=
\frac{W(e^{-1})}{2}(\tau-m)+O(\tau^2),
$$

with

$$
\frac{W(e^{-1})}{2}\simeq0.1392322714,
$$

and optimal source amplitude

$$
a_*\simeq0.565346\sqrt\tau.
$$

These may still be useful quantitative corollaries. Do not assume they are novel without another literature audit.

---

# 4. Current gravity architecture

The gravity application is now the primary research branch.

The intended conceptual chain is

$$
\boxed{
\text{source qubit}
\to
\text{quantized branch-dependent quadrupole}
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

The question is not merely whether a classical gravitational waveform arrives. It is whether the complete source-controlled receiver channel becomes non-entanglement-breaking after causal contact.

---

# 5. Causality formulation that should be preserved

Do **not** state that all source-receiver entanglement must vanish outside the light cone. Vacuum correlations and entanglement harvesting make that too broad.

Use the source-controlled channel statement instead.

Define

$$
\mathcal A_{R,t}:
\text{controllable incoming branch mode}
\to
\text{accessible receiver register at time }t.
$$

Microcausality implies that before causal contact the source-controlled map is a replacer channel,

$$
\mathcal A_{R,t}(\rho)
=
\sigma_{R,t}\operatorname{Tr}\rho,
\qquad t<R/c,
$$

and is therefore EB.

This is the clean causal theorem.

Read:

- `GENERAL_CAUSAL_QUANTUM_CHANNEL_FRONT.md`
- `MICROCAUSAL_REPLACER_THEOREM.md`
- `ACCESSIBLE_RECEIVER_CASCADE_THEOREM.md`

---

# 6. Gravitational source and difference mode

The branch-dependent gravitational radiation is compressed into one normalized bosonic **difference mode** containing all coherent $L/R$ distinguishability.

The branch coherent-state distance is

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

For a narrow-band plus quadrupole,

$$
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}{5\hbar c^5}.
$$

Important distinction:

- $N_\Delta$ is **source strength / branch separation**.
- It controls entanglement/witness magnitude.
- It does not by itself improve the receiver channel quality.

Read:

- `GRAVITATIONAL_DIFFERENCE_MODE_AMPLITUDE.md`
- `QUANTIZED_PLUS_MODE_SOURCE.md`
- `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`
- `EXPLICIT_FOUR_MASS_SOURCE_RECEIVER_LINK.md`

---

# 7. Retarded quadrupole response and storage normalization

For aligned plus quadrupoles, the exact retarded cross self-energy is

$$
\boxed{
\Sigma_{AB}^{R}
=
\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
\qquad
\epsilon=\omega R/c,
}
$$

with

$$
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

The coherent source-output to receiver-input storage amplitude is

$$
\boxed{
t_{BA}^{\rm store}
=
\frac{-i\Sigma_{BA}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}.
}
$$

In the far zone,

$$
\boxed{
\eta_{\rm store}(R)
\simeq
\frac{25\mathcal O}{16(kR)^2}.
}
$$

The $25/16$ coefficient has been checked by three routes:

1. retarded Green function / input-output normalization;
2. quadrupole on-axis power fraction times critical $l=2$ **absorption** cross section;
3. electromagnetic dipole control, which reproduces $9/[16(kR)^2]$.

Do **not** use the old

$$
25/[4(kR)^2]
$$

as a storage probability. That larger factor is tied to the unitary scattering/extinction normalization, not coherent state storage.

Read:

- `DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md`
- `NORMALIZED_GRAVITATIONAL_CROSS_RESPONSE.md`
- `INDEPENDENT_CROSS_RESPONSE_CHECK.md`
- `STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`

---

# 8. Receiver bookkeeping

The receiver intrinsic gravitational linewidth is

$$
\boxed{
\kappa_g
=
\frac{2G\omega^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

Distance does **not** reduce this intrinsic linewidth.

Distance reduces the fraction of the receiver gravitational bath occupied by the selected source mode:

$$
\boxed{
\kappa_\Delta(R)
=
\frac{25\mathcal O}{16(kR)^2}\kappa_g.
}
$$

Keep source strength, propagation/mode overlap, and intrinsic receiver coupling separate.

---

# 9. Fixed physical waveform correction

One of the most important corrections in the repository is that the old logarithmic "quantum reception cone" was an **optimized protocol envelope**, not the time evolution of a single physical source pulse.

For a fixed emitted normalized waveform $f(t)$, the actual coherent capture parameter is

$$
\boxed{
\tau_f(t)
=
\kappa_\Delta
\left|
\int_0^t
 e^{-\kappa(t-s)/2}f(s)\,ds
\right|^2.
}
$$

The branch-independent receiver occupation is

$$
m(t)
=
\bar n_0e^{-\kappa t}
+
\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-\kappa t}).
$$

For the phase-insensitive effective channel, the instantaneous non-EB condition is

$$
\boxed{\tau_f(t)>m(t).}
$$

Do not re-promote the waveform-optimized front as a universal physical trajectory.

Read:

- `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`
- `CURRENT_STATE.md`
- `SIN4_MECHANICAL_SOURCE_QUANTUM_WINDOW.md`

---

# 10. Mechanically closed source result

The preferred finite source waveform is the mechanically closed $\sin^4$ source pulse.

For this source, the receiver can display the finite-time sequence

$$
\boxed{
\mathrm{EB}
\to
\mathrm{non\!-\!EB}
\to
\mathrm{EB}.
}
$$

The optimized dimensionless loading maximum is approximately

$$
H_*\simeq0.8136763,
$$

which gives the source-specific condition

$$
\boxed{
\kappa_\Delta
>
1.22899\,\Gamma_{\rm th}
}
$$

for any non-EB interval in that model.

This finite capability **bubble/window** is the physically relevant replacement for the old indefinitely expanding logarithmic front.

---

# 11. Passive receiver limits — preserve the corrected scope

For a passive nonrelativistic receiver, the current robust quadrupole oscillator-strength bound is

$$
\boxed{
\frac{\kappa_g}{\omega}
\lesssim
\frac23\mathcal C\beta^3,
}
$$

with

$$
\mathcal C=\frac{r_s}{L},
\qquad
\beta=\frac{\omega L}{c}.
$$

Do **not** call the older $\beta^5$ scaling universal. The extra $\beta^2$ arose from a literal geometric-aperture assumption.

Also do not extrapolate the passive nonrelativistic sum-rule ceiling to arbitrary relativistic QFT receivers, active/inverted systems, or strongly self-gravitating compact objects.

Read:

- `PASSIVE_RECEIVER_SUM_RULE.md`
- `QUADRUPOLE_SUM_RULE_BOUND.md`
- `PASSIVE_WAVEZONE_FEASIBILITY_BOUND.md`
- `VACUUM_PASSIVE_ENTANGLEMENT_CEILING.md`
- `FREE_FIELD_STRESS_TEST.md`
- `KMS_MODE_EFFICIENCY.md`

---

# 12. Accessibility is a separate stage

Do not equate strong gravitational absorption with useful accessible quantum memory.

For Gaussian capture followed by Gaussian readout,

$$
\tau_{\rm tot}=\tau_c\tau_r,
$$

$$
m_{\rm tot}=\tau_rm_c+m_r,
$$

and the accessible output is non-EB/NPT-capable iff

$$
\boxed{
\tau_r(\tau_c-m_c)>m_r.
}
$$

This separates

1. capture;
2. retained coherence;
3. operational accessibility/readout.

This distinction matters especially for compact-object receiver thought experiments.

---

# 13. Practical gravity scale

The repository contains intentionally aggressive benchmarks demonstrating that the gravity application is presently a **theoretical structure result**, not a near-term experimental proposal.

A representative extreme benchmark with kilogram-scale masses, meter scale, MHz frequency, $Q\sim10^{12}$, perfect overlap, and wave-zone separation still gives optimized passive source-receiver negativity around

$$
\sim10^{-22}.
$$

Do not market the current model as experimentally imminent.

---

# 14. Highest-value unresolved technical problem

This is the most important current research target.

The source masses have an explicit quantized plus mode and branch-dependent driving, but the **complete actuator/control subsystem has not yet been promoted to an explicit autonomous conserved stress-energy source**.

A referee can attack the gravity paper by saying:

> the unspecified actuator/support may carry compensating branch-dependent energy, momentum, and stress that modifies or cancels the claimed radiative quadrupole.

The next source model must satisfy

$$
\boxed{
\partial_\mu T^{\mu\nu}_{\rm total}=0
}
$$

through the complete branch history.

The target is to compute the gravitational radiation and source-to-receiver coupling from the **total** conserved source-plus-actuator $T^{\mu\nu}$, not just the endpoint masses.

### Required adversarial questions

1. Does actuator stress modify the branch-dependent radiative quadrupole at leading order?
2. Is there an exact conservation cancellation hidden by the endpoint-mass model?
3. What is the minimal internally closed source architecture with a nonzero surviving branch-dependent radiative multipole?
4. Can the quantum branch-control degree of freedom return to its initial state while the mechanical source executes the required closed excursion?
5. Are emitted branch graviton modes still the claimed plus-mode wavepacket after full stress-energy conservation is enforced?
6. Does the $25/[16(kR)^2]$ receiver normalization survive unchanged once the actual conserved source mode is inserted?

This is currently higher value than additional Gaussian-channel algebra.

---

# 15. Do not resurrect these superseded claims

A new agent should treat the following as **dead or narrowed** unless new evidence explicitly reopens them:

- standalone novelty of Schmidt-rank-two Gaussian EB testing;
- standalone novelty of all-finite binary coherent survival;
- standalone novelty of the matched coherent analysis displacement $v_*$;
- generic claim that simple coherent resources newly detect Gaussian EB boundaries;
- old universal logarithmic "quantum cone" for a single physical pulse;
- $25/[4(kR)^2]$ as coherent storage efficiency;
- universal $\beta^5$ passive-receiver suppression;
- universal Planck-area absorption/linewidth limit for all gravitational receivers;
- any claim that stronger source amplitude automatically improves the channel itself;
- any statement that all source-receiver entanglement must vanish outside the light cone.

---

# 16. Numerics

Committed numerical checks exist for

- thermal attenuation;
- thermal amplification;
- additive Gaussian noise;
- near-boundary convergence.

Read:

- `experiments/01-causal-quantum-branch-information/numerics/README.md`
- `NUMERICAL_AUDIT_AMPLIFIER_ADDITIVE_NOISE.md`
- `NUMERICAL_NEAR_BOUNDARY_STRESS_RESULTS.md`

The numerical work is supporting evidence / regression checking, not the source of the analytic sign theorems.

---

# 17. Recommended recovery reading order

After refreshing live `main`, use this order.

1. `AGENTS.md`
2. `CONTEXT_HANDOFF.md`
3. `experiments/01-causal-quantum-branch-information/STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
4. `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`
5. `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
6. `experiments/01-causal-quantum-branch-information/THREE_ELEMENT_WITNESS_VS_FILIPPOV.md`
7. `experiments/01-causal-quantum-branch-information/CURRENT_STATE.md`
8. `experiments/01-causal-quantum-branch-information/CLAIM_LEDGER.md` and any newer addenda
9. `experiments/01-causal-quantum-branch-information/QUANTIZED_PLUS_MODE_SOURCE.md`
10. `experiments/01-causal-quantum-branch-information/CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`
11. `experiments/01-causal-quantum-branch-information/EXPLICIT_FOUR_MASS_SOURCE_RECEIVER_LINK.md`
12. `experiments/01-causal-quantum-branch-information/DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md`
13. `experiments/01-causal-quantum-branch-information/STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`
14. `experiments/01-causal-quantum-branch-information/GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`
15. `experiments/01-causal-quantum-branch-information/SIN4_MECHANICAL_SOURCE_QUANTUM_WINDOW.md`
16. passive/QFT receiver files only as needed for the next question.

Do not reread every historical checkpoint unless reconstructing how a correction arose. Many checkpoint claims were superseded later the same day.

---

# 18. Research method expected in this repo

The correct working style is adversarial rather than accumulative.

For every apparently strong result, attempt in this order:

1. counterexample;
2. hidden assumption;
3. factor-of-two / normalization / convention failure;
4. singular limit;
5. conservation-law failure;
6. stronger theorem making the result trivial;
7. prior art under different notation;
8. numerical truncation artifact;
9. scope inflation.

When prior art kills a headline claim, preserve correct mathematics but immediately downgrade the novelty language.

The project has improved precisely because attractive claims were allowed to die.

---

# 19. What a new agent should do next

Unless live `main` has moved to a newer task, the preferred next sequence is:

### A. Close the source-conservation hole

Construct an explicit internally closed actuator + four-mass model and write a conserved $T^{\mu\nu}_{\rm total}$.

### B. Recompute the branch radiative multipole

Do not assume the endpoint-mass quadrupole survives unchanged. Derive it from total stress-energy conservation.

### C. Recompute the emitted difference mode

Obtain the corrected

$$
\Delta\widetilde Q_{ij}(\omega)
$$

and therefore

$$
N_\Delta.
$$

### D. Reinsert it into the established propagation/receiver map

Use the already-audited storage normalization and fixed-waveform receiver convolution.

### E. Only then rebuild the gravity paper

The paper should clearly separate

- causal signal arrival;
- quantum-channel capability;
- finite certification strength;
- receiver accessibility;
- practical feasibility.

---

# 20. How to maintain this file

When an agent is approaching context exhaustion or after a major state transition:

1. fetch the newest `main` HEAD;
2. compare it with the `Snapshot base` at the top;
3. update this file only after incorporating intervening changes;
4. replace the snapshot SHA/date;
5. update **STOP**, **GO**, and **highest-value unresolved problem** sections first;
6. preserve a short note about major killed claims so later agents do not rediscover and re-promote them;
7. keep equations only when they are canonical enough to prevent convention drift;
8. prefer links/file paths to long duplicated derivations.

If this file conflicts with newer committed research notes, **newer live `main` wins**.
