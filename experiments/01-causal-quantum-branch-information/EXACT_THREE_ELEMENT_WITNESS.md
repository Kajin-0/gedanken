# Exact Three-Element Finite-Cat Thermal Witness

**Timestamp:** 2026-08-07 17:02 EDT  
**Status:** Analytic consequence of the exact finite-cat theorem; independently checked numerically.

## 1. Goal

The exact rank-one witness in `EXACT_FINITE_CAT_WITNESS.md` detects the entire non-entanglement-breaking region for the hybrid source cat

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle+|1\rangle|-a\rangle}{\sqrt2}
$$

sent through a thermal attenuator.

The same negativity can be exposed by a single $2\times2$ principal minor of the partial transpose. This reduces the certification problem to **two populations and one coherence**.

---

## 2. Channel parameters

Let

$$
m=(1-\eta)\bar n>0,
$$

$$
r=\frac{m}{m+1},
$$

$$
s=\frac{\sqrt\eta\,a}{m+1}.
$$

Choose the receiver coherent test amplitude

$$
\boxed{
v_*=\frac{2s}{r}
=\frac{2\sqrt\eta\,a}{m}.
}
$$

This is the same coherent amplitude that appears in the explicit negative vector of the full theorem.

---

## 3. Relevant matrix elements

Write the thermal-channel output in the source basis as

$$
\rho_{AB}
=\frac12
\begin{pmatrix}
\rho_+&X\\
X^\dagger&\rho_-
\end{pmatrix}.
$$

Consider the two-dimensional subspace of the partially transposed state spanned by

$$
|0\rangle_A|0\rangle_B,
\qquad
|1\rangle_A|v_*\rangle_B.
$$

Define the directly observable quantities

$$
\boxed{
p_0
=\langle0,0|\rho_{AB}|0,0\rangle,
}
$$

$$
\boxed{
p_v
=\langle1,v_*|\rho_{AB}|1,v_*\rangle,
}
$$

and

$$
\boxed{
z_v
=\langle1,0|\rho_{AB}|0,v_*\rangle.
}
$$

Partial transpose converts the off-diagonal entry of this principal block into $z_v$.

The principal block is therefore

$$
M_\Gamma
=
\begin{pmatrix}
p_0&z_v^*\\z_v&p_v\end{pmatrix}.
$$

Every separable state must satisfy

$$
\det M_\Gamma\ge0,
$$

so

$$
\boxed{|z_v|^2>p_0p_v}
$$

is an NPT entanglement witness.

---

## 4. Exact evaluation for the finite thermal cat

Using the normal-ordered thermal-channel blocks,

$$
p_0=\frac P2,
$$

$$
p_v
=\frac P2
\exp[-2sv_*-v_*^2(1-r)],
$$

and

$$
|z_v|
=\frac C2
\exp[-v_*^2/2+s v_*],
$$

where

$$
P=\frac1{m+1}
\exp[-\eta a^2/(m+1)],
$$

and

$$
C=\frac1{m+1}
\exp[-2a^2+\eta a^2/(m+1)].
$$

At the optimized coherent test amplitude

$$
v_*=2s/r,
$$

the ratio simplifies exactly to

$$
\boxed{
\frac{|z_v|^2}{p_0p_v}
=q^2,
}
$$

where

$$
\boxed{
q
=\exp\left[
\frac{2a^2}{m}(\eta-m)
\right].
}
$$

Hence

$$
\boxed{
\det M_\Gamma
=p_0p_v(1-q^2).
}
$$

Therefore

$$
\boxed{
|z_v|^2>p_0p_v
\iff
q>1
\iff
\eta>m
\iff
\eta>\frac{\bar n}{\bar n+1}.
}
$$

This is the exact NPT boundary for every finite $a\neq0$.

---

## 5. Why this is stronger than the earlier moment witness

Kreis & van Loock (2012) study the same hybrid state and one-sided thermal beam-splitter channel. Their finite-order Shchukin–Vogel determinant provides a sufficient entanglement region whose boundary depends on $|\alpha|$ and which they explicitly note may fail to detect entangled states throughout part of the non-entanglement-breaking region.

The present principal-minor test is channel/state matched. It satisfies

$$
\boxed{
\text{witness negative}
\iff
\text{state NPT}
\iff
\text{thermal channel non-EB}
}
$$

for every finite coherent branch amplitude.

Thus the theorem does not merely establish hidden entanglement abstractly; it supplies a concrete three-element witness that exposes it.

---

## 6. Measurement interpretation

The three required quantities have a simple operational meaning.

### $p_0$

Probability that the source is found in branch basis state $|0\rangle$ and the receiver in vacuum.

### $p_v$

Probability that the source is found in $|1\rangle$ and the receiver in coherent state $|v_*\rangle$. Operationally this can be reduced to a vacuum projection after displacement by $-v_*$.

### $z_v$

A joint source-receiver coherence between

$$
|1\rangle|0\rangle
\quad\text{and}\quad
|0\rangle|v_*\rangle.
$$

Its real and imaginary parts can in principle be accessed by source-basis interferometry combined with receiver displacement/vacuum projection or an equivalent controlled-erasure measurement.

Thus the exact criterion requires selected joint matrix elements rather than full infinite-dimensional state tomography.

---

## 7. Gravity version

At receiver time $t$, replace

$$
\eta\rightarrow\eta_f(t),
\qquad
m\rightarrow m(t),
\qquad
a\rightarrow\sqrt{N_\Delta}/2.
$$

The optimized receiver test amplitude becomes

$$
\boxed{
v_*(t)
=\frac{\sqrt{\eta_f(t)N_\Delta}}{m(t)}.
}
$$

Then

$$
\boxed{
|z_v(t)|^2>p_0(t)p_v(t)
\iff
\eta_f(t)>m(t).
}
$$

Therefore the exact causal NPT front can, within the ideal model, be certified by a three-element joint witness rather than complete tomography.

For a stationary receiver the earliest possible sign change is still bounded by

$$
T_{\rm NPT}^{\min}
=\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right].
$$

---

## 8. Numerical audit

The determinant formula and the equivalent rank-one witness were independently checked using a direct truncated Fock-space beam-splitter dilation with an explicit thermal environmental mode.

Above the predicted boundary the principal determinant is negative; below it the analytic determinant is positive. Small below-threshold negative eigenvalues seen at insufficient Fock cutoffs converge away, consistent with the exact entanglement-breaking property.

---

## 9. Limitations

- The optimized coherent test amplitude diverges as $m\to0$, so the thermal witness is not the convenient representation of the pure-loss limit. Vacuum loss should be treated separately.
- The witness assumes accurate knowledge of $a$, $\eta$, and $m$ or their gravitational receiver equivalents.
- It is mathematically low-dimensional but may still be experimentally demanding because $|v_*\rangle$ can be a large displacement.
- The exact iff property is specific to the finite binary coherent-cat family and phase-insensitive thermal attenuator considered here.

## 10. Next step

Search for an existing exact principal-minor/hybrid witness of this form. If none is found, this is a more operational candidate contribution than the bare NPT theorem alone.
