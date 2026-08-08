# Adversarial Proof Audit — Binary Coherent Gaussian NPT Theorem

**Date:** 2026-08-07  
**Status:** **INTERNALLY DERIVED — INDEPENDENT ALGEBRAIC RECHECK PASSED**

## 1. Claim under attack

For the one-mode gauge-covariant phase-insensitive Gaussian channel

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp\left[-\frac{2m+1-\tau}{2}|\xi|^2\right],
$$

and any finite nontrivial binary coherent hybrid input

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

the output is NPT iff

$$
\boxed{\tau>m.}
$$

This audit rederives the result without assuming the intermediate formulas in `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`.

---

## 2. Coherent-dyad characteristic function

For a coherent dyad $|\alpha\rangle\langle\beta|$ and the symmetrically ordered characteristic function,

$$
\chi_{\alpha\beta}(\xi)
=\operatorname{Tr}\left[|\alpha\rangle\langle\beta|D(\xi)\right]
=\langle\beta|D(\xi)|\alpha\rangle.
$$

Using the displacement action on coherent states,

$$
\boxed{
\chi_{\alpha\beta}(\xi)
=\langle\beta|\alpha\rangle
\exp\left[
-\frac{|\xi|^2}{2}
+\beta^*\xi
-\alpha\xi^*
\right].
}
$$

After the channel,

$$
\chi_{\rm out}(\xi)
=\langle\beta|\alpha\rangle
\exp\left[
-\frac{2m+1}{2}|\xi|^2
+\sqrt\tau\beta^*\xi
-\sqrt\tau\alpha\xi^*
\right].
$$

The cancellation of the $\tau$ term in the Gaussian width is an important convention check.

---

## 3. Independent Weyl reconstruction

Use

$$
O=\int\frac{d^2\xi}{\pi}\chi_O(\xi)D(-\xi)
$$

and

$$
\langle u|D(-\xi)|v\rangle
=\langle u|v\rangle
\exp\left[-\frac{|\xi|^2}{2}-u^*\xi+v\xi^*\right].
$$

The full exponent becomes

$$
-(m+1)|\xi|^2
+(\sqrt\tau\beta^*-u^*)\xi
+(v-\sqrt\tau\alpha)\xi^*.
$$

Using

$$
\int\frac{d^2\xi}{\pi}
\exp(-A|\xi|^2+B\xi+C\xi^*)
=\frac1A\exp(BC/A),
\qquad \Re A>0,
$$

gives

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

This reproduces the repository kernel independently.

### Sanity checks

#### Vacuum input

Set $\alpha=\beta=0$. Then

$$
\langle0|\Phi(|0\rangle\langle0|)|0\rangle
=\frac1{m+1},
$$

which is the vacuum probability of a thermal state with mean occupation $m$.

#### Coherent input

Set $\alpha=\beta=a$ and evaluate at $u=v=\sqrt\tau a$. Then

$$
\langle\sqrt\tau a|\Phi(|a\rangle\langle a|)|\sqrt\tau a\rangle
=\frac1{m+1},
$$

consistent with a displaced thermal output of occupation $m$.

These checks strongly constrain normalization mistakes.

---

## 4. Symmetric binary state and PT compression

By displacement covariance and phase covariance, any distinct coherent pair can be transformed by local unitaries into

$$
|+a\rangle,
\qquad
|-a\rangle,
\qquad a>0,
$$

with real $a$.

Take the balanced state first:

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle+|1\rangle|-a\rangle}{\sqrt2}.
$$

Define

$$
A=\Phi(|a\rangle\langle a|),
\qquad
B=\Phi(|-a\rangle\langle-a|),
\qquad
X=\Phi(|a\rangle\langle-a|).
$$

After partial transpose on the qubit,

$$
\rho^{T_A}
=\frac12
\begin{pmatrix}
A&X^\dagger\\
X&B
\end{pmatrix}.
$$

Compress onto the **orthonormal** vectors

$$
|0\rangle_A|0\rangle_B,
\qquad
|1\rangle_A|v\rangle_B,
$$

where $|v\rangle$ is a normalized coherent state and $v\in\mathbb R$ for the optimized symmetric problem.

Orthogonality is guaranteed by the qubit labels, so no hidden nonorthogonal-basis determinant issue exists.

The compressed block is

$$
\frac12
\begin{pmatrix}
\langle0|A|0\rangle&\langle0|X^\dagger|v\rangle\\
\langle v|X|0\rangle&\langle v|B|v\rangle
\end{pmatrix}.
$$

A negative determinant is therefore a rigorous NPT certificate.

---

## 5. Recompute all three matrix elements

From the independently derived kernel,

$$
\boxed{
A_{00}
=\langle0|A|0\rangle
=\frac1{m+1}
\exp\left[-\frac{\tau a^2}{m+1}\right].
}
$$

For real $v$,

$$
\boxed{
B_{vv}
=\langle v|B|v\rangle
=\frac1{m+1}
\exp\left[-\frac{(v+\sqrt\tau a)^2}{m+1}\right].
}
$$

Since

$$
\langle-a|a\rangle=e^{-2a^2}
$$

and

$$
|\langle v|0\rangle|^2=e^{-v^2},
$$

we obtain

$$
\boxed{
|X_{v0}|^2
=|\langle v|X|0\rangle|^2
=\frac1{(m+1)^2}
\exp\left[
-4a^2-v^2
+\frac{2\tau a^2+2\sqrt\tau av}{m+1}
\right].
}
$$

---

## 6. Principal-minor ratio

The overall factors from the balanced qubit amplitudes cancel in

$$
R(v)
\equiv
\frac{|X_{v0}|^2}{A_{00}B_{vv}}.
$$

Direct substitution gives

$$
\boxed{
\ln R(v)
=-4a^2-v^2
+\frac{4\tau a^2+4\sqrt\tau av+v^2}{m+1}.
}
$$

No channel approximation is used.

---

## 7. Global optimization for $m>0$

Differentiate:

$$
\frac{d}{dv}\ln R
=-2v+\frac{4\sqrt\tau a+2v}{m+1}.
$$

Therefore

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m}.
}
$$

The second derivative is

$$
\boxed{
\frac{d^2}{dv^2}\ln R
=-\frac{2m}{m+1}<0,
}
$$

so this is the unique global maximum on the real line for $m>0$.

Substitution gives exactly

$$
\boxed{
\ln R(v_*)
=\frac{4a^2}{m}(\tau-m).
}
$$

Hence

$$
\boxed{
R(v_*)>1
\iff
\tau>m.
}
$$

Since a negative $2\times2$ compression determinant implies $\rho^{T_A}\not\ge0$,

$$
\tau>m
\Longrightarrow
\rho_{AB}\text{ NPT}.
$$

The converse follows from the established EB condition $m\ge\tau$.

No gap is visible in this direction.

---

## 8. Pure-loss singular edge $m=0$

The $m>0$ optimizer diverges as $m\to0^+$, so pure loss must not be justified by continuity of $v_*$.

Set $m=0$ directly in the unoptimized expression:

$$
\boxed{
\ln R(v)
=4a^2(\tau-1)+4\sqrt\tau av.
}
$$

For every physical pure-loss channel with

$$
0<\tau\le1,
$$

choose any finite

$$
\boxed{
v>\frac{a(1-\tau)}{\sqrt\tau}.
}
$$

Then

$$
R(v)>1.
$$

At

$$
\tau=0,
$$

the channel is a vacuum replacer and is EB.

Thus the singular edge survives without an infinite-amplitude test state.

---

## 9. Unequal branch weights and relative phase

For

$$
|\Psi\rangle
=\sqrt p|0\rangle|a\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|-a\rangle,
$$

the two diagonal terms in the selected PT block acquire factors

$$
p,
\qquad
1-p,
$$

while the squared coherence acquires

$$
p(1-p).
$$

Therefore

$$
R(v)
$$

is unchanged for every

$$
0<p<1.
$$

The phase $\phi$ multiplies the off-diagonal entry by a unit complex phase and leaves its magnitude unchanged.

Thus neither branch weighting nor source phase produces a loophole.

---

## 10. Arbitrary complex coherent pair

For arbitrary finite

$$
\alpha\ne\beta,
$$

define the midpoint and difference

$$
\gamma=\frac{\alpha+\beta}{2},
\qquad
\delta=\alpha-\beta.
$$

A common input displacement by $-\gamma$ maps the pair to

$$
|\delta/2\rangle,
\qquad
|-\delta/2\rangle.
$$

A phase rotation maps $\delta/2$ to the positive real number

$$
a=|\delta|/2.
$$

Gauge-covariant phase-insensitive Gaussian channels are displacement and phase covariant, with the corresponding transformed output differing only by a local bosonic unitary. Local unitaries preserve PPT/NPT.

Therefore the symmetric real proof covers every distinct finite coherent pair.

---

## 11. Physical parameter edges

The proof does not assume attenuation only.

### Thermal attenuator

$$
0\le\tau\le1,
\qquad
m=(1-\tau)\bar n_E.
$$

The condition is

$$
\bar n_E<\frac{\tau}{1-\tau}.
$$

### Thermal amplifier

For gain $G>1$,

$$
\tau=G,
\qquad
m=(G-1)(\bar n_E+1),
$$

and NPT occurs iff

$$
\bar n_E<\frac1{G-1}.
$$

### Additive Gaussian noise

$$
\tau=1,
$$

and NPT occurs iff

$$
m<1.
$$

These are the established EB boundaries in the repository convention.

---

## 12. Failure modes explicitly attacked

### Attack A — wrong coherent-dyad kernel

Re-derived independently from the characteristic function and Weyl integral. Passed vacuum and displaced-thermal sanity checks.

### Attack B — illegal determinant in a nonorthogonal basis

Not present. The selected vectors are orthogonal because their qubit components are $|0\rangle$ and $|1\rangle$.

### Attack C — optimizer only local, not global

For $m>0$, $\ln R(v)$ is strictly concave in real $v$ with second derivative $-2m/(m+1)$, so $v_*$ is the unique global real optimum.

### Attack D — pure loss requires infinite analysis amplitude

False. Direct $m=0$ optimization gives a finite threshold on $v$ for every $\tau>0$.

### Attack E — branch weights or phase break the theorem

They cancel from the determinant ratio or only rotate the coherence phase.

### Attack F — arbitrary coherent pairs cannot be reduced to symmetric real form

A common displacement plus phase rotation does so, and channel covariance converts the transformation into local output unitaries.

### Attack G — converse uses an unproved state-specific claim

No. The converse uses only the established channel theorem: if $m\ge\tau$, the channel is EB and therefore every bipartite output is separable/PPT.

---

## 13. Current proof verdict

No mathematical counterexample or algebraic failure was found in this audit.

The strongest remaining vulnerability is **external novelty**, not the phase-insensitive proof itself.

The exact theorem should nevertheless be presented with narrow scope:

> For a **known** gauge-covariant phase-insensitive Gaussian channel, every finite nontrivial binary coherent hybrid input has an NPT output exactly when the channel is non-entanglement-breaking.

Do not present the three-element minor as a prepare-and-measure benchmark using only the two conditional output states. Its off-diagonal element contains

$$
\Phi(|a\rangle\langle-a|),
$$

so direct implementation requires access to channel coherence / the hybrid source-replacement state, or an equivalent process-coherent measurement.

---

## 14. Next internal attack

The remaining internal verification should be implementation-independent numerical simulation for

1. thermal attenuation;
2. thermal amplification;
3. additive Gaussian noise;
4. points extremely close to $m=\tau$;
5. random coherent separation and branch weights.

The amplifier and additive-noise scripts should be committed rather than only summarized in Markdown.
