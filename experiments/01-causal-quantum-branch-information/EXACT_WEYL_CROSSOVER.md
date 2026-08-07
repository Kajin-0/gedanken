# Exact Retarded Quadrupole Tidal Crossover

**Timestamp:** 2026-08-07 14:15 EDT  
**Status:** Linearized-gravity result for one clean source/receiver geometry

This note derives a single gauge-invariant electric-curvature transfer function connecting the static near zone to the gravitational-wave zone. It replaces the earlier practice of stitching separate $R^{-5}$ and $R^{-1}$ curvature asymptotics by hand.

---

## 1. Geometry

Choose a pure plus-type STF mass-quadrupole branch difference

$$
\Delta Q_{xx}(t)=q(t),
\qquad
\Delta Q_{yy}(t)=-q(t),
\qquad
\Delta Q_{zz}=0,
$$

with all off-diagonal components zero.

Place the receiver on the positive $z$ axis at radius $R$ and let its freely falling differential baseline point along $x$.

This geometry is useful because:

- the static quadrupole produces a nonzero transverse tidal field at the receiver;
- the outgoing wave along $z$ is plus-polarized and couples directly to the $x$ differential receiver;
- the same single control $q(t)$ therefore connects the near field continuously to the radiative field.

---

## 2. Canonical linearized quadrupole metric

In harmonic gauge, the canonical linearized mass-quadrupole field can be written in terms of the retarded STF moment $Q_{ij}(u)$, $u=t-R/c$. In the standard canonical-multipole convention, the trace-reversed/gothic field contains

$$
h^{00}_{\rm can}
=-\frac{2G}{c^2}\partial_{ab}
\left(\frac{Q_{ab}(u)}{R}\right),
$$

$$
h^{0i}_{\rm can}
=\frac{2G}{c^3}\partial_a
\left(\frac{\dot Q_{ia}(u)}{R}\right),
$$

$$
h^{ij}_{\rm can}
=-\frac{2G}{c^4R}\ddot Q_{ij}(u).
$$

After the linear trace reversal needed to recover the physical metric perturbation, the gauge-invariant Riemann tensor can be evaluated directly. The result below is independent of the intermediate harmonic-gauge representation.

---

## 3. Exact electric-curvature component

Define the physical tidal tensor

$$
\mathcal E_{ij}=c^2R_{0i0j}.
$$

For the geometry above, direct evaluation gives

$$
\boxed{
\Delta\mathcal E_{xx}(t,R)
=
-\frac{G}{R^5}
\left[
3q
+\frac{3R}{c}\dot q
+\frac{3R^2}{c^2}\ddot q
+\frac{2R^3}{c^3}q^{(3)}
+\frac{R^4}{c^4}q^{(4)}
\right]_{t-R/c}.
}
$$

Overall sign depends on Riemann/potential convention and is irrelevant for the distinguishability calculations. The relative coefficients and radial/time-derivative structure are the key result.

The five pieces have the expected physical hierarchy:

$$
\frac{q}{R^5},
\quad
\frac{\dot q}{cR^4},
\quad
\frac{\ddot q}{c^2R^3},
\quad
\frac{q^{(3)}}{c^3R^2},
\quad
\frac{q^{(4)}}{c^4R}.
$$

They correspond schematically to static near field, induction terms, and radiative curvature.

---

## 4. Frequency-domain transfer polynomial

Use the convention

$$
q(t)=q_\omega e^{-i\omega t}.
$$

Define

$$
\epsilon=\frac{\omega R}{c}.
$$

Then

$$
\boxed{
\Delta\mathcal E_{xx}(\omega,R)
=-\frac{Gq_\omega}{R^5}
P(\epsilon)e^{i\omega R/c},
}
$$

where

$$
\boxed{
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
}
$$

Its squared magnitude is

$$
\boxed{
|P(\epsilon)|^2
=\epsilon^8-2\epsilon^6+3\epsilon^4-9\epsilon^2+9.
}
$$

Consistency checks:

### Static near zone

$$
P(0)=3,
$$

so

$$
\Delta\mathcal E_{xx}
\rightarrow
-\frac{3Gq}{R^5}.
$$

### Wave zone

For $\epsilon\gg1$,

$$
P(\epsilon)\sim\epsilon^4,
$$

so

$$
\Delta\mathcal E_{xx}
\rightarrow
-\frac{G\omega^4q_\omega}{c^4R},
$$

which equals the standard gravitational-wave result

$$
\mathcal E_{xx}^{\rm GW}
=-\frac12\ddot h_{xx}^{TT},
\qquad
h_{xx}^{TT}
=\frac{2G}{c^4R}\ddot q.
$$

Thus the same transfer function contains both the Newtonian tidal limit and radiative curvature.

---

## 5. Differential quantum receiver

For a freely falling differential mode with reduced/effective mass $\mu_B$, equilibrium baseline $L_B$, quantum coordinate $x_B$, and

$$
x_{\rm zpf}=\sqrt{\frac{\hbar}{2\mu_B\omega_B}},
$$

the curvature drive is

$$
H_{\rm drive}
=\mu_BL_B\mathcal E_{xx}x_B.
$$

At the receiver resonance $\omega=\omega_B$, the branch-response coefficient per source quadrupole amplitude is

$$
\boxed{
|\mathcal R_B^{(G)}(\epsilon)|
=
\frac{G\mu_BL_Bx_{\rm zpf}}{\hbar R^5}
|P(\epsilon)|.
}
$$

---

## 6. Matching complementary graviton record

For this source geometry,

$$
Q_{ij}Q_{ij}=2q^2.
$$

The standard quadrupole power formula therefore gives

$$
P_{\rm GW}
=\frac{2G}{5c^5}\left(q^{(3)}\right)^2.
$$

In the coherent-radiation branch-record approximation, define the two-sided positive record spectrum by

$$
2\Gamma_\Xi
=\int\frac{d\omega}{2\pi}
S_G(\omega)|\widetilde q(\omega)|^2.
$$

With the same Fourier convention,

$$
\boxed{
S_G(\omega)
\simeq
\frac{2G}{5\hbar c^5}\omega^5,
}
$$

up to one-sided/two-sided factors of order unity.

This is the clean outgoing-radiation contribution only. A complete treatment of the complementary record must handle soft/dressing sectors and any apparatus/environmental records consistently.

---

## 7. Exact crossover history-transfer rate

Using

$$
\gamma_{\rm hist}^{(G)}
=\frac{|\mathcal R_B^{(G)}|^2}{S_G(\omega_B)},
$$

one obtains

$$
\boxed{
\gamma_{\rm hist}^{(G)}(\epsilon)
=
\frac54
\frac{G\mu_BL_B^2c^5}
{R^{10}\omega_B^6}
|P(\epsilon)|^2
}
$$

within the stated spectral convention.

With receiver amplitude damping $\kappa_B$,

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}(\epsilon)
=
\frac54
\frac{G\mu_BL_B^2c^5}
{\kappa_BR^{10}\omega_B^6}
|P(\epsilon)|^2.
}
$$

Define

$$
Q_B=\frac{\omega_B}{\kappa_B}
$$

and the tiny receiver parameter

$$
\boxed{
\nu_G
=\frac{G\mu_BL_B^2Q_B\omega_B^3}{c^5}.
}
$$

Then the entire near-to-wave crossover is

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}(\epsilon)
=
\frac54\,
u_G\,
\frac{|P(\epsilon)|^2}{\epsilon^{10}}.
}
$$

Equivalently,

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}(\epsilon)
=
\frac54\nu_G
\left(
\epsilon^{-2}
-2\epsilon^{-4}
+3\epsilon^{-6}
-9\epsilon^{-8}
+9\epsilon^{-10}
\right).
}
$$

The polynomial representation is preferable near the crossover because the individual inverse-power terms should not be interpreted separately as positive information channels.

---

## 8. Near- and far-zone limits from one formula

### Deep near zone: $\epsilon\ll1$

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\simeq
\frac{45}{4}\nu_G\epsilon^{-10}.
}
$$

### Wave zone: $\epsilon\gg1$

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\simeq
\frac54\nu_G\epsilon^{-2}.
}
$$

### Crossover: $\epsilon=1$

Since

$$
|P(1)|^2=2,
$$

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}(1)
=\frac52\nu_G.
}
$$

For realistic laboratory receivers, $\nu_G$ is extraordinarily small. Thus a **single local differential receiver** is deeply below the strong-history threshold near the point where retardation becomes dynamically order unity.

---

## 9. Example scale

For two approximately $1\,\mathrm g$ receiver masses described by a relative mode,

$$
\mu_B\approx0.5\,\mathrm g,
$$

with

$$
L_B=0.1\,\mathrm m,
\qquad
f_B=1\,\mathrm{Hz},
\qquad
Q_B=10^8,
$$

one finds

$$
\nu_G\approx3.4\times10^{-48}.
$$

Therefore at $\epsilon=1$,

$$
\mathcal C_{\rm hist}^{(G)}\sim8.5\times10^{-48}.
$$

The radiation-only near-zone threshold $\mathcal C_{\rm hist}=1$ occurs at approximately

$$
\epsilon_c\sim2.3\times10^{-5},
$$

or

$$
R_c\sim1.1\,\mathrm{km}.
$$

At that radius the light-travel delay is only a few microseconds, versus a one-second mechanical period. Again: this is an ideal information-efficiency comparison against clean graviton radiation, not a detectability forecast.

---

## 10. Emerging strong-witness limitation

For this exact linearized geometry, the local strong-history cooperativity is controlled by

$$
\nu_G
=\frac{G\mu_BL_B^2Q_B\omega_B^3}{c^5}.
$$

At the causal crossover $\epsilon\sim1$,

$$
\mathcal C_{\rm hist}\sim O(\nu_G)\ll1.
$$

Therefore a single freely falling local receiver cannot simultaneously obtain, within this strong sufficient witness:

1. order-unity dynamical retardation, and
2. a better branch record than the total outgoing gravitational complement,

for ordinary laboratory values of $\nu_G$.

This is **not a no-go theorem for gravity-mediated entanglement**. The history-transfer margin is sufficient rather than necessary, and the present complement model includes the total coherent radiation while omitting a fully gauge-invariant accounting of dressing/soft sectors. The result is a quantified local-mode-capture limitation for this witness.

---

## 11. Why an enclosing receiver is qualitatively different

The local receiver samples one small tensor/mode component of the outgoing field. An ideal enclosing quantum receiver can instead be mode-matched to the full outgoing quadrupolar wave packet.

If it coherently captures a fraction $\tau_{\rm ch}$ of the branch-distinguishing outgoing mode, the pure-loss benchmark gives

$$
\mathcal M_\Xi
=(2\tau_{\rm ch}-1)|\Delta|^2.
$$

A positive strong witness requires

$$
\tau_{\rm ch}>\frac12.
$$

Thus the near-field/wave-zone conflict for a local receiver is not obviously a fundamental prohibition on causal quantum-information transport. It may instead reveal that **the correct wave-zone receiver is a mode collector, not a pointlike test mass**.

---

## 12. Main conceptual result at this checkpoint

> **Once the receiver is formulated in Einstein's natural local observable—geodesic deviation—the entire quadrupolar gravitational interaction can be represented by one retarded electric-curvature transfer polynomial. That polynomial makes the near-field/wave-zone tension explicit: the local receiver can dominate radiative branch leakage only deep in the reactive near field, while order-unity retardation occurs where its capture efficiency is suppressed to the tiny dimensionless scale $\nu_G$. The remaining question is whether this is merely a local-receiver mode-matching problem or a deeper constraint on causal quantum-information transport by gravity.**

---

## 13. Immediate next work

1. Re-derive the same transfer polynomial directly from the gauge-invariant electric Weyl tensor or an independent linearized-GR formalism as a cross-check.
2. Replace the radiation-only complementary spectrum by a fully consistent operational complement including soft/dressing effects.
3. Calculate the enclosing mode-matched receiver channel and its $\tau_{\rm ch}$ explicitly.
4. Determine whether a rigorous upper bound connects local capture efficiency to $\epsilon$ for arbitrary compact receivers.
5. Compare the history-transfer witness with current geodesic-deviation classical/quantum-gravity tests and retarded-GIE proposals before claiming novelty.
