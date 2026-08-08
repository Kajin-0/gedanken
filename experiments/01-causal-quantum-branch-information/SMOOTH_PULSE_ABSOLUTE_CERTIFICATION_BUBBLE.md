# Smooth-Pulse Absolute Certification Bubble

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Leading weak-link finite-certification result obtained by combining the smooth fixed source pulse with the optimized absolute three-element witness gap.

## 1. Source-specific channel variables

For the smooth normalized source pulse

$$
f_T(t)
=\sqrt{\frac8{3T}}
\sin^2\left(\frac{\pi t}{T}\right),
\qquad
0<t<T,
$$

define

$$
x=t/T,
$$

$$
q=\kappa T,
$$

and

$$
y=\min(x,1).
$$

Let

$$
J_q(y)
=\int_0^y dz\,
e^{qz/2}\sin^2(\pi z).
$$

Define two dimensionless response functions

$$
\boxed{
S_q(x)
=\frac{8q}{3}
e^{-qx}J_q^2(y),
}
$$

and

$$
\boxed{
N_q(x)
=1-e^{-qx}.
}
$$

Then for an initially ground-state receiver,

$$
\boxed{
\tau(t,R)
=\frac{\kappa_\Delta(R)}{\kappa}
S_q(x),
}
$$

and

$$
\boxed{
m(t)
=\frac{\Gamma_{\rm th}}{\kappa}
N_q(x).
}
$$

---

## 2. Weak-link absolute witness gap

In the gravitational weak-link regime

$$
\tau,m\ll1,
$$

the optimized absolute three-element witness obeys

$$
G_{\rm abs}^{\rm opt}
= c_0[\tau-m]_+
+O(\tau^2),
$$

where

$$
\boxed{
c_0
=\frac12W(e^{-1})
\simeq0.1392322714.
}
$$

Therefore

$$
\boxed{
G_{\rm abs}^{\rm opt}(x,R)
\simeq
\frac{c_0}{\kappa}
\left[
\kappa_\Delta(R)S_q(x)
-\Gamma_{\rm th}N_q(x)
\right]_+.
}
$$

This is the leading absolute quantum-weight profile of the source-specific receiver bubble.

---

## 3. Finite experimental requirement

Choose an absolute certification requirement

$$
\boxed{
G_{\rm abs}^{\rm opt}
\ge G_{\rm req}>0.
}
$$

To leading order, this is equivalent to

$$
\boxed{
\kappa_\Delta(R)S_q(x)
-\Gamma_{\rm th}N_q(x)
\ge
\frac{\kappa G_{\rm req}}{c_0}.
}
$$

Unlike the normalized ratio criterion, this cannot be satisfied by vanishingly small received probabilities.

---

## 4. Insert the gravitational range dependence

For the aligned wave-zone source/receiver geometry,

$$
\boxed{
\kappa_\Delta(R)
=\frac{K_G}{R^2},
}
$$

where

$$
\boxed{
K_G
=\frac{25\mathcal O}{16k^2}\kappa_g.
}
$$

The finite-certification inequality becomes

$$
\frac{K_G}{R^2}S_q(x)
\ge
\Gamma_{\rm th}N_q(x)
+
\frac{\kappa G_{\rm req}}{c_0}.
$$

Hence, for every local pulse time $x$, certification is possible only inside

$$
\boxed{
R^2
\le
R_G^2(x;q,G_{\rm req}),
}
$$

where

$$
\boxed{
R_G^2(x;q,G_{\rm req})
=\frac{
K_GS_q(x)
}{
\Gamma_{\rm th}N_q(x)
+
\kappa G_{\rm req}/c_0
}.
}
$$

This is the absolute **finite-certification radius at time $x$**.

---

## 5. Maximum absolute certification range

The largest distance at which the chosen smooth pulse can ever produce the required witness strength is

$$
\boxed{
R_{G,\max}(q,G_{\rm req})
=
\max_{x>0}
\sqrt{
\frac{K_GS_q(x)}
{\Gamma_{\rm th}N_q(x)+\kappa G_{\rm req}/c_0}
}.
}
$$

This formula is one of the cleanest current physical predictions in Experiment 01.

It contains

- source temporal shape through $S_q$;
- receiver thermalization through $N_q$;
- wave-zone gravitational propagation through $K_G/R^2$;
- receiver linewidth through $q$ and $\kappa$;
- finite experimental requirement through $G_{\rm req}$.

---

## 6. Bare quantum-capability limit recovered

Set

$$
G_{\rm req}=0.
$$

Then

$$
R_{G,\max}^2
=\frac{K_G}{\Gamma_{\rm th}}
\max_x\frac{S_q(x)}{N_q(x)}.
$$

But

$$
\frac{S_q(x)}{N_q(x)}
=H_q(x),
$$

so

$$
\boxed{
R_{G,\max}(q,0)
=\sqrt{
\frac{K_G}{\Gamma_{\rm th}}
H_{\max}(q)
}.
}
$$

This reproduces the smooth-pulse EB/non-EB maximum range derived independently in `SMOOTH_SIN2_SOURCE_QUANTUM_WINDOW.md`.

Thus the absolute theory reduces continuously to the mathematical capability boundary when the required negative weight tends to zero.

---

## 7. Vacuum finite-certification range

Now set

$$
\Gamma_{\rm th}=0.
$$

The mathematical pure-loss channel is non-EB at every nonzero range-coupling, so the bare EB criterion alone has no finite range.

But the absolute certification radius remains finite:

$$
\boxed{
R_{G,\max}^{\rm vac}
=\sqrt{
\frac{c_0K_G}
{\kappa G_{\rm req}}
\max_x S_q(x)
}.
}
$$

This is a major conceptual advantage of the absolute metric:

> **even in perfect vacuum, a finite measurable entanglement certificate has a finite source-to-receiver range because the coherent gravitational signal decays as $R^{-2}$ in probability.**

No thermal classicalization is required to obtain a finite practical range.

---

## 8. Optimal smooth-pulse bandwidth in vacuum

For the $\sin^2$ pulse family, numerical optimization of

$$
S_{\max}(q)
=\max_xS_q(x)
$$

gives

$$
\boxed{
q_{\rm vac,opt}
=\kappa T
\simeq4.75603,
}
$$

with the peak at

$$
\boxed{
x_{\rm vac,opt}
\simeq0.719445,
}
$$

and

$$
\boxed{
S_*
=\max_{q,x}S_q(x)
\simeq0.795073.
}
$$

Thus the best vacuum finite-certification radius within this pulse family is

$$
\boxed{
R_{G,\max}^{\rm vac,opt}
\simeq
\sqrt{
\frac{0.795073\,c_0K_G}
{\kappa G_{\rm req}}
}.
}
$$

Since

$$
c_0\simeq0.139232,
$$

the product is

$$
0.795073c_0
\simeq0.11067.
$$

Therefore

$$
\boxed{
R_{G,\max}^{\rm vac,opt}
\simeq
0.3327
\sqrt{
\frac{K_G}
{\kappa G_{\rm req}}
}.
}
$$

This is a lower-bound certification range based on the minimal three-element witness, not the exact full-negativity range.

---

## 9. Thermal and finite-strength penalties are fundamentally different

The denominator

$$
\Gamma_{\rm th}N_q(x)
+
\kappa G_{\rm req}/c_0
$$

contains two qualitatively different costs.

### Thermal classicalization

$$
\Gamma_{\rm th}N_q(x)
$$

grows dynamically with receiver exposure time.

### Required observable quantum weight

$$
\kappa G_{\rm req}/c_0
$$

is an absolute finite-strength floor even in vacuum.

Therefore the certification bubble can disappear because

1. the environment records the branch too strongly;
2. the received branch amplitude is simply too small to produce enough negative partial-transpose weight;
3. or both.

---

## 10. Spacetime certification bubble

For a fixed distance $R$, define the required dimensionless level

$$
\mathcal L_R(x)
=
\frac{R^2}{K_G}
\left[
\Gamma_{\rm th}N_q(x)
+
\frac{\kappa G_{\rm req}}{c_0}
\right].
$$

The finite certificate exists at local pulse time $x$ iff

$$
\boxed{
S_q(x)\ge\mathcal L_R(x).
}
$$

When two roots exist,

$$
x_G^-(R)<x_G^+(R),
$$

the laboratory-time certification window is

$$
\boxed{
\frac Rc+Tx_G^-(R)
< T_{\rm lab}
<
\frac Rc+Tx_G^+(R).
}
$$

This finite-strength bubble lies strictly inside the bare EB/non-EB bubble.

---

## 11. Relation to source cat strength

The weak-link optimization that produced

$$
G_{\rm abs}^{\rm opt}
\simeq c_0(\tau-m)
$$

also fixes the leading optimal source branch amplitude:

$$
\boxed{
a_*
\simeq0.565346\sqrt\tau.
}
$$

Thus the source cat used to optimize the minimal absolute witness becomes **smaller**, not larger, as the gravitational link weakens.

This reflects a basic information-flow tradeoff: a large cat makes the uncollected gravitational field an increasingly strong which-branch record.

---

## 12. What this result does not claim

- $G_{\rm abs}$ is a rigorous lower bound, not necessarily the full negativity.
- The smooth $\sin^2$ pulse is a benchmark source family, not a unique physical source.
- $K_G$ uses the current aligned wave-zone storage normalization and stated overlap model.
- The weak-link expansion assumes $\tau,m\ll1$.

For ordinary gravitational reception these assumptions are expected to be highly conservative because the transfer probabilities are extraordinarily small.

---

## 13. Strongest next step

The project now has both

1. a source-specific mathematical quantum-capability bubble;
2. an absolute finite-certification bubble.

The strongest remaining physics step is to replace the abstract narrowband quadrupole envelope by an explicit **conserved mechanical source model** whose branch trajectories generate the chosen smooth quadrupole history, and verify the emitted TT wavepacket normalization directly.