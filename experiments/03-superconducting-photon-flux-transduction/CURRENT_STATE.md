# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**.

## 1. Current physical question

Can one absorbed LWIR photon drive a Josephson/rf-SQUID circuit through a directionally selected fold, after which the circuit recovers into a persistent superconducting flux state, while cold false-switching remains extremely low?

Generation A deliberately uses a small external flux tilt. It is **not photovoltaic**. Generation B may later test intrinsic zero-external-flux directionality.

Preferred write sequence:

```text
8–14 um photon
 -> hot-electron / quasiparticle pulse
 -> temperature-dependent Josephson CPR changes
 -> metastable load-line intersection reaches a fold and disappears
 -> phase moves to favored basin
 -> CPR recovers
 -> persistent flux state remains
```

The optical write may be dissipative. The stored state can be superconducting and nondissipative.

## 2. Noise statement

For an ideal cold storage channel with `Re Z -> 0`, the ordinary finite-frequency resistive Johnson contribution vanishes. This does **not** imply zero total noise or zero dark counts.

Relevant limits now are

```text
thermal phase escape
macroscopic quantum tunneling (MQT)
residual quasiparticles
vortices / trapped flux
stray photons
readout backaction
reset errors
photon statistics.
```

The important detector metrics are therefore `P_capture`, `P_wrong`, DCR, stored-state SNR, reset time/energy and system optical efficiency.

## 3. Preferred general CPR formulation

Define

```math
I_* = \frac{\Phi_0}{2\pi L},
\qquad
\mathcal I(x,T)=\frac{I_s(x,T)}{I_*},
```

with phase force

```math
F(x,T)=x-\delta-\mathcal I(x,T).
```

A static fold obeys

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

Geometrically, the temperature-dependent CPR is tangent to the loop-inductance load line.

If

```math
\mathcal I(x,T)=\beta(T)f(x),
```

then

```math
\boxed{\beta_c=1/f'(x_f),}
\qquad
\boxed{\delta=x_f-f(x_f)/f'(x_f).}
```

The old sinusoidal result is the special case `f(x)=sin x`:

```math
\delta=\tan a-a,
\qquad
\beta_c=\sec a.
```

A sinusoidal benchmark with `delta=0.05`, `beta_cold=1.5`, `I_c=3 uA` gives

```text
beta_c                    = 1.14712
required scalar Ic drop   = 23.53 %
L                         = 164.55 pH
cold barrier / k_B        = 9.443 K
local fp at C=200 fF      = 24.80 GHz
state separation          = 0.4753 Phi0 = 5.97 uA.
```

This is a benchmark only, not the preferred physical CPR.

## 4. Universal near-fold structure

For any smooth one-parameter nondegenerate fold,

```math
F\simeq F_p\Delta p+\frac12F_{xx}(x-x_f)^2.
```

The disappearing barrier is

```math
\boxed{
\Delta U
\simeq
\frac{4\sqrt2}{3}E_L
\frac{|F_p\Delta p|^{3/2}}
{\sqrt{|F_{xx}|}}.
}
```

Therefore

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto|p-p_f|^{5/4}.
```

This is the central physical tradeoff: moving cold operation closer to the fold reduces the photon perturbation needed but rapidly damages cold quantum stability.

## 5. Optical fold-energy condition

For arbitrary electronic heat capacity,

```math
\eta_{th}E_\gamma
=\int_{T_0}^{T_{pk}}C_e(T)dT.
```

The static optical threshold is

```math
\boxed{
E_{fold}
=\frac1{\eta_{th}}
\int_{T_0}^{T_f}C_e(T)dT.
}
```

For `C_e=gamma_S A T`,

```math
\boxed{
E_{fold}
=\frac{\gamma_S A}{2\eta_{th}}(T_f^2-T_0^2).
}
```

`T_f` must come from the **full CPR fold**, not an assumed `I_c(T)` unless the CPR is shape-invariant.

## 6. Finite dwell time above the fold

Static peak temperature is insufficient. For lumped monotonic cooling

```math
C_e(T)\dot T=-P_{cool}(T),
```

the available write interval is

```math
\boxed{
t_>(E_\gamma)
=\int_{T_f}^{T_{pk}(E_\gamma)}
\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

A minimal necessary settling budget is

```math
\boxed{
t_{req}(C)=
\max\left[t_{diff},\ g\sqrt{LC},\ 2R_{hot}C\right].
}
```

The detector requires

```math
\boxed{t_>(E_\gamma)\ge t_{req}(C).}
```

For the published graphene characteristic values `l_D~230 um`, `tau_ep~75 ns`, the inferred scale is `D~0.705 m^2/s`. A 15.5-um^2 square absorber then has `L_abs^2/D~22 ps`, comparable to the current ~20-ps phase-passage benchmark and far shorter than the quoted E-Ph scale.

## 7. Clean-graphene cooling closure

For the idealized lumped laws

```math
C_e=\gamma_SAT,
\qquad
P_{e-ph}=\Sigma A(T^4-T_0^4),
```

```math
\boxed{
t_>
=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\left[
\frac{(T_{pk}^2-T_0^2)(T_f^2+T_0^2)}
{(T_{pk}^2+T_0^2)(T_f^2-T_0^2)}
\right].
}
```

A nontrivial consequence is a finite maximum dwell time even for `T_pk -> infinity`:

```math
\boxed{
t_{>,max}
=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right)
\simeq\frac{\gamma_S}{2\Sigma T_f^2}
}
```

for `T_0 << T_f`.

Thus

```math
\boxed{t_{req}\ge t_{>,max}}
```

is an impossibility condition **within this lumped `T^4` cooling model**: increasing photon energy cannot overcome an intrinsically too-slow write circuit because high-temperature cooling accelerates strongly.

## 8. Cold stability and capacitance window

Thermal false switching requires approximately

```math
\Delta U_c\gtrsim k_BT_0\ln(\Omega_T/D).
```

For the present provisional cubic-form quantum-escape model,

```math
\Gamma_Q(C)
=\frac{\omega(C)}{2\pi}
\exp\left[-\alpha_Q\frac{\Delta U_c}{\hbar\omega(C)}\right],
\qquad
\omega(C)=\sqrt{\frac{\kappa_c}{LC}},
```

with `alpha_Q~7.2`, target DCR `D` gives

```math
\boxed{
C_{min,Q}
=
\frac{\hbar^2\kappa_c}
{\alpha_Q^2\Delta U_c^2L}
\left[
W\left(
\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}
\right)
\right]^2.
}
```

This Lambert-W result is exact algebra **inside the provisional MQT rate model**, not an exact dissipative rf-SQUID DCR.

Write dynamics gives

```math
C<C_{max,R}=\frac{t_>}{2R_{hot}},
```

```math
C<C_{max,\phi}=\frac{t_>^2}{g^2L}.
```

Therefore

```math
\boxed{
C_{min,Q}<C<\min(C_{max,R},C_{max,\phi}).
}
```

Subject only to these monotonic constraints, the smallest write burden occurs near `C=C_min,Q`.

## 9. Current compact feasibility closure

Define

```math
\boxed{
t_{req}^*=
\max\left[
t_{diff},\ g\sqrt{LC_{min,Q}},\ 2R_{hot}C_{min,Q}
\right].
}
```

A candidate device must at minimum satisfy

```math
\boxed{E_\gamma\ge E_{fold},}
```

```math
\boxed{t_>(E_\gamma)\ge t_{req}^*,}
```

```math
\boxed{\Delta U_c\gtrsim k_BT_0\ln(\Omega_T/D).}
```

This is the strongest current theoretical object. It links photon energy, heat capacity, the full CPR/load-line fold, cold metastability, provisional MQT suppression, capacitance and write dynamics.

Detailed derivation: `FEASIBILITY_CLOSURE_2026-08-15.md`.

## 10. Graphene CPR model boundary

Measured ballistic graphene CPRs are strongly forward-skewed at low temperature and evolve toward sinusoidal at higher temperature. Junction length and interface properties matter.

The Huang 2026 MoRe/graphene photon detector has a 600-nm junction. Using the quoted MoRe gap scale `Delta~1.3 meV` and `v_F~1e6 m/s` gives

```math
\xi\sim\hbar v_F/\Delta\approx0.51\,\mu m,
```

so `L_JJ/xi~1.2`.

Therefore the Titov-Beenakker short-junction closed form is **not controlled** for that device. Arbitrary-length CPR theory or measured `I_s(phi,T)` is required.

The short-junction Dirac calculation is retained only as a sensitivity study.

## 11. Toy short-Dirac optimization

For the current 15.5-um^2 thermal scaling and provisional `D=1e-6 s^-1` MQT target:

| beta_cold | T_fold | eta_th,min | cold barrier/k_B | C_min,Q |
|---:|---:|---:|---:|---:|
| 0.60 | 0.787 K | 0.099 | 0.454 K | 30.3 pF |
| 0.70 | 1.506 K | 0.363 | 2.048 K | 2.10 pF |
| 0.80 | 2.172 K | 0.755 | 4.409 K | 0.520 pF |
| 0.85 | 2.480 K | 0.984 | 5.805 K | 0.314 pF |
| 0.90 | 2.769 K | 1.227 | 7.309 K | 0.206 pF |

This illustrates an **interior operating corridor**:

- too close to the fold: optical trigger easy, quantum stability expensive in capacitance;
- too far: cold state robust, but the fixed photon energy cannot reach the fold.

At `beta=0.8`, if `t_>=10 ns`, `C_min,Q~0.52 pF` implies the simple damping requirement

```math
R_{hot}\lesssim9.6\,k\Omega.
```

The numbers are not transferable to the intermediate-length real junction.

## 12. Prior-art boundary

Do **not** claim novelty for:

```text
LWIR superconducting single-photon detection
infrared photon -> hot graphene -> Josephson switching
photon heating -> proximity-JJ Ic suppression -> SQUID voltage detection
single photon -> persistent superconducting single-flux memory
optical heating -> permanent superconducting flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven superconducting phase batteries/vorticity
non-sinusoidal temperature-dependent graphene CPRs.
```

Important direct collisions include Walsh/Huang, Solinas-Giazotto-Pepe, Onen, Rochet, Zhou/Habif/Bocko/Feldman, and Mironov/Mel'nikov/Buzdin. See `LITERATURE_LEDGER.md`.

## 13. Immediate next calculation

The static theory is sufficiently developed. The decisive remaining chain is

```text
arbitrary-length realistic I_s(phi,T)
 -> exact fold curve T_f
 -> exact cold barrier/curvature
 -> C_min,Q using improved dissipative MQT
 -> thermal pulse with diffusion/contact/e-ph loss
 -> stochastic finite-rate fold passage
 -> P_capture, P_wrong, P_no-switch.
```

The most urgent physics input is a defensible arbitrary-length proximity-JJ CPR for a realistic 8–14-um absorber/Josephson geometry.

## 14. Current verdict

**GO for continued theory. NO-GO for manuscript.**

A nonempty idealized operating corridor exists, but broad architectural novelty has collided repeatedly with prior art. The remaining possible contribution is increasingly the **quantitative feasibility/optimality closure**, not the mere device concept.
