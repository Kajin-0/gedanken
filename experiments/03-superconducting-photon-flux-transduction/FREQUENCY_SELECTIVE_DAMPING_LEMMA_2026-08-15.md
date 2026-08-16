# Experiment 03 — Frequency-selective damping feasibility lemma — 2026-08-15

## Status

**Derived filter-level lemma. Not a detector theorem and not novelty-audited.**

This result formalizes why a steeper passive bath rolloff can resolve the competing requirements of weak damping during launch and strong damping during capture/recovery.

## 1. Roll-off family

Consider the dissipative admittance family

\[
\operatorname{Re}Y(\omega)
=\frac{G_0}{1+(\omega/\omega_D)^p},
\qquad p>0.
\]

The one-pole Drude model has `p=2`. The current passive two-pole RLC network has

\[
\operatorname{Re}Y(\omega)
=\frac{1/R}{1+(\omega/\omega_D)^4},
\]

so `p=4`.

## 2. Two-frequency design requirement

Let

- `omega_C` be a characteristic frequency where at least conductance `G_C` is required for useful capture/recovery damping;
- `omega_L > omega_C` be a characteristic launch frequency where conductance must not exceed `G_L`;
- `r = G_C/G_L > 1` be the required damping selectivity;
- `q = omega_L/omega_C > 1` be the dynamical frequency separation.

We seek a choice of `G0` and `omega_D` such that

\[
\operatorname{Re}Y(\omega_C)\ge G_C,
\qquad
\operatorname{Re}Y(\omega_L)\le G_L.
\]

Writing

\[
x=(\omega_C/\omega_D)^p,
\]

the conditions require

\[
G_0\ge G_C(1+x),
\]

and

\[
G_0\le G_L(1+q^p x).
\]

A feasible `G0` therefore exists iff

\[
r(1+x)\le1+q^p x.
\]

For `r>1`, this can have a nonnegative solution `x` iff

\[
\boxed{q^p>r}.
\]

Equivalently,

\[
\boxed{q>r^{1/p}}.
\]

When this condition holds, one valid cutoff range is obtained from

\[
x\ge\frac{r-1}{q^p-r},
\]

or

\[
\boxed{
\frac{\omega_D}{\omega_C}
\le
\left(\frac{q^p-r}{r-1}\right)^{1/p}
}.
\]

The DC conductance `G0` must then lie in the nonempty interval

\[
G_C(1+x)\le G_0\le G_L(1+q^p x).
\]

## 3. Equivalent maximum-selectivity statement

At fixed `q`, the conductance selectivity is

\[
\mathcal S(x)
=\frac{\operatorname{Re}Y(\omega_C)}{\operatorname{Re}Y(\omega_L)}
=\frac{1+q^p x}{1+x}.
\]

For `q>1`, this is monotone increasing in `x` and

\[
\boxed{\mathcal S_{\max}=q^p}
\]

as the cutoff is moved below both characteristic frequencies.

Thus a rolloff exponent `p` converts dynamical frequency separation into damping selectivity with power `p`.

## 4. Drude versus the current two-pole bath

For the same required selectivity `r`,

\[
q_{\min}^{\rm Drude}=r^{1/2},
\qquad
q_{\min}^{\rm two\ pole}=r^{1/4}.
\]

Example: for a tenfold damping contrast (`r=10`),

```text
Drude p=2:        q_min = sqrt(10)      ~= 3.16
quartic p=4:      q_min = 10^(1/4)      ~= 1.78
```

This gives a concrete architectural reason that the quartic passive environment can outperform the one-pole Drude environment when the launch and recovery spectra are separated only modestly.

## 5. Detector interpretation and limitations

This lemma constrains **pointwise frequency-domain conductance requirements**. The real photon latch is nonlinear and nonstationary; its launch and capture stages have broadband spectra and the relevant performance metric is an integral over the trajectory, not two delta-function frequencies.

Therefore:

- do not identify `omega_L` and `omega_C` by fiat;
- extract or bound the stage-resolved spectral content of the actual phase trajectory;
- use the exact passive energy identity as the final check;
- do not claim that `q^p>r` alone guarantees photon capture.

The deterministic dissipation partition currently supports the qualitative mechanism: the strongest two-pole candidates dissipate most resistor energy after first favored-side crossing and before well reformation, while excessive low-R damping shifts a much larger fraction into the launch stage and delays crossing.

## 6. Next test

Compute stage-resolved spectra of the deterministic phase velocity and the corresponding dissipative weighting

\[
\operatorname{Re}Y(\omega)|\tilde v(\omega)|^2
\]

for

1. pre-cross launch;
2. crossing-to-reformation capture.

The purpose is to determine whether the actual nonlinear trajectory supplies a meaningful `q=omega_L/omega_C` that explains the observed R80/high-fidelity lobe.

No novelty claim is authorized.
