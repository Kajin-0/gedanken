# Experiment 03 — Dimensionless capture control map — 2026-08-15

## Status

**Exact nondimensionalization of the current reduced two-pole model, plus heuristic interpretation of one derived exposure variable. Not novelty-audited.**

This note collects the minimum dimensionless groups that control the current reduced photon-latch calculation. It is intended to prevent future work from treating dimensional choices such as `R`, `C`, `lambda`, and absorber area as independent when the equations only depend on particular combinations.

## 1. Phase/filter normalization

The current passive two-pole environment is

\[
LC\dot v+d+F(x,T)=0,
\]

\[
\dot d=\frac{L}{L_f}(v-w),
\]

\[
\dot w=\frac{d}{LC_f}-\frac{w}{RC_f},
\]

with

\[
L_f=\frac{\sqrt2 R}{\omega_D},
\qquad
C_f=\frac{1}{\sqrt2 R\omega_D}.
\]

Let the cold operating point have curvature

\[
\kappa_c=\left.\frac{\partial F}{\partial x}\right|_{c},
\]

and define

\[
\omega_c^2=\frac{\kappa_c}{LC}.
\]

Use dimensionless time and filter variables

\[
s=\omega_ct,
\qquad
u=\frac{v}{\omega_c}=\frac{dx}{ds},
\qquad
D=\frac{d}{\kappa_c},
\qquad
W=\frac{w}{\omega_c},
\]

and normalized CPR force

\[
f(x,T)=\frac{F(x,T)}{\kappa_c}.
\]

Define the two circuit/environment groups

\[
\boxed{
 g=\frac{1}{RC\omega_c}
},
\qquad
\boxed{
 \alpha=\frac{\omega_D}{\omega_c}
}.
\]

The phase/filter equations reduce exactly to

\[
\boxed{
\frac{d^2x}{ds^2}=-(D+f)
},
\]

\[
\boxed{
\frac{dD}{ds}=\frac{\alpha g}{\sqrt2}(\nu-W)
},
\]

\[
\boxed{
\frac{dW}{ds}=\sqrt2\alpha\left(\frac{D}{g}-W\right)
}.
\]

Thus, after fixing the normalized CPR family, the passive two-pole phase/environment dynamics do **not** depend separately on `R`, `C`, and `omega_D`; they depend on them through `g` and `alpha`.

## 2. Optical thermal-drive group

From the exact reduced-model optical similarity theorem, define

\[
\chi_E
=\frac{T_{\rm ad}^2-T_0^2}
       {T_f^2-T_0^2}.
\]

`chi_E=1` is the static calorimetric energy density required to reach the fold temperature. Since

\[
T_{\rm ad}^2-T_0^2
\propto\frac{\eta_{\rm abs}}{A\lambda},
\]

`chi_E` is proportional to the reduced optical drive

\[
\frac{\eta_{\rm abs}}{A\lambda}
\]

for fixed material/fold scale.

The finite-rise group is

\[
\boxed{\rho=\omega_c\tau_{\rm rise}}.
\]

The cooling law contributes additional dimensionless groups obtained by dividing the thermal ODE by `omega_c`; these must remain explicit when the cooling model is varied.

## 3. Finite capture window

Let

\[
t_c=\text{first favored-side crossing},
\]

\[
t_r=\text{cooling-side competing-well reformation}.
\]

The dimensionless capture interval is

\[
\boxed{
\Delta s_C=\omega_c(t_r-t_c)
}.
\]

A necessary condition for the simple `cross first, then trap as the competing well reforms` mechanism is

\[
\boxed{\Delta s_C>0}.
\]

This is exact for that stated mechanism; it is not sufficient for high-fidelity capture.

## 4. Stage-selective filter response

Define the trajectory-conditioned effective dissipative factors

\[
H_{\rm eff,L}^2
=\frac{\int_{0}^{t_c}w^2dt}
       {\int_{0}^{t_c}v^2dt},
\]

\[
H_{\rm eff,C}^2
=\frac{\int_{t_c}^{t_r}w^2dt}
       {\int_{t_c}^{t_r}v^2dt}.
\]

Their ratio is

\[
\boxed{
\mathcal A
=\frac{H_{\rm eff,L}^2}{H_{\rm eff,C}^2}
}.
\]

`mathcal A<1` means the realized nonlinear trajectory is filtered so that resistor-coupled phase-rate power is suppressed more strongly during launch than during capture. This is a **trajectory diagnostic**, not a universal capture criterion.

## 5. Capture damping exposure

For a nearly harmonic oscillatory coordinate, total phase-mode energy satisfies approximately

\[
\frac{\dot E}{E}
\sim-\frac{H_{\rm eff}^2}{RC}.
\]

This motivates the dimensionless finite-window capture exposure

\[
\boxed{
\Lambda_C
=\frac{H_{\rm eff,C}^2}{RC}(t_r-t_c)
=g H_{\rm eff,C}^2\Delta s_C
}.
\]

Within a locally harmonic constant-envelope approximation, `Lambda_C` is the number of **energy-damping e-folds** available between favored-side crossing and well reformation.

Important:

- the identity `Lambda_C=g H_eff,C^2 Delta s_C` is exact from the definitions;
- interpreting it as an exponential energy-decay count is approximate because the real capture stage is nonlinear and time-dependent;
- the exact passive energy identity remains the authoritative deterministic energy accounting.

## 6. Current R80 / 14-um illustration

For the present `rDelta=.6`, `R=80 ohm`, `C=215 fF`, cold `fc~27.256 GHz` case,

\[
g\simeq0.3395.
\]

The deterministic area sweep gives approximately:

| A (um^2) | P_final sym-TWA screen | mathcal A | Lambda_C |
|---:|---:|---:|---:|
| 80 | 0.9990 | 0.836 | 1.94 |
| 84 | 0.9941 | 0.854 | 1.61 |
| 86 | 0.9897 | 0.994 | 1.22 |
| 88 | 0.9858 | 1.47 | 0.69 |
| 90 | 0.9763 | 2.22 | 0.36 |

At `A=100 um^2`, the deterministic favored-side crossing occurs only after the competing well has already reformed, so this launch/capture decomposition ceases to apply.

The near-coincidence between the current `P~.99` boundary, `mathcal A~1`, and `Lambda_C~O(1)` is a hypothesis under cross-parameter stress. None of these numerical values is an exact quantum efficiency threshold.

## 7. Reduced capture map

The current reduced model can therefore be organized schematically as

\[
\boxed{
P_{\rm cap}
=\mathcal P(
\chi_E,\rho,g,\alpha,
\text{dimensionless cooling groups},
\text{normalized CPR topology},
\text{bath-state model}
)
}.
\]

`mathcal A`, `Delta s_C`, and `Lambda_C` are derived trajectory observables of these controls, not independent input parameters.

## 8. Research use

Future parameter scans should report dimensionless controls alongside dimensional device values. A result that fails to collapse under this normalization identifies either

1. a genuinely additional physical parameter, or
2. a numerical/model inconsistency.

No novelty claim is authorized.
