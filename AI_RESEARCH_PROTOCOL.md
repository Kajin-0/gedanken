# AI-First Research Protocol

## Principle

Internal research in this repository is **AI-native by default**.

Human specialists are not part of the normal iteration loop. They are reserved for the final external-review / journal-review boundary, or for a genuinely external fact that cannot be resolved internally.

The objective is not to remove skepticism. It is to automate skepticism.

---

## Standard research loop

A serious candidate result should pass the following stages before it is treated as mature.

### 1. Research / derivation agent

Develop the argument from the current physical question without forcing a predetermined theorem.

Deliverables:

- explicit assumptions;
- definitions;
- derivation;
- dimensional/scaling checks;
- clear distinction between theorem, approximation, example, and conjecture.

### 2. Independent reconstruction agent

Receive the claim, definitions, and assumptions but not the original derivational narrative when practical.

Objective:

- reproduce the result by an independent route;
- identify missing hypotheses;
- detect convention dependence;
- report any coefficient or scaling disagreement.

Agreement is valuable only if the route is genuinely different.

### 3. Hostile technical-referee agent

Assume the paper should be rejected and attempt to produce

- a counterexample;
- an invalid limiting operation;
- a hidden conservation-law failure;
- an operator-domain or continuum problem;
- a normalization error;
- a physical regime that violates the claimed scope.

The agent should prefer falsification over suggestions for extension.

### 4. Prior-art collision agent

Assume the result is already known.

Search by

- equations and dimensional fingerprints;
- historical terminology;
- equivalent physical quantities;
- adjacent fields with isomorphic mathematics;
- old reviews and primary sources;
- architecture-specific special cases that may contain the general result implicitly.

The output must separate

```text
ingredient prior art
method prior art
special-case prior art
exact theorem collision
negative search result
```

A negative search is never proof of priority.

### 5. Numerical counterexample agent

When the assumptions admit computation, do not merely verify examples. Search adversarially for violations.

Typical methods:

- random constrained systems;
- nonnormal / noncommuting matrices;
- extreme parameter sweeps;
- optimization of the ratio `actual / claimed bound`;
- asymptotic scaling regression;
- exact-vs-approximate comparison.

The test should be designed to fail the theorem if possible.

### 6. Symbolic / normalization audit

Independently check

- dimensions;
- factors of `2` and `pi`;
- Fourier-transform conventions;
- one-sided vs two-sided spectra;
- polarization normalization;
- complex-amplitude vs real-amplitude conventions;
- `hbar` cancellation;
- field-energy normalization;
- asymptotic order statements.

Compilation success is not a semantic check.

### 7. Significance / editor agent

Assume the theorem is correct and ask:

> What physical information remains after every established ingredient is credited?

Classify the result as one of

```text
new general method
new field-specific theorem
new parameter elimination / resource closure
useful special case
pedagogical synthesis
not enough for a standalone paper
```

Correctness and publishable significance are separate gates.

### 8. Meta-referee

Read the frozen adversarial reports and issue one decision:

```text
REJECT
MAJOR REVISION
MINOR REVISION
GO FOR SPECIALIST SUBMISSION
```

The meta-referee must state

- strongest surviving objection;
- exact novelty boundary;
- whether more derivation is justified;
- whether the manuscript should be compressed rather than broadened.

### 9. Manuscript compression

Once the theorem survives, remove the development history from the conceptual center.

The main paper should contain only what a new reader needs to understand and audit the result. Keep detailed independent checks in appendices or audit files.

Compression is followed by a second adversarial review because shortening can introduce semantic errors even when LaTeX and numerical CI pass.

### 10. Final external review

Only after the AI loop is closed should human specialists become relevant.

Human review is used as an **independent external measurement**, not as a dependency required to continue internal work.

A human reviewer should be asked to do one of the following:

- find a technical counterexample;
- identify an exact prior theorem;
- identify a field-specific assumption the AI audits missed;
- judge whether the surviving result is significant enough for publication.

Do not wait for human feedback before completing internally automatable work.

---

## Independence discipline

Role-separated AI agents are not automatically statistically independent.

To reduce correlated error:

- freeze intermediate outputs before later agents read them;
- give different agents incompatible objectives;
- withhold derivational history from reconstruction agents when practical;
- use different mathematical representations where possible;
- require numerical/symbolic tests in addition to prose reasoning;
- record when several reports ultimately came from the same underlying model family.

Never describe an internal AI ensemble as equivalent to independent journal peer review.

---

## Repository state expected for a mature result

A mature experiment should normally contain equivalents of

```text
CURRENT_STATE
CLAIM_LEDGER / NOVELTY_BOUNDARY
ASSUMPTION_LEDGER
PRIOR_ART_MATRIX or collision audits
INDEPENDENT_DERIVATION
HOSTILE_REFEREE_REPORT
NUMERICAL_COUNTEREXAMPLE_SEARCH
NORMALIZATION_AUDIT
SIGNIFICANCE_AUDIT
META_REFEREE_DECISION
MANUSCRIPT
VALIDATION / CI record
```

The exact filenames may vary by experiment.

---

## Stop rule

Do not continue deriving merely because AI makes derivation cheap.

Stop internal theorem expansion when

1. the result has a precise scope;
2. independent derivation/normalization checks agree;
3. hostile technical agents fail to produce an in-scope counterexample;
4. prior-art agents have reduced novelty to an exact defensible claim;
5. numerical adversaries pass;
6. the meta-referee says additional generalization is more likely to dilute than strengthen the result.

At that point the highest-value action is manuscript compression and final external review, not another theorem.

---

## Reopen rule

A frozen result may be reopened only for

- a concrete technical defect;
- a specific prior-art collision;
- a reviewer objection that changes correctness or scope;
- a new calculation that directly tests a load-bearing assumption.

Do not reopen a closed theorem for speculative breadth alone.
