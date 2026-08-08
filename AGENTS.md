# AGENTS.md — Canonical Research Recovery Point

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Checkpoint:** 2026-08-07, after the Mele rank-two collision, two coherent-state prior-art passes, independent proof rederivation, covariance-convention repair, and numerical reproducibility upgrade.

This is the first file a new agent should read.

---

## 1. Operating rule: try to kill the result

Do not defend repository claims because they are already written down.

Attack every candidate with

1. counterexamples;
2. hidden assumptions;
3. normalization/convention errors;
4. singular limits;
5. stronger prior art under different terminology;
6. numerical truncation artifacts;
7. scope inflation from a model-specific statement to a general one.

If a claim dies, update the documentation immediately. Never leave a killed result presented elsewhere as the active publication candidate.

---

## 2. Confirmed killed novelty: Schmidt-rank-two Fock theorem

The repository independently derived, for the phase-insensitive Gaussian channel,

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}},
$$

with

$$
\det M_s
=\frac{s^2}{(1+s^2)^2}
\frac{m-\tau}{(m+1)^3}.
$$

Thus the output is NPT iff

$$
\tau>m,
$$

the exact non-entanglement-breaking region.

**The mathematics appears correct. The novelty is dead.**

Mele, Lami, and Giovannetti, arXiv:2303.12867 / *Nature Photonics* (2025), already use

$$
|\Psi_{M,c}\rangle
=c|00\rangle+\sqrt{1-c^2}|MM\rangle
$$

for arbitrary $M\ge1$ and $0<c<1$, locally project onto $\{|0\rangle,|M\rangle\}$, and prove NPT/distillability exactly in the non-EB region.

Their normal-form condition

$$
(1-\lambda)g<1
$$

maps under

$$
\tau=g\lambda,
\qquad
m=g-1
$$

to

$$
\tau>m.
$$

Setting $M=1,c=1/\sqrt2$ gives the repository fixed Bell probe.

Read:

- `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `experiments/01-causal-quantum-branch-information/NOVELTY_AUDIT_SCHMIDT_RANK_TWO_GAUSSIAN_PROBE.md`

Do **not** resurrect the old standalone paper title about Schmidt-rank-two sufficiency as a discovery claim.

---

## 3. Active candidate theorem: every finite binary coherent pair

For

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\ne\beta,
$$

the repository proves for the gauge-covariant phase-insensitive channel $\Phi_{\tau,m}$

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

For symmetric real branches $|\pm a\rangle$ and $m>0$,

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and one coherent-state $2\times2$ PT principal minor gives

$$
\boxed{
R(v_*)
=\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

For pure loss $m=0$, use the separate finite condition

$$
\boxed{
v>\frac{a(1-\tau)}{\sqrt\tau}}
$$

for every $\tau>0$.

### Internal proof status

An independent rederivation has already checked

- the coherent-dyad characteristic function;
- Weyl reconstruction;
- the exact channel kernel;
- all three selected matrix elements;
- orthogonality of the compressed PT basis through the qubit label;
- the unique global optimizer for $m>0$;
- pure loss separately;
- unequal branch weights;
- relative phase;
- arbitrary complex coherent-pair reduction by displacement/rotation covariance;
- attenuator/amplifier/additive-noise parameter maps.

No internal mathematical failure was found.

Read:

- `experiments/01-causal-quantum-branch-information/DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `experiments/01-causal-quantum-branch-information/PURE_LOSS_EDGE_CASE.md`
- `experiments/01-causal-quantum-branch-information/COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`

---

## 4. Exact witness candidate

The selected PT block is

$$
M_\Gamma
=\begin{pmatrix}
p_0&z_v^*\\z_v&p_v
\end{pmatrix},
$$

with NPT certified by

$$
|z_v|^2>p_0p_v.
$$

At the matched $v_*$ it reaches the exact phase-insensitive EB boundary.

Read:

- `experiments/01-causal-quantum-branch-information/EXACT_THREE_ELEMENT_WITNESS.md`

### Scope warning

This is **not** merely a two-input prepare-and-measure benchmark. The off-diagonal element contains

$$
\Phi(|a\rangle\langle-a|),
$$

so the exact criterion assumes access to the hybrid source-replacement coherence or an equivalent process-coherent measurement.

Do not claim lower experimental resources than old two-/three-coherent-state benchmarks without a separate implementation argument.

---

## 5. Prior art already checked around the coherent theorem

The field already contains almost every surrounding ingredient.

### Rigas–Gühne–Lütkenhaus (2006)

Uses exactly

$$
\sqrt{p_0}|0\rangle|\alpha\rangle
+\sqrt{p_1}|1\rangle|-\alpha\rangle
$$

with PPT/EVM verification. In the symmetric Gaussian-noise example their necessary outer relation $\delta<2\eta$ maps to the thermal-channel non-EB boundary, but their actual detection curves remain overlap dependent and sufficient.

### Häseler–Moroder–Lütkenhaus (2008)

Two coherent test states, effective entanglement, PPT/EVM practical channel verification. No exact all-pair actual-state theorem located.

### Namiki (2008)

Explicitly identifies the binary coherent virtual-state criterion as NPT based and develops a two-state quantum-domain benchmark. Still a sufficient benchmark, not the exact actual-state theorem.

### Killoran–Häseler–Lütkenhaus (2010)

Uses the same virtual hybrid state, negativity, and a thermal beam-splitter test channel. Explicitly states its lower bounds do not give the full entanglement picture.

### Killoran–Lütkenhaus (2011)

Improves quantitative finite-subspace bounds and is often faithful over nearly all of the quantum domain, but still minimizes over states compatible with incomplete data rather than calculating the exact known-channel output NPT boundary.

### Kreis–van Loock (2012)

Studies the same balanced hybrid state under thermal photon noise. Their finite Shchukin–Vogel witness is amplitude dependent and leaves part of the non-EB region undetected.

### Ivan–Sabapathy–Simon (2013)

Relates Gaussian nonclassicality-breaking and entanglement-breaking channels, but no implication has been found that **every finite binary coherent pair** has the claimed NPT property.

### Namiki–Azuma and related finite-alphabet benchmarks

Finite coherent alphabets can strongly or optimally benchmark Gaussian channels. Therefore “few coherent states can reach an EB boundary” is not a novelty claim.

Read:

- `experiments/01-causal-quantum-branch-information/COHERENT_PRIOR_ART_DEEP_AUDIT.md`
- `experiments/01-causal-quantum-branch-information/COHERENT_PRIOR_ART_SECOND_PASS.md`
- `experiments/01-causal-quantum-branch-information/NOVELTY_CHECK_GAUSSIAN_BINARY_PROBE.md`
- `experiments/01-causal-quantum-branch-information/NOVELTY_CHECK_FINITE_CAT.md`

**Current verdict:** no exact collision found yet. This is not proof of novelty.

---

## 6. Gaussian canonicalization convention is now fixed

Use throughout

$$
V\mapsto K^T V K+\beta.
$$

A Gaussian unitary $S$ acts as

$$
V\mapsto S^T V S.
$$

With input and output symplectics,

$$
\boxed{
K'=S_{\rm in}KS_{\rm out},
\qquad
\beta'=S_{\rm out}^T\beta S_{\rm out}.
}
$$

For regular orientation-preserving channels choose

$$
S_{\rm out}^T\beta S_{\rm out}=yI,
$$

then

$$
\boxed{
S_{\rm in}=\sqrt\tau\,S_{\rm out}^{-1}K^{-1},
}
$$

so

$$
S_{\rm in}KS_{\rm out}=\sqrt\tau I.
$$

The previous matrix-order mismatch has been corrected in

- `experiments/01-causal-quantum-branch-information/ONE_MODE_GAUSSIAN_CANONICAL_CLASS_PROOF_AUDIT.md`.

---

## 7. Numerical reproducibility status

Executable independent audits are now committed for

1. thermal attenuation — beam splitter + thermal environment;
2. thermal amplification — two-mode squeezer + thermal environment;
3. additive Gaussian noise — direct random-displacement Gauss–Hermite integration;
4. near-boundary stress scans.

Read:

- `experiments/01-causal-quantum-branch-information/numerics/README.md`
- `experiments/01-causal-quantum-branch-information/NUMERICAL_AUDIT_AMPLIFIER_ADDITIVE_NOISE.md`

Scripts:

- `numerics/thermal_cat_scan.py`
- `numerics/amplifier_cat_scan.py`
- `numerics/additive_noise_cat_scan.py`
- `numerics/near_boundary_stress.py`

Finite truncations can show small spurious negative PT eigenvalues on the EB side. Require convergence, not a one-cutoff sign test.

---

## 8. Exact next actions

A new agent should **not** redo the completed proof audit or basic numerical implementations.

Proceed in this order:

### Priority 1 — continue citation-forward search for a full-state exact calculation

Look for papers/theses that retain the source coherence and explicitly diagonalize or partially transpose the qubit–coherent thermal output.

Search especially

- papers citing Kreis–van Loock (2012);
- papers citing Killoran–Lütkenhaus (2011);
- hybrid qubit–oscillator decoherence papers with exact density matrices;
- binary-modulated CV-QKD entanglement-based proofs;
- displaced-thermal hybrid negativity calculations;
- coherent-state process tomography deriving $\Phi(|\alpha\rangle\langle\beta|)$;
- Shchukin–Vogel hierarchy specializations that might reach the exact EB boundary.

A collision counts even if notation is completely different.

### Priority 2 — try to derive the coherent theorem as a corollary of an older general theorem

Attack via

- nonclassicality-breaking/EB duality;
- entanglement potential of nonclassical states;
- general qubit-mode PPT criteria;
- Gaussian-channel order/majorization arguments;
- local filtering equivalences.

If a known general theorem implies the all-pairs statement immediately, novelty is dead even without the same formula.

### Priority 3 — controlled numerical boundary data

Run the committed stress harness near

$$
|\tau-m|=10^{-1},10^{-2},10^{-3},10^{-4}
$$

from both sides and record convergence. Do not mistake the numerical resolution floor for physical NPT.

### Priority 4 — only if novelty survives, build a narrow manuscript

The paper should be about the **exact analytic completion of the binary coherent actual-state problem**, not a new coherent-state benchmarking paradigm.

### Priority 5 — gravity later

Return to gravity only after the coherent theorem's novelty status is substantially resolved. The strongest remaining gravity-specific technical issue is still the complete conserved actuator/control stress-energy of the explicit source.

---

## 9. Canonical reading order

1. `AGENTS.md`
2. `experiments/01-causal-quantum-branch-information/CURRENT_STATE_RANK2_UPDATE.md`
3. `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`
4. `experiments/01-causal-quantum-branch-information/CLAIM_LEDGER_POST_MELE_ADDENDUM.md`
5. `experiments/01-causal-quantum-branch-information/COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`
6. `experiments/01-causal-quantum-branch-information/COHERENT_PRIOR_ART_DEEP_AUDIT.md`
7. `experiments/01-causal-quantum-branch-information/COHERENT_PRIOR_ART_SECOND_PASS.md`
8. `experiments/01-causal-quantum-branch-information/DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
9. `experiments/01-causal-quantum-branch-information/EXACT_THREE_ELEMENT_WITNESS.md`
10. `experiments/01-causal-quantum-branch-information/numerics/README.md`

---

## 10. Current stop/go

### STOP

- rank-two Fock novelty paper;
- broad claims that binary coherent effective-entanglement testing is new;
- claims that the three-element result is automatically a minimal prepare-and-measure benchmark.

### GO

- exact all-finite-binary-coherent-pairs novelty audit;
- exact matched coherent principal-minor novelty audit;
- citation-forward search for hidden full-state calculations;
- controlled near-boundary numerics;
- only after survival, a narrowly scoped manuscript.
