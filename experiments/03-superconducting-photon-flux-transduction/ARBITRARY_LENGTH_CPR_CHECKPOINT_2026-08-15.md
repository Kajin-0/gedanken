# Experiment 03 — Arbitrary-Length Graphene CPR Checkpoint — 2026-08-15

## Purpose

Replace the uncontrolled short-junction graphene CPR sensitivity model with an ideal **arbitrary-length ballistic graphene SNS calculation** based on the Titov–Beenakker secular equation and the Hagymási–Kormányos–Cserti Matsubara-current construction.

This remains an exploratory ideal model. It is not a calibrated representation of the 2026 MoRe/graphene single-photon detector and it establishes no novelty.

## 1. Primary model

Titov and Beenakker derive the bound-state quantization condition

```math
\cos\phi=G(\varepsilon,q),
```

where `G` is their Eq. (14), built from

```math
\alpha(\varepsilon)=\arcsin\left(\frac{\hbar v_F q}{\varepsilon+\mu}\right),
```

```math
k(\varepsilon)=\frac{\varepsilon+\mu}{\hbar v_F}\cos\alpha(\varepsilon),
```

and the Andreev phase `beta=arccos(epsilon/Delta)`.

Hagymási, Kormányos and Cserti use the same secular equation for highly doped superconducting electrodes and evaluate the finite-temperature current without explicitly solving each Andreev level:

```math
I=-\frac{8 e k_BT}{\hbar}
\sum_{m,n}\partial_\phi\ln\mathcal F(i\omega_n,q_m).
```

For

```math
\mathcal F=\cos\phi-G(i\omega_n,q),
```

`G` is phase-independent and

```math
\partial_\phi\ln\mathcal F
=-\frac{\sin\phi}{\cos\phi-G}.
```

The wide-junction implementation replaces the transverse-mode sum by an integral over `Q=qL`. Overall current and `W/L` prefactors cancel from the normalized CPR and fold calculations, while the Matsubara `T` prefactor is retained so that current-amplitude ratios across temperature remain physical.

## 2. Dimensionless variables

Use

```math
\ell=\frac{L}{\xi_0}=\frac{\Delta_0L}{\hbar v_F},
\qquad
\mu_r=\frac{\mu}{\Delta_0},
\qquad
Q=qL,
\qquad
z=\frac{\varepsilon}{\Delta_0}.
```

The present checkpoint takes

```text
Delta0 = 1.3 meV
ell    = 1.1
T0     = 20 mK
delta  = 0.05 rad
```

and studies `mu/Delta0 = 0, 10, 20`.

A standard BCS gap interpolation is used for `Delta(T)`. Since the temperatures of interest are well below the BCS `Tc ~ 8.55 K` associated with `Delta0=1.3 meV`, gap suppression is modest compared with thermal evolution of the Andreev spectrum.

## 3. Numerical validation

### 3.1 Short-junction limit

At the Dirac point, Titov–Beenakker Eq. (20) gives, up to an overall factor,

```math
I(\phi)\propto
\cos(\phi/2)\operatorname{artanh}[\sin(\phi/2)].
```

The arbitrary-length Matsubara implementation was driven to `ell=0.01`, `mu=0`, `T=20 mK`. With the present finite Matsubara/transverse grids, the normalized CPR agrees with the closed short-junction form at the sub-percent-to-percent level; the phase of maximum current also converges to the same region as `ell -> 0`.

This is a numerical implementation check, not a precision error bound on the continuum model.

### 3.2 Intermediate-length qualitative behavior

For `ell ~ 1.1`, the calculated low-temperature CPR becomes forward-skewed, especially at finite doping, and approaches a more harmonic shape with increasing temperature. This is qualitatively the behavior reported by Hagymási et al. for `L ~ xi` and by graphene CPR measurements.

### 3.3 Transverse-cutoff convergence

At `ell=1.1`, `mu/Delta0=20`, the cold fold requires a relatively large `Q` cutoff. The normalized fold moves from roughly `0.17` at `Qmax=12` toward `~0.20` by `Qmax=20–30`. The canonical script therefore uses `Qmax=30` in its full mode. This convergence sensitivity must be retained in future precision work.

## 4. Cold fold threshold

Using the general load-line condition

```math
\mathcal I(x_f,T)=x_f-\delta,
\qquad
\partial_x\mathcal I(x_f,T)=1,
```

with the CPR normalized to its own `Ic(T)`, the cold fold values at `ell=1.1`, `delta=0.05` are approximately

| `mu/Delta0` | cold normalized `beta_fold` |
|---:|---:|
| 0 | 0.463 |
| 10 | 0.325 |
| 20 | 0.200 |

The strong doping dependence is important: a highly doped intermediate-length junction can have a steep, sawtooth-like low-temperature CPR near `phi~pi`, so the load-line slope reaches the fold at a much smaller normalized `beta` than the sinusoidal value.

## 5. Fold temperature versus cold beta — `mu/Delta0=20`

For a loop chosen with cold amplitude

```math
\beta_{cold}=\frac{2\pi L I_{c,0}}{\Phi_0},
```

the fold temperature solves

```math
\beta_{cold}
\frac{I_c(T)}{I_c(T_0)}
=\beta_{fold,norm}(T).
```

The ideal arbitrary-length model gives:

| `beta_cold` | `T_fold` (K) | reference thermal-energy fraction* |
|---:|---:|---:|
| 0.30 | 0.197 | 0.0062 |
| 0.40 | 0.390 | 0.0242 |
| 0.50 | 0.587 | 0.0551 |
| 0.60 | 0.776 | 0.0964 |
| 0.70 | 0.954 | 0.1455 |
| 0.80 | 1.118 | 0.2000 |
| 0.90 | 1.271 | 0.2584 |
| 1.00 | 1.413 | 0.3192 |
| 1.20 | 1.668 | 0.4449 |

*The reference fraction is

```math
\eta_{ref}
=\frac{T_{fold}^2-T_0^2}{(2.5\,K)^2-T_0^2},
```

which uses the earlier graphene heat-capacity reference and is **not** yet a system absorption efficiency.

## 6. Cold barrier, readout separation and provisional MQT capacitance

Fix a physical cold critical-current scale

```text
Ic,0 = 3 uA
```

only to translate dimensionless loop parameters into `L` and energy scales. For `mu/Delta0=20`:

| `beta_cold` | cold barrier / `k_B` (K) | provisional `C_min,Q` | `DeltaPhi/Phi0` | `DeltaI` (uA) | `L` (pH) |
|---:|---:|---:|---:|---:|---:|
| 0.30 | 1.14 | 19.9 pF | 0.0776 | 4.87 | 32.91 |
| 0.40 | 3.41 | 2.11 pF | 0.1160 | 5.47 | 43.88 |
| 0.50 | 6.34 | 0.571 pF | 0.1536 | 5.79 | 54.85 |
| 0.60 | 9.65 | 0.233 pF | 0.1892 | 5.94 | 65.82 |
| 0.70 | 13.14 | 0.120 pF | 0.2225 | 5.99 | 76.79 |
| 0.80 | 16.70 | 0.071 pF | 0.2535 | 5.97 | 87.76 |
| 0.90 | 20.23 | 0.0465 pF | 0.2823 | 5.91 | 98.73 |
| 1.00 | 23.70 | 0.0328 pF | 0.3090 | 5.82 | 109.70 |
| 1.20 | 30.31 | 0.0188 pF | 0.3570 | 5.61 | 131.64 |

`C_min,Q` is **only** the existing Experiment-03 Lambert-W solution inside the provisional cubic MQT model with `D=1e-6 s^-1`. It is not an exact dissipative rf-SQUID DCR requirement.

## 7. Doping sensitivity at `beta_cold=0.8`

| `mu/Delta0` | cold normalized fold | `T_fold` (K) | reference thermal fraction | cold barrier / `k_B` (K) | provisional `C_min,Q` |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.463 | 1.154 | 0.213 | 7.01 | 0.262 pF |
| 10 | 0.325 | 1.117 | 0.199 | 13.76 | 0.103 pF |
| 20 | 0.200 | 1.118 | 0.200 | 16.70 | 0.071 pF |

The fold temperature is surprisingly insensitive to doping across `mu/Delta0=10–20` at this beta, while the **cold barrier and quantum-stability margin improve strongly with doping** in the ideal model.

## 8. Strongest illustrative operating point

The present ideal checkpoint favors examining

```text
ell          ~ 1.1
mu/Delta0    ~ 10–20
beta_cold    ~ 0.8–1.0
delta        = 0.05
Ic,0 scale   ~ 3 uA
```

rather than the earlier sinusoidal `beta=1.5` or the short-junction toy optimum.

For `mu/Delta0=20`, `beta_cold=0.8`:

```text
T_fold                       ~1.118 K
reference retained heat      ~20 % of the 2.5-K reference energy
cold barrier/k_B             ~16.70 K
L                             87.76 pH
provisional C_min,Q          ~71 fF
persistent-state separation  ~0.2535 Phi0
circulating-current gap      ~5.97 uA.
```

This is materially more favorable than the short-junction sensitivity model, which at a superficially similar beta required a fold near `2.17 K` and a provisional capacitance floor near `0.52 pF`.

## 9. Why the change occurs

The arbitrary-length calculation has a denser Andreev spectrum and stronger temperature dependence than the short-junction limit. Hagymási et al. explicitly find that both short and long/intermediate ballistic graphene junctions are nonsinusoidal at low temperature and that the CPR approaches a simple harmonic form as temperature rises. For `L/xi~1.1` and finite doping, their numerical CPR already trends toward a rounded sawtooth at low temperature.

The fold depends on both CPR amplitude and **slope**, so this thermal reshaping matters directly to the photon threshold.

## 10. Critical caveats

The current model still assumes:

- ballistic graphene;
- rigid step-function superconducting pair potential;
- highly doped ideal superconducting electrodes;
- ideal SG interfaces;
- a wide-junction continuum transverse-mode approximation;
- equilibrium Fermi distributions characterized by `T_e`;
- BCS-like `Delta(T)`;
- no self-consistent inverse proximity effect;
- no disorder, contact resistance, interface transparency loss or charge puddles.

The 2026 photon detector has a 600-nm graphene channel. With `Delta~1.3 meV` and `v_F~1e6 m/s`, `xi0=hbar v_F/Delta` is about `0.5 um`, which is why `ell~1.1` is a sensible order-unity sensitivity point but **not** a calibrated geometric fit.

## 11. Consequence for the research program

The previous question

```text
Can one 10-um photon reduce a plausible Ic enough?
```

is no longer the strongest formulation.

The correct question is

```text
Can the photon-driven nonequilibrium full CPR cross the inductive load-line fold
for long enough to settle into the favored basin while the cold full-CPR
potential remains stable against dissipative quantum/thermal escape?
```

The ideal arbitrary-length calculation says **this remains quantitatively plausible** and gives a substantially better static corridor than the short-junction toy model.

It does not yet establish system-level feasibility.

## 12. Next falsification step

The next model should attack the assumptions that most strongly affect the fold:

1. finite/nonideal SG interface transparency and contact doping;
2. self-consistent or experimentally calibrated arbitrary-length CPR;
3. nonequilibrium electron distribution during the first tens of ps after LWIR absorption;
4. dissipative MQT for the actual full-CPR potential;
5. time-dependent fold passage and retrapping with `R_hot(T_e)`;
6. realistic 8–14-um antenna/cavity absorption.

A useful near-term validation target is to reproduce published arbitrary-length CPR/skewness curves quantitatively before using the model for optimization.

## Reproducibility

Canonical script:

```text
calculations/arbitrary_length_graphene_cpr.py
```

## Status

**GO for continued theory. NO-GO for manuscript.**
