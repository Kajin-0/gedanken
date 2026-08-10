# Finite-Dimensional Narrowband Two-Ended Inertia Bound

**Stage:** D assembly of independently validated ingredients.  
**Status:** **ESTABLISHED WITHIN THE DECLARED FINITE-DIMENSIONAL RETAINED-SECTOR MODEL; COMBINED ADVERSARIAL CI PASSED.**  
**Scope:** finite-dimensional passive Markov endpoints, compact nonrelativistic quadrupolar matter, separated free wave-zone propagation, narrowband complex-envelope operation, retained carrier-scale modal sector.

Later repository files separately extend the passive cut to countably infinite bounded-port sectors and control same-two-endpoint passive recurrence.

## 1. Ingredients

### Stage A — passive selected-port cut

For the narrowband envelope transfer matrix `T(nu)`,

```math
\Gamma_{\rm coh}
\equiv
\frac1{2\pi}\int_{\mathcal B_\nu} d\nu\,
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]
```

obeys

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

The band integral is bounded by the corresponding full-line `H2` norm because the integrand is nonnegative.

### Stage B — endpoint gravitational resource

For a retained modal sector satisfying

```math
\omega_n\le\Omega,
```

mass-weighted quadrupole completeness gives

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}I_2\Omega^4,
}
```

where

```math
I_2=\int\rho r^2d^3x
```

about the endpoint center of mass.

For the active narrow carrier model,

```math
\Omega=\omega_0[1+O(B/\omega_0)],
\qquad B/\omega_0\ll1,
```

so

```math
\operatorname{Tr}(K_g^\dagger K_g)
\lesssim
\frac{4G}{3c^5}I_2\omega_0^4.
```

This carrier replacement does not bound uncontrolled modes with `omega_n >> omega_0`; such off-resonant sectors require separate treatment.

### Stage C — compact TT propagation

With

```math
k_0=\frac{\omega_0}{c},
```

and endpoint radii `a_A,a_B`, require

```math
k_0a_A\ll1,
\qquad
k_0a_B\ll1,
\qquad
k_0R\gg1.
```

Then compact separated quadrupolar propagation obeys, at leading wave-zone order,

```math
\boxed{
\eta_{\max}
\lesssim
\frac{25}{16(k_0R)^2}.
}
```

## 2. Assembly

Insert Stages B and C into Stage A:

```math
\Gamma_{\rm coh}
\lesssim
\frac{25}{16(k_0R)^2}
\frac{4G\omega_0^4}{3c^5}
\min(I_{2,A},I_{2,B}).
```

Since

```math
k_0^2=\frac{\omega_0^2}{c^2},
```

this reduces to

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
}
```

Thus the conversation-origin `25/12` coefficient was recovered from three independently reconstructed repository steps rather than assumed.

## 3. Meaning of the bound

`Gamma_coh` is a frequency-integrated coherent-transfer spectral area for the complex envelope and has units `s^-1`. It is not an information capacity.

Within the stated passive compact retained-sector class, increasing resonance height by narrowing linewidth cannot make the integrated coherent source-to-receiver transfer arbitrarily large. The total endpoint gravitational oscillator-strength resource and the compact free-space propagation channel jointly impose the ceiling.

The minimum of `I_{2,A}` and `I_{2,B}` arises because either endpoint can be used as the passive cut.

## 4. What disappears from the leading ceiling

Within the established finite-dimensional retained-sector model, the bound contains no explicit

- passive quality factor;
- finite resonance count;
- passive unitary internal mode-mixing matrix;
- single-mode effective mass;
- critical-coupling choice;
- compact quadrupole orientation after optimization.

These quantities remain important for the shape and attainability of a specific transfer spectrum; they cannot raise the proved integrated ceiling within the stated class.

## 5. Narrowband requirement

This is a carrier-envelope theorem. The integrated variable is detuning `nu`, while `omega_0` is the absolute gravitational carrier frequency.

Required:

```math
B/\omega_0\ll1.
```

The endpoint gravitational rates and TT propagation factor are evaluated at `omega_0` to leading fractional bandwidth order for the retained carrier-scale modal sector.

See `NARROWBAND_NORMALIZATION_AUDIT.md`.

A broad absolute-frequency theorem has not been established.

## 6. Leading wave-zone meaning

The `25/16` propagation coefficient is a leading separated-wave-zone result. Therefore the assembled theorem uses `lesssim` rather than an exact finite-distance inequality.

Experiment 01 independently supplies an exact outgoing finite-distance correction for one aligned plus-mode specialization; Experiment 02 does not assign that subleading form to arbitrary complex quadrupole pairs.

## 7. Later scope hardening

After this finite-dimensional closure was validated, the repository added and separately checked

- `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md` — countably infinite bounded-port Markov modal sectors;
- `PASSIVE_TWO_ENDPOINT_RECURRENCE.md` — repeated passive returns between the same two compact endpoints at leading order;
- `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md` — historical collision search;
- `META_REFEREE_SIGNIFICANCE_AUDIT.md` — significance/editorial review;
- `MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md` — manuscript scope hardening.

Still excluded are uncontrolled high-frequency off-resonant sectors, unbounded PDE boundary ports, non-Markov continua, active systems, added relays/cavities, extended apertures, near-field transfer, and relativistic/nonlinear or higher-multipole regimes.

## 8. Novelty status

No novelty is claimed for the ingredients:

- passive `H2`/Gramian machinery;
- elastic eigenmode gravitational response;
- quadrupole radiation;
- TT projection/directivity;
- reciprocal wave-channel propagation.

The only plausible publication contribution is the complete gravity-specific two-ended inertia closure. Hostile search found strong near-collisions but no inspected source stating the complete theorem; no priority claim is made.

## 9. Validation record

The combined finite-dimensional adversarial regression passed on the real remote:

```text
commit 8fc8da7cf5d51e3a56d7e0b15434407c7e493ecb
run    31393498572
job    93470648716
PASS
```

The regression constructs random complex passive source/receiver systems constrained by the Stage-B endpoint budgets, inserts random contracted two-polarization propagation subject to the Stage-C ceiling, integrates the actual two-ended transfer, and searches for violations of the assembled bound.

Numerical testing supports but does not replace the analytic proof.
