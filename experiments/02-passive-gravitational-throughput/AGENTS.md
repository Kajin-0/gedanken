# AGENTS.md — Experiment 02 Recovery and Freeze Protocol

**Experiment:** `02-passive-gravitational-throughput`  
**Mode:** validated sector-resolved theorem / final PRD submission track.  
**Underlying validated science/theorem SHA:** `bfae23af41aefb3104d639099299b3432b4a14fe`.  
**Validated final submission-manuscript SHA:** `6f7a60b3b05dea9f288b1b07e6f2e55acaf34e83`.  
**Internal verdict:** **GO — submission ready after human sign-off; preserve the sector-resolved theorem unless a concrete technical objection reopens it.**

The later submission checkpoint changes only Acknowledgments/Data Availability and submission-support documentation. It does not alter the theorem or scientific derivation relative to the underlying science checkpoint.

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

Read current state in this order:

1. `RECOVERY_INDEX.md`
2. `CURRENT_STATE.md`
3. `CLAIM_LEDGER.md`
4. `FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md`
5. `THIRD_CRITICAL_REVIEW_AUDIT_2026-08-11.md`
6. `ASSUMPTIONS.md`
7. `CONSTANT_REGRESSION_AUDIT_2026-08-10.md`
8. `NON_MARKOVIAN_CONTINUUM_SCOPE_AUDIT_2026-08-10.md`
9. `SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md`
10. `SECOND_CRITICAL_REVIEW_AUDIT_2026-08-10.md`
11. `submission_prd/CRITICAL_REVIEW_AUDIT_2026-08-10.md`
12. `RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`
13. `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
14. `META_REFEREE_SIGNIFICANCE_AUDIT.md`
15. `submission_prd/README.md`

For operator-scope provenance also read `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`. For recurrence details read `PASSIVE_TWO_ENDPOINT_RECURRENCE.md`.

Older derivation and checkpoint files remain useful provenance. Their older theorem statements are historical states, not instructions to restore them. In particular, the scalar `25/12 * I_2` closure is **not false**; it remains a valid looser compatibility corollary. It is superseded only as the strongest current leading theorem by the sector-resolved result below.

## 4. Canonical theorem

Use

```text
omega(nu) = omega_0 + nu        physical frequency over measured band
omega_-                         infimum physical frequency in measured band
omega_+                         supremum physical frequency in measured band
Omega                           upper retained endpoint modal frequency
R                               endpoint separation
a_A,a_B                         compact endpoint radii
I_Rhat                          int rho [r^2-(Rhat.x)^2] d^3x
Z_Rhat                          int rho (Rhat.x)^2 d^3x
I_2                             I_Rhat + Z_Rhat
```

For the retained passive endpoint realization and outgoing compact-quadrupole TT propagation model, the finite-band geometry-resolved inequality is

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

where `etambar` is the measured-band supremum of the exact outgoing compact-TT sector power singular value.

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

The older scalar leading form remains valid as the looser corollary

```math
Gamma_coh
lesssim
[25 G omega_0^2/(12 c^3 R^2)]
min(I_2,A,I_2,B).
```

Logical relationship:

```text
25/12 * I_2   = valid scalar fallback after discarding STF-sector information
5/4  * I_Rhat = stronger directional leading closure retaining the propagating |m|=2 sector
```

## 5. Essential proof facts

The generic passive selected-port Gramian cut survives unchanged. The on-shell gravitational linewidth is

```math
kappa_g,n = [G omega_n^4/(5 c^5)] (q_n:q_n)/mu_n.
```

Scalar completeness is

```math
sum_n (q_n:q_n)/mu_n <= (20/3) I_2.
```

Sector-resolved completeness about the propagation axis is

```math
sum_n Q_2,n^2/mu_n <= 4 I_Rhat,
sum_n Q_1,n^2/mu_n <= 2 I_Rhat + 4 Z_Rhat,
sum_n Q_0,n^2/mu_n <= (2/3) I_Rhat + (8/3) Z_Rhat.
```

The three sector resources recover `(20/3) I_2`. For a complete displacement basis the unweighted projection sums are Parseval equalities.

Exact outgoing compact-TT sector power singular values, `z=omega R/c`, are

```math
eta_2 = 25(z^8-2z^6+3z^4-9z^2+9)/(16 z^10),
eta_1 = 25(z^6-3z^4+36)/(4 z^10),
eta_0 = 225(z^4+3z^2+9)/(4 z^10).
```

Only `|m|=2` survives at order `R^-2`; hence the leading resource is `I_Rhat`, not scalar `I_2`.

The `5/4` coefficient is sharp at the abstract chained projection-sum level, but no claim is made that an unconstrained homogeneous elastic body realizes simultaneous saturation of every step.

Appendix-C finite-distance formulas have been checked by two independent routes: the numerical TT regression and a later direct symbolic integration from the normalized sector kernels. Both recover the same outgoing amplitudes and `eta_m` closed forms.

## 6. High-frequency and reduced-memory boundary

The modal rate above is an **on-shell linewidth at the mode's own frequency**. It must not be imported unchanged into a far-detuned low-frequency tail. Such tails require frequency-dependent elastic and radiative response.

Completeness alone does not remove the retained-frequency ceiling: an unweighted square-summable projection sequence need not have a finite fourth frequency moment. A genuine all-spectrum inertia-only theorem requires additional elastic/constitutive regularity, a microscopic cutoff, or a different frequency-domain closure.

Do **not** interpret `Markov` as a claim that every reduced coordinate must have memoryless dynamics. A memory kernel generated by eliminating passive harmonic degrees of freedom can be lifted back to a larger local-in-time passive realization. If that enlarged realization is well posed, the selected maps are bounded or otherwise admissible, and the gravitational observation has the required finite trace, the passive-cut argument applies on the enlarged state space.

Therefore reduced non-Markovianity by itself is **not** an escape. What remains unproved is a universal extension to arbitrary hereditary constitutive laws, singular continuum baths, or unbounded distributed systems for which no admissible passive realization and finite gravitational-trace/resource closure has been established.

## 7. Scope that must not be dropped

Do not silently broaden to:

- uncontrolled whole-spectrum endpoint dynamics under the same inertia-only trace;
- arbitrary hereditary or singular continuum reduced models without an admissible passive realization and finite gravitational trace;
- unbounded PDE boundary-control/observation ports without system-node/admissibility analysis;
- extended phased apertures;
- added gravitational relays or external cavities;
- reactive near-field exchange;
- active gain, pumping, inversion, or powered feedback;
- relativistic, nonlinear, higher-multipole-dominated, or strong-field matter.

A bounded finite crystal is **not** excluded merely because continuum elasticity or microscopic damping is used. Application to a specific device still requires a controlled passive retained model over the measured band.

## 8. Historical / novelty boundary

Do not claim novelty for generic passive `H2` machinery, Fano/Bode matching, Chu--Harrington antenna bounds, resonant-mass gravitational antenna theory, material-response sum rules, multimode elastic response, directivity, multiple scattering, generalized-Langevin reduction, passive infinite-dimensional system theory, or gravity as a communication mediator.

The publication candidate is the gravity-specific **two-ended sector-resolved endpoint-resource + compact-TT spectral-area closure**. Literature searches found no exact inspected equivalent; that negative result is not proof of priority. Do not use `first`, `new`, `unique`, or `unprecedented` as priority claims.

## 9. Validation state

Underlying science/theorem SHA:

```text
bfae23af41aefb3104d639099299b3432b4a14fe
```

Validated final submission-manuscript SHA:

```text
6f7a60b3b05dea9f288b1b07e6f2e55acaf34e83
```

The final submission checkpoint passed the PRD compile and all seven physics/regression workflows on the exact head:

```text
PRD compile                run 31497750953
cross-version constant     run 31497750922
recurrence                 run 31497750907
infinite modal             run 31497750904
TT propagation             run 31497750892
endpoint resource          run 31497750903
combined bound             run 31497750916
passive cut                run 31497750968
```

Artifact:

```text
experiment02-prd-submission
artifact ID 9103729907
artifact ZIP sha256 a31ee561019906b28e2e8ecb2ca25f9ce98b1ef0260e1f354198ce2a073b6b98
PDF sha256 ea23e976ed9c1b3f210539c9310b4e4ad80e137eee7cbd82098fedbb9f3906bf
```

The exact-head PDF is 9 pages, visually preflighted, with embedded fonts, no unresolved references/placeholders, and no internal project terminology. Render comparison against the prior validated science PDF found pages 1-8 pixel-identical; only page 9 changed in Acknowledgments/Data Availability.

A cross-version audit was triggered specifically because the longstanding `25/12` coefficient changed after a context-window handoff. It found a **test-coverage regression** in the theorem-transition workflow but no scientific contradiction in `5/4`. The audit restored inherited scalar/end-to-end coverage and added `numerics/verify_constant_regression.py` plus the dedicated cross-version workflow.

The scalar theorem and sector refinement must now be tested together whenever coefficient-sensitive science changes.

See `FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md` for the package-level validation and remaining direct-human blockers.

## 10. Theorem change-control — mandatory

Any future change to a theorem coefficient, normalization, endpoint resource, asymptotic order, or headline inequality must satisfy every gate below **before** the manuscript headline is modified:

1. preserve and rerun all inherited regressions from the prior theorem state;
2. add an independent regression targeted at the new mathematical step;
3. include at least one numerical end-to-end composition test when the theorem is end-to-end;
4. explicitly classify the new result relative to the old one: refinement, incompatible replacement, or correction;
5. independently audit units, normalization conventions, polarization/sector degeneracies, and factors of two;
6. record exact pre-change and post-change science states in a dedicated audit;
7. never delete or narrow older regression coverage merely because the new proof uses a different decomposition;
8. retain a documented fallback theorem whenever the previous result remains valid.

A context reset, new agent, new reviewer prompt, or aesthetically cleaner derivation is **not** sufficient reason to change a validated theorem. New work must beat the inherited validation stack rather than replace it.

## 11. Documentation discipline

Whenever a future objection changes the scientific interpretation or theorem state, update all current handoff layers in the same work:

1. `RECOVERY_INDEX.md` — chronology, tried/rejected/open angles;
2. `CURRENT_STATE.md` — concise canonical state;
3. `CLAIM_LEDGER.md` — claim-level disposition;
4. `ASSUMPTIONS.md` — current theorem class and exclusions;
5. the relevant dedicated audit/checkpoint file — detailed reasoning and validation;
6. current submission helper files if their theorem wording, scale example, scope, or submission-policy state has become stale.

If the manuscript changes, also record the exact validated manuscript SHA and workflow/artifact state. Distinguish an editorial submission-manuscript checkpoint from the underlying science/theorem checkpoint when the scientific body is unchanged. Do not let a new result live only in conversation history.

## 12. Current research mode

The project is now in **human sign-off / APS upload mode**. Do not add theorem extensions merely because they are imaginable. Reopen the science only for a concrete technical defect, a direct prior-art collision, or a substantive specialist/journal objection. Otherwise do not churn the scientific manuscript.
