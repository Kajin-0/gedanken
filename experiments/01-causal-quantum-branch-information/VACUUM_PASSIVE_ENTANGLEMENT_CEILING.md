# Vacuum Passive Wave-Zone Entanglement Ceiling

**Timestamp:** 2026-08-07 17:48 EDT  
**Status:** Leading-order bound for passive nonrelativistic resonant receivers in the weak-capture regime. This is a receiver-class result, not a universal no-go theorem for quantum gravity.

## 1. Why this result matters

At exactly zero thermal occupation, a pure-loss bosonic channel is non-entanglement-breaking for every nonzero transmissivity. Therefore the mathematical NPT range of the receiver can extend arbitrarily far:

$$
\eta>0
\Rightarrow
\text{some finite-cat entanglement survives}.
$$

That makes the bare NPT sign boundary a poor measure of practical quantum transfer in vacuum.

The right question is instead:

> **How much source–receiver entanglement can a passive wave-zone receiver possibly store, even in perfect vacuum?**

The answer is controlled by the source-to-receiver free-space mode overlap multiplied by the receiver's gravitational branching ratio.

---

## 2. Total vacuum storage efficiency

For the compact resonant aligned-plus receiver in the wave zone,

$$
\boxed{
\eta_{\rm ff}(R)
=\frac{25\mathcal O}{16(kR)^2},
}
$$

where $\mathcal O$ is the remaining normalized tensor/temporal/source-receiver mode overlap.

The receiver has intrinsic graviton linewidth

$$
\kappa_g
$$

and total linewidth

$$
\kappa_{\rm tot}
=\kappa_g+\kappa_i+\cdots.
$$

For an optimally time-reversed incoming waveform and asymptotically complete loading, the fraction of the incoming source difference mode stored in the receiver is at most

$$
\boxed{
\eta_Q(R)
=\eta_{\rm ff}(R)
\frac{\kappa_g}{\kappa_{\rm tot}}.
}
$$

Thus

$$
\boxed{
\eta_Q(R)
=\frac{25\mathcal O}{16(kR)^2}
\frac{\kappa_g}{\kappa_{\rm tot}}.
}
$$

This is the **vacuum quantum reception efficiency** of the resonant memory model.

It is the product of two independent losses:

1. free-space source-to-receiver mode overlap;
2. receiver gravitational branching ratio.

---

## 3. Pure-loss source-cat negativity

Let the source branch-difference mode contain coherent-state distance

$$
N_\Delta.
$$

After pure-loss storage fraction $\eta_Q$, the exact source-receiver negativity is

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
s_B=e^{-\eta_QN_\Delta/2},
\qquad
s_E=e^{-(1-\eta_Q)N_\Delta/2}.
$$

At fixed imperfect capture $\eta_Q<1$, arbitrarily large branch separation does **not** maximize entanglement. The uncaptured output becomes an increasingly good branch record and drives the source-receiver negativity back toward zero.

For

$$
\eta_Q\ll1,
$$

optimization over $N_\Delta$ gives the previously derived asymptotics

$$
\boxed{
N_\Delta^{\rm opt}
=4\sqrt{\eta_Q}+O(\eta_Q),
}
$$

and

$$
\boxed{
\mathcal N_{\max}
=\eta_Q-2\eta_Q^{3/2}+O(\eta_Q^2).
}
$$

Therefore, in the weak-capture regime,

$$
\boxed{
\mathcal N_{\max}
\simeq\eta_Q.
}
$$

This is the key bridge from receiver channel efficiency to maximum transferable entanglement.

---

## 4. Passive nonrelativistic receiver bound

For a passive nonrelativistic quadrupole receiver,

$$
\boxed{
\frac{\kappa_g}{\omega_B}
\le
\frac23\mathcal C_B\beta_B^3,
}
$$

where

$$
\mathcal C_B
=\frac{r_{s,B}}{L_B},
$$

and

$$
\beta_B
=\frac{\omega_BL_B}{c}.
$$

If internal loss dominates the graviton linewidth,

$$
\kappa_{\rm tot}\simeq\kappa_i
=\frac{\omega_B}{Q_B},
$$

then

$$
\boxed{
\frac{\kappa_g}{\kappa_{\rm tot}}
\lesssim
\frac23Q_B\mathcal C_B\beta_B^3.
}
$$

Thus

$$
\boxed{
\eta_Q(R)
\lesssim
\frac{25\mathcal O}{24(kR)^2}
Q_B\mathcal C_B\beta_B^3.
}
$$

For weak capture this immediately gives

$$
\boxed{
\mathcal N_{\max}(R)
\lesssim
\frac{25\mathcal O}{24(kR)^2}
Q_B\mathcal C_B\beta_B^3
}
$$

at leading order.

---

## 5. Wave-zone ceiling

Require

$$
kR\ge\zeta,
$$

with $\zeta\gtrsim1$ defining how deeply into the radiation zone the receiver operates.

Then

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\lesssim
\frac{25\mathcal O}{24\zeta^2}
Q_B\mathcal C_B\beta_B^3
}
$$

provided the right-hand side is much smaller than unity so the weak-capture asymptotics are self-consistent.

Define

$$
\boxed{
\mathfrak V_B
\equiv
\frac{25\mathcal O}{24\zeta^2}
Q_B\mathcal C_B\beta_B^3.
}
$$

Then

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\lesssim\mathfrak V_B
}
$$

for

$$
\mathfrak V_B\ll1.
$$

This is the **vacuum passive wave-zone entanglement figure of merit**.

---

## 6. Physical meaning

The three factors are now transparent:

### $\mathcal C_B$

$$
\mathcal C_B=r_s/L_B
$$

measures gravitational compactness.

### $\beta_B^3$

$$
\beta_B^3=(\omega_BL_B/c)^3
$$

is the nonrelativistic quadrupole-radiation suppression.

### $Q_B$

The quality factor determines how many coherent receiver cycles are available before ordinary loss removes the stored excitation.

Thus ordinary laboratory matter suffers from

$$
\boxed{
\text{weak compactness}
\times
\text{nonrelativistic motion}^{\,3}
\times
\text{finite memory time}.
}
$$

No thermal noise is needed for this suppression.

---

## 7. Illustrative upper-bound examples

These are deliberately generous substitutions into the **upper bound**, not proposed devices. Take

$$
\mathcal O=1,
\qquad
\zeta=1,
\qquad
Q_B=10^{12}.
$$

### Example A — $1\,\mathrm{kg}$, $1\,\mathrm m$, $1\,\mathrm{kHz}$

$$
\mathcal C_B\simeq1.49\times10^{-27},
$$

$$
\beta_B\simeq2.10\times10^{-5}.
$$

Therefore

$$
\boxed{
\mathfrak V_B
\simeq1.4\times10^{-29}.
}
$$

Even if the receiver **saturated the passive oscillator-strength bound** and had perfect source-mode matching, the optimized source-receiver negativity at the wave-zone edge would be at most of order $10^{-29}$ in the weak-capture approximation.

### Example B — extremely aggressive $10^3\,\mathrm{kg}$, $1\,\mathrm m$, $1\,\mathrm{MHz}$

$$
\mathcal C_B\simeq1.49\times10^{-24},
$$

$$
\beta_B\simeq2.10\times10^{-2},
$$

so

$$
\boxed{
\mathfrak V_B
\simeq1.4\times10^{-17}.
}
$$

This remains extraordinarily small despite the intentionally extreme assumptions.

### Example C — formal high-frequency compact laboratory object

Take

$$
M=1\,\mathrm{kg},
\quad
L_B=1\,\mathrm{cm},
\quad
f_B=1\,\mathrm{GHz},
\quad
Q_B=10^{12}.
$$

Then

$$
\beta_B\simeq0.21,
$$

already pushing beyond the comfortable nonrelativistic-mechanical regime, yet formally

$$
\boxed{
\mathfrak V_B
\simeq1.4\times10^{-15}.
}
$$

The result improves only as the receiver is driven toward relativistic internal dynamics, where the derivation itself must be replaced by a field-theoretic treatment.

---

## 8. Important distinction from the thermal range

At nonzero temperature, the receiver can become fully entanglement breaking beyond a finite range.

At zero temperature, pure loss is never EB for nonzero transmissivity, so there is no finite **mathematical** NPT range.

Nevertheless

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\lesssim\mathfrak V_B
}
$$

can make the transferable entanglement fantastically small.

Thus the passive wave-zone limitation has two qualitatively different forms:

### Thermal limitation

$$
\text{entanglement may be impossible at all.}
$$

### Vacuum limitation

$$
\text{entanglement exists mathematically but its maximum magnitude is parametrically tiny.}
$$

The vacuum ceiling is therefore the more robust statement when discussing idealized receivers.

---

## 9. Not a universal no-go theorem

The derivation assumes

- passive stationary receiver;
- nonrelativistic particle-coordinate Hamiltonian underlying the quadrupole sum rule;
- one dominant resonant quadrupole mode;
- linearized gravity;
- compact resonant wave-zone storage;
- ordinary internal loss summarized by $Q_B$.

It does not automatically apply to

- relativistic QFT receiver modes;
- strongly self-gravitating/compact systems;
- active or inverted receivers;
- non-Gaussian/heralded protocols;
- coherent distributed arrays whose collective mode changes the relevant oscillator-strength budget;
- near-field virtual gravitational mediation.

---

## 10. Strongest interpretation

> **Even if every thermal excitation were removed, ordinary passive matter can be an extraordinarily poor quantum gravitational receiver. The problem is not merely that the gravitational wave is weak. The receiver has only a tiny gravitational branching ratio, set by compactness and nonrelativistic quadrupole motion, and only a tiny fraction of the outgoing branch mode reaches a distant resonant memory. In the weak-capture regime the maximum source–receiver entanglement is approximately that total quantum storage efficiency.**

This is currently the cleanest passive-matter feasibility statement in Experiment 01.

---

## 11. Next strongest path

1. Search for an existing passive gravitational receiver/branching-ratio bound equivalent to $\mathfrak V_B$.
2. Analyze a relativistic field-theoretic receiver, where the nonrelativistic quadrupole sum-rule ceiling does not apply.
3. Analyze whether a distributed coherent array can parametrically increase $\kappa_g/\kappa_{\rm tot}$ or only improve source-mode overlap.
4. Use $\mathfrak V_B$ as the vacuum baseline when testing active/non-Gaussian loopholes.