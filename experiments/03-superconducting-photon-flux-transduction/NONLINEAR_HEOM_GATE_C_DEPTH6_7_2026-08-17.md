# Experiment 03 — Nonlinear HEOM Gate C.1 depth-6/7 checkpoint — 2026-08-17

## Status

This checkpoint continues `NONLINEAR_HEOM_GATE_C_PILOT_2026-08-16.md`.

```text
Gate A: PASS
Gate B: PASS — harmonic HEOM method validation
Gate C.0: PASS — restricted left-well phase-DVR construction
Gate C.1: ACTIVE — raw hierarchy failed depth-seven discriminator; closure path active
Gate C.2: BLOCKED
Gate D: BLOCKED ON C
Gate E: BLOCKED
```

No detector-capture or efficiency claim is authorized by this checkpoint.

## Dimension-stability diagnosis at depth 5

Run `31986105536` tested integration-step and system-basis alternatives.  The
capped-BDF dim=10, Npade=4, depth=5 trajectory reproduces the same delayed
nonphysical growth seen in the original pilot even with `max_step=0.1`:

```text
tau=20  eigmin=-5.599221592e-05  negmass=7.421723834e-05
tau=30  eigmin=-1.396411286e-03  negmass=1.819971704e-03
tau=40  eigmin=-2.583710669e-02  negmass=4.495699843e-02
tau=50  eigmin=-6.876219358e-01  negmass=9.110850781e-01
tau=60  eigmin=-7.493240721e+00  negmass=1.513858470e+01
```

The growth is therefore not explained by a large adaptive ODE step.  Together
with the converged DVR residuals and earlier Padé/domain controls, the leading
classification is a finite-tier HEOM generator/truncation instability whose
onset depends on system-basis dimension.

The attempted dim=10 LSODA control is not a physical counterexample: LSODA
failed during solver setup with a `MemoryError` while attempting an approximately
63.6-GiB work allocation.  No LSODA trajectory was produced.

## Depth-six basis matrix

Workflow:

```text
run 31986255310
head aa179da875569364d6402036f40aef3ebc4f5ba0
Npade=4
hierarchy depth=6
bath exponents=6
ADO estimate=924
xmin=-3.8
Ngrid=2200
BDF rtol=2e-7 atol=2e-9
```

### dim=8

```text
job 95261697097
max DVR residual = 3.136e-13 K
final trace = 1.000000000000 + 6.93e-17 i
anti-Hermitian residual = 1.745e-16
min eig(rho) = -1.353321296e-06
negative mass = 2.015619849e-06
<y> = +2.6117013672e-03
sigma_y = 4.0115201184e-02
bare-H0 energy = 3.0451757786e-02
top retained population = -1.383074015e-07
late absolute drift = 4.305332874e-07
runtime = 247.904 s
```

### dim=9

```text
job 95261697114
max DVR residual = 5.467e-14 K
final trace = 1.000000000000 - 8.88e-17 i
anti-Hermitian residual = 1.451e-16
min eig(rho) = -1.572538337e-06
negative mass = 2.416820495e-06
<y> = +2.6117258800e-03
sigma_y = 4.0115227579e-02
bare-H0 energy = 3.0451914122e-02
top retained population = +1.581950469e-07
late absolute drift = 4.924083451e-07
runtime = 418.281 s
```

The dim=8 and dim=9 stationary observables agree closely:

```text
Delta <y>       = +2.45128e-08
Delta sigma_y   = +2.6395e-08
Delta bare-H0 E = +1.56336e-07
```

That agreement is now explicitly known to be a false convergence signal for the
raw hierarchy: depth seven destabilizes dim=9.

### dim=10

```text
job 95261697033
max DVR residual = 2.642e-13 K

tau=20  eigmin=-2.495055498e-06  negmass=4.069040323e-06
tau=40  eigmin=-1.043070680e-05  negmass=1.488160057e-05
tau=80  eigmin=-4.641428599e-04  negmass=7.241590800e-04
tau=120 eigmin=-1.668484376e-02  negmass=2.891853172e-02
tau=160 eigmin=-6.060754406e-01  negmass=1.269098121e+00

final <y> = +4.7832208889e-02
final sigma_y = 1.0523021058e-01
final bare-H0 energy = -7.7066483568e-01
late absolute drift = 7.999787770e-01
```

Thus depth 6 stabilizes dim=9 but not dim=10.  The instability is delayed relative
to depth 5, which is consistent with hierarchy-depth dependence rather than a
physical instability of the nonlinear well.

## Depth-seven discriminator

Files:

```text
calculations/heom_nonlinear_depth7_basis.py
.github/workflows/experiment03-heom-nonlinear-depth7-basis.yml
```

Commits:

```text
1e48a85fcbf0142793734969b807d12da4b58c9f  add calculation
b5f4211e2dd7b6bdfa9c752fefa4c0968de4f24a  add/run workflow
```

Workflow run:

```text
31996495432
```

Predeclared matrix:

```text
dim=9,  Npade=4, depth=7
dim=10, Npade=4, depth=7
bath exponents=6
ADO estimate=1716
same physical model, domain, time grid, counterterm, and solver tolerances
```

The acceptance/disposition rule was frozen separately in
`NONLINEAR_HEOM_GATE_C1_ACCEPTANCE_RULE_2026-08-17.md` at commit
`67e13cc0f58e0a164a11d3488c7dc38614d3b6b8`, before either depth-seven result
was read.

### dim=9 result — decisive non-monotone failure

Job `95288972802` completed after 859.624 s.  DVR basis residual remained
`5.335e-14 K`, so the instability is not a loss of the restricted-well basis
solution.

```text
tau=0
  eigmin   = +3.923755752e-16
  negmass  = 0

tau=10
  eigmin   = -7.980838472e-07
  negmass  = 1.112668159e-06

tau=20
  eigmin   = -9.422160182e-07
  negmass  = 1.133892458e-06

tau=40
  eigmin   = -2.837679057e-06
  negmass  = 3.491257709e-06

tau=80
  eigmin   = -1.127755439e-04
  negmass  = 1.453198877e-04

tau=120
  eigmin   = -4.175887342e-03
  negmass  = 5.861670700e-03

tau=160
  eigmin   = -1.543265832e-01
  negmass  = 2.199325372e-01
```

Final diagnostics:

```text
trace                  = 1.000000000000 - 9.14e-18 i
anti-Hermitian residual= 5.620e-15
<y>                    = +1.9759349760e-02
sigma_y                = 5.3526298014e-02
bare-H0 energy         = 7.1409851433e-02
top retained population= 8.243826365e-02
late absolute drift    = 3.984810846e-02
```

This is decisive under the frozen rule.  Dim=9 was stationary at raw depth 6 but
becomes strongly nonphysical at raw depth 7.  Therefore the hard-cutoff hierarchy
is **non-monotone in depth** for this nonlinear restricted-well problem.  The
apparently excellent dim8/dim9 depth-six moment agreement cannot be promoted to a
convergence claim.

The dim=10 depth-seven job may still be retained as provenance when it finishes,
but it cannot reverse this disposition: the predeclared raw-depth route has
already failed because its nominally stable dim=9 control destabilized when depth
was increased.

## Consequence for Gate C.1

Per the frozen acceptance rule:

```text
DO NOT run raw dim10/depth8 as an acceptance search.
DO NOT relax positivity because low-order moments looked converged at depth6.
DO NOT select the apparently stable raw depth6 state as the physical answer.
```

The next authorized route is a controlled hierarchy closure/terminator benchmark,
first in the harmonic problem where an exact FDT state is available as an oracle,
and only then in the nonlinear restricted-well problem.

The active harmonic closure implementation is a Schur-complement-type boundary
correction assembled directly from QuTiP's own depth-(d+1) HEOM generator blocks,
so no bath coefficient/scaling convention is re-derived by hand.  Its retained
block has been verified to reproduce QuTiP's native depth-d generator exactly.

Current disposition:

```text
Gate A: PASS
Gate B: PASS — original raw harmonic HEOM method validation
Gate C.0: PASS — restricted left-well phase-DVR construction
Gate C.1: ACTIVE — raw hierarchy rejected as a converged nonlinear solver;
                  controlled closure validation active
Gate C.2: BLOCKED
Gate D: BLOCKED ON C
Gate E: BLOCKED
```
