# Standalone Paper Core — Schmidt-Rank-Two Tests of One-Mode Gaussian Entanglement Breaking

**Date:** 2026-08-07  
**Status:** Candidate standalone mathematical paper. Novelty remains unverified; this document is for theorem organization and adversarial review, not publication claims.

## Working title

**Schmidt-Rank-Two Probes Suffice to Detect Entanglement Breaking in One-Mode Gaussian Channels**

Alternative:

**Two Pure-Gaussian Branches Detect Every Quantum-Capable One-Mode Gaussian Channel**

---

## Abstract — cautious working version

Entanglement breaking of an infinite-dimensional bosonic channel is formally defined by its action on arbitrary entangled inputs, and standard finite-energy tests of Gaussian channels employ two-mode squeezed states with infinite Schmidt rank. We show that the one-mode Gaussian structure permits a much smaller test family. First, for a gauge-covariant phase-insensitive Gaussian channel we derive a closed coherent-state matrix element and prove that every finite nontrivial qubit–binary-coherent hybrid state has an NPT output exactly when the channel is not entanglement breaking. The proof uses a single optimized $2\times2$ principal minor of the partial transpose. Gaussian-unitary canonicalization then extends the result to all regular orientation-preserving one-mode Gaussian channels, replacing coherent branches by two displaced copies of one pure Gaussian state. The remaining singular $B_1$ class is covered by a finite regularization and PPT-monotonicity argument, while the $A$ and phase-conjugating $D$ classes are entanglement breaking directly from the Gaussian EB criterion. Consequently, every non-entanglement-breaking one-mode Gaussian channel admits an NPT witness using only a qubit reference and two finite equal-covariance pure-Gaussian branches. For the phase-insensitive family the result is stronger: every nontrivial finite coherent pair detects the exact EB boundary. We also derive an explicit three-element witness and its weak-channel absolute negativity lower bound.

---

# 1. Motivation

The EB definition is

$$
\mathcal N\in\mathrm{EB}
\iff
(I_R\otimes\mathcal N)(\rho_{RA})
\text{ separable for every }\rho_{RA}.
$$

For finite dimensions, a maximally entangled state provides the Choi test.

For bosonic channels, the formal maximally entangled state is nonnormalizable. Finite-squeezing TMSV states are known to provide physically valid finite-energy EB tests, but

$$
\operatorname{SRank}(|\mathrm{TMSV}(r)\rangle)=\infty
$$

for every $r>0$.

The question is:

> **How small can the entangled test resource be for a one-mode Gaussian channel?**

The candidate answer is

$$
\boxed{
\text{Schmidt rank }2.
}
$$

---

# 2. Phase-insensitive channel convention

Use

$$
\boxed{
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp\left[-\frac{2m+1-\tau}{2}|\xi|^2\right].
}
$$

Here

- $\tau\ge0$ is intensity transmission/gain;
- $m\ge0$ is the output occupation generated from vacuum.

The established EB boundary is

$$
\boxed{
\Phi_{\tau,m}\in\mathrm{EB}
\iff
m\ge\tau.
}
$$

---

# 3. Lemma: exact coherent-dyad matrix element

For arbitrary coherent states,

$$
\boxed{
\langle u|
\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)
|v\rangle
=
\frac{\langle\beta|\alpha\rangle\langle u|v\rangle}{m+1}
\exp\left[
\frac{(\sqrt\tau\beta^*-u^*)(v-\sqrt\tau\alpha)}{m+1}
\right].
}
$$

## Proof

Use the coherent-dyad symmetric characteristic function

$$
\chi_{\alpha\beta}(\xi)
=\langle\beta|\alpha\rangle
\exp\left[
-\frac{|\xi|^2}{2}
+\beta^*\xi
-\alpha\xi^*
\right],
$$

apply the channel, reconstruct with Weyl operators, and evaluate

$$
\int\frac{d^2\xi}{\pi}
\exp(-A|\xi|^2+B\xi+C\xi^*)
=
A^{-1}e^{BC/A}.
$$

No Fock truncation or Gaussian-state covariance reduction is used.

---

# 4. Main theorem for the phase-insensitive family

Take

$$
|\Psi\rangle
=
\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\neq\beta.
$$

## Theorem 1

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

Thus

$$
\boxed{
\Phi_{\tau,m}\text{ non-EB}
\iff
\text{every finite nontrivial binary coherent probe has NPT output}.
}
$$

---

# 5. Direct finite-principal-minor proof

By displacement/phase covariance reduce the bosonic branches to

$$
|+a\rangle,
\qquad
|-a\rangle,
\qquad a>0.
$$

Compress the partial transpose to

$$
\{|0\rangle|0\rangle,\ |1\rangle|v\rangle\}.
$$

Define

$$
p_0=\langle0,0|\rho|0,0\rangle,
$$

$$
p_v=\langle1,v|\rho|1,v\rangle,
$$

$$
z_v=\langle1,0|\rho|0,v\rangle.
$$

The $2\times2$ block is indefinite iff

$$
|z_v|^2>p_0p_v.
$$

For $m>0$,

$$
\ln\frac{|z_v|^2}{p_0p_v}
=
-4a^2-v^2
+
\frac{4\tau a^2+4\sqrt\tau av+v^2}{m+1}.
$$

The optimum is

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and

$$
\boxed{
\ln\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\frac{4a^2}{m}(\tau-m).
}
$$

Thus $\tau>m$ gives a finite negative PT minor.

If $m\ge\tau$, the established EB criterion implies separability.

---

# 6. Pure-loss edge case

At

$$
m=0,
$$

$$
\ln\frac{|z_v|^2}{p_0p_v}
=
4a^2(\tau-1)
+4\sqrt\tau av.
$$

For every

$$
\tau>0,
$$
choose finite

$$
\boxed{
v>a(1-\tau)/\sqrt\tau}
$$

to obtain NPT.

At $\tau=0$ the channel is a replacer.

Thus the theorem includes the complete pure-loss boundary without an infinite-amplitude limiting state.

---

# 7. Exact three-element witness

The same principal minor is directly operational.

Every separable state satisfies

$$
\boxed{|z_v|^2\le p_0p_v.}
$$

For the optimized phase-insensitive probe,

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\exp\left[
\frac{|\alpha-\beta|^2}{m}
(\tau-m)
\right].
}
$$

Thus two populations plus one coherence detect the full phase-insensitive EB boundary.

---

# 8. Absolute witness weight

Define

$$
M_v=
\begin{pmatrix}
p_0&z_v^*\\z_v&p_v\end{pmatrix}.
$$

Its negative eigenvalue yields

$$
\boxed{
G(v)
=\frac12
\max\left\{
0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
}
$$

Since $M_v$ is a compression of the full partial transpose,

$$
\boxed{\mathcal N(\rho)\ge G(v).}
$$

For weak channels,

$$
\tau,m\ll1,
$$

jointly optimizing branch separation and analysis displacement gives

$$
\boxed{
G_{\rm abs}^{\rm opt}
=\frac{W(e^{-1})}{2}
(\tau-m)+O(\tau^2).
}
$$

This provides an absolute rather than normalized certification strength.

---

# 9. Regular one-mode Gaussian channels

Write a general one-mode Gaussian channel as

$$
V\mapsto XVX^T+Y.
$$

For

$$
\det X>0,
\qquad
Y>0,
$$

Williamson plus input/output symplectic transformations give

$$
X\to\sqrt\tau I,
$$

$$
Y\to yI.
$$

Therefore the channel is Gaussian-unitarily equivalent to $\Phi_{\tau,m}$.

Pulling a coherent pair back through the common input Gaussian unitary gives two states

$$
|\psi_0\rangle,\ |\psi_1\rangle
$$

with

- identical pure covariance;
- distinct phase-space displacement;
- finite energy for finite channel parameters.

Local output unitaries preserve NPT.

Thus every non-EB regular one-mode Gaussian channel admits the desired rank-two probe.

---

# 10. Canonical classes that are automatically EB

For one mode,

$$
K^T\Omega K=(\det K)\Omega.
$$

Using Holevo's Gaussian EB decomposition criterion:

## $\det K=0$

Every physical channel is EB.

## $\det K<0$

Every physical orientation-reversing / phase-conjugating channel is EB.

The proof can be given explicitly by decomposing the CP noise matrix into the two covariance pieces required by the EB criterion.

Therefore only orientation-preserving channels require constructive non-EB probes.

---

# 11. Singular $B_1$ class

The only nontrivial singular-noise case is

$$
K=I,
$$

with rank-one additive noise.

Write its canonical noise as

$$
Y=
\begin{pmatrix}
b&0\\0&0\end{pmatrix}.
$$

Add a finite local post-processing noise

$$
\epsilon>0
$$

in the null quadrature:

$$
Y_\epsilon=
\begin{pmatrix}
b&0\\0&\epsilon\end{pmatrix}.
$$

Choose finite

$$
0<\epsilon<1/b
$$

so the resulting full-rank unit-gain additive channel remains non-EB.

The regular theorem supplies a finite rank-two pure-Gaussian probe whose **post-regularization** output is NPT.

If the pre-regularization $B_1$ output were PPT, local Gaussian noise could not make it NPT.

Therefore the same finite probe already has NPT output after $B_1$.

No infinite squeezing limit is required.

---

# 12. Complete one-mode theorem

Combining all canonical classes:

## Theorem 2

For an arbitrary one-mode Gaussian channel $\mathcal N$,

$$
\boxed{
\mathcal N\text{ non-EB}
}
$$

iff there exists a finite Schmidt-rank-two pure state

$$
\boxed{
|\Psi_G\rangle
=
\sqrt p|0\rangle|\psi_0\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\psi_1\rangle
}
$$

where $|\psi_0\rangle,|\psi_1\rangle$ are two distinct displaced copies of one finite-covariance pure Gaussian state, such that

$$
\boxed{
(I\otimes\mathcal N)(|\Psi_G\rangle\langle\Psi_G|)
\text{ is NPT}.
}
$$

---

# 13. Resource reduction relative to known Gaussian EB tests

Known finite-resource Gaussian EB tests can use a finite-squeezing TMSV:

$$
|\mathrm{TMSV}(r)\rangle
=\frac1{\cosh r}
\sum_{n=0}^{\infty}
(\tanh r)^n|n,n\rangle.
$$

For every finite $r>0$,

$$
\operatorname{SRank}=\infty.
$$

The present theorem reduces the required test structure to

$$
\boxed{
\operatorname{SRank}=2.
}
$$

The reference system can be a qubit.

The bosonic side needs only two finite Gaussian branches.

This—not finite energy alone—is the candidate new resource reduction.

---

# 14. Prior-art positioning

Established neighboring results include:

- Holevo's Gaussian EB criterion and one-mode canonical classification;
- Caruso–Giovannetti–Holevo canonical/unitary reductions;
- finite-squeezing TMSV EB tests for Gaussian channels;
- general Schmidt-number / partially entanglement-breaking channel theory;
- binary coherent/effective-entanglement channel benchmarks;
- Kreis–van Loock's hybrid coherent/qubit thermal-channel analysis.

Targeted searches have not yet located:

1. Schmidt-rank-two sufficiency for all non-EB one-mode Gaussian channels;
2. equal-covariance two-pure-Gaussian-branch sufficiency;
3. the stronger all-finite-coherent-pairs theorem for the phase-insensitive family;
4. the exact three-element principal-minor witness saturating that family’s EB boundary.

This is not proof of novelty.

---

# 15. Why this may deserve a separate paper

The result is independent of gravity.

It has a short theorem statement, a direct proof in the main physical channel family, a complete canonical-class extension, and a clear resource reduction relative to standard CV EB tests.

If novelty survives expert literature review, the cleanest publication strategy may be:

### Paper A — quantum information

Schmidt-rank-two tests of one-mode Gaussian EB channels.

### Paper B — gravitational application

Use the binary coherent theorem as a lemma in the source-resolved gravitational receiver calculation.

This separation would prevent the mathematical result from being obscured by the much more assumption-heavy gravity model.

---

# 16. Submission-critical checks

1. Search Schmidt-number-breaking / $k$-PEB literature for an equivalent one-mode Gaussian result.
2. Have an independent expert reproduce the direct principal-minor proof.
3. Put all covariance conventions into one notation and verify every factor of $1/2$.
4. Determine whether the equal-covariance branch pair can be chosen with a useful energy bound as a function of channel parameters, especially near singular $B_1$.
5. If novelty survives, write this as a standalone theorem paper before the gravity paper.