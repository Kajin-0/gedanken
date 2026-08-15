# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** NO-GO for manuscript until novelty and quantitative gates are passed.

## 1. Current physical idea

Use a superconducting loop with a photon-sensitive Josephson element so that one absorbed photon transiently changes the phase-escape landscape and is captured as a persistent fluxoid transition.

Working sequence:

```text
h nu -> nonequilibrium electronic/quasiparticle excitation
     -> I_c(T_e) and/or phase potential changes
     -> one directional phase escape becomes likely
     -> n -> n+1
     -> quasiparticles/electrons relax
     -> loop remains in new persistent fluxoid state
```

The current architecture intentionally separates the short dissipative write event from the long-lived superconducting storage/readout state.

## 2. Why this branch was opened

The motivating question was whether superconducting + photovoltaic detection could remove detector Johnson noise. The refined answer is:

- an ideal nondissipative superconducting storage channel has no ordinary finite-frequency Johnson-Nyquist floor because Re[Z] -> 0;
- this does not imply zero total fluctuations or zero dark counts;
- finite-temperature quasiparticles, phase slips, macroscopic quantum tunneling (MQT), stray photons, vortices, readout noise, and reset physics remain;
- a latching flux detector is better described by detection efficiency and false-switch rate than by Johnson noise alone.

## 3. Key equations retained from the initial derivation

### Photon energy

```math
E_\gamma = h\nu = hc/\lambda.
```

At 10 µm:

```math
E_\gamma \approx 1.986\times 10^{-20}\,\mathrm{J}\approx123.98\,\mathrm{meV}.
```

### Flux quantum

```math
\Phi_0=h/(2e)=2.068\times10^{-15}\,\mathrm{Wb}.
```

For an idealized loop state with one stored flux quantum:

```math
I_1\sim\Phi_0/L,
\qquad
U_1\sim\Phi_0^2/(2L).
```

A photon-only energy bound is therefore

```math
L\gtrsim \Phi_0^2/(2\eta_E h\nu).
```

At 10 µm and eta_E=1 this scale is about 108 pH. This is an energetic feasibility scale only, not a transition-probability prediction.

### rf-SQUID / phase-potential model

Use as the minimal starting point

```math
U(\phi,T_e)=\frac{E_L}{2}(\phi-\phi_x)^2-E_J(T_e)\cos(\phi-\phi_0),
```

with

```math
E_L=\frac1L\left(\frac{\Phi_0}{2\pi}\right)^2,
\qquad
E_J(T_e)=\frac{\Phi_0 I_c(T_e)}{2\pi},
\qquad
\beta_L=\frac{2\pi L I_c}{\Phi_0}.
```

Multiple metastable fluxoid wells require a sufficiently hysteretic regime, nominally beta_L > 1 for the simple rf-SQUID model.

### Photon heating benchmark

For a graphene-like electronic calorimeter with C_e = gamma_S A T_e,

```math
T_{\rm pk}=\sqrt{T_0^2+\frac{2\eta_{\rm th}h\nu}{\gamma_S A}}.
```

Holding all other material parameters fixed, matching the thermal excursion of a 100 µm^2 absorber at 1.55 µm gives the rough scaling

```math
A(10\,\mu\mathrm m)\sim 15.5\,\mu\mathrm m^2.
```

This is an extrapolation and must not be promoted to a device prediction without wavelength-dependent absorption, heat capacity, doping, and electron-phonon checks.

## 4. Initial stochastic feasibility inequality

Using a thermal photon-triggered escape model

```math
\Gamma_{\rm ph}\simeq\Gamma_0\exp[-\Delta U/(k_B T_{\rm pk})]
```

for a hot interval tau, require

```math
P_{\rm det}=1-\exp(-\Gamma_{\rm ph}\tau)>\eta.
```

This gives

```math
\Delta U < k_B T_{\rm pk}\ln\left[\frac{\Gamma_0\tau}{-\ln(1-\eta)}\right].
```

For dark MQT, the provisional cubic-barrier scaling used was

```math
\Gamma_{\rm MQT}\sim\Gamma_0\exp\left[-\frac{7.2\Delta U}{\hbar\omega_p}\right].
```

Requiring Gamma_dark < D gives

```math
\Delta U > \frac{\hbar\omega_p}{7.2}\ln(\Gamma_0/D).
```

Combining them gives the exploratory feasibility window

```math
\boxed{
\frac{\hbar\omega_p}{7.2}\ln\frac{\Gamma_0}{D}
<\Delta U<
k_B T_{\rm pk}\ln\left[\frac{\Gamma_0\tau}{-\ln(1-\eta)}\right]
}.
```

This inequality is NOT yet a theorem for the proposed detector. Its prefactors and even functional form must be rederived from the actual rf-SQUID potential and damping regime.

## 5. Numerical checkpoint from the provisional model

Exploratory inputs:

```text
T_pk       = 2.5 K
tau_hot    = 75 ns
Gamma_0    = 1e11 s^-1
eta        = 0.90
D          = 1e-6 s^-1
```

The photon condition gave approximately

```math
\Delta U/k_B < 20.2\,\mathrm K.
```

The provisional MQT condition produced an approximate critical plasma-frequency scale near

```math
f_p \lesssim 77\,\mathrm{GHz}
```

for a nonempty window under those assumptions. A design region around 30–50 GHz appeared attractive because lowering plasma frequency suppresses MQT while remaining much faster than a tens-of-nanoseconds hot-electron pulse.

This is a qualitative design insight until the exact escape action and damping are computed.

## 6. Directionality condition

If the two directional escape rates satisfy

```math
\Gamma_\pm\propto\exp[-\Delta U_\pm/(k_B T_{\rm pk})],
```

then

```math
P_+=\Gamma_+/(\Gamma_++\Gamma_-).
```

The required barrier asymmetry is

```math
\Delta U_- - \Delta U_+
> k_B T_{\rm pk}\ln\left[\frac{P_+}{1-P_+}\right].
```

At T_pk = 2.5 K, the simple thermal model gives roughly 0.47 meV for 90% directionality and 0.99 meV for 99% directionality.

## 7. Current candidate implementation generations

### Generation A — physics proof

```text
graphene or equivalent low-C_e Josephson absorber
+ hysteretic superconducting loop
+ small external flux bias
+ SQUID readout
```

Goal: show that one absorbed LWIR photon can be mapped to a persistent fluxoid state with high efficiency and low false-switch probability.

### Generation B — self-directed / photovoltaic-like

Replace external flux bias with an intrinsic phi0 / Josephson-diode / inversion-breaking phase element so that the light-triggered transition is directionally selected at zero externally applied flux bias.

This is closer to the original superconducting-photovoltaic motivation, but presently has more unverified physics.

## 8. Immediate next calculation

Do not continue with constant barriers. Solve the actual time-dependent problem:

```math
T_e(t)
\to I_c[T_e(t)]
\to U[\phi,T_e(t)]
\to \Delta U_\pm(t),\omega_p(t)
\to \Gamma_\pm(t)
\to P_+,P_-,P_0.
```

The competing dark mechanisms must then be added separately rather than hidden in one fitted DCR.

## 9. Current verdict

**GO for continued theory. NO-GO for manuscript.**

The initial model has not revealed an obvious energetic or stochastic contradiction. That is only a reason to continue. It is not evidence that the architecture is novel, fabricable, or superior to existing superconducting photon detectors.
