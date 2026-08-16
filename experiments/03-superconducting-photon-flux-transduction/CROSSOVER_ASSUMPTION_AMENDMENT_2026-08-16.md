# Experiment 03 — crossover assumption amendment

**Date:** 2026-08-16

## Correction

The quantity previously called the exact dissipative quantum/thermal crossover,

\[
\Lambda_1(T_\times)=0,
\]

is exactly the **local sphaleron first-Matsubara stability boundary**.  It is not, by itself, a proof that the globally dominant periodic instanton merges continuously into the sphaleron there.

The production finite-T solver seeds a one-negative-mode periodic branch at `0.94 Tx`, selects the lowest-action accepted branch there, and then continues it to the target temperature.  That procedure is valid for obtaining a low-action periodic saddle, but near `Tx` it does not establish which local bifurcation branch is being followed if multiple periodic saddles coexist.

## New falsification result

A direct pole-residue test approached the local stability boundary from below at `delta=.214`.  Instead of the tracked instanton action approaching the sphaleron action rapidly,

```text
T/Tx=.990 -> DeltaB = Bsph-Binst = 0.3607
T/Tx=.996 -> DeltaB = 0.2859.
```

At the same time the ratio of the magnitude of the signed parabolic-barrier pole to the provisional instanton cancellation term moved **away** from unity:

```text
T/Tx=.900 -> residue ratio ~2.55
.940 -> 2.91
.960 -> 3.43
.975 -> 4.40
.985 -> 6.11
.990 -> 8.24
.994 -> 12.48
.996 -> 17.77.
```

Therefore the simple second-order quartic-merger interpretation is **not currently established**.

## Competing explanations now under test

1. **Multiple periodic branches / first-order crossover.**  The lowest-action one-negative-mode instanton selected at `0.94 Tx` may remain finite-amplitude as the sphaleron local mode softens.  The physically relevant action crossover could then be first order and occur at a different temperature.
2. **Continuation branch-selection artifact.**  A separate small-amplitude branch may merge continuously into the sphaleron but is not the branch selected by the production continuation seed/ranking.
3. **Very sharp asymptotic merger.**  This is mathematically possible but disfavored by the current trend and must be demonstrated rather than assumed.

A direct fixed-temperature multi-seed stationary-branch topology workflow is running to distinguish these cases.

## Consequences

Until that branch topology is resolved:

- `T_x` must be called the **local sphaleron Matsubara stability boundary**, not automatically the physical quantum-to-thermal action crossover;
- the earlier inferred quartic coefficient `g4=lambda1^2/(4 DeltaB)` must not be interpreted as a true local Landau coefficient unless the tracked instanton is shown to be the small-amplitude bifurcating branch;
- the erfc weights computed from the tracked `DeltaB` are descriptive action-space diagnostics only;
- all uniform-rate extensions above the accepted Gaussian design region remain provisional;
- the accepted `.210-.212` design comparison is unaffected because it is based directly on the finite-period saddle and calibrated Gaussian determinant, but proximity-to-crossover error estimates must be revisited after topology resolution.

## Active workflow

`Experiment 03 crossover branch topology`

The workflow independently solves the periodic stationary equation at fixed `T/Tx` from many first-harmonic seed amplitudes and clusters solutions by path amplitude, action, and Morse index.  This is the immediate crossover-theory gate.
