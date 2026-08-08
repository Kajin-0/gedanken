# Novelty Collision — Filippov–Ziman and the All-Binary-Coherent Theorem

**Date:** 2026-08-07  
**Status:** **COLLISION CONFIRMED — DO NOT CLAIM THE ALL-FINITE-BINARY-COHERENT SURVIVAL THEOREM AS NEW**

## 1. Repository theorem that was under audit

For every finite nontrivial qubit–mode hybrid state

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

the repository independently proves for every gauge-covariant phase-insensitive one-mode Gaussian channel $\Phi_{\tau,m}$

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

The direct repository proof remains mathematically valuable. The underlying all-finite-pairs survival phenomenon is not a viable novelty claim after the audit below.

---

## 2. Decisive prior-art source

S. N. Filippov and M. Ziman,

**“Entanglement sensitivity to signal attenuation and amplification,”**

*Phys. Rev. A* **90**, 010301(R) (2014), arXiv:1405.1754.

They consider the phase-insensitive Gaussian channel

$$
\Phi(\kappa,\mu)
$$

with characteristic-function scaling parameter $\kappa$ and total noise $\mu$.

Complete positivity requires

$$
\mu\ge\frac12|\kappa-1|.
$$

Define the excess noise

$$
\boxed{
a=\mu-\frac12|\kappa-1|\ge0.
}
$$

They use the quantum-limited attenuator/amplifier decomposition

$$
\Phi(\kappa,\mu)
=\Phi_{\rm QL,T}\circ\Phi_{\rm QL,\eta},
$$

with

$$
\eta=\frac{\kappa}{T},
$$

and

$$
\boxed{
T=
\begin{cases}
1+a,&0<\kappa<1,\\
\kappa+a,&\kappa>1.
\end{cases}
}
$$

The known entanglement-breaking criterion in these variables is

$$
\boxed{
a\ge\min(\kappa,1).}
$$

---

## 3. Their non-Gaussian coherent-state input

Filippov and Ziman choose

$$
\boxed{
|\psi_\gamma\rangle
=\frac{|\gamma\rangle_A|0\rangle_B
-|0\rangle_A|\gamma\rangle_B}
{\sqrt{2(1-e^{-|\gamma|^2})}},
\qquad
\gamma\ne0.
}
$$

Their Proposition 2 applies independent phase-insensitive Gaussian channels to the two modes and derives an entanglement witness for the output.

The relevant witness is

$$
\boxed{
W_\lambda
=\int\frac{d^2\alpha}{\pi}
\frac{d^2\beta}{\pi}
\,e^{\lambda(|\alpha|^2+|\beta|^2)}
|\alpha\rangle\langle\beta|
\otimes
|\beta\rangle\langle\alpha|.
}
$$

They explicitly allow an unbounded $W_\lambda$ when its expectation on the output remains finite.

---

## 4. One-sided specialization

The repository problem applies a noisy channel to only one member of a bipartite state. Therefore specialize the Filippov–Ziman calculation to

$$
\Phi(\kappa,\mu)_B
$$

on mode $B$ and the identity channel on $A$.

For the identity mode,

$$
T_A=1,
\qquad
\eta_A=1.
$$

Let

$$
t\equiv1-\lambda>0,
\qquad
x\equiv|\gamma|^2.
$$

Specializing their exact witness expectation gives a positive overall prefactor multiplying

$$
\boxed{
E(t;x)
=e^{-Ax}+e^{-Bx}-2e^{-Cx},
}
$$

where

$$
\boxed{
A=\frac{\kappa}{T},
}
$$

$$
\boxed{
B=1+\frac{1-T}{Tt^2},
}
$$

and

$$
\boxed{
C=1-\frac{\sqrt\kappa}{Tt}.
}
$$

This is a direct specialization of their published expectation-value formula.

---

## 5. Choose the witness so the two positive exponentials coincide

For finite excess noise $a>0$, choose

$$
\boxed{
t^2=\frac{T-1}{T-\kappa}.}
$$

Then

$$
\boxed{A=B.}
$$

Therefore

$$
E(t;x)
=2\left(e^{-Ax}-e^{-Cx}\right).
$$

For every finite

$$
x>0,
$$

this is negative iff

$$
C<A.
$$

The condition reduces exactly to

$$
\boxed{
(T-\kappa)(T-1)<\kappa.
}
$$

No small-$\gamma$ approximation is used in this one-sided specialization.

---

## 6. Attenuator: exact EB complement for every finite $\gamma$

For

$$
0<\kappa<1,
$$

Filippov–Ziman have

$$
T=1+a.
$$

Hence

$$
(T-\kappa)(T-1)-\kappa
=(1+a-\kappa)a-\kappa.
$$

Factor:

$$
\boxed{
(1+a-\kappa)a-\kappa
=(a+1)(a-\kappa).
}
$$

Since

$$
a+1>0,
$$

the witness is negative iff

$$
\boxed{a<\kappa.}
$$

But the attenuator is EB iff

$$
a\ge\kappa.
$$

Therefore the Filippov–Ziman coherent state remains entangled, for every finite $\gamma\ne0$, exactly throughout the non-EB attenuator region.

### Quantum-limited pure-loss edge $a=0$

The equal-exponent choice has $t\to0$, but no limiting input state is required. Directly at $a=0$,

$$
A=\kappa,
\qquad
B=1,
\qquad
C=1-\frac{\sqrt\kappa}{t}.
$$

Choose any finite

$$
0<t<\frac{\sqrt\kappa}{1-\kappa}.
$$

Then

$$
C<\kappa=\min(A,B),
$$

so

$$
E(t;x)<0
$$

for every finite $x>0$.

---

## 7. Amplifier: exact EB complement for every finite $\gamma$

For

$$
\kappa>1,
$$

Filippov–Ziman have

$$
T=\kappa+a.
$$

Then

$$
(T-\kappa)(T-1)-\kappa
=a(\kappa+a-1)-\kappa.
$$

Factor:

$$
\boxed{
a(\kappa+a-1)-\kappa
=(a-1)(a+\kappa).
}
$$

Since

$$
a+\kappa>0,
$$

the witness is negative iff

$$
\boxed{a<1.}
$$

But the amplifier is EB iff

$$
a\ge1.
$$

Thus the same finite-$\gamma$ state survives exactly throughout the non-EB amplifier region.

### Quantum-limited amplifier edge $a=0$

At $a=0$,

$$
A=1,
$$

$$
B=1-\frac{\kappa-1}{\kappa t^2},
$$

$$
C=1-\frac1{\sqrt\kappa\,t}.
$$

Choose any finite

$$
t>\frac{\kappa-1}{\sqrt\kappa}.
$$

Then

$$
C<B\le A,
$$

so the witness is negative for every $\gamma\ne0$.

---

## 8. Additive-noise limit

For

$$
\kappa=1,
$$

take the continuous limit

$$
T=1+a.
$$

The equal-exponent choice gives

$$
t=1,
\qquad
\lambda=0.
$$

Then the sign condition becomes

$$
\boxed{a<1,}
$$

again exactly the complement of the unit-gain additive-noise EB threshold.

---

## 9. Mapping their state to the repository qubit–coherent state

The untouched Filippov–Ziman reference mode occupies only

$$
\mathcal S_\gamma
=\operatorname{span}\{|0\rangle,|\gamma\rangle\},
$$

which is two-dimensional for every

$$
\gamma\ne0.
$$

Because $|0\rangle$ and $|\gamma\rangle$ are linearly independent, there exists an invertible local filter on $\mathcal S_\gamma$ satisfying, up to an arbitrary common normalization,

$$
F|\gamma\rangle
=\sqrt p\,|0\rangle_R,
$$

$$
F|0\rangle
=e^{i\theta}\sqrt{1-p}\,|1\rangle_R.
$$

The filter may be scaled to a legitimate finite-rank Kraus operator with nonzero success probability.

Applying it to the untouched reference transforms

$$
|\psi_\gamma\rangle
$$

into

$$
\boxed{
\sqrt p\,|0\rangle_R|0\rangle_B
-e^{i\theta}\sqrt{1-p}\,|1\rangle_R|\gamma\rangle_B.
}
$$

Because the filter acts on the untouched subsystem, it commutes with the channel on $B$.

A common displacement and phase rotation on $B$ converts the pair

$$
|0\rangle,\ |\gamma\rangle
$$

into any desired finite distinct coherent pair

$$
|\alpha\rangle,\ |\beta\rangle
$$

up to local phases. Phase-insensitive Gaussian covariance turns those transformations into local output unitaries, which do not change PPT/NPT.

Thus the Filippov–Ziman family is locally-filter equivalent to the entire binary coherent hybrid family used in the repository.

---

## 10. Why the Filippov–Ziman witness also implies NPT

Their paper states the witness as a general entanglement witness. For the present comparison, its Fock representation is decisive.

Set

$$
t=1-\lambda>0.
$$

Expanding the coherent dyads and carrying out the Gaussian integrals gives

$$
\boxed{
W_\lambda
=\frac1{t^2}
\sum_{m,n=0}^{\infty}
\frac1{t^{m+n}}
|m\rangle\langle n|
\otimes
|n\rangle\langle m|.
}
$$

Define finite truncations

$$
W_{\lambda,N}
=\frac1{t^2}
\sum_{m,n=0}^{N}
\frac1{t^{m+n}}
|m\rangle\langle n|
\otimes
|n\rangle\langle m|.
$$

After partial transpose on the second mode,

$$
\boxed{
W_{\lambda,N}^{T_2}
=\frac1{t^2}
|\Omega_{t,N}\rangle\langle\Omega_{t,N}|
\ge0,
}
$$

where

$$
|\Omega_{t,N}\rangle
=\sum_{n=0}^{N}t^{-n}|n,n\rangle.
$$

Therefore every finite $W_{\lambda,N}$ is a **decomposable NPT witness**.

For the one-sided Gaussian states considered above, the Fock expansion of the published finite witness expectation converges. In the attenuator case the apparently dangerous $t<1$ weighting is still dominated by the geometric thermal tail; with the equal-exponent choice,

$$
\frac{1}{t^2}\frac{a}{a+1}
=\frac{1+a-\kappa}{1+a}<1.
$$

The untouched coherent reference has Poisson tails and therefore finite exponential moments of every finite order.

Hence

$$
\operatorname{Tr}(W_{\lambda,N}\rho)
\longrightarrow
\operatorname{Tr}(W_\lambda\rho)<0.
$$

For sufficiently large finite $N$,

$$
\operatorname{Tr}(W_{\lambda,N}\rho)<0.
$$

Since $W_{\lambda,N}^{T_2}\ge0$, this is impossible for a PPT state. Therefore the Filippov–Ziman output is **NPT**, not merely generically entangled, throughout the one-sided non-EB region.

Because the local reference filter is invertible on the occupied two-dimensional support, partial transpose transforms by an invertible local congruence; PT inertia is preserved. The filtered qubit–coherent state is therefore NPT in the same parameter region.

---

## 11. Exact relation to repository channel parameters

In the repository convention, the phase-insensitive channel is EB iff

$$
m\ge\tau.
$$

The Filippov–Ziman variables map as follows.

### Attenuation

$$
\tau_{\rm repo}=\kappa,
$$

and their excess noise is exactly the repository vacuum-output occupation,

$$
m_{\rm repo}=a.
$$

Thus

$$
a<\kappa
\iff
m_{\rm repo}<\tau_{\rm repo}.
$$

### Amplification

For $\kappa>1$,

$$
\tau_{\rm repo}=\kappa,
$$

while

$$
m_{\rm repo}=\kappa-1+a.
$$

Therefore

$$
a<1
\iff
m_{\rm repo}<\kappa
\iff
m_{\rm repo}<\tau_{\rm repo}.
$$

### Additive noise

$$
\tau_{\rm repo}=1,
qquad
m_{\rm repo}=a,
$$

so

$$
a<1
\iff
m_{\rm repo}<\tau_{\rm repo}.
$$

Thus the one-sided Filippov–Ziman result and the repository theorem have the same exact phase-insensitive NPT/EB boundary.

---

## 12. What this collision kills

Do not claim as new:

1. every finite nonzero coherent separation survives a non-EB thermal attenuator;
2. every finite nonzero coherent separation survives a non-EB phase-insensitive amplifier;
3. every finite nonzero coherent separation survives a non-EB additive-noise channel;
4. arbitrary branch probabilities after a two-dimensional local reference filter;
5. the full statement that every finite nontrivial binary coherent hybrid state remains NPT iff the phase-insensitive channel is non-EB.

The repository's proof is still substantially shorter and more direct, but the underlying survival theorem is already implicit in the 2014 coherent-state witness calculation plus elementary local filtering.

---

## 13. What may still survive as a contribution

The main remaining mathematical candidate is now the repository's **minimal direct principal-minor formulation**.

For symmetric $|\pm a\rangle$ and $m>0$,

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and only three selected output matrix elements are required:

$$
p_0,\qquad p_{v_*},\qquad z_{v_*}.
$$

The exact ratio is

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

Unlike the Filippov–Ziman witness, this is

- a literal $2\times2$ principal minor of the actual partial transpose;
- finite-dimensional at the witness level;
- algebraically elementary;
- directly exposes the EB excess $\tau-m$;
- accompanied by an explicit absolute negative-eigenvalue lower bound.

Whether this **specific minimal witness / proof compression** is publication-worthy and novel remains unverified.

---

## 14. New research priority

Stop searching for novelty of the all-binary-coherent survival theorem itself.

Search instead for prior art on

1. exact $2\times2$ coherent-state PT principal minors for Gaussian channels;
2. three-matrix-element entanglement witnesses for hybrid coherent states;
3. displaced-vacuum projection witnesses equivalent to
   $$|z|^2>p_0p_v;$$
4. closed-form matched displacement
   $$v_*=2\sqrt\tau a/m;$$
5. exact low-dimensional negativity lower bounds proportional to $\tau-m$;
6. concise alternative proofs of the Filippov–Ziman one-sided result.

The strongest possible standalone paper has now narrowed from a theorem about entanglement survival to a theorem about **minimal exact certification / proof compression**.
