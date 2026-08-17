# Experiment 03 — coupled-Lindblad harmonic-state acceptance

Date: 2026-08-17

## Scope

This file freezes the harmonic system-dynamics acceptance criteria **before**
computing the reduced equilibrium state of the p12/p16 physical coupled-Lindblad
baths.

The bath-level p12/p16 criteria were frozen separately and passed in workflow
run `32032743486` / job `95396204874`.

This is still Gate C.1 recovery.  No nonlinear detector dynamics are authorized.

## Exact harmonic formulation

The system Hamiltonian and counterterm are exactly the same ones used in the
accepted direct-port harmonic Gate-B calculation:

```text
H_s/(hbar omega_c) = a^dag a + 1/2 + lambda_ct x^2
x = sigma0 (a + a^dag)
lambda_ct = [Phi_bar^2/hbar * G*omega_D/(2 sqrt(2))]/omega_c
```

For the physical coupled bath, use the Huang et al. Lindblad realization
corresponding to

```text
C_c(tau) = g^dag exp(-i K tau) g
K = H_A - i Gamma
```

with auxiliary vacuum and system-bath Hamiltonian

```text
H_SA = x * sum_k (g_k b_k^dag + conj(g_k) b_k).
```

All quantities use dimensionless time `tau=omega_c t`, exactly as in the
high-order bath audit.

Because the system and all auxiliaries are harmonic and the Lindblad operators
are linear, this enlarged problem is Gaussian.  The primary harmonic benchmark
shall therefore solve the real quadrature drift/diffusion Lyapunov equation
exactly.  This removes auxiliary Fock truncation from the harmonic benchmark;
it does **not** waive explicit local/Fock cutoff convergence for later nonlinear
system dynamics.

## Mandatory implementation identities

Before interpreting the system equilibrium, each order must pass:

1. **BCF drift identity** — the real-quadrature auxiliary drift with vacuum
   covariance must reconstruct `g^dag exp(-i K tau) g` on the existing audit
   grid with max relative discrepancy `< 1e-10`.
2. **Vacuum fixed point** — with system coupling removed, the auxiliary
   covariance `I/2` must satisfy its Lyapunov equation with scaled residual
   `< 1e-12`.
3. **Hamiltonian frequency** — the isolated one-mode system quadratic matrix
   must reproduce the repository system-mode frequency
   `Omega_s/omega_c = 1.1310805656` within `2e-9` relative.
4. **Hurwitz stability** — the full p12 and p16 Gaussian drift matrices must
   have all eigenvalues with strictly negative real part; require
   `max Re(lambda) < -1e-8`.
5. **Steady Lyapunov residual** — scaled Frobenius residual
   `||A V + V A^T + D||_F / max(||D||_F,1) < 1e-10`.
6. **Quantum physicality** — the minimum symplectic eigenvalue of the full
   steady covariance must be `>= 0.5 - 1e-9`.

Any failure stops the coupled-mode system branch for a convention/implementation
audit.  Do not tune physical parameters to repair it.

## p12 -> p16 convergence requirement

For the reduced system Gaussian state, report:

- sigma_x and relative error to exact direct-port FDT width;
- sigma_u and relative error;
- symmetrized q-p covariance;
- one-mode symplectic eigenvalue / effective occupation;
- finite-system Gaussian density matrix and
  `0.5 * ||rho_coupled - rho_exact||_1` in a system-only basis whose exact
  Gaussian reference width error is `<1e-7`.

The p16 state must improve over p12 in **both**:

```text
max absolute relative width error
half nuclear-norm discrepancy
```

A reversal blocks higher-order escalation even if the bath-level fit improved.

## Final harmonic promotion thresholds

These are inherited from Gate B and are **not relaxed** for the independent
solver:

```text
exact finite-system Gaussian reference width error < 1e-7
max relative FDT width error                     < 1e-6
0.5 * nuclear norm(rho-rho_exact)                < 5e-6
```

The Gaussian solution is exactly positive if the physicality checks pass, so
there is no HEOM-style negative-mass allowance to consume.

Also require

```text
|V_qp|/sqrt(V_qq V_pp) < 1e-5
```

at the final accepted order, because the exact equilibrium has zero
symmetrized q-p covariance.

## Higher-order authorization rule

If p16 does not meet the final harmonic thresholds but:

1. all mandatory implementation/physicality checks pass;
2. p16 improves both width and nuclear discrepancy over p12;
3. the larger of those two p16 errors is at least 25% smaller than p12;

then p24 and p32 bath orders are authorized as the **last predeclared
high-order Gaussian matrix**.  No post-hoc p20/p28 scanning.

The p24/p32 matrix must retain all physicality checks and converge toward the
same exact FDT state.  Final promotion still uses the unchanged Gate-B
thresholds above.

If p12->p16 is nonmonotone, or p24->p32 fails coherent convergence, abandon the
Padé-coordinate coupled-mode route and move to a direct positive-real/coupled
realization of the exact physical spectrum.

## Gate status at freeze

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / coupled-Lindblad harmonic-state benchmark
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
