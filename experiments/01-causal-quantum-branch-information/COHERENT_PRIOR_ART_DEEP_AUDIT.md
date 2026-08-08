# Deep Prior-Art Audit — Binary Coherent Hybrid NPT Theorem

**Date:** 2026-08-07  
**Status:** **ACTIVE NOVELTY AUDIT — NO EXACT COLLISION FOUND IN THIS PASS**

## 1. Exact claim being attacked

For every finite nontrivial binary coherent hybrid state

$$
|\Psi\rangle
=\sqrt p\,|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}\,|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\ne\beta,
$$

and every one-mode gauge-covariant phase-insensitive Gaussian channel $\Phi_{\tau,m}$ in the repository convention,

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

For symmetric real branches $|\pm a\rangle$ and $m>0$, the direct proof uses one coherent-state $2\times2$ principal minor and gives

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

This audit asks whether an earlier paper already proves or immediately implies this **actual-output-state NPT iff theorem for every finite coherent pair**, rather than merely using two coherent states to benchmark a channel.

---

## 2. Rigas–Gühne–Lütkenhaus (2006): extremely close architecture

**J. Rigas, O. Gühne, and N. Lütkenhaus**, “Entanglement verification for quantum key distribution systems with an underlying bipartite qubit-mode structure,” *Phys. Rev. A* **73**, 012341 (2006), arXiv:quant-ph/0510022.

### Same virtual hybrid state

Their Eq. (1) starts from

$$
\boxed{
|\Psi\rangle_{AB}
=\sqrt{p_0}|0\rangle_A|\alpha\rangle_B
+\sqrt{p_1}|1\rangle_A|-\alpha\rangle_B.
}
$$

Thus the source-replacement / effective-entanglement state is exactly the symmetric member of the repository's binary coherent family, including arbitrary branch probabilities.

Their purpose is practical entanglement verification when only Bob's conditional first and second moments are known.

### Their method is explicitly PPT/NPT based

They write the qubit-mode state in block form and impose positivity of both the state and its partial transpose as necessary conditions for separability. They then build an expectation-value matrix (EVM) and solve a semidefinite feasibility problem.

If the PPT-compatible EVM feasibility problem is infeasible, the data must have come from an entangled state.

They state in their conclusion that their scheme cannot detect PPT entanglement; therefore the entanglement certified by this method is NPT-type entanglement.

### Symmetric Gaussian-noise example

For balanced coherent inputs they take conditional EVMs with output means

$$
\langle x\rangle_{0/1}=\pm c,
$$

and symmetric quadrature variance

$$
\sigma_x^2=\sigma_y^2=\sigma^2.
$$

They define transmission through

$$
\eta=c^2/|\alpha|^2
$$

and solve the separability feasibility problem numerically. Their Fig. 2 gives an **overlap-dependent** entanglement-detection boundary.

They explicitly state that all of their detected regions obey the necessary relation

$$
\boxed{
\delta<2\eta,
\qquad
\delta\equiv\sigma^2-1.
}
$$

### Important connection to the thermal attenuator EB boundary

For a thermal attenuator with environment occupation $\bar n$ and shot-noise-normalized vacuum variance equal to one,

$$
\sigma^2
=\eta\cdot1+(1-\eta)(2\bar n+1)
=1+2(1-\eta)\bar n.
$$

Therefore

$$
\delta=2(1-\eta)\bar n.
$$

The Rigas necessary relation becomes

$$
2(1-\eta)\bar n<2\eta,
$$

or

$$
\boxed{
\bar n<\frac{\eta}{1-\eta},
}
$$

which is exactly the thermal attenuator non-entanglement-breaking condition.

This is a very important precursor: the exact channel boundary was already visible as the **necessary outer limit** of two-coherent-state NPT verification.

### Why this does not yet kill the repository theorem

Rigas et al. do **not** show that their EVM criterion reaches

$$
\delta=2\eta
$$

for every nonzero coherent-state overlap. Their Fig. 2 boundaries depend strongly on overlap, and their text describes the region below those curves as the region where entanglement can be ensured from the restricted moment data.

Thus their result is

$$
\text{restricted moments satisfy sufficient NPT criterion}
\Longrightarrow
\text{actual state entangled},
$$

not the repository's stronger statement

$$
\text{actual Gaussian-channel output NPT}
\iff
\delta<2\eta
$$

for every finite nonzero coherent separation.

**Current verdict:** very close conceptual and mathematical prior art; no exact theorem collision located.

---

## 3. Namiki (2008): two-state quantum-domain verification and explicit NPT precursor

**R. Namiki**, “Verification of quantum-domain process using two non-orthogonal states,” *Phys. Rev. A* **78**, 032333 (2008), arXiv:0807.0046.

Namiki constructs a two-nonorthogonal-state benchmark against measure-and-prepare / EB channels.

For coherent states, he takes

$$
|\psi_\pm\rangle=|\pm\alpha\rangle
$$

and target states

$$
|\psi'_\pm\rangle=|\pm\sqrt\eta\alpha\rangle.
$$

He notes that displaced threshold-photon detection measures the coherent-state projection probabilities directly.

Most importantly for this audit, Namiki explicitly identifies the earlier Rigas/Häseler approach as a criterion formulated to verify entanglement of the virtual state

$$
\boxed{
|\alpha\rangle|0\rangle+|-\alpha\rangle|1\rangle,
}
$$

and states that the derivation is based on the **negative partial transpose** of that virtual entangled state.

Therefore none of the following may be claimed as new:

- the binary coherent source-replacement state;
- using its NPT as a channel-quantumness witness;
- displaced coherent-state projections for practical verification;
- two nonorthogonal states as an EB/non-EB benchmark resource.

Namiki's own fidelity criterion is a sufficient quantum-domain test from two measured projection probabilities; it is not an exact actual-output NPT theorem for a complete phase-insensitive Gaussian channel family.

**Current verdict:** establishes the NPT-based binary-coherent paradigm decisively, but no exact all-finite-pairs Gaussian boundary theorem located.

---

## 4. Killoran–Häseler–Lütkenhaus (2010): negativity of the exact same virtual hybrid state

**N. Killoran, H. Häseler, and N. Lütkenhaus**, “Quantum Throughput: Quantifying quantum communication with homodyne measurements,” *Phys. Rev. A* **82**, 052331 (2010), arXiv:1005.3380.

### Same state again

Their Eq. (1) is

$$
\boxed{
|\psi\rangle_{AB}
=\frac{|0\rangle_A|\alpha\rangle_B
+|1\rangle_A|-\alpha\rangle_B}{\sqrt2}.
}
$$

They explicitly describe sending the mode half through an optical channel and quantifying the surviving effective entanglement.

### They use negativity directly

They choose the entanglement negativity as the quantitative measure and construct a finite-dimensional projection whose negativity gives a lower bound on the negativity of the full qubit-mode output state.

Thus the use of negativity/NPT for exactly the same source-replacement state is indisputably prior art.

### Thermal beam-splitter test channel

They also explicitly study a simple test channel in which the coherent test state is mixed at a 50:50 beam splitter with a thermalized vacuum. The conditional outputs are displaced thermal states, so this is directly in the same physical neighborhood as the repository's thermal attenuator specialization.

Crucially, however, they state that their negativity lower bounds become trivial while quantum correlations can still be verified and that their bounds **“do not provide the full picture.”** Even after inserting exact conditional eigenvalue/overlap information for the thermal test channel, their two-qubit projection yields nontrivial quantitative bounds for only part of the region where entanglement can be verified.

They propose higher-dimensional truncations as a possible improvement.

### Why this is strong evidence for a real completion

This paper explicitly asks for negativity of the exact same hybrid state under thermal optical noise, yet its practical lower-bound machinery does not characterize the entire entangled region.

The repository's exact coherent principal minor claims to do precisely what this line of work did not:

$$
\boxed{
\text{single finite }2\times2\text{ coherent-state PT minor}
\Longleftrightarrow
\text{full non-EB boundary}
}
$$

for every nonzero coherent separation.

**Current verdict:** strong direct predecessor; no exact collision found.

---

## 5. Häseler–Lütkenhaus (2010): optimal benchmark can require three coherent states

**H. Häseler and N. Lütkenhaus**, “Quantum benchmarks for the storage or transmission of quantum light from minimal resources,” *Phys. Rev. A* **81**, 060306(R) (2010), arXiv:0910.1458.

This paper compares coherent-state channel benchmarks for a lossy thermal-noise model.

It explicitly includes

- two-state fidelity benchmarks;
- two-state EVM/effective-entanglement benchmarks;
- phase-encoded ensembles;
- Gaussian-distributed coherent ensembles.

They find that a **three-coherent-state** homodyne benchmark can match the optimal noise resilience of the Gaussian ensemble.

For the Gaussian effective-entanglement construction based on a finite-squeezing TMSV, they derive the exact thermal-channel boundary

$$
\boxed{
\bar n\le\frac{\eta}{1-\eta}
}
$$

for arbitrary nonzero squeezing.

They contrast this with the weaker two-state practical curves.

### Consequence for current novelty language

Do not claim

> a finite coherent alphabet reaches the Gaussian EB boundary

as a broad novelty.

By 2010, optimal channel benchmarks from only three coherent states were already known.

The surviving candidate is narrower:

> **every single finite nontrivial binary coherent hybrid state itself remains NPT throughout the full non-EB region, even though the old two-state limited-moment benchmark does not certify all of that entanglement.**

---

## 6. Kreis–van Loock (2012): same noisy hybrid state, incomplete moment witness

See `NOVELTY_CHECK_FINITE_CAT.md` for the full audit.

Kreis and van Loock study the same balanced hybrid state under a one-sided thermal photon-noise channel and derive the noisy hybrid state explicitly.

Their finite-order Shchukin–Vogel witness detects entanglement under the amplitude-dependent sufficient condition

$$
\bar n
<
\frac{4\eta|\alpha|^2}
{(1-\eta)(2e^{4|\alpha|^2}-1)}.
$$

They explicitly compare this with the channel EB boundary

$$
\bar n\ge\frac{\eta}{1-\eta}
$$

and note that their witness may fail to detect entangled states in the remaining region.

Again, this is not an exact collision. It is arguably the strongest evidence that the exact full-region state theorem was still missing in that literature line.

---

## 7. What is definitely old after this audit

The following must not be advertised as new:

1. the hybrid state $|0\rangle|\alpha\rangle+|1\rangle|-\alpha\rangle$;
2. arbitrary branch probabilities in that virtual state;
3. binary coherent prepare-and-measure channel testing;
4. source-replacement/effective-entanglement equivalence;
5. PPT/NPT verification of the virtual qubit-mode state;
6. using coherent-state displacement plus vacuum/threshold detection;
7. negativity as a quantitative measure for the same virtual state;
8. thermal beam-splitter noise applied to the same state;
9. the thermal attenuator EB boundary $\bar n=\eta/(1-\eta)$;
10. a finite coherent alphabet capable of attaining optimal Gaussian-channel benchmarking strength.

---

## 8. What remains alive after this pass

The remaining candidate is now extremely narrow and should be worded exactly:

> **For a known gauge-covariant phase-insensitive one-mode Gaussian channel, the actual output obtained from every finite nontrivial binary coherent hybrid input is NPT if and only if the channel is non-entanglement-breaking. A single channel-matched coherent-state $2\times2$ principal minor witnesses this entire region exactly.**

This differs from the old EVM/moment benchmarks because it assumes the channel model and evaluates exact output-state matrix elements rather than inferring entanglement from a restricted set of first/second moments.

It differs from three-state/Gaussian-ensemble benchmarks because it is a theorem about the entanglement of **each individual binary source-replacement state**, not only channel certification from an optimized ensemble.

---

## 9. Why the exact three-element witness may be the cleaner contribution

The most defensible new object may be not the existence statement but the closed-form matched principal minor:

$$
M_\Gamma
=
\begin{pmatrix}
p_0&z_v^*\\z_v&p_v
\end{pmatrix},
$$

with

$$
|z_v|^2>p_0p_v
$$

and, at

$$
v_*=\frac{2\sqrt\tau a}{m},
$$

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

Old two-state EVM methods use several first/second moments and solve a semidefinite program. The repository's witness uses three selected state matrix elements and gives the exact sign boundary in closed form.

A prior-art collision for this object would need either

- the same three displaced-vacuum/coherence matrix elements;
- an algebraically equivalent $2\times2$ PT minor;
- or a theorem immediately implying this exact iff witness for the binary coherent Gaussian output.

No such result was found in this pass.

---

## 10. Next searches

The remaining search should now target equations rather than broad concepts:

- papers citing Rigas 2006 that derive exact rather than moment-limited qubit-mode PPT conditions;
- papers citing Killoran 2010 that improve the projected negativity to an exact thermal-noise result;
- papers citing Kreis–van Loock 2012 that calculate the full NPT spectrum or exact thermal threshold;
- displaced-vacuum matrix-element witnesses for hybrid entanglement;
- Husimi-Q / coherent-state principal minors under partial transpose;
- binary-modulated CV-QKD proofs that may implicitly diagonalize or partially transpose the same source-replacement state;
- exact hybrid-state negativity under thermal amplification and additive Gaussian noise;
- nonclassicality-breaking / entanglement-potential theorems that could imply the coherent result without using the same state representation.

---

## 11. Current verdict

This equation-level pass **does not kill the coherent theorem**.

It does substantially narrow what may be claimed. The field had already reached almost every surrounding ingredient by 2006–2012.

The possible contribution is therefore not a new protocol or a new state, but an **exact analytic completion**:

$$
\boxed{
\text{old: overlap-dependent sufficient two-state NPT witnesses}
\quad\longrightarrow\quad
\text{candidate: exact all-finite-pair actual-state NPT/EB equivalence.}
}

Novelty remains unverified until the citation-forward search is exhausted.
