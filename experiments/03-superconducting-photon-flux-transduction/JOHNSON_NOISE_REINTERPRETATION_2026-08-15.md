# Experiment 03 — Johnson-Noise Reinterpretation After Same-Environment Closure

**Date:** 2026-08-15  
**Status:** conceptual conclusion within the retained passive-bath model

## 1. Original intuition

A purely dissipationless superconducting transport channel has no ordinary local resistor Johnson source because equilibrium voltage noise is proportional to the dissipative part of the impedance,

\[
S_V\propto \operatorname{Re}Z.
\]

This motivated the question whether a superconducting photovoltaic / supercurrent detector could eliminate Johnson noise.

## 2. What the detector architecture actually requires

The metastable flux-latch detector does not use a resistive signal channel, but reliable finite-pulse capture requires damping. The retained design therefore contains a deliberately engineered passive two-pole environment with

\[
\operatorname{Re}Y(\omega)>0.
\]

By fluctuation-dissipation, that damping necessarily brings equilibrium fluctuations. The same `Y(omega)` is used for:

- real-time capture noise;
- the Euclidean dissipative instanton;
- the fluctuation determinant / dark rate.

Thus the architecture can remove **transport-channel Johnson noise** while still having bath-induced fluctuations. These are not contradictory statements.

## 3. Current safe-frontier numbers

Near the current reduced optimum neighborhood,

```text
fc ~ 1.9 GHz
T0 = 20 mK.
```

Hence

\[
\frac{hf_c}{k_BT_0}\approx4.6.
\]

For a Bose mode at this frequency,

\[
\bar n
=\frac{1}{e^{hf_c/(k_BT_0)}-1}
\approx10^{-2}.
\]

The symmetrized quantum-FDT multiplier is

\[
\coth\!\left(\frac{hf_c}{2k_BT_0}\right)
\approx1.02.
\]

Therefore at the phase frequency the bath noise is already overwhelmingly quantum zero-point noise; thermal excess contributes only about two percent to the symmetrized level.

The thermal/quantum crossover frequency set only by the bath temperature is

\[
f_T=\frac{k_BT_0}{h}\approx0.417\ \mathrm{GHz}.
\]

Frequencies well below this remain in the classical thermal-noise regime, so low-frequency equilibrium / technical flux fluctuations are not automatically eliminated.

## 4. Stronger conclusion

The useful statement is not

```text
superconducting detector -> zero noise.
```

It is

```text
dissipationless signal storage can remove one conventional transport-noise term,
but any passive damping used to make the detector latch/recover reintroduces
fluctuations through FDT.
```

At sufficiently low temperature the thermal part of those fluctuations becomes small, but the zero-point part does not vanish. The dark problem then crosses from ordinary Johnson/thermal activation toward quantum escape / tunneling.

The present instanton calculation is precisely the quantitative expression of that residual quantum dark channel.

## 5. Design implication

Cooling below the point where

\[
\hbar\omega_{signal}\gg k_BT
\]

has diminishing leverage on the **high-frequency** bath noise because the symmetrized spectrum approaches its zero-point limit. Further dark-rate improvement must then come from:

- larger Euclidean action / barrier engineering;
- spectral placement of dissipation;
- reduced coupling to unwanted bath modes;
- suppression of non-equilibrium quasiparticle, vortex, stray-photon and technical flux channels.

This is why the current design optimization is fundamentally a sensitivity–damping–dark-action trade rather than a simple `R=0 => no noise` argument.
