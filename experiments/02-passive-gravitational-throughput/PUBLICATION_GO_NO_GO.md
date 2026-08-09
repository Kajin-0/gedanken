# Publication Go / No-Go — Experiment 02

## Verdict

**PHYSICS: GO WITH DECLARED SCOPE**

**MANUSCRIPT: GO AFTER PRIOR-ART CORRECTION**

**NOVELTY: PROVISIONAL GO ONLY FOR THE EXACT MANY-MODE TWO-ENDED RESOURCE CLOSURE**

**BROAD GENERATOR/RECEIVER, RECIPROCITY, Q-INDEPENDENT RESPONSE, AND DIRECTIVITY NOVELTY: NO-GO — HISTORICAL**

**BROADENING TO ARBITRARY INTERACTING/NON-MARKOV MATTER: NO-GO FOR THIS PAPER**

The theorem remains internally coherent within its stated class. Full-text inspection of the strongest historical sources did not expose an exact theorem collision, but it substantially narrowed what can plausibly count as new.

---

## 1. Physics gate — GO

Within

```text
compact passive nonrelativistic linear bosonic source and receiver networks
+ weak quadrupole coupling to linearized gravity
+ band-local stable passive Markov dynamics
+ direct weak one-way wave-zone propagation,
```

the current result is

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right),
}
```

with

```math
\Gamma_{\rm coh}
=\frac1{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
```

The proof no longer depends on a specific four-spoke source, chosen quality factor, single resonance, critical coupling, or internal modal basis.

---

## 2. Proof/normalization gates — PASS

### Passive network

Established completely passive Lyapunov/H2 identities yield

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[\operatorname{Tr}\Gamma_{g,A},
     \operatorname{Tr}\Gamma_{g,B}].
```

The H2 mathematics is prior art. No defect was found in its selected-port use here.

### Microscopic gravitational-port factorization

```math
G_B^\dagger U_RG_A
=
\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2}
```

separates coupling magnitude from normalized radiation geometry. Numerical tests with deliberately overlapping radiation patterns continue to support this factorization.

### Cumulative material resource

For the declared ordinary nonrelativistic linear-bosonic matter class,

```math
\operatorname{Tr}\Gamma_g
=\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
```

This cumulative EWSR step closes the many-passive-resonance loophole.

### Propagation

The normalized separated wave-zone channel obeys

```math
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}
```

at leading retained order. Independent TT-normalization checks remain intact.

---

## 3. Full-text historical gate — STRONG COLLISIONS, NOT A FULL THEOREM COLLISION

### Grishchuk–Sazhin 1975

Already contains a complete gravitational generator--detector calculation and an architecture-specific end-to-end system limitation. Therefore the mere existence of source-to-receiver gravitational accounting or an end-to-end limitation is historical.

### Hirakawa–Narihara–Fujimoto 1976

This is the strongest compact-mechanical collision. The full paper already contains:

- compact mechanical gravitational antenna eigenmodes;
- a quadrupole-derived mode gravitational oscillator strength;
- emission and reception in the same formalism;
- an explicit gravitational reciprocity theorem;
- a `Q`-independent short-pulse response;
- the same compact real-STF directivity functional used here, in equivalent component notation;
- the `D=5/2` directivity maximum;
- resonant sensor loading and thermal-noise analysis.

The exact directivity equivalence is

```math
q:\Lambda(\hat n):q
=q:q-2(q\hat n)\cdot(q\hat n)
+\frac12(\hat n^Tq\hat n)^2,
```

which makes

```math
\frac52\frac{q:\Lambda:q}{q:q}
```

algebraically identical to Hirakawa et al. Eq. (15).

Therefore neither the directivity functional nor its maximum is novel.

Canonical audit: `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`.

---

## 4. What survives the historical gate

No inspected source has yet been found to state the full conjunction

```text
known passive selected-port H2 cut set
+ microscopic gravitational coupling trace at source
+ microscopic gravitational coupling trace at receiver
+ normalized separated TT propagation operator
+ cumulative mass-quadrupole EWSR closure of BOTH endpoint traces
-> many-mode end-to-end frequency-integrated coherent-transfer ceiling
-> channel-specific pure-loss corollaries.
```

That is now the **only** candidate novelty target.

A negative search is not proof of priority.

---

## 5. Significance gate — OPEN, NOT A PHYSICS FAILURE

The strongest hostile-referee objection is now:

> The result may be a mathematically correct synthesis of known compact gravitational-antenna oscillator-strength/reciprocity/directivity physics, known passive H2 theory, and known sum-rule machinery rather than a fundamentally new physical principle.

This is a real publication risk.

The answer cannot be that emission, reception, Q-independent response, directivity, or source--receiver analysis are new; they are not. The paper must stand or fall on whether the **architecture-independent cumulative two-end resource closure** is itself a sufficiently useful and nontrivial theorem.

---

## 6. Sharpness gate — VALID BOUND; GLOBAL SATURATION OPEN

The V7 long-wavelength explicit mode reaches 30% of the endpoint-only EWSR gravitational-linewidth ceiling and saturates the compact TT geometry ceiling.

The exact symmetric two-port EBP optimum reaches

```math
\frac4{45}\simeq0.0889
```

of the combined theorem ceiling in that explicit comparison.

The scaling is therefore represented by a concrete model, but the final numerical coefficient is not claimed globally saturable.

---

## 7. Quantum-information gate — GO AS COROLLARY

`Gamma_coh` is not a quantum capacity.

For a stationary vacuum pure-loss realization:

```math
\eta_{\max}\le\frac12
\quad\Rightarrow\quad Q_1=0,
```

and

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
```

These remain channel-specific consequences, not headline novelty claims.

---

## 8. Manuscript gate — GO AFTER CORRECTION

The manuscript abstract, introduction, discussion, and bibliography have been revised to credit the historical compact antenna and generator--detector results explicitly.

Post-correction validation:

```text
GitHub Actions run: 31342625802
job:                93318795190
LaTeX compile:      PASS
citation/ref scan:  PASS
PDF upload:         PASS
rendered length:    14 pages
visual QA:          PASS
```

The theorem equations themselves were not changed by the historical correction.

---

## 9. Allowed manuscript claim

A referee-safe formulation is:

> We combine established passive linear-system identities with microscopic gravitational coupling traces, cumulative mass-quadrupole spectral bounds at two compact matter interfaces, and a normalized separated TT propagation operator to derive a many-mode end-to-end frequency-integrated ceiling for direct passive gravitational transduction.

The manuscript should immediately acknowledge that compact gravitational antenna reciprocity, quadrupole oscillator strength, Q-independent pulse response, and the real-STF directivity law are historical.

---

## 10. Forbidden manuscript claims

Do not write:

- “first gravitational efficiency-bandwidth bound”;
- “new Q-independent gravitational response law”;
- “first source-receiver gravitational bound”;
- “new gravitational antenna reciprocity”;
- “new compact quadrupole directivity law”;
- “new passive-network theorem”;
- “universal limit on gravitational quantum communication”;
- “all passive matter”;
- “fundamental quantum-gravity capacity bound”;
- “optimal coefficient” without simultaneous saturability;
- first/unique/unprecedented language without substantially stronger priority evidence.

---

## Final decision

```text
PHYSICS THEOREM:                    GO
NUMERICAL VALIDATION:               GO
FULL-TEXT HISTORICAL AUDIT:         GO / CLAIM NARROWED
MANUSCRIPT AFTER CORRECTION:        GO
GENERIC TWO-ENDED NOVELTY:          NO
Q-INDEPENDENT RESPONSE NOVELTY:     NO
DIRECTIVITY / D=5/2 NOVELTY:        NO
EXACT MANY-MODE RESOURCE CLOSURE:   PROVISIONAL GO
PUBLICATION SIGNIFICANCE:           EXTERNAL-JUDGMENT RISK
PRIORITY CLAIM:                     NO
V7 MODIFICATION:                    NO
THEOREM BROADENING:                 NO FOR THIS PAPER
```

The strongest next action is **external specialist review of the exact many-mode resource closure and its significance**, not another internal derivation or broader theorem.
