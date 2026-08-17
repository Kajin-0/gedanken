# Experiment 03 — finite Padé bath spectral-positivity rejection

Date: 2026-08-17

## Purpose

This note records the prerequisite physicality test for using the existing finite direct-port Padé bath expansions as completely positive interacting-pseudomode models.

The result is negative: the finite p4, p5, and p8 exponential correlations are excellent controlled approximations in the time/frequency window relevant to the present HEOM/TEMPO calculations, but they are **not globally positive stationary quantum correlations**.  Therefore they cannot be passed directly into a theorem that requires a physical bath correlation and then interpreted as a CPT pseudomode embedding.

This does not invalidate the underlying direct-port circuit bath, which is physical by construction.  It distinguishes the exact bath from its finite rational Bose approximation.

## Test

Script:

`calculations/direct_port_pade_spectral_positivity.py`

Workflow run:

```text
32006421611
job 95316723872
```

For the finite correlation

```text
C_N(t) = sum_k c_k exp(-gamma_k t), t>=0
C_N(-t)=C_N(t)*
```

the exact two-sided unsymmetrized Fourier spectrum is

```text
S_N(omega) = 2 Re sum_k c_k/(gamma_k-i omega).
```

A Hermitian stationary bath correlation must have `S_N(omega)>=0` for all real `omega`.

The scan covered a dense core `|omega/omega_c|<=20` and logarithmic wings through `|omega/omega_c|=1e6`, with root/minimum refinement.

## Results

### p4

```text
first zero: omega/omega_c = -2.64476601346
minimum:    S_N/S(0)      = -7.622954889e-5
at:         omega/omega_c = -11.7879237504
```

Representative values:

```text
x=-4    Sfit/S0 = -6.95723e-6     exact = +2.60157e-10
x=-8              -5.84336e-5              +1.74167e-19
x=-12             -7.61907e-5              +2.75758e-28
x=-100            -1.27039e-6              +4.88910e-213
```

### p5

```text
first zero: omega/omega_c = -3.20140405858
minimum:    S_N/S(0)      = -2.397304383e-5
at:         omega/omega_c = -17.4163921468
```

At low/relevant frequencies p5 is extremely accurate, but its negative-frequency rational tail still becomes negative.

### p8

```text
first zero: omega/omega_c = -4.87143305783
minimum:    S_N/S(0)      = -1.905254745e-6
at:         omega/omega_c = -40.7500726905
```

At `x=-4`, p8 still matches the tiny exact positive spectrum closely:

```text
Sfit/S0  = +2.6007484e-10
Sexact/S0= +2.6015699e-10
```

but by `x=-8` it has crossed negative:

```text
Sfit/S0 = -1.59605e-9
Sexact/S0 ~ 1.74e-19.
```

Thus increasing Padé order systematically pushes the unphysical region outward and reduces its amplitude, but does not restore global positivity.

## Why the violation is structural

The finite exponential spectrum is rational:

```text
S_N(omega)=2 Re sum_k c_k/(gamma_k-i omega).
```

Its large-frequency expansion is

```text
1/(gamma-i omega)
 = i/omega + gamma/omega^2 - i gamma^2/omega^3 - gamma^3/omega^4 + ...
```

For the present direct-port decompositions, the lower contributions cancel to the accuracy expected from the physical high-frequency structure.  The first nonzero controlling term is the `1/omega^3` contribution.  The relevant moment has the same imaginary part for p4, p5, and p8:

```text
Im sum_k c_k gamma_k^2 = +1.110278401054e5
```

so asymptotically

```text
S_N(omega) ~ +const/omega^3.
```

That reproduces the sign of the exact positive-frequency `omega^-3` direct-port tail for `omega -> +infinity`, but an odd inverse power necessarily flips sign for `omega -> -infinity`.

The exact quantum spectrum does not do this: detailed balance makes the large negative-frequency spectrum exponentially smaller while remaining nonnegative.

Therefore a finite rational approximation that retains this positive-frequency odd-power UV tail cannot simultaneously reproduce the exact exponentially suppressed negative-frequency tail and remain globally nonnegative.  The observed p4/p5/p8 violations are the numerical manifestation of that structural mismatch.

## Disposition

**Do not construct a completely positive pseudomode model by treating the existing p4/p5/p8 Padé exponential correlation as a physical BCF.**

Specifically:

1. p4 is globally unphysical beyond `-2.645 omega_c`.
2. p5 is globally unphysical beyond `-3.201 omega_c`.
3. p8 is globally unphysical beyond `-4.871 omega_c`.
4. Higher Padé order can postpone the violation but does not remove the rational-vs-detailed-balance asymptotic conflict.
5. This is not a failure of the underlying passive direct-port environment.
6. It does not invalidate prior HEOM/TEMPO calculations whose convergence was explicitly checked in the relevant time/frequency window.

## What a physical pseudomode fallback would require

A CPT pseudomode route remains possible only if it starts from a **new positivity-constrained approximation to the exact physical spectrum**, rather than reusing the finite Padé BCF as if it were globally physical.

Such a new approximation must be treated as an additional controlled bath approximation and must pass, before any system dynamics:

1. nonnegative spectrum over all real frequency, with analytic asymptotic control;
2. direct comparison to the exact physical unsymmetrized spectrum over the system-relevant band;
3. time-domain correlation comparison against the exact direct-port correlation over the full memory interval required by the solver;
4. KMS/detailed-balance error characterization;
5. counterterm/static susceptibility consistency;
6. harmonic exact-FDT reduced-state benchmark.

Only after those checks could a physical interacting-pseudomode embedding be considered as a scalable independent solver for Gate C.1.

## Current method status

- direct-port exact bath: PHYSICAL / VALIDATED
- finite p4/p5/p8 Padé BCF: CONTROLLED APPROXIMATION, NOT GLOBALLY PHYSICAL
- direct Padé -> CPT pseudomode mapping: REJECTED
- positivity-constrained exact-spectrum pseudomode approximation: NOT STARTED
- direct TEMPO dim2 mapping: VALIDATED
- direct TEMPO scalability to dim7: UNPROVEN / resource concern
- Gate C.1: ACTIVE / still blocked on final harmonic independent-solver validation
- Gate C.2, D, E: BLOCKED
- Publication: NO-GO
