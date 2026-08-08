# Current State Addendum — Post Mele and Filippov–Ziman Collisions

**Date:** 2026-08-07  
**Status:** Canonical recovery point after two confirmed prior-art kills.  
**Read first:** root `AGENTS.md`.

## 1. Executive verdict

Two broad standalone novelty candidates have now been retired.

### Killed claim 1 — Schmidt-rank-two Fock sufficiency

The repository's compact determinant proof is correct, but Mele–Lami–Giovannetti already contain the finite-rank Fock-pair survival result.

Read:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

### Killed claim 2 — every finite binary coherent pair survives iff the phase-insensitive channel is non-EB

The repository's direct coherent-state proof is also correct, but Filippov–Ziman (2014) already contain enough structure to imply the same one-sided survival theorem.

Their asymmetric coherent-state witness, specialized to one ideal reference mode and one noisy phase-insensitive channel, can be tuned so that its sign is exactly the complement of the channel EB criterion for every finite coherent separation. An invertible local filter on the untouched two-dimensional coherent-state reference span maps their state to the repository qubit–coherent family while preserving PT inertia.

Read:

- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`

Therefore the project must **not** pursue either broad survival theorem as a discovery claim.

---

## 2. Mathematics retained from the Fock calculation

For

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}},
$$

$$
\boxed{
\det M_s
=\frac{s^2}{(1+s^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

Thus the output is NPT iff

$$
\tau>m.
$$

This remains a useful compact lemma/rederivation, not a new theorem.

---

## 3. Mathematics retained from the coherent calculation

For every finite nontrivial binary coherent hybrid state

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

the repository independently proves

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ NPT}
\iff
\tau>m.
}
$$

The direct coherent-dyad kernel is

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

For symmetric real branches $|\pm a\rangle$ and $m>0$,

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

This proof is much shorter than the Filippov–Ziman route and remains useful.

Files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`
- `PURE_LOSS_EDGE_CASE.md`

---

## 4. Strongest surviving standalone candidate — minimal exact PT certification

The active novelty question is no longer whether the entanglement survives.

The candidate is whether the survival boundary can be exposed by an unusually small exact witness that is not already in the literature.

The repository uses the literal $2\times2$ partial-transpose block

$$
\boxed{
M_\Gamma
=\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}.
}
$$

NPT is certified by

$$
\boxed{|z_v|^2>p_0p_v.}
$$

At the matched displacement $v_*$, this reaches the exact Gaussian EB boundary.

Only three selected matrix elements are required:

1. $p_0$;
2. $p_{v_*}$;
3. $z_{v_*}$.

File:

- `EXACT_THREE_ELEMENT_WITNESS.md`

**Novelty status:** still unverified.

---

## 5. Filippov–Ziman comparison that must now frame the result

Filippov–Ziman use a weighted integral/swap-type witness over coherent states. Their one-sided specialization already implies finite-coherent-pair survival throughout the non-EB region.

The repository contribution, if any, must therefore be stated as a simplification/compression such as:

> The full phase-insensitive binary-coherent NPT boundary is visible in one explicit $2\times2$ principal minor, with a closed-form matched coherent analysis state.

The next adversarial question is whether that principal minor is itself already implicit or explicit in earlier coherent-state PPT/kernel literature.

---

## 6. Absolute witness strength may be a secondary contribution

For

$$
M_v=\begin{pmatrix}p_0&z_v^*\\z_v&p_v\end{pmatrix},
$$

the negative weight

$$
\boxed{
G(v)=\frac12
\max\left\{0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}
}
$$

is a lower bound on full negativity.

The repository also derives weak-link optimized asymptotics. These quantitative formulas should now receive a separate novelty audit.

Files:

- `ABSOLUTE_THREE_ELEMENT_WITNESS_GAP.md`
- `WEAK_LINK_ABSOLUTE_GAP_ASYMPTOTIC.md`

---

## 7. Internal audit status

### Coherent theorem

Independent line-by-line rederivation passed.

### Gaussian canonicalization

The transpose/order convention bug has been corrected. Use

$$
V\mapsto K^T V K+\beta,
$$

with

$$
K'=S_{\rm in}KS_{\rm out},
\qquad
\beta'=S_{\rm out}^T\beta S_{\rm out}.
$$

File:

- `ONE_MODE_GAUSSIAN_CANONICAL_CLASS_PROOF_AUDIT.md`

### Numerical checks

Independent executable implementations exist for attenuation, amplification, additive noise, and near-boundary convergence.

The additive-noise stress calculation distinguishes the two sides of the EB boundary through at least

$$
|\tau-m|=10^{-4}
$$

at current numerical resolution.

Files:

- `NUMERICAL_NEAR_BOUNDARY_STRESS_RESULTS.md`
- `numerics/README.md`

---

## 8. Current publication decision

### Do not proceed

Do not submit

- a rank-two Fock survival theorem paper;
- an all-binary-coherent survival theorem paper.

Both underlying phenomena have prior-art collisions.

### Possible narrow paper

Only consider a standalone mathematical note if the following survives search:

> **A three-matrix-element coherent-state principal minor gives an exact, closed-form, finite-dimensional NPT certificate for the full phase-insensitive Gaussian EB boundary.**

The paper would need to cite Filippov–Ziman as the prior survival result and position the contribution as minimal exact certification / proof compression.

---

## 9. Exact next step

Search aggressively for prior results equivalent to

$$
|z_v|^2>p_0p_v
$$

with coherent/displaced-vacuum analysis states, especially

- coherent-state PT principal minors;
- displaced-vacuum hybrid entanglement witnesses;
- Husimi-Q kernel PPT tests;
- coherent-state process-matrix minors;
- finite truncations of weighted-swap/realignment witnesses;
- exact optimized displacement witnesses for thermal Gaussian channels.

Also try to reduce Filippov–Ziman's weighted witness analytically to the repository $2\times2$ block. If that reduction is immediate, even the witness novelty is likely dead.

Root `AGENTS.md` is the authoritative continuation protocol.

---

## 10. Gravity status

The gravity application remains viable as an application of known Gaussian-channel entanglement physics.

If the standalone witness contribution becomes too small, return to the gravity paper rather than manufacturing another mathematical headline.

The strongest unresolved gravity-specific technical issue remains the complete conserved actuator/control stress-energy for the explicit source.
