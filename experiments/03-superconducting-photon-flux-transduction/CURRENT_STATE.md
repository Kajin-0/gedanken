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
```

and

```math
F(x,T)=x-\delta-\mathcal I(x,T).
```

A static fold satisfies

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

Geometrically the temperature-dependent Josephson CPR becomes tangent to the inductive load line.

For any smooth nondegenerate one-parameter fold,

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto|p-p_f|^{5/4}.
```

This is the core trigger-vs-dark-stability tradeoff.

The old sinusoidal checkpoint remains useful only as a regression:

```text
delta=0.05, beta_cold=1.5, Ic=3 uA
beta_fold=1.14712
required scalar Ic drop=23.53 %
L=164.55 pH
cold barrier/k_B=9.443 K
state separation=0.4753 Phi0=5.97 uA.
```

## 4. Arbitrary-length ballistic graphene CPR — current preferred static model

The current CPR calculation uses:

1. the Titov–Beenakker ballistic graphene SNS secular equation before its short-junction reduction;
2. the Hagymási–Kormányos–Cserti Matsubara-current construction, which is applicable to arbitrary junction length within the ideal ballistic/rigid-boundary model;
3. a wide-junction continuum integral over `Q=qL`.

Dimensionless variables:

```math
\ell=\frac{L_{JJ}}{\xi_0}=\frac{\Delta_0L_{JJ}}{\hbar v_F},
\qquad
\mu_r=\mu/\Delta_0.
```

Current checkpoint:

```text
Delta0 = 1.3 meV
ell    = 1.1
delta  = 0.05
T0     = 20 mK
mu/Delta0 = 0, 10, 20.
```

### Validation

- In the controlled `ell -> 0`, `mu=0` limit, the normalized Matsubara CPR converges to the Titov–Beenakker Dirac-point short-junction form; at `ell=0.01` the current finite-grid calculation is at the sub-percent-to-percent normalized-CPR level.
- At `ell~1.1`, the model develops a strongly forward-skewed low-temperature CPR and thermal softening qualitatively consistent with arbitrary-length graphene-JJ theory.
- `Qmax~30` is needed for stable finite-doping cold-fold values around `mu/Delta0=20`; smaller transverse cutoffs bias the fold downward.

Canonical script:

```text
calculations/arbitrary_length_graphene_cpr.py
```

Detailed checkpoint:

```text
ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md
```

## 5. Arbitrary-length fold results

At `ell=1.1`, `delta=0.05`, the cold normalized fold is approximately

| `mu/Delta0` | cold `beta_fold,norm` |
|---:|---:|
| 0 | 0.463 |
| 10 | 0.325 |
| 20 | 0.200 |

For `mu/Delta0=20`:

| `beta_cold` | `T_fold` | reference heat fraction* | cold barrier/k_B | provisional `C_min,Q` |
|---:|---:|---:|---:|---:|
| 0.30 | 0.197 K | 0.006 | 1.14 K | 19.9 pF |
| 0.40 | 0.390 K | 0.024 | 3.41 K | 2.11 pF |
| 0.50 | 0.587 K | 0.055 | 6.34 K | 0.571 pF |
| 0.60 | 0.776 K | 0.096 | 9.65 K | 0.233 pF |
| 0.70 | 0.954 K | 0.145 | 13.14 K | 0.120 pF |
| 0.80 | 1.118 K | 0.200 | 16.70 K | 0.071 pF |
| 0.90 | 1.271 K | 0.258 | 20.23 K | 0.0465 pF |
| 1.00 | 1.413 K | 0.319 | 23.70 K | 0.0328 pF |
| 1.20 | 1.668 K | 0.445 | 30.31 K | 0.0188 pF |

*Reference heat fraction uses the earlier equal-area graphene `C_e ∝ T` scaling relative to a `2.5 K` peak. It is not system absorption efficiency.

### Strong illustrative point

At

```text
ell=1.1
mu/Delta0=20
beta_cold=0.8
Ic,0 physical scale=3 uA
```

the ideal model gives

```text
T_fold                     ~1.118 K
reference retained heat    ~0.200
cold barrier/k_B           ~16.70 K
L                           87.76 pH
provisional C_min,Q        ~71 fF
state separation           ~0.2535 Phi0
circulating-current gap    ~5.97 uA.
```

This is materially more favorable than the short-junction sensitivity model, which gave `T_fold~2.17 K` and `C_min,Q~0.52 pF` at a superficially similar beta.

### Doping lesson

At `beta_cold=0.8`, changing `mu/Delta0` from 0 to 20 changes `T_fold` only from about `1.154 K` to `1.118 K`, but raises the cold barrier from about `7.0 K` to `16.7 K` and lowers the provisional `C_min,Q` from about `262 fF` to `71 fF`.

Within this ideal model, doping primarily buys **cold-state stability**, not a dramatically smaller photon threshold.

## 6. Model boundary — still not a calibrated device

The arbitrary-length model assumes ballistic graphene, rigid step-function superconducting boundaries, highly doped ideal superconducting electrodes, ideal interfaces, equilibrium Fermi distributions and no self-consistent inverse proximity effect.

The 2026 MoRe/graphene detector has a `600 nm` channel. With the quoted `Delta~1.3 meV` and `v_F~1e6 m/s`, `xi0~0.5 um`, so `ell~O(1)` is a reasonable **regime** but `ell=1.1`, `mu/Delta0=10–20` are not calibrated device parameters.

The next model must attack interface transparency/contact doping and nonequilibrium CPR evolution rather than treating the present table as a fabricated-device prediction.

## 7. Optical fold-energy closure

For arbitrary electronic heat capacity,

```math
\eta_{th}E_\gamma=\int_{T_0}^{T_{pk}}C_e(T)dT.
```

Static fold energy:

```math
\boxed{
E_{fold}=\frac1{\eta_{th}}\int_{T_0}^{T_f}C_e(T)dT.
}
```

For `C_e=gamma_S A T`:

```math
E_{fold}=\frac{\gamma_SA}{2\eta_{th}}(T_f^2-T_0^2).
```

`T_f` now comes from the **full arbitrary-length CPR/load-line fold**, not an assumed scalar `I_c(T)`.

## 8. Finite dwell above the fold

For lumped monotonic cooling,

```math
\boxed{
t_>(E_\gamma)=
\int_{T_f}^{T_{pk}(E_\gamma)}
\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

Necessary write-time condition:

```math
\boxed{
t_>(E_\gamma)\ge
\max[t_{diff},\ g\sqrt{LC},\ 2R_{hot}C].
}
```

Using published graphene characteristic scales `l_D~230 um`, `tau_ep~75 ns`, the inferred cross-device diffusivity is about `0.705 m^2/s`; a `15.5 um^2` square absorber has an `L^2/D` scale near `22 ps`.

For the idealized clean-graphene laws

```math
C_e=\gamma_SAT,
\qquad
P_{e-ph}=\Sigma A(T^4-T_0^4),
```

the above-fold interval has a finite maximum even as photon energy tends to infinity:

```math
\boxed{
t_{>,max}
=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right).
}
```

Thus `t_req >= t_>,max` is a model-level **impossibility condition**.

## 9. Cold stability / capacitance closure

The current provisional cubic-MQT model gives a Lambert-W capacitance floor

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

This is exact algebra **inside the assumed MQT rate**, not exact dissipative rf-SQUID escape physics.

Write dynamics gives

```math
C<C_{max,R}=t_>/(2R_{hot}),
\qquad
C<C_{max,\phi}=t_>^2/(g^2L).
```

Necessary nonempty capacitance window:

```math
\boxed{
C_{min,Q}<C<\min(C_{max,R},C_{max,\phi}).
}
```

Define

```math
\boxed{
t_{req}^*=\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}].}
```

The compact necessary chain remains

```math
\boxed{E_\gamma\ge E_{fold},}
```

```math
\boxed{t_>(E_\gamma)\ge t_{req}^*,}
```

```math
\boxed{\Delta U_c\gtrsim k_BT_0\ln(\Omega_T/D).}
```

Detailed derivation: `FEASIBILITY_CLOSURE_2026-08-15.md`.

## 10. Prior-art boundary

Broad novelty claims already closed include:

```text
LWIR superconducting single-photon detection
infrared photon -> hot graphene -> Josephson switching
photon heating -> proximity-JJ Ic suppression -> SQUID voltage detection
single photon -> persistent superconducting single-flux memory
optical heating -> permanent superconducting flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven superconducting phase battery/vorticity
non-sinusoidal temperature-dependent graphene CPR.
```

No novelty claim is authorized.

## 11. Immediate next falsification step

The arbitrary-length ideal CPR problem has now been implemented. The next priority is **nonideality and dynamics**, not more short-junction algebra:

1. validate the arbitrary-length implementation quantitatively against published CPR/skewness curves;
2. introduce finite/nonideal SG interface transparency and realistic contact doping;
3. calibrate `ell`, `mu/Delta0`, `Delta(T)` and `Ic` to a plausible photon-sensitive weak link;
4. replace equilibrium `T` with the early-time nonequilibrium electron distribution or justify rapid local thermalization;
5. compute dissipative MQT for the full-CPR cold potential;
6. solve stochastic time-dependent fold passage/retrapping with `R_hot(T)`;
7. add 8–14-um antenna/cavity absorptance and reset/readout.

## 12. Current verdict

**GO for continued theory. NO-GO for manuscript.**

The arbitrary-length ideal calculation strengthens physical feasibility substantially relative to the short-junction toy model. The remaining possible paper contribution is increasingly a quantitative feasibility/optimality or impossibility closure, not the broad device concept.
