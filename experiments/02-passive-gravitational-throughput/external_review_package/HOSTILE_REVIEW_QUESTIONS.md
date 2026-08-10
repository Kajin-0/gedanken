# Hostile Review Questions

The reviewer is explicitly invited to answer **only the questions relevant to their expertise**. A single concrete failure is more useful than broad comments.

## 1. Historical-priority attack

Can you identify a published theorem, perhaps in gravitational-antenna, mutual-impedance, scattering, reciprocity, cross-section, network, or resonant-mass language, that is mathematically equivalent to

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B)
```

for a passive separated source--receiver system after eliminating `Q`, mode count, individual effective masses/oscillator strengths, and matching parameters?

A citation to an ingredient is not enough; the target is the **complete two-ended inertia closure**.

## 2. Passive-system attack

Does the endpoint representation

```math
A=-iH-\frac12K^\dagger K
```

with selected gravitational port `K_g` faithfully represent a physical compact gravitational antenna over the band of interest? In particular, is there any reason the radiative gravitational continuum must be treated by an unbounded or non-Markov operator in a way that invalidates

```math
\|S_{g\leftarrow u}\|_2^2
\le\operatorname{Tr}(K_g^\dagger K_g)?
```

## 3. Continuum-normalization / double-counting attack

Is the factorization

```math
G_B^\dagger U_RG_A
=\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2}
```

normalized correctly, or has gravitational density of states, solid angle, polarization, or the source/receiver radiation pattern been counted twice or omitted?

Please specifically look for a missing factor of `2`, `2 pi`, `omega`, or a mismatch between amplitude and power normalization.

## 4. Material-resource attack

Within compact nonrelativistic **linear-harmonic matter**, is

```math
\sum_n M A_{Gn}\le\frac{40}{3}I
```

actually sufficient to constrain all quadrupole-active passive degrees of freedom?

Can a legitimate internal coordinate, constrained rotational mode, electronic/collective mode, or nonlocal elastic degree of freedom inside the declared class add gravitational oscillator strength not represented by the displacement-space completeness argument?

## 5. Multimode / bright-mode attack

Can passive hybridization create several simultaneously bright modes whose total gravitational coupling trace exceeds the original endpoint resource?

The manuscript argues that unitary/orthogonal internal mixing preserves

```math
\operatorname{Tr}(G^\dagger G).
```

Tobar--Pikovski--Tobar's multimode bar was used as a concrete stress test because its modal rates contain participation factors whose squared norm sums to the original driven coordinate. Is there a physically relevant multimode construction that evades this trace accounting without introducing an active or additional external resource?

## 6. Propagation attack

For two compact quadrupolar endpoints, is

```math
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}
```

the correct normalized far-field channel ceiling for the same spectral normalization used in `Gamma_coh`?

Please attack the correspondence between:

- TT stationary-phase translation;
- gravitational antenna directivity `D <= 5/2`; and
- reciprocal/Friis-style power transfer.

## 7. Recurrent/common-bath attack

The manuscript sums passive repeated returns as a separated scattering series and finds

```math
\eta_{\rm rec}
\le\frac{\eta}{(1-\eta)^2}
=\eta+O((kR)^{-4}).
```

Can a common gravitational bath generate collective damping, coherent exchange, or another two-endpoint effect that changes the leading `O((kR)^-2)` power coefficient but is **not** captured by the separated passive scattering representation?

## 8. Narrowband attack

Is the passage from the conservative endpoint bound

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le\frac{4G}{3c^5}I\Omega^4
```

to the headline narrowband form with `Omega ~= omega` adequately controlled? Is there a passive spectral construction within the stated band that makes this replacement misleading or invalid?

## 9. Significance attack

Assume every equation is correct and no exact prior theorem exists. Does the final parameter elimination teach a nontrivial new piece of gravitational-antenna physics, or is it an immediate enough corollary of established antenna theory + modal completeness + passive transfer theory that it should not be a standalone paper?

A useful answer should state **why** the closure is or is not physically informative.

## Requested verdict format

Please return one of:

```text
TECHNICAL FAIL — with equation/counterexample.
PRIORITY FAIL — with primary citation and matching equation/result.
CORRECT BUT TOO INCREMENTAL — with a concise reason.
SURVIVES MY ATTACK — no specific defect or equivalent prior theorem found.
```

Optional: identify the single strongest objection that a specialist referee is most likely to raise.
