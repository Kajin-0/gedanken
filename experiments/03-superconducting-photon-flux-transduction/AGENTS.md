# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** **NO-GO**. Do not create a manuscript or novelty claim from the current reduced-model results.

> Repository state is authoritative. Fetch `main` before every write. Older scalar-R, cubic-MQT, local-`T_x`, and stale handoff checkpoints are provenance, not the live frontier.

## 1. Recovery order

Read these first, in order:

1. `CURRENT_STATE.md`
2. `RATE_FRONTIER_PROMOTION_2026-08-16.md`
3. `FIRST_ORDER_CROSSOVER_CHECKPOINT_2026-08-15.md`
4. `FINITE_T_DARK_CHECKPOINT_2026-08-15.md`
5. `ONE_LOOP_RATE_CHECKPOINT_2026-08-15.md`
6. `CLAIM_LEDGER.md`
7. this file
8. live workflows/scripts listed below.

For the active frontier, also inspect:

```text
calculations/delta212_capture_certification.py
calculations/delta213_exact_dark_root.py
calculations/one_loop_rate_capture_213.py
calculations/large_branch_one_loop_rate_214.py
.github/workflows/experiment03-delta212-certification.yml
.github/workflows/experiment03-one-loop-213-capture.yml
.github/workflows/experiment03-delta214-large-branch-rate.yml
```

Do **not** resume from early short-junction, cubic-MQT, scalar-R, deterministic-only, or `T0/Tx>.94` rejection checkpoints.

## 2. Current physical question

Can one absorbed LWIR photon drive a proximity-Josephson/rf-SQUID phase coordinate into a directionally favored metastable basin with high probability, leave a persistent superconducting flux state after recovery, and simultaneously satisfy a very low dark-switch target under the **same causal passive environment**?

Current internal description:

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

Generation A uses external flux tilt and is **not photovoltaic**.

## 3. Live reduced model

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

Passive environment:

```text
phase port -- Lf -- node -- (R || Cf) -- ground
```

with

\[
\operatorname{Re}Y(\omega)=\frac{1/R}{1+(\omega/\omega_D)^4}.
\]

The same environment is used in real-time capture, Euclidean escape, and fluctuation determinants.

## 4. Exact electrical similarity — canonical

At fixed static potential / loop inductance / normalized bath topology,

\[
C'=r^2C,\qquad R'=R/r,\qquad \omega_D'=\omega_D/r,
\]

so

\[
\omega_c'=\omega_c/r.
\]

Zero temperature:

\[
\boxed{B'=rB}.
\]

Finite temperature:

\[
\boxed{B(T;r)=rB_0(rT)}.
\]

For the regular periodic-instanton one-loop prefactor away from a bifurcation,

\[
\boxed{A_{1\ell}(T;r)=r^{-1/2}A_{1\ell,0}(rT)}.
\]

The local sphaleron Matsubara-instability scale obeys

\[
T_\times(r)=T_{\times,0}/r,
\]

but **local `T_x` is not the physical first-order crossover and is not the Gaussian-validity boundary** in the high-tilt regime.

## 5. Dark-rate machinery validated away from the periodic fold

Finite-T periodic Euclidean saddle:

- exact two-pole nonlocal kernel;
- constant + cosine Matsubara basis;
- physical decay branch has exactly one negative even mode;
- odd translation zero mode overlap is numerically unity.

Determinant:

- full even/odd Hessian anatomy;
- analytic UV curvature-tail correction;
- residual basis sensitivity in `log D` at the few-`1e-6` level in hard cases.

Absolute normalization was independently calibrated against the canonical cubic metastable problem:

\[
D_{op}^{exact}=\sqrt{60}=7.74596669,
\qquad
D_{op}^{num}=7.74565249.
\]

Thus

\[
\boxed{\Gamma_{per}=A_{1\ell}e^{-B_{per}}},
\qquad
\boxed{A_{1\ell}=\omega_c\sqrt{\frac{I_s}{2\pi}}D_{raw,corr}}.
\]

Independent same-environment thermal memory-friction screen:

\[
\boxed{\Gamma_{th}=\frac{\omega_m}{2\pi}\frac{\lambda_b}{\omega_b}e^{-\Delta U/(k_BT_0)}},
\]

where

\[
C\lambda_b^2+\lambda_bY_L(\lambda_b)+F_s/L=0.
\]

The reduced dark target is

\[
\boxed{\Gamma_{dark}=10^{-6}\ \mathrm{s}^{-1}}.
\]

Competing quasiparticle, vortex, stray-photon, cosmic/environmental and technical-noise dark channels remain absent, so this is not a complete physical DCR.

## 6. Critical finite-T topology correction

The old identification

```text
local sphaleron n=1 Matsubara instability == physical quantum/thermal crossover
```

is **REJECTED**.

The high-tilt model exhibits a finite-amplitude first-order periodic-instanton structure with three distinct scales:

1. `r_x`: local sphaleron Matsubara instability;
2. `r_c`: periodic/sphaleron action crossing, `B_per=B_sph`;
3. `r_f`: finite-amplitude periodic-instanton fold where a one-negative branch collides with a two-negative companion.

Current values:

| delta | r_x | r_c | r_f |
|---:|---:|---:|---:|
| .212 | 11.67660 | 12.18208 | not needed for safe representative |
| .213 | 11.64824 | 12.03349 | 12.16227131 |
| .214 | 11.61108 | 11.88538 | 12.0069623 |
| .215 | 11.56485 | 11.73736 | 11.85159085 |

The simple O(2) quartic sphaleron-soft-mode uniformization was explicitly tested and **rejected**: the physical periodic branch retains finite amplitude through local `T_x`.

## 7. Periodic fold catastrophe — established

Pseudo-arclength continuation recovers a one-negative periodic branch and a two-negative companion branch meeting at a finite-amplitude fold. The additional even fluctuation eigenvalue changes sign across the turning point.

Fine scaling:

```text
delta=.213: DeltaB exponent 1.5060, |lambda_f| exponent .4859
delta=.214: DeltaB exponent 1.5022, |lambda_f| exponent .4840
delta=.215: DeltaB exponent 1.5125, |lambda_f| exponent .5284
```

with `mu=p_f-p`, consistent with the saddle-node laws

\[
\Delta B\propto\mu^{3/2},\qquad |\lambda_f|\propto\mu^{1/2}.
\]

Therefore the separate Gaussian periodic prefactor blow-up near `r_f` is a **nonuniform saddle approximation**, not a physical divergent DCR.

Do not rank `.214+` by naively summing separate Gaussian periodic and thermal/sphaleron saddles through the first-order/fold region.

## 8. Canonical safe reduced design: `.212` plateau representative

Strict common-random-number paired tests over

```text
.21200, .21225, .21250, .21275, .21300
```

at `A=490,495,500 um^2`, `N=2048`, found no statistically resolved fine-tilt winner. The correct result is a **flat optimum/Pareto band**, not a fifth-decimal optimum.

Use

\[
\boxed{\delta_{rep}=0.212}
\]

as the engineering representative because capture is statistically tied while `.212` has lower compensated capacitance, higher phase clock, lower local flux-bias DCR sensitivity, and greater distance from the high-tilt catastrophe.

Exact `.212` dark operating point used for certification:

```text
r_Gamma     = 10.6229699624
C           = 24.262211 pF
R           = 7.5308506 ohm
fc          = 1.9844267 GHz
T_fold      = 0.2785303 K
Gamma_per   = 9.976990612e-7 /s
Gamma_th    = 2.304378181e-9 /s
Gamma_total = 1.000003439e-6 /s
```

## 9. `.212` high-stat certification — COMPLETE

Workflow:

```text
experiment03-delta212-certification.yml
run 31926948721
N = 8192 per area
```

| area (`um^2`) | `P_final` | Wilson 95% CI |
|---:|---:|---:|
| 470 | 0.99645996 | [0.99492055, 0.99753399] |
| 475 | 0.99438477 | [0.99251878, 0.99578731] |
| 480 | 0.99230957 | [0.99017354, 0.99398410] |
| 485 | 0.99365234 | [0.99168607, 0.99515586] |
| 490 | 0.99243164 | [0.99031039, 0.99409128] |

All five Wilson lower bounds exceed `.99`. On the tested grid:

\[
\boxed{A_{99,point}\ge490\ \mu m^2},
\qquad
\boxed{A_{99,95\%lower}\ge490\ \mu m^2}.
\]

These are tested-grid lower bounds, **not** an exact `A99=490 um^2` crossing.

## 10. `.213` status and exact-root correction

The converged total-dark root is

\[
\boxed{r_\Gamma(.213)=11.2051409652}.
\]

```text
C = 26.994365 pF
R = 7.139580 ohm
fc = 1.874143 GHz
B_per = 39.1140847
Gamma_per = 9.926943e-7 /s
Gamma_th  = 7.328188e-9 /s
Gamma_total = 1.0000225e-6 /s
r_Gamma/r_f ~= .9213
```

The first `.213` capture script accidentally retained an older `RSC=11.19986413`. That historical `N=4096` matrix is therefore superseded for exact-frontier comparisons even though the fractional `r` error is only about `4.71e-4`.

The script was corrected at

```text
d3c60d2bb50aa36a153304dee560e80a2f6b7345
```

and exact-root rerun

```text
31972394510
```

must be read before promoting a canonical `.213` capture table.

## 11. `.214` high-tilt gate

`.214` is not excluded because the finite-amplitude branch disappears at local `T_x`; that old reasoning is obsolete. It is excluded from the **safe canonical frontier** because its dark target is now being tested on the actual dominant large branch.

The first CI scan showed

```text
r=11.450      Gamma_per = 2.079588e-6 /s
r=11.605279   Gamma_per = 1.828000e-6 /s
r=11.707100   Gamma_per = 1.729740e-6 /s
```

with one negative mode and exact translation-zero overlap. An extended scan to `0.998 r_c` then showed a shallow interior rate minimum around `r~11.79`, followed by a rise toward the first-order region as the determinant softens; the coarse minimum remained about `1.70e-6/s`.

`calculations/large_branch_one_loop_rate_214.py` now performs a bounded minimization of this regular pre-crossover rate and re-evaluates the minimum at high basis/grid resolution.

Interpretation gate:

```text
if verified min Gamma_per > 1e-6/s before r_c:
    NO_SAFE_ROOT_BEFORE_ACTION_CROSSOVER
    .214 remains outside canonical frontier
    any putative .214 target requires first-order/thimble/fold-uniform treatment
```

Do not force a formal `.214` root through the multi-saddle region merely to extend the design frontier.

## 12. Photon-capture interpretation guardrail

Capture remains a **symmetrized-FDT truncated-Wigner / semiclassical screen**, not exact nonlinear quantum efficiency.

Current common screen:

```text
lambda = 14 um
rise = 20 ps
post-pulse classification = 2 ns
dt = .125 ps
```

For the current lumped `Ce=gamma A T` thermal model,

\[
P_{cap}(\lambda,A,\eta)=\mathcal P(\eta/(A\lambda)),
\qquad A_p\lambda=\mathrm{constant}.
\]

Equivalent wavelength numbers inferred from `A99` are similarity mappings only. They are not broadband detector cutoff predictions because realistic wavelength-dependent absorptance, spatial energy deposition, diffusion, proximity physics and optical coupling are not restored.

## 13. External-flux robustness

At fixed fabricated `C,R`:

```text
delta=.2120  d ln Gamma / d delta ~ 943
delta=.2125                        ~ 971
delta=.2130                        ~1011
```

Approximate rms external-flux noise producing a 10% increase in mean DCR under the local quasi-static Gaussian approximation:

```text
.2120: 73.7 micro-Phi0
.2125: 71.5 micro-Phi0
.2130: 68.7 micro-Phi0
```

This supports the lower edge when capture is statistically tied.

## 14. Passive damping / noise boundary

At the safe frontier `fc~1.9 GHz`, `T0=20 mK`, so `hf_c/(k_B T0)~4.6` and the local Bose occupation is of order `1e-2`.

For any prescribed real trajectory in a passive equilibrium linear bath,

\[
E_{diss}=\int\frac{d\omega}{2\pi}\Re Y(\omega)|V(\omega)|^2,
\]

and with the project's symmetrized FDT convention,

\[
\langle W_n^2\rangle_{sym}
=\int\frac{d\omega}{2\pi}\hbar|\omega|\coth\!\left(\frac{\hbar|\omega|}{2k_BT}\right)
\Re Y(\omega)|V(\omega)|^2,
\]

hence

\[
\boxed{\langle W_n^2\rangle_{sym}\ge2k_BT\,E_{diss}}.
\]

Passive capture damping is never fluctuation-free.

## 15. Next exact-quantum bridge

The retained two-pole environment has the reaction-coordinate representation

\[
H_{sys}(t)
=
\frac{Q_q^2}{2C}
+U(q,T_e(t))
+\frac{Q_\psi^2}{2C_f}
+\frac{(q-\psi)^2}{2L_f}.
\]

The resistor couples to `psi` as the quantum bath; eliminating filter+bath reproduces the same `Y(omega)` used by the Euclidean problem.

The correct pre-photon quantum state is a metastable left-well quasistationary state conditioned on no escape, not the global Gibbs state of the tilted double well.

The phase-DVR benchmark must use the repaired shift-invert low-energy solver with explicit residual checks; the original raw ARPACK `which='SA'` route produced spurious high-energy Ritz values and is rejected.

## 16. Robust-design boundary

The fine tilt band is already narrower than unresolved model uncertainty. Future optimization should be robust:

\[
\boxed{\max_{\delta,r}\min_{\theta\in\Theta}A_{99}(\delta,r;\theta)}
\]

subject to

\[
\boxed{\Gamma_{dark}(\delta,r;\theta)\le\Gamma_\star\quad\forall\theta\in\Theta}.
\]

Important uncertainty axes include CPR parameters, induced-gap model, thermal pulse, absorption efficiency, bath parasitics, flux-bias noise, missing dark channels and exact nonlinear quantum capture.

## 17. Immediate work queue

1. Read exact-root `.213` rerun `31972394510`; replace the historical capture matrix if completed.
2. Read the latest `.214` bounded-minimum CI run triggered by the current `large_branch_one_loop_rate_214.py`.
3. If `.214` confirms `min Gamma_per > 1e-6/s` before `r_c`, freeze the safe high-tilt boundary at `<.214` until a thimble/fold-uniform rate treatment exists.
4. Finish the repaired shift-invert phase-DVR basis benchmark.
5. Finish the repaired passive dissipation/noise-work trajectory regression.
6. Build the detailed-balance-preserving nonlinear quantum capture benchmark with the exact same reaction-coordinate/bath representation.
7. Restore realistic wavelength-dependent absorption and spatial thermalization before spectral-reach claims.
8. Do not spend additional compute resolving fifth-decimal tilt inside `.212-.213` unless uncertainty propagation later makes it meaningful.

## 18. Stop / reformulate conditions

Stop or reformulate if robust work shows any of:

- no nonempty capture/dark operating set survives exact/open-system quantum evolution;
- realistic spatial thermal transport destroys the lumped calorimetric advantage;
- competing dark channels dominate the periodic/thermal phase-escape floor;
- realistic optical absorption/energy delivery removes the inferred LWIR margin;
- reset/readout destroys the operating distinction;
- narrow prior art already contains the same detector-specific closure.

A negative theorem/bound is a valid result.

**Current verdict: GO for continued theory. NO-GO for manuscript.**
