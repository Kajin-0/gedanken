# Experiment 03 — Open-System Quantum Method Gate — 2026-08-16

## Purpose

Select a quantitatively controlled quantum-open-system route for the next stage of Experiment 03.

The reduced model has reached the point where a convenient Markov master equation would be easy to write but scientifically dangerous. This checkpoint records the numerical gates that constrain the method choice and defines what must be validated before an open-system basin probability can be called a quantum result.

## 1. Why the open system is not optional

The finite-rise/cooling isolated-phase benchmark at the certified `.212`, `A=490 um^2`, `lambda=14 um` point is numerically converged and shows order-unity coherent recrossing after the barrier reforms.

Key results:

```text
fold annihilation  = 16.024 ps
fold reformation   = 380.194 ps
P_R(500 ps)        = 0.99922021
P_R(600 ps)        = 0.81501066
P_R(800 ps)        = 0.01490523
P_R(1000 ps)       = 0.02402655
post-reform span   = 0.98431
max box edge prob  = 3.301e-18
max norm error     = 2.478e-12
```

Thus the optical pulse does not by itself create a quantum latch. Environmental energy removal/decoherence during reformation is constitutive of the stored-basin outcome.

See `FINITE_PULSE_UNITARY_PHASE_CHECKPOINT_2026-08-16.md`.

## 2. Weak-coupling/secular control parameters are not small

At the certified `.212` point:

```text
C = 24.262211 pF
R = 7.5308506 ohm
f_c = 1.9844267 GHz
f_D = 1.7859840 GHz
```

The explicit two-pole realization has

```text
L_f = 0.949077372 nH
C_f = 8.367264980 pF
filter damping ratio zeta = 0.70710678
filter Q = 0.70710678
filter amplitude decay time = 126.010 ps
```

The small-amplitude phase damping inferred from `ReY(omega_c)` is

```text
gamma_phase,amp / omega_c = 0.08690185
phase amplitude decay time = 0.92279 ns
phase energy decay time    = 0.46140 ns
```

The coupled cold phase+filter Hamiltonian has normal modes

```text
f1 = 1.42306755 GHz    gamma1/omega1 = 0.63976325
f2 = 2.49050333 GHz    gamma2/omega2 = 0.14098524
```

and

```text
Delta omega / (gamma1+gamma2) = 0.84518196.
```

The mode splitting is therefore not parametrically larger than the damping scale. A secular global-Davies reduction is not controlled by a large separation parameter.

The optical rise is also strongly nonadiabatic:

```text
omega_c tau_r = 0.24937046
tau_r / T_phase = 0.0396885.
```

Therefore neither a local filter Lindblad model nor a secular instantaneous-eigenbasis master equation is authorized as the quantitative completion.

## 3. Bare-Gibbs equilibrium is not exact even in the UV-safe coordinate sector

The exact cold quantum-FDT covariance of the linear damped circuit was compared with the Gibbs state of the bare coupled phase+filter Hamiltonian.

The filter momentum/voltage variable is excluded from this comparison because its ideal-Ohmic zero-point variance is UV divergent; see Sec. 4.

For the finite `[x,y,u]` sector,

```text
sigma_x bare Gibbs = 3.997064491e-2
sigma_x exact FDT  = 3.989969857e-2
relative sigma_x   = -0.001775

sigma_y bare Gibbs = 7.780719854e-2
sigma_y exact FDT  = 7.165064817e-2
relative sigma_y   = -0.079126

sigma_u bare Gibbs = 4.251634209e-2
sigma_u exact FDT  = 4.264669021e-2
relative sigma_u   = +0.003056
```

The UV-safe covariance-block relative Frobenius mismatch is

```text
0.160154.
```

This is another warning that a weak-coupling model whose stationary state is the bare Gibbs state is not an exact representation of the current bath coupling.

## 4. Explicit reaction-coordinate + ideal Ohmic resistor has a quantum UV incompleteness

The classical/linear reaction-coordinate realization

```math
H_{sys}(t)
=
\frac{Q_q^2}{2C}+U(q,T_e(t))
+\frac{Q_\psi^2}{2C_f}
+\frac{(q-\psi)^2}{2L_f}
```

correctly reproduces the causal port admittance when the filter coordinate and resistor bath are eliminated.

However, treating the residual resistor as ideal Ohmic to arbitrarily high frequency is not sufficient to define every quantum reaction-coordinate moment.

The exact FDT covariance was integrated while varying the residual upper cutoff by many e-folds. The physical phase and filter-coordinate moments converge:

```text
relative change ymax=20 -> 24:
sigma_x : 1.15e-14
sigma_y : 9.15e-13
sigma_u : 1.14e-14
```

but the filter velocity / capacitor-voltage variance obeys a logarithmic UV tail:

```text
Var(s) tail slope per ln(omega_max) = 3.781061935e-3
linear-tail relative residual       = 1.793879e-13
sigma_s(ymax=24)/sigma_s(ymax=16)  = 1.223233.
```

Therefore an explicit reaction-coordinate quantum calculation requires a physically justified microscopic residual-bath cutoff and a cutoff-sensitivity study. The ideal resistor is adequate for the effective low-frequency port response but does not define a cutoff-independent internal momentum variance.

This does **not** invalidate the causal two-pole admittance used by the phase coordinate. It restricts how the auxiliary circuit may be quantized.

## 5. Direct effective port bath is UV regular

For the phase coordinate the relevant equilibrium force/current correlation is defined directly by

```math
S_I^{sym}(\omega)
=\hbar|\omega|\coth\!\left(\frac{\beta\hbar|\omega|}{2}\right)
\operatorname{Re}Y(\omega),
```

with

```math
\operatorname{Re}Y(\omega)
=\frac{G}{1+(\omega/\omega_D)^4}.
```

Define the positive-frequency bosonic spectral density in physical force units by

```math
J_I(\omega)=\hbar\,\omega\operatorname{Re}Y(\omega),
```

or, for the dimensionless phase coupling used in an `hbar=1` solver,

```math
J_x(\omega)
=\frac{\bar\Phi^2}{\hbar}\omega\operatorname{Re}Y(\omega).
```

At high frequency this decays as `omega^-3`, so the phase bath correlation is UV convergent.

The exact unsymmetrized correlation for `t>0` has two complex circuit poles plus Matsubara poles. At `.212`:

```text
omega_D/2pi = 1.7859840 GHz
nu_1/2pi    = 2.6184068 GHz
nu_1/omega_D = 1.46608634
1/nu_1      = 60.7831 ps
circuit-pole decay time = 126.0252 ps
```

The analytic residue expansion has been independently validated against direct oscillatory quadrature:

```text
max relative quadrature disagreement = 9.311e-7
KMS detailed-balance max relative error = 2.023e-16
```

Plain Matsubara truncation errors:

```text
N=8:  t=0    3.373e-3
      t=20ps 7.877e-5

N=16: t=0    8.974e-4
      t=20ps 9.990e-7

N=32: t=0    2.315e-4
      t=20ps 8.037e-10
```

This provides an auditable exponential bath decomposition suitable for HEOM or an equivalent Feynman-Vernon influence-functional solver.

## 6. Literature/method basis

The selected route is standard in open-system methodology, not a novelty claim.

Primary references supporting the method class include:

- Y. Tanimura, *Numerically exact approach to open quantum dynamics: The hierarchical equations of motion (HEOM)*, J. Chem. Phys. **153**, 020901 (2020), DOI `10.1063/5.0011599`.
- L. Cui et al., *Efficient hierarchical equations of motion method for coherent dynamics in dissipative systems*, Fano-spectrum-decomposition work, J. Chem. Phys. **151**, 024110 (2019), DOI `10.1063/1.5092616`.
- M. Xu et al., low-temperature optimized quantum-noise decomposition / HEOM work, arXiv:`2202.04059`.

The project may use QuTiP as an implementation/checking layer, but the physics acceptance criteria are independent of any library.

## 7. Canonical method decision

### Rejected as quantitative final model

```text
local filter Lindblad
secular global Davies / instantaneous-eigenbasis Lindblad
bare-Gibbs weak-coupling closure
explicit reaction coordinate with ideal Ohmic residual bath and no UV cutoff
bath-free unitary snapshot probability
```

These may remain diagnostics or limiting models, but they cannot carry the final quantum-efficiency claim.

### Selected next route

```text
direct UV-regular effective port spectral density
-> exact/exponentially converged equilibrium correlation
-> HEOM / Feynman-Vernon non-Markovian dynamics
-> same time-dependent full-CPR phase Hamiltonian
-> metastable left-well conditioned initial state
-> final basin probability only after dissipative settling
```

## 8. Mandatory validation ladder

No nonlinear quantum capture number is canonical until all gates below pass.

### Gate A — bath correlation

**PASS.** Residue/Matsubara expansion agrees with independent quadrature and detailed balance.

### Gate B — cold harmonic equilibrium

**IN PROGRESS.** A direct-port HEOM calculation must reproduce the independently known exact quantum-FDT phase covariance at `.212`, including the Caldeira-Leggett quadratic counterterm that preserves the measured/static potential.

Required convergence axes:

```text
Hilbert dimension
hierarchy depth
Matsubara / rational-decomposition order
counterterm control
```

### Gate C — nonlinear static equilibrium / metastable local state

After Gate B, increase from harmonic to the cold nonlinear phase Hamiltonian and verify local-well moments / conditioned metastable preparation against the converged DVR basis.

### Gate D — finite-pulse open-system dynamics

Propagate the actual 20-ps deposition + cooling pulse and demonstrate convergence in hierarchy depth, bath decomposition and phase basis.

### Gate E — TWA comparison

Only then compare the exact/open-system final basin population with the existing `N=8192` symmetrized-FDT TWA certification.

The difference, not the TWA number alone, determines whether the reduced model supports a high-fidelity quantum latch.

## 9. Current claim boundary

The current project may state:

> The same passive environment required for classical basin capture admits a UV-regular direct-port quantum spectral density with an independently validated equilibrium correlation decomposition. The isolated phase coordinate does not latch, and weak-coupling/secular Markov reductions lack clean control parameters at the certified operating point. A non-Markovian HEOM/influence-functional calculation is therefore the next required quantum gate.

Do **not** state exact quantum efficiency until Gates B-E are complete.
