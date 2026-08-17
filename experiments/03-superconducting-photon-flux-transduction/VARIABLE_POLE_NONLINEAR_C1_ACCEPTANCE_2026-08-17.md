# Experiment 03 — variable-pole nonlinear Gate C.1 acceptance

**Date:** 2026-08-17  
**Status:** **FROZEN BEFORE ANY VARIABLE-POLE NONLINEAR C.1 RESULT**  
**Scope:** zero-drive nonlinear cold/metastable-state validation only

## 1. Purpose

`VARIABLE_POLE_PHYSICAL_RESULT_2026-08-17.md` passed the independent harmonic
open-system gate with the predeclared rank-16 physical coupled-mode realization
and rank-24 bath-order control.  The next question is narrower than photon
capture:

> Does the same accepted passive environment admit a physical, numerically
> converged, left-well-conditioned metastable cold state when the detector
> coordinate is restored to the full nonlinear phase Hamiltonian?

This file freezes the **physical acceptance conditions and comparison axes**
before that nonlinear calculation is run.  It does not authorize a photon pulse,
a capture probability, a quantum efficiency, or a publication claim.

The old `NONLINEAR_HEOM_GATE_C1_ACCEPTANCE_RULE_2026-08-17.md` remains historical
provenance for the conventional-HEOM branch.  Its HEOM depth/dimension matrix is
not reused here.

## 2. Fixed detector operating point

Use the current engineering representative on the certified safe-side dark
frontier:

```text
delta       = 0.21200
r_Gamma     = 10.6229699624
L           = 111.5 pH
C0          = 215 fF
C           = C0 r_Gamma^2  (~24.262211 pF)
T0          = 20 mK
BETA_COLD   = 0.80
LAMBDA_MIX  = 0.590
```

The nonlinear detector Hamiltonian is the same phase-coordinate/full-CPR model
already validated by `phase_dvr_basis_convergence.py`:

```math
H_s = -\frac{\hbar^2}{2 C \bar\Phi^2}\frac{d^2}{dx^2} + U(x,T_0),
```

with

```math
U(x,T)=\frac{\bar\Phi^2}{L}\int^x F(x',T)\,dx'.
```

No harmonic replacement of `U(x,T0)` is allowed for the accepted nonlinear
result.

## 3. Fixed environment and coupling convention

Use the **accepted variable-pole physical coupled-mode realization**, with no
bath refit:

```text
C(tau) = g^dag exp[(-i H_b-Gamma) tau] g,
H_b     = H_b^dag,
Gamma   = L_b L_b^dag > 0.
```

The rank-16 optimized realization is the **PRIMARY bath**.  The independently
predeclared rank-24 optimized realization is the **bath-order control**.

The exact-C0 initializer normalization from
`VARIABLE_POLE_INITIALIZER_CLARIFICATION_2026-08-17.md` is part of the accepted
model and must be reproduced exactly when the deterministic bath is regenerated.

The nonlinear implementation must preserve the same system-coordinate coupling,
counterterm, auxiliary Hamiltonian, and Lindblad damping convention used by the
accepted harmonic enlarged-system oracle in
`coupled_lindblad_harmonic_gaussian.py`.  No sign, factor-of-two, counterterm, or
frequency normalization may be changed to improve the nonlinear result.

## 4. Prepared-state definition

The physical pre-photon detector state is **not** the global Gibbs state of the
tilted double well.  The lower right well would dominate that state and would not
represent a detector deliberately prepared in the metastable left basin.

Use the left-well phase-DVR construction already validated in
`phase_dvr_basis_convergence.py` as the system-side preparation reference:

1. locate the cold left minimum and separating saddle from the full static force;
2. impose the Dirichlet wall at the separating saddle only while constructing the
   left restricted basis;
3. form the cold left thermal mixture from restricted eigenstates,

```math
\rho_L \propto \sum_n
\exp[-(E_n-E_0)/(k_B T_0)] |n_L\rangle\langle n_L|;
```

4. embed the prepared state into the unrestricted nonlinear phase space for the
   Gate-C.1 evolution/steady-state test.

For the **accepted open-system state**, system-bath correlations must be allowed
to develop.  A permanently factorized `rho_L x auxiliary vacuum` state is not an
acceptable final metastable state merely because it is a convenient initializer.
A confined-left relaxation/conditioning procedure may be used to prepare the
correlated metastable state, but the wall/conditioning rule must be removed for
the subsequent unrestricted no-drive stability test.

The preparation algorithm itself must be reported, deterministic, and subjected
to the convergence controls below.

## 5. No-drive observation window

Use dimensionless time `tau = omega_c t`, with the exact `omega_c` regenerated
from the accepted model.  The primary unrestricted stability window is

```text
tau = 0 ... 96
```

with mandatory late checkpoints

```text
tau = 64, 80, 96.
```

At the current `fc ~ 1.984 GHz`, `tau=96` is approximately 7.7 ns.  A physical
dark rate near `1e-6 s^-1` corresponds to an escape probability of order
`1e-14` on this interval, so observable `1e-4`-scale basin loss is not to be
interpreted as the intended physical dark switching process.

No photon drive, no `T_e(t)` pulse, and no post-pulse classification are allowed
in this gate.

## 6. Physicality requirements

At every reported checkpoint of the unrestricted no-drive trajectory, the
reduced detector density matrix must satisfy

```text
|Tr rho_s - 1|                         < 1e-8
||rho_s-rho_s^dag||_F                  < 1e-8
negative eigenvalue mass              < 5e-8
```

where negative eigenvalue mass is

```math
\sum_{\lambda_i<0}|\lambda_i|.
```

If the numerical representation is a pure-state/trajectory/tensor-network
unravelling rather than an explicit density matrix, these quantities must be
computed from the reconstructed reduced detector state and include sampling
uncertainty where applicable.

Any violation is a hard failure, not a quantity to clip or renormalize away for
the acceptance comparison.

## 7. Metastability and stationarity requirements

Let `P_L` be the projector onto the cold left basin, with the separating saddle
used as the basin boundary.  At `tau=96` require

```text
P_L > 0.995.
```

Over the late unrestricted window require

```text
0.5 ||rho_s(96)-rho_s(80)||_1          < 5e-5
0.5 ||rho_s(80)-rho_s(64)||_1          < 5e-5
|P_L(96)-P_L(80)|                      < 5e-5
|P_L(80)-P_L(64)|                      < 5e-5.
```

These are metastable numerical-stability tests, not measurements of the true
`~1e-6 s^-1` dark rate.

## 8. Mandatory convergence axes

No single discretization/truncation is accepted.  The following axes are all
mandatory.

### 8.1 Nonlinear detector basis

The primary and enlarged detector representations must satisfy at `tau=96`

```text
0.5 ||rho_s^(large)-rho_s^(primary)||_1 < 1e-4
|P_L^(large)-P_L^(primary)|             < 1e-4.
```

The representation may be an unrestricted phase DVR or a converged retained
nonlinear eigenbasis, but it must represent both basins and the separating
region.  A left-only hard-wall Hilbert space cannot be used for the unrestricted
acceptance trajectory.

### 8.2 Auxiliary local/Fock truncation

The accepted harmonic calculation used an infinite-bosonic Gaussian solution;
that convenience does not survive the nonlinear system Hamiltonian.  Therefore
at least two predeclared auxiliary truncation levels must be compared.

At `tau=96` require

```text
0.5 ||rho_s^(Fock-hi)-rho_s^(Fock-primary)||_1 < 5e-5
|P_L^(Fock-hi)-P_L^(Fock-primary)|             < 5e-5.
```

Every local auxiliary basis must additionally report occupation of its highest
retained Fock level (or an equivalent discarded-weight diagnostic).  The exact
local dimensions are **not selected from nonlinear data**.  They will be frozen
in a separate numerical-preflight record using the already accepted harmonic
model before the first nonlinear run.

### 8.3 Tensor/solver accuracy

At least two predeclared solver-accuracy levels must be compared (for example
bond dimension/discarded-weight threshold and timestep/Krylov tolerance as
appropriate to the chosen structured solver).  At `tau=96` require

```text
0.5 ||rho_s^(tight)-rho_s^(primary)||_1 < 5e-5
|P_L^(tight)-P_L^(primary)|             < 5e-5.
```

Reported discarded weight, residual norm, or equivalent internal error estimate
must be finite and consistent with the observed external convergence.

### 8.4 Bath order

Repeat the accepted primary calculation with the rank-24 physical bath under the
same numerical acceptance class.  Require at `tau=96`

```text
0.5 ||rho_s^(rank24)-rho_s^(rank16)||_1 < 1e-4
|P_L^(rank24)-P_L^(rank16)|             < 1e-4.
```

Rank 24 is a control, not an alternative model to select if rank 16 is
unfavorable.

## 9. Harmonic implementation regression is mandatory

Before the nonlinear Hamiltonian is enabled, the explicit finite-bosonic solver
must reproduce the already accepted rank-16 harmonic equilibrium within its own
predeclared truncation/tensor tolerances.

The target remains the independent exact FDT Gaussian state used by
`VARIABLE_POLE_PHYSICAL_RESULT_2026-08-17.md`.

At minimum require the finite-bosonic harmonic implementation to satisfy

```text
max relative system width error       < 1e-5
half trace distance to exact FDT rho  < 2e-5
normalized q-p covariance             < 2e-5
```

and to improve systematically under the same Fock/tensor refinement later used
for the nonlinear state.  These finite-bosonic thresholds are intentionally
looser than the infinite-Gaussian backend's `1e-6/5e-6` gate because their role
is to validate the explicit truncation/solver mapping before nonlinear use.
They may not be relaxed after results are seen.

## 10. Dense tensor-product solver is not an authorized default

For `N_s` detector states and `K=16` auxiliary modes with a uniform local Fock
dimension `d`, the Hilbert dimension is

```math
D=N_s d^{16}.
```

Even the minimal illustrative `N_s=10,d=2` case has

```text
D = 655,360
D^2 = 429,496,729,600 density-matrix elements
~6.87 TB for complex128 density storage alone.
```

A uniform `d=3` tensor product is already astronomically larger.  Therefore a
naive explicit full-density-matrix tensor product is rejected as the default
nonlinear implementation before any result is seen.

A structured representation (for example an MPO/MPS/trajectory formulation or
another solver whose cost exploits the accepted chain/coupled-mode structure)
must be justified by the harmonic numerical preflight before nonlinear C.1 is
run.

## 11. Two-stage numerical freeze

This document freezes the **physics and acceptance metrics** now.

Before any nonlinear rank-16 evolution, a separate harmonic-only numerical
preflight must:

1. deterministically regenerate and archive the accepted optimized rank-16 and
   rank-24 `(H_b,Gamma,g)` matrices;
2. verify they reproduce the accepted harmonic result;
3. report `Gamma` structure/conditioning, auxiliary occupations, harmonic Fock
   tails, and direct-product scaling;
4. choose the structured solver class and freeze the exact detector basis,
   auxiliary Fock dimensions, tensor/bond controls, and solver tolerances to be
   used in the first nonlinear matrix.

That second freeze may use only harmonic/preflight information.  It may not use
any nonlinear C.1 state, trajectory, basin probability, or nonlinear convergence
result.

## 12. Decision rule

Gate C.1 passes only if **all** of the following pass simultaneously:

```text
physicality
left-basin metastability
late-time stationarity
nonlinear detector-basis convergence
auxiliary Fock/local convergence
solver/tensor convergence
rank16 -> rank24 bath-order control
finite-bosonic harmonic regression
```

Failure of one axis blocks Gate C.1.  No threshold is to be weakened, no rank is
to be switched, and no photon pulse is to be introduced to rescue a failure.

If a computational representation is demonstrably infeasible before nonlinear
results are generated, it may be closed and replaced by a different structured
solver **only after a new numerical-preflight freeze is committed**.

## 13. Gate status at freeze

```text
Gate A                              PASS
Gate B                              PASS
Independent harmonic solver        PASS
Gate C.1 nonlinear cold/metastable ACTIVE / acceptance frozen
Gate C.2 nonlinear pulse/capture    BLOCKED
Gate D/E                            BLOCKED
Publication                         NO-GO
```
