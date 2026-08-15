# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**.

## 1. Current physical question

Can one absorbed LWIR photon drive a temperature-dependent Josephson/rf-SQUID circuit through a directionally selected fold, after which the circuit recovers into a persistent superconducting flux state, while cold false switching remains extremely low?

Generation A uses a small external flux tilt and is **not photovoltaic**. Generation B is reserved for a later zero-external-flux mechanism if one survives collision review.

Preferred chain:

```text
8–14 um photon
 -> nonequilibrium hot-electron/quasiparticle pulse
 -> full Josephson CPR changes
 -> metastable CPR/load-line intersection reaches a fold and disappears
 -> phase enters favored basin
 -> CPR recovers
 -> persistent superconducting flux remains.
```

## 2. Noise interpretation

An ideal cold superconducting storage channel with `Re Z -> 0` lacks the ordinary finite-frequency resistive Johnson contribution of that channel. This does **not** imply zero detector noise or zero dark counts.

Relevant limits are thermal phase escape, MQT, residual quasiparticles, vortices, stray photons, readout backaction, reset errors and photon statistics.

Primary metrics: `P_capture`, `P_wrong`, DCR, stored-state SNR, reset time/energy and system optical efficiency.

## 3. General CPR fold — canonical circuit formulation

Define

```math
I_* = \frac{\Phi_0}{2\pi L},
\qquad
\mathcal I(x,T)=\frac{I_s(x,T)}{I_*},
\qquad
F(x,T)=x-\delta-\mathcal I(x,T).
```

A static fold satisfies

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

For any smooth nondegenerate one-parameter fold,

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto|p-p_f|^{5/4}.
```

This is the core trigger-vs-dark-stability tradeoff.

## 4. Arbitrary-length ballistic graphene CPR — validated ideal baseline

The current ideal CPR uses the Titov–Beenakker ballistic graphene SNS secular equation before its short-junction reduction and the Hagymasi–Kormanyos–Cserti Matsubara-current construction for arbitrary junction length.

```math
\ell=\frac{L_{JJ}}{\xi_0}=\frac{\Delta_0L_{JJ}}{\hbar v_F},
\qquad
\mu_r=\mu/\Delta_0.
```

Current baseline:

```text
Delta0 = 1.3 meV
ell    = 1.1
delta  = 0.05
T0     = 20 mK
mu/Delta0 = 0, 10, 20.
```

Canonical code:

```text
calculations/arbitrary_length_graphene_cpr.py
calculations/validate_hagymasi_intermediate_cpr.py
```

Detailed records:

```text
ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md
HAGYMASI_CPR_VALIDATION_2026-08-15.md
```

### Validation state

1. At `ell=0.01`, `mu=0`, the normalized CPR converges to the Titov–Beenakker analytic short-junction result at the sub-percent-to-percent level on the retained grids.
2. The implementation has now been benchmarked at the exact intermediate-length parameter set of Hagymasi et al. Fig. 1(c,d): `xi/L=0.91`, `mu/Delta0=0,20`, `T/Tc=0,0.18,0.35`.
3. Using `T/Tc=0.01` as the numerical low-T proxy gives skewness values approximately

| mu/Delta0 | T/Tc | S |
|---:|---:|---:|
| 0 | 0.01 | 0.329 |
| 0 | 0.18 | 0.196 |
| 0 | 0.35 | 0.063 |
| 20 | 0.01 | 0.546 |
| 20 | 0.18 | 0.250 |
| 20 | 0.35 | 0.077 |

This reproduces the published trend structure: positive low-T forward skewness, much stronger low-T skewness at high doping, rounded-sawtooth behavior around `L/xi~1.1`, and rapid suppression of skewness with temperature.

The values are stable across `(qmax,nq,wmax)=(25,400,15),(30,500,20),(35,700,25)` to the retained phase-grid resolution. This is a parameter-level validation, not a digitized point-by-point reproduction of the figure.

## 5. Ideal fold result

At `ell=1.1`, `delta=0.05`, the ideal cold normalized fold is approximately

| mu/Delta0 | cold beta_fold,norm |
|---:|---:|
| 0 | 0.463 |
| 10 | 0.325 |
| 20 | 0.200 |

The strong illustrative ideal point remains

```text
ell=1.1
mu/Delta0=20
beta_cold=0.8
Ic physical scale=3 uA
T_fold~1.118 K
cold barrier/k_B~16.70 K
L~87.76 pH
provisional C_min,Q~71 fF
state separation~0.2535 Phi0
circulating-current gap~5.97 uA.
```

Within the rigid-boundary ideal model, increasing doping mainly improves cold-state stability rather than strongly reducing the optical fold temperature.

## 6. Empirically anchored interface/skewness stress — new current uncertainty envelope

Nanda et al. measured ballistic MoRe/graphene CPRs and used tight-binding BdG calculations with explicit graphene-superconductor interfaces. Their realistic models show that interface hopping, contact-doping profile, transition smoothness and quasiparticle broadening materially change CPR skewness. Representative reported low-T scales are roughly

```text
hard-gap nn'n calculation: S~0.27
soft-gap nn'n calculation: S~0.22
soft-gap npn calculation:  S~0.19
measured nn'n:             S~0.28
measured npn:              S~0.20.
```

The ideal Experiment-03 high-doping CPR has `S~0.55`, so its shape is clearly optimistic relative to these realistic-interface scales.

A controlled shape-only sensitivity envelope was therefore introduced:

```math
f_\lambda(\phi,T)=
\operatorname{norm}[(1-\lambda)\sin\phi+\lambda f_{ideal}(\phi,T)].
```

This is **not a microscopic interface model**. It deliberately changes only harmonic/skewness shape while retaining the ideal `Ic(T)` amplitude ratio.

Canonical record:

```text
INTERFACE_SKEWNESS_SENSITIVITY_2026-08-15.md
calculations/interface_skewness_sensitivity.py
```

At `beta_cold=0.8`, `Ic=3 uA`:

| cold S scale | cold beta_fold | T_fold | cold barrier/kB | state separation | provisional C_min,Q |
|---:|---:|---:|---:|---:|---:|
| 0.548 ideal | 0.201 | 1.118 K | 16.70 K | 0.2535 Phi0 | 71 fF |
| 0.270 | 0.298 | 0.905 K | 9.12 K | 0.2401 Phi0 | 160 fF |
| 0.220 | 0.335 | 0.841 K | 7.14 K | 0.2303 Phi0 | 230 fF |
| 0.190 | 0.364 | 0.794 K | 5.89 K | 0.2225 Phi0 | 307 fF |

### Strongest current interpretation

Realistic CPR-shape suppression does **not** eliminate the fold at this illustrative circuit point, but it materially weakens cold stability:

- `T_fold` falls by about 19–29%;
- the cold barrier falls by about 45–65%;
- the provisional MQT capacitance floor increases about 2.3–4.3x;
- stored-state separation changes much less, remaining about `0.22–0.24 Phi0`.

Thus interface-induced harmonic suppression primarily attacks **dark-state stability**, not readout-state separation.

The defensible barrier statement is no longer simply `16.7 K`. Until a microscopic interface model exists, the empirically anchored shape envelope is closer to roughly **6–9 K** for realistic skewness scales at this circuit point.

## 7. Model boundary — still not a calibrated detector

The ideal arbitrary-length model assumes ballistic graphene, rigid superconducting boundaries, highly doped ideal electrodes, equilibrium Fermi distributions and no self-consistent inverse proximity effect.

The shape-only stress still holds the ideal `Ic(T)` amplitude ratio fixed. A real interface changes simultaneously

```text
absolute Ic
Ic(T)
induced superconducting gap
CPR harmonics
normal resistance/damping
contact heat diffusion
quasiparticle spectrum.
```

Nanda et al. explicitly report that the induced superconducting gap in graphene can be smaller than the bulk MoRe gap and that realistic contacts are needed to reproduce measured temperature behavior. That reduced induced-gap scale is now the highest-value next stress parameter.

## 8. Optical fold-energy and finite-dwell closure

For arbitrary electronic heat capacity,

```math
\eta_{th}E_\gamma=\int_{T_0}^{T_{pk}}C_e(T)dT,
\qquad
\boxed{E_{fold}=\frac1{\eta_{th}}\int_{T_0}^{T_f}C_e(T)dT.}
```

For lumped monotonic cooling,

```math
\boxed{t_>(E_\gamma)=\int_{T_f}^{T_{pk}(E_\gamma)}\frac{C_e(T)}{P_{cool}(T)}dT.}
```

Necessary write-time condition:

```math
\boxed{t_>(E_\gamma)\ge\max[t_{diff},g\sqrt{LC},2R_{hot}C].}
```

For idealized clean graphene `C_e=gamma_S A T`, `P_e-ph=Sigma A(T^4-T_0^4)`, the above-fold interval has a finite maximum

```math
\boxed{t_{>,max}=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right).}
```

Thus `t_req >= t_>,max` is a model-level impossibility condition.

## 9. Cold stability / capacitance closure

Inside the current provisional cubic-MQT rate model,

```math
\boxed{
C_{min,Q}
=\frac{\hbar^2\kappa_c}{\alpha_Q^2\Delta U_c^2L}
\left[W\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right)\right]^2.
}
```

Write dynamics requires

```math
C<C_{max,R}=t_>/(2R_{hot}),
\qquad
C<C_{max,\phi}=t_>^2/(g^2L).
```

Necessary nonempty window:

```math
\boxed{C_{min,Q}<C<\min(C_{max,R},C_{max,\phi}).}
```

This remains a diagnostic, not exact dissipative rf-SQUID MQT theory.

## 10. Prior-art boundary

No novelty claim is authorized. Broad routes already collided with prior art, including

```text
LWIR superconducting single-photon detection
infrared photon -> hot graphene -> Josephson switching
photon heating -> proximity-JJ Ic suppression -> SQUID detection
single photon -> persistent superconducting single-flux memory
optical heating -> permanent superconducting flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven superconducting phase battery/vorticity
non-sinusoidal temperature-dependent graphene CPR.
```

The possible paper route remains a quantitative feasibility/optimality or impossibility closure if a nontrivial result survives realistic nonideal and dynamical modeling plus a dedicated paper/patent collision audit.

## 11. Immediate next falsification step

The ideal CPR implementation has passed both short-limit and intermediate-length parameter checks. The next priority is now specifically the **induced-gap/interface temperature scale**, not more ideal CPR algebra.

1. Introduce `r_Delta=Delta_ind(0)/Delta_bulk(0)` over a realistic range while retaining the empirically anchored CPR-shape envelope.
2. Recompute `Ic(T)`, `T_fold`, barrier, state separation and provisional capacitance window.
3. Determine whether modest `r_Delta<1` collapses the fold/dwell/stability corridor.
4. If the corridor survives, proceed to a microscopic contact-doping/transparency model or calibrated TB-BdG calculation.
5. Then address early-time nonequilibrium distribution, dissipative full-CPR MQT, stochastic fold passage/retrapping, and real 8–14-um optical coupling/reset/readout.

## 12. Current verdict

**GO for continued theory. NO-GO for manuscript.**

The current result is stronger than the ideal-model checkpoint because it has survived a first empirically anchored CPR-shape nonideality stress. However, the ideal high-doping stability advantage was reduced substantially. The next decisive question is whether a reduced induced superconducting gap destroys the remaining 6–9-K-class cold barrier / sub-kelvin fold corridor.