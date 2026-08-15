# Experiment 03 — Directional Fold Barrier Closure — 2026-08-15

## Statement

The large directional barrier asymmetry seen in the current tilted rf-SQUID model near the metastable-left-well fold is not a numerical accident or a graphene-specific effect. It follows generically from the local saddle-node asymptotics provided the *target* minimum remains a distinct remote stable state at the fold.

This is an elementary catastrophe-theory consequence, not a novelty claim.

---

## 1. Local disappearing-well barrier

Let a smooth one-dimensional potential `U(x,p)` depend on control parameter `p`. At a nondegenerate saddle-node `(x_f,p_f)`,

```math
U_x(x_f,p_f)=0,
\qquad
U_{xx}(x_f,p_f)=0,
```

with

```math
U_{xxx}(x_f,p_f)\neq0,
\qquad
\partial_p U_x(x_f,p_f)\neq0.
```

Let

```math
\epsilon=p_f-p>0
```

be the distance to the fold on the bistable side. The local normal form is

```math
U_{loc}(q,\epsilon)
=U_f-a\epsilon q+\frac{b}{3}q^3+\cdots,
```

with `a,b>0` after orientation choices.

The metastable minimum and saddle lie at

```math
q_{m,s}=\pm\sqrt{a\epsilon/b}+O(\epsilon).
```

Their barrier therefore scales as

```math
\boxed{
B_{write}(\epsilon)
=U(q_s)-U(q_m)
=A\epsilon^{3/2}+O(\epsilon^2),
}
```

where

```math
A=\frac{4}{3}\frac{a^{3/2}}{b^{1/2}}
```

in the leading normal form.

This is the familiar saddle-node `3/2` barrier law.

---

## 2. Remote target-state return barrier

Now assume a separate target minimum `x_R(p)` remains nondegenerate and stable through `p=p_f`:

```math
U_x[x_R(p_f),p_f]=0,
\qquad
U_{xx}[x_R(p_f),p_f]>0,
```

and is distinct from the local saddle-node coordinate.

The separating saddle approaches `x_f` continuously as `epsilon->0`. Therefore the target-to-saddle barrier is a regular quantity:

```math
B_{return}(\epsilon)
=U[x_s(\epsilon),p]-U[x_R(\epsilon),p].
```

By smoothness,

```math
\boxed{
B_{return}(\epsilon)
=B_0+O(\epsilon^{1/2})
}
```

in full generality, with the leading correction potentially containing `sqrt(epsilon)` through the saddle displacement. Here

```math
B_0
=U(x_f,p_f)-U[x_R(p_f),p_f].
```

If the target minimum is genuinely lower than the fold saddle,

```math
\boxed{B_0>0.}
```

The key result is the nonzero limiting return barrier, not the exact leading correction power.

---

## 3. Divergent directional barrier ratio

Combining the two barriers gives

```math
\boxed{
\frac{B_{return}}{B_{write}}
\sim
\frac{B_0}{A}\epsilon^{-3/2}
\to\infty
\qquad
(\epsilon\to0^+).
}
```

Thus a one-sided fold can make the desired write escape arbitrarily easy relative to reverse escape, **without requiring the target-state retention barrier to vanish at the same point**.

This does not create a free detector: pulse-time fluctuations, finite-time transport, quantum escape from the target state, and causal damping still constrain performance. It does create a structural asymmetry that changes which barrier should be used in the noise analysis.

---

## 4. Current Experiment-03 numerical realization

For the retained `rDelta=.6` tilted full-CPR loop,

```text
T = 0.0200 K:
  B_write/kB  ~ 6.91 K
  B_return/kB ~12.20 K
  ratio       ~ 1.77

T = 0.62699 K (~90% of fold span):
  B_write/kB  ~0.369 K
  B_return/kB ~4.669 K
  ratio       ~12.7

T = 0.67420 K (~97%):
  B_write/kB  ~0.0607 K
  B_return/kB ~4.052 K
  ratio       ~66.8

T = 0.68768 K (~99%):
  B_write/kB  ~0.0117 K
  B_return/kB ~3.896 K
  ratio       ~333.
```

The numerical trend is exactly the qualitative asymptotic expected above: the disappearing left-well barrier collapses while the remote favored-state barrier approaches a finite value around `3.8–3.9 k_B K`.

Canonical numerical source:

```text
calculations/directional_recovery_barriers.py
.github/workflows/experiment03-directional-recovery.yml
run 31913077311
```

---

## 5. Detector interpretation

The appropriate architecture is therefore not merely

```text
photon lowers a barrier.
```

It is more specifically

```text
photon drives the INITIAL metastable state toward a one-sided fold
while the TARGET state survives with a finite reverse barrier.
```

If the phase reaches the target side before the metastable state and saddle reform during cooling, the detector can enter a state with finite directional protection immediately upon recovery.

For the current `14 um`, `rise=20 ps`, `R=250 ohm` causal-filter trajectories:

```text
first favored-side crossing ~44.6–46.9 ps
left-well/saddle reformation ~57.75 ps
return barrier at reformation ~3.83 k_B K.
```

So the current deterministic model realizes the required ordering.

---

## 6. Scope and limits

This closure is generic to smooth tilted bistable potentials with a one-sided saddle-node and a surviving remote target minimum. It is therefore **not** itself a novelty route.

Its value for Experiment 03 is methodological:

- use the disappearing barrier for write sensitivity;
- use the surviving target barrier for post-write retention;
- do not compare late recovery fluctuations to the disappearing left barrier;
- focus stochastic/open-system analysis on whether the trajectory reaches the protected side before reformation.

The remaining hard problem is dynamical and quantum, not static barrier existence.

**Status: derived asymptotic architecture principle; GO for continued theory; NO-GO for manuscript.**
