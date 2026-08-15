# Dark-Count / Capture-Time Elimination — 2026-08-15

## Purpose

Eliminate the explicit capacitance variable from the current Experiment-03 MQT/capture closure and expose the smallest set of physical quantities that control the trade among

```text
cold dark-event target
capture time
thermal dwell
spectral reach.
```

This is exact algebra **inside the current provisional MQT rate and current `g sqrt(LC)` phase-time convention**. It is not yet exact dissipative rf-SQUID quantum escape theory and is not a novelty claim.

## 1. Starting point

Retain the current diagnostic quantum-escape model

```math
\Gamma_Q(C)
=\frac{\omega(C)}{2\pi}
\exp\!\left[-\alpha_Q\frac{\Delta U_c}{\hbar\omega(C)}\right],
```

with

```math
\omega(C)=\sqrt{\frac{\kappa_c}{LC}}.
```

Here

```text
Delta U_c  cold metastable barrier
kappa_c    dimensionless cold curvature in the retained phase normalization
L          loop inductance
C          effective junction/circuit capacitance
alpha_Q    present cubic-barrier diagnostic coefficient (~7.2)
D          target dark-switch rate.
```

Solving `Gamma_Q=D` gives the already-derived capacitance floor

```math
C_{min,Q}
=\frac{\hbar^2\kappa_c}{\alpha_Q^2\Delta U_c^2L}
\left[
W\!\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right)
\right]^2.
```

Define

```math
W_D
\equiv
W\!\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right).
```

## 2. Quantum-stability time

Define the single time scale

```math
\boxed{
\tau_Q(D)
\equiv
\frac{\hbar\sqrt{\kappa_c}}
{\alpha_Q\Delta U_c}
W_D.
}
```

Then the capacitance expression collapses exactly to

```math
\boxed{LC_{min,Q}=\tau_Q^2,}
```

or

```math
\boxed{C_{min,Q}=\tau_Q^2/L.}
```

Thus all of the cold MQT/capacitance design information contained in the current diagnostic can be represented by `tau_Q`.

## 3. Phase and damping write times at the quantum-stability optimum

The present deterministic phase-time envelope is

```math
t_\phi=g\sqrt{LC}.
```

At the smallest capacitance compatible with target `D`,

```math
\boxed{t_{\phi,Q}^*=g\tau_Q.}
```

This eliminates both `L` and `C` from the phase-limited branch.

The current damping envelope is

```math
t_R=2R_{hot}C.
```

At `C=C_min,Q`,

```math
\boxed{
t_{R,Q}^*
=2\frac{R_{hot}}{L}\tau_Q^2.
}
```

Thus `L` and `R_hot` enter only through the ratio

```math
\zeta_R\equiv R_{hot}/L,
```

not independently.

The optimized necessary write-time scale becomes

```math
\boxed{
t_{req}^*(D)
=\max\!\left[
t_{diff},\;
g\tau_Q(D),\;
2\zeta_R\tau_Q^2(D)
\right].
}
```

This is a cleaner closure than carrying `C_min,Q`, `L` and `C` separately.

## 4. Clean-graphene thermal-dwell closure

For the retained clean-graphene model

```math
C_e=\gamma A T,
\qquad
P_{e-ph}=\Sigma A(T^4-T_0^4),
```

the exact infinite-photon-energy dwell ceiling above a fold at `T_f` is

```math
\boxed{
t_{>,max}(T_f)
=\frac{\gamma}{4\Sigma T_0^2}
\ln\!\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right).
}
```

For `T_0 << T_f`,

```math
\boxed{t_{>,max}\simeq2\tau_{ep}(T_f),}
```

where

```math
\tau_{ep}(T_f)=\frac{\gamma}{4\Sigma T_f^2}.
```

Therefore **no photon energy can rescue the design within this cooling law** unless

```math
\boxed{
\max\!\left[
t_{diff},\;g\tau_Q,\;2\zeta_R\tau_Q^2
\right]
<2\tau_{ep}(T_f).
}
```

Equivalently, the two circuit conditions are

```math
\boxed{g\tau_Q<2\tau_{ep}(T_f),}
```

and

```math
\boxed{\zeta_R\tau_Q^2<\tau_{ep}(T_f).}
```

The second can be written

```math
\boxed{
\frac{R_{hot}}{L}
<\frac{\tau_{ep}(T_f)}{\tau_Q^2}.
}
```

This is the current cleanest dark-stability / damping / thermal-dwell condition.

## 5. Direct dark-count floor for a specified phase-capture interval

The same algebra can be inverted without Lambert `W`.

Suppose a phase-capture budget `t_c` imposes

```math
g\sqrt{LC}\le t_c.
```

The largest capacitance allowed by this branch is

```math
C_{max,\phi}=\frac{t_c^2}{g^2L}.
```

Because increasing `C` suppresses the present MQT rate, the smallest MQT dark rate compatible with this phase-capture budget occurs at `C=C_max,phi`.

At that point

```math
\omega_{min}=\frac{g\sqrt{\kappa_c}}{t_c}.
```

Therefore

```math
\boxed{
D_{min,\phi}(t_c)
=\frac{g\sqrt{\kappa_c}}{2\pi t_c}
\exp\!\left[
-\frac{\alpha_Q\Delta U_c t_c}
{\hbar g\sqrt{\kappa_c}}
\right].
}
```

This is independent of `L` and `C` separately.

For a target `D`, the cold barrier must satisfy

```math
\boxed{
\Delta U_c
\ge
\frac{\hbar g\sqrt{\kappa_c}}
{\alpha_Q t_c}
\ln\!\left(
\frac{g\sqrt{\kappa_c}}
{2\pi D t_c}
\right),
}
```

provided the logarithm is positive.

This makes the detector trade transparent:

```text
shorter allowed capture time
 -> larger required cold barrier
 -> harder optical fold trigger.
```

## 6. Spectral-dark-capture bound near a smooth thermal fold

Near a nondegenerate fold, if temperature is the smooth control parameter, write the cold barrier locally as

```math
\boxed{
\Delta U_c
\simeq K_T(T_f-T_0)^{3/2}.
}
```

`K_T` is **not universal**. It is determined by the local CPR/load-line normal form and thermal tuning susceptibility.

For a specified phase-capture budget `t_c`, define

```math
\Delta U_{req,Q}(D,t_c)
\equiv
\frac{\hbar g\sqrt{\kappa_c}}
{\alpha_Q t_c}
\ln\!\left(
\frac{g\sqrt{\kappa_c}}
{2\pi D t_c}
\right).
```

Then quantum dark stability requires

```math
T_f-T_0
\gtrsim
\left(\frac{\Delta U_{req,Q}}{K_T}\right)^{2/3}.
```

For graphene-like `C_e=gamma A T`, one absorbed photon satisfies the static fold condition only if

```math
\frac{hc}{\lambda}
\ge
\frac{\gamma A}{2\eta_{th}}
(T_f^2-T_0^2).
```

Combining these gives the explicit phase-limited local bound

```math
\boxed{
\lambda
\lesssim
\frac{2\eta_{th}hc}
{\gamma A
\left\{
\left[T_0+
\left(\Delta U_{req,Q}/K_T\right)^{2/3}
\right]^2-T_0^2
\right\}}.
}
```

This is the first closed Experiment-03 expression directly linking

```text
maximum photon wavelength
<-> dark-switch target D
<-> allowed phase-capture time t_c
```

without explicit `L` or `C`.

It is **asymptotic and model-conditional**, because it uses the smooth-fold `3/2` law and the provisional MQT expression.

### Low-`T0` scaling

If

```text
T0 << Tf
```

and all fold coefficients are treated as fixed, then

```math
\lambda_{max}
\propto
\Delta U_{req,Q}^{-4/3}.
```

Since

```math
\Delta U_{req,Q}
\sim
\frac1{t_c}
\ln\!\left(\frac1{Dt_c}\right),
```

one obtains the characteristic scaling

```math
\boxed{
\lambda_{max}
\propto
\left[
\frac{t_c}{\ln(1/Dt_c)}
\right]^{4/3}
}
```

up to the fixed material/fold prefactor and the more precise dimensionless factors above.

This scaling is a candidate theoretical object for later novelty audit, **not a novelty claim**.

## 7. Parametric stable-spectral frontier without local-fold approximation

The previous section is local. A more robust formulation uses the actual CPR-derived constitutive functions

```text
Delta U_c(T_f)
kappa_c(T_f)
zeta_R(T_f)=R_hot/L.
```

Define

```math
\tau_Q(T_f,D)
=
\frac{\hbar\sqrt{\kappa_c(T_f)}}
{\alpha_Q\Delta U_c(T_f)}
W\!\left(
\frac{\alpha_Q\Delta U_c(T_f)}
{2\pi\hbar D}
\right).
```

The dynamically feasible fold-temperature set is

```math
\mathcal F_D
=\left\{T_f:
\max[t_{diff},g\tau_Q,2\zeta_R\tau_Q^2]
<t_{>,max}(T_f),
\quad
k_BT_f<\Delta_s
\right\}.
```

For `C_e=gamma A T`, the **stable absorbed-photon spectral frontier** is then

```math
\boxed{
\lambda_{max}^{stable}(D;A)
=\sup_{T_f\in\mathcal F_D}
\frac{2\eta_{th}hc}
{\gamma A(T_f^2-T_0^2)}.
}
```

This is a useful endpoint for the present reduction:

- explicit `C` has disappeared;
- `L` appears only through the physically meaningful damping ratio `R_hot/L`;
- the remaining input is a small set of measurable or microscopically calculable constitutive functions.

## 8. What this establishes

Within the present model stack:

1. the MQT capacitance floor can be represented by one time `tau_Q`;
2. optimized phase capture is independent of `L` and `C` separately;
3. damping depends on `R_hot/L`, not on `R_hot`, `L`, and `C` independently once `C=C_min,Q`;
4. a closed wavelength-dark-count-capture-time bound follows near a smooth thermally controlled fold;
5. the `4/3` spectral scaling is the direct composition of the generic fold `3/2` barrier law with graphene `E~T^2` calorimetry.

## 9. What remains open

The following can still invalidate the quantitative closure:

- exact dissipative bounce action and prefactor replacing the cubic `alpha_Q=7.2` diagnostic;
- frequency-dependent damping rather than a scalar `R_hot`;
- CPR/fold behavior far enough from the local saddle-node that the `K_T` approximation fails;
- nonequilibrium rather than thermal early-time Josephson current;
- contact heat leakage and non-`T^4` cooling;
- stochastic basin capture and retrapping;
- external readout/backaction.

The generic statement that faster detectors trade against dark counts is not itself a novelty route; current quantum-detector thermodynamics already establishes broad dark-count/dead-time tradeoffs. Any later paper claim must be specific to the superconducting fold/calorimetric closure and its coefficients.

## Status

**GO for continued theory. NO-GO for manuscript.**
