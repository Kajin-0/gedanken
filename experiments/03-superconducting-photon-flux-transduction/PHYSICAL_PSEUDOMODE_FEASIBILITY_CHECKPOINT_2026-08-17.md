# Experiment 03 — physical pseudomode feasibility checkpoint

Date: 2026-08-17

## Scope

This checkpoint records the scalable independent-solver fallback opened because direct TEMPO, while validated at dim=2, has not yet demonstrated practical scaling to the required harmonic dim7/dim8 basis.

No pseudomode system dynamics have been authorized.  Gate C.1 remains blocked on an independent harmonic exact-state solver.

## 1. Existing finite Padé BCFs are not globally physical

The p4/p5/p8 finite exponential correlations were tested through their exact two-sided spectra

```text
S_N(omega)=2 Re sum_k c_k/(gamma_k-i omega).
```

They become negative at large negative frequency:

```text
order  first zero omega/omega_c  minimum S_N/S(0)
p4     -2.64476601346             -7.622954889e-5
p5     -3.20140405858             -2.397304383e-5
p8     -4.87143305783             -1.905254745e-6
```

The violation is structural: the rational expansion retains an odd `1/omega^3` UV term, which necessarily changes sign between positive and negative frequency, whereas the exact quantum bath remains nonnegative and suppresses the negative-frequency tail exponentially by detailed balance.

Therefore the existing Padé BCFs cannot simply be declared physical CPTP pseudomode correlations.

See `PADE_BATH_SPECTRAL_POSITIVITY_REJECTION_2026-08-17.md`.

## 2. Broad independent thermal Lorentzian modes are inadequate

Script:

`calculations/physical_lorentzian_pseudomode_feasibility.py`

Workflow run `32006953427`, job `95318298322`.

A 633-mode globally nonnegative thermal Lorentzian dictionary was fit to the exact physical spectrum with nonnegative weights.  The optimizer strongly suppressed amplitudes because broad Lorentzian tails leak excessive weight into the exponentially suppressed negative-frequency side.

Representative result:

```text
full dictionary active modes ~28
C(0) relative error          ~0.903
```

Compressed K=8/16/32/64 fits remain grossly inaccurate.  K64 gives approximately

```text
max rel spectral error where exact>1e-5 ~0.913
detailed-balance max log error            ~19.2
max relative time-correlation error       ~15
C(0) relative error                       ~0.900
```

Conclusion: broad independent thermal modes are not a viable compression.

## 3. Dense narrow independent modes remain impractical

Script:

`calculations/physical_lorentzian_continuum_scaling.py`

Workflow run `32007103938`, job `95318738293`.

The exact positive-frequency spectrum was discretized constructively into 64–512 globally physical thermal modes, with widths `gamma=eta*DeltaOmega`, `eta=.2,.5,1`.

Even the best tested 512-mode narrow case remains poor as a compressed accurate bath:

```text
N=512, eta=.2
max relative spectral error (exact>1e-5) ~1.33
detailed-balance max log error            ~20.0
max relative correlation error            ~29.2
C(0) relative error                       ~0.00746
```

Narrowing the modes improves zero-time normalization and reduces negative-frequency leakage but creates a dense quasi-continuum with long auxiliary memory and poor time-domain cancellation.

Workflow conclusion:

```text
INDEPENDENT_PHYSICAL_CONTINUUM_NOT_PRACTICAL_AT_N_LE_512
```

Therefore independent Lorentzian pseudomodes are not the active scalable route.

## 4. Coupled-Lindblad realization is the active pseudomode branch

Primary method: Huang, Park, Chan, Lin, *Coupled Lindblad pseudomode theory for simulating open quantum systems* (2026).

For a quasi-Lindblad realization

```text
Cq(t)=l^dag exp(-i Lambda t) r,
```

physical coupled-Lindblad feasibility is tested through

```text
Y > 0
Y r = l
i(Y Lambda - Lambda^dag Y) >= 0.
```

When exact feasibility fails, the published correction minimizes

```text
||l-Yr||_2^2
```

subject to the same positive-semidefinite generator condition.

Implemented:

`calculations/coupled_lindblad_pade_sdp.py`

Launch wrapper:

`calculations/run_coupled_lindblad_pade_sdp.py`

Workflow:

`.github/workflows/experiment03-coupled-lindblad-pade-sdp.yml`

Current run:

```text
32007602698
```

The wrapper only binds the canonical `HBAR` symbol used by the detailed-balance reporting diagnostic; it changes no SDP, bath coefficient, physical parameter, or acceptance logic.

The SDP tests p4/p5/p8 and reports:

- minimum physical correction residual;
- `Y` conditioning;
- coupled damping matrix `Gamma` eigenvalues;
- global spectrum positivity;
- exact-spectrum error over the system-relevant band;
- detailed-balance error;
- coupled BCF versus original Padé and exact direct-port correlation over `0<=tau<=24`.

## Decision rule

A small SDP residual alone is insufficient.

A corrected coupled bath is only worth advancing if it simultaneously has:

1. positive semidefinite `Gamma` within numerical tolerance;
2. globally nonnegative spectrum on the wide scan;
3. small correction to the already validated time-domain bath correlation;
4. acceptable exact-spectrum and detailed-balance error in the system-relevant band;
5. acceptable `C(0)` and static/counterterm consistency.

If p8 is promising, freeze a stricter bath-acceptance rule before any system dynamics and then benchmark the corrected coupled bath against the exact harmonic FDT state with explicit pseudomode Fock/mode-count convergence.

If p8 is not promising, do **not** return to independent Lorentzian fits.  The next pseudomode route is a direct frequency-domain realization of the exact physical spectrum followed by the physical gauge/SDP construction.

## Parallel direct-TEMPO branch

Direct TEMPO remains validated at dim=2 but scalability to dim7 is unproven.  The combined long-memory dim2 matrix is still active:

```text
run 32005827817
p4, tcut=20, tend=64, epsrel=1e-12
dt=.2 and .1
```

Do not infer from runtime.

## Gate status

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / independent harmonic solver recovery
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
