# Current State Addendum — Post Rank-Two Prior-Art Collision

**Date:** 2026-08-07  
**Status:** Canonical recovery point after the Mele–Lami–Giovannetti collision audit.  
**Read first:** root `AGENTS.md` and `NOVELTY_COLLISION_MELE_RANK_TWO.md`.

## 1. Executive verdict

The repository's Schmidt-rank-two Fock calculations remain mathematically credible, but the principal novelty claim has been killed by prior art.

The previous proposed headline

> **Schmidt-Rank-Two Probes Suffice to Detect Entanglement Breaking in One-Mode Gaussian Channels**

must **not** be treated as the current publication target.

Mele, Lami, and Giovannetti, arXiv:2303.12867 (first submitted 22 March 2023; later *Nature Photonics* 2025), already use finite Schmidt-rank-two Fock-pair inputs and prove in Supplementary Remark 1 that, after a local two-level projection, the resulting state is non-PPT/distillable exactly throughout the non-entanglement-breaking region of their canonical phase-insensitive Gaussian channel. Their result holds for every positive Fock index $M$ and every nonzero Schmidt weight.

Under the parameter map

$$
\tau=g\lambda,
\qquad
m=g-1,
$$

their exact condition

$$
(1-\lambda)g<1
$$

becomes

$$
\boxed{\tau>m,}
$$

which is exactly the repository's determinant boundary.

Setting

$$
M=1,
\qquad
c=1/\sqrt2
$$

gives the fixed vacuum–one-photon Bell state.

See:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`
- root `AGENTS.md`

---

## 2. Rank-two Fock theorem: mathematics retained, novelty retired

For

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}},
\qquad s>0,
$$

the repository independently derives

$$
M_s
=\frac{1}{(1+s^2)(m+1)^2}
\begin{pmatrix}
m&s\sqrt\tau\\
s\sqrt\tau&s^2(m+1-\tau)
\end{pmatrix},
$$

with

$$
\boxed{
\det M_s
=\frac{s^2}{(1+s^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

Therefore

$$
\rho_{\rm out}\text{ NPT}
\iff
\tau>m.
$$

This compact proof is still useful as

1. an independent derivation;
2. a transparent two-dimensional principal-minor proof;
3. a convenient lemma for later calculations.

It is **not** presently a discovery claim.

Files retained for mathematical reference:

- `TRUNCATED_TMSV_RANK_TWO_THEOREM.md`
- `TWO_DIMENSIONAL_CHOI_TRUNCATION_CRITERION.md`
- `MINIMAL_QUBIT_ANCILLA_GAUSSIAN_EB.md`
- `ARBITRARILY_WEAK_RANK_TWO_GAUSSIAN_PROBES.md`

These files should be read as rediscovery/simplification notes unless separately revised.

---

## 3. General one-mode extension after the collision

The repository's class audit still suggests the mathematical statement

$$
\text{every non-EB one-mode Gaussian channel admits a finite rank-two NPT probe}
$$

is correct.

However, for regular orientation-preserving one-mode Gaussian channels this follows essentially from

1. the existing phase-insensitive rank-two Fock result of Mele et al.;
2. standard Gaussian input/output canonicalization;
3. local-unitary invariance of Schmidt rank and NPT.

The remaining singular $B_1$ class is handled in the repository by a finite regularization:

$$
Y_{B_1}=\operatorname{diag}(b,0),
\qquad
Y_\epsilon=\operatorname{diag}(b,\epsilon),
$$

with finite

$$
0<\epsilon<1/b.
$$

Then

$$
\sqrt{b\epsilon}<1,
$$

so the regularized unit-gain channel is non-EB. If the pre-regularization output were PPT, subsequent local Gaussian noise could not make it NPT. Hence the original $B_1$ output is already NPT for the same finite probe.

This argument has survived the current adversarial audit, but after the Mele collision it is a **singular-class closure argument**, not enough by itself to justify the previous standalone-paper headline.

Files:

- `ONE_MODE_GAUSSIAN_CANONICAL_CLASS_PROOF_AUDIT.md`
- `CONSTRUCTIVE_B1_FINITE_PROBE.md`

---

## 4. Strongest surviving standalone candidate: binary coherent probes

The active theorem candidate is now structurally different from the killed Fock result.

For every finite nontrivial hybrid state

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

the repository proves

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

For symmetric real branches $|\pm a\rangle$ and $m>0$, define the coherent-state principal-minor ratio

$$
R(v)=\frac{|z_v|^2}{p_0p_v}.
$$

The exact optimum is

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and

$$
\boxed{
R(v_*)
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

Thus every finite nonzero coherent separation detects the exact EB boundary.

For pure loss $m=0$, the maximizing displacement moves to infinity, but no infinite test state is required: any finite

$$
v>\frac{a(1-\tau)}{\sqrt\tau}
$$

certifies NPT for every $\tau>0$.

Files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `PURE_LOSS_EDGE_CASE.md`

**Novelty status:** candidate novelty, unverified. No exact prior-art theorem matching the all-finite-coherent-pairs iff statement has yet been located.

---

## 5. Second surviving candidate: exact three-element coherent witness

For the same coherent hybrid state, one $2\times2$ partial-transpose block

$$
M_\Gamma=
\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}
$$

provides the condition

$$
\boxed{|z_v|^2>p_0p_v.}
$$

At the matched displacement $v_*$ this criterion is equivalent to

$$
\boxed{\tau>m.}
$$

Thus two populations plus one coherence detect the full actual-state NPT boundary of the binary coherent output.

File:

- `EXACT_THREE_ELEMENT_WITNESS.md`

**Novelty status:** candidate novelty, unverified.

---

## 6. Coherent-state prior-art boundary already established

### Häseler–Moroder–Lütkenhaus (2008)

Already established two-nonorthogonal-coherent-state quantum-device testing, effective entanglement, and PPT/expectation-value-matrix methods.

Therefore none of those general ideas are new.

### Kreis–van Loock (2012)

They study the same symmetric hybrid state

$$
(|0\rangle|\alpha\rangle+|1\rangle|-\alpha\rangle)/\sqrt2
$$

under one-sided thermal photon noise. They derive the noisy hybrid state and apply a finite-order Shchukin–Vogel moment witness. Their sufficient threshold is amplitude dependent, and their discussion explicitly leaves an undetected region below the known thermal-channel EB threshold.

This is the most important surviving novelty comparison: the repository's result claims an exact necessary-and-sufficient actual-state NPT completion of precisely that gap.

### Namiki–Azuma (2015)

Coherent-state ensembles and homodyne measurements can benchmark all one-mode Gaussian channels against entanglement-breaking performance. This is an established ensemble benchmark, not the same as the individual binary hybrid-state theorem.

Files:

- `NOVELTY_CHECK_GAUSSIAN_BINARY_PROBE.md`
- `NOVELTY_CHECK_FINITE_CAT.md`
- `PRIOR_ART_BINARY_COHERENT_TESTS.md`

---

## 7. Current strongest next step

The highest-value task is now **not more theorem expansion**.

Proceed in this order:

1. citation-forward and equation-level literature search from Kreis–van Loock (2012) and Häseler–Moroder–Lütkenhaus (2008);
2. search for exact binary-coherent actual-state NPT conditions under thermal attenuation, amplification, and additive Gaussian noise;
3. search for displaced-vacuum / coherent-state $2\times2$ PT principal-minor witnesses that reach an EB boundary;
4. independently rederive the coherent-dyad kernel and optimized ratio using one fixed Gaussian convention;
5. reconstruct and commit the amplifier and additive-noise numerical scripts;
6. only then decide whether a coherent-state standalone note/paper is justified.

Root `AGENTS.md` contains the exact continuation protocol and search targets.

---

## 8. Writeup issue that still requires correction

The general Gaussian-channel audit currently mixes covariance-map conventions. It states a convention equivalent to

$$
V\mapsto K^T V K+\beta
$$

while some canonicalization matrices are ordered as if using

$$
V\mapsto KVK^T+\beta.
$$

This appears to be a notation/order issue rather than a counterexample, but it must be repaired before any manuscript uses the arbitrary-channel extension.

---

## 9. Publication priority after the collision

### Do not proceed

Do not proceed with the old rank-two Fock standalone paper as a novelty submission.

`PAPER_CORE_RANK_TWO_GAUSSIAN_EB_V2.md` is retained as a historical/internal derivation, not the active paper architecture.

### Active candidate

If novelty survives the new audit, a much narrower standalone result could center on

> **Every finite nontrivial binary coherent hybrid probe detects the exact entanglement-breaking boundary of a phase-insensitive one-mode Gaussian channel.**

The exact three-element witness would be the operational corollary.

### Gravity

The gravity application remains secondary. The strongest unresolved gravity-specific technical problem is still the complete conserved actuator/control stress-energy for the explicit source.

Do not expand the gravity receiver architecture until the coherent lemma novelty search is substantially complete.
