# Hostile Prior-Art Collision Audit — Experiment 02

**Purpose:** assume the Experiment-02 result is already known and try to identify the exact historical collision under gravitational-antenna, resonant-mass, generator–receiver, oscillator-strength, absorption-cross-section, or generic wave-channel notation.

**Audit stance:** a negative search result is not proof of priority. This file is designed to narrow claims, not manufacture novelty.

## 1. Candidate result under attack

Within the current bounded-port passive, compact, narrowband, leading-wave-zone class, Experiment 02 has independently reconstructed

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}),
```

where

```math
I_2=\int\rho r^2d^3x
```

and `Gamma_coh` is a complex-envelope coherent-transfer spectral area.

The audit asks whether the **complete closure** already appears in older work, even if expressed through effective area, cross section, modal mass, oscillator strength, or generator–receiver signal formulas.

## 2. Collision matrix

| Source | Established content relevant here | Collision classification | Consequence for Experiment 02 |
|---|---|---|---|
| Hirakawa, Narihara & Fujimoto, JPSJ 41, 1093 (1976), DOI `10.1143/JPSJ.41.1093` | Eigenmode gravitational-antenna theory; emission, reception, directivity, thermal-noise/coupling discussion | **INGREDIENT PRIOR ART** | No novelty claim for eigenmode emission/reception, reciprocity/directivity framework, or compact gravitational antenna normalization |
| Paik & Wagoner, Phys. Rev. D 13, 2694 (1976), *Calculation of the absorption cross section of a cylindrical gravitational-wave antenna* | Resonant-mass gravitational absorption/cross-section theory for a cylindrical antenna | **STRONG NEAR-COLLISION / INGREDIENT PRIOR ART** | Integrated/spectral gravitational response of resonant matter is historical; do not sell Experiment 02 as the first integrated passive response bound |
| Aguiar, arXiv:1009.1138, review of resonant-mass detectors | Explicitly reviews an **integrated cross section** for a bar and notes that after adding a resonant transducer, producing two normal modes, the integrated cross section still scales with first power of mass and second power of sound speed | **STRONG NEAR-COLLISION** | Strong evidence that mode splitting / added passive resonance does not create unlimited integrated gravitational response was already understood. Standalone many-mode or Q-independence novelty is not safe |
| Lobo, Phys. Rev. D 52, 591 (1995), arXiv:`gr-qc/0006102` | General formalism for arbitrary solid elastic-body response to metric GW perturbations; mass-orthogonal eigenmodes, multimode transfer, absorption cross sections, STF/tidal-force structure | **STRONG INGREDIENT PRIOR ART** | Arbitrary-body modal projection, long-wavelength tidal influence fields, multimode transfer and STF completeness are historical. The `20/3` Bessel contraction is not safe as a standalone novelty claim |
| Srivastava, Widom & Pizzella, arXiv:`gr-qc/0302024` | Exact microscopic total GW cross-section formulation at lowest order in `G`; dispersion relations and frequency-integrated sum rules for material response | **STRONG METHOD / SUM-RULE PRIOR ART** | Gravitational material-response sum-rule methodology is historical. Experiment 02 cannot claim novelty for using a cumulative material-response resource or a frequency integral by itself |
| Grishchuk & Sazhin, Sov. Phys. JETP 41, 787 (1975) | Historical laboratory high-frequency GW generation/detection / Hertz-experiment analysis | **GENERATOR–RECEIVER PRIOR ART** | End-to-end gravitational generation/detection calculations are historical |
| Rudenko, arXiv:`gr-qc/0307105` | Explicit optimization of a complete generator–receiver gravitational Hertz couple; source power, receiver sensitivity, coherent radiators/receivers, wave mismatch, geometry and frequency optimization | **STRONG TWO-ENDED NEAR-COLLISION** | The existence of complete source–receiver calculations is not new. Rudenko is architecture-specific and detectability/SNR-based rather than an endpoint-eliminated passive spectral-area theorem |
| Miller, Appl. Opt. 39, 1681 (2000), DOI `10.1364/AO.39.001681` | Orthogonal wave communication channels between arbitrary volumes and limits on connection strengths | **GENERIC METHOD PRIOR ART** | No novelty claim for source–receiver SVD/channel decomposition or generic coupling-strength limits |
| Molesky, Venkataram, Jin & Rodriguez, Phys. Rev. B 101, 035408; arXiv:`1907.03000` | Shape-independent two-body radiative-transfer limits using material response and wave propagation constraints | **GENERIC TWO-BODY BOUND PRIOR ART** | No novelty claim for the abstract architecture “endpoint response constraints + propagation operator -> transfer bound” |
| Baras & Brockett (1975); Opmeer, Reis & Wollner (2013) | Infinite-dimensional `H2` realizations and operator Lyapunov/Gramian machinery | **GENERIC SYSTEMS PRIOR ART** | No novelty claim for the countably infinite bounded-port extension mathematics |
| Redheffer, J. Math. Phys. 41, 1 (1962), DOI `10.1002/sapm19624111` | Scattering/transfer composition and repeated network returns | **GENERIC SCATTERING PRIOR ART** | No novelty claim for the recurrence resolvent/star-product mathematics |

## 3. Most damaging historical collision: integrated resonant-mass response

Aguiar's resonant-mass review explicitly writes an integrated absorption cross section

```math
\int_0^\infty \sigma_n(\nu)d\nu
```

for a bar antenna and attributes the result to Paik & Wagoner (1976). More importantly for Experiment 02, the review states that adding a resonant transducer changes the mechanical system from one harmonic oscillator to two normal modes, but the **integrated cross section continues to depend on the first power of antenna mass and second power of sound speed**.

This is a direct historical warning against claiming that Experiment 02 newly discovered the general idea that extra passive resonances cannot manufacture unlimited integrated gravitational response.

Accordingly:

```text
integrated resonant-mass GW cross section:             HISTORICAL
mode splitting preserves a finite integrated resource: STRONG HISTORICAL PRECEDENT
Q / resonance-count independence as broad concept:     DO NOT CLAIM AS NOVEL
```

The surviving Experiment-02 question is narrower: whether arbitrary compact passive endpoint response can be eliminated at **both ends** into the scalar second moments `I_2A,I_2B`, then combined with the compact TT propagation ceiling into one end-to-end `min(I_2A,I_2B)/R^2` spectral-area bound.

## 4. Stage-B standalone novelty is strongly narrowed

Lobo's arbitrary-body framework already contains the physical ingredients needed to project long-wavelength gravitational tidal forcing onto mass-orthogonal elastic modes and to treat multimode response. Srivastava–Widom–Pizzella already provide gravitational material-response dispersion and sum-rule machinery.

The Experiment-02 identity

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I_2
```

is a short Bessel/Parseval consequence once the STF tidal influence fields are written explicitly. The present audit has not located the exact coefficient `20/3` in the inspected primary sources, but that absence is not enough to justify a standalone novelty claim.

Current claim discipline:

```text
STF tidal-force fields:                    HISTORICAL
arbitrary-body modal projection:           HISTORICAL
modal completeness / effective mass logic: HISTORICAL
response sum-rule methodology:             HISTORICAL
20/3 as standalone mathematical novelty:   DO NOT CLAIM
4/3 endpoint resource as standalone novelty: DO NOT CLAIM
```

The `20/3` and `4/3` formulas remain useful proof lemmas in the final closure even if they are historically implicit or derivable from established ingredients.

## 5. Strongest complete-generator–receiver near-collision

Rudenko's 2003 paper is explicitly about optimizing a **couple generator–receiver** for a gravitational Hertz experiment. It derives a signal-to-noise expression for the complete couple and studies coherent numbers of radiators/receivers, source/receiver powers, wave mismatch, geometry and operating frequency.

This defeats any broad claim that Experiment 02 is the first complete gravitational source–receiver link analysis.

However, in the inspected paper Rudenko retains architecture-specific quantities such as deformation amplitude, material sound velocity, thermal noise, coherent element counts, geometry and frequency mismatch. It does not state the Experiment-02 object

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int d\nu\,\operatorname{Tr}(T^\dagger T)
```

nor eliminate both endpoints into

```math
\min(I_{2,A},I_{2,B})
```

with a universal compact TT propagation coefficient.

Classification: **strong near-collision, not an exact collision found in the inspected text.**

## 6. Generic mathematical novelty is not available

Miller's communication-mode framework already supplies orthogonal source–receiver channels and connection-strength limits for waves between arbitrary volumes. Modern two-body radiative-transfer bounds likewise organize constrained endpoint responses around a propagation operator. Passive `H2`, infinite-dimensional Gramian, and Redheffer recurrence mathematics are all established.

Therefore Experiment 02 should not be positioned as a new general wave-bound method.

The only plausible contribution is the **gravity-specific physical closure** that makes the generic machinery collapse to a simple matter resource at both ends.

## 7. Exact collision search result

Across the inspected gravitational-antenna, resonant-mass, Hertz-experiment, material-response, generic wave-channel, passive-system, and multiple-scattering sources, this audit has **not found** a source stating the complete theorem

```text
selected-port coherent spectral-area cut
-> gravitational coupling trace at source and receiver
-> cumulative compact-matter resource bounded by I_2 at BOTH endpoints
-> compact TT propagation ceiling
-> same-endpoint passive recurrence controlled at leading order
-> explicit end-to-end min(I_2A,I_2B)/R^2 ceiling.
```

Equivalently, no inspected source states

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
```

for the current bounded-port passive narrowband class.

This is a **negative prior-art search result, not proof of priority**.

## 8. Final hostile novelty matrix

```text
gravity antenna eigenmode theory:                  HISTORICAL
arbitrary-body modal GW projection:                HISTORICAL
STF tidal/completeness machinery:                   HISTORICAL
integrated resonant-mass cross section:             HISTORICAL
mode-splitting finite integrated response:          HISTORICAL STRONG PRECEDENT
gravity material-response sum rules:                HISTORICAL
generator–receiver Hertz calculations:              HISTORICAL
generic source–receiver channel/SVD math:            HISTORICAL
generic two-body response + propagation bounds:     HISTORICAL
finite/infinite passive H2 machinery:                HISTORICAL
multiple-scattering recurrence:                     HISTORICAL
20/3 standalone novelty:                            NO CLAIM
4/3 standalone novelty:                             NO CLAIM
complete two-ended inertia-only closure:            NO EXACT COLLISION FOUND
priority claim:                                     NO
```

## 9. Publication consequence

If Experiment 02 becomes a paper, the manuscript should be organized around one narrow statement:

> established gravitational-antenna and passive-wave ingredients combine into an explicit cumulative **two-ended inertia ceiling** for frequency-integrated coherent propagation through weak linearized gravity.

The paper should lead with the final bound, credit the historical integrated-cross-section/multimode precedents early, and avoid presenting the intermediate modal and systems machinery as new.

The remaining risk is now **significance/priority judgment**, not an identified internal correctness defect inside the declared model.

## 10. Primary sources used in this audit

- H. Hirakawa, K. Narihara, M.-K. Fujimoto, *Theory of Antennas for Gravitational Radiation*, J. Phys. Soc. Jpn. **41**, 1093–1101 (1976), DOI `10.1143/JPSJ.41.1093`.
- H. J. Paik and R. V. Wagoner, *Calculation of the absorption cross section of a cylindrical gravitational-wave antenna*, Phys. Rev. D **13**, 2694 (1976).
- O. D. Aguiar, *The Past, Present and Future of the Resonant-Mass Gravitational Wave Detectors*, arXiv:`1009.1138`.
- J. Alberto Lobo, *What can we learn about GW Physics with an elastic spherical antenna?*, Phys. Rev. D **52**, 591 (1995), arXiv:`gr-qc/0006102`.
- Y. N. Srivastava, A. Widom, G. Pizzella, *Electronic Enhancements in the Detection of Gravitational Waves by Metallic Antennae*, arXiv:`gr-qc/0302024`.
- V. N. Rudenko, *Optimization of parameters of a couple generator-receiver for a gravitational Hertz experiment*, arXiv:`gr-qc/0307105`.
- D. A. B. Miller, *Communicating with waves between volumes: evaluating orthogonal spatial channels and limits on coupling strengths*, Appl. Opt. **39**, 1681–1699 (2000), DOI `10.1364/AO.39.001681`.
- S. Molesky, P. S. Venkataram, W. Jin, A. W. Rodriguez, *Fundamental limits to radiative heat transfer: theory*, Phys. Rev. B **101**, 035408, arXiv:`1907.03000`.
- J. S. Baras and R. W. Brockett, *H2-Functions and Infinite-Dimensional Realization Theory*, SIAM J. Control **13**, 221–241 (1975), DOI `10.1137/0313013`.
- M. R. Opmeer, T. Reis, W. Wollner, *Finite-Rank ADI Iteration for Operator Lyapunov Equations*, SIAM J. Control Optim. **51**, 4084–4117 (2013), DOI `10.1137/120885310`.
- R. Redheffer, *On the Relation of Transmission-Line Theory to Scattering and Transfer*, J. Math. Phys. **41**, 1–41 (1962), DOI `10.1002/sapm19624111`.
