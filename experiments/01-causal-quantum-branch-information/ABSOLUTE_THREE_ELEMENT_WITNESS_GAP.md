# Absolute Three-Element Witness Gap

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Exact absolute certification metric for the same $2\times2$ principal-minor witness. This corrects the practical weakness of using only the normalized ratio $\Lambda=\ln(|z|^2/p_0p_v)$.

## 1. Problem with the normalized ratio

For the binary coherent Gaussian-channel theorem, the ratio

$$
\frac{|z_v|^2}{p_0p_v}
$$

is ideal for locating the NPT boundary because

$$
|z_v|^2>p_0p_v
$$

is exactly the condition that the selected $2\times2$ partial-transpose principal minor is negative.

However the normalized logarithmic margin

$$
\Lambda(v)
=\ln\frac{|z_v|^2}{p_0p_v}
$$

can be misleading as an experimental-strength metric.

In weak-transmission limits, the ratio-optimal coherent analysis state can move far into phase space. Then

$$
p_v,\ |z_v|
$$

can become exponentially small even while $\Lambda$ remains finite or large.

Thus $\Lambda$ measures **relative violation**, not absolute observable strength.

---

## 2. Exact $2\times2$ compression

For the source/bosonic output state $\rho$, choose the orthonormal states

$$
|e_0\rangle=|0\rangle_A|0\rangle_B,
$$

$$
|e_v\rangle=|1\rangle_A|v\rangle_B.
$$

They are orthogonal because the source-qubit factors are orthogonal.

Compress the source partial transpose to their span:

$$
\boxed{
M_v
=\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix},
}
$$

where

$$
p_0=\langle0,0|\rho|0,0\rangle,
$$

$$
p_v=\langle1,v|\rho|1,v\rangle,
$$

and

$$
z_v=\langle1,0|\rho|0,v\rangle.
$$

The two eigenvalues are

$$
\lambda_\pm(v)
=\frac{p_0+p_v
\pm
\sqrt{(p_0-p_v)^2+4|z_v|^2}}
2.
$$

Therefore

$$
\boxed{
\lambda_-(v)<0
\iff
|z_v|^2>p_0p_v.
}
$$

---

## 3. Absolute witness gap

Define

$$
\boxed{
G(v)
\equiv
\max\{0,-\lambda_-(v)\}.
}
$$

Explicitly,

$$
\boxed{
G(v)
=
\frac12
\max\left\{
0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
}
$$

This has the desired properties:

1. $G(v)$ has the same absolute scale as probabilities/density-matrix elements;
2. $G(v)=0$ at and below the selected witness boundary;
3. $G(v)\to0$ when all relevant measurable matrix elements vanish;
4. no normalization by exponentially tiny populations is required.

---

## 4. Rigorous lower bound on full negativity

Let

$$
\rho^{\Gamma_A}
$$

be the full partial transpose.

The smallest eigenvalue of a Hermitian operator is no greater than the smallest eigenvalue of any orthogonal compression:

$$
\lambda_{\min}(\rho^{\Gamma_A})
\le
\lambda_-(M_v).
$$

The full negativity is

$$
\mathcal N(\rho)
=\sum_{\lambda_i<0}|\lambda_i|.
$$

Hence, whenever $\lambda_-(M_v)<0$,

$$
\boxed{
\mathcal N(\rho)
\ge
G(v).
}
$$

Therefore $G(v)$ is not merely a witness score; it is a rigorous **lower bound on the actual source-receiver negativity**.

---

## 5. Exact matrix elements for the symmetric binary coherent probe

Take

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle
+|1\rangle|-a\rangle}{\sqrt2},
$$

with real $a>0$, and send the bosonic mode through $\Phi_{\tau,m}$.

For real coherent analysis amplitude $v$,

$$
\boxed{
p_0
=\frac1{2(m+1)}
\exp\left[-\frac{\tau a^2}{m+1}\right],
}
$$

$$
\boxed{
p_v
=\frac1{2(m+1)}
\exp\left[-\frac{(v+\sqrt\tau a)^2}{m+1}\right],
}
$$

and

$$
\boxed{
|z_v|^2
=\frac1{4(m+1)^2}
\exp\left[
-4a^2-v^2
+\frac{2\tau a^2+2\sqrt\tau av}{m+1}
\right].
}
$$

These expressions make $G(v)$ completely explicit.

---

## 6. Ratio-optimal and gap-optimal analysis states are different

The ratio

$$
R(v)=\frac{|z_v|^2}{p_0p_v}
$$

is maximized, for $m>0$, by

$$
\boxed{
v_{\rm ratio}
=\frac{2\sqrt\tau a}{m}.
}
$$

This choice is ideal for proving the exact sign theorem because

$$
R(v_{\rm ratio})
=\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
$$

But it need not maximize $G(v)$.

Indeed, when $m$ and $\tau$ are both small while their ratio is held fixed,

$$
v_{\rm ratio}\propto m^{-1/2}
$$

can become very large, driving the absolute event probabilities toward zero.

For practical certification define instead

$$
\boxed{
G_{\rm abs}(\tau,m,a)
\equiv
\sup_{v\in\mathbb R}G(v).
}
$$

This is a one-dimensional optimization over an explicit smooth function.

---

## 7. Exact boundary survives absolute optimization

For a non-EB channel,

$$
\tau>m,
$$

the direct binary coherent proof guarantees the existence of at least one finite $v$ with

$$
|z_v|^2>p_0p_v.
$$

Therefore

$$
G_{\rm abs}>0.
$$

If

$$
m\ge\tau,
$$

the channel is entanglement breaking, so the complete state is separable and every partial-transpose principal minor is positive semidefinite. Hence

$$
G(v)=0
$$

for all $v$.

Thus

$$
\boxed{
G_{\rm abs}>0
\iff
\tau>m.
}
$$

So the absolute metric retains the exact channel boundary while avoiding the normalized-margin pathology.

---

## 8. Practical finite-certification threshold

Choose an absolute experimental threshold

$$
\boxed{
G_{\rm abs}(t,R)
\ge G_{\rm req}>0.
}
$$

This defines an **absolute certification window** inside the mathematical non-EB window.

For a specified source waveform,

$$
\tau=\tau_f(t,R),
$$

$$
m=m(t),
$$

so

$$
\boxed{
G_{\rm abs}(t,R)
=
\sup_v
G[v;\tau_f(t,R),m(t),a].
}
$$

The certification boundaries are the solutions of

$$
\boxed{
G_{\rm abs}(t,R)=G_{\rm req}.
}
$$

Unlike the normalized $\Lambda$ threshold, this requirement necessarily disappears when the actual received quantum state becomes too weak to produce finite negative weight.

---

## 9. Relation to exact full negativity

The preferred hierarchy is now:

### Exact full negativity available

Use

$$
\mathcal N(\rho).
$$

### Full negativity unavailable but binary Gaussian model valid

Use

$$
G_{\rm abs}
$$

as a rigorous three-element lower bound.

### Only sign/boundary needed

Use the analytically optimized ratio

$$
R(v_{\rm ratio})>1.
$$

This separates mathematical capability from practical certification cleanly.

---

## 10. Pure-loss limit

For an ideal pure-loss channel, the exact source-receiver negativity is already available in `VACUUM_PASSIVE_ENTANGLEMENT_CEILING.md` and should be preferred over the principal-minor lower bound.

For source coherent-state distance $N_\Delta$ and storage fraction $\eta$,

$$
\mathcal N
=\frac14
\left[
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
\right],
$$

with

$$
s_B=e^{-\eta N_\Delta/2},
\qquad
s_E=e^{-(1-\eta)N_\Delta/2}.
$$

For weak capture, source optimization gives

$$
\mathcal N_{\max}
=\eta-2\eta^{3/2}+O(\eta^2).
$$

This is the cleanest absolute vacuum metric.

---

## 11. Consequence for Experiment 01

The receiver theory should now distinguish three levels:

1. **channel capability**
   $$
   \tau_f>m;
   $$
2. **state-level mathematical witness**
   $$
   R(v)>1;
   $$
3. **finite observable quantum weight**
   $$
   G_{\rm abs}\ge G_{\rm req}
   \quad\text{or}\quad
   \mathcal N\ge\mathcal N_{\rm req}.
   $$

This removes the artificial implication that a finite normalized witness ratio necessarily corresponds to an experimentally significant quantum signal.

---

## 12. Strongest next step

For the fixed exponential source in `EXPONENTIAL_SOURCE_QUANTUM_WINDOW.md`, evaluate

$$
G_{\rm abs}(x,r,a)
$$

throughout the EB $\to$ non-EB $\to$ EB window and optimize over both

- coherent analysis amplitude $v$;
- source branch separation $a$.

This will give the first physically meaningful **finite-certification bubble** in spacetime.