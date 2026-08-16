# Experiment 03 — Constant-dark-action high-tilt checkpoint — 2026-08-15

## Status

**Canonical frontier checkpoint.** The previous pure-electrical rescue at `delta=.05` is no longer the leading screening design. The dominant optimization is now a higher-directional-tilt family with exact electrical compensation chosen to hold the same zero-temperature nonlocal dark action.

This remains a **screening/model result**, not a detector prediction. Capture probabilities are symmetrized-FDT TWA values; equal Euclidean action is not equal physical finite-temperature dark-count rate.

## 1. Constraint manifold

At each nominal directional tilt `delta`, first solve the full same-environment nonlocal Euclidean bounce at the base electrical point and obtain

\[
B_0(\delta).
\]

Then choose

\[
\boxed{r(\delta)=B_\star/B_0(\delta)},
\qquad B_\star=37.61,
\]

and apply the exact electrical similarity

\[
\boxed{
C\to r^2C,
\qquad
R\to R/r,
\qquad
\omega_D\to\omega_D/r.
}
\]

At fixed static CPR potential this gives

\[
B\to rB,
\qquad
\omega_c\to\omega_c/r,
\qquad
g=1/(RC\omega_c)\ \text{fixed},
\qquad
\alpha=\omega_D/\omega_c\ \text{fixed}.
\]

The optimization variable is therefore

\[
\boxed{A_{99}(\delta\mid B=B_\star)}
\]

with the compensated phase clock carried as an explicit speed cost.

## 2. Why higher tilt can help even though it hurts dark action

Increasing positive directional tilt has three competing effects:

1. lowers the thermal fold/trigger scale;
2. increases energetic preference for the favored basin;
3. lowers the unscaled dark tunneling action.

Electrical compensation restores item 3 by increasing phase inertia. This creates a controlled trade:

```text
higher tilt -> easier photon trigger + stronger directionality
larger C    -> restored dark action + slower phase response + narrower absolute cold Wigner cloud.
```

The previous statement “tilt and dark stability are antagonistic” remains true at fixed electrical parameters. The new point is that the lost action can be bought back with a distinct control variable.

## 3. Baseline and closed alternatives

Baseline same-environment action at

```text
beta=.80
delta=.05
C=215 fF
R=80 ohm
alpha=.90
```

is

\[
B_0=29.765636.
\]

Pure electrical compensation to `B=37.61` required

```text
r=1.26354
C=343.3 fF
R=63.3 ohm
fc=21.57 GHz
```

and produced a 14-um / 20-ps `P~.99` area of only about

```text
83–84 um^2
```

or roughly `11.6–11.8 um` for a fixed `100 um^2` absorber under the exact reduced optical similarity.

Two alternative static rescues are now closed:

- reducing tilt: raises action but destroys one-sided capture probability;
- increasing `beta_cold`: raises action but raises the photon fold too strongly.

The mild `beta=.825` + equal-action electrical hybrid is also dominated: its equal-action `A99` is only about `75–76 um^2`.

## 4. Exact higher-tilt nonlocal action continuation

Same-environment stationary bounce, base `C=215 fF`, `R=80 ohm`, `alpha=.90`:

| delta | fold T [K] | base fc [GHz] | B_diss | r to B=37.61 |
|---:|---:|---:|---:|---:|
| .050 | .694406 | 27.25590 | 29.765636 | 1.26354 |
| .060 | .665053 | 27.03601 | 27.142968 | 1.38563 |
| .070 | .637062 | 26.80605 | 24.774233 | 1.51811 |
| .080 | .609988 | 26.56498 | 22.611277 | 1.66333 |
| .085 | .596885 | 26.43991 | 21.594791 | 1.74162 |
| .090 | .583909 | 26.31159 | 20.616687 | 1.82425 |
| .100 | .558422 | 26.04440 | 18.765038 | 2.00426 |
| .110 | .533437 | 25.76175 | 17.039591 | 2.20721 |
| .120 | .508869 | 25.46161 | 15.427536 | 2.43785 |
| .130 | .484519 | 25.14149 | 13.917470 | 2.70236 |
| .140 | .460293 | 24.79837 | 12.499033 | 3.00903 |
| .150 | .436111 | 24.42855 | 11.163322 | 3.36907 |
| .160 | .411853 | 24.02728 | 9.903160 | 3.79778 |
| .180 | .362588 | 23.10375 | 7.588472 | 4.95620 |
| .200 | .311068 | 21.94790 | 5.520634 | 6.81262 |
| .220 | .255673 | 20.39210 | 3.658774 | 10.2794 |
| .240 | .192147 | 17.96272 | 1.909888 | 19.6923 |
| .250 | .153560 | 15.88069 | 1.017045 | 36.9797 |

The spectral bounce retains exactly one negative even mode through `.25` in the sparse continuation. At `.26` the current stationary solver returns two negative modes / poor stationarity, so `.26` is not an accepted bounce result.

Independent cold topology scan finds the static double well still exists at `.26` but is gone by `.27`.

## 5. Equal-action capture frontier completed through delta=.14

All values below use:

```text
lambda = 14 um
rise = 20 ps
B_target = 37.61
alpha = .90
N = 2048 per point
dt = .125 ps
symmetrized-FDT TWA screening.
```

Approximate `P~.99` thresholds:

| delta | compensated fc [GHz] | A99 [um^2] | fixed-100 equivalent lambda [um] |
|---:|---:|---:|---:|
| .050 | 21.57 | 83–84 | 11.6–11.8 |
| .055 | 20.51 | ~88 | ~12.3 |
| .060 | 19.51 | ~92 | ~12.9 |
| .065 | 18.56 | ~97 | ~13.6 |
| .070 | 17.66 | ~103–104 | ~14.5 |
| .075 | 16.80 | ~105–106 | ~14.8 |
| .080 | 15.97 | ~113–114 | ~15.9 |
| .085 | 15.18 | ~118–119 | ~16.6 |
| .090 | 14.42 | ~126 | ~17.6 |
| .100 | 12.99 | ~139–140 | ~19.5 |
| .110 | 11.67 | ~152–153 | ~21.3 |
| .120 | 10.44 | ~167 | ~23.4 |
| .130 | 9.30 | high-180s | ~26.4 |
| .140 | 8.24 | ~210 | ~29.4 |

Representative `.14` points:

```text
A=178 -> P=1.000000
A=190 -> P=1.000000
A=202 -> P=0.998047
A=214 -> P=0.986328
A=226 -> P=0.944824.
```

Thus the equal-action high-tilt family has already improved the reduced-model fixed-100 spectral screening scale from roughly `11.7 um` to roughly `29 um` before the turnover is located.

Do **not** interpret that as a physical detector cutoff. It uses constant absorption efficiency and the lumped thermal similarity well beyond the wavelength range where detailed optics/material assumptions have been restored.

## 6. Most of the gain is static-fold reduction

Define

\[
Q_{99}=A_{99}(T_f^2-T_0^2).
\]

Because the lumped photon-energy density scales as `1/A` at fixed wavelength, `Q99` removes the trivial static-fold factor and is proportional to inverse dynamic headroom.

Approximate values rise only from

```text
Q99 ~40.2 at delta=.05
```

to

```text
Q99 ~44.4 at delta=.14.
```

Therefore most of the large `A99` gain is the engineered reduction of the static fold energy; stronger directionality mainly prevents the slower compensated phase coordinate from losing too much dynamic margin.

## 7. Critical-slowing asymptotic

Let

\[
\epsilon=\delta_c-\delta\to0^+.
\]

For the generic saddle-node normal form,

\[
\Delta U\propto\epsilon^{3/2},
\qquad
\omega_{c,0}\propto\epsilon^{1/4},
\qquad
B_0\propto\epsilon^{5/4}.
\]

Holding `B=B_star` by electrical similarity therefore requires

\[
r\propto\epsilon^{-5/4},
\qquad
C\propto\epsilon^{-5/2},
\]

and the compensated phase clock obeys

\[
\boxed{\omega_{c,\star}\propto\epsilon^{3/2}}.
\]

Hence finite-time response must eventually fail even if the static trigger energy keeps falling.

Detailed derivation: `CONSTANT_ACTION_TILT_ASYMPTOTIC_2026-08-15.md`.

## 8. Quantum localization under compensation

For the low-temperature harmonic cold state,

\[
\sigma_x^2=\frac{\hbar}{2C\bar\Phi^2\omega_c}.
\]

Under electrical scaling,

\[
\boxed{\sigma_x^2\to\sigma_x^2/r},
\qquad
\boxed{\sigma_x\to\sigma_x/\sqrt r}.
\]

Thus compensation narrows the **absolute** cold Wigner cloud while slowing the phase clock. Near the saddle-node both the compensated width and the minimum-saddle distance scale as `epsilon^(1/2)`, so relative localization does not improve parametrically without bound.

## 9. Finite-temperature dark caveat

Equal zero-temperature Euclidean action is not equal physical finite-temperature dark rate.

The static barrier falls with increasing tilt. Through `.085` the actual barrier at `T0=20 mK` still satisfies `DeltaU/(kBT0)>265`, so ordinary thermal activation is irrelevant there. Farther toward the cold fold this will cease to be true.

An extended thermal diagnostic through `.22` is running to identify when a crude GHz-attempt Arrhenius screen approaches the provisional `10^-6 /s` target. This is only a falsification diagnostic, not a Kramers-rate calculation.

## 10. Active turnover probe

Workflow:

```text
experiment03-high-tilt-sparse-turnover.yml
run 31922308116
```

Tests equal-action capture at

```text
delta=.15  -> compensated fc ~7.25 GHz
delta=.16  -> ~6.33 GHz
delta=.18  -> ~4.66 GHz
```

with area grids chosen around the static-fold projection.

At checkpoint time these jobs were still running. Do not infer their result from this file.

## 11. Current design interpretation

The architecture should now be viewed as a Pareto surface in

\[
(\text{zero-T dark action},\ \text{photon/spectral reach},\ \text{electrical speed},\ \text{basin probability},\ \text{finite-T dark stability}).
\]

The former pure-electrical `delta=.05` point is no longer the leading spectral design at fixed zero-T action.

The next accepted design point must satisfy both:

1. the numerical finite-time turnover / speed constraint;
2. a finite-temperature dark-stability check, not zero-T action alone.

## 12. Blockers unchanged

No physical efficiency, cutoff wavelength or dark-count rate is authorized yet. Remaining blockers include:

- detailed-balance-preserving nonlinear open-quantum capture;
- normalized nonlocal tunneling prefactor and finite-T dissipative crossover;
- flux-noise sensitivity under external tilt;
- quasiparticle, vortex and stray-photon dark channels;
- wavelength-dependent optical absorptance/coupling;
- spatial nonequilibrium thermalization;
- readout/reset loading;
- narrow prior-art/patent collision audit.

**Verdict: GO for continued theory; NO-GO for manuscript.**
