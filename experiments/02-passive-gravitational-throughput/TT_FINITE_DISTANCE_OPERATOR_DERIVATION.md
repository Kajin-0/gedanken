# Exact finite-distance outgoing compact-TT operator

**Date:** 2026-08-10  
**Purpose:** close the reviewer-style objection that the `25/16` propagation coefficient was presented only as an unquantified stationary-phase limsup.

## Result

Let `z=kR` and choose the source-receiver separation as the `z` axis. Rotational symmetry about the separation axis diagonalizes the five-dimensional complex STF quadrupole space into `m=0`, `|m|=1`, and `|m|=2` sectors.

After TT normalization and azimuthal integration, the unit-normalized angular kernels are

```math
K_2(\mu)=\frac{5}{32}(1+6\mu^2+\mu^4),
```

```math
K_1(\mu)=\frac58(1-\mu^2)(1+\mu^2),
```

```math
K_0(\mu)=\frac{15}{16}(1-\mu^2)^2,
```

and each obeys

```math
\int_{-1}^{1}K_m(\mu)\,d\mu=1.
```

The full fixed-frequency overlap is

```math
S_m(z)=\int_{-1}^{1}K_m(\mu)e^{iz\mu}\,d\mu.
```

Exact integration and separation of the outgoing `e^{iz}` piece gives

```math
S_{+,2}(z)=
-\frac{5i}{4z^5}
(z^4+2iz^3-3z^2-3iz+3)e^{iz},
```

```math
S_{+,1}(z)=
-\frac{5}{2z^5}
(z^3+3iz^2-6z-6i)e^{iz},
```

```math
S_{+,0}(z)=
\frac{15i}{2z^5}
(z^2+3iz-3)e^{iz}.
```

Therefore

```math
\eta_2(z)=\frac{25}{16z^{10}}
(z^8-2z^6+3z^4-9z^2+9),
```

```math
\eta_1(z)=\frac{25}{4z^{10}}
(z^6-3z^4+36),
```

```math
\eta_0(z)=\frac{225}{4z^{10}}
(z^4+3z^2+9).
```

For `z>=3`, direct comparison shows `eta_2 >= eta_1, eta_0`. Hence the exact outgoing operator norm in the compact angular model is

```math
\boxed{
\|P_g(z)\|_{op}^2
=\frac{25}{16z^2}
\left(1-\frac{2}{z^2}+\frac{3}{z^4}-\frac{9}{z^6}+\frac{9}{z^8}\right)
}
```

on that separated branch.

At `z=100`, the correction factor is

```text
0.999800029991...
```

so the leading `25/(16 z^2)` coefficient exceeds the exact outgoing compact-TT value by about `0.020%` in power.

## Scope

This result closes only the finite-`kR` propagation uncertainty inside the normalized compact quadrupole angular model. It does **not** provide a universal finite-size remainder for arbitrary extended endpoints and does **not** remove the carrier-freezing error at nonzero `B/omega_0`. Those approximations remain explicit in the manuscript.

The isolated outgoing component is the retarded source-to-receiver branch. No near-zone probability/channel interpretation of that isolated component is asserted.

## Independent numerical check

`numerics/verify_tt_propagation_bound.py` now:

1. integrates each `K_m exp(i z mu)` numerically and checks it against outgoing plus incoming exact pieces;
2. verifies `|m|=2` is maximal on a logarithmic grid for `z>=3`;
3. checks the `z=100` correction factor;
4. retains the existing random STF normalization, directivity, and stationary-phase `25/16` tests.
