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

The short-junction simplification was replaced with the Titov–Beenakker secular equation **before** its short-junction approximation, evaluated at finite temperature with the Hagymasi–Kormanyos–Cserti Matsubara method.

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

Detailed record: `ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md`.

## Step 31: intermediate-length CPR validation strengthened

The arbitrary-length implementation was tested against the exact intermediate parameter family used by Hagymasi et al. rather than only against the analytic short limit:

```text
xi/L=0.91
mu/Delta0=0,20
T/Tc=0,0.18,0.35.
```

Using `T/Tc=0.01` as the numerical low-T proxy, the solver gives approximately

```text
mu=0:  S=0.329, 0.196, 0.063
mu=20: S=0.546, 0.250, 0.077
```

as temperature increases. This reproduces the published trend structure including the strongly sawtooth-like high-doping low-T CPR. The values are stable across enlarged transverse and Matsubara cutoffs.

Record: `HAGYMASI_CPR_VALIDATION_2026-08-15.md`.

## Step 32: realistic-interface CPR skewness cuts the ideal stability margin

Nanda et al. realistic interface calculations/measurements put representative low-T skewness near `S~0.19–0.28`, well below the ideal `S~0.55` high-doping result.

A shape-only interpolation toward those empirical scales was applied while holding the ideal `Ic(T)` amplitude ratio fixed. At `beta=0.8`, `Ic=3 uA`:

```text
S~0.27 -> T_fold~0.905 K, barrier~9.12 K, Cmin~160 fF
S~0.22 -> T_fold~0.841 K, barrier~7.14 K, Cmin~230 fF
S~0.19 -> T_fold~0.794 K, barrier~5.89 K, Cmin~307 fF.
```

The fold survives, but cold stability is weakened by roughly a factor of two to three relative to the ideal barrier. State separation is much less sensitive and remains around `0.22–0.24 Phi0`.

Record: `INTERFACE_SKEWNESS_SENSITIVITY_2026-08-15.md`.

## Step 33: reduced induced gap exposes a fixed-loop fragility threshold

The gap entering the graphene ABS spectrum was reduced while holding physical junction length, physical gate doping and loop inductance fixed. This changes `ell`, `mu/Delta`, physical `Ic` and `beta_L` self-consistently inside the equilibrium model.

With realistic-skewness shape stress and `L=87.76 pH`:

```text
r_Delta=1.0 -> barrier~9.10 K
0.6 -> ~3.29 K
0.4 -> ~0.94 K
0.3 -> ~0.21 K
0.24 -> ~0.002 K
0.22 -> selected metastable well absent.
```

Formal bistability disappears near `r_Delta~0.23–0.24` in this fixed-loop sensitivity calculation, but useful cold stability collapses much earlier.

Record: `INDUCED_GAP_SENSITIVITY_2026-08-15.md`.

## Step 34: inductance retuning rescues topology but not barrier energy

If `Ic` is reduced, restoring a chosen cold screening parameter requires

```math
L=\beta\Phi_0/(2\pi I_c)\propto I_c^{-1}.
```

At fixed normalized CPR shape, the physical barrier obeys

```math
\Delta U=E_Lu_b\propto L^{-1}\propto I_c.
```

Therefore inductance is a compensation knob but not a free cure.

For the realistic-skewness family retuned to `beta=0.8`:

```text
r=1.0: L~87.8 pH, barrier~9.10 K, Cmin~161 fF
r=0.6: L~111.5 pH, barrier~6.87 K, Cmin~215 fF
r=0.4: L~140.3 pH, barrier~5.22 K, Cmin~287 fF.
```

The fixed-L topology threshold is therefore not an architecture-level impossibility. Retuning preserves the fold while consuming barrier, current-readout and dynamic margin.

Record: `INDUCTANCE_RETUNING_CLOSURE_2026-08-15.md`.

## Step 35: finite dwell simplifies to a local relaxation-time criterion

For clean graphene

```math
C_e=\gamma AT,
\qquad P_{e-ph}=\Sigma A(T^4-T_0^4),
```

the local small-signal E-Ph time is

```math
\tau_{ep}(T)=\gamma/(4\Sigma T^2).
```

The exact infinite-photon-energy maximum dwell above the fold reduces for `T0 << Tf` to

```math
\boxed{t_{>,max}\simeq2\tau_{ep}(T_f).}
```

Hence a clean necessary dynamic condition is

```math
\boxed{
\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}]
<2\tau_{ep}(T_f).
}
```

or, on the damping branch,

```math
R_{hot}C_{min,Q}<\tau_{ep}(T_f).
```

Record: `RETUNED_DWELL_CLOSURE_2026-08-15.md`.

## Step 36: fast graphene diffusion was reinterpreted correctly

The earlier `~22 ps` cross-device diffusion estimate is **not** a 22-ps energy-decay time. Huang et al. explicitly use the fact that `l_D~230 um` is much larger than the sample to argue that diffusion rapidly homogenizes the electron temperature before E-Ph dissipation.

They identify direct heat leakage into MoRe contacts when `k_BT_e` exceeds the parent superconducting gap `Delta_s~1.3 meV`. At the reference `T_pk~2.5 K`, `k_BT_pk~0.215 meV`, so the present MoRe geometry is far below that leakage threshold.

This strengthens the lumped E-Ph dwell picture in the current temperature regime and removes the tentative idea that ordinary contact diffusion must dominate the cooling just because spatial diffusion is fast.

## Step 37: induced gap and parent-electrode gap were separated

A crucial design distinction is now explicit:

```text
Delta_ind -> ABS/CPR spectrum, Ic(T), thermal fold
Delta_s   -> parent-electrode quasiparticle escape threshold / thermal confinement.
```

Nanda et al. already indicate that the induced graphene gap can be smaller than bulk MoRe, so `Delta_ind < Delta_s` is physically plausible.

For graphene heat capacity, the simultaneous fold and conservative contact-confinement conditions

```math
T_f\le T_{pk}\lesssim \Delta_s/k_B
```

give the absorber-area window

```math
\frac{2\eta E_\gamma}{\gamma[(\Delta_s/k_B)^2-T_0^2]}
\le A\le
\frac{2\eta E_\gamma}{\gamma(T_f^2-T_0^2)}.
```

A nonempty conservative window requires simply

```math
\boxed{\Delta_s>k_BT_f.}
```

and its width ratio is approximately

```math
A_{max}/A_{min}\simeq(\Delta_s/k_BT_f)^2.
```

For the MoRe-parent baseline `Delta_s~1.3 meV`, `T_Delta~15.1 K`; at `Tf~0.905 K` the area margin is about `278x`. Parent-gap confinement is therefore not close to limiting the baseline.

This points toward a preferred **gap hierarchy**: engineer a thermally responsive smaller `Delta_ind` while retaining a high `Delta_s` parent electrode for calorimetric confinement, subject to enough `Ic` and cold barrier.

Record: `THERMAL_CONFINEMENT_GAP_CLOSURE_2026-08-15.md`.

## Step 38: recent ABS-engineering work closes another broad novelty route

Jung et al., Phys. Rev. Applied 26, 014078 (2026), systematically engineer proximity-JJ thermal sensitivity through channel length, transparency, carrier density and superconducting material, explicitly identifying the proximity-induced gap as a key variable.

Therefore Experiment 03 cannot claim novelty for optimizing ABS/Josephson thermal sensitivity or induced gap itself. The remaining research target is the narrower persistent-flux-capture feasibility/optimality/impossibility closure combining trigger, confinement, cold stability, dynamics and readout.

## Current interpretation

The branch has survived increasingly realistic static stresses but with much smaller margins than the ideal model suggested.

The current preferred materials picture is no longer a single-gap graphene/MoRe parameter sweep. It is a **two-gap design problem**:

```text
smaller engineered Delta_ind for thermal CPR response
+
high parent Delta_s for calorimetric confinement
+
retuned L/C for cold stability and write dynamics.
```

The dominant unresolved physics is now

```text
quantitative two-gap feasible-region map
realistic contact/transparency model for Ic(T) and CPR
nonequilibrium distribution during the photon pulse
dissipative MQT for the full CPR potential
stochastic fold passage/retrapping
real 8–14 um optical coupling and reset/readout.
```

Broad architecture novelty has repeatedly collided with prior art. The plausible paper route remains a **quantitative feasibility/optimality or impossibility closure** if it survives these next calculations and a dedicated patent/paper audit.
