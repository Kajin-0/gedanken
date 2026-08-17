# Experiment 03 — Nonlinear HEOM Gate C.1 depth-6/7 checkpoint — 2026-08-17

## Status

This checkpoint continues `NONLINEAR_HEOM_GATE_C_PILOT_2026-08-16.md`.

```text
Gate A: PASS
Gate B: PASS — harmonic HEOM method validation
Gate C.0: PASS — restricted left-well phase-DVR construction
Gate C.1: ACTIVE — nonlinear cold left-well HEOM convergence
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

That agreement is encouraging but is not sufficient to establish system-basis
convergence because dim=10 does not remain physical at the same hierarchy depth.

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

## Active depth-seven discriminator

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

Interpretation rule:

1. If dim=10 becomes stationary/physical and agrees with dim=9 while the
   depth-6 -> depth-7 changes are small, hierarchy truncation was the limiting
   axis and Gate C.1 can be assessed against an explicit acceptance threshold.
2. If dim=10 remains unstable while dim=9 remains stable, do not promote C.1 and
   do not infer that dim=9 is a converged physical basis.  Stop blind basis
   extrapolation and evaluate a controlled hierarchy terminator/closure.
3. If both dim=9 and dim=10 become unstable at depth 7, treat the raw hard-cutoff
   hierarchy as non-monotone and return immediately to closure/stability analysis.

The positivity criterion is not to be relaxed merely because low-order moments
appear converged.
