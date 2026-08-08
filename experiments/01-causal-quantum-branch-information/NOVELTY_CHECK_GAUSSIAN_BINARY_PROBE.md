# Novelty Check — Binary Coherent Probe Completeness for Phase-Insensitive Gaussian Channels

**Updated:** 2026-08-07  
**Status:** **ACTIVE CANDIDATE NOVELTY — ADVERSARIAL SEARCH IN PROGRESS**

## 1. Candidate theorem under audit

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
\alpha\neq\beta,
$$

and every one-mode gauge-covariant phase-insensitive Gaussian channel $\Phi_{\tau,m}$,

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m,
}
$$

where $\tau>m$ is exactly the non-entanglement-breaking region in the repository convention.

For symmetric real branches $|\pm a\rangle$ and $m>0$, the direct principal-minor proof gives

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

Thus the matched $2\times2$ partial-transpose principal minor is negative exactly in the non-EB region for every finite $a>0$.

The pure-loss edge $m=0$ is treated separately with a finite analysis displacement.

---

## 2. Important change after the Mele–Lami–Giovannetti audit

The repository previously treated the finite Schmidt-rank-two **Fock** theorem as a possible novelty. That claim has now been killed by prior art.

Mele, Lami, and Giovannetti, arXiv:2303.12867 / *Nature Photonics* (2025), use

$$
|\Psi_{M,c}\rangle
=c|0,0\rangle+\sqrt{1-c^2}|M,M\rangle
$$

and prove in Supplementary Remark 1 that, after a local $\{|0\rangle,|M\rangle\}$ projection, the state is non-PPT/distillable exactly when their phase-insensitive channel is non-EB, independently of $M$ and $c$.

Under

$$
\tau=g\lambda,
\qquad
m=g-1,
$$

their condition

$$
(1-\lambda)g<1
$$

is exactly

$$
\tau>m.
$$

Therefore **rank-two Fock sufficiency is prior art**.

See:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

### Why this does not automatically kill the present coherent theorem

The Mele input branches are orthogonal number states

$$
|0\rangle,\quad |M\rangle.
$$

The present theorem claims something different and stronger within a specific nonorthogonal family:

> **every pair of distinct finite coherent states works, at every nonzero separation, with arbitrary nonzero branch weights.**

No inference from existence of a Fock rank-two probe establishes that every nonorthogonal coherent pair has the same exact property.

The coherent theorem therefore remains an independent novelty question.

---

## 3. Häseler–Moroder–Lütkenhaus (2008): paradigm collision, not yet theorem collision

H. Häseler, T. Moroder, and N. Lütkenhaus,

**“Testing Quantum Devices: Practical Entanglement Verification in Bipartite Optical Systems,”**

PRA 77, 032303 (2008), arXiv:0711.2709.

Established there:

- device/channel testing with nonorthogonal input states;
- effective-entanglement reformulation;
- a binary coherent alphabet $|\pm\alpha\rangle$;
- partial-transpose expectation-value matrices;
- practical coherent-state/homodyne tests.

This is conceptually very close and must be cited prominently.

However, their operational criterion is based on restricted measured expectation values/moments. The corresponding separability-compatible noise boundary depends on the coherent-state overlap/amplitude.

The current repository result instead assumes the exact Gaussian channel and evaluates selected matrix elements of the **actual output state**. Its claimed NPT boundary is independent of every finite nonzero coherent separation.

No theorem in the inspected Häseler paper has yet been found that states

$$
\forall\alpha\neq\beta:\quad
\rho_{\rm out}\text{ NPT}\iff\Phi\text{ non-EB}.
$$

---

## 4. Kreis–van Loock (2012): strongest direct predecessor

K. Kreis and P. van Loock,

**“Classifying, quantifying, and witnessing qudit-qumode hybrid entanglement,”**

PRA 85, 032307 (2012), arXiv:1111.0478.

This is currently the most dangerous coherent-state prior art because it studies the same symmetric hybrid input

$$
\frac{|0\rangle|\alpha\rangle+|1\rangle|-\alpha\rangle}{\sqrt2}
$$

with one-sided thermal photon noise modeled by a beam splitter with a thermal environment.

They derive the noisy hybrid state and apply a finite-order Shchukin–Vogel moment witness.

Their stated sufficient thermal-entanglement condition is amplitude dependent:

$$
\bar n
<
\frac{4\eta|\alpha|^2}
{(1-\eta)(2e^{4|\alpha|^2}-1)}.
$$

They compare this with the known thermal-channel EB threshold and note that the chosen moment witness can fail to detect entanglement in part of the non-EB region.

### Current distinction

The repository claims to close precisely that gap:

$$
\boxed{
\bar n<\frac{\eta}{1-\eta}
\Longrightarrow
\rho_{AB}\text{ NPT for every finite }\alpha\neq0,
}
$$

with the converse following from the channel being EB.

If correct and absent from later literature, this is the strongest novelty case because the same state/channel problem was explicitly studied previously without an exact full-region result.

See:

- `NOVELTY_CHECK_FINITE_CAT.md`

---

## 5. Namiki–Azuma and coherent-state ensemble benchmarks

R. Namiki and K. Azuma,

**“Quantum Benchmark via an Uncertainty Product of Canonical Variables,”**

PRL 114, 140503 (2015), arXiv:1404.2643.

They establish a benchmark based on a Gaussian-distributed coherent-state ensemble and homodyne measurements that can verify quantum-domain performance for all one-mode Gaussian channels.

Therefore do not claim that coherent states had not previously provided complete Gaussian-channel quantum benchmarks.

The distinction under audit is:

- their result: ensemble/average benchmark against EB channels;
- current candidate: exact NPT of **each individual binary coherent hybrid state**, for every finite nonzero pair separation.

---

## 6. Other neighboring results already checked

### Rigas–Gühne–Lütkenhaus

Qubit-mode separability criteria and effective-entanglement verification using covariance information / semidefinite methods. Relevant framework, but no exact all-coherent-pair thermal-channel NPT iff theorem located.

### Sabapathy–Ivan–Simon

Analytic non-Gaussian entanglement robustness under noisy attenuator/amplifier channels, including Fock/NOON-like families. Important technical neighborhood, but no inspected result matching the binary qubit–coherent theorem.

### Ivan–Sabapathy–Simon

Nonclassicality-breaking and entanglement-breaking Gaussian channels are closely related/up to Gaussian unitaries. Important structural result, but no direct implication has yet been found that forces every binary coherent hybrid state to be NPT throughout the full non-EB region.

### Entangled coherent-state literature

Two-bosonic-mode entangled coherent states under thermal noise are related but are not the same DV–CV hybrid state. These papers must nevertheless be searched for partial-transpose identities that may specialize to the current witness.

---

## 7. Exact theorem ingredients that a collision must reproduce or imply

A prior-art collision need not use the repository's notation. It counts if it proves or immediately implies all of the substantive content below.

### State family

Every finite pair

$$
\alpha\ne\beta
$$

and every

$$
0<p<1.
$$

### Channel family

All gauge-covariant phase-insensitive one-mode Gaussian channels, including

- thermal attenuation;
- thermal amplification;
- additive Gaussian noise;
- pure loss as a singular edge.

### Actual-state criterion

Not merely a sufficient limited-moment test, but

$$
\rho_{\rm out}\text{ NPT}
\iff
\text{channel non-EB}.
$$

### Exact low-dimensional witness

For $m>0$, a finite coherent analysis state with

$$
v_*=2\sqrt\tau a/m
$$

gives a $2\times2$ principal minor whose sign is exactly

$$
\operatorname{sgn}(m-\tau).
$$

If prior art proves these facts by another representation, the candidate novelty is dead.

---

## 8. Pure-loss edge must remain separate in any audit

The optimized thermal witness has

$$
v_*=2\sqrt\tau a/m,
$$

which diverges as $m\to0^+$.

This does **not** mean an infinite-amplitude witness is required at pure loss.

For $m=0$,

$$
\ln R(v)
=4a^2(\tau-1)+4\sqrt\tau av.
$$

For every

$$
\tau>0,
$$

choose any finite

$$
\boxed{
v>\frac{a(1-\tau)}{\sqrt\tau}.
}
$$

Then $R(v)>1$ and the output is NPT.

Any prior-art comparison that treats only $m>0$ does not automatically cover this finite pure-loss witness construction, although pure-loss survival of hybrid coherent entanglement itself is certainly not new.

---

## 9. Current strongest novelty hypothesis

The safest candidate statement is now:

> **For every gauge-covariant phase-insensitive one-mode Gaussian channel, every individual finite nontrivial binary coherent hybrid input has NPT output if and only if the channel is not entanglement breaking. This iff boundary is exposed by one channel-matched $2\times2$ coherent-state principal minor.**

Do not broaden this to claims about coherent-state quantum benchmarks generally.

---

## 10. Required adversarial search

Priority searches:

1. citation-forward search of Kreis–van Loock (2012), especially papers computing full negativity/PPT rather than moment witnesses;
2. citation-forward search of Häseler–Moroder–Lütkenhaus (2008), especially upgrades from EVM sufficiency to exact state criteria;
3. binary-modulated CV-QKD entanglement proofs;
4. hybrid qubit–oscillator entanglement under thermal amplifiers and additive Gaussian noise;
5. coherent-state matrix-element / Husimi-Q-function partial-transpose witnesses;
6. displaced-vacuum projection witnesses;
7. general theorems linking coherent-state nonclassicality, nonclassicality breaking, and entanglement potential strongly enough to imply the all-pairs result.

Search equations, supplements, appendices, theses, and follow-up papers. The Mele collision was buried in supplementary material and demonstrates why abstract-level searches are insufficient.

---

## 11. Current assessment

### Killed

- rank-two Fock probe novelty;
- fixed Fock Bell-state novelty as an underlying sufficiency theorem.

### Still alive but unverified

- every finite binary coherent pair works;
- exact actual-state NPT/EB equivalence for the coherent hybrid family;
- exact matched three-element coherent-state witness.

### Confidence

The mathematics currently appears strong, supported by a direct coherent-kernel proof, a separate pure-loss edge proof, and independent channel simulations. The dominant uncertainty is **prior art**, not internal algebra.

No originality claim should be made until the citation-forward search described above is exhausted.
