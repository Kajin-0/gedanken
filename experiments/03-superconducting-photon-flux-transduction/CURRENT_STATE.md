# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript** until quantitative and novelty gates are passed.

## 1. Preferred physical architecture

Generation A is now a **calorimetrically triggered rf-SQUID bifurcation**:

```text
single absorbed 8–14 um photon
 -> hot-electron / quasiparticle pulse
 -> transient change of the Josephson current-phase relation
 -> metastable flux well reaches a saddle-node and disappears
 -> phase moves toward the flux-favored surviving basin
 -> Josephson coupling recovers
 -> persistent superconducting flux state is latched
```

This is stronger than the initial fixed-barrier thermal-hopping picture. The optical write may be dissipative; the stored state can subsequently be superconducting and nondissipative.

This architecture is **not yet novel by default**. Important pieces already exist in prior art: photon-triggered Josephson switching, single-photon-to-single-flux memory, optically written persistent flux, and transient critical-current suppression of an rf-SQUID barrier. See `LITERATURE_LEDGER.md`.

## 2. Noise statement retained from the original question

For an ideal cold superconducting storage channel with `Re Z -> 0`, the ordinary finite-frequency resistive Johnson contribution vanishes. This does not imply zero total detector noise or zero dark events.

The relevant false-event channels are instead

```text
thermal phase escape
macroscopic quantum tunneling (MQT)
quasiparticles
vortices / trapped flux
stray photons
flux/readout backaction
reset errors
```

The device should therefore be judged primarily by `P_capture`, `P_wrong`, DCR, stored-state SNR, dead time and reset cost, not by Johnson noise alone.

## 3. Exact sinusoidal Generation-A model

For the benchmark sinusoidal current-phase relation,

```math
U(\phi,T_e)=\frac{E_L}{2}(\phi-\phi_x)^2-E_J(T_e)\cos\phi,
```

where

```math
E_L=\frac1L\left(\frac{\Phi_0}{2\pi}\right)^2,
\qquad
\beta(T_e)=\frac{2\pi L I_c(T_e)}{\Phi_0}.
```

Choose an external directional tilt

```math
\phi_x=\pi+\delta,
\qquad
x=\phi-\pi.
```

Then

```math
\boxed{
u(x)=\frac{U}{E_L}=\frac12(x-\delta)^2+\beta\cos x.}
```

Stationary points satisfy

```math
x-\delta-\beta\sin x=0,
```

with curvature

```math
\nu''(x)=1-\beta\cos x.
```

For `delta>0`, the left well is metastable and the right well is energetically favored.

## 4. Exact saddle-node threshold

At disappearance of the metastable well,

```math
\nu'(x_c)=\nu''(x_c)=0.
```

Writing `x_c=-a`, `a>0`, gives the exact fold equations

```math
\boxed{\delta=\tan a-a,}
\qquad
\boxed{\beta_c=\sec a.}
```

For small `delta`,

```math
\boxed{\beta_c-1\sim\frac12(3\delta)^{2/3}.}
```

The static photon-trigger criterion is

```math
\boxed{\beta_{cold}>\beta_c>\beta_{hot}.}
```

If only the amplitude `I_c` changes,

```math
\boxed{
q_{req}>1-\frac{\beta_c}{\beta_{cold}}
}
```

is the required fractional `I_c` suppression.

## 5. General current-phase-relation fold — preferred formulation

A graphene/proximity junction need not have a sinusoidal CPR. Define the current scale

```math
I_* = \frac{\Phi_0}{2\pi L}
```

and choose the loop-current sign convention so that

```math
\mathcal I(x,T)=\frac{I_s(x,T)}{I_*}.
```

The dimensionless potential and phase force can be written

```math
u(x,T)
=\frac12(x-\delta)^2
-\int^x \mathcal I(\theta,T)d\theta,
```

```math
F(x,T)=\partial_x\nu=x-\delta-\mathcal I(x,T).
```

A completely general static saddle-node satisfies

```math
\boxed{
\mathcal I(x_c,T_c)=x_c-\delta,
}
```

```math
\boxed{
\partial_x\mathcal I(x_c,T_c)=1.
}
```

Geometrically: the temperature-dependent Josephson CPR becomes tangent to the inductive load line.

If the CPR is separable,

```math
\mathcal I(x,T)=\beta(T)f(x),
```

then

```math
\boxed{
\beta_c=\frac1{f'(x_c)},
\qquad
\delta=x_c-\frac{f(x_c)}{f'(x_c)}.
}
```

The sinusoidal result is recovered with `f(x)=sin x`.

### Universal fold scaling

For any smooth one-parameter crossing of a nondegenerate fold,

```math
F\simeq F_p\Delta p+\frac12F_{xx}(x-x_c)^2.
```

Therefore the disappearing-well barrier has the universal local scaling

```math
\boxed{
\Delta U
\simeq
\frac{4\sqrt2}{3}E_L
\frac{|F_p\Delta p|^{3/2}}{\sqrt{|F_{xx}|}}.
}
```

For a separable amplitude control `p=beta`, this becomes

```math
\boxed{
\Delta U
\simeq
\frac{4\sqrt2}{3}E_L
\frac{|f_c|^{3/2}}{\sqrt{|\beta_c f''_c|}}
|\beta-\beta_c|^{3/2}.
}
```

The minimum curvature scales as `|beta-beta_c|^(1/2)`, hence

```math
\omega_m\propto|\beta-\beta_c|^{1/4},
```

and the basic quantum-action scale behaves as

```math
\Delta U/(\hbar\omega_m)\propto|\beta-\beta_c|^{5/4}.
```

This produces the central design conflict: moving cold operation closer to the photon-trigger threshold lowers the required optical perturbation but rapidly weakens cold-state quantum stability.

### CPR-shape sensitivity

A normalized illustrative family

```math
f_r(x)\propto\sin x+r\sin2x
```

shows that the threshold is materially CPR-dependent. For `delta=0.05`, `beta_cold=1.5`:

```text
r       beta_c      required beta suppression
-0.10   1.40065       6.62 %
 0.00   1.14712      23.53 %
+0.10   0.99269      33.82 %
+0.20   0.90225      39.85 %
+0.30   0.84584      43.61 %
```

These are sensitivity examples, not a graphene CPR model. They establish that a measured or microscopic CPR is mandatory before treating `23.5%` as a real device threshold.

Reproducible calculation: `calculations/general_cpr_fold.py`.

## 6. Sinusoidal numerical benchmark

Exploratory parameters:

```text
delta       = 0.05 rad
beta_cold   = 1.5
I_c,cold    = 3.0 uA
C           = 200 fF
```

Exact results:

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
f_p,left                  = 24.80 GHz
```

The earlier cubic MQT expression gives a diagnostic exponent near 57, but this is **not** an absolute DCR until the dissipative bounce and prefactor are treated correctly.

### Readout-state correction

Fluxoid labels do not imply measured loop-flux separation exactly equal to `Phi0`. For this benchmark,

```math
\boxed{
\Delta\Phi
=\frac{\Phi_0}{2\pi}(x_R-x_L)
=0.47526\Phi_0,
}
```

so

```math
\boxed{\Delta I=5.97\,\mu\mathrm A.}
```

Future readout/SNR calculations must use the actual stationary points.

Reproducible calculation: `calculations/rfsquid_bifurcation_scan.py`.

## 7. Deterministic phase timescale

A minimal RCSJ diagnostic gives

```math
x''+\alpha x'+x-\delta-\beta(s)\sin x=0,
\qquad
s=t/\sqrt{LC},
```

with

```math
\alpha=\sqrt{L/C}/R_{eff}.
```

For the benchmark,

```text
sqrt(LC)=5.74 ps.
```

A square pulse from `beta=1.5` to `beta_hot=1.05<beta_c` crosses `x=0` in roughly `20 ps` over representative weak-to-moderate damping used in the diagnostic.

This is orders of magnitude shorter than the `~75 ns` electron-phonon relaxation scale extracted in the 2026 graphene single-photon experiment. Thus phase motion is unlikely to be the bottleneck if the optical pulse genuinely drives the CPR through the fold.

Capture is not yet proved: finite-rate fold passage, damping, retrapping and noise must still be solved.

## 8. Optical-to-bifurcation thermal closure

Define the critical electron temperature by the **actual CPR fold condition**. In the scalar-amplitude approximation this reduces to

```math
\boxed{
I_c(T_{crit})
=I_c(T_0)\frac{\beta_c}{\beta_{cold}}.
}
```

For a graphene-like electronic calorimeter with

```math
C_e=\gamma_S A T,
```

the absorbed-energy threshold is

```math
\boxed{
\eta_{th}h\nu
\ge
\frac{\gamma_S A}{2}
(T_{crit}^2-T_0^2).
}
```

Equivalently,

```math
\boxed{
A_{max}
=\frac{2\eta_{th}h\nu}
{\gamma_S(T_{crit}^2-T_0^2)}.
}
```

Using a reference calorimeter eliminates `gamma_S`:

```math
\boxed{
\eta_{th,min}
=\frac{A}{A_{ref}}
\frac{E_{ref}}{E_\gamma}
\frac{T_{crit}^2-T_0^2}
{T_{pk,ref}^2-T_0^2}.
}
```

### Conditional 10-µm margin

The published 2026 MoRe/graphene device reports an approximately 30% decrease in switching-current scale between `20 mK` and `1.2 K`. If a comparable monotonic equilibrium `I_c(T)` were applicable to the proposed nonequilibrium hot-electron pulse, the sinusoidal benchmark's `23.53%` threshold would occur at some

```text
T_crit <= 1.2 K.
```

Using the same published thermal reference

```text
A_ref       = 100 um^2
lambda_ref  = 1.55 um
T_pk,ref    = 2.5 K
T0          = 0.020 K
```

and a `10 um` photon gives at `T_crit=1.2 K`:

```text
E_gamma                          = 123.98 meV
A_max at eta_th=1                = 67.29 um^2
energy-scaled target area        = 15.50 um^2
heat-capacity area margin        = 4.34 x
eta_th,min for A=15.5 um^2       = 0.230
required retained electronic heat= 28.56 meV
```

So simple heat capacity does not presently kill the idea. Under this **conditional** benchmark, only about 23% of a 10-µm photon's absorbed energy would need to remain in the electronic system to reach 1.2 K in a 15.5-µm^2 absorber.

The caveat is substantial: equilibrium switching current versus bath temperature is not automatically the nonequilibrium `I_s(phi,T_e)` of a single-photon pulse.

Reproducible calculation: `calculations/thermal_bifurcation_margin.py`.

## 9. Published thermal/Josephson benchmarks retained

Huang et al. 2026:

```text
100 um^2 graphene active area
T_1p ~ 2.5 K in fitted thermal model
tau_ep ~ 75 ns
eta ~ 0.87 at dark count < 1/s
eta ~ 0.75 at dark count < 1/week
```

Jung et al. 2026 shows that proximity-JJ thermal critical-current sensitivity is engineerable, with reported examples around

```text
|dJ_c/dT| ~ 0.2 uA K^-1 um^-1 at 0.1 K  (Al platform)
max |(dI_c/dT)/I_c| ~ 0.6 K^-1 at 50 mK (Ti platform).
```

These are plausibility benchmarks, not direct parameters for Experiment 03.

## 10. Prior-art boundary

The following broad claims are closed:

```text
LWIR superconducting single-photon detection                     PRIOR ART
photon -> hot graphene -> Josephson switching                    PRIOR ART
single photon -> persistent superconducting single-flux memory   PRIOR ART
optical heating -> permanent superconducting flux/vortex         PRIOR ART
transient I_c suppression -> rf-SQUID barrier lowering/freeze    PRIOR ART
field-free Josephson/superconducting diode directionality        PRIOR ART
illumination -> superconducting phase battery/vorticity          PRIOR ART
```

The strongest direct collisions are:

- Onen et al. 2020: single-photon-to-single-flux conversion with superconducting multilevel memory;
- Rochet et al. 2020: optically written permanent single vortices;
- Zhou/Habif/Bocko/Feldman 2001: transient `I_c` suppression as an rf-SQUID tipping/freeze mechanism.

No novelty claim is authorized.

## 11. Surviving research corridor

The branch remains worth pursuing only if one of these survives quantitative and collision review:

1. realistic **single-LWIR-photon calorimetric bifurcation** with high capture and exceptionally low cold DCR;
2. a new general closure connecting photon heat capacity, full CPR, fold threshold, cold barrier/MQT, damping and stored readout signal;
3. a genuinely self-directed zero-external-flux implementation not already covered by diode / phase-battery prior art;
4. a matched performance consequence not already achieved by SNSPD, KID, graphene-JJ or single-photon-single-flux platforms;
5. a useful impossibility/optimality bound if the device itself fails.

## 12. Immediate next calculation

The static fold problem is now solved both for sinusoidal and general CPRs. The decisive next problem is

```text
absorbed 8–14 um photon
 -> nonequilibrium T_e(t), including diffusion and e-ph loss
 -> physically defensible I_s(phi,T_e)
 -> time-dependent fold crossing
 -> stochastic/damped basin capture
 -> P_capture, P_wrong, P_no-switch
```

Cold-state dark rates must be treated separately from the exact metastable potential using thermal activation plus **dissipative** MQT.

Priority data need: measured or microscopic `I_s(phi,T)` / `I_c(T)` for the actual proposed junction, not an assumed scalar temperature law.

## 13. Current verdict

**GO for continued theory. NO-GO for manuscript.**

Physical feasibility has strengthened: the exact circuit admits a fold trigger and the first thermal-energy margin is nonempty. Simultaneously, the literature audit has eliminated several broad novelty routes. The next work must therefore become more quantitative, not more speculative.
