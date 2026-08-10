# Narrowband Frequency-Normalization Audit — Experiment 02

**Purpose:** prevent a hidden conflation between the frequency integrated in the passive `H2` transfer metric and the absolute gravitational carrier frequency that sets quadrupole radiation and free-space propagation.

## 1. Two frequency variables

Stage A uses a passive Markov envelope realization

```math
H(\nu)=-K_o(i\nu I-A)^{-1}K_i^\dagger,
```

where `nu` is the frequency variable of the narrowband envelope relative to its operating carrier.

The spectral-area metric should therefore be written

```math
\boxed{
\Gamma_{\rm coh}
=\frac1{2\pi}
\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
}
```

It has units `s^-1`.

Stages B and C use the **absolute** gravitational angular frequency, denoted here by

```math
\omega_0>0.
```

At this carrier,

```math
\kappa_g\propto\omega_0^4
```

and

```math
k_0=\frac{\omega_0}{c},
\qquad
\eta_{\rm TT}\propto\frac1{(k_0R)^2}.
```

These are different roles and should not share one unqualified symbol inside the final proof.

## 2. Narrowband Markov condition

Let the physical frequencies be

```math
\omega=\omega_0+\nu
```

with envelope bandwidth `B` satisfying

```math
\boxed{
B/\omega_0\ll1.
}
```

Then the slowly varying endpoint gravitational rates and TT propagation factor may be evaluated at the carrier to leading fractional order:

```math
K_g(\omega_0+\nu)
=K_g(\omega_0)+O(B/\omega_0),
```

and

```math
P_g(\omega_0+\nu)
=P_g(\omega_0)+O(B/\omega_0)
```

in the regular wave-zone regime.

Thus Stages A–C are compatible as a narrowband envelope theorem.

## 3. What is actually bounded

Stage A supplies

```math
\Gamma_{\rm coh}
\le
\eta_{\max}(\omega_0)
\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
]
```

for the envelope spectral area, with the physical couplings evaluated at the carrier.

Stage B gives, for a retained endpoint modal sector lying in the same narrow operating region,

```math
\operatorname{Tr}(K_g^\dagger K_g)
\lesssim
\frac{4G}{3c^5}I_2\omega_0^4
```

up to the controlled fractional bandwidth variation.

Stage C gives

```math
\eta_{\max}(\omega_0)
\lesssim
\frac{25}{16(k_0R)^2}.
```

The final carrier-frequency coefficient can therefore be assembled without integrating `omega^4` and `1/omega^2` as though they were constant over an arbitrary broad physical spectrum.

## 4. Broad-band statement is not yet proved

Experiment 02 does **not** currently claim the same simple inertia-only coefficient over a broad absolute-frequency interval.

A broad-band theorem would require retaining the explicit frequency dependence of

- gravitational endpoint couplings;
- propagation;
- possibly material and port operators;
- the realization used in the passivity cut.

A conservative supremum bound may be possible, but it is not the active theorem and may be unnecessarily loose.

## 5. Convention check

The Stage-A two-sided envelope convention

```math
\frac1{2\pi}\int_{-\infty}^{\infty}d\nu
```

is the standard `H2` convention for complex narrowband amplitudes. It should not be confused with integrating a real physical spectrum over both positive and negative **absolute** frequencies.

No factor of two is introduced when the theorem is stated consistently in the complex-envelope representation.

## 6. Required final notation

From this checkpoint onward:

```text
omega_0   absolute carrier angular frequency
nu        envelope detuning frequency
B         envelope bandwidth scale
k_0       omega_0 / c
Gamma_coh H2-like area integrated over nu
I_2       int rho r^2 dV about the endpoint center of mass
```

Any manuscript or theorem statement must retain this distinction.
