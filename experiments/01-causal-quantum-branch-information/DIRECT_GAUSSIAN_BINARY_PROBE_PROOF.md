# Direct Finite-Minor Proof of the Binary Coherent Gaussian-Channel Theorem

**Timestamp:** 2026-08-07 18:12 EDT  
**Status:** Independent analytic audit of `PHASE_INSENSITIVE_GAUSSIAN_BINARY_PROBE_THEOREM.md`. This proof avoids thermal attenuator dilation, Fock truncation, and unbounded inverse congruences.

## 1. Channel convention

Use the one-mode gauge-covariant phase-insensitive Gaussian channel

$$
\boxed{
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\,\xi)
\exp\left[-\frac{2m+1-\tau}{2}|\xi|^2\right].
}
$$

Here

- $\tau\ge0$ is intensity transmission/gain;
- $m\ge0$ is vacuum-output thermal occupation.

The channel is entanglement breaking iff

$$
\boxed{m\ge\tau.}
$$

We independently prove that a finite binary coherent hybrid output is NPT whenever

$$
\tau>m.
$$

---

## 2. Coherent dyad characteristic function

For an arbitrary coherent dyad

$$
|\alpha\rangle\langle\beta|,
$$

the symmetrically ordered characteristic function is

$$
\boxed{
\chi_{\alpha\beta}(\xi)
=
\langle\beta|\alpha\rangle
\exp\left[
-\frac{|\xi|^2}{2}
+\beta^*\xi
-\alpha\xi^*
\right].
}
$$

After the channel,

$$
\boxed{
\chi_{\rm out}(\xi)
=
\langle\beta|\alpha\rangle
\exp\left[
-\frac{2m+1}{2}|\xi|^2
+\sqrt\tau\,\beta^*\xi
-\sqrt\tau\,\alpha\xi^*
\right].
}
$$

The channel dependence enters only through $\tau$ and $m$.

---

## 3. Exact coherent-state matrix element

Use Weyl reconstruction

$$
O
=\int\frac{d^2\xi}{\pi}
\chi_O(\xi)D(-\xi)
$$

with the convention used above.

The coherent-state displacement matrix element is

$$
\langle u|D(-\xi)|v\rangle
=
\langle u|v\rangle
\exp\left[
-\frac{|\xi|^2}{2}
-u^*\xi
+v\xi^*
\right].
$$

Therefore

$$
\langle u|
\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)
|v\rangle
$$

is a two-dimensional Gaussian integral. Using

$$
\int\frac{d^2\xi}{\pi}
\exp(-A|\xi|^2+B\xi+C\xi^*)
=\frac1A\exp(BC/A)
$$

for $\operatorname{Re}A>0$, with

$$
A=m+1,
$$

gives the exact identity

$$
\boxed{
\langle u|
\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)
|v\rangle
=
\frac{\langle\beta|\alpha\rangle
\langle u|v\rangle}
{m+1}
\exp\left[
\frac{(\sqrt\tau\,\beta^*-u^*)
(v-\sqrt\tau\,\alpha)}
{m+1}
\right].
}
$$

This formula is valid for attenuation, amplification, and additive phase-insensitive Gaussian noise in the stated channel convention.

It is the key independent audit result.

---

## 4. Symmetric binary coherent hybrid state

By displacement and phase covariance, any distinct finite coherent pair can be reduced by local unitaries to

$$
|+a\rangle,
\qquad
|-a\rangle,
$$

with

$$
a>0.
$$

Take the balanced source state

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle
+|1\rangle|-a\rangle}{\sqrt2}.
$$

Define output bosonic blocks

$$
A=\Phi(|a\rangle\langle a|),
$$

$$
B=\Phi(|-a\rangle\langle-a|),
$$

$$
X=\Phi(|a\rangle\langle-a|).
$$

Then

$$
\rho_{AB}
=\frac12
\begin{pmatrix}
A&X\\
X^\dagger&B
\end{pmatrix}.
$$

After partial transpose on the source qubit,

$$
\rho_{AB}^{\Gamma_A}
=\frac12
\begin{pmatrix}
A&X^\dagger\\
X&B
\end{pmatrix}.
$$

---

## 5. One explicit $2\times2$ principal minor

Consider the two-dimensional subspace spanned by

$$
|0\rangle_A|0\rangle_B
$$

and

$$
|1\rangle_A|v\rangle_B,
$$

where $|v\rangle$ is a coherent state to be optimized.

Define

$$
p_0
=\langle0,0|\rho|0,0\rangle
=\frac12\langle0|A|0\rangle,
$$

$$
p_v
=\langle1,v|\rho|1,v\rangle
=\frac12\langle v|B|v\rangle,
$$

and

$$
z_v
=\langle1,0|\rho|0,v\rangle.
$$

The corresponding principal minor of $\rho^{\Gamma_A}$ is negative iff

$$
\boxed{|z_v|^2>p_0p_v.}
$$

Because every positive semidefinite operator has nonnegative principal minors, this is a rigorous finite-dimensional NPT certificate.

---

## 6. Exact diagonal terms

Using the matrix-element identity,

$$
\boxed{
\langle0|A|0\rangle
=
\frac1{m+1}
\exp\left[-\frac{\tau a^2}{m+1}\right].
}
$$

For real $v$,

$$
\boxed{
\langle v|B|v\rangle
=
\frac1{m+1}
\exp\left[-\frac{(v+\sqrt\tau a)^2}{m+1}\right].
}
$$

---

## 7. Exact off-diagonal term

For

$$
X=\Phi(|a\rangle\langle-a|),
$$

$$
\langle-a|a\rangle
=e^{-2a^2}.
$$

The exact matrix element is

$$
\langle v|X|0\rangle
=
\frac{e^{-2a^2}\langle v|0\rangle}
{m+1}
\exp\left[
\frac{\tau a^2+\sqrt\tau av}{m+1}
\right].
$$

Since

$$
|\langle v|0\rangle|^2=e^{-v^2},
$$

$$
\boxed{
|\langle v|X|0\rangle|^2
=
\frac1{(m+1)^2}
\exp\left[
-4a^2-v^2
+\frac{2\tau a^2+2\sqrt\tau av}{m+1}
\right].
}
$$

The factor $1/2$ from the source amplitudes cancels in the principal-minor ratio.

---

## 8. Optimize the exact principal-minor ratio

Define

$$
R(v)
\equiv
\frac{|z_v|^2}{p_0p_v}.
$$

Combining the previous expressions gives

$$
\ln R(v)
=
-4a^2-v^2
+
\frac{4\tau a^2+4\sqrt\tau av+v^2}
{m+1}.
$$

Differentiate:

$$
\frac{d}{dv}\ln R
=-2v+
\frac{4\sqrt\tau a+2v}{m+1}.
$$

The optimum is

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m}.}
$$

Substitution yields

$$
\boxed{
\ln R(v_*)
=
\frac{4a^2}{m}(\tau-m).
}
$$

Therefore

$$
\boxed{
R(v_*)
=
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

Since

$$
N_\Delta=4a^2,
$$

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\exp\left[
\frac{N_\Delta}{m}(\tau-m)
\right].
}
$$

This reproduces the previously derived exact matched witness by an entirely independent route.

---

## 9. Direct NPT proof

If

$$
\tau>m,
$$

then for every

$$
a>0,
$$

$$
R(v_*)>1.
$$

Hence the $2\times2$ principal minor of $\rho^{\Gamma_A}$ is negative and

$$
\boxed{
\rho_{AB}\text{ is NPT}.
}
$$

Conversely, if

$$
m\ge\tau,
$$

the Gaussian channel is entanglement breaking, so every output state is separable.

Therefore

$$
\boxed{
\rho_{AB}\text{ NPT}
\iff
\tau>m.
}
$$

This proof uses only

1. the Gaussian channel characteristic function;
2. one finite coherent-state matrix element;
3. one optimized $2\times2$ principal minor;
4. the established channel EB boundary for the converse.

It does not rely on the detailed thermal attenuator dilation.

---

## 10. Unequal branch weights

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

the principal-minor diagonal terms acquire factors $p$ and $1-p$, while the squared coherence acquires exactly the product $p(1-p)$.

Therefore these factors cancel in

$$
|z_v|^2/(p_0p_v).
$$

The result remains

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

A nonzero source relative phase only changes the phase of $z_v$ and not its magnitude.

Thus the theorem holds for every nonzero branch weight and phase.

---

## 11. Arbitrary coherent pair

For arbitrary distinct finite coherent states $|\alpha\rangle,|\beta\rangle$, use displacement covariance to remove the midpoint

$$
\gamma=(\alpha+\beta)/2
$$

and phase covariance to rotate the separation

$$
\delta=\alpha-\beta
$$

to the real axis.

Then

$$
a=|\delta|/2,
$$

so

$$
4a^2=|\alpha-\beta|^2.
$$

Hence

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\exp\left[
\frac{|\alpha-\beta|^2}{m}(\tau-m)
\right]
}
$$

when the coherent analysis basis has first been displaced/rotated into the symmetric representation.

The exact location $v_*$ transforms back with the inverse local output displacement/rotation.

---

## 12. Special cases

### Thermal attenuator

$$
0\le\tau\le1,
\qquad
m=(1-\tau)\bar n_E.
$$

NPT iff

$$
\tau>(1-\tau)\bar n_E,
$$

or

$$
\boxed{
\tau>\frac{\bar n_E}{\bar n_E+1}.
}
$$

### Thermal amplifier

$$
\tau=G>1,
$$

$$
m=(G-1)(\bar n_E+1).
$$

NPT iff

$$
(G-1)(\bar n_E+1)<G,
$$

or

$$
\boxed{
\bar n_E<\frac1{G-1}.
}
$$

### Additive Gaussian noise

$$
\tau=1.
$$

NPT iff

$$
\boxed{m<1.}
$$

Each is exactly the corresponding channel's non-EB region.

---

## 13. Importance for Experiment 01

This direct proof materially strengthens the mathematical core of the project.

The causal-front theorem relies on the binary branch state detecting the receiver channel's EB boundary exactly. The result is now established by a finite principal-minor calculation that applies directly to the whole phase-insensitive Gaussian family.

Therefore the gravitational binary coherent branches are not merely a plausible probe of receiver nonclassicality. Within the Gaussian receiver model they are an **exact front-faithful probe** with an explicit low-dimensional witness.

---

## 14. Remaining novelty question

The direct proof is simple enough that an equivalent result may exist implicitly in coherent-state channel-testing literature even if it has not been stated in this form.

The novelty search should therefore focus on

- exact coherent-state matrix-element tests of Gaussian EB boundaries;
- two-state effective-entanglement tests beyond moment-based criteria;
- full partial-transpose analyses of hybrid coherent/qubit states under amplifiers and additive-noise channels.

No originality claim should be made until that search is complete.