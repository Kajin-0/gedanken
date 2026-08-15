# Experiment 03 — Photon/Fold/Stability Feasibility Closure — 2026-08-15

## Purpose

Collect the first compact necessary-condition chain linking

```text
photon energy / absorber heat capacity
-> temperature-dependent Josephson CPR fold
-> cold thermal/MQT stability
-> capacitance
-> write-time phase/damping constraints.
```

This is an **exploratory model closure**, not a validated device theorem and not a novelty claim.

## 1. General CPR fold

Define

```math
I_* = \frac{\Phi_0}{2\pi L},
\qquad
\mathcal I(x,T)=\frac{I_s(x,T)}{I_*},
```

and phase force

```math
F(x,T)=x-\delta-\mathcal I(x,T).
```

A fold occurs when

```math
\boxed{F(x_f,T_f)=0,}
\qquad
\boxed{\partial_xF(x_f,T_f)=0.}
```

Equivalently,

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

`T_f` is therefore determined by the **full temperature-dependent CPR**, not by `I_c(T)` alone unless the CPR changes only by a scalar amplitude.

## 2. Optical energy condition

Let `C_e(T)` be the absorber electronic heat capacity and let `eta_th` be the fraction of absorbed photon energy retained in the electronic system on the relevant initial thermalization timescale.

The peak electronic temperature is set by

```math
\eta_{th}E_\gamma
=
\int_{T_0}^{T_{pk}} C_e(T)dT.
```

A necessary static fold condition is

```math
\boxed{T_{pk}\ge T_f.}
```

Thus the static optical threshold is

```math
\boxed{
E_{fold}
=\frac{1}{\eta_{th}}
\int_{T_0}^{T_f} C_e(T)dT.
}
```

For graphene-like

```math
C_e=\gamma_S A T,
```

this becomes

```math
\boxed{
E_{fold}
=\frac{\gamma_S A}{2\eta_{th}}
(T_f^2-T_0^2).
}
```

## 3. Finite write-time condition

Static crossing is not sufficient. Let `t_>(E_gamma)` be the interval during which the thermally evolving CPR remains beyond the fold.

For a spatially lumped monotonic cooling law

```math
C_e(T)\frac{dT}{dt}=-P_{cool}(T),
```

the time above the fold is

```math
\boxed{
t_>(E_\gamma)
=
\int_{T_f}^{T_{pk}(E_\gamma)}
\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

A necessary capture condition is

```math
\boxed{
t_>(E_\gamma)\ge t_{req}(C),
}
```

where a minimal deterministic timescale budget is

```math
\boxed{
t_{req}(C)
=\max\!\left[
t_{diff},
g\sqrt{LC},
2R_{hot}C
\right].
}
```

Here

```text
t_diff      absorber thermal-spreading scale
g sqrt(LC)  phase-passage / settling scale
a factor g  is extracted from the dimensionless phase trajectory
2 R_hot C   simple RCSJ damping-envelope scale.
```

This condition is necessary, not sufficient; noise-driven basin selection and retrapping remain.

## 4. Clean-graphene cooling example

For the idealized lumped laws

```math
C_e=\gamma_S A T,
\qquad
P_{e-ph}=\Sigma A(T^4-T_0^4),
```

the area cancels from the cooling time:

```math
\boxed{
t_>
=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\!\left[
\frac{(T_{pk}^2-T_0^2)(T_f^2+T_0^2)}
{(T_{pk}^2+T_0^2)(T_f^2-T_0^2)}
\right].
}
```

Define

```math
q_f=\frac{T_f^2-T_0^2}{T_f^2+T_0^2},
\qquad
R_t=\exp\!\left(\frac{4\Sigma T_0^2}{\gamma_S}t_{req}\right).
```

The minimum peak temperature that supplies the required dwell time is obtained from

```math
q_{pk}=R_t q_f,
```

provided

```math
\boxed{R_tq_f<1.}
```

Then

```math
\boxed{
T_{pk,min}^2
=T_0^2\frac{1+R_tq_f}{1-R_tq_f}.
}
```

The corresponding photon threshold is

```math
\boxed{
E_{\gamma,min}
=\frac{\gamma_S A}{2\eta_{th}}
(T_{pk,min}^2-T_0^2).
}
```

### Finite maximum dwell time

For `T^4` electron-phonon cooling, even formally taking `T_pk -> infinity` gives a finite maximum interval above a fixed fold temperature:

```math
\boxed{
t_{>,max}(T_f)
=
\frac{\gamma_S}{4\Sigma T_0^2}
\ln\!\left(
\frac{T_f^2+T_0^2}{T_f^2-T_0^2}
\right).
}
```

For `T_0 << T_f`,

```math
\boxed{
t_{>,max}\simeq\frac{\gamma_S}{2\Sigma T_f^2}.}
```

Therefore

```math
\boxed{t_{req}\ge t_{>,max}}
```

is an **impossibility condition within this lumped clean-graphene cooling model**: no arbitrarily energetic photon can maintain the electron system above the fold long enough because higher-temperature electron-phonon cooling accelerates strongly.

This is a model result, not yet a device-independent theorem.

## 5. Cold thermal stability

Let the cold metastable barrier be `Delta U_c`. A standard thermal-activation condition for dark target `D` is approximately

```math
\boxed{
\Delta U_c
\gtrsim
k_BT_0\ln\!\left(\frac{\Omega_T}{D}\right).
}
```

Near a generic nondegenerate fold, if `epsilon` measures cold distance from the fold and

```math
\Delta U_c=K\epsilon^{3/2},
```

then the thermal dark-rate constraint gives

```math
\boxed{
\epsilon
\gtrsim
\left[
\frac{k_BT_0\ln(\Omega_T/D)}{K}
\right]^{2/3}.
}
```

This quantifies the conflict between a low optical trigger threshold and cold thermal stability.

## 6. Provisional quantum-stability / capacitance constraint

Retain, only as the present diagnostic MQT model,

```math
\Gamma_Q(C)
=\frac{\omega(C)}{2\pi}
\exp\!\left[-\alpha_Q
\frac{\Delta U_c}{\hbar\omega(C)}\right],
```

with

```math
\omega(C)=\sqrt{\frac{\kappa_c}{LC}},
\qquad
\alpha_Q\approx7.2.
```

For fixed cold potential (`Delta U_c`, `kappa_c`, `L` fixed), the capacitance required to reach target diagnostic dark rate `D` can be solved exactly within this model:

```math
\boxed{
C_{min,Q}
=
\frac{\hbar^2\kappa_c}
{\alpha_Q^2\Delta U_c^2L}
\left[
W\!\left(
\frac{\alpha_Q\Delta U_c}
{2\pi\hbar D}
\right)
\right]^2.
}
```

`W` is the principal Lambert-W branch for the positive argument above.

This is **not** an exact dissipative rf-SQUID MQT formula. Its value is that it makes the capacitance tradeoff explicit within the same cubic-barrier diagnostic used in the initial model.

## 7. Dynamic upper bounds on capacitance

The two circuit settling requirements imply

```math
\boxed{
C<C_{max,R}
=\frac{t_>}{2R_{hot}},
}
```

and

```math
\boxed{
C<C_{max,\phi}
=\frac{t_>^2}{g^2L}.
}
```

Therefore a necessary nonempty capacitance window is

```math
\boxed{
C_{min,Q}(D)
< C <
\min(C_{max,R},C_{max,\phi}).
}
```

Because increasing `C` leaves the **static fold threshold** unchanged while improving the provisional MQT action and slowing both phase motion and damping, the capacitance that minimizes write-time burden subject only to this MQT constraint is

```math
\boxed{C\simeq C_{min,Q}.}
```

Additional readout, parasitic-capacitance or noise constraints can move that optimum.

## 8. Compact necessary feasibility chain

For the current model class, a candidate device must satisfy all three:

```math
\boxed{
E_\gamma\ge E_{fold}
}
```

plus

```math
\boxed{
C_{min,Q}(D)<
\min\!\left[
\frac{t_>(E_\gamma)}{2R_{hot}},
\frac{t_>^2(E_\gamma)}{g^2L}
\right]
}
```

and

```math
\boxed{
\Delta U_c
\gtrsim k_BT_0\ln(\Omega_T/D).
}
```

A more compact optimized necessary condition is obtained by setting `C=C_min,Q` and defining

```math
\boxed{
t_{req}^*
=
\max\!\left[
t_{diff},
g\sqrt{LC_{min,Q}},
2R_{hot}C_{min,Q}
\right].
}
```

Then photon-triggered persistent capture requires at minimum

```math
\boxed{
t_>(E_\gamma)\ge t_{req}^*.}
```

For the clean-graphene cooling example this can be inverted analytically to `E_gamma,min` using Section 4.

## 9. Short-graphene CPR sensitivity example

This section is intentionally **not** a prediction for the 2026 MoRe/graphene detector. Its `L_JJ ~ 0.6 um` is comparable to `hbar v_F/Delta ~ 0.5 um`, so the Titov-Beenakker short-junction closed form is not controlled for that device. The table below only demonstrates the coupled optimization.

Using the short ballistic Dirac-point CPR sensitivity model, the current 15.5-um^2 thermal scaling, and the provisional MQT target `D=1e-6 s^-1`:

| beta_cold | T_fold (K) | eta_th,min to reach fold | cold barrier / k_B (K) | C_min,Q |
|---:|---:|---:|---:|---:|
| 0.60 | 0.787 | 0.099 | 0.454 | 30.3 pF |
| 0.70 | 1.506 | 0.363 | 2.048 | 2.10 pF |
| 0.80 | 2.172 | 0.755 | 4.409 | 0.520 pF |
| 0.85 | 2.480 | 0.984 | 5.805 | 0.314 pF |
| 0.90 | 2.769 | 1.227 | 7.309 | 0.206 pF |

Interpretation:

- moving closer to the fold (`beta_cold` smaller) dramatically reduces optical energy needed;
- but the cold barrier collapses and the capacitance required for quantum stability grows sharply;
- moving too far from the fold makes the photon energy insufficient under the fixed 15.5-um^2 reference scaling (`eta_th,min > 1` by beta=0.9);
- therefore an **interior operating corridor** appears in the toy model.

For example, at `beta_cold=0.8`, `C_min,Q~0.52 pF`. If the useful interval above the fold is `10 ns`, the simple damping bound requires

```math
R_{hot}<\frac{10\,ns}{2(0.52\,pF)}\approx9.6\,k\Omega.
```

The phase-passage bound is much looser at this point; damping rather than raw phase speed is the likely dynamic capacitance limit.

Again: the numerical corridor is not transferable to the intermediate-length MoRe/graphene device without an arbitrary-length CPR calculation.

## 10. What is established vs open

### Established within the present model

- general CPR/load-line fold conditions;
- universal `3/2` barrier scaling near a smooth fold;
- static optical fold-energy condition;
- general cooling-time integral above the fold;
- exact clean-graphene `T^4` cooling integral and finite-maximum-dwell result;
- Lambert-W capacitance solution inside the provisional MQT rate model;
- necessary nonempty capacitance window;
- a real three-way optimization between optical trigger energy, cold stability and write dynamics.

### Not established

- the actual arbitrary-length `I_s(phi,T_e)` for the proposed LWIR weak link;
- the exact dissipative MQT rate;
- `R_hot(T_e)` and finite-rate retrapping;
- system optical absorptance at 8–14 um;
- high-fidelity stochastic capture probability;
- any publication novelty.

## 11. Next decisive calculation

Use an arbitrary-length graphene/SNS Josephson model or measured CPR to obtain

```text
I_s(phi,T)
-> fold curve T_f(delta,L,...)
-> cold exact barrier and curvature
-> C_min,Q
-> thermal pulse t_>(E_gamma)
-> stochastic RCSJ basin capture.
```

Only then should the toy operating corridor be promoted or rejected.

## Status

**GO for continued theory. NO-GO for manuscript.**
