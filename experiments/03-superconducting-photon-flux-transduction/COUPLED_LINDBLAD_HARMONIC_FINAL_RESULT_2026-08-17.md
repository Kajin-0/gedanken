# Experiment 03 — final Padé-coordinate coupled-Lindblad harmonic result

Date: 2026-08-17

This result is governed by the thresholds and stopping rule frozen in
`COUPLED_LINDBLAD_HARMONIC_ACCEPTANCE_2026-08-17.md` before the p12/p16
calculation.

## Provenance

Initial p24/p32 workflow `32033862008` computed all physical states but hit a
post-calculation reporting bug (`relSDP` vs stored key `relsdp`).  No scientific
quantity failed.

The reporting key was corrected without changing any physics or numerical
parameter.  The authoritative rerun is:

```text
workflow: .github/workflows/experiment03-coupled-lindblad-harmonic-p24-p32-final.yml
run:      32034030825
job:      95400156358
commit:   a22db101396f215719f25a4d9b75b3a197da7d86
```

Automatic classification:

```text
FINAL_COUPLED_GAUSSIAN_ACCEPTANCE mandatory=1 monotone_state=1 monotone_bath=1 finalpass=0
COUPLED_LINDBLAD_HARMONIC_FINAL_FAIL
PADE_COORDINATE_COUPLED_ROUTE_CLOSED_IF_NO_IMPLEMENTATION_FAILURE
```

## Final convergence matrix

```text
order   rel SDP bath correction   max FDT width error   half nuclear discrepancy
p16     4.371732397355e-4          1.097140548818e-4    1.080427038299e-4
p24     1.899327249574e-4          4.525611639949e-5    4.454012325572e-5
p32     1.232976270974e-4          3.734642419739e-5    3.691041348888e-5
```

All three states remain physical and numerically controlled:

```text
order   drift max Re(lambda)   min full symplectic nu   normalized q-p covariance
p16    -6.0354978e-2           0.5                       1.31e-14
p24    -6.0349058e-2           0.5                       1.62e-14
p32    -6.0347883e-2           0.5                       4.93e-14
```

The p24 and p32 implementation checks also remain at numerical precision:
BCF real-drift identity ~1e-12, auxiliary-vacuum fixed-point residual ~1e-17,
Lyapunov residual ~3e-15, and isolated system-frequency error ~1.8e-11.

## Why the route fails

The final acceptance thresholds were inherited unchanged from harmonic Gate B:

```text
max relative FDT width error       < 1e-6
half nuclear-norm discrepancy      < 5e-6
```

At p32:

```text
max width error       = 3.734642419739e-5
half nuclear          = 3.691041348888e-5
```

Thus p32 misses the width requirement by a factor of ~37.3 and the full-state
requirement by a factor of ~7.38.

The failure is **not** instability, positivity loss, quadrature convention,
Lyapunov error, or nonconvergence of the state direction.  The route remains
monotone, but the frozen stopping rule does not permit further Padé-order
extrapolation after p32.

## Scientific conclusion

The coupled-Lindblad realization itself is validated as a physical and highly
controlled representation strategy.  What is rejected is the specific
**Padé-pole-coordinate quasi-Lindblad input representation** as the active
route to the required independent harmonic accuracy under the predeclared
resource/stopping rule.

Do not run p36/p40/p48 or other post-hoc Padé orders.

## Next authorized method

Move to the already predeclared fallback:

**direct positive-real / coupled-Lindblad realization fitted to the exact
physical direct-port spectrum or exact BCF**, rather than physicalizing the
fixed Padé pole set.

The useful machinery that should be retained is:

- published coupled-Lindblad SDP physicalization;
- exact real-quadrature Gaussian system benchmark;
- exact FDT/full-state harmonic oracle;
- unchanged final Gate-B state thresholds.

Only the rational pole/coordinate representation should change.

No nonlinear detector calculation is authorized until a new representation
passes the same harmonic state gate.

## Gate status

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / direct exact-spectrum coupled realization next
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
