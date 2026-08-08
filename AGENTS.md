# AGENTS.md — Canonical Research Recovery Point

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Checkpoint:** 2026-08-07, after two confirmed prior-art kills: Mele–Lami–Giovannetti for rank-two Fock probes and Filippov–Ziman for all finite binary coherent-pair survival.

This is the first file a new agent should read.

---

## 1. Operating rule

Try to kill every claim before trying to publish it.

Attack by

1. counterexample;
2. hidden assumption;
3. convention/normalization error;
4. singular limit;
5. stronger prior art under different terminology;
6. a general theorem that makes the result an immediate corollary;
7. numerical truncation artifacts;
8. scope inflation.

If a claim dies, update the documentation immediately.

---

## 2. First confirmed kill — rank-two Fock novelty

The repository independently derived

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}}
$$

with

$$
\det M_s
=\frac{s^2}{(1+s^2)^2}
\frac{m-\tau}{(m+1)^3},
$$

so the output is NPT iff

$$
\tau>m.
$$

The mathematics appears correct.

**Novelty is dead.**

Mele–Lami–Giovannetti, arXiv:2303.12867 / *Nature Photonics* (2025), already use

$$
|\Psi_{M,c}\rangle
=c|00\rangle+\sqrt{1-c^2}|MM\rangle
$$

for arbitrary $M\ge1$ and nonzero Schmidt weight, and prove non-PPT/distillability exactly in the non-EB phase-insensitive region after local projection.

Read:

- `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`

Do not resurrect the old rank-two standalone-paper claim.

---

## 3. Second confirmed kill — all finite binary coherent-pair survival theorem

The repository also independently proves that every finite nontrivial

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
\qquad
\alpha\ne\beta,
$$

has NPT output under a phase-insensitive Gaussian channel iff

$$
\tau>m.
$$

The direct repository proof is correct and exceptionally compact, but the underlying survival theorem is already implicit in

S. N. Filippov and M. Ziman, *Phys. Rev. A* **90**, 010301(R) (2014), arXiv:1405.1754.

They study

$$
|\psi_\gamma\rangle
\propto
|\gamma\rangle_A|0\rangle_B
-|0\rangle_A|\gamma\rangle_B
$$

under asymmetric phase-insensitive Gaussian channels and derive an exact coherent-state witness family.

### One-sided specialization

Leave $A$ ideal and apply the noisy channel only to $B$.

In Filippov–Ziman variables, let

$$
a=\mu-\frac12|\kappa-1|
$$

be excess noise and let

$$
T=
\begin{cases}
1+a,&\kappa<1,\\
\kappa+a,&\kappa>1.
\end{cases}
$$

With

$$
t=1-\lambda>0,
$$

their exact witness expectation reduces, up to a positive prefactor, to

$$
E(t;x)=e^{-Ax}+e^{-Bx}-2e^{-Cx},
\qquad x=|\gamma|^2,
$$

with

$$
A=\frac\kappa T,
$$

$$
B=1+\frac{1-T}{Tt^2},
$$

$$
C=1-\frac{\sqrt\kappa}{Tt}.
$$

Choose

$$
\boxed{
t^2=\frac{T-1}{T-\kappa}}
$$

for finite excess noise. Then

$$
A=B
$$

and negativity of the witness for **every finite $\gamma\ne0$** is equivalent to

$$
(T-\kappa)(T-1)<\kappa.
$$

This factors as

$$
(a+1)(a-\kappa)<0
\iff a<\kappa
$$

for attenuation, and

$$
(a+\kappa)(a-1)<0
\iff a<1
$$

for amplification. The additive-noise limit is also $a<1$.

Those are exactly the complements of the Filippov–Ziman EB condition

$$
a\ge\min(\kappa,1).
$$

The quantum-limited attenuation/amplification edges are handled by finite direct choices of $t$.

### Mapping to the repository state

The untouched reference mode occupies only

$$
\operatorname{span}\{|0\rangle,|\gamma\rangle\}.
$$

An invertible local filter on this two-dimensional support maps

$$
|\gamma\rangle_A,|0\rangle_A
$$

to orthogonal qubit labels with arbitrary nonzero weights. It commutes with the channel on $B$ and preserves PT inertia on the occupied support.

A common displacement/phase rotation on $B$ maps the pair

$$
|0\rangle,|\gamma\rangle
$$

to any finite distinct coherent pair.

### NPT refinement

Their weighted-swap witness has finite Fock truncations satisfying

$$
W_{\lambda,N}^{T_2}
\propto
|\Omega_{\lambda,N}\rangle
\langle\Omega_{\lambda,N}|
\ge0.
$$

Thus the truncations are decomposable NPT witnesses. The one-sided Gaussian expectation converges; a negative limiting expectation implies a negative finite truncation and therefore NPT.

Read the full derivation:

- `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`

**Do not claim the all-finite-binary-coherent survival theorem as new.**

---

## 4. Main remaining candidate — minimal exact three-element PT witness

The strongest surviving possible contribution is now much narrower.

For symmetric branches $|\pm a\rangle$, the repository selects one $2\times2$ block of the actual partial transpose:

$$
M_\Gamma
=
\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}.
$$

NPT is certified iff

$$
|z_v|^2>p_0p_v.
$$

For $m>0$, the exact matched coherent analysis displacement is

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m}}
$$

and

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

This is valuable because it turns a known survival phenomenon into a literal finite $2\times2$ PT minor using only

1. one population $p_0$;
2. one displaced population $p_{v_*}$;
3. one coherence $z_{v_*}$.

It is substantially simpler than the Filippov–Ziman weighted integral witness.

Read:

- `experiments/01-causal-quantum-branch-information/EXACT_THREE_ELEMENT_WITNESS.md`
- `experiments/01-causal-quantum-branch-information/DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `experiments/01-causal-quantum-branch-information/COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`

### Important scope warning

The off-diagonal term contains

$$
\Phi(|a\rangle\langle-a|),
$$

so this is not automatically a two-conditional-output prepare-and-measure benchmark. Treat it as an exact state/process-coherence witness unless a separate implementation argument is supplied.

---

## 5. Secondary candidate — exact absolute witness strength

The selected block also provides the finite negativity lower bound

$$
G(v)=\frac12
\max\left\{0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
$$

The repo has additional weak-link asymptotics and exact low-dimensional strength formulas.

Potential novelty is now in **certification strength / proof compression**, not the existence of surviving entanglement.

Search these files after the three-element witness:

- `ABSOLUTE_THREE_ELEMENT_WITNESS_GAP.md`
- `WEAK_LINK_ABSOLUTE_GAP_ASYMPTOTIC.md`

---

## 6. Internal proof and convention status

The direct coherent-dyad proof has independently survived a line-by-line rederivation.

The earlier covariance-order bug in the arbitrary Gaussian-channel audit has been fixed. Use throughout

$$
V\mapsto K^T V K+\beta.
$$

For input/output symplectics,

$$
K'=S_{\rm in}KS_{\rm out},
$$

$$
\beta'=S_{\rm out}^T\beta S_{\rm out}.
$$

Read:

- `ONE_MODE_GAUSSIAN_CANONICAL_CLASS_PROOF_AUDIT.md`

---

## 7. Numerical status

Executable independent checks are committed for

- thermal attenuation;
- thermal amplification;
- additive Gaussian noise;
- near-boundary convergence.

The additive-noise stress test resolves the analytic sign change down to at least

$$
|\tau-m|=10^{-4}
$$

with the current cutoffs.

Read:

- `numerics/README.md`
- `NUMERICAL_NEAR_BOUNDARY_STRESS_RESULTS.md`

---

## 8. Exact next actions

A new agent should **not** restart the rank-two or all-coherent-pairs novelty searches. Both broad claims are dead.

Proceed in this order.

### Priority 1 — kill the three-element witness novelty

Search for

- $2\times2$ coherent-state principal minors of partial transposes;
- displaced-vacuum entanglement witnesses;
- hybrid coherent-state criteria of the form $|z|^2>p_0p_v$;
- coherent-state process-matrix minors;
- Husimi-Q / off-diagonal Q-kernel PPT criteria;
- finite truncations of weighted-swap witnesses that collapse to a two-vector block;
- exact optimized displacement witnesses under thermal attenuators/amplifiers/additive noise.

The collision need not use the repository notation.

### Priority 2 — compare directly against Filippov–Ziman

Ask whether their weighted-swap witness can be analytically minimized/projected to the repository three-element principal minor. If yes, even the witness novelty may collapse to a proof simplification.

### Priority 3 — audit absolute-strength formulas

Check whether the selected-block negative eigenvalue and weak-link optimum are genuinely new quantitative corollaries.

### Priority 4 — decide publication value

Only if the minimal witness or quantitative bound survives should a standalone note be drafted. The manuscript would need to present itself as a **minimal exact certification/simplification of known entanglement-survival physics**, not as a newly discovered survival theorem.

### Priority 5 — gravity

If the standalone quantum-information contribution becomes too small, return to the gravity application. The strongest unresolved gravity-specific issue remains the complete conserved actuator/control stress-energy of the explicit source.

---

## 9. Canonical reading order

1. `AGENTS.md`
2. `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
3. `experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md`
4. `experiments/01-causal-quantum-branch-information/CURRENT_STATE_RANK2_UPDATE.md`
5. `experiments/01-causal-quantum-branch-information/CLAIM_LEDGER_POST_MELE_ADDENDUM.md`
6. `experiments/01-causal-quantum-branch-information/EXACT_THREE_ELEMENT_WITNESS.md`
7. `experiments/01-causal-quantum-branch-information/DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
8. `experiments/01-causal-quantum-branch-information/COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`
9. `experiments/01-causal-quantum-branch-information/NUMERICAL_NEAR_BOUNDARY_STRESS_RESULTS.md`
10. `experiments/01-causal-quantum-branch-information/numerics/README.md`

---

## 10. Stop/go

### STOP

- rank-two Fock novelty paper;
- all-finite-binary-coherent-pairs survival theorem as novelty;
- broad claims that binary coherent effective-entanglement testing is new;
- broad claims that a small coherent alphabet newly reaches a Gaussian EB boundary.

### GO

- minimal exact three-element PT witness novelty audit;
- exact negative-eigenvalue / absolute-strength audit;
- reduction/comparison to Filippov–Ziman's weighted-swap witness;
- only then a narrowly scoped paper or return to gravity.
