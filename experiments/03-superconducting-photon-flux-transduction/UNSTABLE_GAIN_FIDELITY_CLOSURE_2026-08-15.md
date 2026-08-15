# Experiment 03 — Unstable Gain–Fidelity Closure — 2026-08-15

## Purpose

The causal-FDT tangent analysis predicts that the cold phase mode's small zero-point width can be amplified to order-radian scale during the transient near-fold dynamics. Large amplification alone does **not** imply poor detector fidelity, because the deterministic directional signal is amplified by the same unstable dynamics.

This checkpoint isolates the simplest exact statement: linear unstable gain cannot improve signal-to-initial-uncertainty ratio without an independent symmetry-breaking displacement/force.

This is elementary linear dynamics, not a novelty claim.

---

## 1. Minimal unstable write model

Take one unstable coordinate `q` after a rapid quench,

```math
\ddot q-\Omega^2q=a,
```

where `a` is a constant directional acceleration representing the local effect of tilt/asymmetry.

The static particular solution is

```math
q_p=-\frac{a}{\Omega^2}.
```

For initial `(q_0,v_0)`,

```math
q(t)
=q_p+(q_0-q_p)\cosh(\Omega t)
+\frac{v_0}{\Omega}\sinh(\Omega t).
```

Assume

```math
\langle q_0\rangle=0,
\qquad
\langle v_0\rangle=0,
\qquad
\operatorname{Cov}(q_0,v_0)=0.
```

Then

```math
\boxed{
\bar q(t)
=\frac{a}{\Omega^2}
[\cosh(\Omega t)-1].
}
```

The variance is

```math
\boxed{
\sigma_q^2(t)
=\sigma_{q0}^2\cosh^2(\Omega t)
+\frac{\sigma_{v0}^2}{\Omega^2}
 \sinh^2(\Omega t).
}
```

---

## 2. Exponential gain cancels out of asymptotic SNR

For `Omega t >> 1`, both the deterministic displacement and fluctuations grow as `exp(Omega t)`.

Therefore

```math
\boxed{
\frac{\bar q}{\sigma_q}
\longrightarrow
\frac{a/\Omega^2}
{\sqrt{
\sigma_{q0}^2+\sigma_{v0}^2/\Omega^2
}}.
}
```

There is no exponential improvement of standardized directional separation.

If the incoming phase mode is a harmonic quantum state with

```math
\sigma_{v0}=\omega_0\sigma_{q0},
```

then

```math
\boxed{
\mathrm{SNR}_{unstable}
\to
\frac{a}
{\Omega^2\sigma_{q0}
\sqrt{1+(\omega_0/\Omega)^2}}.
}
```

Thus an unstable latch is not a free preamplifier of detection fidelity. The same local Lyapunov growth that separates trajectories also magnifies the incoming quantum phase-space ellipse.

---

## 3. Detector interpretation

The correct figure is not

```text
large tangent amplification A_phase.
```

It is a standardized directional distance such as

```math
\frac{x_{det}(t)-x_{boundary}(t)}
{\sigma_{normal}(t)},
```

or, ultimately, the full basin probability under the open quantum dynamics.

A high-gain switching trajectory can still be robust if the directional bias moves the mean sufficiently far from the basin boundary. Conversely, making the transient instability stronger does not automatically improve fidelity.

This is directly relevant to the current Experiment-03 result:

```text
cold sigma_x ~0.115 rad
-> near-fold transient tangent dynamics can produce O(1 rad) linearized spread.
```

That spread is a warning about sensitivity, but it must be judged against the simultaneous deterministic mean/basin displacement.

---

## 4. Design levers exposed

The closure separates several physically different levers:

```text
unstable gain / curvature Omega
    -> accelerates both mean and fluctuations;

directional tilt / asymmetric force a
    -> moves the mean relative to the fluctuation ellipse;

cold quantum width sigma_q0
    -> set by circuit quantization and stability/speed tradeoffs;

quench duration / recovery timing
    -> determines how long unstable gain acts before the target barrier reforms.
```

Therefore improving fidelity should focus on

```text
larger normalized directional displacement,
smaller incoming quantum width,
shorter vulnerable near-boundary dwell,
appropriate spectral damping,
```

not merely larger dynamical gain.

---

## 5. Relation to the directional fold

The one-sided fold remains advantageous because it can simultaneously provide

```text
small/vanishing write barrier
+
finite target-state return barrier.
```

But the initial state's quantum uncertainty must still be routed overwhelmingly into the target basin. The current linearized stationary-history result is not sufficient to establish that: its predicted spread is large enough that the tangent approximation becomes self-inconsistent.

A nonlinear open-system propagation is therefore the correct next falsification test.

**Status: exact minimal-model closure; no novelty claim; GO for continued theory; NO-GO for manuscript.**
