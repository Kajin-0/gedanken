# Experiment 03 — Phase-DVR Safe-Plateau Checkpoint — 2026-08-16

## Purpose

Validate the one-dimensional phase-coordinate quantum basis needed for the next exact/open-system capture calculation across the full safe reduced-model tilt plateau `delta=.212-.213`.

This checkpoint validates only the **phase Hamiltonian discretization and metastable-well initialization basis**. It does not compute open-system quantum capture probability.

## Hamiltonian

With

```math
q=\bar\Phi x,
```

the isolated phase Hamiltonian is

```math
H_x(T)
=-\frac{\hbar^2}{2C\bar\Phi^2}\frac{d^2}{dx^2}+U(x,T).
```

The cold metastable initialization benchmark restricts the domain to the left well with a Dirichlet wall at the separating cold saddle. The full tilted-double-well spectrum is also calculated on a large symmetric box.

## Numerical repair retained

A previous raw ARPACK call using `eigsh(...,which='SA')` produced spurious interior Ritz values because the finite-difference kinetic diagonal is tens of kelvin while the physical low spectrum is sub-kelvin.

The validated implementation uses:

```text
eigsh(H, sigma=0, which='LM')
```

with explicit eigenpair residual checks and integral normalization of the eigenvectors.

The `.212` electrical scale was also corrected to the certified total-dark root

```text
r_Gamma(.212)=10.6229699624
```

rather than the older stale value.

## Validation workflow

```text
workflow: .github/workflows/experiment03-phase-dvr-basis.yml
run:      31972799107
head:     eb90f05976d103c0ff9039fc4f98073cf166abb1
status:   SUCCESS
matrix:   delta=.21200,.21250,.21300
```

All three jobs passed.

## Cold local-well metrics

| delta | r | C (pF) | f_m (GHz) | `hbar omega_m/kB` (K) | nbar(20 mK) | DVR `dE01/kB` (K) | DVR/harmonic | transition-domain shift (K) | max eig. residual (K) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| .21200 | 10.6229699624 | 24.262211 | 1.9844267 | 0.09523746 | 8.6233e-3 | 0.094183653 | 0.98893493 | 1.290e-5 | 1.504e-13 |
| .21250 | 10.8855782110 | 25.476600 | 1.9328742 | 0.09276333 | 9.76995e-3 | 0.091747173 | 0.98904572 | 1.288e-5 | 1.080e-13 |
| .21300 | 11.2051409652 | 26.994365 | 1.8741430 | 0.08994468 | 1.12653e-2 | 0.088973695 | 0.98920467 | 1.287e-5 | 1.717e-13 |

The lowest left-well spacing remains only about `1.08-1.11%` below the local harmonic spacing across the plateau, which is consistent with weak local anharmonicity rather than a basis pathology.

The restricted spectrum is highly converged with respect to the left domain. The maximum change in the first eight transition energies between the two largest domains is only approximately

```text
1.29e-5 K.
```

## Full-box convergence

The full tilted-well calculation used `X=3.2,N=1800` and `X=3.8,N=2200` boxes. The maximum shift among the first 30 transition energies was

| delta | max transition shift (K) |
|---:|---:|
| .21200 | 2.487484e-3 |
| .21250 | 2.490760e-3 |
| .21300 | 2.494479e-3 |

all within the predeclared `3e-3 K` gate.

The global cold low-energy states localize predominantly in the deeper right well, as expected for the tilted double well. Therefore the global Gibbs ground state is **not** the correct pre-photon initialization for a detector intentionally prepared in the metastable left well.

## Photon-hot topology at 14 um, A=500 um^2

For all three tilts,

```text
T_ad(14 um, 500 um^2)=0.37253725 K.
```

This exceeds the static left-well fold temperatures:

```text
delta=.21200: T_f=0.27853028 K
delta=.21250: T_f=0.27713437 K
delta=.21300: T_f=0.27573184 K
```

and the hot stationary-point search contains only the right minimum. In every matrix job:

```text
hot_left_min_exists = False.
```

Thus the photon-hot isolated phase Hamiltonian is single-well in this screening case; the nontrivial quantum question is the **time-dependent open-system passage and recapture during cooling**, not tunneling through a surviving hot static barrier.

## Interpretation

Three points are now numerically secure:

1. the repaired shift-invert phase-DVR basis is accurate across the complete `.212-.213` safe plateau;
2. the metastable cold left-well restricted basis is a controlled initialization basis, with the first spacing tracking the harmonic plasma mode to about 1%;
3. at the representative 14-um, 500-um2 photon pulse, the left well is statically annihilated for the entire plateau.

The appropriate next quantum calculation should therefore initialize a **metastable left-well quasistationary density operator conditioned on no prior escape**, couple it to the same reaction-coordinate/resistor bath used elsewhere in the project, evolve it under the time-dependent thermal potential, and calculate final basin occupation after the left well reforms.

## Claim boundary

This checkpoint does not establish:

- exact quantum detection efficiency;
- detailed-balance-consistent open-system dynamics;
- a physical metastable lifetime beyond the independently calculated dark rate;
- optical absorptance;
- final capture after the full bath is quantized.

## Disposition

```text
PHASE-DVR BASIS / METASTABLE INITIALIZATION GATE: CLOSED / PASS
```
