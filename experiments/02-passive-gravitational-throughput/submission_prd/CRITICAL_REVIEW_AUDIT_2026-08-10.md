# Adversarial audit of supplied revised-manuscript review — 2026-08-10

**Target:** Experiment 02 PRD submission layer.  
**Pre-audit `main`:** `049464dfd41f0a2dcea028dd516744a196f7d148`.  
**Rendered artifact inspected:** GitHub Actions artifact `9085045403`, exact PDF built from that head.  
**Role of the supplied report:** reviewer-style adversarial input only; it is not treated as an authority or as formal journal peer review.

## Verdict

The report is useful as a simulation of objections a real referee might raise, but several of its technical and visual claims are false. The correct response is therefore selective: retain valid clarity/tightness concerns, reject incorrect physics and normalization claims, and do not change the frozen theorem or its `25/12` coefficient.

## 1. Rendered-PDF claims checked directly

The exact CI-built PDF is seven pages.

- **Equation-reference claim — rejected.** The propagation section correctly says `Combining Eqs. (20), (35), and (44)`, and Eq. (44) is the operator propagation bound. The report's claim of an Eq. (46) versus Eq. (44) typo is not present in the built manuscript.
- **`text[[...]]` artifact — rejected.** No such string is visible on page 7 of the exact CI-built PDF.
- **`exec cutable` typo — rejected as a source error.** The PDF hyphenates `executable` across the two-column page break as `exe-` at the bottom of the left column and `cutable` at the top of the right column. This is normal TeX hyphenation, not a misspelling. The sentence is nevertheless rephrased in the submission source to remove the opportunity for misreading.
- **Appendix-B table — presentation concern accepted.** It is already a genuine LaTeX `tabular`, contrary to the report's description of it as plain text, but the narrow justified columns produce poor spacing and awkward word breaks. The table is reformatted using a ragged-right `tabularx` layout.

## 2. Quadrupole-radiation check in the report is wrong

The manuscript uses the standard leading nonrelativistic mass-quadrupole radiation formula

```math
\overline P_g
=\frac{G}{5c^5}\overline{\dddot Q_{ij}\dddot Q_{ij}}
=\frac{G\omega^6}{10c^5}|\xi_0|^2(q:q).
```

The supplied report instead rewrites this with `\ddot Q_{ij}` and therefore obtains an `\omega^4` power scaling. That is not the gravitational quadrupole radiation formula. Its subsequent decay-rate arithmetic is also internally inconsistent: an `\omega^4` radiated power divided by harmonic energy proportional to `\omega^2` would scale as `\omega^2`, not the manuscript's correct `\omega^4` decay rate.

**Action:** no manuscript change. The existing `\dddot Q` normalization is retained.

## 3. What the `20/3` completeness factor does and does not claim

The report asks whether a uniform elastic sphere nearly saturates

```math
\sum_n \frac{q_n:q_n}{\mu_n}\le\frac{20}{3}I_2.
```

The distinction it misses is important:

1. for a **complete displacement basis**, Parseval gives equality for the unweighted projection sum; this is not special to a sphere;
2. the theorem uses only a **retained carrier-scale modal subset**, and that subset need not capture the complete-basis value;
3. the fraction captured below the retained cutoff depends on the body's elastic spectrum and geometry.

Lobo's spherical-antenna analysis confirms that a homogeneous sphere has spheroidal mode families and that only the appropriate monopole/quadrupole families couple to metric tidal fields; it does not, without an additional normalization calculation, establish that the present retained-band `20/3` resource is nearly saturated by the first quadrupole family.

**Action:** add an explicit statement that no retained-band tightness claim is made. Do not add a speculative numerical saturation factor.

## 4. The report's “Helmholtz decomposition” criticism is misframed

The manuscript assumes a normal-mode expansion in the mass Hilbert space, as standard in elastic gravitational-antenna theory. It does not require a Helmholtz decomposition of the material displacement into a “TT part.” The transverse-traceless projection belongs to the radiative gravitational field. Modes with zero quadrupole overlap contribute zero to `q_n:q_n`; they are not assigned spurious gravitational radiation merely because the Bessel sum is written over the modal basis.

The bound can certainly be loose for a retained subset, but the source of that looseness is the projection/truncation and the subsequent frequency ceiling, not the existence of nonradiating modes in the basis.

**Action:** no theorem change.

## 5. Directivity: broad concern valid, bar example wrong

The report correctly recognizes that `25/16` is an optimized propagation ceiling. The manuscript already states that `D\le5/2` is attained by a plus quadrupole viewed along its symmetry-normal direction.

The report's specific bar-antenna example is incorrect. In the ideal slender longitudinal-bar limit the STF quadrupole is axisymmetric, proportional to

```math
q\propto\operatorname{diag}(2,-1,-1)
```

with the first axis along the bar. Substitution into the manuscript's angular form

```math
F_q(\hat n)=q:q-2(q\hat n)\cdot(q\hat n)+\frac12|\hat n\cdot q\hat n|^2
```

gives `F_q=0` when viewed along the bar axis. Thus the report's statement that the optimal receiver should be placed on the bar symmetry axis is the opposite of the idealized quadrupole radiation pattern.

The underlying referee-style concern remains useful: a fixed or polarization-mismatched geometry generally lies below the optimized ceiling.

**Action:** add one sentence making that optimism explicit, without introducing the erroneous bar example.

## 6. Paik–Wagoner / integrated-cross-section claim in the report is not accepted

The report supplies a Lorentzian-looking cross-section formula and then asserts

```text
integrated cross section ∝ M L^2 omega_0^2 / Q.
```

That conclusion is not supported by the checked literature. Aguiar's 2011 resonant-mass review explicitly presents the Paik–Wagoner integrated bar cross section and states that it depends on the first power of antenna mass and the second power of material sound speed; after adding a resonant transducer and splitting the mechanical response into two normal modes, that integrated scaling remains in the first power of `M` and second power of `v`. No `1/Q` scaling of the integrated cross section is stated there.

Moreover, the formula written in the supplied report is itself insufficient to support its stated `1/Q` conclusion without additional damping factors in the numerator.

**Action:** do not add a false `1/Q` comparison. Instead clarify only that historical integrated cross sections and the present energy-normalized selected-port spectral area use different response normalizations and are not identified numerically.

Primary literature boundary retained:

- H. J. Paik and R. V. Wagoner, *Phys. Rev. D* **13**, 2694–2699 (1976), DOI `10.1103/PhysRevD.13.2694`.
- O. D. Aguiar, *Research in Astronomy and Astrophysics* **11**, 1–42 (2011), DOI `10.1088/1674-4527/11/1/001`, arXiv:`1009.1138`.

## 7. Quantum-communication citations

The report's presentation concern is reasonable: a reader may wonder why quantum-communication papers are cited in a classical spectral-area theorem.

**Action:** state explicitly that those works locate the gravity-as-communication context; their quantum-information criteria are not used in the proof. Do not claim that the present theorem is itself a capacity or entanglement bound.

## 8. Scale and practical relevance

The report is correct that the displayed 1-kHz, `k_0R=100` example requires a very large separation and yields an extraordinarily small spectral-area ceiling. The manuscript already says this is a conceptual/architectural result rather than a near-term experimental proposal.

The report overstates this as a universal “astronomical separation” problem: the geometric wave-zone length scales as `c/omega_0`, so the required absolute separation decreases with increasing carrier frequency. That observation does not rescue practical coupling, because realistic carrier-scale mechanical endpoint resources also change strongly with device scale and frequency.

**Action:** no additional practical-performance claim.

## 9. Changes authorized by this audit

Submission-layer exposition only:

1. clarify that complete-basis Parseval saturation does not imply retained-band saturation;
2. state explicitly that `25/16` optimizes orientation/polarization and mismatches lower transfer;
3. distinguish historical integrated-cross-section normalization from `Gamma_coh` without asserting a `Q` law;
4. explain why quantum gravity-communication papers are cited;
5. improve Appendix-B table rendering;
6. rephrase the AI-verification sentence to avoid a misleading column-break hyphenation.

No change is authorized to

- the theorem statement;
- the `20/3`, `4/3`, `25/16`, or `25/12` coefficients;
- the retained-sector assumptions;
- the bounded-port infinite-dimensional scope;
- the recurrence result.

## Final assessment

The supplied report is best treated as a useful hostile-reader simulation. Its favorable overall verdict is encouraging, but its authority is irrelevant: only objections that survive independent mathematical, source, and rendered-document checks are incorporated.
