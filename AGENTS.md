# AGENTS.md — Research Recovery and Continuation Protocol

**Repository:** `Kajin-0/gedanken`  
**Primary active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Last canonical update:** 2026-08-07 22:22 EDT  

This file is the first document a new research agent should read. It exists so that a context-window reset does not cause the project to rediscover old results, resurrect superseded novelty claims, or lose the current proof/novelty boundary.

---

## 1. Research rule

The project is run adversarially.

The objective is **not** to defend a preferred theorem. The objective is to kill every claim that can be killed by

1. a counterexample;
2. a hidden assumption;
3. a convention mismatch;
4. a stronger or equivalent prior-art theorem;
5. an invalid limiting argument;
6. a numerical artifact;
7. a model-dependence that was presented as generality.

A result survives only after those attacks fail.

Whenever a claim is weakened or killed, update the documentation immediately. Do not leave a stale paper core or current-state file implying novelty that the project no longer believes.

---

## 2. Current high-level verdict

### Mathematics that currently appears correct

For the phase-insensitive one-mode Gaussian channel in the repository convention

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp[-(2m+1-\tau)|\xi|^2/2],
$$

the entanglement-breaking boundary is

$$
\boxed{\Phi_{\tau,m}\in\mathrm{EB}\iff m\ge\tau.}
$$

The repository's Fock rank-two calculation is algebraically correct:

$$
|\psi_\lambda\rangle
=\frac{|00\rangle+\lambda|11\rangle}{\sqrt{1+\lambda^2}},
$$

$$
M_\lambda=
\frac{1}{(1+\lambda^2)(m+1)^2}
\begin{pmatrix}
m&\lambda\sqrt\tau\\
\lambda\sqrt\tau&\lambda^2(m+1-\tau)
\end{pmatrix},
$$

$$
\boxed{
\det M_\lambda=
\frac{\lambda^2}{(1+\lambda^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

Thus the output is NPT for every $\lambda>0$ iff $\tau>m$.

**Do not claim this rank-two Fock result as novel.** See Section 3.

### Current surviving candidate novelty

The strongest surviving non-gravity candidate is instead the **all-binary-coherent-pairs theorem**:

For every finite nontrivial state

$$
|\Psi\rangle
=\sqrt p\,|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}\,|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,\qquad \alpha\ne\beta,
$$

the repository proves for every gauge-covariant phase-insensitive Gaussian channel

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

This candidate remains **novelty unverified**. It is the first priority to attack.

A second candidate is the associated exact low-dimensional coherent-state witness using only two populations and one coherence.

---

## 3. Confirmed fatal prior-art collision: Mele–Lami–Giovannetti

Read first:

`experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`

Primary source:

F. A. Mele, L. Lami, and V. Giovannetti,  
“Maximum tolerable excess noise in continuous-variable quantum key distribution and improved lower bound on two-way capacities,”  
arXiv:2303.12867 (submitted 22 March 2023), later *Nature Photonics* (2025), DOI `10.1038/s41566-024-01595-9`.

Their supplement defines

$$
\mathcal N_{g,\lambda}
=\Phi_{g,0}\circ\mathcal E_{\lambda,0}
$$

and uses the finite Schmidt-rank-two family

$$
|\Psi_{M,c}\rangle
=c|0,0\rangle+\sqrt{1-c^2}|M,M\rangle,
$$

for arbitrary

$$
M\in\mathbb N^+,\qquad c\in(0,1).
$$

After Bob locally projects onto

$$
\Pi_M=|0\rangle\langle0|+|M\rangle\langle M|,
$$

Supplementary Remark 1 proves that the resulting two-qubit state is non-PPT/distillable iff

$$
\boxed{(1-\lambda)g<1,}
$$

independently of $c$ and $M$.

For this normal form, the repository parameters are

$$
\tau=g\lambda,
\qquad
m=g-1.
$$

Therefore

$$
(1-\lambda)g<1
\iff
g\lambda>g-1
\iff
\boxed{\tau>m}.
$$

Setting

$$
M=1,
\qquad
c=1/\sqrt2
$$

gives the repository's fixed vacuum–one-photon Bell probe.

Local CP filtering cannot convert a PPT state into an NPT state. Therefore their post-filter NPT result already implies NPT of the unfiltered output.

### Consequence

The following must be treated as prior art / rediscovery, not headline novelty:

- phase-insensitive Schmidt-rank-two sufficiency;
- arbitrary nonzero Schmidt weight in $|00\rangle+\lambda|11\rangle$;
- fixed vacuum–one-photon Bell-state sufficiency;
- qubit-ancilla sufficiency for the phase-insensitive family;
- the fact that the exact sign boundary is $\tau-m$;
- the broad finite-Fock-pair phenomenon, which Mele et al. prove for every $M\ge1$.

The repository's determinant proof may still be a useful **shorter derivation**, but it is not a new theorem unless a demonstrably distinct statement is isolated.

For regular orientation-preserving one-mode Gaussian channels, the rank-two extension is largely an immediate corollary of this prior art plus standard Gaussian input/output canonicalization. The repository's finite $B_1$ regularization argument appears correct and closes a singular class, but it is not presently considered sufficient to support the previous standalone-paper headline.

---

## 4. Surviving coherent-state theorem: exact proof target

Canonical proof file:

`experiments/01-causal-quantum-branch-information/DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`

The key coherent-dyad identity is

$$
\boxed{
\langle u|\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)|v\rangle
=
\frac{\langle\beta|\alpha\rangle\langle u|v\rangle}{m+1}
\exp\left[
\frac{(\sqrt\tau\beta^*-u^*)(v-\sqrt\tau\alpha)}{m+1}
\right].
}
$$

For symmetric real branches $|\pm a\rangle$ and $m>0$, one exact $2\times2$ principal minor gives

$$
\ln R(v)
=-4a^2-v^2+
\frac{4\tau a^2+4\sqrt\tau av+v^2}{m+1}.
$$

The optimum is

$$
\boxed{v_*=\frac{2\sqrt\tau a}{m},}
$$

and

$$
\boxed{
R(v_*)
=\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

Hence, for every $a>0$,

$$
R(v_*)>1\iff\tau>m.
$$

Unequal branch weights contribute the same product $p(1-p)$ to the squared coherence and diagonal product and therefore cancel. A relative phase changes only the phase of the off-diagonal element. Arbitrary coherent pairs reduce to symmetric $|\pm a\rangle$ by displacement and phase covariance.

### Pure-loss edge

Read:

`experiments/01-causal-quantum-branch-information/PURE_LOSS_EDGE_CASE.md`

For $m=0$,

$$
\ln R(v)=4a^2(\tau-1)+4\sqrt\tau av.
$$

For every physical pure-loss channel with $\tau>0$, any finite

$$
\boxed{v>\frac{a(1-\tau)}{\sqrt\tau}}
$$

certifies NPT. At $\tau=0$ the channel is a vacuum replacer and EB.

A new agent should independently rederive these equations before trusting them.

---

## 5. Exact three-element witness candidate

Canonical file:

`experiments/01-causal-quantum-branch-information/EXACT_THREE_ELEMENT_WITNESS.md`

The witness uses a $2\times2$ block

$$
M_\Gamma=
\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}
$$

inside the partial transpose. The condition

$$
\boxed{|z_v|^2>p_0p_v}
$$

certifies NPT.

At the matched coherent displacement $v_*$ above, the witness reaches the full phase-insensitive EB boundary.

The exact novelty question is **not** whether principal-minor PPT witnesses exist. They certainly do. The question is whether prior work already showed that these particular three selected coherent-state matrix elements provide an exact iff test of the actual binary-hybrid output state for every finite nonzero coherent separation and every phase-insensitive Gaussian channel.

---

## 6. Closest coherent-state prior art already checked

### Häseler–Moroder–Lütkenhaus (2008)

arXiv:0711.2709, PRA 77, 032303.

Established:

- two nonorthogonal coherent states as a device/channel test;
- effective-entanglement representation;
- partial-transpose expectation-value matrices;
- coherent-state/homodyne practical benchmarks.

Their experimentally restricted criterion is based on limited measured moments. No exact all-finite-amplitude output-state NPT/EB equivalence has been located there.

### Kreis–van Loock (2012)

arXiv:1111.0478, PRA 85, 032307.

This is the most dangerous coherent-state predecessor because it studies the **same symmetric hybrid state and thermal beam-splitter channel**. They derive the noisy state but use a finite-order Shchukin–Vogel moment witness. Their sufficient threshold is amplitude dependent, and they explicitly note a region below the known EB boundary that their witness may fail to detect.

This is currently the strongest evidence that the repository's exact finite-amplitude NPT completion was not already obtained in that paper.

### Namiki–Azuma (2015)

arXiv:1404.2643, PRL 114, 140503.

Established a coherent-state ensemble benchmark that verifies quantum-domain performance for all one-mode Gaussian channels. This is not a single binary hybrid-state NPT theorem.

### Other neighboring areas that still need citation-forward search

- papers citing Kreis–van Loock on thermal hybrid entanglement;
- papers citing Häseler–Moroder–Lütkenhaus on two-state effective entanglement;
- Shchukin–Vogel moment/PPT hierarchies specialized to hybrid coherent cats;
- binary-modulated CV-QKD security/entanglement proofs;
- entangled coherent-state robustness under thermal attenuators/amplifiers;
- nonclassicality-breaking versus entanglement-breaking Gaussian channels;
- finite coherent alphabets as complete EB tests;
- hybrid qubit–oscillator negativity under additive Gaussian noise and amplifiers.

---

## 7. Immediate next research tasks, in order

### Priority 1 — try to kill the all-coherent-pairs theorem by prior art

Search at the **equation level**, not only title/abstract level.

Queries should include variants of:

- `binary coherent hybrid thermal channel NPT exact`
- `|0>|alpha> + |1>|-alpha> thermal noise partial transpose`
- `hybrid coherent state entanglement breaking boundary`
- `two coherent states complete entanglement breaking test Gaussian channel`
- `coherent state principal minor PPT thermal attenuator`
- `qubit mode coherent state negativity thermal amplifier`
- `binary coherent state additive Gaussian noise entanglement`
- `effective entanglement exact thermal channel coherent states`

Then do citation-forward searches from the 2008 Häseler paper and 2012 Kreis–van Loock paper.

A candidate collision only counts after the source is opened and its theorem/equations are compared explicitly with

$$
R(v_*)=\exp[4a^2(\tau-m)/m].
$$

### Priority 2 — try to kill the three-element witness

Search for exact low-dimensional coherent-state PT minors, displaced-vacuum projections, and hybrid entanglement witnesses that reach the EB boundary.

The novelty bar is narrow: an older result need not use the project's notation. If it measures or bounds the same matrix elements after displacement and proves the same iff boundary, the witness novelty is dead.

### Priority 3 — independent proof audit

Re-derive the coherent-dyad kernel from the Weyl characteristic function, checking all normalization conventions.

Then independently recompute

- $p_0$;
- $p_v$;
- $z_v$;
- $R(v)$;
- the maximizing $v_*$;
- $m=0$ separately;
- attenuation, amplifier, and additive-noise parameter maps.

Try complex $a,v$ before using covariance to reduce to the real line.

### Priority 4 — reproducibility

The repository currently commits only

`numerics/thermal_cat_scan.py`

for numerical channel simulation.

The reported thermal-amplifier and additive-noise numerical audits are documented in Markdown but their executable implementations are not committed. Reconstruct and commit them, together with

- dependency versions;
- convergence tests versus Fock cutoff/quadrature order;
- near-boundary scans;
- a random physical-parameter sweep comparing numerical PT sign with $\operatorname{sgn}(m-\tau)$.

A useful target is at least $10^3$ random physical parameter points plus dense sweeps near $|\tau-m|\lesssim10^{-4}$.

### Priority 5 — only then return to gravity

The gravity stream remains secondary until the coherent theorem's novelty boundary is settled.

The strongest gravity-specific unresolved technical item is the complete conserved actuator/control stress-energy for the explicit branch source. Do not invent another receiver architecture before closing that issue.

---

## 8. Known mathematical/writeup vulnerabilities

### Covariance convention mismatch

`ONE_MODE_GAUSSIAN_CANONICAL_CLASS_PROOF_AUDIT.md` declares a convention equivalent to

$$
V\mapsto K^T V K+\beta,
$$

but parts of its canonicalization are written with matrix ordering more natural for

$$
V\mapsto KVK^T+\beta.
$$

The standard canonical-equivalence theorem is not in doubt, but the manuscript derivation must be rewritten using one convention consistently. Do not publish the general-channel derivation until this is fixed.

### Do not infer novelty from proof simplicity

The Mele collision demonstrated that a result can be buried in a supplement under a different operational objective. Search supplements, appendices, and proofs, not just abstracts.

### Do not use numerical NPT at an EB point as evidence

Finite Fock truncations can produce small spurious negative PT eigenvalues in exactly EB channels. Require convergence toward zero and compare against analytic controls.

---

## 9. Documentation discipline

After every significant result, update at least the relevant subset of:

- `AGENTS.md`
- `experiments/01-causal-quantum-branch-information/CLAIM_LEDGER.md`
- `experiments/01-causal-quantum-branch-information/CURRENT_STATE_RANK2_UPDATE.md`
- the relevant `NOVELTY_*.md` file
- the relevant proof file if an algebraic correction is found.

Use these labels consistently:

- **ESTABLISHED PRIOR ART**
- **INTERNALLY DERIVED — MATHEMATICS AUDITED**
- **CANDIDATE NOVELTY — UNVERIFIED**
- **COLLISION CONFIRMED — DO NOT CLAIM**
- **SUPERSEDED / INCORRECT**

Never leave a killed claim described elsewhere as the project's strongest publication candidate.

---

## 10. Canonical reading order for a new agent

Read in this order:

1. `AGENTS.md`
2. `experiments/01-causal-quantum-branch-information/CURRENT_STATE_RANK2_UPDATE.md`
3. `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`
4. `experiments/01-causal-quantum-branch-information/CLAIM_LEDGER.md`
5. `experiments/01-causal-quantum-branch-information/DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
6. `experiments/01-causal-quantum-branch-information/PURE_LOSS_EDGE_CASE.md`
7. `experiments/01-causal-quantum-branch-information/EXACT_THREE_ELEMENT_WITNESS.md`
8. `experiments/01-causal-quantum-branch-information/NOVELTY_CHECK_GAUSSIAN_BINARY_PROBE.md`
9. `experiments/01-causal-quantum-branch-information/NOVELTY_CHECK_FINITE_CAT.md`
10. `experiments/01-causal-quantum-branch-information/PRIOR_ART_BINARY_COHERENT_TESTS.md`

Only after those should a new agent read the older rank-two paper cores or resume the gravity calculations.

---

## 11. Current stop/go decision

### STOP

Do not prepare or submit the previous standalone paper

**“Schmidt-Rank-Two Probes Suffice to Detect Entanglement Breaking in One-Mode Gaussian Channels”**

as a novelty claim in its current form.

### GO

Continue adversarial work on:

1. the exact all-finite-binary-coherent-pairs NPT/EB equivalence;
2. the exact matched three-element coherent-state witness;
3. reproducible numerical verification;
4. gravity only after the first two novelty questions are substantially resolved.
