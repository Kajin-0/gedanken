# Novelty Check — Binary Coherent Probe Completeness for Phase-Insensitive Gaussian Channels

**Updated:** 2026-08-07  
**Status:** **COLLISION CONFIRMED — BROAD SURVIVAL THEOREM IS NOT AN ACTIVE NOVELTY CLAIM**

## 1. Repository result

The repository independently proves that for every finite nontrivial binary coherent hybrid state

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\neq\beta,
$$

and every gauge-covariant phase-insensitive one-mode Gaussian channel $\Phi_{\tau,m}$,

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

For symmetric real branches $|\pm a\rangle$ and $m>0$, the repository's direct proof gives

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

The proof has survived an independent algebraic audit and numerical stress tests. The mathematics remains useful.

The underlying all-finite-pairs survival theorem is no longer considered novel.

---

## 2. Decisive collision: Filippov–Ziman (2014)

S. N. Filippov and M. Ziman,

**“Entanglement sensitivity to signal attenuation and amplification,”**

*Phys. Rev. A* **90**, 010301(R) (2014), arXiv:1405.1754.

They study the non-Gaussian coherent state

$$
|\psi_\gamma\rangle
\propto
|\gamma\rangle_A|0\rangle_B
-|0\rangle_A|\gamma\rangle_B
$$

under asymmetric phase-insensitive Gaussian channels and derive an exact coherent-state weighted-swap witness family.

A one-sided specialization, with the $A$ channel set to the identity, can be tuned so the witness is negative for **every finite $\gamma\ne0$** exactly when the $B$ channel is non-entanglement-breaking.

In their variables, with excess noise

$$
a=\mu-\frac12|\kappa-1|,
$$

the channel is EB iff

$$
a\ge\min(\kappa,1).
$$

Their witness can be tuned so its sign reduces exactly to

$$
a<\kappa
$$

for attenuation and

$$
a<1
$$

for amplification/additive noise, i.e. the exact complement of the EB condition.

An invertible local filter on the untouched two-dimensional span

$$
\operatorname{span}\{|0\rangle,|\gamma\rangle\}
$$

maps their reference mode to orthogonal qubit labels with arbitrary nonzero branch weights. A common displacement/rotation on the noisy mode maps $|0\rangle,|\gamma\rangle$ to any finite distinct coherent pair.

Finite Fock truncations of the Filippov–Ziman weighted-swap witness have positive partial transpose after transposition of the witnessed subsystem, so a convergent negative expectation provides NPT certification rather than merely generic entanglement detection.

Full derivation:

- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`

---

## 3. Claims now retired

Do not claim as new:

- every finite binary coherent pair survives every non-EB thermal attenuator;
- the corresponding amplifier/additive-noise survival statement;
- arbitrary nonzero branch weights via local filtering;
- the broad iff statement that the binary coherent hybrid output is NPT exactly in the phase-insensitive non-EB region.

The repository's proof may be substantially shorter and more transparent, but that is a **proof-compression question**, not a new survival theorem.

---

## 4. What remains under novelty audit

The strongest possible contribution is the literal finite-dimensional PT certificate

$$
M_\Gamma
=\begin{pmatrix}
p_0&z_v^*\\z_v&p_v\end{pmatrix},
$$

with

$$
|z_v|^2>p_0p_v,
$$

and the exact matched displacement

$$
\boxed{v_*=2\sqrt\tau a/m.}
$$

At that displacement,

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp[4a^2(\tau-m)/m].
}
$$

Potentially new content, still unverified:

1. reducing the known survival boundary to one explicit $2\times2$ principal minor of the **actual partial transpose**;
2. requiring only two selected populations and one coherence;
3. the closed-form matched coherent analysis state $v_*$;
4. the associated exact selected-block negative eigenvalue / absolute negativity lower bound;
5. optimized weak-link witness-strength asymptotics.

Files:

- `EXACT_THREE_ELEMENT_WITNESS.md`
- `ABSOLUTE_THREE_ELEMENT_WITNESS_GAP.md`
- `WEAK_LINK_ABSOLUTE_GAP_ASYMPTOTIC.md`

---

## 5. Prior-art search now required

Do not spend further effort asking whether the broad coherent-pair survival theorem is new.

Search instead for

- coherent-state $2\times2$ principal minors of partial transposes;
- displaced-vacuum hybrid entanglement witnesses;
- state/process criteria equivalent to $|z|^2>p_0p_v$;
- coherent-state matrix-element PPT tests;
- finite reductions of weighted-swap / realignment witnesses;
- exact optimized displacement tests for thermal attenuation/amplification/additive noise;
- quantitative selected-block negativity bounds reaching Gaussian EB boundaries.

Also try to derive the repository's three-element witness directly from Filippov–Ziman's weighted witness. If the reduction is immediate, the remaining novelty may be only pedagogical simplification.

---

## 6. Current verdict

**Broad theorem: killed as novelty.**  
**Direct proof: mathematically strong and useful.**  
**Three-element principal-minor certification: strongest surviving candidate, novelty unverified.**
