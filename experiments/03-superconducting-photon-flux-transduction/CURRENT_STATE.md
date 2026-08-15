# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** NO-GO for manuscript until novelty and quantitative gates are passed.

## 1. Current physical idea

The preferred Generation-A architecture is now a **calorimetrically triggered rf-SQUID bifurcation**, not ordinary stochastic hopping over a fixed barrier.

```text
single absorbed LWIR photon
 -> hot-electron / quasiparticle pulse
 -> transient suppression of Josephson I_c
 -> metastable rf-SQUID well reaches a saddle-node and disappears
 -> phase is driven toward the flux-favored surviving well
 -> I_c recovers
 -> the new superconducting flux state is latched
```

The architecture intentionally separates a short nonequilibrium/dissipative write event from the long-lived superconducting storage/readout state.

This operating principle does **not** by itself establish novelty. Single-photon-to-flux memory and transient critical-current suppression of rf-SQUID barriers both have prior art; see `LITERATURE_LEDGER.md`.

## 2. Noise interpretation

The motivating Johnson-noise question is retained with a narrower statement:

- an ideal nondissipative superconducting storage channel has no ordinary finite-frequency resistive Johnson-Nyquist floor because `Re[Z] -> 0`;
- zero resistance does not mean zero total fluctuations or zero dark counts;
- cold-state false events can arise from thermal activation, macroscopic quantum tunneling (MQT), quasiparticles, vortices, stray photons and readout backaction;
- the hot write event may itself be dissipative;
- detector performance is therefore better characterized by photon-triggered capture probability, wrong-way capture probability, dark switching, stored-state SNR and reset cost than by Johnson noise alone.

## 3. Exact sinusoidal Generation-A potential

Start from the rf-SQUID potential

```math
U(\phi,T_e)=\frac{E_L}{2}(\phi-\phi_x)^2-E_J(T_e)\cos\phi,
```

with

```math
E_L=\frac1L\left(\frac{\Phi_0}{2\pi}\right)^2,
\qquad
E_J(T_e)=\frac{\Phi_0 I_c(T_e)}{2\pi},
\qquad
\beta(T_e)=\frac{2\pi L I_c(T_e)}{\Phi_0}.
```

For a small directional external-flux tilt, write

```math
\phi_x=\pi+\delta,
\qquad
x=\phi-\pi.
```

Then

```math
\boxed{
u(x;\beta,\delta)=\frac{U}{E_L}
=\frac12(x-\delta)^2+\beta\cos x.}
```

Stationary points satisfy

```math
x-\delta-\beta\sin x=0,
```

and local curvature is

```math
\nu''(x)=1-\beta\cos x.
```

For `delta > 0`, the left well is metastable and the right well is favored.

## 4. Exact saddle-node threshold

The metastable left well disappears when its minimum merges with the intervening saddle:

```math
\nu'(x_c)=0,
\qquad
\nu''(x_c)=0.
```

Set `x_c=-a`, `a>0`. The two conditions reduce to

```math
\boxed{\delta=\tan a-a,}
```

```math
\boxed{\beta_c=\sec a.}
```

For small flux tilt,

```math
a\sim(3\delta)^{1/3},
```

so

```math
\boxed{\beta_c-1\sim\frac12(3\delta)^{2/3}.}
```

This gives a direct photon-trigger condition:

```math
\boxed{\beta_{\rm cold}>\beta_c>\beta_{\rm hot}.}
```

Since `beta` is proportional to `I_c`, the minimum fractional critical-current suppression required to cross the static bifurcation is

```math
\boxed{
q_{\rm req}
=1-\frac{I_{c,\rm hot}}{I_{c,\rm cold}}
>1-\frac{\beta_c}{\beta_{\rm cold}}.
}
```

This is now the strongest analytic checkpoint. In the quasistatic idealization, a photon need not thermally hop over a surviving barrier: the barrier can be removed.

## 5. Near-threshold cold-state barrier and plasma frequency

Let

```math
\mu=\beta-\beta_c>0.
```

Expanding the exact potential about the saddle-node gives the metastable barrier

```math
\boxed{
\Delta U_-
\simeq
\frac{2^{5/2}}{3}E_L
\sin a\sqrt{\cos a}\,\mu^{3/2}.
}
```

The curvature of the metastable minimum scales as

```math
\nu''_{\min}
\simeq
\frac{\sqrt2\sin a}{\sqrt{\cos a}}\mu^{1/2},
```

and therefore

```math
\omega_m
=\frac1{\sqrt{LC}}\sqrt{\nu''_{\min}}
\propto\mu^{1/4}.
```

Consequently, a cubic-barrier-type MQT action scale behaves near the bifurcation as

```math
\frac{\Delta U_-}{\hbar\omega_m}\propto\mu^{5/4}.
```

This exposes a real design tradeoff: operating closer to the bifurcation reduces the required photon-induced `I_c` suppression but rapidly weakens cold-state metastability against quantum escape.

## 6. Concrete benchmark

Use the exploratory point

```text
delta       = 0.05 rad
beta_cold   = 1.5
I_c,cold    = 3.0 uA
C           = 200 fF
```

The exact sinusoidal model gives

```text
a                         = 0.51204 rad
beta_c                    = 1.14712
required I_c suppression  = 23.53 %
L                         = 164.55 pH
E_L/k_B                   = 47.67 K
```

Cold stationary points are

```text
x_left metastable = -1.43649
x_saddle          = -0.10051
x_right favored   = +1.54967
```

with exact barriers

```text
Delta U_left/k_B  = 9.443 K
Delta U_right/k_B = 16.570 K
well-energy bias  = 7.127 K
```

The local left-well plasma frequency is approximately

```text
f_p = 24.80 GHz
```

for `C = 200 fF`.

Using the earlier *diagnostic* cubic MQT exponent only,

```math
B_{\rm MQT}\sim7.2\Delta U/(\hbar\omega_p),
```

gives `B ≈ 57.1`. This is not yet an absolute DCR prediction because damping and the exact bounce action have not been treated.

### Important correction to the early flux estimate

For an rf-SQUID, adjacent fluxoid labels do **not** imply that the measured loop flux differs by exactly `Phi0`.

For this benchmark,

```math
\Delta\Phi
=\frac{\Phi_0}{2\pi}(x_R-x_L)
\approx0.4753\Phi_0,
```

and

```math
\Delta I=\Delta\Phi/L\approx5.97\,\mu\mathrm A.
```

The earlier use of `Delta Phi = Phi0` should therefore be understood only as an idealized scale estimate, not the exact rf-SQUID signal.

## 7. Deterministic phase dynamics

The RCSJ-like equation is

```math
C\left(\frac{\Phi_0}{2\pi}\right)^2\ddot x
+
\frac1R\left(\frac{\Phi_0}{2\pi}\right)^2\dot x
+
\frac{\partial U}{\partial x}=\xi(t).
```

Ignoring noise for the deterministic tipping test and using dimensionless time `s=t/sqrt(LC)` gives

```math
\boxed{
x''+\alpha x'+x-\delta-\beta(s)\sin x=0,
}
```

with

```math
\alpha=\frac{\sqrt{L/C}}{R_{\rm eff}}.
```

For the benchmark above,

```text
sqrt(LC) = 5.74 ps.
```

A step from `beta_cold=1.5` to `beta_hot=1.05 < beta_c` drives the phase through `x=0` on a scale of roughly 20 ps across representative weak-to-moderate damping values used in the numerical diagnostic. This is orders of magnitude shorter than the approximately 75 ns hot-electron relaxation benchmark from the 2026 graphene Josephson single-photon experiment.

Therefore the static saddle-node condition is likely the correct zeroth-order operating criterion **if** a realistic photon pulse can suppress `I_c` below `beta_c` for long enough and the hot-state damping is sufficient to capture the favored well before `I_c` recovers.

A useful settling scale is approximately

```math
\tau_{\rm damp}\sim2R_{\rm hot}C.
```

The architecture does not require a permanently resistive shunt in principle: hot quasiparticle conductance could provide write-time damping while cold-state conductance becomes much smaller. This is a research hypothesis, not an established device property.

## 8. Thermal transducer benchmark

The 2026 graphene Josephson single-photon experiment gives the empirical hot-pulse scale

```text
T_1p   ~ 2.5 K
tau_ep ~ 75 ns
```

for a 100 µm^2, 1550-nm device in its thermal model, with about 87% intrinsic efficiency at dark count below 1 s^-1 and about 75% intrinsic efficiency at dark count below one per week.

A separate 2026 graphene-JJ thermal-sensitivity study reports

```text
Al device: |dJ_c/dT| ~ 0.2 uA K^-1 um^-1 at 0.1 K
Ti device: max |(dI_c/dT)/I_c| ~ 0.6 K^-1 at 50 mK
```

These results support the plausibility of engineering strong thermal `I_c` response, but they are **not** an `I_c(T_e)` model for the proposed LWIR device.

The old simple heat-capacity scaling

```math
A(10\,\mu\mathrm m)\sim15.5\,\mu\mathrm m^2
```

is retained only as an extrapolation to be replaced by an actual optical/thermal model.

## 9. Superseded stochastic-barrier checkpoint

The previous constant-barrier inequality

```math
\frac{\hbar\omega_p}{7.2}\ln\frac{\Gamma_0}{D}
<\Delta U<
k_BT_{\rm pk}\ln\left[\frac{\Gamma_0\tau}{-\ln(1-\eta)}\right]
```

remains useful historically but is no longer the preferred photon-switching model. If the photon drives `beta(t)` below `beta_c`, the hot metastable barrier vanishes rather than remaining finite.

The stochastic analysis is still required for:

- subthreshold photon events;
- cold-state thermal/MQT dark switching;
- noise-driven wrong-way trajectories near a dynamic bifurcation;
- incomplete damping and retrapping;
- realistic finite-rate passage through the saddle-node.

## 10. Prior-art boundary after the new collision pass

Do not claim novelty for any of the following:

```text
superconducting MIR/LWIR single-photon detection
photon -> hot graphene -> Josephson switching
single photon -> persistent superconducting single-flux memory
optical heating -> persistent superconducting flux/vortex generation
transient I_c suppression -> lowered rf-SQUID barrier -> frozen flux state
field-free Josephson directionality
illumination-driven superconducting phase batteries / vorticity switching
```

The 2020 Onen et al. single-photon single-flux detector is a particularly important collision: persistent flux memory from photon detections has already been demonstrated.

The 2001 rf-SQUID tipping-pulse work is another direct collision: transient critical-current suppression to lower the rf-SQUID barrier and then refreeze the flux state is also prior art.

The surviving research question is therefore narrower: whether a **single absorbed LWIR photon** can calorimetrically drive a useful directional rf-SQUID bifurcation with a quantitatively distinct efficiency/dark-count/storage tradeoff, and whether a zero-external-bias version or a new general bound survives collision review.

## 11. Current implementation generations

### Generation A — externally tilted proof architecture

```text
LWIR antenna/cavity
+ low-C_e photon-sensitive Josephson element
+ hysteretic rf-SQUID
+ small external flux tilt delta
+ persistent flux readout
```

Photon criterion:

```math
I_c[T_e(t)]<I_{c,\rm crit}
=\frac{\Phi_0\beta_c(\delta)}{2\pi L}
```

for a sufficient interval to cross and settle into the favored basin.

### Generation B — self-directed / photovoltaic-like

Replace the external tilt with a `phi0`, Josephson-diode, or other intrinsic inversion/time-reversal-breaking element. This remains more speculative and must be collision-audited independently.

## 12. Immediate next calculation

The next decisive model is no longer generic barrier root-finding. It is the coupled thermal-dynamical problem

```text
absorbed 8–14 um photon
 -> T_e(t), including diffusion and electron-phonon cooling
 -> measured/realistic I_c[T_e(t)]
 -> beta(t)
 -> stochastic RCSJ passage through beta_c
 -> capture probability and settling
```

with cold-state DCR computed separately from the exact rf-SQUID potential and dissipative MQT/thermal theory.

Required outputs:

```text
P_capture
P_wrong
P_no-switch
Gamma_dark,thermal
Gamma_dark,MQT
DeltaPhi_readout
reset energy/time
```

The reproducible exact-potential checkpoint is in `calculations/rfsquid_bifurcation_scan.py`.

## 13. Current verdict

**GO for continued theory. NO-GO for manuscript.**

The exact rf-SQUID model strengthens physical feasibility by revealing a deterministic bifurcation route, but the literature audit simultaneously narrows the possible novelty claim. The next phase must test realistic `I_c(T_e)` and dynamic capture rather than expanding the architecture rhetorically.