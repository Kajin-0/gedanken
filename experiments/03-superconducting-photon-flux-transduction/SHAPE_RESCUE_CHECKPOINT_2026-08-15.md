# Experiment 03 — Barrier-shape rescue checkpoint — 2026-08-15

## Status

**Canonical design checkpoint.**

This note compares static barrier/tilt shaping with the validated pure electrical dark-action rescue. The low-tilt branch and the beta-shaped nonlocal continuation are now complete. A final mild-shape hybrid (`beta=.825`) is under direct capture test.

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

at fixed static CPR potential and normalized two-pole topology gives

\[
B\to rB.
\]

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

This remains the rescue benchmark to beat.

## 2. Live canonical static point

```text
beta_cold = .80
delta_tilt = .05
lambda_mix = .590
L = 111.5 pH
C = 215 fF
R = 80 ohm
alpha = .90.
```

The baseline full same-environment nonlocal bounce is

\[
\boxed{B_{diss}=29.765636}.
\]

## 3. Full beta-shaped nonlocal continuation

Completed workflow:

```text
experiment03-beta-shape-continuation.yml
run 31919933142
```

At fixed `delta=.05`, `C=215 fF`, `R=80 ohm`, `alpha=.90`:

| beta_cold | fc (GHz) | B_iso | B_diss | Delta B_env |
|---:|---:|---:|---:|---:|
| .800 | 27.25590 | 25.03730 | 29.76564 | 4.72833 |
| .825 | 27.57047 | 27.99285 | 33.33606 | 5.34321 |
| .850 | 27.88630 | 31.11872 | 37.11688 | 5.99816 |
| .875 | 28.20352 | 34.41155 | 41.10423 | 6.69268 |
| .900 | 28.52219 | 37.86749 | 45.29345 | 7.42596 |

Every continued bounce converged with exactly one negative even-parity mode.

Thus beta shaping raises both the isolated barrier action and the environmental action correction. The effect is real and monotonic over this interval.

## 4. Pure beta=.90 and beta=.85 shape rescue — spectrally dominated

The completed 14-um / 20-ps sym-FDT TWA screens show that the dark-action gain from increasing `beta_cold` is paid for by a much larger thermal-fold/photon-energy requirement.

### beta=.90

Completed workflow:

```text
experiment03-beta090-capture.yml
run 31919761936
```

Representative screen:

```text
A=45 um^2 -> P_final ~1
A=50       -> P_final ~0.999
A=55       -> P_final ~0.965
A=60       -> P_final ~0.79
```

The `P~.99` area is only slightly above `50 um^2`, equivalent by the exact reduced optical similarity to only order `7 um` for a fixed `100 um^2` absorber.

### beta=.85

Completed workflow:

```text
experiment03-beta085-capture.yml
run 31919781220
```

Representative screen:

```text
A=60 um^2 -> P_final ~0.999–1
A=65       -> P_final ~0.997–0.999
A=70       -> P_final ~0.983
A=75       -> P_final ~0.93
A=80       -> P_final ~0.82
```

The `P~.99` area is only in the mid/high 60s, equivalent to roughly `9–9.5 um` for fixed `100 um^2`.

Therefore

\[
\boxed{
\text{pure strong beta shaping is spectrally dominated by the electrical rescue.}
}
\]

## 5. Low-tilt dark action — exact gain

The exact tilt/action theorem states that reducing positive directional tilt increases the dark tunneling action while reducing right-well directionality.

Completed same-environment continuation:

```text
experiment03-low-tilt-nonlocal-bounce.yml
run 31919989692
```

| delta | fold T (K) | fc (GHz) | B_iso | B_diss |
|---:|---:|---:|---:|---:|
| .050 | .694406 | 27.25590 | 25.03730 | 29.76564 |
| .045 | .709856 | 27.36238 | 26.09567 | 31.19443 |
| .040 | .725776 | 27.46666 | 27.20108 | 32.72262 |
| .035 | .742289 | 27.56885 | 28.35935 | 34.37138 |

All stationary bounces converged with one negative mode.

Thus `.050 -> .035` buys

\[
\Delta B_{diss}\approx+4.61.
\]

Note the corrected live continuation: the fold at `.035` is about `.742 K`, not the earlier exploratory `~.703 K` estimate.

## 6. Low tilt — dynamically rejected

Completed capture workflow:

```text
experiment03-tilt035-capture.yml
run 31919974010
```

Parameters:

```text
beta=.80
delta=.035
R=80 ohm
alpha=.90
C=215 fF
lambda=14 um
rise=20 ps
N=2048
dt=.125 ps.
```

The loss of directional bias strongly degrades the favored-basin probability:

```text
A=75 um^2 -> P_final = 0.971680
A=80       -> P_final = 0.921875
A=84       -> P_final = 0.840332
A=86       -> P_final = 0.797363
A=88       -> P_final = 0.745605
A=90       -> P_final = 0.698730
A=95       -> P_final = 0.569824.
```

Therefore

\[
\boxed{
\text{the low-tilt rescue is rejected as a preferred high-fidelity solution.}
}
\]

The dark-action gain is real, but it is purchased with exactly the directional basin margin required for one-sided photon latching.

This is an important falsification of the earlier hypothesis that tilt reduction might be a nearly free dark-stability lever.

## 7. Last plausible static/electrical hybrid: beta=.825

The mild point

```text
beta=.825
delta=.05
```

has the converged same-environment action

\[
\boxed{B_{diss}=33.3360645}.
\]

To reach the same screening action scale as the pure electrical benchmark (`B_target~37.61`), it would require only

\[
\boxed{
r_{extra}\approx\frac{37.61}{33.336}\approx1.128,
}
\]

rather than `r=1.2635` from the beta=.80 baseline.

This is the only remaining shape/electrical hybrid that can plausibly beat the current benchmark. Its unscaled 14-um capture curve is being tested in

```text
experiment03-beta0825-capture.yml
run 31921234930.
```

Do not infer the result before reading that workflow log.

## 8. Current design ranking

1. **Validated benchmark:** beta=.80, delta=.05 + pure electrical scale `r~1.26`.
2. **Final challenger under test:** beta=.825, delta=.05 + smaller electrical scale `r~1.13` if its unscaled capture margin remains sufficient.
3. **Rejected as preferred:** low tilt `.035` — dark action improves, but directional capture collapses.
4. **Rejected as preferred:** beta=.85/.90 pure shape — dark action improves, but thermal/spectral reach collapses.

## 9. Next decision

1. read the completed beta=.825 unscaled capture screen;
2. if its area margin remains competitive, apply `r~1.128` with the exact electrical-similarity rescaling while keeping the physical graphene pulse unchanged;
3. compare the resulting 14-um `A_99` directly with the `83–84 um^2` pure-electrical benchmark;
4. if the hybrid does not beat that benchmark, close static-shape/tilt rescue and retain pure electrical scaling as the Generation-A design point.

**Publication status remains NO-GO.** The nonlinear detailed-balance-preserving quantum capture problem, properly normalized tunneling prefactor/finite-T crossover, competing dark channels, and optical/material realism remain unresolved.
