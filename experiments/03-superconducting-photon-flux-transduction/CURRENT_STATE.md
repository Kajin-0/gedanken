# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15 late-session checkpoint  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**.

## 1. Current physical question

Can one absorbed LWIR photon drive a proximity-Josephson/rf-SQUID phase coordinate into a directionally favored metastable basin with high probability, leave a persistent superconducting flux state after recovery, and simultaneously satisfy a very low dark-switch target under **one physically consistent passive environment**?

Current internal description:

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

Generation A uses external flux tilt and is **not photovoltaic**. Generation B remains reserved for a later zero-external-flux / intrinsic-directionality mechanism if this theory survives.

## 2. Canonical reduced model

Static / CPR parameters:

```text
BETA_COLD  = 0.80
LAMBDA_MIX = 0.590
L           = 111.5 pH
T0          = 20 mK
```

The design coordinate now being optimized is positive directional tilt `delta`.

Electrical reference:

```text
C0 = 215 fF
R0 = 80 ohm
alpha = omega_D / omega_c = 0.90
```

Passive bath topology:

```text
phase port -- Lf -- node -- (R || Cf) -- ground
```

with

\[
L_f=\frac{\sqrt2R}{\omega_D},\qquad
C_f=\frac{1}{\sqrt2R\omega_D},
\]

and

\[
\boxed{\operatorname{Re}Y(\omega)=\frac{1/R}{1+(\omega/\omega_D)^4}}.
\]

The same positive-real two-pole environment is used for photon capture, the Euclidean dark saddle, and the fluctuation determinant.

## 3. Capture probabilities remain screening quantities

Photon-capture Monte Carlo uses a real Gaussian force with the **symmetrized** quantum-FDT spectrum plus a cold harmonic Wigner initial state. This is a truncated-Wigner / semiclassical stress model.

Therefore

```text
P_final from sym-FDT TWA != exact physical quantum efficiency.
```

The current comparison uses

```text
lambda = 14 um
rise   = 20 ps
post-pulse classification horizon = 2 ns
Ntraj  = 1024 per coarse area point
dt     = 0.125 ps
```

The reduced thermal model has the exact similarity

\[
\boxed{P_{cap}(\lambda,A,\eta_{abs})=\mathcal P(\eta_{abs}/(A\lambda))},
\]

so at fixed absorption model

\[
\boxed{A_p\lambda=\text{constant}}.
\]

Any equivalent wavelength inferred from this relation is a **reduced-model similarity result**, not a realistic broadband optical prediction.

## 4. Major rejected approximations / closed rescue branches

### Cubic MQT surrogate — rejected

At the original live neighborhood the old cubic formula gave roughly `B~38`, but the exact isolated zero-energy bounce is

\[
\boxed{B_{iso}=25.033050}.
\]

The full same-environment zero-temperature nonlocal bounce at `delta=.05, C=215 fF, R=80 ohm` is

\[
\boxed{B_{diss}=29.765636}.
\]

The original electrical point is therefore dark-unstable under the current model.

### Low-tilt rescue — rejected

Lower tilt increases dark action but destroys one-sided stochastic photon capture. Example: at `delta=.035`, even `A=80 um^2` gave only `P_final~0.922` in the relevant screen.

### Beta/barrier-shape rescue — rejected in the current neighborhood

Mild shaping such as `beta=.825` raises the Euclidean action but increases the photon-trigger fold enough that its equal-dark-action capture frontier is substantially worse than the `beta=.80` family.

### Dominant rescue direction

Increase directional tilt, then compensate the lost dark stability electrically. This simultaneously lowers the photon-trigger fold and strengthens directional basin bias while the added capacitance restores dark suppression at the cost of slower phase dynamics.

## 5. Exact electrical similarity

At fixed loop inductance, static CPR, tilt, and normalized two-pole bath topology,

\[
\boxed{C'=r^2C,\qquad R'=R/r,\qquad \omega_D'=\omega_D/r}.
\]

Then

\[
\omega_c'=\omega_c/r,
\qquad g'=g,
\qquad \alpha'=\alpha.
\]

At zero temperature the entire Euclidean action scales exactly:

\[
\boxed{B'=rB}.
\]

At finite temperature the stronger exact identity is

\[
\boxed{B(T;r)=rB_0(rT)}.
\]

The local sphaleron Matsubara-instability temperature obeys

\[
\boxed{T_\times(r)=T_{\times,0}/r}.
\]

For the calibrated periodic-instanton one-loop prefactor away from a branch singularity,

\[
\boxed{A_{1\ell}(T;r)=r^{-1/2}A_{1\ell,0}(rT)}.
\]

This similarity is central to all current dark optimization.

## 6. Finite-temperature dissipative instanton and determinant are numerically controlled

The physical Euclidean period is

\[
P_s=\frac{\hbar\omega_c}{k_BT}.
\]

The finite-period solver retains the constant mode plus cosine Matsubara modes and uses the exact two-pole nonlocal kernel. Accepted periodic saddles have exactly one negative even mode.

The full fluctuation Hessian includes:

- even constant/cosine sector;
- odd sine sector;
- one negative even mode;
- one odd translation zero mode.

The translation zero-mode overlap is numerically unity.

The determinant has an analytic high-frequency curvature tail. After UV correction, representative `N=80 -> 96` changes in `log D` are only a few parts in `10^-6`.

### Cubic normalization calibration

For the canonical cubic metastable benchmark,

\[
D_{op}^{exact}=\sqrt{60}=7.74596669,
\]

while the numerical calculation gives

\[
D_{op}^{num}=7.74565249,
\]

with relative error about `4.1e-5`.

The correct conversion from dimensionless-action Hessians is

\[
\boxed{D_{op}=D_{raw}/\sqrt{A_k}}.
\]

The resulting calibrated periodic-instanton one-loop prefactor is

\[
\boxed{A_{1\ell}=\omega_c\sqrt{\frac{I_s}{2\pi}}D_{raw,corr}},
\]

and

\[
\boxed{\Gamma_{1\ell}=A_{1\ell}e^{-B}}.
\]

## 7. Current dark-design constraint

The former fixed exponent `B=37.61` is obsolete as a final design criterion.

The current reduced-model constraint is

\[
\boxed{\Gamma_{1\ell}(T_0=20\,\mathrm{mK};\delta,r)=10^{-6}\ \mathrm{s}^{-1}}.
\]

Regular Gaussian periodic-instanton roots already obtained:

| delta | r_rate | C | R | fc | B20 | T0/Tx |
|---:|---:|---:|---:|---:|---:|---:|
| .200 | 7.60969 | 12.450 pF | 10.513 ohm | 2.884 GHz | 39.482 | 0.588 |
| .205 | ~8.55 | 15.7 pF | 9.36 ohm | 2.53 GHz | ~39.35 | ~0.71 |
| .2075 | 9.09670 | 17.791 pF | 8.794 ohm | 2.355 GHz | 39.269 | 0.775 |
| .210 | 9.82570 | 20.757 pF | 8.142 ohm | 2.161 GHz | 39.184 | 0.839 |
| .211 | 10.18791 | 22.316 pF | 7.852 ohm | 2.077 GHz | 39.149 | 0.871 |
| .212 | 10.62176 | 24.257 pF | 7.532 ohm | 1.985 GHz | 39.115 | 0.910 |

The old solver found a formal `.213` Gaussian root but at `T0/Tx=0.962`, so that result is not canonical. It found no root at `.214` before the local Matsubara instability. Those statements are now superseded by the first-order-crossover correction in Sec. 9 below.

## 8. One-loop-rate-constrained 2-ns capture frontier

On the self-consistent `Gamma_1loop=1e-6/s` manifold, the coarse 14-um / 2-ns screens give approximately

```text
delta=.200   A99 ~ 420 um^2
delta=.205   A99 ~ 458 um^2
delta=.2075  A99 ~ 472 um^2
delta=.210   A99 ~ 485 um^2
```

The frontier is still increasing through `.210`.

Active workflow `experiment03-one-loop-edge-capture.yml` is resolving `.211` and `.212`, the last points that were clean under the pre-correction Gaussian classification.

No final Generation-A optimum is declared yet.

## 9. CRITICAL NEW CORRECTION: the local Matsubara instability is not the physical crossover

The finite-T solver originally assumed that the sphaleron's first nonzero Matsubara eigenvalue crossing,

\[
\Lambda_1(T_\times)=0,
\]

was also the physical quantum-to-thermal crossover.

A direct O(2) quartic center-manifold test has **falsified that assumption** for the relevant high-tilt branch.

At `.212` and `.213`, as `T -> T_x^-`, the accepted lowest-action one-negative-mode periodic instanton does **not** shrink continuously into the sphaleron. Instead:

- the periodic first-harmonic amplitude remains finite;
- `B_sph - B_per` remains finite (of order 0.4–0.5 even at `0.996 Tx`);
- an effective quartic coefficient inferred from `lambda^2/(4 DeltaB)` collapses rather than converging;
- the simple second-order soft-mode formula fails badly.

Therefore the proposed quartic uniform correction

\[
\frac12\left[1+\operatorname{erf}\sqrt{B_{sph}-B_{per}}\right]
\]

is **rejected for the physical finite-amplitude branch**.

This behavior is consistent with a **first-order quantum-to-thermal escape crossover**: a finite-amplitude periodic branch remains relevant through the sphaleron's local linear-instability temperature, and the physical crossover must be found from the competing actions/rates rather than by setting `T=Tx`.

The current finite-T solver is therefore incomplete above `Tx` because it automatically switches to the sphaleron there.

Active workflow:

```text
experiment03-first-order-crossover-branch.yml
```

continues the same one-negative-mode periodic branch through and above `Tx` and searches for

\[
\boxed{B_{per}(T_c)=B_{sph}(T_c)}.
\]

The corresponding electrical scale is

\[
\boxed{r_c=T_c/T_0}.
\]

Until this branch continuation finishes, `.213/.214` cannot be classified as physical dark-rate NO-GO points.

## 10. Second correction: sphaleron action is an exponent ceiling, not an absolute rate ceiling

Earlier notes sometimes treated

\[
B_{sph}=\Delta U/(k_BT)
\]

as implying that capacitance cannot further reduce the dark **rate** once thermal activation dominates. That statement is too strong.

For linear memory friction the classical barrier-crossing rate has the generalized Kramers/Grote-Hynes structure

\[
\boxed{\Gamma_{th}=\frac{\omega_m}{2\pi}\frac{\lambda_b}{\omega_b}e^{-\Delta U/k_BT}},
\]

with positive unstable growth rate

\[
\boxed{C\lambda_b^2+\lambda_bY_L(\lambda_b)+F_s/L=0}.
\]

Under the electrical similarity, the exponent stops increasing in the thermal regime but the dynamical prefactor continues to scale approximately as `1/r`. Thus additional electrical inertia can still reduce the thermal rate **algebraically**.

The prior `delta_ceiling=0.215024` should therefore be interpreted as an exponent/action landmark, not an absolute physical rate termination.

## 11. Immediate recovery queue

1. Finish `experiment03-one-loop-edge-capture.yml` and determine the `.211/.212` coarse `A99` frontier.
2. Finish `experiment03-first-order-crossover-branch.yml` and establish whether the finite-amplitude one-negative-mode periodic branch persists above local `Tx`, where it crosses the sphaleron action, and whether it folds first.
3. Replace the current `finiteT_bounce()` hard switch at `T>=Tx` with branch-aware selection.
4. Recompute the physical dark-rate manifold across the actual first-order crossover, including both periodic and generalized thermal rates.
5. Only then extend photon-capture optimization beyond `.212`.
6. After the dark topology is fixed, return to the larger unresolved requirement: a detailed-balance-preserving nonlinear quantum/open-system capture model.

## 12. Publication / claim boundary

**GO for continued theory. NO-GO for manuscript.**

Do not claim:

- exact physical quantum efficiency;
- complete physical dark-count rate;
- novelty of a superconducting photon/flux latch;
- a final optimized detector;
- a room-temperature or broadband detector result.

The current strongest legitimate statement is narrower:

> Within the reduced same-environment model, high directional tilt plus electrical inertia produces a strong photon-threshold / dark-stability trade that substantially outperforms the original low-tilt design. Finite-temperature instanton and one-loop calculations are numerically controlled away from crossover, but the high-tilt dark frontier has exposed a first-order quantum-to-thermal branch topology that must be resolved before a final operating point is selected.
