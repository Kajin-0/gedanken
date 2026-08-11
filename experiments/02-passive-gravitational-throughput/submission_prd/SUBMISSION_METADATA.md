# PRD Submission Metadata

## Article

- Journal: Physical Review D
- Article type: Research Article
- Title: *An Inertia-Controlled Spectral-Area Bound for Passive Far-Zone Gravitational Transduction*
- Underlying validated science/theorem checkpoint: `bfae23af41aefb3104d639099299b3432b4a14fe`
- Validated submission-manuscript checkpoint after APS-policy alignment: `6f7a60b3b05dea9f288b1b07e6f2e55acaf34e83`
- Submission-layer source: this `submission_prd/` directory

The submission checkpoint changes only Acknowledgments/Data Availability and submission-support documentation; it does not change the theorem or scientific derivation relative to the underlying science checkpoint.

## Author

- Author name: Terence Fisher
- Affiliation: Brooks Photonics
- Email: terence@brooks-photonics.com
- ORCID: [REQUIRED FOR CORRESPONDING AUTHOR — PROVIDE/AUTHENTICATE IN APS SYSTEM]
- Corresponding author: Terence Fisher

## Suggested subject framing

- Gravitation
- Gravitational-wave theory / propagation
- Passive linear systems / resonant-mass response as supporting methodology

Do not classify the paper primarily as quantum information or detector instrumentation.

## One-sentence significance

Within the compact retained-modal passive far-zone class, arbitrary passive resonant complexity can reshape but cannot increase the leading frequency-integrated gravitational power-transmission spectral area beyond a two-ended ceiling fixed by the smaller separation-axis endpoint inertia resource and transverse-traceless propagation.

## Current theorem shorthand

Rigorous far-zone coefficient:

```math
\limsup_{R\to\infty}R^2\Gamma_{\rm coh}
\le
\frac{5G\Omega^4}{4c^3\omega_-^2}
\min(I_{\hat R,A},I_{\hat R,B}).
```

Carrier-scale narrowband form:

```math
\Gamma_{\rm coh}
\lesssim
\frac{5G\omega_0^2}{4c^3R^2}
\min(I_{\hat R,A},I_{\hat R,B}).
```

The former `25/12 * I_2` result remains a valid looser scalar corollary.

## Metric discipline

`Gamma_coh` is a band-limited squared `H2` norm / power-transmissivity spectral area with units `s^-1`. It is not a bit rate, information capacity, detector sensitivity, waiting time, or strain-noise PSD.

## Novelty boundary

Present the contribution as the complete two-ended sector-resolved far-zone inertia closure. Historical ingredients include resonant-mass integrated response, gravitational-antenna modal theory, material sum rules, classical matching/antenna limits, passive `H2` methods, multiple scattering, generic wave-channel bounds, and gravity-mediated communication in general. Do not make a priority claim from a negative literature search.

## Final-preflight exact-head validation

Submission checkpoint `6f7a60b...` passed:

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

Compiled artifact:

```text
name: experiment02-prd-submission
artifact ID: 9103729907
artifact ZIP digest: sha256:a31ee561019906b28e2e8ecb2ca25f9ce98b1ef0260e1f354198ce2a073b6b98
PDF SHA256: ea23e976ed9c1b3f210539c9310b4e4ad80e137eee7cbd82098fedbb9f3906bf
```

See `../FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md` for the full visual, policy, reference, and continuity audit.

## Submission-history fields

- Previously submitted to APS? [CONFIRM]
- Concurrent submission elsewhere? MUST BE NO at submission
- Related manuscripts / joint submission? [CONFIRM]
- Preprint posted? [CONFIRM; ADD IDENTIFIER IF YES]

## Referees

Recommended referees: [OPTIONAL — HUMAN SELECTION]

Excluded referees: [OPTIONAL — HUMAN SELECTION WITH REASON]

## Data/software availability

The manuscript states that no experimental data were created or analyzed and that numerical verification code supporting Appendix D is available from the author upon reasonable request. Do not place project source-control identifiers in the article.

## Internal reproducibility record

Internal source-control and workflow identifiers may be kept here for project recovery, but must not be copied into the physics manuscript or cover letter. The current recovery record is `RECOVERY_INDEX.md`; theorem-constant compatibility is recorded in `CONSTANT_REGRESSION_AUDIT_2026-08-10.md`.

## Disclosure

The manuscript contains a substantive-AI disclosure in the Acknowledgments. It identifies OpenAI ChatGPT, identifies GPT-5.6 Sol for the final pre-submission revision, describes the scientific and manuscript tasks assisted, and explains author direction and verification. Exact earlier per-session model identifiers were not systematically archived; no retrospective list is invented.
