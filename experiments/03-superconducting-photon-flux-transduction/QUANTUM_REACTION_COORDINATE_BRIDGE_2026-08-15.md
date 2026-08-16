# Experiment 03 — Exact Reaction-Coordinate Bridge to Nonlinear Quantum Capture

**Date:** 2026-08-15  
**Status:** model reformulation / next-solver specification; no new detector claim

## 1. Motivation

The current photon-capture screen uses a symmetrized-FDT truncated-Wigner force. The dark calculation, by contrast, uses the full passive two-pole environment in the Euclidean action and now has a calibrated one-loop prefactor away from periodic folds.

The next major physics requirement is therefore not another semiclassical noise refinement. It is a nonlinear quantum/open-system capture calculation that preserves nonsymmetrized detailed balance while using **exactly the same passive environment**.

The retained two-pole network has a natural reaction-coordinate realization that makes this possible.

## 2. Explicit circuit coordinates

Let

\[
q=\bar\Phi x
\]

be the rf-SQUID / Josephson phase-node flux coordinate and let `psi` be the internal filter-node flux.

The passive network is

```text
q node -- L_f -- psi node -- (R || C_f) -- ground.
```

Ignoring the resistor bath for one line, the two-coordinate Hamiltonian is

\[
\boxed{
H_{sys}(t)
=
\frac{Q_q^2}{2C}
+U(q,T_e(t))
+\frac{Q_\psi^2}{2C_f}
+\frac{(q-\psi)^2}{2L_f}.
}
\]

The resistor is represented as an Ohmic quantum bath coupled linearly to `psi`, with the usual counterterm / renormalization convention chosen to reproduce the physical circuit impedance.

This is not a new environment. It is an explicit-coordinate realization of the same rational positive-real admittance already used in the real-time and Euclidean calculations.

## 3. Classical elimination reproduces the retained admittance

For linear response at angular frequency `omega`, the load seen from `q` has impedance

\[
Z_{load}(\omega)
=i\omega L_f
+\frac{1}{1/R+i\omega C_f}
\]

(up to Fourier-sign convention), hence

\[
\boxed{Y(\omega)=1/Z_{load}(\omega)}.
\]

With the retained parameterization

\[
L_f=\frac{\sqrt2R}{\omega_D},
\qquad
C_f=\frac{1}{\sqrt2R\omega_D},
\]

one obtains

\[
\boxed{
\operatorname{Re}Y(\omega)
=\frac{1/R}{1+(\omega/\omega_D)^4}.
}
\]

Thus integrating out the reaction coordinate and resistor returns the exact bath topology used by the present detector model.

## 4. Quantum FDT and detailed balance

For the physical resistor bath, use the nonsymmetrized current spectra rather than replacing them by one real symmetrized stochastic force.

For `omega>0`, one consistent two-sided convention is

\[
S_{II}^{>}(\omega)
=2\hbar\omega\,[n_B(\omega)+1]\,\operatorname{Re}Y(\omega),
\]

\[
S_{II}^{<}(\omega)
=2\hbar\omega\,n_B(\omega)\,\operatorname{Re}Y(\omega),
\]

so

\[
\boxed{
\frac{S_{II}^{<}(\omega)}{S_{II}^{>}(\omega)}
=e^{-\beta\hbar\omega}.
}
\]

The corresponding symmetrized spectrum is

\[
S_{II}^{sym}(\omega)
=\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT_b}\right)
\operatorname{Re}Y(\omega),
\]

which is the spectrum used by the current TWA stress screen. The missing information in that screen is precisely the operator ordering / emission-absorption asymmetry encoded by the nonsymmetrized spectra.

For dimensionless phase `x`, the bath force couples through `q=barPhi x`, so the influence-functional spectral kernel carries the corresponding `barPhi^2` factor.

## 5. Exact influence-functional statement

Integrating out the complete linear environment gives a Feynman-Vernon influence functional for the nonlinear coordinate `q` whose real-time noise and dissipation kernels are fixed by the same `Y(omega)`.

In imaginary time, the Matsubara kernel is proportional to

\[
|\nu_n|Y_L(|\nu_n|),
\]

which is exactly the structure used in the current finite-T nonlocal Euclidean action.

Therefore the reaction-coordinate / influence-functional quantum capture model and the calibrated Euclidean dark model can be made two representations of one environment, not separately tuned approximations.

## 6. Candidate numerical routes

### Route A — reaction coordinate + quantum Brownian bath

Retain `(q,psi)` explicitly:

\[
H_{sys}(t)
=
Q_q^2/(2C)+U(q,T_e(t))
+Q_\psi^2/(2C_f)+(q-\psi)^2/(2L_f).
\]

Represent the resistor with a quantum-Brownian / HEOM-type dissipator that preserves detailed balance.

Advantages:

- the structured bath becomes local in enlarged coordinate space;
- the circuit parameters are directly physical;
- no colored classical force is introduced.

Challenge:

- the retained filter is strongly damped, so a weak-damping Lindblad oscillator is not automatically controlled.

### Route B — integrate the full bath and propagate `q` with an influence functional

Use the effective spectral density implied by `Re Y(omega)` and propagate the reduced density matrix with a numerically exact or systematically converged influence-functional method.

Advantages:

- only the nonlinear phase coordinate is retained explicitly;
- detailed balance is built into the complex bath correlation function.

Challenge:

- bath memory on the filter timescale and the long 2-ns capture horizon can make direct TEMPO/QUAPI expensive.

### Route C — controlled nonsecular master-equation benchmark

Truncate the phase Hamiltonian to a converged instantaneous/fixed basis and use the nonsymmetrized bath spectrum in a Redfield/TCL-type calculation.

This is computationally cheaper but model-dependent because the photon pulse is strongly nonadiabatic relative to the increasingly slow high-capacitance phase coordinate. It should be used as a benchmark, not silently promoted to an exact answer.

## 7. Recommended next quantum benchmark

After the safe reduced-model tilt optimum is statistically refined:

1. freeze the optimum circuit/static parameters;
2. construct a converged phase-coordinate DVR or low-energy eigenbasis spanning both cold wells and the transient barrier region;
3. verify unitary propagation for the exact time-dependent `U(q,T_e(t))`;
4. add the explicit filter reaction coordinate and check that its **classical** linear response reproduces `Y(omega)` numerically;
5. couple the filter to a detailed-balance-preserving resistor bath;
6. compare quantum basin occupation / persistent-flux probability against the sym-FDT TWA result for the same pulse;
7. vary Hilbert-space truncation, bath cutoff/representation and time step until the capture probability is numerically stable.

Only after this benchmark should the current TWA `P_final` be interpreted quantitatively.

## 8. Claim boundary

This reaction-coordinate bridge is an exact **representation of the retained linear passive environment**, not a claim that a particular finite-dimensional master equation is exact.

Do not claim that:

- a Lindblad treatment of the resistor is automatically controlled;
- the current sym-FDT TWA already preserves detailed balance;
- the reduced 14-um capture probability is the physical quantum efficiency.

The useful result is narrower:

> The same two-pole environment used in the real-time and Euclidean detector calculations admits an explicit circuit-coordinate Hamiltonian. This provides a direct route to a detailed-balance-preserving nonlinear quantum capture calculation without changing the environment between the signal and dark problems.
