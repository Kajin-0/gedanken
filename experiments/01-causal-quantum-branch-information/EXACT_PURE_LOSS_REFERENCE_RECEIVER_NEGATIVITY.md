# Exact Reference–Receiver Negativity for the Pure-Loss End-to-End Link

**Date:** 2026-08-08  
**Status:** **QUANTITATIVE COROLLARY — CONVERTS THE V6 LINK TRANSMISSIVITY INTO AN EXACT ENTANGLEMENT AMOUNT**

## 1. Purpose

The V6 vacuum/coherent link reduces exactly to a pure-loss channel from the virtual branch-difference mode to the accessible receiver,

$$
\boxed{
\eta
\equiv
\tau_{A\to B}(t)
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).}
$$

The known binary-coherent survival result guarantees NPT for every

$$
\eta>0
$$

and every finite nonzero branch amplitude.

For the gravity paper, the sign is not enough. The practical question is:

> How much reference–receiver entanglement survives when the complete link transmissivity is fantastically small?

For pure loss, the negativity can be calculated exactly.

---

# 2. Input hybrid state

Let the virtual difference mode be prepared in the symmetric binary-coherent hybrid state

$$
\boxed{
|\Phi_A\rangle
=\frac{
|0\rangle_R|+A\rangle
+|1\rangle_R|-A\rangle
}{\sqrt2},}
$$

with real

$$
A>0
$$

without loss of generality.

The reference states are orthogonal, so the normalization is exactly

$$
1/\sqrt2
$$

independent of the coherent-state overlap.

Send the bosonic mode through a pure-loss channel of transmissivity

$$
\eta.
$$

A beamsplitter dilation gives receiver branch amplitudes

$$
\boxed{
\pm B,
\qquad
B=\sqrt\eta\,A,}
$$

and complementary-environment amplitudes

$$
\boxed{
\pm E,
\qquad
E=\sqrt{1-\eta}\,A.}
$$

---

# 3. Reduced reference–receiver state

The complementary environment overlap is

$$
\boxed{
 s_E
\equiv
\langle-E|+E\rangle
=e^{-2(1-\eta)A^2}.}
$$

The receiver branch overlap is

$$
\boxed{
 s_B
\equiv
\langle-B|+B\rangle
=e^{-2\eta A^2}.}
$$

After tracing the environment,

$$
\boxed{
\rho_{RB}
=\frac12
\begin{pmatrix}
|B\rangle\langle B|
&
s_E|B\rangle\langle-B|
\\
s_E|-B\rangle\langle B|
&
|-B\rangle\langle-B|
\end{pmatrix}_{R}.}
$$

All effect of the complementary pure-loss output is contained in the one overlap factor

$$
s_E.
$$

---

# 4. Orthonormal receiver cat basis

The receiver support is two dimensional for

$$
B\ne0.
$$

Define normalized even/odd cat states

$$
\boxed{
|C_+\rangle
=\frac{|B\rangle+|-B\rangle}
{\sqrt{2(1+s_B)}},}
$$

$$
\boxed{
|C_-\rangle
=\frac{|B\rangle-|-B\rangle}
{\sqrt{2(1-s_B)}}.}
$$

Then

$$
|B\rangle
=a|C_+\rangle+d|C_-\rangle,
$$

$$
|-B\rangle
=a|C_+\rangle-d|C_-\rangle,
$$

with

$$
\boxed{
a=\sqrt{\frac{1+s_B}{2}},
\qquad
d=\sqrt{\frac{1-s_B}{2}}.}
$$

Thus the partial-transpose problem is an exact

$$
2\times2
\otimes
2\times2
$$

problem despite the bosonic Hilbert space.

---

# 5. Partial transpose block decomposition

After partial transpose on the reference qubit, the matrix commutes with the combined symmetry

$$
X_R\otimes Z_{\rm cat}.
$$

It therefore decomposes into two

$$
2\times2
$$

blocks.

The block that contains the negative eigenvalue is

$$
\boxed{
M_-
=\frac14
\begin{pmatrix}
(1+s_B)(1-s_E)
&
\sqrt{1-s_B^2}(1+s_E)
\\
\sqrt{1-s_B^2}(1+s_E)
&
(1-s_B)(1-s_E)
\end{pmatrix}.}
$$

Its trace is

$$
\boxed{
\Tr M_-
=\frac{1-s_E}{2}.}
$$

Its determinant is

$$
\boxed{
\det M_-
=-\frac{s_E(1-s_B^2)}{4}<0}
$$

for every

$$
A>0,
\qquad
\eta>0.
$$

Thus there is exactly one negative eigenvalue in this block.

The other symmetry block has positive determinant and nonnegative trace, so it contributes no additional negativity.

---

# 6. Exact negativity

The negative eigenvalue is

$$
\lambda_-
=\frac14
\left[
1-s_E
-
\sqrt{
(1-s_E)^2s_B^2
+(1+s_E)^2(1-s_B^2)
}
\right].
$$

The square root simplifies because

$$
(1-s_E)^2s_B^2
+(1+s_E)^2(1-s_B^2)
=(1+s_E)^2-4s_Es_B^2.
$$

Therefore the exact output negativity is

$$
\boxed{
\mathcal N(\eta,A)
=
\frac{
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
}{4},}
$$

with

$$
\boxed{
 s_E=e^{-2(1-\eta)A^2},
\qquad
 s_B=e^{-2\eta A^2}.}
$$

This is the complete pure-loss reference–receiver entanglement amount for the symmetric binary-coherent probe.

---

# 7. Checks

## Zero link

For

$$
\eta=0,
$$

$$
s_B=1,
$$

so

$$
\boxed{\mathcal N=0.}
$$

## Perfect link

For

$$
\eta=1,
$$

$$
s_E=1,
$$

and

$$
\boxed{
\mathcal N(1,A)
=\frac12\sqrt{1-e^{-4A^2}},}
$$

which is exactly the negativity of the pure input hybrid state.

## Any finite nonzero link

For

$$
0<\eta\le1,
\qquad
A>0,
$$

$$
\det M_-<0,
$$

so

$$
\boxed{\mathcal N>0.}
$$

This reproduces the pure-loss NPT survival result.

---

# 8. Weak-link expansion at fixed branch amplitude

Take

$$
\eta\ll1
$$

with fixed

$$
A>0.
$$

Expanding the exact result gives

$$
\boxed{
\mathcal N(\eta,A)
=
\eta
\frac{2A^2}
{e^{2A^2}-1}
+O(\eta^2).}
$$

Thus the output negativity is **linear in the complete link transmissivity** for every fixed finite branch amplitude.

The coefficient satisfies

$$
0<
\frac{2A^2}{e^{2A^2}-1}
<1.
$$

Large branch separation is actually unfavorable for an extremely weak link because the complementary environment then obtains a strong which-branch record.

---

# 9. Optimized weak-link asymptotics

For a very weak link, the branch amplitude can itself be optimized.

The correct asymptotic balance occurs when

$$
\boxed{
A^2=y\sqrt\eta}
$$

with

$$
y=O(1).
$$

Writing

$$
\epsilon=\sqrt\eta,
$$

the exact negativity expands as

$$
\boxed{
\mathcal N
=
\epsilon^2
-
\left(y+\frac1y\right)\epsilon^3
+
\frac{y^4+6y^2+6}{3y^2}\epsilon^4
+O(\epsilon^5).}
$$

The first correction is optimized by

$$
\boxed{y=1.}
$$

Therefore

$$
\boxed{
A_{\rm opt}^2
=\sqrt\eta
+O(\eta),}
$$

or equivalently

$$
\boxed{
A_{\rm opt}
\sim\eta^{1/4}.}
$$

The optimized negativity is

$$
\boxed{
\mathcal N_{\max}(\eta)
=
\eta
-2\eta^{3/2}
+\frac{13}{3}\eta^2
+O(\eta^{5/2}).}
$$

In particular,

$$
\boxed{
\mathcal N_{\max}(\eta)
\sim\eta
\qquad(\eta\to0).}
$$

There is no hidden square-root enhancement of the delivered entanglement in the weak-link limit.

---

# 10. Relation to branch-distance norm

The total branch-difference coherent-state distance of the virtual input is

$$
\boxed{
N_{\Delta,{\rm all}}
=4A^2.}
$$

At the weak-link optimum,

$$
\boxed{
N_{\Delta,{\rm all}}^{\rm opt}
\sim4\sqrt\eta.}
$$

Thus maximizing the absolute delivered negativity of an extremely weak link favors a **weak branch source**, not a macroscopically separated coherent pair.

The reason is complementary-record leakage:

- increasing
  $$
  A
  $$
  increases the receiver branch separation;
- but it also increases the branch record left in the unobserved complement.

The optimum balances those two effects.

This is the same physical logic that appeared in earlier weak-link witness optimization, now expressed directly in the exact entanglement negativity.

---

# 11. V6 benchmark consequence

For the ordinary/ordinary historical link ceiling,

$$
\eta_Q^{\rm link}
\simeq1.87\times10^{-42},
$$

and ideal temporal shaping,

$$
\eta\simeq1.87\times10^{-42}.
$$

Therefore the maximum pure-loss reference–receiver negativity is, to an accuracy utterly dominated by the leading term,

$$
\boxed{
\mathcal N_{\max}
\simeq1.87\times10^{-42}.}
$$

For the matched passive exponential benchmark,

$$
\eta\simeq1.01\times10^{-42},
$$

so

$$
\boxed{
\mathcal N_{\max}
\simeq1.01\times10^{-42}.}
$$

For the one-ideal-interface receiver-local scale,

$$
\eta\sim10^{-22},
$$

the optimized negativity is likewise of order

$$
10^{-22}.
$$

Thus the end-to-end branching correction propagates directly into the entanglement amount rather than being softened by the nonlinear state geometry.

---

# 12. Logarithmic negativity

The logarithmic negativity is

$$
E_N
=\log_2(1+2\mathcal N).
$$

For

$$
\mathcal N\ll1,
$$

$$
\boxed{
E_N
=\frac{2}{\ln2}\mathcal N
+O(\mathcal N^2).}
$$

Therefore the optimized weak-link logarithmic negativity also scales linearly with

$$
\eta.
$$

No choice of entanglement monotone removes the basic end-to-end transmissivity suppression in the weak-link regime.

---

# 13. Noise changes the conclusion quantitatively

This note treats pure loss only.

If the effective link has phase-insensitive Gaussian noise

$$
m>0,
$$

then the link becomes entanglement breaking when

$$
\eta\le m
$$

in the repository convention.

Close to that boundary the negativity is further suppressed and eventually vanishes exactly.

Source phase diffusion or other non-Gaussian noise requires a separate treatment, as emphasized in

`SOURCE_DEPHASING_BEYOND_BRANCHING.md`.

Thus

$$
\mathcal N_{\max}\sim\eta
$$

is an optimistic vacuum-link ceiling on the amount of transferred entanglement.

---

# 14. Manuscript recommendation

The paper should add one short quantitative paragraph after the link-budget benchmark:

> In the ideal vacuum link, the exact negativity of the binary-coherent reference–receiver state can be evaluated analytically. If \(A\) is the virtual branch amplitude and \(\eta=\tau_{A\to B}\), the complementary and receiver overlaps are \(s_E=e^{-2(1-\eta)A^2}\) and \(s_B=e^{-2\eta A^2}\), giving
> $$
> \mathcal N=
> \frac{\sqrt{(1+s_E)^2-4s_Es_B^2}-(1-s_E)}{4}.
> $$
> Optimizing for \(\eta\ll1\) gives \(A_{\rm opt}^2\sim\sqrt\eta\) and \(\mathcal N_{\max}=\eta-2\eta^{3/2}+O(\eta^2)\). Thus the extremely small end-to-end link coefficient translates directly into an equally small deliverable entanglement scale.

This converts the V6 feasibility discussion from a channel-efficiency statement into an actual entanglement amount without invoking a new Gaussian theorem.
