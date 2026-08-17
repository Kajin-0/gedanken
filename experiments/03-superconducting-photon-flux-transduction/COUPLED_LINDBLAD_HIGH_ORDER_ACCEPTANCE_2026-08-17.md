# Experiment 03 — coupled-Lindblad high-order acceptance rule

Date: 2026-08-17

## Purpose

This file freezes the acceptance criteria for extending the physical coupled-Lindblad Padé correction from p8 to p12/p16 **before** those higher-order results are computed.

No system dynamics are authorized by this file.  This is a bath-level Gate C.1 recovery test only.

## Controlling p4/p5/p8 result

Corrected-normalization workflow run `32007957189`, job `95321261710` established:

```text
order   rel SDP correction   max rel exact C(t) error   C(0) rel error   min coupled spectrum
p4      6.912307e-3          9.056088e-3                9.056088e-3     +5.351e-9
p5      4.496342e-3          5.849317e-3                5.849317e-3     +6.035e-9
p8      1.779699e-3          2.238268e-3                2.238268e-3     +2.675e-9
```

After the published SDP plus numerical PSD-floor enforcement, p8 has

```text
Gamma_min = +3.295e-7
```

and is therefore physical on the tested generator/spectrum criteria.

The time-domain correction improves coherently p4 -> p5 -> p8.  However the quantum detailed-balance defect remains substantial away from the central system band, so p8 is **promising, not accepted**.

## Parallel direct-TEMPO disposition

Run `32005827817` (`tcut=20`, `tend=64`, `epsrel=1e-12`, `dt=.2,.1`) was externally cancelled after about three hours before either direct-TEMPO job emitted a state metric.

This is a computational no-result.  Do not count it as evidence for or against TEMPO.  Do not rerun the same configuration unchanged.

## Predeclared p12/p16 criteria

Higher Padé order is useful only if the **physical coupled correction converges coherently**, rather than trading a better time-domain norm for worse detailed balance or generator physicality.

### A. Mandatory physicality at each order

For both p12 and p16 after the published SDP and the same deterministic PSD-floor enforcement:

1. `Y_min > 0`;
2. `Gamma_min >= -1e-12` after numerical enforcement;
3. wide scanned coupled spectrum minimum `>= -1e-10`;
4. no anomalous conditioning jump larger than 10x relative to p8 without an independent numerical explanation.

Any failure blocks the branch.

### B. Mandatory monotonic convergence

The sequence p8 -> p12 -> p16 must decrease **both**:

- relative SDP correction `||l-Yr||/||l||`;
- maximum relative exact time-domain BCF error over the existing `0 <= tau <= 24` audit grid.

A reversal at p12 or p16 rejects high-order Padé-coordinate correction as the active compression route, even if one scalar threshold below happens to pass.

### C. p16 time-domain target

For p16:

```text
max relative exact C(t) error < 1.0e-3
C(0) relative error           < 1.0e-3
```

This is a bath-compression criterion only, not a harmonic-state acceptance criterion.

### D. System-band detailed-balance target

The far negative-frequency tail is exponentially small and is not used by itself as a relative-error acceptance metric.  Instead evaluate detailed balance explicitly at system-relevant positive frequencies.

The high-order probe must report

```text
x = omega/omega_c = 0.5, 1.0, 1.13, 1.5, 2.0
```

with

```text
E_DB(x) = | ln[S(-x)/S(+x)] + beta*hbar*omega_c*x |.
```

Required:

```text
p16: E_DB(1.0)  < 2.0e-2
p16: E_DB(1.13) < 3.0e-2
```

and p8 -> p12 -> p16 must improve `E_DB` at x=1.0, 1.13, and 2.0 monotonically.

The x=2.0 value is a convergence diagnostic, not a standalone pass/fail ceiling at this stage.

### E. Spectrum error metric

Do not use the previous maximum relative spectral error over points where the exact spectrum is merely `>1e-5`; that statistic is dominated by exponentially tiny negative-frequency values and becomes numerically misleading.

The high-order probe must additionally report:

1. maximum absolute spectral error normalized by `S_exact(0)` over `-4 <= x <= 6`;
2. RMS spectral error normalized by `S_exact(0)` over the same interval;
3. maximum relative spectral error only where `S_exact(x) >= 1e-3 S_exact(0)`.

These metrics must improve p8 -> p12 -> p16.  No absolute pass threshold is imposed until the p12/p16 trend is observed; they are used to prevent a false pass based only on C(t).

## Promotion rule

If all mandatory physicality and monotonicity conditions hold and p16 meets the time-domain and system-band detailed-balance ceilings, the coupled-Lindblad bath is promoted only to **harmonic system-dynamics benchmarking**.

It is not promoted to nonlinear detector dynamics.

The next stage would then require:

- explicit auxiliary-mode/Fock truncation convergence;
- harmonic equilibrium comparison to the exact Gaussian/FDT state;
- full-state trace distance / nuclear-norm metric;
- positivity, trace, Hermiticity, and late-time stationarity;
- mode-count/order comparison, at minimum p12 vs p16.

Only after that independent harmonic solver passes can nonlinear Gate C.1/C.2 work resume.

If the high-order bath fails, abandon Padé-coordinate physical correction and move to a direct positive-real/coupled realization fitted to the exact physical spectrum.  Do not return to independent Lorentzian pseudomodes or unchanged long-memory direct TEMPO.

## Gate status at freeze

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / bath-level independent-solver recovery
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
