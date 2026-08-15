# Exact Closed-System Quantum Quench Benchmark — 2026-08-15

## Purpose

Test the current truncated-Wigner / classical-trajectory approximation in a controlled nonlinear subproblem before adding an open electromagnetic environment.

The benchmark is intentionally simpler than the full detector:

```text
cold harmonic ground-state Gaussian
-> instantaneous quench to a fixed hot nonlinear rf-SQUID potential
-> no damping
-> no cooling
-> compare exact Schrodinger propagation against classical propagation of the same cold Wigner distribution.
```

The measured benchmark observable is the probability that the phase coordinate lies to the right of the retained hot saddle at a specified time.

This is **not** the final persistent-flux capture probability.

## 1. Why this benchmark is required

The current basin-probability calculation samples the exact harmonic Wigner state at `t=0` but evolves samples using the classical nonlinear RCSJ map. For a closed nonlinear Hamiltonian,

```math
\partial_tW
=-\frac{p}{m}\partial_xW
+U'\partial_pW
-\frac{\hbar^2}{24}U'''\partial_p^3W
+O(\hbar^4).
```

The sampled-trajectory calculation omits the Moyal terms. Since the current cold action scale is only `DeltaU/(hbar omega_c)~5.3`, a percent-level check is necessary.

## 2. Canonical code and workflow

```text
calculations/quantum_quench_benchmark.py
.github/workflows/experiment03-quantum-quench.yml
```

The quantum calculation uses split-operator FFT evolution with physical phase mass

```math
m_x=C\bar\Phi^2,
\qquad
\bar\Phi=\Phi_0/(2\pi),
```

and physical potential obtained from the same full-CPR force used in the deterministic solver.

The classical comparison uses vectorized Hamiltonian propagation initialized from the same Gaussian Wigner covariance.

Benchmark hot temperature:

```text
T_hot = T_q + 0.030 K
```

while retaining a finite hot saddle.

## 3. Quick-grid regression

Workflow run:

```text
31909432077
```

showed maximum exact-quantum vs TWA probability differences of order a few percentage points, motivating a finer run rather than indicating catastrophic failure.

## 4. Finer benchmark

Workflow run:

```text
31909516856
```

completed successfully.

### rDelta = 0.8

| time | exact quantum | classical Wigner | exact - TWA |
|---:|---:|---:|---:|
| 5 ps | 0.000500 | 0.000500 | ~0.000000 |
| 10 ps | 0.029397 | 0.034758 | -0.005361 |
| 20 ps | 0.591964 | 0.552583 | +0.039381 |
| 30 ps | 0.835370 | 0.812208 | +0.023162 |
| 40 ps | 0.879503 | 0.853525 | +0.025978 |

### rDelta = 0.6

| time | exact quantum | classical Wigner | exact - TWA |
|---:|---:|---:|---:|
| 5 ps | 0.000252 | 0.000267 | -0.000015 |
| 10 ps | 0.012294 | 0.015225 | -0.002931 |
| 20 ps | 0.431316 | 0.404842 | +0.026475 |
| 30 ps | 0.798562 | 0.775217 | +0.023346 |
| 40 ps | 0.877621 | 0.865683 | +0.011938 |

## 5. Interpretation

Three conclusions are justified.

### A. Truncated-Wigner does not catastrophically fail in this benchmark

The classical-Wigner and exact wavepacket probabilities follow the same broad time evolution over the retained 40-ps interval.

Therefore the present semiclassical basin calculations remain useful for architectural screening and for locating operating regions.

### B. Percent-level fidelity is not controlled by truncated-Wigner

Differences reach approximately

```text
3.94 percentage points at 20 ps for rDelta=.8
2.65 percentage points at 20 ps for rDelta=.6.
```

Those errors are material if the desired detector efficiency is `>=0.99`.

### C. The correction is not a one-sign “extra tunneling” effect

At 10 ps the exact probability is slightly **lower** than the classical-Wigner result, whereas at 20–40 ps it is generally higher.

Thus it is not defensible to correct the semiclassical detector efficiency by simply adding a quantum-tunneling probability. Interference, wavepacket deformation and nonlinear quantum transport contribute to the difference.

## 6. Boundary of this result

The benchmark is closed-system and fixed-hot. It does not include

```text
finite optical rise,
cooling,
dissipative environment,
FDT noise,
dissipative MQT,
final cold-basin retrapping,
readout.
```

It therefore quantifies only the **nonlinear closed-phase quantum correction** to the launch/crossing subproblem.

The final detector needs an open-system quantum treatment using the same physical environment for damping, fluctuations and cold quantum escape.

## 7. Consequence for current probability numbers

The converged initial-Wigner basin probabilities in `INITIAL_WIGNER_CAPTURE_CHECKPOINT_2026-08-15.md` should be described as

```text
semiclassical initial-state capture probabilities
```

not exact quantum efficiencies.

They can rank candidate dynamical regions, but a `0.99` semiclassical result is not sufficient to claim `99%` detector efficiency.

## 8. Next quantum step

A controlled progression is:

1. refine the scalar-R semiclassical probability optimum;
2. add an Ohmic fluctuation-dissipation-consistent bath and compare against the closed-system benchmark;
3. use an open-system quantum method appropriate to the nonlinear phase degree of freedom and moderate damping;
4. then replace scalar Ohmic damping with causal colored `Y(omega)`.

The exact method for Step 3 must be chosen with care; a simple classical white-noise Langevin equation is not controlled because `hf/k_B` is comparable to the hot/fold temperature.

## Status

**GO for continued theory. NO-GO for manuscript.**
