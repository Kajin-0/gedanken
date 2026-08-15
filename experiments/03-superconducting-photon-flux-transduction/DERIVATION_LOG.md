# Experiment 03 — DERIVATION_LOG

This file records the chronological logical trail. It is not a polished derivation and does not establish novelty. Detailed formulas that become current are mirrored in `CURRENT_STATE.md`; claim status is controlled by `CLAIM_LEDGER.md`.

## 2026-08-15 — Step 1: optical response in a superconductor

Starting question: can superconductivity coexist with photoconductive / photovoltaic response?

Refinement: below `T_c`, ordinary DC photoconductivity is not the clean language because the condensate already supplies a zero-resistance channel. Useful optical observables are quasiparticle population/conductivity, superfluid density, `I_c`, kinetic inductance, phase and flux.

## Step 2: Johnson-noise question

For an ideal storage channel,

```math
S_V(\omega)\propto \mathrm{Re}\,Z(\omega),
```

so the ordinary finite-frequency resistive Johnson contribution vanishes as `Re Z -> 0`.

Correction retained: zero resistance does **not** imply zero total fluctuations or zero dark counts. Photon statistics, quasiparticles, phase slips, MQT, vortices, stray photons, readout and reset remain.

## Step 3: lossless response implies memory

Without relaxation,

```math
I_s(t)=I_0+N_\gamma(t)\Delta I_\gamma.
```

A perfectly lossless photon response is naturally an integrator / memory, which motivated a latching architecture.

## Step 4: photon statistics survive internal gain

For a linear photon-triggered impulse, internal gain multiplies signal and photon-arrival fluctuations together. The Poisson photon-noise floor referred to optical power remains

```math
\mathrm{NEP}_\gamma=\sqrt{2Ph\nu/\eta}.
```

Potential advantage: reduce detector-added noise, not photon statistics.

## Step 5: initial photon-to-flux architecture

Proposed chain:

```text
photon -> nonequilibrium excitation -> phase perturbation -> flux write -> persistent state
```

At 10 µm,

```math
E_\gamma\approx123.98\,\mathrm{meV}.
```

An idealized one-flux energy comparison gave

```math
L\gtrsim\Phi_0^2/(2\eta_E h\nu)\approx108\,\mathrm{pH}
```

for `eta_E=1`. This is only an energy scale; Step 17 corrects the early assumption that an rf-SQUID's measured state separation is exactly `Phi0`.

## Step 6: LWIR absorption need not be dissipationless

A 10-µm photon is generally far above conventional superconducting pair-breaking scales. Requiring `h nu < 2 Delta` in weak-coupling BCS would imply a `T_c` of order 400 K.

Architecture changed to:

```text
brief nonequilibrium / dissipative write
-> recovery
-> persistent superconducting storage
```

rather than demanding dissipationless optical absorption.

## Step 7: graphene Josephson calorimeter benchmark

Huang et al. 2026 provides an experimental benchmark for

```text
photon -> hot graphene electrons -> Josephson switching.
```

Relevant values:

```text
A_ref       ~ 100 um^2
T_1p        ~ 2.5 K in fitted thermal model
tau_ep      ~ 75 ns
eta         ~ 0.87 at dark count < 1/s
eta         ~ 0.75 at dark count < 1/week
```

The earlier conversation incorrectly stated the latter dark-count point as one per hour; corrected here and in the literature ledger.

Simple energy/area scaling to 10 µm gives

```math
A_{10}\sim100(1.55/10)=15.5\,\mu\mathrm m^2
```

for the same idealized peak temperature.

## Step 8: rf-SQUID mapping

Minimal potential:

```math
U(\phi,T_e)=\frac{E_L}{2}(\phi-\phi_x)^2-E_J(T_e)\cos\phi,
```

```math
E_L=(\Phi_0/2\pi)^2/L,
\quad
E_J=\Phi_0 I_c/(2\pi),
\quad
\beta=2\pi L I_c/\Phi_0.
```

Photon heating is used to modulate `I_c` and the phase landscape.

## Step 9: passive-barrier sanity bound

Generic thermal false switching

```math
\Gamma\sim\Omega e^{-E_b/k_BT}
```

implies `E_b >= k_B T ln(Omega/D)` for dark target `D`. If the photon had to pay that entire energy barrier directly, a 10-µm photon with `Omega=1e11 s^-1`, `D=1e-6 s^-1` gives a temperature scale near 37 K.

This motivated a triggered metastable landscape instead of photon-paid output energy.

## Step 10: provisional fixed-barrier photon/MQT window

A first model combined hot thermal escape and cubic-barrier MQT:

```math
\frac{\hbar\omega_p}{7.2}\ln\frac{\Gamma_0}{D}
<\Delta U<
k_BT_{pk}\ln\left[\frac{\Gamma_0\tau}{-\ln(1-\eta)}\right].
```

Useful as an initial falsification test, but now superseded as the preferred photon-trigger mechanism by saddle-node barrier annihilation.

## Step 11: capacitance / plasma-frequency insight

Because a cubic MQT action grows as `Delta U/(hbar omega_p)` and `omega_p` decreases with larger `C`, capacitance can suppress quantum escape while circuit dynamics can still remain far faster than a ns-scale thermal pulse.

Quantitative optimum remains open.

## Step 12: first stochastic directionality estimate

For two thermal escape rates,

```math
P_+=\frac{1}{1+\exp[-(\Delta U_- - \Delta U_+)/k_BT]}.
```

At 2.5 K, the simple model required about 0.47 meV barrier asymmetry for 90% directionality and 0.99 meV for 99%.

This is no longer the preferred Generation-A directionality mechanism because the tilted bifurcation can remove only one well.

## Step 13: two-generation plan

Generation A: small external flux tilt, chosen to isolate the physics with minimal speculation.

Generation B: replace external tilt with intrinsic `phi0` / Josephson-diode / inversion-breaking directionality if a zero-external-bias architecture later survives.

## Step 14: exact biased rf-SQUID reduction

For Generation A set

```math
\phi_x=\pi+\delta,
\qquad
x=\phi-\pi.
```

Then

```math
\boxed{u(x;\beta,\delta)=\frac{U}{E_L}=\frac12(x-\delta)^2+\beta\cos x.}
```

Stationary points and curvature:

```math
u'(x)=x-\delta-\beta\sin x,
\qquad
u''(x)=1-\beta\cos x.
```

For `delta>0`, the left well is metastable and the right well favored.

## Step 15: exact saddle-node threshold

At disappearance of the left well, `u'=u''=0`. Set `x_c=-a`, `a>0`:

```math
\boxed{\delta=\tan a-a,}
\qquad
\boxed{\beta_c=\sec a.}
```

For small `delta`:

```math
\boxed{\beta_c-1\sim\tfrac12(3\delta)^{2/3}.}
```

The photon-trigger condition becomes

```math
\boxed{\beta_{cold}>\beta_c>\beta_{hot}.}
```

Since `beta ∝ I_c`, the static fractional suppression threshold is

```math
\boxed{q_{req}>1-\beta_c/\beta_{cold}.}
```

This is the strongest current operating principle: the photon can destroy the metastable barrier rather than wait for a rare hop over it.

## Step 16: near-threshold cold stability

Let `mu=beta-beta_c>0`. Expansion about the saddle-node gives

```math
\boxed{
\Delta U_-
\simeq
\frac{2^{5/2}}{3}E_L\sin a\sqrt{\cos a}\,\mu^{3/2},
}
```

while

```math
\omega_m\propto\mu^{1/4}.
```

Hence the basic quantum-action scale obeys

```math
\Delta U_-/\hbar\omega_m\propto\mu^{5/4}.
```

Thus moving cold operation closer to bifurcation makes photon triggering easier but rapidly damages dark-state stability. The barrier asymptotic was checked numerically against exact roots.

## Step 17: exact numerical benchmark and flux correction

Chosen checkpoint:

```text
delta       = 0.05 rad
beta_cold   = 1.5
I_c,cold    = 3.0 uA
C           = 200 fF
```

Results:

```text
a                         = 0.512040 rad
beta_c                    = 1.147122
required I_c suppression  = 23.53 %
L                         = 164.55 pH
E_L/k_B                   = 47.67 K
x_left                    = -1.436492
x_saddle                  = -0.100507
x_right                   = +1.549665
Delta U_left/k_B          = 9.443 K
Delta U_right/k_B         = 16.570 K
well bias/k_B             = 7.127 K
f_p,left (C=200 fF)       = 24.80 GHz
```

A provisional cubic MQT exponent diagnostic is about 57, not yet an absolute DCR.

Crucial correction:

```math
\Delta\Phi
=\frac{\Phi_0}{2\pi}(x_R-x_L)
=0.47526\Phi_0,
```

so

```math
\Delta I=5.972\,\mu\mathrm A
```

for this `L`. Fluxoid index change does not imply measured loop-flux separation exactly equal to `Phi0`.

## Step 18: deterministic RCSJ tipping diagnostic

Ignoring noise,

```math
\boxed{x''+\alpha x'+x-\delta-\beta(s)\sin x=0,}
\qquad
s=t/\sqrt{LC}.
```

For the benchmark,

```text
sqrt(LC)=5.74 ps.
```

A square pulse to `beta_hot=1.05 < beta_c` drives first passage through `x=0` on roughly a 20-ps scale across tested weak/moderate damping. This is orders faster than the ~75-ns graphene hot-electron benchmark.

Interpretation: phase motion is unlikely to be the slow element if realistic `I_c(T_e)` crosses the saddle-node. Capture still requires damping/retrapping analysis.

## Step 19: major prior-art collisions

Three novelty routes closed during this pass:

1. **Onen et al. 2020:** experimentally demonstrated single-photon-to-single-flux conversion with superconducting multilevel memory. Broad `single photon -> persistent flux memory` is prior art.
2. **Rochet et al. 2020:** optically generated permanent individual Abrikosov vortices. Broad optical writing of persistent quantized superconducting flux is prior art.
3. **Zhou/Habif/Bocko/Feldman 2001:** used transient suppression of rf-SQUID junction critical current to lower the double-well barrier and then refreeze a flux state. Generic `I_c suppression -> rf-SQUID tipping/freeze` is prior art.

Surviving novelty, if any, must be in a much narrower LWIR calorimetric implementation, a self-directed version, or a genuinely new quantitative closure.

## Step 20: engineered thermal `I_c` sensitivity

Jung et al., Phys. Rev. Applied 26, 014078 (2026), reports engineered graphene-JJ thermal sensitivities including

```text
Al: |dJ_c/dT| ~ 0.2 uA K^-1 um^-1 at 0.1 K
Ti: max |(dI_c/dT)/I_c| ~ 0.6 K^-1 at 50 mK.
```

This is enough to keep a tens-of-percent photon-induced `I_c` suppression physically plausible, but not enough to define the proposed device's nonequilibrium `I_c(T_e)`.

## Step 21: absorbed-photon thermal bifurcation criterion

Define the critical electron temperature implicitly by

```math
\boxed{
I_c(T_{crit})
=I_c(T_0)\frac{\beta_c}{\beta_{cold}}.
}
```

For an electronic calorimeter with

```math
C_e=\gamma_S A T_e,
```

the no-loss absorbed-energy condition to reach the bifurcation is

```math
\boxed{
\eta_{th}h\nu
\ge
\frac{\gamma_S A}{2}(T_{crit}^2-T_0^2).
}
```

Therefore

```math
\boxed{
A_{max}
=\frac{2\eta_{th}h\nu}
{\gamma_S(T_{crit}^2-T_0^2)}.
}
```

Eliminate `gamma_S` using a reference calorimeter `(A_ref,E_ref,T_pk,ref)`:

```math
\boxed{
\eta_{th,min}
=
\frac{A}{A_{ref}}
\frac{E_{ref}}{E_\gamma}
\frac{T_{crit}^2-T_0^2}
{T_{pk,ref}^2-T_0^2}.
}
```

This is the first direct closure between the optical calorimeter and the rf-SQUID bifurcation threshold.

### Conditional numerical margin

The benchmark circuit requires

```text
I_c/I_c0 < beta_c/beta_cold = 0.76475,
```

i.e. a 23.53% reduction.

In the published MoRe/graphene single-photon device, the switching-current scale decreases by about 30% between 20 mK and 1.2 K. If a comparable `I_c(T_e)` is monotonic and applicable to our nonequilibrium pulse, the 23.5% threshold would occur at some

```text
T_crit <= 1.2 K.
```

This is a plausibility inference, not a validated nonequilibrium law.

Using the same published thermal reference

```text
A_ref       = 100 um^2
lambda_ref  = 1.55 um
T_pk,ref    = 2.5 K
T0          = 0.020 K
```

for a 10-µm photon gives, at `T_crit=1.2 K`,

```text
A_max(eta_th=1)                 = 67.29 um^2
energy-scaled target area       = 15.50 um^2
area / heat-capacity margin     = 4.34 x
eta_th,min at A=15.5 um^2       = 0.2304
required electronic heat        = 28.56 meV
10-um photon energy              = 123.98 meV.
```

Thus the *absorbed-photon heat capacity* does not presently appear to be the limiting contradiction: under the reference scaling, only about 23% of the 10-µm photon energy would need to remain in the electronic system to reach 1.2 K in a 15.5-µm^2 absorber.

The main unresolved issue is now the mapping between nonequilibrium `T_e(t)` and the Josephson `I_c`, plus optical absorption/diffusion and cold dark stability.

Reproducible calculation: `calculations/thermal_bifurcation_margin.py`.

## Current next step

Build a physically defensible `I_c(T_e)` for the actual proximity junction and couple it to a thermal pulse with diffusion/electron-phonon loss:

```text
absorbed 8–14 um photon
 -> T_e(t)
 -> I_c[T_e(t)]
 -> beta(t)
 -> finite-rate stochastic passage through beta_c
 -> P_capture, P_wrong, P_no-switch.
```

Cold dark rates then require the exact metastable potential plus thermal activation and dissipative MQT. No manuscript or novelty claim is authorized.
