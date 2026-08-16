# Experiment 03 — Passive Damping / Fluctuation-Work Identity

**Date:** 2026-08-15  
**Status:** exact linear-bath identity for a prescribed trajectory; nonlinear detector implications are conditional

## 1. Motivation

The detector concept began from the observation that a dissipationless superconducting signal/storage channel need not have an ordinary local resistor Johnson source. The actual latch architecture nevertheless requires passive damping for capture and recovery.

The fluctuation-dissipation theorem then implies a stronger trajectory-level statement: for a prescribed signal trajectory, the mean energy dissipated into a passive equilibrium bath and the variance of the bath's fluctuating work along that same trajectory are controlled by the **same spectral weight**.

The quantum FDT used here is the Callen–Welton generalized-noise relation (H. B. Callen and T. A. Welton, *Physical Review* **83**, 34–40, 1951, DOI 10.1103/PhysRev.83.34), specialized to an electrical admittance.

## 2. Conventions

Let `q(t)` be a real generalized flux coordinate and

\[
V(t)=\dot q(t)
\]

the corresponding generalized voltage.

Let the passive linear environment have admittance `Y(omega)` with

\[
\operatorname{Re}Y(\omega)\ge0.
\]

Use the two-sided Fourier convention

\[
V(t)=\int\frac{d\omega}{2\pi}V(\omega)e^{-i\omega t},
\]

and the symmetrized current-noise PSD convention already used by the Experiment-03 TWA code,

\[
\boxed{
S_I^{sym}(\omega)
=\epsilon_T(\omega)\operatorname{Re}Y(\omega),
}
\]

with

\[
\boxed{
\epsilon_T(\omega)
=\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT}\right).
}
\]

## 3. Dissipated energy along a prescribed trajectory

For a real trajectory, the deterministic energy delivered to the dissipative part of the bath is

\[
\boxed{
E_{diss}
=\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
\operatorname{Re}Y(\omega)|V(\omega)|^2.
}
\]

Define the nonnegative dissipative spectral measure

\[
\boxed{
d\mu(\omega)
=\frac{d\omega}{2\pi}
\operatorname{Re}Y(\omega)|V(\omega)|^2.
}
\]

Then simply

\[
E_{diss}=\int d\mu.
\]

## 4. Fluctuating bath work along the same trajectory

Let `I_n(t)` be the zero-mean equilibrium bath-current fluctuation and define the linear fluctuating work functional

\[
W_n=\int dt\,V(t)I_n(t).
\]

For the prescribed c-number trajectory, its symmetrized second moment is

\[
\boxed{
\langle W_n^2\rangle_{sym}
=\int\frac{d\omega}{2\pi}
S_I^{sym}(\omega)|V(\omega)|^2.
}
\]

Substituting FDT gives the exact identity

\[
\boxed{
\langle W_n^2\rangle_{sym}
=\int \epsilon_T(\omega)\,d\mu(\omega).
}
\]

Therefore

\[
\boxed{
\frac{\langle W_n^2\rangle_{sym}}
     {E_{diss}}
=\langle\epsilon_T\rangle_{diss},
}
\]

where

\[
\langle\epsilon_T\rangle_{diss}
=\frac{\int\epsilon_T(\omega)d\mu(\omega)}{\int d\mu(\omega)}
\]

is a dissipation-weighted quantum energy scale.

This is the cleanest exact statement: **passive dissipation and symmetrized fluctuation work cannot be independently chosen.** Spectral engineering changes the weighting but does not break the relation.

## 5. Universal finite-temperature lower bound

For `x>=0`,

\[
x\coth x\ge1.
\]

With

\[
x=\frac{\hbar|\omega|}{2k_BT},
\]

it follows that

\[
\epsilon_T(\omega)\ge2k_BT
\]

at every frequency.

Because `dmu>=0` for a passive bath,

\[
\boxed{
\langle W_n^2\rangle_{sym}
\ge
2k_BT\,E_{diss}.
}
\]

Equality is approached when the dissipative spectral weight lies in the classical low-frequency regime

\[
\hbar|\omega|\ll k_BT.
\]

In that limit,

\[
\boxed{
\langle W_n^2\rangle
\to2k_BT\,E_{diss}.
}
\]

This is the familiar classical work fluctuation–dissipation scaling expressed for a prescribed electrical trajectory.

## 6. Zero-temperature / quantum limit

At `T->0`,

\[
\epsilon_T(\omega)\to\hbar|\omega|,
\]

so

\[
\boxed{
\langle W_n^2\rangle_{sym,T=0}
=
\hbar\int |\omega|\,d\mu(\omega).
}
\]

There is no nonzero frequency-independent lower bound at `T=0` because a passive bath could in principle move dissipation toward arbitrarily small frequencies. For a given capture protocol / finite-time bandwidth, however, the relevant dissipation-weighted mean frequency remains finite.

Define

\[
\bar\omega_{diss}
=\frac{\int|\omega|d\mu}{E_{diss}}.
\]

Then at zero temperature

\[
\boxed{
\langle W_n^2\rangle_{sym,T=0}
=\hbar\bar\omega_{diss}E_{diss}.
}
\]

Thus quantum spectral shaping matters: dissipating the same trajectory energy at lower characteristic frequency reduces zero-point fluctuation work, but doing so eventually conflicts with the finite-time capture requirement.

## 7. Gaussian-bath signal-to-fluctuation interpretation

For a linear Gaussian bath and prescribed trajectory, `W_n` is Gaussian. Define

\[
\sigma_W^2=\langle W_n^2\rangle_{sym}.
\]

Then

\[
\boxed{
\frac{E_{diss}}{\sigma_W}
=\sqrt{\frac{E_{diss}}
 {\langle\epsilon_T\rangle_{diss}}}.
}
\]

In the classical limit,

\[
\frac{E_{diss}}{\sigma_W}
=\sqrt{\frac{E_{diss}}{2k_BT}}.
\]

This does **not** prove a detector error-probability bound by itself, because the actual nonlinear detector trajectory is stochastic and bath back-action changes the path. It does show why adding passive damping cannot be treated as a noiseless way of increasing trapping margin.

## 8. Detector design interpretation

For Experiment 03:

- larger low-frequency damping can improve retrapping / energetic lock;
- the same `Re Y` increases equilibrium force fluctuations;
- moving dissipation to higher frequencies generally raises the quantum energy factor `epsilon_T`;
- moving it to lower frequencies reduces the noise-work cost per dissipated joule but may be too slow for a finite optical pulse.

Therefore the passive-environment problem is naturally a **spectral optimization of dissipation-weighted fluctuation energy**, not simply “maximize damping.”

The retained two-pole network can now be judged against the exact metric

\[
\boxed{
\langle\epsilon_T\rangle_{diss}
=
\frac{\int\epsilon_T(\omega)\Re Y(\omega)|V(\omega)|^2d\omega}
     {\int\Re Y(\omega)|V(\omega)|^2d\omega}.
}
\]

This may be a more physically meaningful bath-design diagnostic than a scalar resistance or quality factor.

## 9. Scope / non-claims

The identity is exact for:

- a passive linear equilibrium bath;
- a prescribed c-number trajectory;
- the stated symmetrized noise convention.

It is **not** by itself:

- an exact nonlinear detector capture-error theorem;
- a two-projective-measurement quantum-work distribution;
- proof that the current two-pole bath is optimal;
- a novelty claim.

The next useful test is to evaluate `E_diss`, `sigma_W^2`, and `epsilon_eff=<epsilon_T>_diss` on the deterministic photon-capture trajectories of candidate passive networks and test whether this metric predicts the stochastic capture/dark Pareto frontier.
