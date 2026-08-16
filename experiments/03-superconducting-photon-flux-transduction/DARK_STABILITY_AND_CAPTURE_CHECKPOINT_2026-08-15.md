# Experiment 03 — Dark stability and capture-rescue checkpoint — 2026-08-15

## Status

**Major canonical checkpoint.**

- Architecture-level theory: **GO for continued falsification / optimization.**
- Original electrical point `rDelta=.6, C=215 fF, R=80 ohm, alpha=.90`: **NO-GO as a final dark-stable candidate under the current zero-temperature action model.**
- Electrically rescaled and/or barrier-shaped descendants: **still alive.**
- Manuscript: **NO-GO.**

This file supersedes any earlier inference that the `C=215 fF` R80 candidate was near the `10^-6 /s` dark target merely because the cubic-barrier MQT surrogate gave a favorable number.

## 1. Live canonical force parameters

The current force model in `calculations/full_dynamic_rfsquid.py` uses

```text
DELTA_TILT = 0.05
BETA_COLD  = 0.80
LAMBDA_MIX = 0.590
```

and, for `rDelta=.6`,

```text
L = 111.5 pH
C = 215 fF
static Tf checkpoint ~= 0.695 K.
```

Older handoff text carrying `DELTA_TILT=.35` or `LAMBDA_MIX=.50` is stale. Recent exact bounce results below were computed with the **live** parameters above.

## 2. Strong capture environment retained for screening

The current strongest passive environment is the two-pole network

```text
phase port -- Lf -- node -- (R || Cf) -- ground
```

with

\[
L_f=\frac{\sqrt2 R}{\omega_D},
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

The principal screening point is

```text
R = 80 ohm
alpha = omega_D/omega_c = .90.
```

Its deterministic energy identity is exact:

\[
\frac{d(E/E_L)}{dt}
=U_T\dot T-\frac{L}{R}w^2.
\]

The environment allocates relatively little resistor loss before first favored-side crossing and most loss during post-cross capture/recovery in the strong-capture regime.

## 3. Capture probabilities remain screening quantities

Current nonlinear Monte Carlo capture calculations use a real Gaussian force with the **symmetrized** quantum-FDT spectrum. This is a useful truncated-Wigner / semiclassical stress but does not preserve nonsymmetrized quantum detailed balance in a nonlinear metastable system.

Therefore

```text
P_final from sym-FDT TWA != exact physical quantum efficiency
zero-photon sym-TWA switching != physical quantum DCR.
```

See

```text
QUANTUM_DETAILED_BALANCE_CORRECTION_2026-08-15.md
```

for the canonical warning.

## 4. Current 14-um capture scale at the unscaled R80 point

At fixed `R=80 ohm`, `alpha=.90`, 20-ps rise, the reduced model has the exact optical similarity

\[
P_{cap}(\lambda,A,\eta)
=\mathcal P\!\left(\frac{\eta}{A\lambda}\right).
\]

High-stat sym-TWA screens place the 14-um `P~.99` transition near

```text
A ~ 86–87.5 um^2
```

with `A=86 um^2` supported above `.99` when independent high-stat runs are combined, while `A>=87.5 um^2` is supported below `.99` in the current screen.

This maps to a fixed `A=100 um^2` dynamic 99%-screening wavelength around

```text
~12.0–12.3 um
```

for constant absorption efficiency, substantially shorter than the static fold-only scale near `20 um`.

The dynamic spectral derating identity is

\[
\boxed{
\lambda_p/\lambda_{fold}=1/\chi_p.
}
\]

## 5. Old cubic dark inference is rejected

At the live cold R80 point,

```text
cold metastable x_m = -0.6841796
central saddle       = -0.0204310
right minimum        = +0.8173092
zero-energy turning  = +0.3453114
cold fc              ~= 27.2559 GHz
barrier/kB            ~= 6.9097 K
DeltaU/(hbar omega_c) ~= 5.2833.
```

The old cubic-barrier approximation used

\[
B_{cubic}\approx7.2\frac{\Delta U}{\hbar\omega_c}
\]

and gave

\[
B_{cubic}\approx38.04.
\]

That approximation is badly wrong for the actual barrier shape.

## 6. Exact isolated bounce

`calculations/R80_dissipative_bounce_screen.py` evaluates the actual non-sinusoidal cold potential two independent ways.

The exact isolated zero-energy bounce action is

\[
\boxed{B_{iso}=25.033050.}
\]

The time-domain Euclidean integration and independent 1D quadrature agree at essentially machine/numerical precision.

Thus

\[
\boxed{
B_{iso}/B_{cubic}\approx0.658.
}
\]

The current barrier is much thinner in Euclidean phase space than the cubic surrogate implied.

Define the shape factor

\[
\beta_U
=\frac{B_{iso}}
       {\Delta U/(\hbar\omega_c)}.
\]

Current value:

\[
\boxed{\beta_U\approx4.74}
\]

rather than `7.2`.

## 7. Same-environment dissipative bounce

The first-order and restricted variational screens showed that the selected two-pole environment increases the action by only several units:

```text
isolated-path environmental correction ~4.20
width-only restricted saddle            ~29.18
width+amplitude restricted saddle        ~30.06.
```

The decisive calculation is

```text
calculations/R80_nonlocal_bounce_spectral.py
workflow run 31919134623
```

which solves the full nonlocal stationary Euclidean equation in a converged spectral basis using the **same two-pole admittance**.

Convergence ladder:

```text
Nbasis=24: Benv ~29.77046
Nbasis=36: Benv ~29.76566
Nbasis=48: Benv ~29.76564.
```

Final current value:

\[
\boxed{B_{R80}=29.765636.}
\]

The environment adds

\[
\boxed{\Delta B_{env}\approx4.7283.}
\]

The spectral Hessian has exactly one negative even-parity mode, as required for the metastable bounce.

This is the current authoritative **zero-temperature exponent** of the reduced R80 electrical model.

## 8. Baseline dark verdict

A `10^-6 /s` target with an attempt scale anywhere around `10^9–10^11 /s` corresponds roughly to an exponent scale

\[
34.5\lesssim B_{req}\lesssim39.1
\]

before detailed prefactor normalization.

Therefore `B=29.77` is not plausibly a `10^-6 /s`-class design unless the prefactor provides an unexpectedly enormous suppressive factor.

A finite-box determinant screen has found **no evidence for such an exponential prefactor suppression**. Its raw determinant factor is in the opposite direction, but the absolute rate normalization is not yet trusted because the translation zero mode requires a proper collective-coordinate treatment.

Hence:

\[
\boxed{
\text{the original }C=215\,\mathrm{fF},R=80\,\Omega
\text{ point fails the current dark-action target provisionally.}
}
\]

Do not quote a physical DCR yet.

## 9. Exact electrical dark-action similarity

At fixed loop inductance, static CPR and normalized passive two-pole topology, apply

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
\alpha'=\alpha,
\qquad
g'=g,
\]

and the **full zero-temperature Euclidean action functional** scales as

\[
\boxed{S_E'=rS_E.}
\]

Therefore the exact dissipative bounce obeys

\[
\boxed{B'=rB.}
\]

Persistent current separation is unchanged because `L` is unchanged.

The cost is electrical speed:

\[
\boxed{\omega_c'=\omega_c/r.}
\]

With fixed physical photon-rise time

\[
\rho=\omega_c\tau_{rise},
\]

we therefore have the exact invariant

\[
\boxed{B\rho=\mathrm{constant}}
\]

along the electrical similarity family.

See

```text
ELECTRICAL_DARK_ACTION_SIMILARITY_2026-08-15.md
DARK_ACTION_SPEED_INVARIANT_2026-08-15.md
```

## 10. Size of the electrical rescue

Using the converged baseline action `B0=29.765636`, reaching a plausible `B_req~34.5–39.1` requires only approximately

```text
r ~1.16–1.31
```

at the exponent level.

Using the crude same-dimensionless-prefactor screen

\[
(f_{c0}/r)e^{-rB_0}=10^{-6}/s
\]

gives

```text
r ~1.264
C ~343 fF
R ~63.3 ohm
fc ~21.6 GHz
```

as an order-of-magnitude rescue scale, **not a final device point**.

## 11. Capture survival under electrical rescue

The coarse workflow

```text
calculations/electrical_dark_rescue_capture.py
```

keeps the physical graphene thermal pulse unchanged while applying the electrical similarity.

Representative sym-TWA screens:

```text
r=1.00:
  A=80 um^2 -> P~.999
  A=86.5    -> P~.994

r=1.15:
  A=80      -> P~.997
  A=86.5    -> P~.983

r=1.288:
  A=80      -> P~.995
  A=86.5    -> P~.969

r=1.45:
  A=80      -> P~.995
  A=86.5    -> P~.954.
```

Thus dark-action rescaling does **not** automatically destroy photon capture. It reduces the allowed thermal/absorber-area margin.

A focused high-stat run near `r=1.263542` is in progress and should be used as the next capture-rescue checkpoint.

## 12. Static tilt tradeoff

For a linearly tilted cold phase potential

\[
V(x;\delta)=V_0(x)-E_L\delta x,
\]

increasing positive tilt simultaneously

- increases energetic preference for the favored right well;
- lowers the metastable barrier;
- lowers the exact isolated bounce action;
- and, for any tilt-independent linear passive environment, lowers the stationary dissipative bounce action as well.

The dissipative result is

\[
\boxed{
\frac{dB_{diss}}{d\delta}
=-\frac{E_L}{\hbar}
\int d\tau\,[x_b(\tau)-x_m]<0
}
\]

for a bounce toward larger phase.

Therefore static tilt directionality and dark-action protection are antagonistic control objectives. A passive shunt cannot reverse that sign if its admittance is tilt-independent.

See

```text
TILT_DIRECTIONALITY_DARK_ACTION_LEMMA_2026-08-15.md
```

## 13. Barrier-shape rescue is open

The dark failure is not solely a barrier-height problem; the current exact shape factor is only `beta_U~4.74`.

A second rescue route is therefore to alter normalized rf-SQUID/CPR topology so the metastable barrier is wider in phase space at acceptable fold and directionality.

Important synchronization:

```text
live baseline beta_cold=.80
live baseline tilt=.05
```

An earlier exploratory scan around tilt `.2–.4` was based on stale context and is not applicable to the live design. The corrected barrier-shape scan must reproduce `B_iso=25.03305` at `(beta=.80, tilt=.05)` before any ranking is accepted.

## 14. Open-system quantum status

The zero-temperature bounce exponent is now much stronger than the old cubic surrogate, but a publication-grade dark prediction still requires

1. properly normalized fluctuation determinant / prefactor;
2. finite-temperature crossover;
3. consistency with the same passive environment used for capture;
4. competing dark channels: quasiparticles, vortices, stray photons, etc.

Likewise, the current sym-FDT TWA capture screen must ultimately be replaced or benchmarked by a detailed-balance-preserving nonlinear open-system calculation.

## 15. Current decision tree

### If focused electrical rescue retains high capture

Continue with a joint Pareto surface

```text
zero-T dark action B
vs
sym-TWA capture screen
vs
absorber thermal drive / spectral reach.
```

Then normalize the dark prefactor and replace sym-TWA with a controlled quantum/open-system capture model.

### If barrier shaping raises B materially at comparable fold/directionality

Test whether that route buys more dark action per unit loss of capture/spectral margin than capacitance scaling.

### If neither rescue produces a simultaneous region

The current external-tilt Generation-A architecture should be rejected rather than pushed toward a manuscript.

## 16. Verdict

\[
\boxed{
\text{baseline R80/C215 point: dark-stability NO-GO provisionally}
}
\]

but

\[
\boxed{
\text{architecture family: still GO for continued theory}
}
\]

because an exact electrical-rescaling route exists and coarse capture tests show a surviving region with substantial thermal headroom.

**Manuscript remains NO-GO.**
