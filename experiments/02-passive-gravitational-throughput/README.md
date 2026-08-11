# Experiment 02 — Passive Gravitational Throughput

**Status:** validated sector-resolved theorem; PRD submission science frozen unless a concrete technical defect, direct prior-art collision, or substantive external objection reopens it.  
**Authoritative validated science/manuscript SHA:** `bfae23af41aefb3104d639099299b3432b4a14fe`.  
**Current submission target:** Physical Review D Research Article.

## Current result

For two separated compact passive nonrelativistic linear-harmonic matter systems in weak leading mass-quadrupole gravity, define

```math
\Gamma_{\rm coh}
=\frac{1}{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

`Gamma_coh` has units `s^-1`. It is a coherent-transfer spectral area / band-limited squared `H2` norm, not an information capacity, bit rate, detector sensitivity, waiting time, or strain-noise PSD.

Choose the source-receiver direction `Rhat` and define

```math
I_Rhat = \int \rho [r^2-(Rhat\cdot x)^2] d^3x,
Z_Rhat = \int \rho (Rhat\cdot x)^2 d^3x,
I_2 = I_Rhat+Z_Rhat.
```

Within the retained passive endpoint realization and outgoing compact-quadrupole TT propagation model, the strongest finite-band closure is

```math
\Gamma_{\rm coh}
\le
\frac{G\Omega^4}{5c^5}
\min[\mathcal G_A(R),\mathcal G_B(R)],
```

with the exact measured-band `m=0,|m|=1,|m|=2` propagation weights contained in `mathcal G_X`.

The rigorous far-zone coefficient is

```math
\boxed{
\limsup_{R\to\infty}R^2\Gamma_{\rm coh}
\le
\frac{5G\Omega^4}{4c^3\omega_-^2}
\min(I_{\hat R,A},I_{\hat R,B}).
}
```

For a retained carrier-scale narrow band,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{5G\omega_0^2}{4c^3R^2}
\min(I_{\hat R,A},I_{\hat R,B}).
}
```

The former scalar result remains a **valid looser corollary**, not a failed theorem:

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
```

The transition `25/12 * I_2 -> 5/4 * I_Rhat` is a directional refinement obtained by retaining the STF propagation sectors before closing the endpoint resource. The dedicated cross-version regression preserves the older scalar theorem as a fallback and independently tests the newer refinement.

## What survived the derivation chain

The following remain load-bearing:

- the passive selected-port `H2`/Gramian cut;
- the on-shell quadrupole linewidth `kappa_g,n = G omega_n^4(q_n:q_n)/(5c^5 mu_n)`;
- scalar completeness `sum (q:q)/mu <= (20/3) I_2`;
- sector completeness about `Rhat`;
- the compact TT leading coefficient `25/16` and exact outgoing finite-distance sector powers;
- the two-ended minimum endpoint cut;
- countably infinite retained realizations under the stated well-posed/admissible finite-trace conditions;
- same-two-endpoint passive recurrence leaving the leading `R^-2` coefficient unchanged.

## What was superseded or rejected

- Carrier-frozen propagation is no longer the strongest finite-band derivation; the current theorem retains `P_g[omega(nu),R]` over the measured band.
- `25/12 * I_2` is no longer the strongest leading closure, but remains valid as the scalar fallback.
- Reduced non-Markovianity is not by itself an exclusion: an admissible enlarged passive realization may remain covered.
- A universal whole-spectrum inertia-only closure is **not** established; completeness does not control the unrestricted fourth modal-frequency moment.
- Reviewer claims based on a second time derivative of the quadrupole, a universal `1/Q` integrated Paik-Wagoner scaling, bar-axis maximum radiation, or near-unit endpoint reflectivity defeating the far-zone recurrence bound were rejected after independent checks.
- Generic passive gain-bandwidth theory, resonant-mass response, material sum rules, directivity, multiple scattering, and gravity-mediated communication are historical ingredients, not novelty claims.

## Scope

The current theorem requires weak linearized gravity, nonrelativistic leading mass-quadrupole matter, passive linear endpoint dynamics, a retained modal ceiling `omega_n <= Omega`, compact endpoints across the measured band, and separated outgoing propagation with `omega_- R/c >> 1`.

The direct operator proof covers finite or countably infinite well-posed passive retained realizations with the required bounded/admissible selected maps and finite gravitational observation trace. Reduced memory can remain inside the logic after lifting to such an enlarged passive realization. Arbitrary hereditary media, singular continuum baths, or unbounded distributed control/observation models are not universally covered without a separate realization/admissibility/trace proof.

Still outside scope are uncontrolled whole-spectrum endpoint dynamics, active gain/pumping/feedback, extended phased apertures, added relays or external cavities, reactive near-field exchange, relativistic/nonlinear matter, higher-multipole-dominated operation, and strong-field/curved-background focusing.

## Scale and interpretation

For a uniform sphere, `I_Rhat=2Ma^2/5` and `Z_Rhat=Ma^2/5`, so the leading equal-endpoint form is

```math
\Gamma_{\rm coh}\lesssim
\frac{G\omega_0^2Ma^2}{2c^3R^2}.
```

For `M=1000 kg`, `a=1 m`, `f_0=1 kHz`, and `k_0R=100`, this is approximately `2.15e-39 s^-1`. The result is therefore primarily a structural passive-resource theorem, not a near-term detector-performance claim.

## Recovery order

Read current state in this order:

1. `AGENTS.md`
2. `RECOVERY_INDEX.md`
3. `CURRENT_STATE.md`
4. `CLAIM_LEDGER.md`
5. `ASSUMPTIONS.md`
6. `CONSTANT_REGRESSION_AUDIT_2026-08-10.md`
7. `NON_MARKOVIAN_CONTINUUM_SCOPE_AUDIT_2026-08-10.md`
8. `SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md`
9. reviewer and prior-art audits listed in `RECOVERY_INDEX.md`
10. `submission_prd/README.md`

`INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`, `FINITE_TWO_ENDED_INERTIA_BOUND.md`, `NARROWBAND_NORMALIZATION_AUDIT.md`, and other dated derivation/audit files preserve earlier validated stages. Their older coefficients or scope language are historical checkpoints and must not be mistaken for the current theorem.

The physics article itself must never mention repository infrastructure, commit hashes, source control, CI, or internal project bookkeeping.
