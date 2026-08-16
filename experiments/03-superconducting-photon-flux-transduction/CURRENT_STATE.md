# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**.

## 1. Current physical question

Can one absorbed LWIR photon drive a proximity-Josephson/rf-SQUID phase into a directionally favored metastable basin with high probability, leave a persistent superconducting flux state after recovery, and simultaneously satisfy a very low dark-switch target under **one physically consistent passive environment**?

Current internal description:

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

Generation A uses a small external flux tilt and is **not photovoltaic**. Generation B remains reserved for a later zero-external-flux / intrinsic-directionality mechanism if the theory survives.

## 2. Live canonical force parameters

The current model in `calculations/full_dynamic_rfsquid.py` uses

```text
DELTA_TILT = 0.05
BETA_COLD  = 0.80
LAMBDA_MIX = 0.590
```

and for the favored `rDelta=.6` family

```text
L = 111.5 pH
C = 215 fF
static Tf checkpoint ~= 0.695 K.
```

Any older handoff carrying `DELTA_TILT=.35` or `LAMBDA_MIX=.50` is stale.

Never collapse

```text
Delta_ind -> induced/minigap controlling ABS spectrum, Ic(T), CPR and fold
Delta_s   -> parent-electrode gap controlling hot-carrier escape/confinement.
```

## 3. Current strongest passive capture environment

The leading environment is the passive two-pole network

```text
phase port -- Lf -- node -- (R || Cf) -- ground
```

with

\[
L_f=\frac{\sqrt2R}{\omega_D},
\qquad
C_f=\frac{1}{\sqrt2R\omega_D},
\]

and

\[
\boxed{
\operatorname{Re}Y(\omega)
=\frac{1/R}{1+(\omega/\omega_D)^4}.
}
\]

The principal baseline is

```text
R = 80 ohm
alpha = omega_D/omega_c = .90.
```

The exact deterministic passive-network energy balance is

\[
\boxed{
\frac{d(E/E_L)}{dt}
=U_T\dot T-\frac{L}{R}w^2.
}
\]

The environment suppresses launch less strongly than it damps capture/recovery in the strong-capture regime. Generic selective/frequency-dependent Josephson damping is prior art; only the detector-specific finite-pulse closure remains of interest.

## 4. Capture probabilities are still screening quantities

The current nonlinear Monte Carlo capture workflow uses a real Gaussian force with the **symmetrized** quantum-FDT spectrum. It is a truncated-Wigner / semiclassical stress model.

It does **not** preserve nonsymmetrized quantum detailed balance in a nonlinear metastable system. Therefore

```text
P_final from sym-FDT TWA != exact physical quantum efficiency
zero-photon sym-TWA switching != physical quantum DCR.
```

See `QUANTUM_DETAILED_BALANCE_CORRECTION_2026-08-15.md`.

The cold harmonic Wigner state and causal linear-bath covariance have been independently regression-tested; the unresolved quantum issue is the nonlinear/open-system crossing itself.

## 5. Exact optical/capture similarity of the reduced thermal model

For `Ce=gamma A T`, fixed normalized rise/cooling law, fixed material and fixed circuit/bath,

\[
\boxed{
P_{cap}(\lambda,A,\eta_{abs})
=\mathcal P\!\left(
\frac{\eta_{abs}}{A\lambda}
\right).
}
\]

At fixed absorption efficiency,

\[
\boxed{A_p\lambda=\mathrm{constant}}
\]

for a target screening probability `p`.

Define the thermal headroom

\[
\chi_E
=\frac{T_{ad}^2-T_0^2}{T_f^2-T_0^2}.
\]

Then at fixed geometry

\[
\boxed{
\lambda_p/\lambda_{fold}=1/\chi_p.
}
\]

Thus the static fold wavelength is not the high-fidelity dynamic wavelength.

## 6. Baseline 14-um capture scale before dark-action rescue

At the unscaled `C=215 fF`, `R=80 ohm`, `alpha=.90`, 20-ps-rise point, high-stat sym-FDT/TWA screens place the 14-um `P~.99` area transition near

```text
A ~ 86–87.5 um^2.
```

The statistically defensible current statement is:

```text
A=86 um^2 is supported above P=.99 when independent high-stat runs are combined;
A>=87.5 um^2 is supported below P=.99 in the current screen.
```

By optical similarity, a fixed `A=100 um^2` absorber therefore has a dynamic 99%-screening wavelength of roughly

```text
~12.0–12.3 um,
```

not the static fold-only scale near `20 um`.

## 7. Dimensionless finite-pulse controls

For the current two-pole model define

\[
\boxed{g=\frac1{RC\omega_c}},
\qquad
\boxed{\alpha=\frac{\omega_D}{\omega_c}},
\qquad
\boxed{\rho=\omega_c\tau_{rise}}.
\]

Let `t_c` be first favored-side crossing and `t_r` the cooling-side competing-well reformation. Then

\[
\Delta s_C=\omega_c(t_r-t_c).
\]

The simple cross-then-trap mechanism requires

\[
\boxed{\Delta s_C>0.}
\]

Define stage-conditioned dissipative factors

\[
H_{eff,L}^2=\frac{\int_0^{t_c}w^2dt}{\int_0^{t_c}v^2dt},
\qquad
H_{eff,C}^2=\frac{\int_{t_c}^{t_r}w^2dt}{\int_{t_c}^{t_r}v^2dt},
\]

and capture exposure

\[
\boxed{
\Lambda_C=gH_{eff,C}^2\Delta s_C.
}
\]

Across the current cross-parameter screen, `Lambda_C` is the strongest one-dimensional organizer found so far:

\[
\rho_{Spearman}(\Lambda_C,1-P)\approx-0.85.
\]

But it is not sufficient. A simple rectangular threshold rule in `(chi_E,Lambda_C,Lambda_L)` failed an independent holdout with six false negatives. Do not promote fitted scalar thresholds into a theorem.

## 8. Exact deterministic energetic-lock criterion

Once a separating saddle exists, define the extended-system energy relative to it:

\[
\boxed{
e_s(t)
=\frac12LCv^2+[U(x,T)-U(x_s,T)]
+\frac12\frac{L_f}{L}d^2
+\frac12LC_fw^2.
}
\]

and

\[
\boxed{
\dot e_s
=[U_T(x,T)-U_T(x_s,T)]\dot T
-\frac{L}{R}w^2.
}
\]

`e_s<0` on the favored side is a deterministic trapping certificate.

At the baseline R80 point the mean deterministic trajectory is already deeply trapped at reformation for absorber areas where stochastic capture is degrading; therefore the high-fidelity failure is primarily a **distribution/basin-selection problem**, not failure of the mean trajectory to dissipate enough energy.

## 9. Critical correction: the old cubic MQT estimate is rejected

For the live cold `rDelta=.6` R80 point:

```text
metastable minimum x_m  = -0.6841796
central saddle          = -0.0204310
right minimum           = +0.8173092
zero-energy turning     = +0.3453114
cold fc                 ~= 27.2559 GHz
barrier/kB               ~= 6.9097 K
DeltaU/(hbar omega_c)    ~= 5.2833.
```

The old cubic approximation

\[
B_{cubic}\approx7.2\Delta U/(\hbar\omega_c)
\]

gives

\[
B_{cubic}\approx38.04.
\]

This is **not valid for the actual barrier shape**.

The exact isolated zero-energy bounce gives

\[
\boxed{B_{iso}=25.033050.}
\]

Thus

\[
B_{iso}/B_{cubic}\approx0.658.
\]

The exact shape factor

\[
\beta_U
=\frac{B_{iso}}
       {\Delta U/(\hbar\omega_c)}
\]

is only

\[
\boxed{\beta_U\approx4.74.}
\]

This is one of the most important corrections in Experiment 03.

## 10. Full same-environment nonlocal dissipative bounce

The authoritative zero-temperature dark-action calculation is

```text
calculations/R80_nonlocal_bounce_spectral.py
workflow run 31919134623.
```

It solves the full nonlocal stationary Euclidean equation for the **same passive two-pole environment** used in the capture model.

Convergence:

```text
Nbasis=24 -> B = 29.77046
Nbasis=36 -> B = 29.76566
Nbasis=48 -> B = 29.76564.
```

Final current result:

\[
\boxed{B_{R80}=29.765636.}
\]

The environment adds only

\[
\boxed{\Delta B_{env}\approx4.7283.}
\]

over the exact isolated action.

The converged Hessian has exactly one negative even-parity mode.

Therefore the original `C=215 fF, R=80 ohm` point is **NO-GO as a final dark-stable candidate under the current zero-temperature action model**.

Do not quote a physical DCR yet: the properly normalized fluctuation determinant/prefactor and finite-temperature crossover remain open.

## 11. Prefactor status

A finite-box determinant screen has been run on the same nonlocal bounce. It finds no evidence for the enormous suppressive prefactor that would be needed to rescue `B=29.77`; the raw determinant ratio is instead large.

However the translation zero mode requires a proper collective-coordinate normalization, so the raw `Abar` from that screen is **not yet a physical rate prefactor**.

Robust conclusion only:

```text
no evidence that the prefactor erases the many-action-unit deficit of the unscaled point.
```

## 12. Exact electrical dark-action similarity

At fixed loop inductance, static CPR and normalized two-pole topology, apply

\[
\boxed{
C'=r^2C,
\qquad
R'=R/r,
\qquad
\omega_D'=\omega_D/r.
}
\]

Then

\[
\omega_c'=\omega_c/r,
\qquad
g'=g,
\qquad\alpha'=\alpha,
\]

and the full zero-temperature Euclidean action functional scales exactly:

\[
\boxed{S_E'=rS_E.}
\]

Therefore

\[
\boxed{B'=rB.}
\]

The persistent-current signal is unchanged because `L` is fixed.

With fixed physical rise time,

\[
\rho'=\rho/r,
\]

so

\[
\boxed{B\rho=\text{constant}}
\]

along this pure electrical-rescaling family.

This exposes an exact dark-action / electrical-speed tradeoff.

## 13. Electrical rescue scale and focused capture result

A `10^-6 /s` target with an attempt scale in the broad `10^9–10^11 /s` range corresponds roughly to

\[
34.5\lesssim B_{req}\lesssim39.1
\]

before exact prefactor normalization. Against `B0=29.7656`, pure electrical similarity therefore needs approximately

```text
r ~1.16–1.31.
```

A convenient screening-scale point is

```text
r = 1.263542
C = 343.3 fF
R = 63.3 ohm
fc = 21.57 GHz
B = 37.61
alpha = .90.
```

At this point, keeping the physical graphene thermal pulse unchanged, the focused `N=4096`, `dt=.125 ps` sym-FDT/TWA screen gives at `14 um`:

```text
A=76 um^2 -> P_final = 0.999512
A=78       -> P_final = 0.999268
A=80       -> P_final = 0.998047
A=82       -> P_final = 0.996338
A=84       -> P_final = 0.989502.
```

Thus the electrical dark-action rescue **does not collapse photon capture**.

The point-estimate 99%-screening area moves from roughly `86–87 um^2` before rescue to roughly `83–84 um^2` after rescue. By optical similarity, a fixed `100 um^2` absorber has a current post-rescue dynamic 99%-screening wavelength near

```text
~11.6–11.8 um.
```

This is only a few-percent spectral-reach cost for approximately a 26% increase in the zero-temperature dark action.

Hence the architecture family remains alive.

## 14. Static tilt is an exact dark-action tradeoff

For a linearly tilted potential

\[
V(x;\delta)=V_0(x)-E_L\delta x,
\]

positive tilt toward the favored state simultaneously

- increases the right-well energetic preference;
- lowers the left metastable barrier;
- lowers the exact isolated bounce action;
- and, for any tilt-independent linear passive environment, lowers the stationary dissipative bounce action.

For the dissipative bounce,

\[
\boxed{
\frac{dB_{diss}}{d\delta}
=-\frac{E_L}{\hbar}
\int d\tau\,[x_b(\tau)-x_m]<0
}
\]

for escape toward larger phase.

Therefore static directional tilt and dark-action protection are antagonistic objectives. A passive shunt cannot reverse this sign if its admittance is tilt-independent.

## 15. Barrier-shape rescue is the current competing design lever

The exact dark failure is partly a **shape** failure: the live barrier has `beta_U~4.74`, much thinner than the old cubic surrogate.

The competing rescue route is therefore to change normalized rf-SQUID / CPR topology so the metastable barrier is wider in phase space at acceptable fold and directionality, rather than buying all dark action through capacitance and slower dynamics.

Critical live baseline:

```text
beta_cold = .80
tilt      = .05
```

An earlier exploratory scan around tilt `.2–.4` was based on stale context and is invalid for the live design. The corrected live-neighborhood scan must reproduce `B_iso=25.03305` at `(beta=.80, tilt=.05)` before any shape ranking is accepted.

That corrected scan is the immediate static-design task.

## 16. Open-system quantum requirements still blocking a paper

Even after the exact zero-temperature action advance, a publication-grade detector prediction still requires

1. properly normalized dissipative fluctuation determinant / prefactor;
2. finite-temperature tunneling crossover;
3. a detailed-balance-preserving nonlinear quantum/open-system capture calculation;
4. competing dark channels: quasiparticles, vortices, stray photons, etc.;
5. restoration of wavelength-dependent optical coupling / absorption and spatial thermalization.

No absolute efficiency or dark-count rate is authorized yet.

## 17. Prior-art boundary

No novelty claim is authorized.

Known collisions include superconducting MIR/LWIR SPDs, graphene Josephson photon heating/switching, persistent flux memory, optically written vortices/flux, phase batteries, field-free Josephson directionality, frequency-dependent damping/retrapping, selective dissipation, generic rate-induced tipping, quantum/classical Josephson basin capture, and dissipative MQT.

The possible surviving contribution is increasingly narrow:

```text
single-LWIR-photon calorimetric drive
+ nonadiabatic proximity-JJ basin transfer
+ persistent superconducting flux
+ one passive environment used for capture and dark action
+ exact thermal/electrical similarity closures
+ a simultaneous dark-action / dynamic-spectral-reach bound or Pareto law.
```

## 18. Immediate work queue

1. Finish the **corrected live low-tilt barrier-shape scan** and compare shape rescue against the electrical `r~1.26` benchmark.
2. Finish/normalize the nonlocal bounce fluctuation determinant; do not use the current raw finite-box prefactor as a physical DCR.
3. Map the joint dark-action / 14-um capture Pareto surface around the electrically rescaled family.
4. Replace symmetrized-noise TWA capture with a detailed-balance-preserving nonlinear open-system calculation or a systematically controlled benchmark.
5. Add finite-temperature tunneling crossover and other dark channels.
6. Restore real `eta_abs(lambda)`, antenna/cavity collection, spatial thermalization and area-dependent parasitics.
7. Only after a simultaneous region survives, run the narrow paper/patent collision audit.

## 19. Verdict

\[
\boxed{
\text{original R80/C215 point: dark-action NO-GO}
}
\]

but

\[
\boxed{
\text{electrically rescaled architecture family: still GO for theory}
}
\]

because the exact action can be raised into the desired exponent range while the current harsh capture screen remains high for realistic thermal headroom.

**Manuscript remains NO-GO.**
