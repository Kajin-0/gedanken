# Experiment 03 — Environment / Quantum-Dynamics Literature Ledger — 2026-08-15

This file records literature collisions and modeling guidance for the causal-environment stage. It supplements the earlier Experiment-03 literature ledgers.

## A. Frequency-dependent Josephson damping is established

### Stornaiuolo et al., Phys. Rev. B 87, 134517 (2013)

**Title:** Resolving the effects of frequency-dependent damping and quantum phase diffusion in YBa2Cu3O7-x Josephson junctions  
**DOI:** 10.1103/PhysRevB.87.134517

Primary relevance:

- analyzes Josephson phase dynamics with frequency-dependent damping;
- uses a two-quality-factor model to fit device behavior;
- explicitly connects environmental damping structure to quantum phase diffusion.

**Collision implication:** replacing a scalar resistor by a frequency-dependent environment is established Josephson physics. Experiment 03 cannot claim novelty from colored damping itself.

The role here is narrower: determine whether a single-photon, nonadiabatic persistent-flux latch has any causal environment that simultaneously satisfies launch, capture, fluctuation-dissipation and dark-escape constraints.

## B. Exact phase-space stochastic mapping for quadratic quantum Brownian motion

### Kondaurov and Polyakov, Phys. Rev. A 114, 012213 (2026)

**Title:** Quantum Brownian motion as a classical stochastic process in phase space  
**DOI:** 10.1103/32jw-91ck

Primary result relevant to Experiment 03:

- for the Caldeira-Leggett model with an external potential at most quadratic, the exact quantum dynamics can be represented as a classical non-Markovian stochastic process in phase space;
- correlated system-bath thermal equilibrium is treated explicitly;
- arbitrary system preparations can be incorporated through Wigner-function statistical weights;
- for more general smooth nonlinear potentials, the paper identifies a route toward controlled approximation rather than claiming exact classical propagation.

**Experiment-03 implication:** the cold linearized well and its causal-bath covariance can be treated substantially more rigorously than the nonlinear switching event. This reinforces the current hierarchy:

```text
cold harmonic state + linear bath -> exact/controlled open-system treatment available;
nonlinear photon-driven barrier crossing -> requires explicit quantum/open-system validation.
```

This is consistent with the Experiment-03 exact-quench benchmark, where truncated-Wigner propagation differed from exact closed-system quantum evolution by several percentage points in the nonlinear crossing regime.

## C. Dissipative Josephson modeling requires environmental consistency

The established Caldeira-Leggett / Ambegaokar-Eckern-Schon framework remains the foundational boundary:

```text
the same environmental spectral density that produces damping also produces fluctuations and modifies quantum tunneling/escape.
```

Experiment 03 therefore forbids the following inconsistent workflow:

```text
choose R for deterministic capture
+
add an unrelated noise model
+
use a nondissipative MQT formula independently.
```

The next physical model must instead use one causal `Y(omega)` / spectral density throughout.

## D. Current modeling consequence

The one-pole Drude environment

```math
Y(\omega)=\frac{G_0}{1-i\omega/\omega_D}
```

is retained only as the **minimal causal regularization**, not as a novelty claim or final circuit design.

It is useful because:

```text
1. ReY rolls off at high frequency;
2. the momentum/velocity variance becomes finite;
3. the memory kernel is represented by one auxiliary current state;
4. the scalar-R limit is recovered as omega_D -> infinity;
5. the same Y(omega) can later feed FDT noise and dissipative escape calculations.
```

## E. Novelty boundary after this search

Closed as novelty claims:

```text
frequency-dependent Josephson damping;
quantum phase diffusion from a dissipative environment;
non-Markovian phase-space stochastic descriptions of linear quantum Brownian motion;
generic bath-induced modification of tunneling.
```

The only possible contribution remains detector-specific and conjunctive:

```text
single absorbed LWIR photon
+ proximity-JJ nonadiabatic potential change
+ causal quantum environment
+ finite probability of capture into persistent flux
+ cold dark-stability constraint
+ explicit spectral/rise-time/readout closure.
```

No priority claim is authorized.
