# Current State — Experiment 02

**Status:** **SECTOR-RESOLVED THEOREM VALIDATED; REDUCED-MEMORY/CONTINUUM SCOPE CLARIFIED; SCIENCE FROZEN AT `bfae23af41aefb3104d639099299b3432b4a14fe`; FINAL PRD SUBMISSION MANUSCRIPT VALIDATED AT `6f7a60b3b05dea9f288b1b07e6f2e55acaf34e83`.**

The later submission checkpoint changes only Acknowledgments/Data Availability and submission-support documentation for current APS policy. It does not change the theorem, equations, scientific sections, appendices, bibliography, or numerical regressions relative to the science checkpoint.

Primary recovery records:

- `RECOVERY_INDEX.md`
- `CLAIM_LEDGER.md`
- `ASSUMPTIONS.md`
- `FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md`
- `THIRD_CRITICAL_REVIEW_AUDIT_2026-08-11.md`
- `CONSTANT_REGRESSION_AUDIT_2026-08-10.md`
- `NON_MARKOVIAN_CONTINUUM_SCOPE_AUDIT_2026-08-10.md`
- `SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md`

## 1. Operational quantity

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

`Gamma_coh` is a coherent-transfer spectral area with units `s^-1`, not an information capacity, bit rate, detector sensitivity, waiting time, or noise PSD.

Use physical frequency `omega(nu)=omega_0+nu`, lower and upper measured-band physical frequencies `omega_-`,`omega_+`, retained modal ceiling `Omega`, compact endpoint radii `a_A,a_B`, and separation axis `Rhat`.

Define

```math
I_Rhat = int rho [r^2-(Rhat.x)^2] d^3x,
Z_Rhat = int rho (Rhat.x)^2 d^3x,
I_2 = I_Rhat + Z_Rhat.
```

`I_Rhat` is the conventional moment of inertia about the line joining the endpoints.

## 2. Strongest finite-band closure

Within the retained passive endpoint realization and outgoing compact-quadrupole TT propagation model,

```math
\boxed{
Gamma_coh <= [G Omega^4/(5 c^5)] min[G_A(R),G_B(R)]
}
```

with

```math
G_X(R)=
4 eta2bar I_Rhat,X
+ eta1bar (2 I_Rhat,X + 4 Z_Rhat,X)
+ eta0bar [(2/3) I_Rhat,X + (8/3) Z_Rhat,X],
```

where `etambar` is the supremum over the actual measured band of the exact outgoing compact-TT sector power singular value.

This form retains propagation variation over the measured band; it does not freeze the propagator at `omega_0`.

## 3. Far-zone theorem and scalar fallback

The exact outgoing sector powers are

```math
eta_2(z)=25(z^8-2z^6+3z^4-9z^2+9)/(16 z^10),
eta_1(z)=25(z^6-3z^4+36)/(4 z^10),
eta_0(z)=225(z^4+3z^2+9)/(4 z^10),
```

with `z=omega R/c`. Their leading orders are `R^-2`, `R^-4`, and `R^-6` in power. Therefore only `|m|=2` survives at leading far-zone power order.

The rigorous asymptotic theorem is

```math
\boxed{
limsup_{R->infty} R^2 Gamma_coh
<= [5 G Omega^4/(4 c^3 omega_-^2)]
min(I_Rhat,A,I_Rhat,B).
}
```

For a carrier-scale retained narrow band:

```math
\boxed{
Gamma_coh
lesssim
[5 G omega_0^2/(4 c^3 R^2)]
min(I_Rhat,A,I_Rhat,B).
}
```

The former scalar leading result remains a valid looser corollary:

```math
Gamma_coh
lesssim
[25 G omega_0^2/(12 c^3 R^2)]
min(I_2,A,I_2,B).
```

Thus the theorem history is **refinement, not contradiction**. If a future defect is found specifically in the sector-weighted closure, the independently preserved scalar theorem is the fallback.

## 4. Endpoint resource

The on-shell gravitational energy linewidth is

```math
kappa_g,n=[G omega_n^4/(5 c^5)](q_n:q_n)/mu_n.
```

Scalar completeness:

```math
sum_n (q_n:q_n)/mu_n <= (20/3) I_2.
```

Sector completeness relative to `Rhat`:

```math
sum_n Q_2,n^2/mu_n <= 4 I_Rhat,
sum_n Q_1,n^2/mu_n <= 2 I_Rhat + 4 Z_Rhat,
sum_n Q_0,n^2/mu_n <= (2/3) I_Rhat + (8/3) Z_Rhat.
```

The three sector resources sum to `(20/3) I_2`. For a complete displacement basis each unweighted sector projection sum is a Parseval equality.

Resolving the endpoint resource before the propagation cut removes the unnecessary independent maximization that produced the looser scalar headline.

## 5. Tightness checks

At the abstract retained-modal projection level, complete `|m|=2` Parseval saturation together with retained modes at `Omega` saturates the chained resource-propagation coefficient `5/4`. This does not establish realizability by an arbitrary homogeneous elastic body.

For an ideal slender free-free bar observed in its maximum-radiation transverse direction, the fundamental longitudinal mode occupies

```math
48/pi^4 ~= 0.493
```

of the complete leading `|m|=2` endpoint resource.

For a uniform sphere,

```math
I_Rhat=2Ma^2/5,
Z_Rhat=Ma^2/5,
```

so

```math
Gamma_coh lesssim G omega_0^2 M a^2/(2 c^3 R^2).
```

At `M=1000 kg`, `a=1 m`, `f_0=1 kHz`, and `k_0R=100`, the leading value is approximately `2.15e-39 s^-1`.

## 6. High-frequency/off-resonant boundary

The modal linewidth above is on shell at `omega_n`. It cannot be assigned unchanged to the low-frequency tail of a far-detuned mode.

The retained-modal ceiling remains a real mathematical assumption: scalar or sector completeness controls an unweighted modal projection sum, not its fourth frequency moment. A whole-spectrum inertia-only theorem therefore needs additional constitutive regularity, microscopic cutoff information, or a different frequency-domain argument.

This is currently the strongest unresolved mathematical frontier.

## 7. Reduced-memory / continuum boundary

A bounded finite crystal is not automatically a frequency continuum, and a reduced memory kernel can arise by eliminating passive degrees of freedom from a larger local-in-time system.

Therefore:

```text
reduced memory / non-Markovianity alone != escape from the passive cut
```

If the eliminated degrees of freedom can be restored to a well-posed passive enlarged realization, the selected maps are bounded or otherwise admissible, and the gravitational observation has the required finite trace, the Gramian cut can be applied on the enlarged state space.

What is not proved is universal applicability to arbitrary hereditary constitutive laws, singular continuum baths, or unbounded distributed systems without an explicit passive realization, admissibility proof, and gravity-specific finite-trace/resource closure.

This clarification changes no theorem coefficient and does not remove the independent retained-frequency limitation in Sec. 6.

## 8. Infinite retained sectors and recurrence

Countably infinite separable retained modal spaces are covered under the stated well-posed passive / admissible selected-map / finite gravitational-trace hypotheses.

Repeated passive returns between the same two separated compact endpoints satisfy the exact resolvent estimate

```math
||P_eff|| <= p_+/(1-p_+p_-)
```

when `p_+p_-<1`. Since `p_+,p_-=O(R^-1)` in the separated far zone, recurrence does not modify the leading `R^-2` power coefficient. The first possible correction to the upper ceiling is `O(R^-4)` in power.

## 9. Validation state

Underlying validated science/theorem SHA:

```text
bfae23af41aefb3104d639099299b3432b4a14fe
```

Validated final submission-manuscript SHA:

```text
6f7a60b3b05dea9f288b1b07e6f2e55acaf34e83
```

The final submission checkpoint passed the PRD compile plus all seven physics/regression workflows on that exact head:

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

Exact-head artifact:

```text
experiment02-prd-submission
artifact ID 9103729907
artifact ZIP sha256 a31ee561019906b28e2e8ecb2ca25f9ce98b1ef0260e1f354198ce2a073b6b98
PDF sha256 ea23e976ed9c1b3f210539c9310b4e4ad80e137eee7cbd82098fedbb9f3906bf
```

The 9-page PDF was visually preflighted with embedded fonts, no unresolved references/placeholders, and no internal project terminology. A pixel comparison with the previous validated PDF found pages 1-8 identical and only page 9 changed in the Acknowledgments/Data Availability region.

After the `25/12 -> 5/4` continuity concern, a separate cross-version audit restored inherited scalar/end-to-end regressions that had been lost during the sector transition. The final submission checkpoint passes that accumulated test as well.

See `FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md` for the complete final package audit.

## 10. What survived / failed / remains open

**Survived:** passive Gramian cut, correct quadrupole linewidth, scalar and sector completeness, `25/16` TT leading normalization, exact outgoing sector powers, two-ended minimum cut, infinite retained-sector extension under stated operator conditions, recurrence leading-order result.

**Superseded but still valid:** scalar `25/12 * I_2` headline; carrier-frozen propagation derivation; older blanket reduced-memory scope wording.

**Rejected:** reviewer second-derivative quadrupole power, universal `1/Q` integrated Paik-Wagoner claim, bar-axis maximum-radiation claim, recurrence blow-up from endpoint reflectivity alone, generic ingredient novelty/priority claims.

**Open:** whole-spectrum fourth-frequency closure, constitutive realizability/joint saturation, broader unbounded distributed-system admissibility, practical engineering relevance, and any noise/information-theory layer.

## 11. Research mode

The hostile reviews triggered legitimate reopenings only where concrete objections survived checking. Those reopenings are now closed at the declared model level. The final package is technically submission-ready after direct human sign-off. Further theorem work requires a new concrete technical issue, direct prior-art collision, or substantive external objection; otherwise do not churn the manuscript.
