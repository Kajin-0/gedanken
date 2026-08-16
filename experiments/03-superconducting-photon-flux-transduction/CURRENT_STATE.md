# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-16 / certified `.212` frontier + `.214` safe-side gate  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**

Primary newest checkpoint:

```text
RATE_FRONTIER_PROMOTION_2026-08-16.md
```

## 1. Current physical question

Can one absorbed LWIR photon drive a proximity-Josephson/rf-SQUID phase coordinate into a directionally favored metastable basin with high probability, leave a persistent superconducting flux state after recovery, and simultaneously satisfy a very low dark-switch target under **one physically consistent passive environment**?

Current internal description:

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

Generation A uses external flux tilt and is **not photovoltaic**.

## 2. Live reduced model

```text
BETA_COLD  = 0.80
LAMBDA_MIX = 0.590
L           = 111.5 pH
T0          = 20 mK
C0          = 215 fF
R0          = 80 ohm
alpha       = omega_D/omega_c = 0.90
```

Main design coordinate: positive directional tilt `delta`.

Passive bath:

```text
phase node -- Lf -- internal node -- (R || Cf) -- ground
```

\[
L_f=\frac{\sqrt2R}{\omega_D},
\qquad
C_f=\frac{1}{\sqrt2R\omega_D},
\]

\[
\boxed{
\operatorname{Re}Y(\omega)=
\frac{1/R}{1+(\omega/\omega_D)^4}
}.
\]

The same positive-real environment is used in real-time capture, Euclidean dark escape and the fluctuation determinant.

## 3. Exact electrical similarity

At fixed static potential / loop inductance / normalized bath topology,

\[
\boxed{
C\to r^2C,
\qquad
R\to R/r,
\qquad
\omega_D\to\omega_D/r
}
\]

and

\[
\omega_c\to\omega_c/r.
\]

Zero temperature:

\[
\boxed{B\to rB}.
\]

Finite temperature:

\[
\boxed{B(T;r)=rB_0(rT)}.
\]

For a regular periodic instanton away from a bifurcation,

\[
\boxed{
A_{1\ell}(T;r)=r^{-1/2}A_{1\ell,0}(rT)
}.
\]

These identities have been numerically regression-tested on the full nonlocal finite-period saddle.

## 4. Dark-rate calculation used for safe-side designs

The old cubic MQT surrogate is rejected. In the original low-tilt neighborhood,

\[
B_{iso}=25.033050,
\qquad
B_{diss}=29.765636,
\]

rather than the old cubic estimate near 38.

The finite-temperature periodic instanton uses the exact two-pole nonlocal kernel. The regular decay saddle has one negative even mode and one odd translation zero mode.

The determinant has an analytic UV tail correction. Absolute normalization was independently calibrated against the canonical cubic metastable problem:

\[
D_{op}^{exact}=\sqrt{60}=7.74596669,
\qquad
D_{op}^{num}=7.74565249.
\]

The correct dimensionless-action conversion is

\[
D_{op}=D_{raw}/\sqrt{A_k},
\]

and the calibrated regular periodic one-loop rate is

\[
\boxed{
\Gamma_{per}
=
\omega_c\sqrt{\frac{I_s}{2\pi}}
D_{raw,corr}
\,e^{-B_{per}}.
}
\]

The independent same-environment thermal memory-friction screen is

\[
\boxed{
\Gamma_{th}
=\frac{\omega_m}{2\pi}
\frac{\lambda_b}{\omega_b}
 e^{-\Delta U/(k_BT_0)}
}
\]

with

\[
C\lambda_b^2+\lambda_bY_L(\lambda_b)+F_s/L=0.
\]

Current reduced dark design target:

\[
\boxed{
\Gamma_{dark}\equiv\Gamma_{per}+\Gamma_{th}
=10^{-6}\ \mathrm{s}^{-1}
}
\]

when the relevant periodic saddle is safely within a single-saddle Gaussian regime.

This is **not** a complete physical DCR: quasiparticle, vortex, stray-photon, cosmic/environmental and technical-noise channels remain absent.

## 5. Critical finite-T topology: `r_x != r_c != r_f`

The former identification of the sphaleron's first Matsubara instability with the physical quantum/thermal crossover is rejected.

Three distinct scales exist at high tilt:

1. `r_x`: local sphaleron first-Matsubara instability;
2. `r_c`: finite-amplitude periodic/sphaleron action crossing;
3. `r_f`: finite-amplitude periodic-instanton saddle-node/fold.

Representative results:

| delta | r_x | r_c | r_f |
|---:|---:|---:|---:|
| .212 | 11.67660 | 12.18208 | not needed for current safe representative |
| .213 | 11.64824 | 12.03349 | 12.16227131 |
| .214 | 11.61108 | 11.88538 | 12.0069623 |
| .215 | 11.56485 | 11.73736 | 11.85159085 |

The simple continuous O(2) quartic sphaleron-soft-mode model was explicitly tested and **rejected**: the physical periodic branch remains finite-amplitude through local `T_x`.

## 6. Periodic fold catastrophe is established numerically

Pseudo-arclength continuation passes through the finite-amplitude periodic fold and recovers a two-negative companion branch. The additional even Hessian mode crosses zero while the odd translation zero mode remains distinct.

With

\[
\mu=p_f-p,
\qquad p=r/r_x,
\]

fine scaling gives:

| delta | `Delta B` exponent | soft-eigenvalue exponent |
|---:|---:|---:|
| .213 | 1.5060 | 0.4859 |
| .214 | 1.5022 | 0.4840 |
| .215 | 1.5125 | 0.5284 |

consistent with

\[
\Delta B\propto\mu^{3/2},
\qquad
|\lambda_f|\propto\mu^{1/2}.
\]

Therefore the Gaussian periodic prefactor blow-up near `r_f` is a nonuniform saddle approximation, **not** a physical divergent DCR.

Do not rank `.214+` by naively adding separate Gaussian periodic and sphaleron contributions through the first-order crossover/fold region.

## 7. Safe-side dark operating points

### `.212` engineering representative

The self-consistent reduced dark root is

\[
\boxed{r_\Gamma(.212)=10.6229699624}.
\]

Certification operating values:

```text
C           = 24.262211 pF
R           = 7.5308506 ohm
fc          = 1.9844267 GHz
T_fold      = 0.2785303 K
Gamma_per   = 9.976990612e-7 /s
Gamma_th    = 2.304378181e-9 /s
Gamma_total = 1.000003439e-6 /s
```

### `.213` exact dark root

\[
\boxed{r_\Gamma(.213)=11.2051409652}.
\]

```text
C = 26.994365 pF
R = 7.1395800 ohm
fc = 1.8741430 GHz
B_per = 39.114084737
Gamma_per = 9.926942995e-7 /s
Gamma_th  = 7.328188266e-9 /s
Gamma_total = 1.000022488e-6 /s
```

with

\[
r_\Gamma/r_f\approx0.9213.
\]

Thus `.213` is about 7.9% below its actual periodic fold. The old `T0/Tx>.94` rejection rule is obsolete.

## 8. Photon capture remains a screening calculation

Current nonlinear capture uses a real Gaussian force with the **symmetrized** quantum-FDT spectrum and a cold harmonic Wigner initial state. It is a truncated-Wigner / semiclassical stress model, not an exact detailed-balance-preserving nonlinear quantum calculation.

Current screen:

```text
lambda = 14 um
rise = 20 ps
post-pulse classification = 2 ns
dt = .125 ps
```

Reduced thermal similarity:

\[
\boxed{
P_{cap}(\lambda,A,\eta_{abs})
=\mathcal P(\eta_{abs}/(A\lambda))
}
\]

so at fixed absorption model

\[
A_p\lambda=\mathrm{constant}.
\]

This is a lumped thermal similarity, **not a broadband optical cutoff law**. The current `adiabatic_photon_temperature()` calibration contains no explicit wavelength-dependent external absorption efficiency.

## 9. High-tilt capture rise and turnover

Coarse fixed-dark screens first showed

```text
delta=.200   A99_point ~420 um^2
delta=.205   ~458
delta=.2075  ~472
delta=.210   ~485
delta=.211   ~485
delta=.212   ~500
delta=.213   ~489
```

where `A99_point` is a central-probability estimate rather than a confidence-qualified boundary.

From `.212` to `.213`, the static photon fold decreases from about `0.27853 K` to `0.27573 K`, which by itself improves the static calorimetric threshold. Simultaneously the dark constraint forces larger capacitance and a slower phase coordinate:

```text
C  ~24.26 -> 26.99 pF
fc ~1.984  -> 1.874 GHz.
```

The observed turnover is therefore interpreted as a finite-pulse write-speed / basin-selection penalty overtaking the lower static threshold.

The reduced-model interior-balance condition is

\[
\boxed{
\frac{d\ln\chi_p}{d\delta}
=-\frac{d}{d\delta}\ln(T_f^2-T_0^2)
}
\]

along the fixed-dark-rate manifold.

## 10. Strict paired fine-tilt comparison: no narrow winner

A strict common-random-number workflow used a common prehistory/FFT grid and identical underlying Gaussian Fourier variates with candidate-specific physical PSD scaling.

Deltas:

```text
.21200, .21225, .21250, .21275, .21300
```

with `N=2048` at `A=490,495,500 um^2`.

No exact paired McNemar comparison was significant. Examples:

```text
A=490: .212 -> .21250, dP=+.001953, paired SE=.001544, p=.344
A=495: .212 -> .21275, dP=+.002441, paired SE=.001891, p=.302
A=500: .21200 and .21300 tied in central P; all pairwise exact p=1
```

Canonical interpretation:

\[
\boxed{
\text{No statistically resolved fine-tilt winner exists over }\delta=.212-.213
}
\]

at the present reduced-model resolution.

The correct result is a **flat reduced-model optimum/Pareto band**. Do not report `.21250` or any other fifth-decimal tilt as a physical optimum.

## 11. High-stat `.212` capture certification — COMPLETE

Workflow:

```text
experiment03-delta212-certification.yml
run 31926948721
N = 8192 per area
```

Results:

| area (`um^2`) | `P_final` | Wilson 95% CI | failures |
|---:|---:|---:|---:|
| 470 | 0.99645996 | [0.99492055, 0.99753399] | 29 |
| 475 | 0.99438477 | [0.99251878, 0.99578731] | 46 |
| 480 | 0.99230957 | [0.99017354, 0.99398410] | 63 |
| 485 | 0.99365234 | [0.99168607, 0.99515586] | 52 |
| 490 | 0.99243164 | [0.99031039, 0.99409128] | 62 |

All five Wilson 95% lower bounds exceed 0.99. Therefore, on the tested grid,

\[
\boxed{A_{99,point}\ge490\ \mu m^2}
\]

and

\[
\boxed{A_{99,95\%\ lower}\ge490\ \mu m^2}.
\]

These are lower bounds on the largest tested passing area, **not** a proof that the exact crossing equals `490 um^2`.

## 12. Engineering representative of the flat band

Use

\[
\boxed{\delta_{rep}=0.212}
\]

as the current engineering representative, not because it has statistically higher capture probability, but because capture is indistinguishable across the plateau while `.212` provides:

- smallest compensated capacitance in the plateau;
- highest phase clock / best temporal margin;
- lower external-flux dark-rate sensitivity;
- greater separation from the high-tilt instanton catastrophe.

This is now a stronger choice than before because the `.212` capture screen has an explicit `N=8192` confidence-qualified certification.

## 13. `.213` exact-root capture correction

The first accepted `.213` capture run used the slightly stale scale

```text
RSC = 11.19986413
```

instead of the later exact total-dark root

```text
r_Gamma = 11.2051409652.
```

The difference is only about `4.71e-4` fractionally in `r`, but exact-frontier comparisons must use the exact dark manifold.

The script was corrected at commit

```text
d3c60d2bb50aa36a153304dee560e80a2f6b7345
```

and exact-root workflow rerun

```text
31972394510
```

was launched. Until that rerun completes, the older `.213` `N=4096` matrix is historical/superseded for exact-frontier purposes.

See `RATE_FRONTIER_PROMOTION_2026-08-16.md` for the historical matrix and provenance.

## 14. `.214` safe-side gate

The `.214` branch-topology result remains important: a finite-amplitude one-negative periodic branch survives through local `r_x` and remains regular until the later first-order/fold structure.

However, simply finding that branch does **not** authorize `.214` as a design point.

A dedicated CI run of `large_branch_one_loop_rate_214.py` found on its first pass:

```text
r=11.450      Gamma_per = 2.079588e-6 /s
r=11.605279   Gamma_per = 1.828000e-6 /s
r=11.707100   Gamma_per = 1.729740e-6 /s
```

with the correct one-negative large branch, still above the `1e-6/s` target. The original script therefore failed because **no root existed before its conservative pre-action-crossing cutoff**.

This failure is now being treated as a scientific negative gate rather than a software defect. Commit

```text
c00f314de141d331e27cd0f89ad524d96523362c
```

extends the regular dominant-branch scan to `0.998 r_c`, performs a high-basis safe-edge check, and passes with an explicit

```text
NO_SAFE_ROOT_BEFORE_ACTION_CROSSOVER
```

classification if the periodic contribution remains above target.

If that gate passes, the conclusion is not that `.214` is impossible in all treatments. It is that **any `.214` target solution necessarily enters the first-order multi-saddle/Stokes/fold-uniform regime**, so `.214` cannot displace the safe `.212` representative without a uniform/thimble-aware rate treatment.

## 15. External-flux robustness favors the lower edge

At fixed fabricated `C,R`, the local logarithmic dark-rate sensitivity increases with tilt:

```text
delta=.2120  d ln Gamma / d delta ~ 943
delta=.2125                        ~ 971
delta=.2130                        ~1011
```

Under the local quasi-static Gaussian approximation, the rms external-flux noise producing a 10% increase in mean DCR is approximately

```text
.2120: 73.7 micro-Phi0
.2125: 71.5 micro-Phi0
.2130: 68.7 micro-Phi0
```

This independently supports `.212` when capture is statistically tied.

## 16. Johnson-noise conclusion after same-environment closure

At the safe frontier `fc~1.9 GHz` and `T0=20 mK`, so

\[
hf_c/(k_BT_0)\approx4.6,
\]

and the local Bose occupation is only of order `10^-2`.

Thus bath fluctuations near the phase frequency are overwhelmingly zero-point rather than thermal. A superconducting storage channel can remove an ordinary transport-resistor Johnson term, but passive damping required for capture/recovery necessarily carries FDT fluctuations.

For any prescribed real trajectory in a passive equilibrium linear bath,

\[
E_{diss}
=\int\frac{d\omega}{2\pi}
\Re Y(\omega)|V(\omega)|^2,
\]

and with the project's symmetrized FDT convention,

\[
\langle W_n^2\rangle_{sym}
=\int\frac{d\omega}{2\pi}
\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT}\right)
\Re Y(\omega)|V(\omega)|^2.
\]

Hence

\[
\boxed{
\langle W_n^2\rangle_{sym}
\ge2k_BT\,E_{diss}
}
\]

for any passive bath and prescribed trajectory.

## 17. Next exact-quantum bridge

The retained two-pole environment has an explicit reaction-coordinate representation. With phase-node flux `q=Phi_bar x` and filter-node flux `psi`,

\[
\boxed{
H_{sys}(t)
=
\frac{Q_q^2}{2C}
+U(q,T_e(t))
+\frac{Q_\psi^2}{2C_f}
+\frac{(q-\psi)^2}{2L_f}.
}
\]

The resistor couples to `psi` as the quantum bath. Eliminating the filter coordinate and bath reproduces the same `Y(omega)` used by the Euclidean problem.

The correct pre-photon quantum state is a **metastable left-well quasistationary state conditioned on no escape**, not the global Gibbs state of the tilted double well.

A phase-DVR basis benchmark remains an active bridge. The first raw ARPACK `which='SA'` attempt was rejected after producing spurious high-energy Ritz values; the repaired route uses shift-invert around the physical low-energy spectrum with explicit residual checks.

## 18. Robust-design boundary

The `.212-.213` fine scan is already much narrower than unresolved physical-model uncertainty. The final design problem should become robust rather than continue refining `delta` numerically:

\[
\boxed{
\max_{\delta,r}\min_{\theta\in\Theta}A_{99}(\delta,r;\theta)
}
\]

subject to

\[
\boxed{
\Gamma_{dark}(\delta,r;\theta)\le\Gamma_\star
\quad\forall\theta\in\Theta.
}
\]

Important uncertainty axes include CPR parameters, induced-gap model, thermal pulse, absorption efficiency, bath parasitics, flux-bias noise, missing dark channels and exact nonlinear quantum capture.

## 19. Immediate recovery queue

1. Read exact-root `.213` capture rerun `31972394510` and promote its replacement matrix.
2. Read the revised `.214` safe-side CI gate triggered by `c00f314...`.
3. If `.214` returns `NO_SAFE_ROOT_BEFORE_ACTION_CROSSOVER`, keep it outside the canonical frontier until a fold-uniform/thimble-aware rate is derived.
4. Finish the repaired shift-invert phase-DVR basis benchmark.
5. Finish the repaired passive dissipation/noise-work trajectory regression.
6. Build a detailed-balance-preserving nonlinear quantum capture benchmark using the exact same reaction-coordinate/bath representation.
7. Restore realistic wavelength-dependent absorption and spatial thermalization before making spectral-reach claims.
8. Stop refining tilt inside `.212-.213` unless robust uncertainty analysis justifies that resolution.

## 20. Claim boundary

**GO for continued theory. NO-GO for manuscript.**

Do not claim:

- exact physical quantum efficiency;
- complete physical dark-count rate;
- a fabrication-level optimum at a fifth-decimal tilt;
- physical broadband LWIR cutoff from the lumped thermal similarity;
- a completed fold-uniform rate for `.214+`;
- novelty of the detector architecture.

The strongest current statement is:

> Within the reduced same-environment model, high directional tilt plus electrical compensation creates a broad optimum near `delta~.212-.213`. Strict paired stochastic tests do not resolve a unique fine-tilt winner. The lower edge `.212` is the engineering representative because it preserves statistically indistinguishable capture while reducing capacitance, increasing phase speed, improving flux-bias robustness and remaining better separated from the high-tilt instanton catastrophe. At that `.212` point, an `N=8192` certification places the Wilson-95%-qualified `A99` frontier at or above `490 um^2` on the tested grid. `.214+` remains a separate first-order/fold-uniform research branch.
