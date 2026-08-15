# Two-Stage Launch / Capture Damping Closure — 2026-08-15

## Purpose

Use the exact parametric phase-work identity to formalize why the full deterministic solver develops a finite damping window.

The key distinction is between

```text
Stage A: launch / separatrix crossing
Stage B: target-basin capture / retrapping.
```

Dissipation has opposite functional roles in these stages.

This is an exact energy accounting within scalar-R time-dependent RCSJ dynamics while the relevant saddle exists. It is not a complete stochastic capture theorem and is not a novelty claim.

## 1. Separatrix-relative energy

Retain

```math
\mathcal E_s(t)
=\frac12LC\dot x^2
+U[x,T]
-U[x_s(T),T]
```

and

```math
\boxed{
\dot{\mathcal E}_s
=[U_T(x,T)-U_T(x_s,T)]\dot T
-\frac{L}{R}\dot x^2.
}
```

Initially the phase is at the cold left minimum with zero velocity, so

```math
\boxed{\mathcal E_s(0)=-B_c,}
```

where

```math
B_c=U_s(T_0)-U_L(T_0)>0
```

is the cold forward barrier.

Define accumulated separatrix-relative parametric work

```math
W_s(t)
=\int_0^t
[U_T(x,T)-U_T(x_s,T)]\dot Tdt'
```

and dissipative loss

```math
Q_R(t)
=\int_0^t\frac{L}{R}\dot x^2dt'.
```

Then

```math
\boxed{
\mathcal E_s(t)
=-B_c+W_s(t)-Q_R(t).
}
```

## 2. Stage A — energetic launch condition

For the trajectory to become energetically capable of crossing the instantaneous separatrix while it exists, it must reach

```math
\mathcal E_s\ge0.
```

Therefore a necessary launch condition is

```math
\boxed{
W_s(t)-B_c\ge Q_R(t).
}
```

Let `t_x` be the actual first crossing of the moving saddle. At that instant `x=x_s` and

```math
\mathcal E_s(t_x)
=\frac12LC\dot x^2(t_x)
\equiv K_x\ge0.
```

Hence the exact crossing energy balance is

```math
\boxed{
W_s(t_x)
=B_c+Q_{R,<}+K_x,
}
```

where

```math
Q_{R,<}
=\int_0^{t_x}\frac{L}{R}\dot x^2dt.
```

This equation makes the pre-crossing role of damping explicit:

> At fixed trajectory-parametric work, every unit of phase energy dissipated before crossing must be replaced by additional optical/parametric work.

Thus excessive launch-stage dissipation can suppress switching even when photon energy is unchanged.

## 3. Stage B — capture condition after crossing

After first crossing, let the phase continue while the thermal pulse cools and the cold double-well reforms.

At a time `t_r` after the drive has effectively returned to the cold landscape, define

```math
E_\phi(t_r)
=\frac12LC\dot x^2(t_r)+U[x(t_r),T_0].
```

A simple sufficient energetic condition for remaining in the target basin in the frozen cold potential is

```math
\boxed{
E_\phi(t_r)<U_s(T_0)
}
```

together with the coordinate lying on the target side of the separatrix.

Let

```math
E_x
=U[x_s(T_x),T_x]+K_x
```

be the phase energy at first crossing and define the post-crossing parametric work

```math
W_{T,>}
=\int_{t_x}^{t_r}U_T(x,T)\dot Tdt.
```

The absolute phase-energy identity gives

```math
E_\phi(t_r)
=E_x+W_{T,>}-Q_{R,>},
```

where

```math
Q_{R,>}
=\int_{t_x}^{t_r}\frac{L}{R}\dot x^2dt.
```

Therefore the simple cold-trapping condition requires

```math
\boxed{
Q_{R,>}
>
E_x+W_{T,>}-U_s(T_0).
}
```

If the right-hand side is negative, cooling/potential recovery already leaves the phase below the cold saddle and no additional dissipative loss is energetically required by this sufficient condition.

Otherwise, **post-crossing dissipation is beneficial and may be necessary**.

## 4. The damping conflict in one line

The two stages require schematically

```math
\boxed{
Q_{R,<}
\lesssim
W_s-B_c
}
```

but

```math
\boxed{
Q_{R,>}
\gtrsim
Q_{cap,min}.
}
```

Thus a successful detector wants

```text
small enough dissipation before crossing
and
large enough dissipation after crossing.
```

A constant broadband scalar resistance must compromise between these two requirements. This is the energy-accounting origin of the finite capture windows observed in the full deterministic solver.

## 5. Why the optimum environment should be state/frequency dependent

For constant `R`,

```math
Q_{R,<}=\frac{L}{R}\int_{launch}\dot x^2dt,
```

and

```math
Q_{R,>}=\frac{L}{R}\int_{capture}\dot x^2dt.
```

The same scalar coefficient `L/R` controls both the harmful pre-crossing loss and the useful post-crossing loss.

A more flexible environment can in principle shape

```text
Re Y(omega,T,state)
```

so that its effective dissipation differs during launch, capture and cold storage.

The target qualitative profile is

```text
launch:       relatively weak phase damping
capture:      stronger damping / energy removal
cold storage: low dissipative coupling.
```

This is not a free improvement. Every real dissipative admittance contributes equilibrium/quantum fluctuations through fluctuation-dissipation and changes the tunneling action.

## 6. Connection to the original zero-Johnson-noise question

The detector does not need to maintain a resistive signal current during storage.

A photon can act as a trigger that redirects pre-existing Josephson/inductive free energy into another persistent flux state. The cold output can then be stored in a superconducting degree of freedom with very small `Re Z`.

The cost has moved from continuous `4kTR` signal-channel noise to

```text
metastability / false switching
write-stage dissipation
quantum escape
readout/reset backaction.
```

This is a more precise statement than saying the detector has "zero noise."

## 7. Stored-energy amplification is allowed, but not free

Because the initial flux state can be metastable and because an external flux bias or Josephson/inductive potential stores free energy, the electrical/phase energy released during switching need not be limited to `h nu`.

Therefore an apparent electrical energy gain

```math
E_{phase,out}/E_\gamma>1
```

does not violate energy conservation if the additional energy is drawn from the pre-biased superconducting potential.

But increasing stored metastable energy generally changes the forward barrier and hence the dark-switch problem. This is a future optimization axis, not a free gain mechanism.

## 8. What remains to compute

The full dynamic solver should be extended to record

```text
first separatrix crossing time t_x
K_x
W_s(t_x)
Q_R,<
W_T,>
Q_R,>
final cold energy relative to target saddle.
```

Then capture and noncapture trajectories can be compared directly against the two-stage inequalities above.

If a simple dimensionless separation emerges, it can become the reduced deterministic model supplied to the later causal-admittance and stochastic calculations.

## Status

**GO for continued theory. NO-GO for manuscript.**
