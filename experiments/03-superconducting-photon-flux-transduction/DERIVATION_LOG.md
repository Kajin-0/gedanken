# Experiment 03 — DERIVATION_LOG

This is the chronological reasoning trail. It records successful steps, corrections, rejected assumptions and prior-art collisions. `CURRENT_STATE.md` is the compact live model; `CLAIM_LEDGER.md` controls claim status.

## 2026-08-15 — Steps 1–6: from superconducting photoconductivity to a latching optical write

The starting question was whether superconductivity could coexist with photoconductive / photovoltaic response. Below `T_c`, conventional DC photoconductivity is not the clean language because the condensate already supplies a zero-resistance channel. Useful optical observables are quasiparticle population, superfluid density, critical current, kinetic inductance, phase and flux.

Fluctuation-dissipation showed that an ideal cold superconducting storage channel can eliminate its ordinary finite-frequency resistive Johnson contribution, but **not** photon statistics, quasiparticle fluctuations, phase slips, MQT, vortices, stray photons, readout or reset errors.

A perfectly lossless photon-induced current has no passive reset and naturally accumulates state. This changed the target from a continuous photoconductor to a latching/integrating superconducting detector.

Internal superconducting gain does not beat Poisson photon statistics:

```math
NEP_\gamma=\sqrt{2Ph\nu/\eta}.
```

At 10 um, `E_gamma~123.98 meV`. Because this is far above ordinary superconducting pair-breaking scales, the requirement of dissipationless LWIR absorption was rejected. Preferred architecture:

```text
brief nonequilibrium / dissipative write
-> recovery
-> persistent superconducting storage.
```

## Steps 7–13: graphene calorimetry, rf-SQUID mapping and first stochastic model

Huang et al. 2026 established a useful photon-heated graphene/Josephson benchmark:

```text
active area ~100 um^2
thermal-model T_1p ~2.5 K
tau_ep ~75 ns
eta ~0.87 at DCR <1/s
eta ~0.75 at DCR <1/week.
```

A simple equal-peak-temperature energy scaling gives an initial 10-um absorber scale near `15.5 um^2`; this remains only an extrapolation.

The optical event was mapped to an rf-SQUID phase landscape. A first fixed-barrier thermal/MQT feasibility window was derived and found nonempty. Capacitance emerged as an MQT control knob because increasing `C` lowers plasma frequency while remaining potentially much faster than the thermal pulse.

A Generation-A / Generation-B split was adopted:

```text
A: small external flux tilt; prove the physics; not photovoltaic.
B: later attempt intrinsic phi0/diode/photogalvanic directionality.
```

## Steps 14–18: exact sinusoidal fold and deterministic tipping

For `phi_x=pi+delta`, `x=phi-pi`, the sinusoidal rf-SQUID potential is

```math
u(x)=\frac12(x-\delta)^2+\beta\cos x.
```

The metastable saddle-node obeys exactly

```math
\boxed{\delta=\tan a-a,}
\qquad
\boxed{\beta_c=\sec a.}
```

Thus the photon can eliminate the metastable well rather than rely on rare hot-state barrier hopping:

```math
\beta_{cold}>\beta_c>\beta_{hot}.
```

Near the fold:

```math
\Delta U\propto(\beta-\beta_c)^{3/2},
\qquad
\omega_m\propto(\beta-\beta_c)^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto(\beta-\beta_c)^{5/4}.
```

This exposed the core trigger-vs-dark-stability tension.

Sinusoidal checkpoint:

```text
delta=0.05
beta_cold=1.5
Ic=3 uA
beta_c=1.14712
required Ic drop=23.53 %
L=164.55 pH
cold barrier/k_B=9.443 K
local fp(C=200 fF)=24.80 GHz.
```

Important correction: adjacent rf-SQUID fluxoid labels do **not** imply measured `DeltaPhi=Phi0`. The exact state separation is `0.47526 Phi0 = 5.97 uA` for this checkpoint.

A deterministic RCSJ pulse below the fold gives central phase passage near 20 ps; raw phase motion is therefore unlikely to be the dominant slow process.

## Steps 19–20: major prior-art collisions

Broad novelty routes closed:

- Onen et al. 2020: single-photon-to-single-flux superconducting memory already demonstrated.
- Rochet et al. 2020: optical writing of persistent superconducting vortices already demonstrated.
- Zhou/Habif/Bocko/Feldman 2001: transient `I_c` suppression used to lower an rf-SQUID barrier and refreeze a flux state.
- Walsh/Huang: photon-heated graphene/Josephson switching is prior art.
- Solinas/Giazotto/Pepe: photon heating of an SNS weak link to modulate SQUID response is prior art.
- Mironov/Mel'nikov/Buzdin: illumination-driven superconducting phase-battery/vorticity physics is prior art.

The possible contribution narrowed to a quantitative closure, a narrower persistent-fold architecture, a zero-external-flux result or an impossibility bound.

## Steps 21–23: optical energy, general CPR and thermal transport

For arbitrary heat capacity, the static optical fold energy is

```math
\boxed{
E_{fold}=\frac1{\eta_{th}}\int_{T_0}^{T_f}C_e(T)dT.
}
```

The scalar `I_c(T)` picture was replaced by the full CPR/load-line formulation. Define

```math
I_* = \Phi_0/(2\pi L),
\quad
\mathcal I(x,T)=I_s(x,T)/I_*,
\quad
F=x-\delta-\mathcal I.
```

A fold obeys

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

For a general smooth fold:

```math
\Delta U\propto|p-p_f|^{3/2}.
```

Published graphene characteristic values `l_D~230 um`, `tau_ep~75 ns` imply a cross-device diffusivity scale near `0.705 m^2/s`. A `15.5 um^2` square absorber then has `L^2/D~22 ps`, comparable to the phase-passage scale and much shorter than the E-Ph scale.

## Steps 24–26: short-junction graphene model tested, then demoted

The Titov–Beenakker short-junction graphene CPR was implemented as a sensitivity model. It showed that CPR shape can radically change the fold threshold and produced a toy interior trigger/stability optimum.

But the Huang device has `L_JJ~600 nm`; using the quoted MoRe `Delta~1.3 meV` and `v_F~1e6 m/s` gives `xi~0.5 um`, so `L_JJ/xi~O(1)`. The short-junction closed form is therefore not controlled for that device.

The short-CPR results were demoted to sensitivity-only status. Arbitrary-length graphene-JJ theory became mandatory.

## Steps 27–29: capacitance closure and finite dwell-time impossibility condition

Inside the provisional cubic MQT model,

```math
\Gamma_Q(C)=\frac{\omega(C)}{2\pi}
\exp[-\alpha_Q\Delta U_c/(\hbar\omega(C))],
\qquad
\omega(C)=\sqrt{\kappa_c/(LC)},
```

solving `Gamma_Q=D` gives

```math
\boxed{
C_{min,Q}
=\frac{\hbar^2\kappa_c}{\alpha_Q^2\Delta U_c^2L}
\left[
W\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right)
\right]^2.
}
```

Dynamic upper bounds are

```math
C<t_>/(2R_{hot}),
\qquad
C<t_>^2/(g^2L).
```

For monotonic cooling,

```math
\boxed{
t_>(E_\gamma)=\int_{T_f}^{T_{pk}}\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

For idealized clean graphene, `C_e=gamma A T`, `P=Sigma A(T^4-T0^4)`, the time above a fixed fold has a finite maximum even as `T_pk -> infinity`:

```math
\boxed{
t_{>,max}
=\frac{\gamma}{4\Sigma T_0^2}
\ln\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right).
}
```

Thus `t_req >= t_>,max` is a model-level **impossibility condition**: no larger photon energy rescues an intrinsically too-slow write circuit under this cooling law.

The compact necessary closure became

```math
E_\gamma\ge E_{fold},
```

```math
t_>(E_\gamma)\ge
\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}],
```

plus cold thermal stability.

Detailed derivation: `FEASIBILITY_CLOSURE_2026-08-15.md`.

## Step 30: arbitrary-length graphene CPR implemented and validated

The short-junction simplification was replaced with the Titov–Beenakker secular equation **before** its short-junction approximation, evaluated at finite temperature with the Hagymási–Kormányos–Cserti Matsubara method.

Dimensionless model:

```math
\ell=\Delta_0L_{JJ}/(\hbar v_F),
\qquad
\mu_r=\mu/\Delta_0,
\qquad
Q=qL.
```

Canonical implementation:

```text
calculations/arbitrary_length_graphene_cpr.py
```

Validation:

1. At `ell=0.01`, `mu=0`, the normalized CPR converges to Titov–Beenakker Eq.20 at the sub-percent-to-percent level on the current finite grids.
2. At `ell~1.1`, the low-T CPR becomes strongly forward-skewed and thermally softens, qualitatively matching the expected intermediate-length graphene-JJ behavior.
3. Finite-doping fold values require large transverse cutoff; `Qmax~30` was retained after convergence testing.

At `ell=1.1`, `delta=0.05`, cold normalized fold:

```text
mu/Delta0=0    beta_fold~0.463
mu/Delta0=10   beta_fold~0.325
mu/Delta0=20   beta_fold~0.200.
```

For `mu/Delta0=20`, `beta_cold=0.8`, `Ic0=3 uA`:

```text
T_fold                     ~1.118 K
reference heat fraction    ~0.200
cold barrier/k_B           ~16.70 K
L                           87.76 pH
provisional C_min,Q        ~71 fF
state separation           ~0.2535 Phi0
current-state gap          ~5.97 uA.
```

This is substantially more favorable than the short-junction toy result at similar beta (`T_fold~2.17 K`, provisional `C_min,Q~0.52 pF`).

Doping produces a particularly useful model trend: at `beta_cold=0.8`, `T_fold` remains near `1.1 K` from `mu/Delta0=0` to `20`, while the cold barrier rises from about `7.0 K` to `16.7 K` and provisional `C_min,Q` falls from about `262 fF` to `71 fF`. In the ideal model, doping primarily improves **cold-state stability**, not optical threshold.

Detailed record: `ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md`.

## Current interpretation

The ideal static circuit/thermal feasibility is now stronger than at the start of the branch. Simple photon energy is no longer the leading concern in the idealized model.

The dominant unresolved physics is now:

```text
nonideal SG interface transparency / contact doping
self-consistent or calibrated arbitrary-length CPR
nonequilibrium electron distribution during the early photon pulse
dissipative MQT for the full CPR potential
finite-rate stochastic fold passage and retrapping
real 8–14 um optical coupling and reset/readout.
```

Broad architecture novelty has repeatedly collided with prior art. The most plausible surviving paper route is increasingly a **quantitative feasibility/optimality or impossibility closure**, if it survives the next nonideal/dynamical calculations and a dedicated patent/paper audit.
