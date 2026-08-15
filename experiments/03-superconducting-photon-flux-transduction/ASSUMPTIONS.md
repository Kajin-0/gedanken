# Experiment 03 — ASSUMPTIONS

These assumptions define the current exploratory model. They are expected to change.

## Optical

- Primary target band: 8–14 µm, with 10 µm used for numerical checkpoints.
- Photon absorption may create quasiparticles / hot electrons; sub-gap absorption is not required.
- The absorber may be much smaller than the optical collection aperture if antenna/cavity coupling is used.
- Initial calorimetric scaling assumes absorbed energy thermalizes rapidly enough to define an effective electronic temperature `T_e(t)`. This must be checked for the eventual material/platform.

## Superconducting circuit

- A hysteretic loop can support metastable fluxoid states.
- The photon-sensitive element modulates `I_c`, phase bias, or the effective phase potential strongly enough to alter escape probabilities during the optical transient.
- Persistent storage occurs after the nonequilibrium excitation relaxes.
- Generation-A calculations may use nonzero external flux bias. Zero-bias self-directionality is not assumed until a concrete phi0/diode mechanism is modeled.

## Noise / stochastic dynamics

- Ordinary Johnson noise of an ideal storage channel is not the only or necessarily dominant false-event mechanism.
- Thermal activation and MQT must be treated separately.
- The provisional MQT formula with exponent `7.2 DeltaU/(hbar omega_p)` is a scaling placeholder, not an exact result for arbitrary rf-SQUID damping or barrier geometry.
- Stray optical photons, residual quasiparticles, vortices, readout backaction, flux noise and cosmic/environmental events are outside the first minimal model but must be added before performance claims.

## Readout

- Persistent flux can in principle be measured with a SQUID or equivalent superconducting readout.
- Readout noise is initially separated from intrinsic detector switching physics; total system sensitivity must eventually include it.

## Reset

- A perfectly isolated persistent flux state does not passively reset.
- Reset may require an active pulse or controlled barrier modification. Reset energy/noise/dead time must eventually be included.

## Scope exclusions for the first model

Do not initially claim:

- room-temperature operation;
- zero total noise;
- zero dark counts;
- zero dissipation during photon absorption;
- deterministic one-photon/one-flux conversion;
- unit optical absorptance;
- superiority to SNSPD/KID/Josephson-calorimeter platforms;
- photovoltaic classification at zero bias;
- novelty.

The first task is only to determine whether a physically plausible parameter region exists once the time-dependent stochastic dynamics are treated consistently.
