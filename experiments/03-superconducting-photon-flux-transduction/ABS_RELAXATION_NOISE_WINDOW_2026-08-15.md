# Experiment 03 — ABS Relaxation / Noise Window — 2026-08-15

## Purpose

The finite-CPR-response and intrinsic-admittance gates are linked microscopically, but the linkage is subtler than “faster relaxation always means more noise.” A simple relaxing Andreev-occupation mode shows that dissipation and occupation-noise power in the phase band are maximal when the relaxation time is comparable to the inverse phase frequency.

This is a generic linear-response orientation result, not a microscopic graphene-JJ prediction and not a novelty claim.

---

## 1. Relaxing occupation mode

Let `delta n` denote a fluctuation of an Andreev occupation around thermal equilibrium. The minimal stationary Langevin model is

```math
\dot{\delta n}
=-\frac{\delta n}{\tau}
+\xi(t),
```

with equilibrium variance

```math
\langle(\delta n)^2\rangle=\sigma_n^2.
```

Detailed balance for the classical Markov form requires white drive

```math
\langle\xi(t)\xi(t')\rangle
=\frac{2\sigma_n^2}{\tau}\delta(t-t').
```

The two-sided occupation PSD is therefore

```math
\boxed{
S_n(\omega)
=\frac{2\sigma_n^2\tau}
{1+\omega^2\tau^2}.
}
```

The integrated variance is independent of `tau`, as it must be:

```math
\int\frac{d\omega}{2\pi}S_n(\omega)=\sigma_n^2.
```

Changing the relaxation time redistributes fluctuation power in frequency rather than changing the equilibrium variance for free.

---

## 2. Current-noise consequence

For one Andreev contribution

```math
I_s=I_A^{(0)}(\phi)[1-2n],
```

small occupation fluctuations give

```math
\delta I=-2I_A^{(0)}\delta n.
```

Hence

```math
\boxed{
S_I^{(n)}(\omega)
=4[I_A^{(0)}]^2S_n(\omega)
=\frac{8[I_A^{(0)}]^2\sigma_n^2\tau}
{1+\omega^2\tau^2}.
}
```

At a fixed detector frequency `omega`, the in-band occupation-noise scale behaves as

```text
tau -> 0:       S_I(omega) ~ tau -> 0
tau ~ 1/omega:  largest in-band contribution
tau -> infinity:S_I(omega) ~ 1/(omega^2 tau) -> 0.
```

The slow limit does not solve Experiment 03 because occupations then fail to track the hot equilibrium CPR.

---

## 3. Dissipative susceptibility has the same window

If the equilibrium occupation target changes by `delta n_eq`, the linear response is

```math
\boxed{
\frac{\delta n(\omega)}{\delta n_{eq}(\omega)}
=\frac{1}{1-i\omega\tau}.
}
```

Its lag/dissipative quadrature contains

```math
\boxed{
\frac{\omega\tau}{1+\omega^2\tau^2}.
}
```

This is maximal at

```math
\boxed{\omega\tau=1.}
```

and decreases in both the fast and frozen limits.

Therefore causality/FDT do not imply that arbitrarily fast equilibration must produce maximal microwave loss at the phase frequency. In a simple relaxation model, sufficiently fast kinetics push the occupation fluctuation spectrum above the detector band while allowing the occupations to track the instantaneous equilibrium target.

---

## 4. Experiment-03 scale

The retained phase frequency is roughly

```text
f_c ~20–30 GHz
```

depending on the current circuit branch.

Thus the crossover

```math
\tau\sim\omega_c^{-1}
```

is of order

```text
~5–8 ps
```

for `1/omega`, or equivalently tens of picoseconds if one compares to a full oscillation period `2pi/omega`.

The exact numerical definition must match the kinetic transfer function; do not substitute `1/f` for `1/omega` casually.

This makes the several-picosecond occupation-response range particularly important: it is simultaneously where CPR lag becomes dynamically significant and where a Debye-like relaxing occupation mode produces its largest dissipative quadrature at the phase frequency.

---

## 5. Design interpretation

There are three kinetic regimes:

### A. Fast adiabatic occupation response

```math
\omega_c\tau_{ABS}\ll1.
```

Then

```text
CPR follows T_e(t) with small lag;
in-band occupation noise from this simple mode scales downward with tau;
thermal switching can remain prompt.
```

This is the desirable microscopic regime for the present mechanism.

### B. Intermediate relaxation

```math
\omega_c\tau_{ABS}\sim1.
```

Then

```text
CPR has substantial phase lag;
dissipative susceptibility is maximal;
occupation-noise power overlaps the phase band strongly;
reformation phase matching can be badly disturbed.
```

This is the dangerous regime.

### C. Frozen occupations

```math
\omega_c\tau_{ABS}\gg1.
```

Then in-band relaxation loss can become small again, but

```text
the hot equilibrium CPR is not reached on the write timescale;
thermal barrier suppression is delayed or absent;
the intended detector mechanism changes qualitatively.
```

Thus low dissipation in the frozen limit is not useful for the current thermal-CPR latch.

---

## 6. Limits of the closure

The single-mode Langevin model omits

```text
multiple ABS with different tau_j,
continuum quasiparticles,
parity constraints,
Landau-Zener transitions,
phase-dependent matrix elements,
non-Markovian relaxation,
quantum rather than classical occupation noise.
```

It is therefore only an organizing principle.

The quantitative gate remains:

```text
1. determine the tolerated effective tau_CPR numerically;
2. calculate or bound microscopic tau_j and Y_JJ(omega,phi,T_e);
3. verify that the microscopic spectrum lies in the fast-adiabatic region rather than the intermediate-loss window.
```

---

## Strongest conclusion

There is no generic “fast response versus noise” impossibility at the level of a simple relaxing Andreev occupation. The problematic region is specifically when the occupation relaxation rate overlaps the phase-dynamics band.

Therefore a very fast microscopic ABS relaxation channel could, in principle, satisfy both

```text
rapid equilibrium-CPR tracking
+
small occupation-noise spectral density at the phase frequency.
```

Whether graphene proximity junctions in the current hot phase/temperature regime actually occupy that regime is an open microscopic question.

**GO for continued theory. NO-GO for manuscript.**
