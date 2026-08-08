# Exact Three-Element Coherent-State PT Witness

**Updated:** 2026-08-07  
**Status:** **STRONGEST SURVIVING POSSIBLE STANDALONE CONTRIBUTION — NOVELTY UNVERIFIED**

## 1. What is and is not being claimed

The underlying entanglement-survival theorem is **not** treated as novel anymore.

Filippov–Ziman (2014) already provide a coherent-state witness which, after one-sided specialization and local filtering of the untouched two-dimensional coherent-state span, implies that every finite binary coherent hybrid survives exactly throughout the non-entanglement-breaking region of a phase-insensitive Gaussian channel.

See:

- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`

The possible contribution in this file is narrower:

> **The same full NPT boundary is exposed by one literal $2\times2$ principal minor of the actual partial transpose, requiring only two selected populations and one coherence, with a closed-form matched coherent analysis displacement.**

Whether that minimal formulation already exists in the literature remains under active audit.

---

## 2. Channel and state

Use the one-mode gauge-covariant phase-insensitive Gaussian channel

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\,\xi)
\exp\left[-\frac{2m+1-\tau}{2}|\xi|^2\right].
$$

Its established entanglement-breaking boundary is

$$
\boxed{
\Phi_{\tau,m}\in\mathrm{EB}
\iff
m\ge\tau.
}
$$

By displacement and phase covariance, an arbitrary distinct finite coherent pair can be reduced to real symmetric branches

$$
|+a\rangle,\qquad|-a\rangle,\qquad a>0.
$$

Take the balanced hybrid state

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle+|1\rangle|-a\rangle}{\sqrt2}.
$$

Unequal nonzero branch weights and a relative phase do not change the principal-minor ratio; see `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`.

---

## 3. Three selected matrix elements

Write the channel output in the source basis as

$$
\rho_{AB}
=\frac12
\begin{pmatrix}
A&X\\
X^\dagger&B
\end{pmatrix},
$$

where

$$
A=\Phi(|a\rangle\langle a|),
$$

$$
B=\Phi(|-a\rangle\langle-a|),
$$

$$
X=\Phi(|a\rangle\langle-a|).
$$

After partial transpose on the source qubit,

$$
\rho_{AB}^{T_A}
=\frac12
\begin{pmatrix}
A&X^\dagger\\
X&B
\end{pmatrix}.
$$

Choose the orthonormal two-vector subspace

$$
|0\rangle_A|0\rangle_B,
\qquad
|1\rangle_A|v\rangle_B.
$$

The vectors are orthogonal because of the source-qubit labels even though the bosonic states need not be orthogonal.

Define

$$
\boxed{
p_0
=\langle0,0|\rho_{AB}|0,0\rangle,
}
$$

$$
\boxed{
p_v
=\langle1,v|\rho_{AB}|1,v\rangle,
}
$$

and

$$
\boxed{
z_v
=\langle1,0|\rho_{AB}|0,v\rangle.
}
$$

The compressed partial-transpose block is

$$
\boxed{
M_\Gamma(v)
=
\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v\end{pmatrix}.
}
$$

Therefore

$$
\boxed{
\det M_\Gamma(v)<0
\iff
|z_v|^2>p_0p_v
}
$$

is a rigorous finite-dimensional NPT certificate.

---

## 4. Exact channel matrix elements

The coherent-dyad kernel is

$$
\langle u|\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)|v\rangle
=
\frac{\langle\beta|\alpha\rangle\langle u|v\rangle}{m+1}
\exp\left[
\frac{(\sqrt\tau\beta^*-u^*)(v-\sqrt\tau\alpha)}{m+1}
\right].
$$

For real $a,v$,

$$
\boxed{
\langle0|A|0\rangle
=\frac1{m+1}
\exp\left[-\frac{\tau a^2}{m+1}\right],
}
$$

$$
\boxed{
\langle v|B|v\rangle
=\frac1{m+1}
\exp\left[-\frac{(v+\sqrt\tau a)^2}{m+1}\right],
}
$$

and

$$
\boxed{
|\langle v|X|0\rangle|^2
=\frac1{(m+1)^2}
\exp\left[
-4a^2-v^2+
\frac{2\tau a^2+2\sqrt\tau av}{m+1}
\right].
}
$$

The common source factor $1/2$ cancels from the ratio

$$
R(v)
\equiv
\frac{|z_v|^2}{p_0p_v}.
$$

Thus

$$
\boxed{
\ln R(v)
=-4a^2-v^2
+\frac{4\tau a^2+4\sqrt\tau av+v^2}{m+1}.
}
$$

---

## 5. Exact matched coherent analysis state

For

$$
m>0,
$$

$$
\frac{d}{dv}\ln R
=-2v+\frac{4\sqrt\tau a+2v}{m+1}.
$$

Hence the unique global maximum is

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m}.
}
$$

The strict concavity is

$$
\frac{d^2}{dv^2}\ln R
=-\frac{2m}{m+1}<0.
$$

Substitution gives the central closed-form identity

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

Therefore

$$
\boxed{
|z_{v_*}|^2>p_0p_{v_*}
\iff
\tau>m.
}
$$

Since $m\ge\tau$ is exactly the EB region,

$$
\boxed{
\text{selected }2\times2\text{ PT minor negative}
\iff
\text{actual output NPT}
\iff
\text{channel non-EB}
}
$$

for every finite $a>0$.

The nontrivial part of the possible contribution is therefore **not** the survival boundary itself, but its compression into this one exact finite block.

---

## 6. Pure-loss edge

The optimizer

$$
v_*=2\sqrt\tau a/m
$$

diverges as $m\to0^+$, so pure loss must be treated directly rather than by taking that optimizer to a limit.

At

$$
m=0,
$$

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

any finite

$$
\boxed{
v>\frac{a(1-\tau)}{\sqrt\tau}
}
$$

gives

$$
R(v)>1.
$$

Thus no infinite coherent analysis state is required to certify NPT at pure loss.

---

## 7. Unequal branch weights

For

$$
|\Psi\rangle
=\sqrt p|0\rangle|a\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|-a\rangle,
$$

with

$$
0<p<1,
$$

the diagonal product acquires

$$
p(1-p)
$$

and the squared coherence acquires the same factor. Therefore

$$
R(v)
$$

is unchanged.

The relative phase changes only the complex phase of $z_v$, not its magnitude.

Thus the same exact sign criterion holds for every nonzero branch weight.

---

## 8. Measurement interpretation and limitation

### $p_0$

Joint population for source state $|0\rangle$ and receiver vacuum.

### $p_v$

Joint population for source state $|1\rangle$ and receiver coherent state $|v\rangle$. Operationally, a coherent-state projection can be converted to a vacuum projection after displacement by $-v$.

### $z_v$

Joint coherence between

$$
|1\rangle|0\rangle
\quad\text{and}\quad
|0\rangle|v\rangle.
$$

This term contains the channel off-diagonal dyad

$$
\Phi(|a\rangle\langle-a|).
$$

Therefore this exact witness is **not automatically a two-conditional-output prepare-and-measure benchmark**. Direct implementation requires coherent source-replacement access, process-coherent control, or an equivalent measurement capable of recovering that joint coherence.

The safe claim is mathematical/operational:

> selected joint state/process matrix elements replace full infinite-dimensional tomography.

Do not claim that only two independently prepared coherent test states and ordinary output measurements suffice unless a separate protocol is derived.

---

## 9. Relation to prior art

### Filippov–Ziman (2014)

Their weighted coherent-state swap witness already implies the broad finite-coherent-pair survival theorem in a one-sided specialization. The present candidate distinction is that the same boundary is exposed by one literal $2\times2$ PT principal minor with a closed-form matched analysis state.

This distinction must be tested aggressively. If their weighted witness can be reduced immediately to this block, novelty collapses to proof simplification.

### Rigas / Häseler / Namiki / Killoran / Kreis–van Loock

Earlier effective-entanglement and hybrid-state papers already use

- binary coherent source-replacement states;
- PPT/NPT logic;
- negativity;
- displaced coherent/vacuum projections;
- thermal beam-splitter channels;
- finite subspace or moment witnesses.

The candidate is only the **exact three-element full-boundary compression**, not those ingredients.

---

## 10. Exact selected-block negativity lower bound

The smaller eigenvalue of

$$
M_\Gamma(v)
$$

is

$$
\mu_-(v)
=\frac12
\left[
 p_0+p_v
-
\sqrt{(p_0-p_v)^2+4|z_v|^2}
\right].
$$

Therefore

$$
\boxed{
\mathcal N(\rho)
\ge
G(v)
\equiv
\frac12
\max\left\{0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
}
$$

This converts the sign witness into an absolute finite negativity lower bound.

Detailed optimization is kept separately in

- `ABSOLUTE_THREE_ELEMENT_WITNESS_GAP.md`
- `WEAK_LINK_ABSOLUTE_GAP_ASYMPTOTIC.md`

Those quantitative formulas require their own novelty audit.

---

## 11. Gravity application

For the one-mode Gaussian receiver model, replace

$$
\tau\to\tau_f(t),
\qquad
m\to m(t),
\qquad
2a\to\sqrt{N_\Delta}.
$$

Then

$$
\boxed{
v_*(t)
=\frac{\sqrt{\tau_f(t)N_\Delta}}{m(t)},
}
$$

and

$$
\boxed{
|z_{v_*}(t)|^2>p_0(t)p_{v_*}(t)
\iff
\tau_f(t)>m(t).
}
$$

Thus, within the receiver model, the causal non-EB/NPT front can be represented by a finite joint witness rather than full state tomography.

The novelty of the gravitational source→receiver construction is a separate question from the generic Gaussian-channel survival theorem.

---

## 12. Current research question

The next task is specifically:

> **Has an exact coherent/displaced-vacuum $2\times2$ PT principal minor of this form, or an algebraically equivalent three-matrix-element witness, already been used to reach the full phase-insensitive Gaussian EB boundary?**

Search for

- coherent-state principal minors of partial transpose;
- displaced-vacuum hybrid entanglement witnesses;
- coherent-state process-matrix minors;
- Husimi-Q / off-diagonal coherent-kernel PPT criteria;
- finite truncations or specializations of weighted-swap witnesses;
- exact criteria of the form $|z|^2>p_0p_v$;
- optimized coherent analysis displacements under Gaussian noise.

No originality claim should be made until this search is substantially exhausted.
