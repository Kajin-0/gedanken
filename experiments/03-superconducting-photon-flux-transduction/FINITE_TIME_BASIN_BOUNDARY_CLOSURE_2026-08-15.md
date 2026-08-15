# Finite-Time Basin-Boundary Closure — 2026-08-15

## Purpose

Replace the failed instantaneous/local scalar capture criteria with the exact deterministic phase-space object for a finite thermal pulse, and show how that object connects naturally to later stochastic capture probabilities.

This is standard nonautonomous dynamical-systems structure applied to Experiment 03. It is **not** a novelty claim.

## 1. Deterministic flow

For a prescribed thermal/electronic drive and deterministic environment, write the phase state

```math
z=(x,v),
\qquad
v=\dot x.
```

The scalar-R model is

```math
\dot z
=G[z,t;T(\cdot),R].
```

More generally, a causal environment can be represented with auxiliary variables or a memory kernel; the present finite-dimensional notation is retained for clarity.

Let

```math
\Phi_{t,t_0}
```

be the deterministic flow map from time `t0` to `t`.

Choose a final time `t_f` after the optical/thermal drive has essentially recovered to the cold operating landscape.

## 2. Final recovered basins

At `t_f`, let

```text
Omega_L^f  final phase-space basin of the original left flux state
Omega_R^f  final basin of the target right flux state.
```

Their boundary is the stable manifold of the cold saddle in the autonomous recovered system:

```math
\boxed{
\partial\Omega_L^f
=\partial\Omega_R^f
=W_f^s.
}
```

For the two-state model this is a codimension-one curve in the 2D `(x,v)` phase plane.

## 3. Pull the basin boundary back through the photon pulse

The initial states that ultimately reach the target basin are

```math
\boxed{
\Omega_R^0
=\Phi_{t_f,0}^{-1}(\Omega_R^f).
}
```

Similarly,

```math
\Omega_L^0
=\Phi_{t_f,0}^{-1}(\Omega_L^f).
```

Therefore the **exact deterministic initial-time capture boundary** is

```math
\boxed{
\mathcal B_0
=\Phi_{t_f,0}^{-1}(W_f^s).
}
```

This is the correct nonautonomous replacement for

```text
instantaneous saddle energy
instantaneous stable-manifold tangent
static fold location
moving-minimum lag
or local unstable e-fold count.
```

Those are approximations to pieces of the pulled-back boundary, not the boundary itself.

## 4. Why the instantaneous stable manifold failed

At an intermediate time `t`, the frozen system has an instantaneous saddle and a local tangent stable manifold.

But the detector outcome depends on the **future** evolution of the potential:

```text
saddle continues moving
the well can disappear/reappear
damping continues acting
phase retains velocity
cooling reforms the cold landscape.
```

A trajectory can transiently cross the instantaneous frozen stable-manifold tangent and still return to the original final basin.

The pulled-back final basin boundary automatically includes the entire future pulse history.

## 5. Exact deterministic capture criterion

The physical cold initial state is approximately

```math
z_c=(x_c,0)
```

in the deterministic model.

Then

```text
capture      iff z_c lies in Omega_R^0
noncapture   iff z_c lies in Omega_L^0
boundary     iff z_c lies on B_0.
```

This gives a mathematically exact deterministic formulation of the scalar-R pulse problem.

The full solver's observed rise-time / resistance boundary is simply the parameter locus on which

```math
\boxed{z_c\in\mathcal B_0(\text{pulse parameters}).}
```

## 6. Practical edge-tracking construction

A computationally practical route is:

1. choose `t_f` after the pulse has recovered;
2. construct a short segment of the final cold saddle stable manifold near the saddle;
3. integrate that segment backward through the full time-dependent dynamics;
4. adaptively extend/refine it where necessary;
5. determine which side contains `(x_c,0)`.

An equivalent shooting method at fixed `x=x_c` is to find the initial velocity

```math
v_{edge}
```

such that

```math
\boxed{(x_c,v_{edge})\in\mathcal B_0.}
```

For the physical deterministic initial velocity `v=0`, the signed quantity

```math
\boxed{\Delta v_{FT}=-v_{edge}}
```

(with a fixed orientation convention) becomes a finite-time basin margin.

Unlike a local saddle metric, this margin already includes the complete pulse history.

## 7. Connection to rate/damping boundary

At the deterministic capture boundary in a control parameter `p`,

```math
\Delta v_{FT}(p)=0.
```

Near a regular boundary point,

```math
\Delta v_{FT}
\simeq
A_p(p-p_c)+A_R/R+\cdots.
```

This provides a geometric interpretation of the empirically observed

```math
R_{min}\propto1/(\tau_c-\tau_r)
```

scaling: it is the local zero of the finite-time basin margin under a smooth first-order expansion in rise time and damping parameter `1/R`.

Thus `RATE_DAMPING_CRITICAL_SCALING_2026-08-15.md` is naturally interpreted as a local section through the pulled-back basin boundary.

## 8. Bridge to stochastic initial conditions

Suppose, first in a semiclassical/classical approximation, the cold initial phase state has probability density

```math
\rho_0(z).
```

If the pulse dynamics itself is deterministic, the target capture probability is exactly

```math
\boxed{
P_R
=\int_{\Omega_R^0}\rho_0(z)\,d^2z.
}
```

Wrong/no-switch probability is the complementary mass in the other pulled-back basin(s).

This turns deterministic basin geometry directly into a detector-efficiency calculation.

## 9. Local Gaussian boundary approximation

Near the mean cold state `mu`, approximate the pulled-back boundary by

```math
n^T(z-z_b)=0
```

and the initial phase-space distribution by a Gaussian covariance `Sigma`.

Then the signed normalized basin distance is

```math
\boxed{
 d_B
=\frac{n^T(\mu-z_b)}
{\sqrt{n^T\Sigma n}}.
}
```

The corresponding one-sided Gaussian capture probability is

```math
\boxed{
P_R\simeq\Phi(d_B)
}
```

with orientation chosen so positive `d_B` is the target side.

This is a **local classical/semi-classical approximation**, not the final quantum detector result.

## 10. Cold harmonic thermal covariance — classical limit only

Let

```math
\bar\Phi=\Phi_0/(2\pi).
```

Near a cold stable minimum with dimensionless curvature `kappa_c`, the physical quadratic phase Hamiltonian is

```math
H_\phi
\simeq
\frac12 C\bar\Phi^2v^2
+\frac12\frac{\bar\Phi^2}{L}\kappa_c(\delta x)^2.
```

In the **classical thermal limit**, equipartition gives

```math
\boxed{
\sigma_x^2
=\frac{k_BT_0L}
{\bar\Phi^2\kappa_c},
}
```

```math
\boxed{
\sigma_v^2
=\frac{k_BT_0}
{C\bar\Phi^2}.
}
```

This could be inserted into the local `d_B` estimate when the classical approximation is justified.

At the millikelvin / tens-of-GHz scales relevant to Experiment 03, quantum fluctuations and tunneling are important. **Do not use these classical variances as a substitute for MQT or full quantum open-system dynamics.**

## 11. Quantum/noisy generalization

When noise acts throughout the pulse, a deterministic pulled-back basin is no longer sufficient.

Let

```math
K(z_f,t_f|z_0,0)
```

be the stochastic transition kernel generated by the Langevin/Fokker-Planck/open-system dynamics.

Then

```math
\boxed{
P_R
=\int dz_0\,\rho_0(z_0)
\int_{\Omega_R^f}dz_f\,
K(z_f,t_f|z_0,0).
}
```

The deterministic formula is recovered when `K` collapses onto the deterministic flow.

For the final superconducting detector, the same environmental spectral density must determine

```text
classical/quantum fluctuation force
phase damping kernel
dissipative MQT / quantum escape.
```

This is the correct route from the current deterministic theory to `P_capture`, `P_wrong` and dark counts.

## 12. Why this is a better next model

The finite-time basin formulation naturally preserves the quantities the failed scalar reductions lost:

```text
phase position
phase velocity
full pulse history
moving basin geometry
launch damping
post-crossing retrapping.
```

It also gives an immediate statistical interpretation through probability mass relative to the pulled-back boundary.

## 13. Next numerical task

For the current scalar-R model:

1. construct `B_0` by backward stable-manifold integration for representative 14-um pulses;
2. verify that the known `R_min(tau_r)` points correspond to `(x_c,0)` crossing `B_0`;
3. calculate a signed finite-time basin margin away from the boundary;
4. compare that margin with full capture robustness under small perturbations of initial `(x,v)`;
5. only then add stochastic forcing.

If successful, this becomes the deterministic backbone of the later causal-admittance/noise model.

## Status

**FINITE-TIME BASIN BOUNDARY: preferred exact deterministic capture object.**

**SCALAR LOCAL CRITERIA: regression/intuition only.**

**EXPERIMENT 03: GO for continued theory; NO-GO for manuscript.**
