# Rate-Induced Tipping Collision Audit — 2026-08-15

## Purpose

Classify the new sub-fold nonadiabatic switching result against the general dynamical-systems literature before assigning any novelty to it.

## 1. Direct conceptual collision

### Ashwin, Wieczorek, Vitolo, and Cox (2012)

**Title:** Tipping points in open systems: bifurcation, noise-induced and rate-dependent examples in the climate system  
**Journal:** Philosophical Transactions of the Royal Society A 370, 1166–1184  
**DOI:** 10.1098/rsta.2011.0306  
**arXiv:** 1103.0169

This work explicitly introduces rate-dependent / rate-induced tipping: sufficiently rapid variation of an input parameter can cause a trajectory to leave a branch of attractors even when the corresponding frozen system has no bifurcation at the tipping point.

**Collision:** the generic Experiment-03 statement

```text
fast thermal parameter variation can trigger switching even when the instantaneous frozen system still contains the original metastable well
```

is an instance of already-established nonautonomous tipping structure and must not be presented as a new mathematical phenomenon.

### Ashwin, Perryman, and Wieczorek (2017 publication; arXiv 1506.07734)

**Title:** Parameter shifts for nonautonomous systems in low dimension: Bifurcation- and Rate-induced tipping

Develops rate-induced tipping for smooth time-varying parameter shifts and distinguishes tracking of stable frozen equilibria at sufficiently slow rates from loss of tracking at higher rates.

### Wieczorek, Xie, and Ashwin, arXiv:2111.15497

**Title:** Rate-Induced Tipping: Thresholds, Edge States and Connecting Orbits

Develops a multidimensional framework in which rate-induced tipping is associated with loss of tracking and basin-boundary / edge-state geometry. It emphasizes that nonautonomous instability need not be understandable from frozen bifurcations alone.

This is particularly close in spirit to Experiment 03 because the current full RCSJ trajectories can cross a basin boundary while the frozen hot potential still contains the original metastable state.

## 2. Josephson-specific dynamical background

Josephson systems already have extensive literature on switching, hysteresis, bifurcation and transient dynamics. Examples identified in the current search include:

- pulse-driven/stochastic switching of Josephson junctions and superconducting wires;
- bifurcation and hysteresis in driven `phi0` Josephson systems;
- transient quench dynamics in superconducting Josephson structures;
- self-heating-modified RCSJ switching and phase diffusion in graphene Josephson junctions.

These further reinforce that neither fast switching nor nonlinear basin selection in a Josephson system is a broad novelty route.

A dedicated detector-specific collision search remains necessary for the exact conjunction

```text
single absorbed LWIR photon
-> proximity-JJ nonadiabatic metastable switching
-> directionally favored persistent flux state
-> explicit cold-dark / rise-time / damping / wavelength closure.
```

## 3. Current terminology rule

It is acceptable internally to describe the fast-pulse regime as

```text
rate-induced / nonadiabatic metastable switching
```

when that language is technically useful.

Do **not** say or imply that Experiment 03 discovered rate-induced tipping.

The rf-SQUID fold remains the quasistatic organizing limit; the full detector dynamics belongs to the broader known class of nonautonomous basin/tipping problems.

## 4. Surviving theoretical questions

Potentially distinct objects that still require collision audit include:

1. the detector-specific sudden-quench energy threshold

```math
U(x_{cold},T_q)=U(x_{saddle},T_q);
```

2. the three spectral scales

```text
lambda_fold
lambda_dynamic
lambda_quench;
```

3. the explicit MQT dark-stability time

```math
tau_Q(D)
```

and its coupling to finite-rate optical capture;

4. the exact parametric phase-work accounting

```math
dE_phi/dt=U_T dot T-(L/R) dot x^2
```

applied to single-photon persistent-flux transduction;

5. any device-specific optimality/impossibility bound after the same causal environmental admittance is used for capture noise and dissipative MQT.

None is authorized as novel yet.

## Status

**GENERIC RATE-INDUCED-TIPPING NOVELTY ROUTE: CLOSED.**

**EXPERIMENT 03: GO for continued detector-specific theory; NO-GO for manuscript.**
