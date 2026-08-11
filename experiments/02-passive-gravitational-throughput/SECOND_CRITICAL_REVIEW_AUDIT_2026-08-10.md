# Adversarial audit of second reviewer-style critique — 2026-08-10

**Role:** hostile-referee simulation, not authority. Every objection was re-derived or checked against primary literature before manuscript changes were authorized.

## Verdict

The critique contains three useful substantive pressures, two overstatements, and one incorrect recurrence interpretation. The manuscript is stronger after resolving them, but the central `25/12` leading coefficient and endpoint sum rule survive.

## 1. Asymptotic theorem wording — accepted and strengthened

The previous displayed theorem mixed a strict passive cut with a propagation `limsup` and then wrote the final result using `lesssim`. That presentation made it too easy to read the result as a uniform finite-distance bound.

Resolution:

- the theorem is now stated as the precise asymptotic coefficient

```math
\limsup_{k_0R\to\infty}(k_0R)^2\Gamma_{coh}
\le \frac{25G\Omega^4}{12c^5}\min(I_{2,A},I_{2,B});
```

- the familiar carrier form using `omega_0` is explicitly labeled the leading narrowband/compact form;
- the finite-`kR` propagation correction is derived exactly by STF `m`-sector decomposition;
- at `kR=100` the compact-TT propagation correction is `0.99980003`, i.e. about `0.020%` in power;
- no universal finite-source remainder is invented.

## 2. Retained high-frequency modal sector — concern accepted, reviewer wording corrected

The restriction is genuinely consequential. The theorem does not prove that high-frequency off-resonant tails are negligible for a particular material. A full-device application requires either a justified retained model or a separate omitted-sector bound.

The critique's blanket description of a finite body as having a continuous phonon spectrum is not adopted. A finite continuum elastic body has a countable normal-mode spectrum; microscopic lattice physics introduces high-frequency structure beyond the continuum approximation. The real issue is uncontrolled omitted spectral weight, not the word `continuous`.

## 3. Bode--Fano / Chu--Harrington — context gap accepted, equivalence claim rejected

Primary-source check:

- Fano 1950 studies matching a prescribed load impedance to a resistance with a reactive network and derives integral relations involving `log |reflection coefficient|`.
- Chu 1948 and Harrington 1960 constrain antenna `Q`, gain/directivity, efficiency, and electrical size.

These are close conceptual precedents for passive gain--bandwidth and size--bandwidth tradeoffs, so they belong in the manuscript.

They are not mathematically identical to the present selected-port `H2` cut, and they do not supply the gravity-specific steps

```math
Tr(K_g^\dagger K_g) -> I_2
```

or

```math
TT propagation -> 25/16
```

or the two-ended `min(I_2A,I_2B)` closure. The manuscript now says explicitly that the generic passive redistribution principle is not the novelty claim.

Primary references added:

- R. M. Fano, J. Franklin Inst. 249, 57--83 (1950), DOI 10.1016/0016-0032(50)90006-8.
- L. J. Chu, J. Appl. Phys. 19, 1163--1175 (1948), DOI 10.1063/1.1715038.
- R. F. Harrington, J. Res. NBS 64D, 1--12 (1960), DOI 10.6028/jres.064D.003.

## 4. Is the ceiling remotely tight? — concern accepted, answered without unsafe normalization matching

Rather than equating the paper's energy-normalized `Gamma_coh` to a historical absorption cross section with a different convention, the revision adds a self-contained canonical bar check.

For an ideal slender free--free bar with fundamental longitudinal mode

```math
w_x=sin(pi x/L),
```

one obtains

```math
mu=M/2,
I_2=ML^2/12,
(q:q)/mu=64 ML^2/(3 pi^4),
```

and therefore

```math
\frac{(q:q)/\mu}{(20/3)I_2}
=\frac{192}{5\pi^4}
\simeq 0.394.
```

So a single idealized bar mode already occupies about 39% of the endpoint Bessel resource. Its axisymmetric quadrupole has maximum directivity `15/8`, compared with the unrestricted STF maximum `5/2`.

This shows that the endpoint and angular constants are not loose by dozens of orders of magnitude solely because of the sum-rule/directivity relaxations. It does **not** show that real resonant-mass detectors approach the full two-ended selected-port spectral-area ceiling. The revised manuscript says that explicitly.

## 5. Communication motivation — accepted as a framing issue

The quantum gravity-communication papers were removed from the opening motivation. The introduction now starts from resonant transduction, integrated response, passive systems, and classical gain--bandwidth theory. Quantum communication papers remain only in the prior-work discussion, where the manuscript says their information-theoretic criteria are not used in the proof.

This makes the delivered result match the stated question: a classical passive coherent-transfer spectral-area ceiling, not a claim about usable information capacity.

## 6. Recurrence objection — rejected

The critique confuses endpoint reflectivity with propagation norm.

The exact result is

```math
\|P_eff\| <= p_+/(1-p_+ p_-),
```

because `||R_A||,||R_B||<=1`. The round-trip loop contains **two propagation factors**. Even if both endpoint reflection blocks have norm one, the loop norm is at most `p_+ p_-`.

In the far zone, `p_+,p_-=O(1/kR)`, so `p_+p_-=O((kR)^-2)<<1`. Near-unit endpoint reflectivity therefore cannot drive the loop toward unity while the separated-wave assumption remains valid. The Taylor series is used only to identify the order of the correction; the resolvent inequality itself is exact whenever `p_+p_-<1`.

The manuscript now says this explicitly.

## 7. Manuscript-style constraint

The submission paper must not discuss internal source-control, code-hosting, commit identifiers, or project bookkeeping. Such provenance belongs in internal research records, not in the physics article. All such references were removed from the manuscript source. Numerical checks remain described scientifically as independent validation calculations.

## Net scientific effect

The second critique did not expose an arithmetic failure or invalidate the endpoint/resource/directivity chain. It did expose a presentational weakness in the theorem statement and a real prior-context omission. The response therefore improves rigor rather than merely adding disclaimers:

- exact asymptotic theorem statement;
- explicit finite-distance compact-TT propagation correction;
- Bode--Fano/Chu--Harrington context with a clear gravity-specific boundary;
- ideal resonant-bar tightness benchmark;
- stronger retained-sector limitation;
- corrected recurrence interpretation;
- narrower motivation aligned with the actual result.
