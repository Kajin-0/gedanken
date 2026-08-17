# Experiment 03 — open-system current state

Date: 2026-08-17
Status: **Gate C.1 ACTIVE / harmonic direct-TEMPO method validation**  
Publication: **NO-GO**

This file is the authoritative recovery point for the open-system quantum branch.  It supersedes the older reaction-coordinate/DVR recovery queue in `CURRENT_STATE.md` for quantum-method work.  The reduced dark/capture design history in `CURRENT_STATE.md` remains useful, but its sections 17–19 are historical.

## Gate disposition

```text
Gate A  direct-port bath correlation                 PASS
Gate B  harmonic conventional HEOM exact-state gate  PASS
Gate C.1 nonlinear cold/metastable state             ACTIVE / BLOCKED on final harmonic TEMPO validation
Gate C.2 nonlinear open-system continuation          BLOCKED
Gate D  finite-pulse nonlinear open capture          BLOCKED
Gate E  exact-open vs N8192 TWA                      BLOCKED
Publication                                           NO-GO
```

## Canonical physical environment

The same passive positive-real direct-port environment remains controlling:

```text
phase port -- Lf -- node -- (R || Cf) -- ground
ReY(omega) = (1/R) / [1 + (omega/omega_D)^4]
```

The direct-port correlation is exactly represented, for the present harmonic solver work, by two physical circuit poles plus the already validated Bose-Padé thermal terms.  No spectral-density refit or alternate damping model is authorized.

## Exact harmonic oracle

```text
sigma_x = 3.989969857213e-2
sigma_u = 4.264669020793e-2
sigma0  = 4.01157261977e-2
nbar    = 0.0286833504
r_eq    = 0.03329044903832
```

Existing Gate-B full-state thresholds remain frozen:

```text
finite-basis exact-reference width error < 1e-7
max FDT width error                      < 1e-6
0.5 ||rho-rho_exact||_1                  < 5e-6
negative eigenvalue mass                 < 5e-8
```

## Conventional HEOM status

Harmonic Gate B passed at bare dim8, p4, depth9.

Raw nonlinear hard-cutoff depth escalation is **closed** under the predeclared non-monotone rule.  Do not run nonlinear depth8+.

Direct nonlinear spectral pollution is explicitly resolved.  For dim10,p4,d5:

```text
lambda_max = +0.292668905 +/- 0.885737876 i
```

and the dominant unstable eigenmode has

```text
terminal hierarchy-tier weight = 0.9948761
root-ADO weight                 = 9.51e-12
top-3 system-level weight       = 0.8878851
```

Thus the failure is a coupled hierarchy-boundary x system-basis-boundary artifact.

## Rejected recovery routes

### Stable-mode projection

Removes exponential growth but fails the exact harmonic state oracle.  Not authorized for nonlinear use.

### Diagonal NZ/Schur terminator

Acts approximately like one effective extra hierarchy tier.  Improves moments/spectrum but does not solve full-state positivity/convergence.  Not sufficient for C.1.

### Free-Pole HEOM

Implementation passes real and complex analytic pure-dephasing audits at ~1e-15 accuracy, but the dim8 depth sequence is non-monotone in physicality and dim12 depth2 is dynamically unstable.  Closed in:

`FP_HEOM_HARMONIC_ORACLE_FINAL_2026-08-17.md`.

No deeper FP escalation is authorized.

### PT-TEMPO reusable process tensor

Rejected because analytic pure-dephasing error worsens under timestep refinement:

```text
dt=.100  2.6912e-5
dt=.050  2.8284e-4
dt=.025  1.3133e-3
```

Direct TEMPO is **not** rejected by this result.

## Direct TEMPO: active method

Direct OQuPy TEMPO with `CustomCorrelations` is the active independent solver route.

Analytic interface audits:

```text
real exponential pure dephasing    ~1e-13 error  PASS
complex-pole pure dephasing         ~1e-13 error  PASS
```

Therefore the explicit-correlation and negative-time conjugation conventions are validated.

The full acceptance rule is frozen in:

`TEMPO_HARMONIC_ACCEPTANCE_RULE_2026-08-17.md`.

No threshold may be relaxed after seeing later results.

## Dim2 finite-system reference

Conventional p4 HEOM stationary state is depth/order converged:

```text
rho_ref = diag(0.9662704692933118,
               0.03372953070668817)
```

Convergence:

```text
p4 d8 -> d9 pop1 change = 6.84e-10
p5 d8 - p4 d9           = 2.61e-7
```

Thus the TEMPO mapping reference is not the source of the observed ~1e-3 finite-memory bias.

## Direct TEMPO mapping is validated at dim2

A full-history TEMPO-vs-HEOM transient comparison, where no bath history is discarded, shows essentially exact second-order timestep convergence:

```text
max 0.5||rho_TEMPO-rho_HEOM||_1

dt=.20  4.022613e-4
dt=.10  1.004917e-4
dt=.05  2.510405e-5
```

Each timestep halving reduces the error by ~4.003x.

At fixed `dt=.05`, tightening tensor tolerance to `epsrel=1e-12` gives

```text
max mapping error = 2.509646e-5
max trace error   = 2.29e-10
max anti-Herm     = 7.736e-9
```

with `PASS_FINE_TEMPO_TENSOR_PHYSICALITY`.

Therefore the finite-system direct-port TEMPO mapping is strongly validated; the full-history discrepancy is finite second-order timestep error, while tensor physicality is independently controllable.

See:

`TEMPO_DIM2_MAPPING_CONVERGENCE_2026-08-17.md`.

## Finite-memory bias is separately established

Exact signed integrated bath tail:

```text
tcut=8   6.67319e-3
tcut=12  5.52458e-4
tcut=16  4.46652e-5
tcut=20  3.41131e-6
tcut=24  2.53454e-7
```

At `dt=.2,tcut=8,epsrel=1e-10`, extending the trajectory to tau64 gives

```text
half-distance to HEOM stationary state = 1.5313745e-3
late drift tau48->64                   = 8.34e-6
```

which matches the predeclared fitted `tcut=8` plateau `D_inf~1.532e-3`.

Changing only memory at the same `dt=.2,epsrel=1e-10,tend=32` gives

```text
tcut=8   half-distance = 1.625899e-3
tcut=12  half-distance = 4.046547e-4
```

so enlarging memory alone improves the state by ~4.02x at tau32.

A coarse same-grid `dt=.4,tend=64` comparison gives

```text
tcut=8   ~2.0884e-3
tcut=20  ~6.3642e-4
```

again showing substantial memory improvement, although absolute values are coarse-grid/tensor diagnostic results only.

## Preferred final harmonic TEMPO basis

Use the counterterm-renormalized system normal mode, not the bare oscillator basis and not the equilibrium-squeezed basis.

```text
Omega_s/omega_c = 1.131080565620
r_sys            = 0.06158671428343
r_eff            = -0.02829626524511
```

In this basis:

```text
H = Omega_s (b^dag b + 1/2)
x = sigma0 exp(-r_sys)(b+b^dag)
u = i sigma0 exp(+r_sys)(b^dag-b)
```

and the exact coupled reduced equilibrium is only weakly squeezed.

Finite-reference width errors:

```text
dim6  8.66848e-7
dim7  5.06612e-8   <-- minimum acceptance basis
dim8  2.95092e-9   <-- larger-basis control
```

The explicit high-basis unitary transformation agrees at ~2.5e-16 relative error.

## Current controlling run

Combined dim2 long-memory/timestep matrix:

```text
workflow run 32005827817

tcut=20
tend=64
epsrel=1e-12

case d200: dt=.2
case d100: dt=.1
```

Purpose:

1. test whether the clean `dt^2` mapping trend survives after memory bias is largely removed;
2. measure the combined stationary error at the first physically justified long-memory cutoff;
3. decide whether a costly `dt=.05,tcut=20` case is warranted.

Do not call this final harmonic acceptance even if favorable; dim2 is a mapping/convergence test only.

## Immediate queue

1. Read run `32005827817` d200/d100 results.
2. Read the still-pending strict `tcut=12,tend=64` case `32003044791 / 95306963004` if it completes first.
3. If `tcut=20` d200->d100 is coherent and approximately second order, authorize one `dt=.05,tcut=20,epsrel` case with tensor tolerance chosen from the completed fine-step audit.
4. Close dim2 combined convergence before moving system dimension upward.
5. Then run the harmonic direct-port TEMPO exact-state convergence matrix in **system-mode dim7**, with dim8 control, under `TEMPO_HARMONIC_ACCEPTANCE_RULE_2026-08-17.md`.
6. Only after harmonic TEMPO passes every frozen convergence axis may nonlinear Gate C.1 begin.
7. For nonlinear C.1, recover/use the nonlinear restricted-well Hamiltonian; do not use the legacy harmonic-Wigner `quantum_initial_capture.py` as quantum initialization.
8. Do not run photon-pulse Gate D until the nonlinear cold/metastable state is independently stable and converged.

## Claim boundary

No current open-system calculation authorizes claims of:

- exact physical nonlinear quantum efficiency;
- exact persistent-latch probability;
- nonlinear detailed-balance-preserving capture;
- a completed physical DCR;
- a publishable detector architecture novelty claim.

The strongest current method statement is:

> The direct-port bath correlation and harmonic conventional HEOM benchmark are validated.  Conventional nonlinear hard-cutoff HEOM develops demonstrable boundary-localized spectral pollution, and tested projection/terminator/FP/PT-TEMPO recovery routes do not provide a controlled nonlinear solver.  Direct TEMPO has independently passed real/complex analytic correlation tests and, on a noncommuting dim2 finite-system benchmark, converges to depth-converged HEOM with clean second-order timestep scaling while finite-memory bias is separately measurable and strongly reduced by increasing the memory window.  The remaining task is combined long-memory/fine-step convergence followed by the frozen dim7/dim8 harmonic exact-state TEMPO gate.  Nonlinear Gate C.1 remains blocked until that gate passes.
