# Experiment 03 — Quantum / Causal-Environment Checkpoint — 2026-08-15

## Current mechanism

Experiment 03 remains a **photon-triggered nonadiabatic metastable superconducting flux latch**. Generation A uses external flux tilt and is not photovoltaic.

The current strongest chain is

```text
single absorbed LWIR photon
 -> rapid local electronic heating / CPR change
 -> nonlinear phase acceleration across a time-dependent barrier
 -> target-basin transfer
 -> recovery of the cold double-well
 -> persistent right-flux capture.
```

Static fold disappearance remains only the quasistatic organizing limit.

## 1. Deterministic capture was superseded by basin probability

The correct semiclassical initial-state quantity is

```math
P_{cap}^{init}
=\iint_{\Omega_R^0}\rho_W(x,v)\,dx\,dv,
```

where `Omega_R^0` is the target basin pulled back through the nonlinear pulse dynamics.

The cold harmonic phase mode is deep in the quantum regime and has approximately

```text
sigma_x ~0.115 rad.
```

Geometry-aware basin-strip integration replaced tensor Gauss-Hermite sampling because the basin indicator is folded/discontinuous.

Validated examples:

```text
rDelta=0.6, rise=20 ps, R=75 ohm  -> P~0.81377
rDelta=0.6, rise=20 ps, R=120 ohm -> P~0.96640
rDelta=0.8, rise=5 ps,  R=300 ohm -> P~0.76774.
```

## 2. Coarse >99% corridor weakened under refinement

A coarse scalar-R damping scan suggested

```text
rDelta=0.6, rise=20 ps:
R=160 ohm -> P~0.9927
R=250 ohm -> P~0.9935
R=400 ohm -> P~0.9896.
```

Higher-resolution nested x integration corrected these to approximately

```text
R=160 ohm -> 0.98012
R=250 ohm -> 0.99009
R=400 ohm -> 0.98707.
```

Therefore `P>0.99` is **not yet established**. At `R=250 ohm`, the `nx=17 -> 33` shift remained about `+0.0063`, so a deeper `nx=65` refinement was launched:

```text
calculations/quantum_optimum_deep_refine.py
.github/workflows/experiment03-quantum-optimum-deep.yml
```

Do not treat the previous `0.9935` scouting value as a physical fidelity result.

## 3. Exact closed-system quantum benchmark

A fixed-hot sudden-quench benchmark now compares exact split-operator Schrodinger evolution with classical propagation of the same initial harmonic Wigner distribution.

Representative refined discrepancies:

```text
rDelta=0.8, t=20 ps: P_Q~0.59196, P_TWA~0.55258, delta~+0.03938
rDelta=0.6, t=20 ps: P_Q~0.43132, P_TWA~0.40484, delta~+0.02648.
```

The correction changes sign at early time.

**Conclusion:** truncated-Wigner/classical propagation is useful for architecture screening but cannot certify percent-level detector efficiency in the nonlinear crossing regime.

Canonical files:

```text
calculations/quantum_quench_benchmark.py
EXACT_QUANTUM_QUENCH_CHECKPOINT_2026-08-15.md
```

## 4. Quantum localization-speed-signal identity

For the harmonic cold mode,

```math
\boxed{
\sigma_x^2\tau_0\Delta I
=\frac{2\pi e\zeta}{\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT}\right)
},
```

with `tau0=1/omega_c` and `DeltaPhi=zeta Phi0`.

At 20 mK the coth factor is effectively unity.

Thus localization, phase speed and persistent current separation cannot all be scaled independently.

Canonical record:

```text
QUANTUM_SPEED_SIGNAL_CLOSURE_2026-08-15.md
```

## 5. Infinite-bandwidth Ohmic bath rejected as final model

Quantum FDT requires

```math
S_I^{sym}(\omega)
=\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT_{bath}}\right)
\operatorname{Re}Y(\omega).
```

For an ideal Ohmic bath, the cold coordinate variance converges but the velocity/momentum variance diverges logarithmically in the ultraviolet.

Therefore an infinite-bandwidth scalar resistor cannot define the physical quantum phase-space state required for the probability calculation.

## 6. Minimal causal bath: one-pole Drude admittance

Retain provisionally

```math
Y(\omega)
=\frac{G_0}{1-i\omega/\omega_D},
```

with time-domain auxiliary state

```math
LC\ddot x+Lj+F(x,T)=0,
```

```math
\tau_D\dot j+j=G_0\dot x,
\qquad \tau_D=1/\omega_D.
```

This is a minimal physical regularization, not a final circuit design or novelty claim.

Damping-retention rule:

```math
\boxed{
\frac{\omega_D}{\omega_c}
\ge\sqrt{\frac{\eta}{1-\eta}}
}
```

for retaining fraction `eta=ReY(omega_c)/G0`.

Hence

```text
95% damping retention -> omega_D/omega_c >=4.36
99% retention         -> >=9.95.
```

For current `27–32 GHz` phase modes, first-pass cutoffs are roughly `130–320 GHz`.

## 7. Drude cold covariance

For `rDelta=0.6`, `R0=250 ohm`:

```text
d=omega_D/omega_c=2:
  ReY/G0=0.8000
  var_x/isolated=0.97839
  var_v/isolated=1.05870

d=5:
  ReY/G0=0.96154
  var_x/isolated=0.97328
  var_v/isolated=1.09859

d=10:
  ReY/G0=0.99010
  var_x/isolated=0.97066
  var_v/isolated=1.13563.
```

A causal bath redistributes the reduced-state fluctuations; it does not simply narrow the Wigner cloud.

Canonical record:

```text
DRUDE_BATH_CUTOFF_CLOSURE_2026-08-15.md
calculations/drude_bath_variance.py
```

## 8. Causal deterministic propagation survives

Full nonlinear Drude-center dynamics was evaluated for

```text
rDelta=0.6
rise=20 ps
R0=160–400 ohm
omega_D/omega_c=2,5,10,20.
```

Every tested center trajectory transferred to the right state.

A longer persistence diagnostic then evaluated `R0={160,250,400} ohm`, `d={5,10}` through 10 ns. All six cases were on the right side and below the cold separatrix energy already at 0.8 ns and remained trapped while cooling.

Thus causal memory/reactive loading does **not** destroy deterministic persistent capture in the tested neighborhood.

Canonical calculations:

```text
calculations/drude_dynamic_center.py
calculations/drude_settle_check.py
```

## 9. Bath and weak-link temperatures must be separated

Do not substitute the photon-heated electronic temperature into FDT automatically.

```text
T_e(t)    -> controls CPR / Josephson force / calorimetric pulse
T_bath(t) -> controls equilibrium bath fluctuations.
```

For an external cold shunt, `T_bath` can remain near 20 mK while `T_e` reaches ~0.6–0.8 K.

At 27–32 GHz and 20 mK, the quantum/classical FDT factor is about `32–38`, so classical Johnson noise is badly inadequate at the phase frequency.

## 10. Damping-noise-persistent-signal identity

Define the local quality factor

```math
Q_c=\frac{\omega_c C}{\operatorname{Re}Y(\omega_c)}.
```

Using

```math
\omega_c^2=\frac{\kappa_c}{LC},
\qquad
\Delta I=\frac{\zeta\Phi_0}{L},
```

and quantum FDT yields

```math
\boxed{
\frac{S_I^{sym}(\omega_c)}{\Delta I}
=
\frac{e\kappa_c}{\pi\zeta Q_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_{bath}}\right)
}.
```

In the deep quantum regime,

```math
\boxed{
\frac{S_I^{sym}(\omega_c)}{\Delta I}
\to
\frac{e\kappa_c}{\pi\zeta Q_c}.
}
```

At fixed normalized topology and required `Q_c`, the zero-point bath-noise spectral density per persistent-current separation is independent of `L`, `C` and `omega_c` separately.

If nonlinear capture imposes `Q_c <= Qmax`, then it automatically imposes a minimum dynamic noise-to-signal scale.

Canonical record:

```text
DAMPING_NOISE_SIGNAL_IDENTITY_2026-08-15.md
```

## 11. Literature boundary strengthened

Frequency-dependent Josephson damping and quantum phase diffusion are established prior art (e.g. Stornaiuolo et al., PRB 87, 134517 (2013)).

Kondaurov and Polyakov, PRA 114, 012213 (2026), show an exact classical non-Markovian phase-space stochastic representation for Caldeira-Leggett quantum Brownian motion with at-most-quadratic external potential, reinforcing the distinction between the tractable cold harmonic state and the nonlinear switching event.

Canonical record:

```text
LITERATURE_LEDGER_ENVIRONMENT_2026-08-15.md
```

## 12. Immediate frontier

The theory is no longer blocked by deterministic causal capture. The critical remaining steps are:

```text
1. finish deep scalar-R basin convergence near R~250 ohm;
2. quantify causal-Drude change in pulled-back basin volume while holding the initial cloud fixed (propagator-only stress);
3. construct the correlated equilibrium state of the causal bath + phase mode;
4. propagate with the same bath's FDT noise during the pulse;
5. replace truncated-Wigner nonlinear propagation by an explicit open-system quantum benchmark where fidelity matters;
6. use the identical spectral density in dissipative dark-escape/MQT;
7. only then quote physical P_capture / P_wrong / dark-count operating regions.
```

A propagator-only Drude basin workflow has been added:

```text
calculations/drude_basin_geometry.py
.github/workflows/experiment03-drude-basin.yml
```

It deliberately reuses the isolated `(x,v)` Gaussian and sets `j0=0`; therefore it isolates the effect of causal propagation and is **not** a detector efficiency estimate.

## Verdict

**GO for continued theory. NO-GO for manuscript.**

The architecture remains alive after causal deterministic damping. The dominant uncertainty is now genuinely quantum/open-system: the bath-consistent initial state, stochastic pulse-time fluctuations, nonlinear quantum corrections and dissipative dark escape.
