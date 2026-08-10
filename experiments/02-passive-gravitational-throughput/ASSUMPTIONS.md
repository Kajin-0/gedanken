# Assumptions and Scope — Experiment 02

These assumptions define the theorem currently established in the repository. They are part of the claim boundary, not optional prose.

## Included theorem class

- weak linearized gravity on an approximately flat background;
- nonrelativistic endpoint matter;
- leading mass-quadrupole coupling;
- passive, linear, time-invariant endpoint dynamics;
- complex-envelope operation about absolute carrier angular frequency `omega_0`;
- envelope bandwidth `B/omega_0 << 1`;
- characteristic endpoint radii `a_A,a_B` satisfying `k_0 a_A,k_0 a_B << 1`, with `k_0=omega_0/c`;
- endpoint separation satisfying `k_0 R >> 1`;
- finite or countably infinite separable modal sectors with bounded Markov port operators;
- retained endpoint physical modal frequencies satisfying

```text
omega_n <= Omega,
Omega = omega_0[1+O(B/omega_0)]
```

when the simple carrier-scale `omega_0^4` gravitational endpoint resource is used;
- arbitrary passive internal unitary mode mixing within the retained sector;
- all unobserved loss/radiation channels retained in the passive model rather than silently discarded;
- same-two-endpoint passive gravitational recurrence when `p_+ p_- < 1`.

## Not assumed

The proof does not require

- single-mode endpoints;
- equal source and receiver linewidths;
- critical coupling;
- identical source/receiver geometries;
- high-`Q` or low-`Q` limits;
- saturation of any intermediate inequality;
- a finite resonance count;
- a particular passive internal basis.

## Explicit exclusions

The current theorem does not cover

- a broad absolute-frequency interval represented by one carrier coefficient;
- uncontrolled modes with physical frequencies `omega_n >> omega_0` whose off-resonant tails enter the measured envelope band;
- active gain, inversion, parametric pumping, or externally powered feedback;
- extended phased apertures with `k_0 a` not small;
- added gravitational relays, mirrors, or external cavities;
- reactive/near-field exchange with `k_0 R` not large;
- relativistic or strongly nonlinear matter motion;
- higher-multipole-dominated operation;
- strong-field or curved-background focusing;
- arbitrary unbounded PDE boundary-control/observation ports without a separate admissibility proof;
- genuinely non-Markov continua;
- quantum-gravity corrections beyond quantized linearized modes.

## Frequency convention

```text
omega_0   absolute carrier angular frequency
nu        complex-envelope detuning
omega     physical frequency = omega_0 + nu
B         envelope bandwidth
Omega     upper physical frequency of retained modal sector
```

The passive `H2` integration is over detuning `nu`; the quadrupole rate and free-space propagation resource are evaluated at the physical carrier to leading narrowband order.

## Asymptotic discipline

The headline coefficient is a retained narrowband leading-wave-zone coefficient. Equality must not be used where only an asymptotic upper ceiling has been proved.

In particular, the recurrence result is

```math
\|P_{\rm eff}\|^2
\le \frac{\eta}{(1-\eta)^2},
```

not an equality for actual recurrent transfer.

## Novelty discipline

The theorem may be studied as a gravity-specific two-ended closure. Do not claim novelty for its generic systems, modal, directivity, integrated-response, or scattering ingredients. No priority claim is established for the complete closure.
