# Experiment 03 — variable-pole nonlinear C.1 numerical freeze

**Date:** 2026-08-17  
**Status:** **FROZEN BEFORE ANY VARIABLE-POLE NONLINEAR OPEN-SYSTEM RESULT**

This file completes the second pre-result freeze required by
`VARIABLE_POLE_NONLINEAR_C1_ACCEPTANCE_2026-08-17.md`.

It uses only:

- the already accepted harmonic variable-pole bath;
- the deterministic harmonic/Fock preflight;
- static nonlinear phase-DVR basis diagnostics;
- implementation-level scaling/solver information.

No nonlinear open-system state, trajectory, basin probability, or convergence
result was used to select the settings below.

## 1. Preflight provenance

### Accepted bath regeneration / harmonic structure

```text
run       32040199268
job       95418029137
artifact  9291819419
sha256    c10fe7b60adc38b6e0e5a56ce3565c628b7c3c03de865c528f3cc5c0796375e0
```

The accepted rank-16 harmonic result was reproduced exactly enough to re-pass
its original gate.

Rank-16 structural diagnostics:

```text
H tridiagonal leakage             = 0
||g[1:]||/||g||                   = 2.47e-17
Gamma off-diagonal Fro fraction   = 0.64452
Gamma beyond-nearest fraction     = 0.50857
Gamma_min                         = 2.0573e-9
Gamma_max                         = 1.33457e2
cond(Gamma)                       = 6.4870e10
```

Thus the accepted gauge is an excellent Hamiltonian chain/system-coupling gauge,
but **not** a local-dissipation gauge.  The dense positive `Gamma` must be kept
exactly; it may not be dropped to its diagonal or nearest-neighbor part.

### Static detector basis

The first lowest-global basis test was scientifically rejected even though its
numerical workflow succeeded.  Up to 96 lowest global states retained essentially
zero of the prepared left state.

The replacement unrestricted metastable-window basis passed the static closure
diagnostic:

```text
run       32041105285
job       95420446671
artifact  9291966253
sha256    984a45ccac2fde8e06855295c7cf5ba9bf4683ee47b67dd643d86c92a6899337
```

At dimension 16:

```text
rho_L preparation loss     = 8.93e-10
y-image loss               = 3.86e-9
y^2-image loss             = 2.47e-7
```

At dimension 24:

```text
rho_L preparation loss     = 8.81e-10
y-image loss               = 1.89e-9
y^2-image loss             = 5.01e-9
```

## 2. Frozen detector basis

Use unrestricted full-double-well eigenstates selected by shift-invert nearest

```math
E_{target}=U(x_m)+E_{0,L}.
```

Freeze

```text
PRIMARY detector dimension   Ns = 16
ENLARGED detector control    Ns = 24
```

The basis ordering is by increasing `|E-E_target|` using the same full phase grid
and target construction as `variable_pole_c1_resonant_basis_preflight.py`.

The system-bath coordinate is the centered phase displacement

```math
y=x-x_m.
```

The counterterm operator is the directly projected physical `P y^2 P`, never
`(P y P)^2`.

## 3. Frozen bath gauge

Keep the accepted **Hermitian-Lanczos chain gauge** without an additional unitary
rotation:

```text
H_b      real symmetric tridiagonal
g        sqrt(C0) e1 to numerical precision
Gamma    full dense positive matrix
```

Reason: this gauge makes the Hamiltonian and system coupling maximally local.
Diagonalizing `Gamma` would make the dissipators local but turns the Hamiltonian
into a dense all-to-all matrix and distributes the system coupling.  No such
post-acceptance gauge change is needed for the first structured solver.

The rank-16 optimized bath is primary; rank 24 is the fixed bath-order control.

## 4. Frozen finite-bosonic cutoffs

Harmonic one-mode marginals in the accepted chain gauge give for rank 16:

```text
mode 0: nbar=2.7493e-2
        tail above d=4  = 1.0790e-5
        tail above d=6  = 5.9170e-8
        tail above d=8  = 3.454e-10

largest non-mode0 occupation: nbar=5.3889e-3
largest non-mode0 tail above d=4 = 2.0282e-7
```

Freeze the first Fock matrix as

```text
PRIMARY Fock:
  mode 0       d0 = 6
  modes 1..K-1 d  = 4

HIGH Fock control:
  mode 0       d0 = 8
  modes 1..K-1 d  = 6
```

For rank 16, the sum of the one-mode harmonic marginal tail diagnostics is
approximately

```text
PRIMARY = 2.79e-7
HIGH    = 4.89e-10.
```

These are preflight diagnostics only.  They do not replace the frozen nonlinear
Fock convergence requirement.

Use the same PRIMARY local rule for the rank-24 bath-order control.  Rank 24 is
not allowed to choose a different cutoff because its nonlinear result looks
better or worse.

## 5. Structured solver class

A full density tensor is rejected by the acceptance file (`~6.87 TB` already for
`Ns=10,d=2,K=16`).

Freeze the first structured method as a **deterministic vectorized density-operator
MPS (MPDO in Liouville space) evolved under an MPO Liouvillian**.

Implementation target:

```text
Julia
ITensorMPS v0.4.1
ITensors version resolved compatibly and printed/archived by CI
```

The package choice is frozen before nonlinear results.  The exact resolved
`ITensors` version from the implementation-oracle CI is to be recorded before
the harmonic finite-bosonic matrix is interpreted.

Why deterministic MPDO rather than quantum trajectories:

- the acceptance metric is a reduced density matrix at `5e-5`--`1e-4` scale;
- a deterministic density representation avoids adding Monte-Carlo sampling
  uncertainty to every convergence comparison;
- local operator-space dimensions remain finite and modest after the harmonic
  Fock preflight;
- the dense positive `Gamma` can be represented exactly through collective
  Lindblad operators without replacing it by local damping.

## 6. Exact finite-bosonic generator

In dimensionless `tau=omega_c t`, use

```math
H_{tot}
=H_s+\lambda_{ct}P y^2P
+\sum_{jk}(H_b)_{jk} b_j^\dagger b_k
+(P y P)\sum_j(g_j b_j^\dagger+g_j^* b_j).
```

The system bare Hamiltonian is diagonal in the selected unrestricted resonant
basis; an irrelevant scalar energy offset may be removed.

Let the accepted positive damping matrix have Cholesky factor

```math
\Gamma=L L^\dagger.
```

Use the collective collapse operators

```math
c_\mu=\sqrt{2}\sum_j L_{j\mu}^* b_j.
```

This gives the required auxiliary first-moment drift

```math
\dot b=(-iH_b-\Gamma)b
```

before system coupling.

No diagonal approximation to `Gamma` is permitted.

For column-major vectorization, the dense-oracle Liouvillian convention is

```math
\mathcal L_H=-i[I\otimes H_{tot}-H_{tot}^T\otimes I],
```

and for every collapse operator

```math
\mathcal D_c
=c^*\otimes c
-\frac12 I\otimes c^\dagger c
-\frac12(c^\dagger c)^T\otimes I.
```

The MPS implementation must reproduce this convention in its small-system oracle.

## 7. Initial state and correlation build-up

Use the static left restricted thermal mixture projected into the unrestricted
resonant system basis, tensor the auxiliary vacuum product state at `tau=0`, and
then evolve the **unrestricted** zero-drive generator.

Do not keep a hard wall during the acceptance trajectory.

The factorized state is only the initializer.  System-bath correlations are
allowed to develop dynamically.  Acceptance is judged only after the late
`tau=64,80,96` stationarity window already frozen in the physical acceptance
file.

## 8. Mandatory implementation oracles before nonlinear C.1

### 8.1 Dense finite-mode Liouvillian oracle

On a deterministic two-auxiliary finite-Fock model, require:

```text
collective-collapse vs direct Kossakowski Liouvillian relative Fro error < 1e-12
auxiliary first-moment drift matrix vs (-iH-Gamma) relative error        < 1e-12
column-vectorization dense propagation vs direct master-equation state  < 1e-11
```

### 8.2 MPDO/MPO oracle

For the same small model, compare the tensor-network result to the dense
Liouvillian result at multiple times. Require

```text
max half trace distance < 1e-9
max trace error         < 1e-10
max anti-Herm Fro error < 1e-10.
```

Failure closes the implementation before the accepted rank-16 bath is run.

### 8.3 Harmonic rank-16 finite-bosonic gate

The first full-rank tensor-network calculation is harmonic, not nonlinear.  It
must satisfy the already frozen finite-bosonic harmonic thresholds:

```text
max width error                     < 1e-5
half trace distance to exact FDT    < 2e-5
normalized q-p covariance           < 2e-5
```

and must improve/cohere under PRIMARY -> HIGH Fock/tensor refinement.

Only after this passes may the nonlinear Hamiltonian be enabled.

## 9. Frozen tensor-evolution matrix

Use two-site TDVP so a product MPDO can grow its bond dimension.

```text
PRIMARY tensor evolution
  nsite          = 2
  time_step      = 0.02
  maxdim         = 128
  SVD cutoff     = 1e-10
  local Krylov tolerance = 1e-11
  normalize      = false

TIGHT tensor control
  nsite          = 2
  time_step      = 0.01
  maxdim         = 256
  SVD cutoff     = 1e-12
  local Krylov tolerance = 1e-13
  normalize      = false
```

The no-drive C.1 checkpoints remain

```text
tau = 0, 20, 40, 64, 80, 96
```

with all physicality/stationarity metrics evaluated at the frozen times.  The
harmonic pre-gate may additionally extend to `tau=120` if needed to compare to
the exact equilibrium oracle; that extension cannot be used to retune the
nonlinear `tau=96` gate.

Every run must report maximum bond dimension and accumulated/maximum discarded
weight or the closest solver-native truncation diagnostic.

## 10. Frozen first nonlinear matrix after harmonic pass

If and only if all implementation and harmonic finite-bosonic oracles pass, run:

```text
A  PRIMARY:       bath16, Ns16, Fock PRIMARY, tensor PRIMARY
B  system basis:  bath16, Ns24, Fock PRIMARY, tensor PRIMARY
C  Fock control:  bath16, Ns16, Fock HIGH,    tensor PRIMARY
D  tensor control:bath16, Ns16, Fock PRIMARY, tensor TIGHT
E  bath control:  bath24, Ns16, Fock PRIMARY, tensor PRIMARY
```

No photon pulse is part of this matrix.

No result-dependent sixth case may be added without a new pre-result freeze.

## 11. Stopping rule

If the dense implementation oracle fails, fix only the implementation error and
rerun the unchanged oracle.

If the MPDO oracle fails under the frozen method, the MPDO implementation is not
authorized for the full bath until the cause is identified and a new solver
freeze is committed.

If the harmonic finite-bosonic gate fails physically or fails to converge under
the frozen PRIMARY/HIGH matrix, do **not** run nonlinear C.1.

If the harmonic gate passes, execute the five-case nonlinear matrix unchanged and
judge it only against `VARIABLE_POLE_NONLINEAR_C1_ACCEPTANCE_2026-08-17.md`.

## Gate state at numerical freeze

```text
Gate A                              PASS
Gate B                              PASS
Independent harmonic backend       PASS
C.1 physics acceptance             FROZEN
C.1 numerical representation       FROZEN / implementation oracles next
C.1 nonlinear result               NOT YET RUN
C.2 photon pulse                    BLOCKED
Publication                         NO-GO
```
