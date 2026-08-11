# Sector-Resolved Theorem Checkpoint — 2026-08-10

## Status

**VALIDATED SCIENCE/MANUSCRIPT CHECKPOINT**

Science/manuscript SHA:

```text
3bf26c7535919597d711fdcd781e6098b76b5d68
```

Commit:

```text
Replace scalar closure with sector-resolved inertia theorem
```

This checkpoint supersedes the former scalar `25/12 * I_2` headline for current submission recovery.

## Trigger

A hostile review raised three substantive issues:

1. independent optimization of total endpoint quadrupole strength and propagation directivity might make the final coefficient unnecessarily loose;
2. carrier-frozen propagation left a qualitative `O(B/omega_0)` band error;
3. the retained high-frequency-sector assumption needed a sharper physical and mathematical interpretation.

Reopening those layers produced a stronger closure rather than a failure of the passive theorem.

## Current theorem

Define the separation-axis resources

```math
I_Rhat = int rho [r^2-(Rhat.x)^2] d^3x,
Z_Rhat = int rho (Rhat.x)^2 d^3x,
I_2 = I_Rhat+Z_Rhat.
```

The STF modal quadrupole space decomposes into `|m|=2`, `|m|=1`, and `m=0` sectors relative to `Rhat`. Sectorwise Bessel/Parseval gives

```math
sum Q_2^2/mu <= 4 I_Rhat,
sum Q_1^2/mu <= 2 I_Rhat+4 Z_Rhat,
sum Q_0^2/mu <= (2/3)I_Rhat+(8/3)Z_Rhat.
```

The exact outgoing compact-TT sector powers at `z=omega R/c` are

```math
eta_2=25(z^8-2z^6+3z^4-9z^2+9)/(16z^10),
eta_1=25(z^6-3z^4+36)/(4z^10),
eta_0=225(z^4+3z^2+9)/(4z^10).
```

For retained physical modal frequencies `omega_n<=Omega`, define `eta_mbar` as the supremum of `eta_m` over the measured physical frequency band. Then

```math
Gamma_coh <= [G Omega^4/(5c^5)] min[G_A(R),G_B(R)],
```

where

```math
G_X=4 eta_2bar I_Rhat,X
+ eta_1bar(2 I_Rhat,X+4 Z_Rhat,X)
+ eta_0bar[(2/3)I_Rhat,X+(8/3)Z_Rhat,X].
```

This is a finite-band, finite-`kR` inequality within the retained bounded-port Markov endpoint model and outgoing compact-quadrupole TT propagation model. It does not freeze the propagator at the carrier.

For a fixed measured band with lower physical frequency `omega_->0`, only `|m|=2` survives at leading far-zone power order, giving

```math
\boxed{
limsup_{R->infty} R^2 Gamma_coh
<= [5G Omega^4/(4c^3 omega_-^2)]
min(I_Rhat,A,I_Rhat,B).
}
```

For a carrier-scale narrow band,

```math
\boxed{
Gamma_coh lesssim
[5G omega_0^2/(4c^3R^2)]
min(I_Rhat,A,I_Rhat,B).
}
```

## What changed physically

The old closure used the full scalar endpoint projection resource `(20/3)I_2` and separately applied the maximum compact-TT directivity. The stronger proof projects the endpoint resource into propagation-defined STF sectors before the passive cut is closed. The leading channel sees only the `|m|=2` resource, which is exactly controlled by the conventional moment of inertia about the source-receiver axis.

The `5/4` coefficient is sharp at the abstract projection-sum level: for a complete displacement basis the `|m|=2` sum equals `4I_Rhat`, and an abstract retained sector placed at the modal ceiling can saturate the chained resource-propagation constant. This is not a constitutive realizability claim for an arbitrary homogeneous body.

## High-frequency scope result

The formula

```math
kappa_g,n=[G omega_n^4/(5c^5)](q_n:q_n)/mu_n
```

is an on-shell modal linewidth at `omega_n`. It is invalid to import that on-shell frequency factor unchanged into a far-detuned response at `omega_0 << omega_n`; the latter requires a frequency-dependent elastic/radiative response.

The retained-sector assumption cannot nevertheless be eliminated by completeness alone. Completeness controls an unweighted modal projection sum, while an unrestricted fourth frequency moment can diverge for a square-summable projection sequence. A whole-spectrum inertia-only theorem would need additional constitutive/elastic regularity, microscopic cutoff information, or another frequency-domain sum rule.

## Scale checks

### Uniform sphere

```math
I_Rhat=2Ma^2/5,
Z_Rhat=Ma^2/5,
Gamma_coh lesssim G omega_0^2 M a^2/(2c^3R^2).
```

For `M=1000 kg`, `a=1 m`, `f_0=1 kHz`, `k_0R=100`:

```text
R ~= 4.77e6 m
leading Gamma_coh ~= 2.15e-39 s^-1
finite-z sector factor ~= 1.00020009
```

### Ideal slender bar

The fundamental free-free longitudinal mode in its maximum-radiation transverse direction occupies

```math
48/pi^4 ~= 0.493
```

of the complete leading `|m|=2` endpoint projection resource.

## Exact-head validation

All dedicated workflows passed on science/manuscript SHA `3bf26c7535919597d711fdcd781e6098b76b5d68`:

```text
passive cut        31452652657 — PASS
endpoint resource  31452652672 — PASS
TT propagation     31452652787 — PASS
combined bound     31452652636 — PASS
infinite modal     31452652694 — PASS
recurrence         31452652697 — PASS
PRD manuscript     31452652653 — PASS
```

Compiled artifact:

```text
name: experiment02-prd-submission
artifact ID: 9086872919
ZIP size: 352219 bytes
SHA256: 675e6d67baaf6538f34602f0d3a48c81b3dccb07fe4fabd1caf0076db2945738
head SHA: 3bf26c7535919597d711fdcd781e6098b76b5d68
```

## Submission-language constraint

The submitted paper must contain no mention of repository infrastructure, commit history, CI, internal experiment labels, or project bookkeeping. These checkpoint details are internal only.

## Research stop

This theorem reopening was justified by a concrete hostile-review objection. It is now closed at the declared model level. Do not extend the theorem further merely because an extension is imaginable. Reopen only for a concrete technical defect, direct literature collision, or substantive external review objection.
