# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15 late-session / strict-paired checkpoint  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**

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

## 4. Dark-rate calculation now used for safe-side designs

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
\]

\[
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

when the regular periodic saddle is safely away from its fold.

This is **not** a complete physical DCR: quasiparticle, vortex, stray-photon and technical-noise channels remain absent.

## 5. Critical finite-T topology: `r_x != r_c != r_f`

The former identification of the sphaleron's first Matsubara instability with the physical quantum/thermal crossover is rejected.

Three distinct scales exist at high tilt:

1. `r_x`: local sphaleron first-Matsubara instability;
2. `r_c`: finite-amplitude periodic/sphaleron action crossing;
3. `r_f`: finite-amplitude periodic-instanton saddle-node/fold.

Representative action-crossing results:

| delta | r_x | r_c |
|---:|---:|---:|
| .212 | 11.67660 | 12.18208 |
| .213 | 11.64824 | 12.03349 |
| .214 | 11.61108 | 11.88538 |
| .215 | 11.56485 | 11.73736 |

The simple continuous O(2) quartic sphaleron-soft-mode model was explicitly tested and **rejected**: the physical periodic branch remains finite-amplitude through local `T_x`.

## 6. Periodic fold catastrophe is established numerically

Pseudo-arclength continuation passes through the finite-amplitude periodic fold and recovers a two-negative companion branch. The additional even Hessian mode crosses zero while the odd translation zero mode remains distinct.

Fine fold scaling with

\[
\mu=p_f-p,
\qquad p=r/r_x,
\]

gives:

| delta | r_f | `Delta B` exponent | soft-eigenvalue exponent |
|---:|---:|---:|---:|
| .213 | 12.16227131 | 1.5060 | 0.4859 |
| .214 | 12.0069623 | 1.5022 | 0.4840 |
| .215 | 11.85159085 | 1.5125 | 0.5284 |

consistent with the canonical saddle-node laws

\[
\Delta B\propto\mu^{3/2},
\qquad
|\lambda_f|\propto\mu^{1/2}.
\]

Therefore the Gaussian periodic prefactor blow-up near `r_f` is a nonuniform saddle approximation, **not** a physical divergent DCR.

The absolute fold-uniform/thimble-aware rate for `.214+` remains unresolved. Do not rank `.214+` by naively summing separate Gaussian stationary-saddle contributions.

## 7. Exact safe-side `.213` dark root

The `.213` target lies safely before its actual periodic fold:

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
r_f(.213)=12.16227131,
\qquad
r_\Gamma/r_f\approx0.9213.
\]

Thus the `.213` operating root is about 7.9% below the actual determinant catastrophe. The older `T0/Tx>.94` rejection rule is obsolete.

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

This is a lumped thermal similarity, **not a broadband optical cutoff law**.

The current `adiabatic_photon_temperature()` calibration contains no explicit wavelength-dependent external absorption efficiency. Treat wavelength mappings as conditional on absorbed energy until realistic optics are restored.

## 9. High-tilt capture rise, turnover and physical interpretation

Coarse dark-rate-constrained screens first showed

```text
delta=.200   A99_point ~420 um^2
delta=.205   ~458
delta=.2075  ~472
delta=.210   ~485
delta=.211   ~485
delta=.212   ~500
delta=.213   ~489
```

where `A99_point` denotes a central-probability estimate, not a confidence-qualified boundary.

From `.212` to `.213`, the static photon fold decreases from about `0.27853 K` to `0.27573 K`, which by itself improves the static calorimetric threshold. Simultaneously the dark constraint forces larger capacitance and a slower phase coordinate:

```text
C  ~24.26 -> 26.99 pF
fc ~1.984  -> 1.874 GHz.
```

The cold harmonic phase cloud also narrows slightly, so the observed turnover is not caused by broader initial zero-point fluctuations. It is a **finite-pulse write-speed / basin-selection penalty** overtaking the lower static threshold.

The exact reduced-model interior-balance condition is

\[
\boxed{
\frac{d\ln\chi_p}{d\delta}
=-\frac{d}{d\delta}\ln(T_f^2-T_0^2)
}
\]

along the fixed-dark-rate manifold, where `chi_p` is the dynamical headroom above the static fold.

## 10. Strict paired fine-tilt comparison: NO narrow winner

Independent-seed coarse screens gave unstable sub-`1e-3` tilt rankings. A strict common-random-number workflow therefore used:

- one common prehistory equal to the slowest candidate's `12 tau_cold`;
- one common FFT grid;
- identical underlying Gaussian Fourier variates;
- candidate-specific physical PSD scaling;
- per-trajectory final basin labels;
- `N=2048` at `A=490,495,500 um^2`;
- exact paired discordant counts / McNemar tests.

Deltas:

```text
.21200, .21225, .21250, .21275, .21300
```

### A=490 um^2

Marginal P ranged only `.98828-.99023`. No paired comparison was significant. Example `.212 -> .21250`:

```text
dP = +.001953
paired SE = .001544
McNemar p = .344.
```

### A=495 um^2

Marginal P ranged `.98975-.99219`. The nominal best was `.21275`, but versus `.212`:

```text
dP = +.002441
paired SE = .001891
McNemar p = .302.
```

No paired comparison was significant.

### A=500 um^2

Marginal P ranged `.98877-.98926`. `.21200` and `.21300` were exactly tied in central P. Every paired exact McNemar test returned `p=1`.

### Canonical interpretation

\[
\boxed{
\text{No statistically resolved fine-tilt winner exists over }\delta=.212-.213
}
\]

at the present reduced-model resolution.

Therefore do **not** report `.21250` or any other fifth-decimal tilt as a physical optimum. The correct result is a **flat reduced-model optimum/Pareto band**.

## 11. Engineering representative of the flat band

Use

\[
\boxed{\delta_{rep}=0.212}
\]

as the current engineering representative, not because it has a statistically higher capture probability, but because its capture is statistically indistinguishable from the rest of the plateau while it has favorable secondary margins:

- smallest compensated capacitance in the plateau;
- highest phase clock / best temporal margin;
- lower external-flux dark-rate sensitivity;
- farther from the high-tilt instanton catastrophe than larger tilts.

The self-consistent `.212` reduced dark root used by the strict paired workflow is

\[
\boxed{r_\Gamma(.212)\approx10.622969962},
\]

with approximately

```text
C = 24.262211 pF
fc = 1.9844267 GHz
Tf = 0.2785303 K.
```

A high-stat single-design certification workflow is active:

```text
experiment03-delta212-certification.yml
```

at `A=470,475,480,485,490 um^2`, `N=8192` each.

Its purpose is to report separately:

```text
A99_point
A99_95lower
```

rather than use the coarse central-probability crossing as a confidence-qualified detector boundary.

## 12. External-flux robustness favors the lower edge

At fixed fabricated `C,R`, the local logarithmic dark-rate sensitivity increases with tilt:

```text
delta=.2120  d ln Gamma / d delta ~ 943
delta=.2125                        ~ 971
delta=.2130                        ~1011.
```

Under the local quasi-static Gaussian approximation, the rms external-flux noise producing a 10% increase in mean DCR is approximately

```text
.2120: 73.7 micro-Phi0
.2125: 71.5 micro-Phi0
.2130: 68.7 micro-Phi0.
```

This is a fixed-design robustness diagnostic, not a full technical flux-noise model. It independently supports `.212` as the engineering representative when capture is statistically tied.

## 13. Johnson-noise conclusion after same-environment closure

At the safe frontier `fc~1.9 GHz` and `T0=20 mK`, so

\[
hf_c/(k_BT_0)\approx4.6,
\]

and the local Bose occupation is only of order `10^-2`.

Thus the bath fluctuations at the phase frequency are overwhelmingly zero-point rather than thermal. A superconducting signal/storage channel can remove one ordinary transport-resistor Johnson term, but the passive damping required to make the latch capture/recover necessarily brings FDT fluctuations.

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

for any passive bath and prescribed trajectory. Passive capture damping is therefore never fluctuation-free.

## 14. Next exact-quantum bridge

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

A phase-DVR basis benchmark is in progress. The first raw ARPACK `which='SA'` attempt was rejected after producing spurious high-energy Ritz values; the solver has been repaired to shift-invert around the physical low-energy spectrum with explicit residual checks.

## 15. Robust-design boundary

The `.212-.213` fine scan is already much narrower than the unresolved physical-model uncertainty. The final design problem should therefore become robust rather than continue refining `delta` numerically:

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

Important uncertainty axes include CPR parameters, induced-gap model, thermal pulse, absorption efficiency, bath parasitics, flux bias noise, missing dark channels and exact nonlinear quantum capture.

## 16. Immediate recovery queue

1. Finish `experiment03-delta212-certification.yml`; report `A99_point` and `A99_95lower` separately.
2. Finish the repaired shift-invert phase-DVR basis benchmark.
3. Finish the repaired passive dissipation/noise-work trajectory regression.
4. Update `AGENTS.md` / claim ledger with the high-stat `.212` certification.
5. Stop refining tilt inside `.212-.213` unless a later uncertainty analysis justifies it.
6. Build the detailed-balance-preserving nonlinear quantum capture benchmark using the exact same reaction-coordinate/bath representation.
7. Restore realistic wavelength-dependent absorption and spatial thermalization before making spectral-reach claims.
8. Keep `.214+` as a separate fold-uniform-rate research branch; do not let it contaminate the safe representative.

## 17. Claim boundary

**GO for continued theory. NO-GO for manuscript.**

Do not claim:

- exact physical quantum efficiency;
- complete physical dark-count rate;
- a fabrication-level optimum at a fifth-decimal tilt;
- physical broadband LWIR cutoff from the lumped thermal similarity;
- a completed fold-uniform rate for `.214+`;
- novelty of the detector architecture.

The strongest current statement is:

> Within the reduced same-environment model, high directional tilt plus electrical compensation creates a broad optimum near `delta~.212-.213`. Strict paired stochastic tests do not resolve a unique fine-tilt winner. The lower edge `.212` is therefore the current engineering representative because it preserves statistically indistinguishable capture while reducing capacitance, increasing phase speed, improving flux-bias robustness and remaining well separated from the high-tilt periodic-instanton catastrophe.
