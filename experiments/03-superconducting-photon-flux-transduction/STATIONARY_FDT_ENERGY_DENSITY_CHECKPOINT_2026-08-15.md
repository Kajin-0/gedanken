# Experiment 03 — Stationary FDT Energy-Density Checkpoint — 2026-08-15

## Question

The fully stationary linear-FDT calculation at the original `14 um`, `A=100 um^2` point produced order-radian phase uncertainty at cooling-side reformation. Was that an architecture-level no-go, or a marginal absorbed-energy-density operating point?

A full stationary-history FDT wavelength/energy-density scan answers the first part: **the large 14-um susceptibility is not architecture-wide in the current model.** Shorter-wavelength-equivalent energy densities can produce much larger standardized coordinate separation under the same causal bath.

However, the favorable states remain highly anisotropic in phase space. Coordinate-only margins are not physical capture probabilities.

Canonical calculation:

```text
calculations/stationary_fdt_wavelength_screen.py
.github/workflows/experiment03-stationary-fdt-wavelength.yml
run 31913961527
```

Model:

```text
rDelta=.6
R=250 ohm
rise=20 ps
A=100 um^2
full CPR Tmax=.95 K
stationary cold bath history
symmetrized quantum FDT linear response
```

---

## 1. `alpha=omega_D/omega_c=0.50`

Cold reduced widths:

```text
sigma_x,cold ~0.11432
sigma_u,cold ~0.11600
```

At cooling-side reformation:

| lambda-equivalent | Tpeak [K] | x | u | x-saddle | sigma_x | sigma_u | rho_xu | x margin | principal rms |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 um | 0.88581 | +0.9853 | +0.0517 | 1.2806 | 0.0882 | 1.0840 | -0.930 | **14.52** | 0.0323, 1.0871 |
| 9 | 0.84551 | +0.8872 | +0.2447 | 1.1825 | 0.3799 | 0.4421 | -0.992 | **3.11** | 0.0372, 0.5817 |
| 10 | 0.81069 | +0.5489 | +0.3220 | 0.8441 | 0.3801 | 0.0611 | +0.575 | **2.22** | 0.0497, 0.3818 |
| 11 | 0.78018 | +0.2304 | +0.1286 | 0.5257 | 0.1819 | 0.1712 | +0.650 | **2.89** | 0.1042, 0.2270 |
| 12 | 0.75312 | +0.2791 | -0.1535 | 0.5743 | 0.3359 | 0.2723 | -0.953 | 1.71 | 0.0651, 0.4275 |
| 13 | 0.72890 | +0.9093 | -0.2284 | 1.2045 | 0.5702 | 0.6030 | +0.997 | 2.11 | 0.0330, 0.8292 |
| 14 | 0.70704 | +0.4214 | +0.3306 | 0.7167 | 1.1786 | 0.3809 | +0.999 | **0.61** | 0.0197, 1.2384 |

The 14-um marginal point reproduces the earlier stationary-history result.

The `8–11 um` energy-density region is qualitatively different: the coordinate uncertainty at reformation is far smaller relative to the target-side displacement.

---

## 2. Coordinate rescue is phase-space rotation, not free squeezing

The most dramatic example is the `8 um` equivalent:

```text
sigma_x ~0.088 < cold sigma_x ~0.114
```

but simultaneously

```text
sigma_u ~1.084 >> cold sigma_u ~0.116.
```

The covariance has principal rms widths

```text
~0.032 and ~1.087
```

and correlation

```text
rho_xu ~-0.93.
```

Thus the bath/phase dynamics have rotated and stretched the stationary covariance so that its `x` projection is focused while the velocity-like coordinate is strongly anti-focused.

This validates the phase-space focusing interpretation in

```text
REFORMATION_PHASE_MATCHING_CLOSURE_2026-08-15.md
```

and simultaneously proves that a `14.5 sigma` **coordinate** margin cannot be read as a 14.5-sigma capture probability.

The full finite-time basin orientation in `(x,u)` is mandatory.

---

## 3. `alpha=.35` remains less favorable

For the slower/lower-cutoff environment:

```text
lambda  x margin
10 um   0.78
11      1.88
12      1.49
13      1.80
14      0.67.
```

Thus the strong short-energy-density rescue is not produced simply by deeper heating. It depends jointly on the causal environment and reformation phase.

This reinforces the capture-lobe / phase-matching picture.

---

## 4. The 14-um no-go signal is reclassified

Previous statement:

```text
14-um stationary-history linear FDT produces order-radian uncertainty and
<1-sigma x separation at reformation.
```

That statement remains correct for the original `A=100 um^2` operating point.

But the stronger conclusion

```text
therefore the architecture cannot support high-fidelity LWIR capture
```

is **rejected**.

The current model contains absorbed-energy-density trajectories with much better stationary-FDT coordinate separation.

The correct status is now

```text
original 14-um / 100-um^2 point -> fragile / near-no-go
architecture as a whole          -> still alive
energy-density/environment tuning -> first-order design requirement.
```

---

## 5. Direct translation back to 14 um

Inside the retained thermal model,

```math
T(t;A,\lambda)
```

depends on area and wavelength through

```math
A\lambda.
```

Therefore the complete deterministic thermal/phase trajectory for

```text
8 um, A=100 um^2
```

maps to

```text
14 um, A=100*(8/14) ~57.1 um^2,
```

provided the circuit, rise time and optical deposition model remain unchanged.

Likewise

```text
9 um equivalent  -> A~64.3 um^2 at 14 um
10 um equivalent -> A~71.4 um^2
11 um equivalent -> A~78.6 um^2.
```

Thus the favorable stationary-FDT energy-density branch can, in principle, be moved into the desired LWIR band by reducing the thermally active area rather than changing photon wavelength.

This is conditional on being able to decouple thermally active area from Josephson CPR/circuit and optical collection area.

---

## 6. Spatial-rise consistency

Using only the retained cross-device diffusion orientation scale

```math
D_{char}\sim0.705\;m^2/s,
```

for a square active area heated near its center,

```math
 t_{diff}\sim\frac{(\sqrt A/2)^2}{D}
=\frac{A}{4D}.
```

Then

```text
A=100 um^2  -> ~35.5 ps
A=78.6      -> ~27.9 ps
A=71.4      -> ~25.3 ps
A=64.3      -> ~22.8 ps
A=57.1      -> ~20.2 ps.
```

The area that maps the favorable `8 um` equivalent to `14 um` therefore also brings this crude central-diffusion scale almost exactly onto the `20 ps` rise used in the favorable calculation.

This is only an internal consistency screen: the `D_char` value is not a cryogenic GJJ transient diffusivity calibration.

---

## 7. Next decisive tests

Two stronger calculations are active:

```text
1. conditional Mahalanobis finite-time basin radius at 14 um;
2. nonlinear causal-FDT truncated-Wigner / generalized-Langevin ensemble
   at 8, 10, 11 and 14 um-equivalent energy densities.
```

The second calculation is particularly important because it lets the large reformation covariance deform nonlinearly rather than extrapolating a Gaussian tangent filament beyond its validity range.

A favorable result must also survive parameter/cutoff robustness; `tangent_alpha_robustness.py` is scanning whether the alpha~0.5 region is broad or resonance-like.

---

## Verdict

**The stationary-FDT 14-um warning is an operating-point no-go, not yet an architecture no-go.**

The strongest current route is

```text
smaller thermally active volume
+ alpha around the favorable causal-filter phase region
+ one-sided fold directionality
+ active/non-passive reset if long cold ringdown becomes limiting.
```

No physical capture efficiency is yet established.

**GO for continued theory. NO-GO for manuscript.**
