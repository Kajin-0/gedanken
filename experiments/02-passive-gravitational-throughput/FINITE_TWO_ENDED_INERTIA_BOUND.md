# Finite-Dimensional Narrowband Two-Ended Inertia Bound

**Stage:** D assembly of independently validated ingredients.  
**Status:** algebraic closure derived; integrated adversarial regression to be run before promotion.  
**Scope:** finite-dimensional passive Markov endpoints, compact nonrelativistic quadrupolar matter, separated free wave-zone propagation, narrowband complex-envelope operation.

## 1. Ingredients

### Stage A — passive selected-port cut

For the narrowband envelope transfer matrix `T(nu)`,

```math
\Gamma_{\rm coh}
\equiv
\frac1{2\pi}\int d\nu\,
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

### Stage B — endpoint gravitational resource

At carrier angular frequency `omega_0`, for a sufficiently narrow retained modal sector,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\lesssim
\frac{4G}{3c^5}I_2\omega_0^4,
}
```

where

```math
I_2=\int\rho r^2d^3x
```

about the endpoint center of mass.

### Stage C — compact TT propagation

With

```math
k_0=\frac{\omega_0}{c},
```

compact separated quadrupolar propagation obeys, at leading wave-zone order,

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

Thus the conversation-origin `25/12` coefficient has been **recovered from three independently reconstructed repository steps**, rather than assumed.

## 3. Meaning of the bound

`Gamma_coh` is a frequency-integrated coherent-transfer spectral area for the complex envelope and has units `s^-1`. It is not an information capacity.

The theorem says, within the stated passive compact narrowband class, that increasing a resonance height by narrowing its linewidth cannot make the integrated coherent source-to-receiver transfer arbitrarily large. The total endpoint gravitational oscillator-strength resource and the compact free-space propagation channel jointly impose the ceiling.

The minimum of `I_{2,A}` and `I_{2,B}` arises because either endpoint can be used as the passive cut.

## 4. What disappears from the leading ceiling

Within the established finite-dimensional model, the bound contains no explicit

- passive quality factor;
- finite resonance count;
- passive unitary internal mode-mixing matrix;
- single-mode effective mass;
- critical-coupling choice;
- compact quadrupole orientation after optimization.

This does not mean those quantities are irrelevant to achieving a particular transfer spectrum. It means they cannot raise the integrated ceiling beyond the endpoint resource and propagation constraints in the stated class.

## 5. Narrowband requirement

This is a carrier-envelope theorem. The integrated variable is detuning `nu`, while `omega_0` is the absolute gravitational carrier frequency.

Required:

```math
B/\omega_0\ll1.
```

The endpoint gravitational rates and TT propagation factor are evaluated at `omega_0` to leading fractional bandwidth order.

See `NARROWBAND_NORMALIZATION_AUDIT.md`.

A broad absolute-frequency theorem has not been established.

## 6. Leading wave-zone meaning

The `25/16` propagation coefficient is a leading separated-wave-zone result. Therefore the assembled theorem uses `lesssim` rather than an exact finite-distance inequality.

For the aligned plus-mode specialization, Experiment 01 independently supplies the exact outgoing finite-distance correction polynomial, but Experiment 02 does not assume that same subleading form for every complex source/receiver quadrupole superposition.

## 7. Current exclusions

The assembled result does not yet cover

- countably infinite bounded-port modal sectors without a separate operator proof;
- arbitrary unbounded PDE boundary ports;
- genuinely non-Markov continua;
- repeated source-receiver gravitational returns beyond the one-way leading cut;
- active gain, inversion, pumping, or feedback that changes the passive balance;
- extended phased apertures;
- gravitational relays or external cavities;
- reactive near-field exchange;
- relativistic/nonlinear matter or higher-multipole-dominated operation.

These are separate adversarial stages, not hidden assumptions.

## 8. Novelty status

No novelty is claimed for the ingredients:

- passive `H2`/Gramian machinery;
- elastic eigenmode gravitational response;
- quadrupole radiation;
- TT projection/directivity;
- reciprocal wave-channel propagation.

The only possible later publication claim is the **complete gravity-specific two-ended inertia closure** after historical collision search and scope hardening.

At this checkpoint, priority remains `OPEN`.

## 9. Required integrated adversary

`numerics/verify_combined_inertia_bound.py` should construct random complex passive source/receiver systems whose gravitational port traces are constrained below Stage B resource budgets, insert random contracted two-polarization propagation with the Stage-C ceiling, integrate the actual two-ended transfer, and search for

```math
\Gamma_{\rm coh}
>
\frac{25}{12R^2}\min(I_{2,A},I_{2,B})
```

in units `G=c=omega_0=1`.

Only after that CI passes should the finite-dimensional narrowband `25/12` result be promoted to `ESTABLISHED WITHIN MODEL`.
