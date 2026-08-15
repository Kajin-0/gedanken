# Experiment 03 — DERIVATION_LOG

This file records the chronological logical trail. It is not a polished derivation and it does not establish novelty.

## 2026-08-15 — Step 1: superconducting + photoconductive / photovoltaic motivation

Initial question: can a material/device be both superconducting and optically conductive or photovoltaic?

Key refinement: below Tc, conventional DC photoconductivity is a poor language because the condensate already gives a zero-resistance channel. The more useful observables are quasiparticle conductivity, superfluid density, critical current, kinetic inductance, phase, and persistent flux.

## Step 2: Johnson-noise question

For an ideal superconducting sensing/storage channel,

```math
S_V(\omega)=4k_BT\,\mathrm{Re}\,Z(\omega)
```

in the classical finite-frequency limit, so Re Z -> 0 removes the ordinary resistive Johnson contribution of that channel.

Important correction: zero resistance does not imply zero total fluctuations. An almost lossless RL loop has its equilibrium current fluctuations pushed toward arbitrarily low frequency as R -> 0, and an isolated fluxoid state is instead metastably frozen. Other noise/false-event mechanisms remain.

## Step 3: lossless detector implies memory

If each photon adds a superconducting current increment and there is no relaxation,

```math
I_s(t)=I_0+N_\gamma(t)\Delta I_\gamma.
```

Therefore a perfectly lossless device naturally behaves as an integrator / memory rather than a stationary linear photoconductor.

This motivated a latching detector rather than forcing a conventional continuous-current architecture.

## Step 4: photon statistics survive internal gain

For a linear photon-triggered current impulse with lifetime tau, both responsivity and photon shot noise acquire the same transfer function and internal gain. Referred to incident optical power, the Poisson photon-noise limit remains

```math
\mathrm{NEP}_\gamma=\sqrt{2Ph\nu/\eta}.
```

Therefore superconducting gain cannot beat photon-arrival statistics; the possible advantage is suppression of detector-added dissipation/noise.

## Step 5: flux-state architecture

A photon-to-flux detector was proposed:

```text
photon -> nonequilibrium excitation -> phase perturbation -> fluxoid write -> persistent flux
```

For a loop inductance L,

```math
I_n\sim n\Phi_0/L,
\qquad
U_n\sim n^2\Phi_0^2/(2L).
```

At 10 µm,

```math
E_\gamma\approx123.98\,\mathrm{meV}.
```

The one-flux energy scale requires

```math
L\gtrsim\Phi_0^2/(2\eta_E h\nu).
```

For eta_E=1 this is about 108 pH. Thus nanohenry/sub-nanohenry loops are not excluded by simple energy conservation.

## Step 6: pair breaking is not avoidable in ordinary LWIR superconductors

At 10 µm the photon frequency is about 30 THz and energy about 124 meV. Requiring h nu < 2 Delta in weak-coupling BCS would imply an unrealistically high Tc of order 400 K.

Therefore the practical architecture should not require sub-gap absorption. It should tolerate a brief quasiparticle/hot-electron event and use that event to write a persistent superconducting state.

## Step 7: graphene Josephson calorimeter as benchmark

Published single-photon graphene Josephson switching at 1550 nm provides a concrete benchmark for low-electronic-heat-capacity calorimetric phase escape.

The initial conversation used approximate benchmark values

```text
A ~ 100 um^2
T_pk ~ 2.5 K
tau_ep ~ 75 ns
```

and scaled the absorber area as A proportional to photon energy to preserve approximately the same hot-electron excursion. This gives

```math
A_{10\,\mu m}\sim100(1.55/10)\approx15.5\,\mu\mathrm m^2.
```

This is only a first scaling estimate.

## Step 8: rf-SQUID mapping

Minimal phase potential:

```math
U(\phi,T_e)=\frac{E_L}{2}(\phi-\phi_x)^2-E_J(T_e)\cos(\phi-\phi_0),
```

with

```math
E_L=(\Phi_0/2\pi)^2/L,
E_J=\Phi_0 I_c/(2\pi),
\beta_L=2\pi L I_c/\Phi_0.
```

Photon heating lowers I_c and therefore changes the barrier structure. The desired event is not simply "resistance appears" but a transition into a neighboring metastable fluxoid well followed by recovery of superconductivity.

## Step 9: passive-barrier thermal bound

For a generic thermal dark escape

```math
\Gamma_{\rm dark}=\Omega e^{-E_b/(k_BT)},
```

requiring a target dark rate D gives

```math
E_b\gtrsim k_BT\ln(\Omega/D).
```

If the photon itself must directly supply that barrier energy, then

```math
h\nu\gtrsim k_BT\ln(\Omega/D).
```

With Omega = 1e11 s^-1 and D = 1e-6 s^-1, the simple 10-µm scale gives T of order 37 K. This motivated using a metastable/bias energy landscape where the photon acts as a trigger rather than paying the full final-state energy.

## Step 10: stochastic photon/MQT feasibility window

Provisional hot-state thermal escape:

```math
\Gamma_{\rm ph}\simeq\Gamma_0 e^{-\Delta U/(k_BT_{\rm pk})}.
```

Demanding P_det > eta during a hot interval tau gives

```math
\Delta U < k_BT_{\rm pk}\ln\left[\frac{\Gamma_0\tau}{-\ln(1-\eta)}\right].
```

Using the standard approximate cubic-barrier MQT form

```math
\Gamma_{\rm MQT}\sim\Gamma_0\exp[-7.2\Delta U/(\hbar\omega_p)],
```

and demanding Gamma_MQT < D gives

```math
\Delta U > \frac{\hbar\omega_p}{7.2}\ln(\Gamma_0/D).
```

Hence the provisional nonempty-window condition

```math
\frac{\hbar\omega_p}{7.2}\ln\frac{\Gamma_0}{D}
<k_BT_{\rm pk}\ln\left[\frac{\Gamma_0\tau}{-\ln(1-\eta)}\right].
```

This is the most important current mathematical checkpoint, but it must be rederived for the actual rf-SQUID potential/damping rather than imported as a universal law.

## Step 11: plasma-frequency design insight

The provisional MQT exponent scales inversely with omega_p. Therefore reducing plasma frequency can exponentially suppress quantum dark switching while remaining much faster than the calorimetric pulse.

Because

```math
f_p\propto\sqrt{I_c/C},
```

increasing junction capacitance is a possible control knob. The exploratory parameter window suggested 30–50 GHz as potentially more attractive than maximizing f_p.

## Step 12: directionality

For two thermally activated directional barriers,

```math
\Gamma_\pm\propto e^{-\Delta U_\pm/(k_BT_{\rm pk})},
```

so

```math
P_+=\frac1{1+\exp[-(\Delta U_- - \Delta U_+)/(k_BT_{\rm pk})]}.
```

Thus

```math
\Delta U_- - \Delta U_+ > k_BT_{\rm pk}\ln[P_+/(1-P_+)].
```

At T_pk = 2.5 K this is about 0.47 meV for 90% and 0.99 meV for 99% directional capture in the simple thermal model.

## Step 13: two-generation strategy

Generation A should use a small external flux bias to prove photon -> persistent-flux mapping with the least additional speculative physics.

Generation B should replace the external bias with an intrinsic phi0 / Josephson-diode / inversion-breaking element to obtain a self-directed, photovoltaic-like superconducting detector.

## Current next step

Replace all constant-barrier estimates with the actual time-dependent stochastic dynamics of the chosen rf-SQUID/Josephson potential and explicitly compute P+, P-, P0 and each dark mechanism.
