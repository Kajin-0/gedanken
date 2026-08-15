# Experiment 03 — DERIVATION_LOG

This is the chronological reasoning trail. It records successful steps, corrections, rejected assumptions and prior-art collisions. `CURRENT_STATE.md` is the compact live model; `CLAIM_LEDGER.md` controls claim status.

## 2026-08-15 — Step 1: superconducting optical response

Starting question: can superconductivity coexist with photoconductive / photovoltaic response?

Refinement: below `T_c`, ordinary DC photoconductivity is not the clean language because the condensate already supplies a zero-resistance channel. Useful observables are quasiparticle population/conductivity, superfluid density, critical current, kinetic inductance, phase and flux.

## Step 2: Johnson noise

Fluctuation-dissipation gives finite-frequency resistive noise proportional to `Re Z`. An ideal cold superconducting storage channel can therefore eliminate the ordinary Johnson contribution of that channel.

Correction: zero resistance does **not** imply zero total fluctuations. Photon statistics, quasiparticles, phase slips, MQT, vortices, stray photons, readout and reset remain.

## Step 3: lossless response implies memory

Without relaxation, photon-induced current increments accumulate. A perfectly lossless detector is naturally an integrator / memory rather than a stationary linear photoconductor. This motivated a latching flux-state architecture.

## Step 4: photon statistics survive internal gain

For a linear transducer, superconducting internal gain amplifies signal and photon-arrival fluctuations together. The Poisson optical floor remains

```math
NEP_\gamma=\sqrt{2Ph\nu/\eta}.
```

Possible advantage is lower detector-added noise, not violation of photon statistics.

## Step 5: initial photon-to-flux concept

Proposed chain:

```text
photon -> nonequilibrium excitation -> phase perturbation -> flux write -> persistent state.
```

At 10 um,

```text
E_gamma ~ 123.98 meV.
```

An ideal one-flux energy comparison gave `L~108 pH` as an energetic scale at unit conversion. This was never a switching criterion.

## Step 6: dissipationless LWIR absorption rejected

A 10-um photon is far above ordinary superconducting pair-breaking scales. The architecture was changed to

```text
brief nonequilibrium / dissipative write
-> recovery
-> persistent superconducting storage.
```

## Step 7: graphene Josephson calorimeter benchmark

Huang et al. 2026 gives a concrete experimental reference for photon-heated graphene triggering Josephson switching:

```text
area          ~100 um^2
T_1p fit      ~2.5 K
tau_ep fit    ~75 ns
eta           ~0.87 at dark count <1/s
eta           ~0.75 at dark count <1/week.
```

Correction: an earlier conversation statement incorrectly said the latter point was one per hour.

Simple equal-peak-temperature energy scaling gives a 10-um absorber area near `15.5 um^2`. This remains an extrapolation.

## Step 8: rf-SQUID mapping

Minimal sinusoidal potential:

```math
U(\phi,T)=\frac{E_L}{2}(\phi-\phi_x)^2-E_J(T)\cos\phi,
```

with `beta=2 pi L I_c/Phi0`. Photon heating changes the Josephson landscape.

## Step 9: passive-barrier sanity bound

A generic thermal dark rate `Omega exp(-E_b/kT)` showed that making the photon directly pay a thermally stable barrier becomes restrictive. This motivated using the photon as a trigger for a metastable energy landscape rather than as the sole source of stored output energy.

## Step 10: provisional fixed-barrier photon/MQT window

The first stochastic model combined hot thermal escape and cubic-barrier MQT. It produced a nonempty window for plausible parameters but treated the hot barrier as fixed.

This was useful as an initial falsification test but is now superseded as the preferred photon-switch mechanism.

## Step 11: capacitance as an MQT control knob

Because the provisional MQT action increases as plasma frequency falls and `omega_p~C^-1/2`, increasing capacitance can suppress quantum escape while circuit dynamics can remain much faster than a nanosecond thermal pulse.

## Step 12: first stochastic directionality estimate

A two-barrier activation model gave sub-meV asymmetry scales for strong directionality at `T~2.5 K`. This became secondary once a tilted fold mechanism was found.

## Step 13: Generation A / B split

Generation A: small external flux tilt to isolate the physics.

Generation B: later attempt to replace external tilt with intrinsic `phi0` / diode / inversion-breaking directionality.

Generation A is not photovoltaic.

## Step 14: exact sinusoidal fold

Set

```math
\phi_x=\pi+\delta,
\qquad
x=\phi-\pi,
```

so

```math
u(x)=\frac12(x-\delta)^2+\beta\cos x.
```

At the metastable saddle-node, `u'=u''=0`. With `x_c=-a`:

```math
\boxed{\delta=\tan a-a,}
\qquad
\boxed{\beta_c=\sec a.}
```

Thus the photon can trigger by driving

```math
\beta_{cold}>\beta_c>\beta_{hot},
```

removing the metastable well instead of waiting for a rare hot-state barrier crossing.

## Step 15: near-fold stability scaling

With `mu=beta-beta_c>0`:

```math
\Delta U\propto\mu^{3/2},
\qquad
\omega_m\propto\mu^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto\mu^{5/4}.
```

This exposed the core trigger/stability tension: cold operation too near the fold is optically easy but quantum-mechanically fragile.

## Step 16: sinusoidal numerical checkpoint

For

```text
delta=0.05
beta_cold=1.5
I_c=3 uA
C=200 fF
```

exact calculation gives

```text
beta_c             = 1.14712
required Ic drop   = 23.53 %
L                  = 164.55 pH
cold barrier/k_B   = 9.443 K
local fp           = 24.80 GHz.
```

The provisional cubic MQT exponent is ~57 but is not an absolute DCR.

## Step 17: measured flux-state correction

Early reasoning used `DeltaPhi=Phi0`. Exact rf-SQUID stationary points give instead

```math
\Delta\Phi
=\frac{\Phi_0}{2\pi}(x_R-x_L).
```

For the benchmark:

```text
DeltaPhi = 0.47526 Phi0
DeltaI   = 5.97 uA.
```

Fluxoid label change therefore does not imply an exactly one-`Phi0` measured loop-flux step.

## Step 18: deterministic phase dynamics

A noiseless RCSJ pulse from `beta=1.5` to `1.05<beta_c` gives central phase passage in roughly `20 ps` across representative weak/moderate damping.

For the benchmark `sqrt(LC)=5.74 ps`. Raw phase motion is therefore unlikely to be the slow element if the thermal pulse truly drives the circuit beyond the fold.

## Step 19: first major novelty collisions

Three broad routes closed:

1. Onen et al. 2020: single-photon-to-single-flux superconducting memory already demonstrated.
2. Rochet et al. 2020: optical writing of persistent single vortices already demonstrated.
3. Zhou/Habif/Bocko/Feldman 2001: transient `I_c` suppression to lower an rf-SQUID barrier and then refreeze a flux state already proposed.

The project therefore cannot claim photon-to-flux memory or rf-SQUID tipping in broad form.

## Step 20: thermal critical-current plausibility

Jung et al. 2026 shows proximity-JJ thermal sensitivity can be strongly engineered by length, transparency, carrier density and superconducting material. This supports continuing but does not supply the required nonequilibrium CPR for the proposed detector.

## Step 21: static optical-to-fold energy closure

Define `T_f` through the actual CPR fold. For arbitrary heat capacity,

```math
\boxed{
E_{fold}
=\frac1{\eta_{th}}
\int_{T_0}^{T_f} C_e(T)dT.
}
```

For `C_e=gamma_S A T`,

```math
E_{fold}=\frac{\gamma_SA}{2\eta_{th}}(T_f^2-T_0^2).
```

Using the Huang thermal reference and a conditional `T_f<=1.2 K` in the sinusoidal benchmark gave a nonempty 10-um heat-capacity margin: a 15.5-um^2 absorber would need roughly 23% retained electronic energy. This was explicitly conditional on a comparable nonequilibrium `I_c(T_e)`.

## Step 22: general CPR fold replaces scalar `I_c`

Define

```math
I_* = \Phi_0/(2\pi L),
\qquad
\mathcal I(x,T)=I_s(x,T)/I_*,
```

```math
F(x,T)=x-\delta-\mathcal I(x,T).
```

A fold satisfies

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

This load-line tangency is the preferred formulation. A second-harmonic sensitivity test showed that CPR shape can move the required scalar-amplitude suppression from single-digit percent to above 40% at the same external tilt.

## Step 23: thermal diffusion / damping checkpoint

From Huang's reported `l_D~230 um` and `tau_ep~75 ns`:

```text
D_characteristic ~0.705 m^2/s.
```

For a `15.5 um^2` square absorber:

```text
L_abs^2/D ~22 ps,
```

comparable to the ~20-ps phase passage and far shorter than the E-Ph scale.

The simple damping envelope

```math
\tau_{damp}\sim2R_{hot}C
```

gives, for `C=200 fF`, `R_hot<25 kOhm` if the useful hot interval is 10 ns.

No obvious timescale contradiction appeared.

## Step 24: short-junction graphene CPR tested and demoted

The Titov-Beenakker short ballistic graphene CPR was implemented as a sensitivity model.

However, the Huang device has `L_JJ~600 nm`, while the quoted MoRe gap `Delta~1.3 meV` and `v_F~1e6 m/s` give

```math
\xi\sim\hbar v_F/\Delta\approx0.51 um,
```

so `L_JJ/xi~1.2`.

Therefore the short-junction closed form is **not controlled** for that device. Hagymasi/Kormanyos/Cserti arbitrary-length theory and measured CPR literature are the correct direction.

Nanda et al. measured strongly forward-skewed graphene CPR at low temperature, with skewness suppressed toward sinusoidal behavior at higher temperature. This confirms that full CPR evolution matters.

## Step 25: toy short-Dirac trigger/stability corridor

Although not predictive, the short-CPR sensitivity model revealed a useful optimization pattern for the 15.5-um^2 scaling and provisional `D=1e-6 s^-1` MQT target:

```text
beta   T_fold   eta_th,min   barrier/k_B   C_min,Q
0.60   0.787 K    0.099        0.454 K      30.3 pF
0.70   1.506 K    0.363        2.048 K       2.10 pF
0.80   2.172 K    0.755        4.409 K       0.520 pF
0.85   2.480 K    0.984        5.805 K       0.314 pF
0.90   2.769 K    1.227        7.309 K       0.206 pF
```

Too near the fold: photon energy requirement is small but quantum stability demands very large capacitance. Too far: cold stability improves but the 10-um photon cannot reach the fold under the fixed thermal scaling. An interior corridor appears in the toy model.

## Step 26: another architecture collision

Solinas, Giazotto and Pepe proposed a proximity-SQUID single-photon detector in which an antenna-coupled SNS weak link is photon-heated, its critical current is strongly suppressed, SQUID asymmetry appears, and a voltage pulse is read out.

Therefore `photon heating -> proximity-JJ I_c suppression -> SQUID detection` is also prior art. The surviving route is narrower still: persistent fold capture and/or a new quantitative closure.

## Step 27: Lambert-W quantum-capacitance constraint

Inside the provisional cubic MQT model,

```math
\Gamma_Q(C)=\frac{\omega(C)}{2\pi}
\exp\left[-\alpha_Q\frac{\Delta U_c}{\hbar\omega(C)}\right],
\qquad
\omega(C)=\sqrt{\frac{\kappa_c}{LC}}.
```

Solving `Gamma_Q=D` gives

```math
\boxed{
C_{min,Q}
=\frac{\hbar^2\kappa_c}
{\alpha_Q^2\Delta U_c^2L}
\left[
W\left(
\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}
\right)
\right]^2.
}
```

This is exact algebra within the provisional rate model, not exact dissipative rf-SQUID MQT physics.

Dynamic upper bounds are

```math
C<\frac{t_>}{2R_{hot}},
\qquad
C<\frac{t_>^2}{g^2L}.
```

Hence the necessary capacitance window

```math
\boxed{
C_{min,Q}<C<\min(C_{max,R},C_{max,\phi}).
}
```

At toy short-Dirac `beta=0.8`, `C_min,Q~0.52 pF`; with a 10-ns useful interval this requires `R_hot<~9.6 kOhm` from the simple damping envelope.

## Step 28: finite above-fold dwell time

Static `T_pk>T_f` is not enough. For monotonic lumped cooling,

```math
\boxed{
t_>(E_\gamma)
=\int_{T_f}^{T_{pk}(E_\gamma)}
\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

The circuit needs

```math
\boxed{
t_>(E_\gamma)
\ge
\max[t_{diff},\ g\sqrt{LC},\ 2R_{hot}C].
}
```

For the idealized clean-graphene laws

```math
C_e=\gamma_SAT,
\qquad
P=\Sigma A(T^4-T_0^4),
```

the integral is analytic and, importantly, has a finite maximum as `T_pk -> infinity`:

```math
\boxed{
t_{>,max}
=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right)
\simeq\frac{\gamma_S}{2\Sigma T_f^2}.
}
```

Thus if the circuit's required settling time exceeds this value, **no photon energy can save the design within this cooling model**. This is the first explicit model-level impossibility condition in the branch.

## Step 29: compact feasibility closure

Using the quantum-limited smallest allowed capacitance,

```math
\boxed{
t_{req}^*
=\max\left[
t_{diff},\ g\sqrt{LC_{min,Q}},\ 2R_{hot}C_{min,Q}
\right],
}
```

the current necessary chain is

```math
\boxed{E_\gamma\ge E_{fold},}
```

```math
\boxed{t_>(E_\gamma)\ge t_{req}^*,}
```

```math
\boxed{\Delta U_c\gtrsim k_BT_0\ln(\Omega_T/D).}
```

with `C_min,Q` defined by the Lambert-W relation above.

This combines photon energy / heat capacity, the full CPR fold, cold thermal stability, provisional MQT suppression, capacitance, diffusion, phase motion and damping.

Detailed derivation: `FEASIBILITY_CLOSURE_2026-08-15.md`.

## Current next step

The remaining bottleneck is **not** more static rf-SQUID algebra. It is a realistic arbitrary-length proximity-JJ model:

```text
I_s(phi,T)
-> fold curve T_f
-> exact cold barrier / curvature
-> improved dissipative MQT
-> photon thermal pulse with contact + E-Ph loss
-> stochastic finite-rate basin capture.
```

Broad device novelty has collided repeatedly. The most plausible surviving paper route is now a genuinely new feasibility/optimality closure or a strong impossibility result, if one survives a dedicated paper-and-patent audit.
