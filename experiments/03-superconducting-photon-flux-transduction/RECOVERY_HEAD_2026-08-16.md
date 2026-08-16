# Experiment 03 — Recovery Head — 2026-08-16

This file is a compact live handoff for the post-rate-frontier / exact-open-system phase. It supplements `AGENTS.md`; repository state remains authoritative.

## Recovery order

Read, in order:

1. `CURRENT_STATE.md`
2. `RATE_FRONTIER_RESOLUTION_2026-08-16.md`
3. `OPEN_SYSTEM_METHOD_GATE_2026-08-16.md`
4. `CLAIM_LEDGER_QUANTUM_FRONTIER_2026-08-16.md`
5. `RATE_FRONTIER_PROMOTION_2026-08-16.md` for historical provenance
6. `AGENTS.md`
7. active scripts/workflows listed below

## Closed rate-frontier gates

### `.212`

Canonical engineering representative of the reduced `.212-.213` plateau.

```text
r_Gamma = 10.6229699624
C       = 24.262211 pF
R       = 7.5308506 ohm
fc      = 1.9844267 GHz
```

High-stat capture certification, run `31926948721`, `N=8192` per area:

```text
A99_point   >= 490 um^2 on tested grid
A99_95lower >= 490 um^2 on tested grid
```

### `.213`

Exact total-dark root:

```text
r_Gamma = 11.2051409652
```

Exact-root capture rerun `31972394510`, `N=4096` per area:

```text
A99_point   >= 485 um^2 and <495 um^2 on tested points
A99_95lower >= 475 um^2 and <485 um^2 on tested points
```

This does not overturn the strict paired no-unique-winner result because the independent certification runs are not a common-random-number paired comparison. It strengthens `.212` as the engineering representative.

### `.214`

The finite-amplitude one-negative periodic branch is real, but the controlled pre-action-crossing Gaussian dark target has no root.

Run `31972574115`:

```text
r_c            = 11.885380810
r_min          = 11.787962959
Gamma_per,min  = 1.700777e-6 /s
r_min/r_c      = 0.991803557
classification = NO_SAFE_ROOT_BEFORE_ACTION_CROSSOVER
```

Therefore `.214` is excluded from the controlled safe Gaussian design frontier. Any reconsideration requires a uniform/thimble-aware first-order multi-saddle rate treatment. Do not run a canonical `.214` capture comparison before that dark-rate problem is solved.

## Exact/open-system quantum frontier

The isolated finite-pulse phase calculation shows coherent recrossing after barrier reformation, so dissipation/decoherence is constitutive of latching. Local Lindblad and secular global-Davies closures are not quantitatively controlled at the `.212` operating point. The direct effective port bath is UV regular for the phase coordinate and has a validated exponential correlation decomposition.

Mandatory sequence:

```text
A. direct-port bath correlation              PASS
B. harmonic HEOM versus exact cold FDT       IN PROGRESS
C. nonlinear cold/metastable HEOM gate       NOT STARTED
D. finite-pulse nonlinear HEOM convergence   NOT STARTED
E. exact/open versus N=8192 TWA comparison   NOT STARTED
```

Active Gate-B files:

```text
calculations/direct_port_bath_correlation.py
calculations/heom_harmonic_port_validation.py
calculations/requirements-heom.txt
.github/workflows/experiment03-heom-harmonic-port.yml
```

Gate-B workflow:

```text
run 31973895654
head d2e7976f18423777d765ca212717100b384ae5f8
```

At the time this recovery record was written, the HEOM solve step was still running. Do not infer pass/fail from this file; inspect the live workflow result.

## Claim discipline

Do not call the TWA capture probability exact quantum efficiency. Do not call `.214` impossible under every uniform first-order treatment. Do not create a manuscript from Experiment 03 yet.

The next agent should first inspect live `main` and Gate-B run `31973895654`. If Gate B passes, record the covariance/convergence metrics and proceed to a nonlinear cold/metastable HEOM validation before any finite-pulse detector probability. If Gate B fails, repair the bath mapping/counterterm/hierarchy before advancing.
