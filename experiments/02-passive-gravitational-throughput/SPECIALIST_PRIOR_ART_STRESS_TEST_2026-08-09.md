# Specialist Prior-Art Stress Test — 2026-08-09

## Purpose

This audit attacks the remaining publication risk in Experiment 02 after the manuscript-v1 theorem checkpoint: not whether individual ingredients are known, but whether older gravitational-antenna literature already contains the same two-ended passive integrated resource theorem under different language.

The frozen theorem checkpoint and V7 are not modified by this audit.

---

## 1. Current theorem under test

Experiment 02 defines

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega
```

and, for direct weak one-way wave-zone propagation between compact passive nonrelativistic linear bosonic endpoints, derives

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min\!\left(\langle I_A\rangle,\langle I_B\rangle\right).
```

The proof chain is

```text
passive H2 endpoint cut set
-> microscopic gravitational-port factorization
-> mass-quadrupole EWSR closure at both endpoints
-> normalized compact TT propagation singular-value ceiling.
```

The question in this audit is whether that complete conjunction is old.

---

## 2. Internal specialist attack on the physics bridge

### Passive H2 cut set

No new defect was found in the selected-port Gramian step. For a stable completely passive realization,

```math
A=-iH-\frac12K^\dagger K,
```

the full controllability Gramian is the identity, while a selected-input Gramian satisfies

```math
0\le P_u\le I.
```

Therefore

```math
\|S_{g\leftarrow u}\|_2^2
=\operatorname{Tr}(K_gP_uK_g^\dagger)
\le\operatorname{Tr}(K_g^\dagger K_g).
```

Applying the same resource cut from either endpoint gives the minimum of the two endpoint gravitational coupling traces. The H2/Gramian mathematics is established prior art; the issue is only its gravity-specific closure.

### Microscopic port factorization

The factorization

```math
G=V\Gamma_g^{1/2},
\qquad
\Gamma_g=G^\dagger G,
```

and hence

```math
G_B^\dagger U_RG_A
=\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2},
\qquad
P_g=V_B^\dagger U_RV_A,
```

continues to cleanly separate endpoint coupling magnitude from normalized radiation-mode geometry. Nonorthogonal radiation patterns are retained through the Gram matrix rather than assumed to be independent ports.

The remaining normalization sensitivity is the usual band-local Markov convention connecting microscopic continuum coupling to the input-output matrix `K_g`. No concrete factor-of-two or `2 pi` inconsistency was found because the equality `K_g^dagger K_g = G^dagger G` is the defining normalization of the retained gravitational port sector.

### Mass-quadrupole EWSR coefficient

The coefficient was rechecked independently. For an orthonormal STF basis `E^a_ij` and

```math
Q_a=\sum_r m_r E^a_{ij}x_{r,i}x_{r,j},
```

the STF completeness relation gives

```math
\sum_{a,k}E^a_{kj}E^a_{kl}=\frac53\delta_{jl}.
```

Using the ordinary nonrelativistic coordinate Hamiltonian double commutator then yields

```math
\sum_a\frac12\langle[Q_a,[H,Q_a]]\rangle
=\frac{10}{3}\hbar^2\langle I\rangle.
```

Combined with the standard one-graviton quadrupole transition rate

```math
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}Q^*:Q,
```

this reproduces

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le\frac{4G}{3c^5}\langle I\rangle\Omega^4.
```

No coefficient defect was found inside the declared ordinary-nonrelativistic-matter scope.

### One-way TT propagation

The most sensitive remaining physics point is not the leading `25/16` coefficient, which has independent V7 checks, but the one-way projection implicit in replacing the full translated angular overlap by the outgoing `+R` stationary contribution. A fully reciprocal common-bath treatment would contain feedback/cross-damping terms. Experiment 02 explicitly assumes weak one-way direct wave-zone propagation, so this is presently a scope condition rather than an identified error.

**Physics verdict of this pass:** no new fatal defect found.

---

## 3. Historical collision found: two-ended gravitational links are not new

The previous novelty language placed too much weight on the fact that both source and receiver interfaces are retained. Older literature already studies complete gravitational generator-receiver systems.

### Grishchuk and Sazhin — 1975

L. P. Grishchuk and M. V. Sazhin, *Excitation and detection of standing gravitational waves*, Sov. Phys. JETP 41, 787 (1975/1976 translation).

The work is explicitly a generation-and-detection problem. It belongs to the historical electromagnetic/standing-wave laboratory program rather than the present passive compact-matter propagating-wave-zone class, but it blocks any generic novelty claim based only on placing a generator and detector in one calculation.

### Hirakawa, Narihara, and Fujimoto — 1976

H. Hirakawa, K. Narihara, and M. Fujimoto, *Theory of Antennas for Gravitational Radiation*, J. Phys. Soc. Jpn. 41, 1093–1101 (1976).

The publisher abstract explicitly states that the work treats both emission and reception characteristics and the directivity pattern of gravitational antennas. This is the closest unresolved historical collision candidate found in this pass because it potentially combines reciprocity, directivity, emission, and reception in one antenna framework.

The full article was not available through the inspection route used here, so the exact degree of overlap with the Experiment 02 integrated two-ended resource inequality remains unresolved. This paper must be inspected in full before any priority-sensitive manuscript wording is finalized.

### Grishchuk — 1977 and 2003

L. P. Grishchuk's laboratory-gravity work explicitly discusses a complete source-plus-detector experiment. The later review *Electromagnetic Generators and Detectors of Gravitational Waves* emphasizes that the efficiency of generation and detection must be evaluated jointly and describes a detector placed in the standing/focal gravitational field of an electromagnetic emitter.

This is not the same architecture as Experiment 02: it is active electromagnetic, spatially extended, and based on a focal/standing field rather than a direct compact passive far-field hop. Nevertheless, it establishes that complete end-to-end generator-detector bookkeeping is historical.

### Rudenko — 2003

V. N. Rudenko, *Optimization of parameters of a couple generator-receiver for a gravitational Hertz experiment*, arXiv:gr-qc/0307105.

Rudenko explicitly formulates a complete “generator-receiver” gravitational Hertz couple and writes signal-to-noise expressions for the pair near the wave-zone boundary. Again, this is an engineering/active architecture rather than the Experiment 02 passive H2 theorem, but it further eliminates any broad novelty claim for a two-ended gravitational link itself.

### Füzfa — 2017/2018

A. Füzfa, *Electromagnetic Gravitational Waves Antennas for Directional Emission and Reception*, arXiv:1702.06052.

This work develops directional electromagnetic gravitational-wave emission and reception and explicitly places it in the lineage of earlier generation-and-detection laboratory proposals. It is active and extended-aperture, hence outside the theorem class, but is important neighboring prior art.

---

## 4. Claim correction forced by this audit

The following novelty language is now too broad:

```text
"two-ended gravitational link"
"retaining both matter-gravity interfaces"
"source plus propagating gravity plus receiver"
```

These concepts are historical in sufficiently broad form.

The surviving candidate contribution must be stated at the level of the actual inequality:

> A frequency-integrated passive H2 resource bound for a direct compact quadrupolar wave-zone link, in which the abstract gravitational coupling traces at both endpoints are independently closed by the mass-quadrupole EWSR and the middle free-space channel is bounded by a normalized TT singular value.

Equivalently, the potentially distinctive conjunction is

```text
passive selected-port H2 cut set
+ source gravitational coupling trace
+ receiver gravitational coupling trace
+ EWSR closure of both traces
+ normalized compact TT propagation singular-value ceiling
+ end-to-end integrated coherent-transfer bound
+ channel-specific pure-loss corollaries.
```

No inspected source in this pass was found to state that full conjunction.

That remains a negative search result, not proof of priority.

---

## 5. Consequence for manuscript v1

The theorem manuscript is presently **literature-incomplete** even though no physics defect was found.

Before submission, the introduction and bibliography should acknowledge at least the historical complete generator-receiver line represented by

- Grishchuk and Sazhin (1975);
- Hirakawa, Narihara, and Fujimoto (1976);
- Grishchuk (1977; later review 2003);
- Rudenko (2003);
- Füzfa (2017/2018), where useful for the modern active-emission/reception context.

The manuscript should then distinguish Experiment 02 not by the existence of a two-ended system, but by the passive integrated-resource inequality and its microscopic closure.

No manuscript edits are made in this audit because the theorem checkpoint is intentionally frozen until the highest-risk historical source, Hirakawa et al. (1976), is inspected in full.

---

## 6. Updated publication decision

```text
PHYSICS THEOREM:                 GO WITH DECLARED SCOPE
H2 <-> MICROSCOPIC BRIDGE:       NO NEW DEFECT FOUND
EWSR COEFFICIENT:                INDEPENDENTLY RECHECKED
25/16 TT COEFFICIENT:            NO NEW CONTRADICTION
GENERIC TWO-ENDED NOVELTY:       NO — HISTORICAL PRIOR ART
PASSIVE INTEGRATED CLOSURE:      PROVISIONAL GO
MANUSCRIPT LITERATURE STATE:     REVISION REQUIRED BEFORE SUBMISSION
PRIORITY CLAIM:                  NO
V7 MODIFICATION:                 NO
THEOREM BROADENING:              NO
```

---

## 7. Strongest next epistemic step

The next task is no longer another derivation.

1. Obtain and inspect the full Hirakawa–Narihara–Fujimoto 1976 article, specifically searching for an integrated source-to-receiver power/transfer inequality, reciprocity/Friis-style end-to-end formula, oscillator-strength sum, or a bound controlled by both endpoint resources.
2. Inspect the full Grishchuk–Sazhin 1975 calculation for any equivalent far-field two-ended normalization hidden in the standing-wave treatment.
3. If neither contains the Experiment 02 resource inequality, revise manuscript-v1 introduction/bibliography and narrow the novelty language accordingly.
4. Only after that pass should the manuscript be sent for external specialist review.

Do not broaden the theorem while this prior-art gate remains open.
