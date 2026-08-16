# Experiment 03 — Barrier-shape rescue checkpoint — 2026-08-15

## Status

**Canonical design checkpoint.**

This note compares static barrier shaping against the already-validated pure electrical dark-action rescue. It records completed results only; calculations still running at checkpoint time are labeled explicitly and must not be inferred.

## 1. Benchmark to beat: pure electrical rescue

The converged baseline same-environment zero-temperature action is

\[
B_{R80}=29.765636.
\]

The exact electrical similarity

\[
C\to r^2C,
\qquad
R\to R/r,
\qquad
\omega_D\to\omega_D/r
\]

gives

\[
B\to rB
\]

at fixed static CPR potential and normalized two-pole topology.

The focused rescue point

```text
r = 1.263542
C = 343.3 fF
R = 63.3 ohm
fc = 21.57 GHz
B = 37.61
alpha = .90
```

retains, under the current symmetrized-FDT TWA capture screen at 14 um / 20 ps,

```text
A=76 um^2 -> P=0.999512
A=78       -> P=0.999268
A=80       -> P=0.998047
A=82       -> P=0.996338
A=84       -> P=0.989502.
```

Thus its point-estimate `P~.99` absorber area is roughly `83–84 um^2`, mapping by the exact reduced optical similarity to a fixed `100 um^2` wavelength near `11.6–11.8 um` for constant absorption efficiency.

This is the current rescue benchmark.

## 2. Correct live static barrier scan

Live baseline:

```text
beta_cold = .80
delta_tilt = .05
lambda_mix = .590.
```

The corrected exact isolated-action scan around this point gives, at fixed `delta=.05`:

| beta_cold | B_iso | fold T (K) | cold fc (GHz) |
|---:|---:|---:|---:|
| .80 | 25.033 | ~.694 | ~27.26 |
| .85 | 31.044 | ~.769 | ~28.14 |
| .90 | 37.628 | ~.846 | ~29.01 |
| .95 | 45.243 | ~.93 | larger |

Thus increasing `beta_cold` is a very strong dark-action lever **without slowing the cold phase clock**.

However it raises the thermal fold strongly, so its cost appears on the photon-energy/spectral axis instead.

## 3. Pure beta=.90 shape rescue — rejected as preferred spectral solution

Completed workflow:

```text
experiment03-beta090-capture.yml
run 31919761936
```

Parameters:

```text
beta_cold=.90
delta=.05
C=215 fF
R=80 ohm
alpha=.90
lambda=14 um
rise=20 ps
N=2048
dt=.125 ps.
```

Symmetrized-FDT TWA screen:

```text
A=45 um^2 -> P_final = 1.000000
A=50       -> P_final = 0.998535
A=55       -> P_final = 0.964844
A=60       -> P_final = 0.790527
A=65       -> P_final = 0.630859
A=70       -> P_final = 0.500000
A=75       -> P_final = 0.342773
A=80       -> P_final = 0.232422.
```

Therefore the `P~.99` area is only slightly above `50 um^2`, implying by exact reduced-model optical similarity a fixed-`100 um^2` dynamic screening wavelength of only order

```text
~7 um.
```

Conclusion:

\[
\boxed{
\text{pure }\beta=.90\text{ shape rescue is spectrally dominated by the electrical }r\sim1.26\text{ rescue.}
}
\]

This remains a screening conclusion because the capture model is sym-TWA, but the penalty is so large that `.90` is not the preferred current design direction.

## 4. Pure beta=.85 shape rescue — also spectrally inferior

Completed workflow:

```text
experiment03-beta085-capture.yml
run 31919781220
```

Same environment / 14-um / 20-ps conditions, with `beta=.85`:

```text
A=55 um^2 -> P_final = 1.000000
A=60       -> P_final = 1.000000
A=65       -> P_final = 0.997070
A=70       -> P_final = 0.981934
A=75       -> P_final = 0.924316
A=80       -> P_final = 0.825684
A=85       -> P_final = 0.715820.
```

Thus its `P~.99` area is roughly mid/high 60s, mapping to only roughly

```text
~9–9.5 um
```

for a fixed `100 um^2` absorber at constant absorption efficiency.

Conclusion:

\[
\boxed{
\text{pure }\beta=.85\text{ is also worse than the pure electrical rescue on spectral reach.}
}
\]

A mild `beta=.85 + small electrical r` hybrid can only become competitive if the same-environment dissipative action is already extremely favorable; this is being evaluated separately.

## 5. More promising static lever: reduce directional tilt

The exact tilt/action monotonicity lemma proves that reducing positive linear tilt increases dark action while reducing right-well energetic directionality.

At fixed live `beta=.80`, the corrected static scan gives approximately:

```text
delta=.050:
  B_iso = 25.033
  fold  ~= .694 K
  right-well bias ~= 5.48 K

delta=.035:
  B_iso = 28.963
  fold  ~= .703 K
  right-well bias ~= 3.84 K.
```

Thus lowering tilt from `.050` to `.035` buys approximately

\[
\boxed{\Delta B_{iso}\approx+3.93}
\]

with almost no static thermal-fold penalty.

This is qualitatively more attractive than increasing `beta_cold`, because the principal price is **reduced directional bias**, not a ~20% increase in fold temperature.

The decisive question is therefore dynamic:

```text
Does delta=.035 preserve sufficiently one-sided photon capture under the causal two-pole environment?
```

## 6. Running at checkpoint time — not results

The following workflows were launched but had not completed when this checkpoint was written:

### Low-tilt capture

```text
experiment03-tilt035-capture.yml
run 31919985143
```

Tests `beta=.80, delta=.035`, R80/alpha=.90, 14 um, 20 ps over absorber area.

### Low-tilt same-environment nonlocal bounce

```text
experiment03-low-tilt-nonlocal-bounce.yml
run 31920022267
```

Continues the full nonlocal stationary bounce from `delta=.050 -> .035`.

### Beta-shaped nonlocal continuation

```text
experiment03-beta-shape-continuation.yml
run 31919928779
```

Continues the stationary nonlocal bounce from `beta=.80 -> .90` without relying on the failed strict-tail seed.

Do **not** infer their outcomes from this note. Read the workflow logs first.

## 7. Current design ranking before low-tilt completion

1. **Leading:** pure electrical rescue near `r~1.26`.
   - exact action gain;
   - modest spectral-screening cost;
   - known speed penalty `B rho = const`.

2. **Potential challenger:** reduced tilt `.035` + smaller electrical scaling.
   - ~4 isolated action units at almost unchanged fold;
   - unknown capture-directionality cost until workflow completes.

3. **Secondary:** beta=.85 + small electrical scaling.
   - substantial action gain;
   - already significant thermal/spectral penalty.

4. **Not preferred:** pure beta=.90 or stronger shaping.
   - excellent static action;
   - severe 14-um capture penalty from raised fold.

## 8. Next decision

Once the two low-tilt workflows finish:

1. obtain `B_diss(delta=.035)` under the same two-pole environment;
2. determine its 14-um `A_99` screening scale;
3. compute the additional electrical scale
   \[
   r_{extra}=B_{target}/B_{diss}(\delta=.035)
   \]
   only if needed;
4. test that low-tilt + scaled hybrid directly;
5. compare its fixed-`100 um^2` dynamic wavelength with the current `~11.6–11.8 um` electrical-only benchmark.

If low tilt cannot preserve one-sided capture, retain the pure electrical rescue as the leading Generation-A point.

**Manuscript remains NO-GO.**
