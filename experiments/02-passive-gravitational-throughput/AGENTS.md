# AGENTS.md — Experiment 02 Recovery and Freeze Protocol

**Experiment:** `02-passive-gravitational-throughput`  
**Mode:** validated sector-resolved theorem / externally responsive submission track.  
**Current validated science/manuscript SHA:** `3bf26c7535919597d711fdcd781e6098b76b5d68`.  
**Internal verdict:** **GO — preserve the sector-resolved theorem unless a concrete technical objection reopens it.**

This file is the first operational file an automated contributor should read after the repository-level `AGENTS.md`.

## 1. Live-state discipline

Before every write:

1. fetch the current `main` head;
2. verify this experiment exists at that exact ref;
3. inspect intervening commits;
4. fetch exact target blobs immediately before replacement;
5. never force-update a stale ref;
6. after writing, fetch the new remote head and changed files;
7. validate substantive science/manuscript changes on the exact resulting SHA.

Conversation history is not evidence of remote state.

## 2. Submission-manuscript style constraint

The physics article itself must **never mention the repository, GitHub, commit hashes, internal experiment labels, source-control state, CI, or project bookkeeping**. Those belong only in internal records. Numerical checks may be described scientifically as validation calculations. Do not refer to internal project artifacts as companion papers.

## 3. Canonical recovery order

Read first:

1. `SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md`
2. `CURRENT_STATE.md`
3. `CLAIM_LEDGER.md`
4. `SECOND_CRITICAL_REVIEW_AUDIT_2026-08-10.md`
5. `RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`
6. `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
7. `META_REFEREE_SIGNIFICANCE_AUDIT.md`
8. `submission_prd/README.md`

Older derivation documents remain useful provenance, but where they retain the former scalar `25/12 * I_2` closure they are superseded by the sector-resolved submission derivation at the validated SHA above.

## 4. Canonical theorem

Use

```text
omega(nu) = omega_0 + nu        physical frequency over measured band
omega_-                         infimum physical frequency in measured band
Omega                           upper retained endpoint modal frequency
R                               endpoint separation
a_A,a_B                         compact endpoint radii
I_Rhat                          int rho [r^2-(Rhat.x)^2] d^3x
Z_Rhat                          int rho (Rhat.x)^2 d^3x
I_2                             I_Rhat + Z_Rhat
```

For the retained bounded-port Markov modal sector and outgoing compact-quadrupole TT propagation model, the finite-band geometry-resolved inequality is

```math
Gamma_coh <= [G Omega^4/(5 c^5)] min[G_A(R),G_B(R)],
```

with

```math
G_X(R)=
4 eta2bar I_Rhat,X
+ eta1bar (2 I_Rhat,X + 4 Z_Rhat,X)
+ eta0bar [(2/3) I_Rhat,X + (8/3) Z_Rhat,X],
```

where `etambar` is the measured-band supremum of the exact outgoing compact-TT sector singular value.

The rigorous far-zone statement is

```math
\boxed{
limsup_{R->infty} R^2 Gamma_coh
<= [5 G Omega^4/(4 c^3 omega_-^2)]
min(I_Rhat,A,I_Rhat,B)
}
```

and the transparent carrier-scale narrowband form is

```math
\boxed{
Gamma_coh
lesssim
[5 G omega_0^2/(4 c^3 R^2)]
min(I_Rhat,A,I_Rhat,B).
}
```

This supersedes the older `25/12 * min(I_2A,I_2B)` headline.

## 5. Essential proof facts

Sector-resolved endpoint completeness about the propagation axis gives

```math
sum_n Q_2,n^2/mu_n <= 4 I_Rhat,
sum_n Q_1,n^2/mu_n <= 2 I_Rhat + 4 Z_Rhat,
sum_n Q_0,n^2/mu_n <= (2/3) I_Rhat + (8/3) Z_Rhat.
```

The three sums recover `(20/3) I_2`. For a complete displacement basis the unweighted sector projection sums are Parseval equalities.

Exact outgoing compact-TT sector power singular values, `z=omega R/c`, are

```math
eta_2 = 25(z^8-2z^6+3z^4-9z^2+9)/(16 z^10),
eta_1 = 25(z^6-3z^4+36)/(4 z^10),
eta_0 = 225(z^4+3z^2+9)/(4 z^10).
```

Only `|m|=2` survives at order `R^-2`; hence the leading resource is `I_Rhat`, not scalar `I_2`.

The final coefficient `5/4` is sharp at the abstract chained projection-sum level, but no claim is made that an unconstrained homogeneous elastic body realizes the simultaneously saturating modal arrangement.

## 6. High-frequency / Markov boundary

The modal rate

```math
kappa_g,n = [G omega_n^4/(5 c^5)] (q_n:q_n)/mu_n
```

is an **on-shell linewidth at the mode's own frequency**. It must not be imported unchanged into a far-detuned low-frequency tail. Such tails require frequency-dependent elastic and radiative response.

Completeness alone nevertheless does not remove the retained-frequency ceiling: an unweighted square-summable projection sequence need not have a finite fourth frequency moment. A genuine all-spectrum inertia-only theorem requires additional elastic/constitutive regularity, a microscopic cutoff, or a different frequency-domain closure.

## 7. Scope that must not be dropped

Do not silently broaden to:

- uncontrolled whole-spectrum endpoint dynamics under the same on-shell Markov trace;
- unbounded PDE boundary-control/observation ports without admissibility analysis;
- genuinely non-Markov continua;
- extended phased apertures;
- added gravitational relays or external cavities;
- reactive near-field exchange;
- active gain, pumping, inversion, or powered feedback;
- relativistic, nonlinear, higher-multipole-dominated, or strong-field matter.

## 8. Historical / novelty boundary

Do not claim novelty for generic passive `H2` machinery, Fano/Bode matching, Chu--Harrington antenna bounds, resonant-mass gravitational antenna theory, material-response sum rules, multimode elastic response, directivity, multiple scattering, or gravity as a communication mediator.

The publication candidate is the gravity-specific **two-ended sector-resolved endpoint-resource + compact-TT spectral-area closure**. Literature searches found no exact inspected equivalent; that negative result is not proof of priority. Do not use `first`, `new`, `unique`, or `unprecedented` as priority claims.

## 9. Validation state

Science/manuscript SHA `3bf26c7535919597d711fdcd781e6098b76b5d68` passed all six physics workflows and the PRD manuscript compile workflow. Exact run IDs and artifact digest are recorded in `SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md`.

## 10. Current research mode

Do not add theorem extensions merely because they are imaginable. Reopen the science only for a concrete technical defect, a direct prior-art collision, or a substantive specialist/journal objection. Otherwise restrict work to submission preparation and verification.
