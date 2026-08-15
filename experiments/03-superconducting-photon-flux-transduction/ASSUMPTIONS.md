# Experiment 03 — ASSUMPTIONS

These assumptions define the current exploratory model. They are expected to change and must not be silently broadened.

## Optical / thermal

- Primary target band: 8–14 µm, with 10 µm used for numerical checkpoints.
- Photon absorption may create quasiparticles / hot electrons; sub-gap absorption is not required.
- The absorber may be much smaller than the optical collection aperture if antenna/cavity coupling is used.
- Initial calorimetric treatment assumes absorbed energy thermalizes rapidly enough to define an effective electronic temperature `T_e(t)`. This must be checked against electron-electron, diffusion and electron-phonon times for the eventual platform.
- The rough `15.5 µm^2` graphene area scaling is not a device design. Wavelength-dependent absorption, proximity electrodes, doping, heat capacity and diffusion are not yet included.

## Generation-A superconducting circuit

- The first exact model is a single-junction rf-SQUID with a sinusoidal current-phase relation.
- Write `phi_x = pi + delta` and `x = phi-pi`; the dimensionless potential is

```math
u(x)=\frac12(x-\delta)^2+\beta\cos x,
\qquad
\beta=\frac{2\pi L I_c}{\Phi_0}.
```

- `delta>0` is a deliberately applied external-flux tilt used only for the Generation-A proof architecture.
- The photon transducer is assumed to reduce `I_c[T_e(t)]`, and hence `beta(t)`, during the hot pulse.
- The preferred trigger criterion is crossing the static saddle-node `beta_c(delta)`, not assuming a fixed hot barrier.
- The exact static saddle-node is defined by `delta = tan(a)-a`, `beta_c=sec(a)`.
- The static condition `beta_cold > beta_c > beta_hot` is necessary for barrier annihilation in the simple model but is not sufficient to prove high-fidelity dynamic capture.
- A real graphene/proximity junction can have a nonsinusoidal current-phase relation; replacing the sinusoidal CPR is a required robustness test before strong claims.
- Loop inductance is initially treated as lumped and temperature-independent during the write pulse.

## Dynamics / damping

- The first deterministic diagnostic uses an RCSJ-like equation with effective capacitance `C` and effective hot-state resistance `R_eff`.
- The hot write state is allowed to be dissipative. Persistent cold storage need not retain the same conductance or damping.
- The simple damping time `~2 R_hot C` is only an envelope scale.
- Dynamic saddle-node delay, finite-rate passage, noise-induced trajectories, retrapping and wrong-way capture are not yet solved.
- The phase-motion timescale being much shorter than the thermal pulse in one benchmark does not by itself establish deterministic detection.

## Noise / dark events

- Ordinary Johnson noise of an ideal storage channel is not the only or necessarily dominant false-event mechanism.
- Thermal activation and MQT must be treated separately from photon-triggered dynamics.
- The provisional MQT expression with exponent `7.2 DeltaU/(hbar omega_p)` is a diagnostic scaling imported from cubic-barrier Josephson escape, not an exact rf-SQUID DCR.
- Dissipative MQT action/prefactor, flux noise, residual quasiparticles, vortices, stray optical photons, readout backaction and cosmic/environmental events remain to be added before performance claims.

## Readout

- Adjacent fluxoid states are not assumed to differ in measured loop flux by exactly `Phi0`.
- The readout signal must be computed from the actual stationary points:

```math
\Delta\Phi=\frac{\Phi_0}{2\pi}(x_2-x_1).
```

- Persistent flux can in principle be measured with a SQUID or equivalent superconducting readout.
- Readout noise is initially separated from intrinsic switching physics; total system performance must eventually include it.

## Reset

- A persistent flux state does not passively reset in the ideal storage limit.
- Reset may require an active flux/current/critical-current pulse or controlled barrier modification.
- Reset energy, reset-induced errors and dead time must eventually be included.

## Prior-art / terminology boundaries

Do not claim novelty for:

- superconducting MIR/LWIR single-photon detection;
- photon-triggered graphene/Josephson thermal switching;
- single-photon-to-persistent-single-flux superconducting memory;
- optical creation of persistent superconducting flux/vortices;
- transient `I_c` suppression to lower an rf-SQUID barrier and then refreeze a flux state;
- superconducting/Josephson diode effects;
- illumination-driven superconducting phase batteries or vorticity switching.

Do not call Generation A photovoltaic: it uses an externally applied flux tilt.

## Scope exclusions for the current model

Do not currently claim:

- room-temperature operation;
- zero total noise or zero dark counts;
- zero dissipation during photon absorption;
- demonstrated deterministic one-photon/one-flux conversion in this architecture;
- unit optical absorptance;
- superiority to SNSPD, KID, graphene-JJ or existing single-photon-single-flux platforms;
- novelty;
- a publication-ready theorem.

The next task is to determine whether a realistic `T_e(t) -> I_c[T_e(t)] -> beta(t)` pulse can cross the bifurcation and settle with high fidelity while the cold-state escape rate remains acceptably low.