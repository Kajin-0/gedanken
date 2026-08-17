# Experiment 03 — coupled-Lindblad harmonic p12/p16 result

Date: 2026-08-17

Evaluated against the criteria frozen in
`COUPLED_LINDBLAD_HARMONIC_ACCEPTANCE_2026-08-17.md` at commit
`7b17d97199dcfd91758e1808f92e76a7553557b0` before this workflow ran.

## Provenance

```text
workflow: .github/workflows/experiment03-coupled-lindblad-harmonic-gaussian.yml
run:      32033673843
job:      95399068042
commit:   7fb357640359135887c04f8e31c5c85296b50638
```

Automatic classification:

```text
GAUSSIAN_ACCEPTANCE mandatory=1 trend=1 improvement25=1 finalpass=0 authorize_p24_p32=1
COUPLED_LINDBLAD_HARMONIC_AUTHORIZE_P24_P32
```

## Exact reference

System-only Gaussian reference basis `dim=16`:

```text
basis error = 0 at displayed precision
sigma_x = 3.989969857213e-2
sigma_u = 4.264669020793e-2
sigma0  = 4.011572619770e-2
nbar    = 2.868335041480e-2
r       = 3.329044903832e-2
```

## Implementation identities

Both p12 and p16 pass the predeclared convention/implementation checks.

```text
                               p12                p16
BCF real-drift identity        1.776e-13          1.033e-12
aux vacuum Lyapunov residual   3.257e-17          2.818e-17
Omega_iso/omega_c              1.131080565620     1.131080565620
frequency relative error       1.764e-11          1.764e-11
full drift max Re(lambda)     -6.03636e-2        -6.03550e-2
steady Lyapunov residual       2.388e-15          2.750e-15
minimum full symplectic nu     0.5                 0.5
```

Thus the real-quadrature representation reproduces the published coupled bath
BCF, the Lindblad vacuum noise normalization, the repository counterterm/system
frequency, and a stable physical Gaussian steady state.

## Reduced harmonic state

```text
                                p12                 p16
sigma_x rel error              +2.066928e-4        +1.097141e-4
sigma_u rel error              +2.009199e-4        +1.065308e-4
max width error                 2.066928e-4         1.097141e-4
half nuclear discrepancy        2.036443e-4         1.080427e-4
normalized q-p covariance       2.52e-15            1.31e-14
system symplectic nu            0.5288988704         0.5287976817
system nbar_eff                 0.0288988704         0.0287976817
Gaussian rho reconstruction     1.27e-15            2.41e-15
```

The p16 state improves over p12 in both predeclared state metrics by roughly a
factor of 1.9.  The cross covariance remains numerically zero, as required by
the exact equilibrium symmetry.

## Interpretation

This is strong evidence that the physical coupled-Lindblad approximation is
converging to the same exact direct-port harmonic equilibrium rather than merely
matching a time-domain BCF norm.

However p16 does **not** meet the unchanged final harmonic standards:

```text
required max width error      < 1e-6
p16                            1.097e-4

required half nuclear         < 5e-6
p16                            1.080e-4
```

Therefore the independent harmonic solver is not yet accepted.

The predeclared higher-order rule is satisfied (`improvement25=1`), so exactly
one final matrix is authorized:

```text
p24
p32
```

No p20/p28/post-hoc order scan is authorized.

The p24/p32 matrix must retain all implementation/physicality checks and
continue toward the exact FDT state.  Final acceptance thresholds remain
unchanged.

If p32 still fails the final thresholds, or p24->p32 reverses convergence, the
Padé-coordinate coupled-mode route is closed and the next method is a direct
positive-real/coupled realization of the exact physical spectrum.

## Gate status

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / final p24-p32 coupled Gaussian matrix authorized
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
