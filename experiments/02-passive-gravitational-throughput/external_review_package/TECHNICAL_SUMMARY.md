# One-Page Technical Summary

## Question

For two separated compact passive matter interfaces coupled only through propagating linearized gravity, how large can the **frequency-integrated coherent local-port-to-local-port transfer** be when arbitrary passive internal resonances and coherent mode mixing are allowed?

Define

```math
\Gamma_{\rm coh}
=\frac{1}{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]\,d\omega.
```

It has units of inverse time. For a scalar channel it is the area under the power-transmissivity spectrum.

## Claimed bound

For a narrow band centered at angular frequency `omega`, separated compact nonrelativistic linear-harmonic endpoints, and leading quadrupolar wave-zone gravity,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

`I_A` and `I_B` are the internal mass inertia moments about the two endpoint centers of mass.

The result is classical. Quantization reproduces the same oscillator-strength normalization and supplies later pure-loss quantum-channel corollaries.

## Proof chain

### 1. Passive selected-port cut

For an energy-normalized passive realization

```math
A=-iH-\frac12K^\dagger K,
```

partition the ports into useful local channels and gravitational channels. The selected-port Gramian satisfies `0 <= P_u <= I`, hence

```math
\boxed{
\|S_{g\leftarrow u}\|_2^2
\le \operatorname{Tr}(K_g^\dagger K_g).
}
```

For the complete source--propagation--receiver chain,

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

The same result holds directly for countably infinite bounded-port passive Markov modal sectors when `K_g` is Hilbert--Schmidt.

### 2. Cumulative gravitational material resource

For elastic normal modes `w_n` with modal masses `mu_n`, standard modal completeness applied to the STF tidal/quadrupole influence fields gives

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le \frac{20}{3}I.
```

Using Hirakawa's gravitational effective area

```math
A_{Gn}=\frac{2q_n:q_n}{M\mu_n},
```

one obtains

```math
\boxed{
\sum_n M A_{Gn}\le\frac{40}{3}I.
}
```

Hirakawa's radiated-power normalization gives

```math
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
```

Therefore for retained modes with `omega_n <= Omega`,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
}
```

This same finite trace is what supplies the Hilbert--Schmidt regularity needed by the countably infinite endpoint theorem.

### 3. Compact TT propagation

For normalized compact STF quadrupole radiation spaces,

```math
\boxed{
\eta_{\max}
=\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}
}
```

at leading wave-zone order. The coefficient is independently reproduced by the historical compact-antenna maximum directivity `D=5/2` and reciprocal far-field transfer.

Combining this with the endpoint resource at `Omega ~= omega` gives the headline bound.

## Passive escape routes already tested

The leading ceiling is unchanged by:

- increasing passive `Q`;
- adding a finite or countably infinite number of bounded-port passive modes;
- coherent bright/dark mode mixing;
- optimizing compact quadrupole orientation; or
- arbitrarily many passive returns between the same two endpoints, since

```math
\eta_{\rm rec}
\le\frac{\eta}{(1-\eta)^2}
=\eta+O((kR)^{-4}).
```

## What would falsify the paper

Any one of the following is sufficient:

1. a passive compact counterexample whose integrated transfer exceeds the bound within the stated assumptions;
2. a failure of the selected-port / gravitational-port identification or its continuum normalization;
3. a historical theorem already equivalent to the final inertia-only two-ended closure; or
4. a missing physical resource that makes `I_A,I_B` insufficient to close the endpoint traces.
