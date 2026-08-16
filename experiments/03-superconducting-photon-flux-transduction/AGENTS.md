# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** **NO-GO**. Do not create a manuscript or novelty claim from the current reduced-model results.

> Repository state is authoritative. Fetch `main` before every write. Older scalar-R / cubic-MQT checkpoints are provenance, not the live frontier.

## 1. Recovery order

Read these first, in order:

1. `CURRENT_STATE.md`
2. `FIRST_ORDER_CROSSOVER_CHECKPOINT_2026-08-15.md`
3. `FINITE_T_DARK_CHECKPOINT_2026-08-15.md`
4. `ONE_LOOP_RATE_CHECKPOINT_2026-08-15.md`
5. `CLAIM_LEDGER.md`
6. this file
7. live workflows/scripts listed below.

The current calculation frontier is in `calculations/`; do **not** resume from early short-junction, cubic-MQT, scalar-R, or deterministic-only checkpoints.

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

## 5. Dark-rate machinery now considered validated away from the periodic fold

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
\]

numerical

\[
D_{op}^{num}=7.74565249.
\]

Thus the regular periodic one-loop rate is

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

The current reduced dark target is

\[
\boxed{\Gamma_{dark}=10^{-6}\ \mathrm{s}^{-1}}.
\]

Competing quasiparticle, vortex, stray-photon and technical-noise dark channels are still absent, so this is not a complete physical DCR.

## 6. Critical finite-T topology correction

The old identification

```text
local sphaleron n=1 Matsubara instability == physical quantum/thermal crossover
```

is **REJECTED**.

The high-tilt model exhibits a finite-amplitude first-order periodic-instanton structure.

Three distinct scales must be kept separate:

1. `r_x`: local sphaleron Matsubara instability;
2. `r_c`: periodic/sphaleron action crossing, `B_per=B_sph`;
3. `r_f`: finite-amplitude periodic-instanton fold where a one-negative branch collides with a two-negative companion.

Direct continuation gave approximately:

| delta | r_x | r_c |
|---:|---:|---:|
| .212 | 11.67660 | 12.18208 |
| .213 | 11.64824 | 12.03349 |
| .214 | 11.61108 | 11.88538 |
| .215 | 11.56485 | 11.73736 |

The simple O(2) quartic sphaleron-soft-mode uniformization was explicitly tested and **rejected**: the physical periodic branch retains finite amplitude as `T -> T_x`.

## 7. Periodic fold catastrophe — numerically established

Pseudo-arclength continuation recovers a one-negative periodic branch and a two-negative companion branch meeting at a finite-amplitude fold. The additional even fluctuation eigenvalue changes sign across the turning point.

Fine universal scaling:

### delta=.213

\[
r_f=12.16227131,
\]

\[
\Delta B_{12}\propto\mu^{1.5060},\qquad
|\lambda_f|\propto\mu^{0.4859}.
\]

### delta=.214

\[
r_f=12.0069623,
\]

\[
\Delta B_{12}\propto\mu^{1.5022},\qquad
|\lambda_f|\propto\mu^{0.4840}.
\]

### delta=.215

\[
r_f=11.85159085,
\]

\[
\Delta B_{12}\propto\mu^{1.5125},\qquad
|\lambda_f|\propto\mu^{0.5284}.
\]

with `mu = p_f-p`, `p=r/r_x`.

These are the canonical saddle-node exponents `3/2` and `1/2` to numerical accuracy.

Therefore the large separate Gaussian periodic prefactor near `r_f` is a **nonuniform saddle approximation**, not evidence for a physically divergent DCR.

Do not rank `.214+` using a naive sum of separate Gaussian periodic and thermal saddles. A fold-uniform / thimble-aware treatment is still required there.

## 8. Current safe dark-rate design frontier

The exact reduced dark root at `delta=.213` is now numerically converged:

\[
\boxed{r_\Gamma=11.205140965}.
\]

Physical/electrical values:

```text
C = 26.994365 pF
R = 7.139580 ohm
fc = 1.874143 GHz
B_per = 39.1140847
Gamma_per = 9.926943e-7 /s
Gamma_th  = 7.328188e-9 /s
Gamma_total = 1.0000225e-6 /s
```

72->88 basis change in total rate is only `3.6e-6` of the target.

Most important validity margin:

\[
\boxed{r_\Gamma/r_f=11.20514/12.16227\approx0.9213}.
\]

So the `.213` dark root is about **7.9% below the actual periodic fold**. The misleading diagnostic `T0/Tx~0.962` is no longer a rejection criterion.

## 9. Photon-capture screen and current interior optimum

Capture remains a **symmetrized-FDT truncated-Wigner / semiclassical screen**, not exact nonlinear quantum efficiency.

Current common screen:

```text
lambda = 14 um
rise = 20 ps
post-pulse classification = 2 ns
N = 1024 coarse
 dt = .125 ps
```

Approximate dark-rate-constrained 99% area frontier:

```text
delta=.200   A99 ~420 um^2
delta=.205   A99 ~458 um^2
delta=.2075  A99 ~472 um^2
delta=.210   A99 ~485 um^2
delta=.211   A99 ~485 um^2
delta=.212   A99 ~500 um^2
delta=.213   A99 ~489 um^2
```

Thus **capture turns over between `.212` and `.213` before the dark fold is encountered**.

Active workflow:

```text
experiment03-safe-tilt-optimum.yml
```

is resolving `.21225`, `.21250`, `.21275`; each point first solves its own `Gamma_per+Gamma_th=1e-6/s` dark root and then runs the same 2-ns capture grid.

Do not declare a final Generation-A point until this narrow scan and a high-stat refinement of the winner are complete.

## 10. Reduced optical similarity — interpretation guardrail

For the current lumped `Ce=gamma A T` thermal model,

\[
P_{cap}(\lambda,A,\eta)=\mathcal P(\eta/(A\lambda)),
\qquad A_p\lambda=\mathrm{constant}.
\]

Equivalent wavelength numbers inferred from `A99` are **similarity mappings only**. They are not broadband detector cutoff predictions because realistic wavelength-dependent absorptance, spatial energy deposition, diffusion, proximity physics and optical coupling are not restored.

## 11. Closed / rejected routes

- old cubic MQT exponent as final dark model — **REJECTED**;
- low tilt as dark rescue — **REJECTED by capture**;
- mild beta/barrier shaping in current neighborhood — **REJECTED by fold/capture trade**;
- local `T_x` as physical crossover — **REJECTED**;
- O(2) quartic soft-mode uniformization about the sphaleron — **REJECTED for physical finite-amplitude branch**;
- thermal action `DeltaU/kBT` as an absolute rate ceiling — **REJECTED**; thermal prefactor still scales with inertia;
- Gaussian periodic prefactor blow-up at `r_f` as physical DCR divergence — **REJECTED**;
- naive addition of all stationary saddles through a first-order/fold transition as final rate — **NOT JUSTIFIED / DO NOT USE**.

## 12. Immediate work queue

1. Finish `experiment03-safe-tilt-optimum.yml`.
2. Take the best `.212-.213` point and run a focused high-stat `N>=4096` capture screen at the exact dark root.
3. Update `CURRENT_STATE.md`, `CLAIM_LEDGER.md` and the first-order checkpoint with the final safe-side optimum.
4. Keep `.214+` as a separate upside branch. If pursuing it, derive a thimble-aware fold/Airy uniform rate or perform a model-specific center-manifold integration; do not use the divergent Gaussian determinant.
5. After the reduced design is stable, attack the larger unresolved physics: detailed-balance-preserving nonlinear open-system quantum capture, spatial thermalization, realistic optical absorptance, and competing dark channels.
6. Only after those survive should novelty/patent audit become manuscript-relevant.

## 13. Stop / reformulate conditions

Stop or reformulate if robust work shows any of:

- no nonempty capture/dark operating set survives exact/open-system quantum evolution;
- realistic spatial thermal transport destroys the lumped calorimetric advantage;
- competing dark channels dominate the periodic/thermal phase-escape floor;
- realistic optical absorption/energy delivery removes the inferred LWIR margin;
- reset/readout destroys the operating distinction;
- narrow prior art already contains the same detector-specific closure.

A negative theorem/bound is a valid result.

**Current verdict: GO for continued theory. NO-GO for manuscript.**
