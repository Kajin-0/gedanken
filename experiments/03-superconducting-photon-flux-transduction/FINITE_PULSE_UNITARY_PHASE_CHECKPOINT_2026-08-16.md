# Experiment 03 — Finite-Pulse Unitary Phase Checkpoint — 2026-08-16

## Purpose

Determine what the *isolated nonlinear phase coordinate* does under the actual reduced-model optical pulse before adding the passive environment.

This is the controlled bridge between the converged cold phase-DVR basis and the required reaction-coordinate/open-system calculation.

It answers a narrower question than detector efficiency:

> Does the 20-ps photon-heating/cooling potential itself produce a persistent right-well quantum latch, or is dissipation during barrier reformation essential to the final stored state?

## Model

The benchmark evolves

```math
H_x(t)
=-\frac{\hbar^2}{2C\bar\Phi^2}\frac{d^2}{dx^2}+U[x,T_e(t)]
```

with the exact Experiment-03 full-CPR force and the same reduced thermal history used by the capture calculations:

```math
\frac{dT_e^2}{dt}
=\frac{\Delta T_{ad}^2}{\tau_r}e^{-t/\tau_r}
-\frac{T_e^4-T_0^4}{2\tau_0T_0^2}.
```

Benchmark point:

```text
delta       = .212
r_Gamma     = 10.6229699624
C           = 24.262211 pF
area        = 490 um^2
lambda      = 14 um
rise        = 20 ps
T0          = 20 mK
phase box   = [-4.2,+4.2)
nx          = 2048
dt          = .05 ps
tmax        = 1000 ps
```

No resistor, filter reaction coordinate, stochastic bath, measurement or readout is present. The evolution is exactly unitary within the retained one-dimensional phase model.

## Initial state

The primary initialization is a six-state thermal mixture of the converged metastable left-well DVR eigenstates,

```math
\rho_L
=\sum_n p_n|n_L\rangle\langle n_L|,
\qquad
p_n\propto e^{-(E_n-E_0)/(k_BT_0)}.
```

At `.212` the weights are

```text
p0 = 0.9909829840
p1 = 0.0089308780
p2 = 8.5259896e-5
p3 = 8.6837300e-7
p4 = 9.5246068e-9
p5 = 1.1396605e-10
```

The run also propagates three diagnostic initial states:

1. the metastable DVR ground state;
2. a pure local-harmonic ground Gaussian;
3. the historical finite-T broadened pure Gaussian.

The primary result therefore does not rely on the latter historical pure-state approximation.

## Validation workflow

```text
workflow: .github/workflows/experiment03-finite-pulse-unitary-phase.yml
run:      31973110054
head:     8aa8c77d3fc2da0467ad07d550436534bd5bbea0
status:   SUCCESS
```

Numerical quality:

```text
maximum FFT-box edge occupation = 3.301e-18
maximum norm error              = 2.478e-12
DVR initialization residual     = 1.831e-13 K
```

The large late-time occupation changes are therefore not caused by box wraparound or norm loss.

## Thermal trajectory and barrier topology

For `A=490 um^2`, the no-cooling calorimetric temperature would be

```text
T_ad = 0.37630860 K.
```

With simultaneous deposition and cooling, the actual trajectory reaches

```text
T_peak = 0.35352733 K at 66.000 ps.
```

The cold left-well fold temperature is

```text
T_f = 0.27853028 K.
```

The thermal trajectory crosses this fold upward and downward at

```text
fold annihilation:  16.024 ps
fold reformation:  380.194 ps
```

Thus the left well is absent for roughly

```text
364.17 ps.
```

## Unitary right-side occupation

The primary thermal-mixture probability `P_R=Pr[x>x_s,cold]` evolves as:

| time (ps) | T (K) | `P_R` |
|---:|---:|---:|
| 100 | 0.34730 | 0.00000098 |
| 166 | 0.32750 | 0.00819703 |
| 200 | 0.31802 | 0.08439320 |
| 300 | 0.29420 | 0.83831088 |
| 355.194 | 0.28314 | 0.97137561 |
| 380.194 | 0.27853 | 0.98696327 |
| 400 | 0.27503 | 0.99274859 |
| 405.194 | 0.27414 | 0.99374001 |
| 480.194 | 0.26210 | 0.99889733 |
| 500 | 0.25918 | **0.99922021** |
| 600 | 0.24579 | **0.81501066** |
| 800 | 0.22424 | **0.01490523** |
| 1000 | 0.20753 | **0.02402655** |

The post-reformation probability span is

```text
max(P_R)-min(P_R) = 0.98431.
```

This is the central result.

## Initialization sensitivity is much smaller than the recrossing

Across all sampled times:

```text
max |thermal DVR mixture - DVR ground|       = 0.00291
max |DVR ground - harmonic ground Gaussian| = 0.00347
max |DVR ground - legacy broadened Gaussian|= 0.00461
```

Those sub-half-percentage differences are material for final `99%` metrology, but they are negligible compared with the `98.431`-percentage-point coherent post-reformation swing.

Therefore the major missing physics is not primarily the precise cold-state mixture. It is environmental decoherence/dissipation during and after barrier reformation.

## Physical conclusion

The isolated phase coordinate **does not latch**.

The optical pulse drives the wavefunction almost completely to the right side near the moment when the cold barrier reforms, but unitary evolution subsequently carries amplitude back across the dividing surface. A snapshot near 500 ps would misleadingly suggest nearly perfect capture:

```text
P_R(500 ps)=0.99922021,
```

whereas only 300 ps later

```text
P_R(800 ps)=0.01490523.
```

Hence a final persistent-flux state cannot be defined by the photon-driven phase Hamiltonian alone.

The detector's latching operation is fundamentally an **open-system basin-selection problem**:

```text
photon pulse creates a large right-directed phase excursion
+ passive environment removes phase-space energy / destroys coherence
+ barrier reforms
-> stored basin occupation.
```

The passive environment is therefore not a perturbative correction to an otherwise complete unitary detector model. It is constitutive of the latch.

## Consequence for the current TWA certification

The `N=8192` symmetrized-FDT TWA result at `.212` remains valuable as a same-environment semiclassical screening/certification result, but it cannot be interpreted as the exact quantum efficiency.

This checkpoint strengthens that claim boundary for a second reason beyond the earlier fixed-hot quench comparison: without the environment there is not even a stable asymptotic basin probability to compare against.

## Required next calculation

The next quantum calculation must include the retained passive environment while preserving detailed balance.

The already-established reaction-coordinate Hamiltonian is

```math
H_{sys}(t)
=
\frac{Q_q^2}{2C}
+U(q,T_e(t))
+\frac{Q_\psi^2}{2C_f}
+\frac{(q-\psi)^2}{2L_f},
```

with the physical resistor bath coupled to `psi`.

The target observable is then a true reduced density-matrix basin population after reformation and dissipative settling, not a unitary snapshot probability.

## Claim boundary

This checkpoint does **not** establish that the actual bath produces high-fidelity quantum latching. It establishes the opposite logical dependency:

> Any high-fidelity latch in this architecture must be demonstrated with the bath included, because the corresponding isolated phase dynamics exhibits order-unity coherent recrossing after barrier reformation.

## Disposition

```text
ISOLATED-PHASE LATCH: NO
OPEN-SYSTEM LATCH REQUIREMENT: ESTABLISHED
PHASE-ONLY UNITARY NUMERICS: PASS
```
