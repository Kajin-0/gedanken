# Experiment 03 — Gaussian Basin-Radius Probability Bound — 2026-08-15

## Purpose

The stationary-history linear FDT state at cooling-side reformation is highly anisotropic. Coordinate-only margins such as `(x-x_s)/sigma_x` therefore do not control capture probability.

A more geometry-invariant sufficient condition is available whenever the relevant state distribution is Gaussian and all subsequent dynamics are deterministic: measure the largest covariance-standardized ball that is entirely contained in the target basin.

This is an elementary Gaussian probability bound, not a novelty claim.

---

## 1. Standardize the Gaussian state

Let the `n`-dimensional state at some decision time be

```math
z\sim\mathcal N(\mu,\Sigma),
```

with positive-definite covariance `Sigma`.

Define whitened coordinates

```math
\boxed{
y=\Sigma^{-1/2}(z-\mu).}
```

Then

```math
y\sim\mathcal N(0,I_n).
```

The Mahalanobis radius is

```math
r_M(z)
=\sqrt{(z-\mu)^T\Sigma^{-1}(z-\mu)}
=\|y\|.
```

---

## 2. Inscribed-basin radius

Let `Omega_T` denote the set of states that deterministically evolve into the target persistent-flux basin.

Define the largest standardized ball around the mean contained in the target basin:

```math
\boxed{
r_*
=\sup\{r:
\{z:r_M(z)<r\}\subseteq\Omega_T\}.
}
```

Equivalently, `r_*` is the minimum Mahalanobis distance from the mean to any non-target state/basin boundary, provided the target basin contains the mean.

Then every state with `r_M<r_*` succeeds.

Therefore

```math
\boxed{
P_T
\ge
P(\chi_n<r_*),
}
```

where `chi_n` is the chi distribution with `n` degrees of freedom.

This bound does not require the basin boundary to be planar, aligned with covariance axes, or convex outside the inscribed ball.

---

## 3. Two-dimensional phase-space result

For reduced phase coordinates such as

```math
z=(x,u),
\qquad u=\dot x/\omega_c,
```

we have `n=2` and

```math
P(\chi_2<r)=1-e^{-r^2/2}.
```

Hence

```math
\boxed{
P_T\ge1-e^{-r_*^2/2}.
}
```

Required sufficient radii are

```text
target lower bound   required r_*
90%                   2.146
95%                   2.448
99%                   3.035
99.9%                 3.717
99.99%                4.292
99.9999%              5.257.
```

These radii are deliberately more conservative than a one-dimensional half-space criterion. For example, a locally flat 99% half-space boundary lies at `2.326 sigma`, but a complete 2D Gaussian disk of radius `2.326` contains less than 99% of the probability mass.

---

## 4. Why this matters for the current 14-um result

The stationary-history linear FDT covariance at reformation has roughly

```text
major rms width ~1.1–1.2
minor rms width ~0.015–0.020
rho_xu ~0.98–0.999.
```

Thus the distribution is a long thin filament.

The coordinate projection

```math
(x_{det}-x_s)/\sigma_x<1
```

cannot determine whether the actual finite-time basin boundary cuts across the long direction or is nearly parallel to it.

The canonical next calculation therefore searches the future deterministic basin in whitened coordinates and estimates `r_*` directly:

```text
calculations/mahalanobis_basin_margin14.py
.github/workflows/experiment03-mahalanobis-basin14.yml
```

---

## 5. Scope limitations

The bound is rigorous only for the model to which its assumptions apply.

For Experiment 03, current caveats are substantial:

```text
- the reformation covariance is obtained from linear symmetrized-FDT response;
- order-radian major-axis spread means the linear Gaussian approximation may fail;
- the reduced (x,u) screen conditions on the deterministic bath-memory state;
- future bath noise is omitted in the conditional basin scan;
- exact open-system quantum dynamics can be non-Gaussian and nonclassical.
```

Therefore the present use of `r_*` is a **geometry/falsification screen**, not a certified detector-efficiency theorem.

A strong result is still useful:

```text
r_* << 1
 -> strong evidence that the linearized ensemble directly intersects failure geometry;

r_* > 3
 -> the alarming x-only projection was largely a covariance-orientation artifact,
    although open-system quantum corrections remain.
```

---

## Status

**Exact Gaussian geometry bound; conditional application to Experiment 03.**

No novelty claim. No physical efficiency claim yet.

**GO for continued theory. NO-GO for manuscript.**
