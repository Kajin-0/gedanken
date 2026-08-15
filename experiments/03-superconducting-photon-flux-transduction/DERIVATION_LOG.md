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

For an idealized loop inductance L,

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

For eta_E=1 this is about 108 pH. This remains only an idealized energy scale; Step 17 below corrects the assumption that an rf-SQUID's measured flux-state separation is exactly Phi0.

## Step 6: pair breaking is not avoidable in ordinary LWIR superconductors

At 10 µm the photon frequency is about 30 THz and energy about 124 meV. Requiring h nu < 2 Delta in weak-coupling BCS would imply an unrealistically high Tc of order 400 K.

Therefore the practical architecture should not require sub-gap absorption. It should tolerate a brief quasiparticle/hot-electron event and use that event to write a persistent superconducting state.

## Step 7: graphene Josephson calorimeter as benchmark

Published single-photon graphene Josephson switching at 1550 nm provides a concrete benchmark for low-electronic-heat-capacity calorimetric phase escape.

Correct benchmark from Huang et al. 2026:

```text
active graphene area ~ 100 um^2
T_1p                ~ 2.5 K in the fitted thermal model
tau_ep               ~ 75 ns
eta                   ~ 0.87 at dark count < 1/s
eta                   ~ 0.75 at dark count < 1/week
```

The earlier conversation incorrectly stated the latter dark-count point as roughly one per hour; that has been corrected.

Scaling absorber area only by photon energy to preserve the same simple heat-capacity excursion gives

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

## Step 10: provisional stochastic photon/MQT feasibility window

Provisional hot-state thermal escape:

```math
\Gamma_{\rm ph}\simeq\Gamma_0 e^{-\Delta U/(k_BT_{\rm pk})}.
```

Demanding P_det > eta during a hot interval tau gives

```math
\Delta U < k_BT_{\rm pk}\ln\left[\frac{\Gamma_0\tau}{-\ln(1-\eta)}\right].
```

Using the approximate cubic-barrier MQT form

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

This was useful as a first feasibility test but is superseded as the preferred photon-switching picture by the exact bifurcation derivation below.

## Step 11: plasma-frequency design insight

The provisional MQT exponent scales inversely with omega_p. Therefore reducing plasma frequency can exponentially suppress quantum dark switching while remaining much faster than the calorimetric pulse.

Because

```math
f_p\propto\sqrt{I_c/C},
```

increasing junction capacitance is a possible control knob. Quantitative optimization remains open.

## Step 12: stochastic directionality estimate

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

At T_pk = 2.5 K this is about 0.47 meV for 90% and 0.99 meV for 99% directional capture in the simple thermal model. The bifurcation model below gives a stronger way to obtain directionality: remove only the metastable well.

## Step 13: two-generation strategy

Generation A uses a small external flux bias to prove photon -> persistent-flux mapping with the least additional speculative physics.

Generation B attempts to replace external bias with an intrinsic phi0 / Josephson-diode / inversion-breaking element to obtain a self-directed, photovoltaic-like superconducting detector.

## Step 14: exact biased rf-SQUID reduction

Set `phi0=0`, choose

```math
\phi_x=\pi+\delta,
\qquad
x=\phi-\pi.
```

Then, in units of E_L,

```math
\boxed{
u(x;\beta,\delta)=\frac12(x-\delta)^2+\beta\cos x.}
```

Stationary points satisfy

```math
x-\delta-\beta\sin x=0,
```

and curvature is

```math
\nu''(x)=1-\beta\cos x.
```

For delta > 0, the left well is metastable and the right well is favored.

## Step 15: saddle-node criterion — stronger operating principle

The left minimum disappears when it merges with the saddle:

```math
\nu'(x_c)=0,
\qquad
\nu''(x_c)=0.
```

Let `x_c=-a`, `a>0`. Then

```math
\boxed{\delta=\tan a-a,}
```

```math
\boxed{\beta_c=\sec a.}
```

For small delta,

```math
a\sim(3\delta)^{1/3},
\qquad
\boxed{\beta_c-1\sim\tfrac12(3\delta)^{2/3}.}
```

Because beta is proportional to I_c, a photon pulse can in principle trigger the detector by satisfying

```math
\boxed{\beta_{\rm cold}>\beta_c>\beta_{\rm hot}.}
```

Required fractional critical-current suppression is

```math
\boxed{q_{\rm req}>1-\beta_c/\beta_{\rm cold}.}
```

This changes the preferred Generation-A mechanism. The photon need not rely on rare thermal hopping over a finite hot barrier: it can remove the metastable barrier by driving a saddle-node bifurcation.

## Step 16: near-saddle-node barrier and MQT scaling

Let

```math
\mu=\beta-\beta_c>0.
```

Expanding the exact potential around the saddle-node gives

```math
\boxed{
\Delta U_-
\simeq
\frac{2^{5/2}}{3}E_L\sin a\sqrt{\cos a}\,\mu^{3/2}.
}
```

The metastable-minimum curvature is

```math
\nu''_{\min}
\simeq
\frac{\sqrt2\sin a}{\sqrt{\cos a}}\mu^{1/2},
```

so

```math
\omega_m\propto\mu^{1/4}.
```

Therefore the basic quantum-escape action scale behaves as

```math
\Delta U_-/\hbar\omega_m\propto\mu^{5/4}.
```

This produces a real optimization tension: moving cold beta closer to beta_c reduces required photon-induced I_c suppression but rapidly weakens cold-state MQT stability.

The local barrier asymptotic was checked numerically against exact stationary-point barriers and converges to the exact result as mu -> 0.

## Step 17: exact benchmark and correction of the Phi0 signal assumption

Choose

```text
delta       = 0.05 rad
beta_cold   = 1.5
I_c,cold    = 3 uA
C           = 200 fF
```

Solving `delta=tan(a)-a` gives

```text
a       = 0.512040 rad
beta_c  = 1.147122
```

so the static bifurcation requires

```text
q_required = 23.53 % I_c suppression.
```

The corresponding inductance and energy scale are

```text
L       = 164.55 pH
E_L/k_B = 47.67 K.
```

Exact cold stationary points:

```text
x_left   = -1.436492   metastable minimum
x_saddle = -0.100507
x_right  = +1.549665   favored minimum
```

Exact barriers:

```text
Delta U_left/k_B  = 9.443 K
Delta U_right/k_B = 16.570 K
well bias/k_B     = 7.127 K.
```

For C=200 fF the local left-well small-oscillation frequency is

```text
f_p = 24.80 GHz.
```

The old cubic-form MQT diagnostic gives an exponent scale near 57, but that is not an absolute DCR prediction until the actual dissipative bounce and prefactor are calculated.

Important correction: adjacent fluxoid labels do not mean the measurable rf-SQUID loop flux differs by exactly Phi0. The exact benchmark separation is

```math
\Delta\Phi
=\frac{\Phi_0}{2\pi}(x_R-x_L)
=0.47526\Phi_0,
```

corresponding to

```math
\Delta I=\Delta\Phi/L=5.972\,\mu\mathrm A.
```

The earlier `Delta Phi=Phi0` / `Delta I=Phi0/L` language is therefore only an idealized scale estimate.

## Step 18: deterministic RCSJ tipping diagnostic

The damped phase equation is

```math
C\left(\frac{\Phi_0}{2\pi}\right)^2\ddot x
+\frac1R\left(\frac{\Phi_0}{2\pi}\right)^2\dot x
+\partial_xU=\xi(t).
```

With `s=t/sqrt(LC)` and noise omitted for the first deterministic test,

```math
\boxed{x''+\alpha x'+x-\delta-\beta(s)\sin x=0,}
```

where

```math
\alpha=\sqrt{L/C}/R_{\rm eff}.
```

For the benchmark,

```text
sqrt(LC)=5.74 ps.
```

A step from beta=1.5 to beta_hot=1.05 < beta_c removes the metastable well. Numerical integration gives first passage through x=0 on a scale of roughly 20 ps across representative weak-to-moderate damping values. This is enormously shorter than the ~75 ns hot-electron relaxation benchmark.

The implication is not that real switching is guaranteed in 20 ps. It is that phase motion is unlikely to be the slow element if the photon can suppress I_c below beta_c for an appreciable fraction of the thermal pulse.

A damping-envelope scale is roughly

```math
\tau_{\rm damp}\sim2R_{\rm hot}C.
```

This motivates testing whether hot-state quasiparticle conductance can provide capture damping while cold-state dissipation remains low. That is a hypothesis, not an established advantage.

## Step 19: new literature collisions

The novelty corridor narrowed substantially during the exact-model pass.

### Collision A — photon -> persistent flux memory

Onen et al., Nano Letters 20, 664–668 (2020), experimentally demonstrated a superconducting device combining single-photon detection and multilevel memory through single-photon-to-single-flux conversion.

Therefore persistent superconducting flux memory of photon detections is already prior art.

### Collision B — optically written persistent flux

Rochet et al., Nano Letters 20, 6488–6493 (2020), optically generated permanent individual Abrikosov vortices by local laser-induced thermal quench.

Therefore broad optical generation of persistent quantized superconducting flux is also prior art.

### Collision C — transient I_c suppression of rf-SQUID barrier

Zhou, Habif, Bocko and Feldman (2001) proposed an rf-SQUID tipping-pulse scheme in which SFQ pulses transiently suppress junction critical current, lower the double-well barrier and then allow the flux state to freeze when the barrier is restored.

Therefore transient critical-current suppression as a generic rf-SQUID tipping mechanism is prior art.

### Consequence

Any surviving contribution must be narrower. Candidate routes are now:

1. the quantitative single-LWIR calorimetric feasibility of driving the saddle-node while retaining extremely low cold dark switching;
2. a new analytic performance closure connecting heat capacity, I_c(T), beta_c(delta), cold barrier/MQT, damping and stored-flux readout;
3. a genuinely self-directed zero-external-flux implementation that is not already covered by phase-battery / diode prior art;
4. a matched performance advantage over existing SNSPD/KID/single-photon-single-flux architectures.

No novelty claim is authorized.

## Step 20: thermal-I_c plausibility benchmark

Jung et al., Phys. Rev. Applied 26, 014078 (2026), show that proximity-Josephson thermal critical-current sensitivity is strongly engineerable. Reported examples include width-normalized

```text
|dJ_c/dT| ~ 0.2 uA K^-1 um^-1 at 0.1 K
```

for an Al-based graphene JJ and maximum relative

```text
|(dI_c/dT)/I_c| ~ 0.6 K^-1 at 50 mK
```

for Ti-based graphene JJs.

These data make a tens-of-percent transient I_c suppression physically plausible enough to continue investigating, but they cannot be directly extrapolated into the proposed device's I_c(T_e) because geometry, proximity gap, carrier density and temperature range differ.

## Current next step

The static exact-potential problem is now solved sufficiently for this stage. The next decisive task is to couple a realistic LWIR thermal pulse to the bifurcation dynamics:

```text
absorbed photon
 -> T_e(t) from heat capacity + diffusion + e-ph cooling
 -> realistic I_c[T_e(t)]
 -> beta(t)
 -> stochastic/damped passage through beta_c
 -> P_capture, P_wrong, P_no-switch
```

Cold dark rates must then be calculated separately from the exact metastable potential with thermal activation and dissipative MQT. See `calculations/rfsquid_bifurcation_scan.py` for the reproducible static/deterministic checkpoint.
