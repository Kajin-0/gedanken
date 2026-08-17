# Experiment 03 — PT-TEMPO reusable-process-tensor rejection

Date: 2026-08-17

## Scope

This note closes the attempted OQuPy PT-TEMPO process-tensor reuse optimization for the current Gate-C.1 method-recovery program.

It does **not** reject direct TEMPO.  Direct TEMPO previously reproduced both real- and complex-exponential analytic pure-dephasing oracles to the ~1e-13 numerical floor.  The rejection here is specifically for the tested reusable PT-TEMPO construction under timestep refinement.

## Motivation

The frozen TEMPO harmonic acceptance rule requires initial-state independence.  A reusable process tensor would be computationally attractive because one bath influence object could be contracted against multiple factorized system initial states without rebuilding the influence functional.

Before using that optimization on the direct-port bath, it was tested on the analytically soluble pure-dephasing problem

```text
C(t)=0.2 exp(-|t|)
H=0
q=diag(0,1)
```

with exact coherence

```text
rho01(t)=rho01(0) exp[-0.2 (t - 1 + exp(-t))].
```

## Reuse audit

Script:

`calculations/pttempo_pure_dephasing_reuse_selftest.py`

Workflow run `32003640581`, job `95308676058`.

One process tensor at

```text
dt=.1
tcut=tend=5
epsrel=1e-10
```

was reused for two materially different initial density matrices.

Both initial states gave the same analytic error:

```text
max relative coherence error = 2.69120298e-5
max trace error              = 8.64569e-10
max Hermiticity error        = 3.19663e-12
```

Thus process-tensor reuse itself behaved consistently across initial states, but the analytic error was far larger than the direct-TEMPO result on the same oracle.

## Timestep-convergence audit

Script:

`calculations/pttempo_dephasing_dt_convergence.py`

Workflow run `32003792628`.

At fixed

```text
tcut=tend=5
epsrel=1e-10
```

timestep refinement produced:

```text
dt=.100:
  max relative error = 2.69120298e-5
  max trace error    = 8.64569e-10
  max Hermiticity    = 3.19663e-12

dt=.050:
  max relative error = 2.82838094e-4
  max trace error    = 8.05242e-10
  max Hermiticity    = 2.84228e-11

dt=.025:
  max relative error = 1.31330702e-3
  max trace error    = 1.06344e-9
  max Hermiticity    = 3.39042e-8
```

The analytic error therefore worsens strongly and monotonically as the timestep is refined over `.1 -> .05 -> .025` at the fixed tensor tolerance.  The finest case also violates the Hermiticity guard.

## Disposition

**The tested PT-TEMPO reusable-process-tensor route is rejected as the current production solver path.**

Reasons:

1. It fails basic analytic convergence under timestep refinement.
2. The failure appears before any direct-port bath or detector physics is introduced.
3. Co-tuning the tensor tolerance solely to rescue a computational optimization would create an unnecessary extra convergence manifold when direct TEMPO already passes the same analytic oracle at the numerical floor.
4. A reusable process tensor is not required for physical correctness; it is only an optimization.

Therefore:

- do not use the present PT-TEMPO construction for harmonic acceptance;
- do not use it for nonlinear Gate C.1;
- do not infer a failure of direct TEMPO from this result;
- do not relax the analytic guard or select the favorable `dt=.1` point.

The active independent solver remains **direct TEMPO**, currently undergoing finite-system TEMPO-vs-HEOM mapping tests and direct-port harmonic pilots.

## Gate status

- Gate A: PASS
- Gate B conventional harmonic HEOM: PASS
- Gate C.1: ACTIVE / direct-TEMPO method recovery
- Gate C.2: BLOCKED
- Gate D: BLOCKED
- Gate E: BLOCKED
- Publication: NO-GO
