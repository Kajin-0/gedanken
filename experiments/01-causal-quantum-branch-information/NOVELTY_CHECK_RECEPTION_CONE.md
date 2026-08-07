# Novelty Check — Quantum Reception Cone

**Timestamp:** 2026-08-07 17:25 EDT  
**Status:** Targeted literature check; finite quantum range itself is established in neighboring free-space quantum communication, while the exact time-resolved NPT-front construction remains potentially distinctive.

## Candidate gravity construction

For a finite-aperture wave-zone gravitational receiver, the useful branch-mode coupling behaves asymptotically as

$$
\kappa_\Delta(R)=\frac{K}{R^2}.
$$

With stationary thermal injection $\Gamma_{\rm th}$, define

$$
R_Q=\sqrt{K/\Gamma_{\rm th}}.
$$

The exact waveform-optimal finite-cat NPT front is

$$
\boxed{
T_{\rm NPT}^{\min}(R)
=
\frac Rc-
\frac1{\kappa_0+K/R^2}
\ln[1-(R/R_Q)^2],
\qquad R<R_Q.
}
$$

No NPT front exists for $R\ge R_Q$ within the model, and the front diverges logarithmically as $R\to R_Q^-$.

---

## 1. Finite quantum range is not new by itself

Free-space quantum-communication theory already treats distance-dependent transmissivity, diffraction/aperture loss, atmospheric loss, background thermal noise, and resulting limits on entanglement/secret-key distribution.

For example, Pirandola (2021, arXiv:2012.01725) derives fundamental bounds for satellite/free-space quantum communication including diffraction, extinction, background noise, and fading, and explicitly studies achievable entanglement/key distribution versus propagation distance.

Thus the broad statement

> finite aperture + distance-dependent loss + background noise can impose a finite useful quantum-communication range

is established neighboring physics and should not be claimed as new.

---

## 2. What is sharper in the current construction

The present receiver model adds an explicit **dynamical quantum memory/capture process** after the retarded gravitational mode reaches the receiver.

The resulting prediction is not only a static condition such as

$$
\text{channel non-EB at distance }R.
$$

It is a spacetime boundary:

$$
\boxed{
T_{\rm NPT}^{\min}(R)-R/c
=-\kappa_{\rm tot}^{-1}(R)
\ln\left[1-\Gamma_{\rm th}/\kappa_\Delta(R)\right].
}
$$

The light cone fixes the first allowed signal arrival; receiver dynamics impose a later entanglement-build latency. As the local source-matched receiver channel approaches its EB surface, this latency diverges logarithmically.

The targeted search did not locate this exact combination of:

1. retarded field arrival;
2. normalized-waveform-optimal capture;
3. exact binary coherent NPT condition;
4. logarithmic entanglement-onset delay;
5. finite-distance vertical asymptote.

---

## 3. Neighboring entanglement-onset literature

Prior literature contains many examples of

- entanglement sudden birth/death in thermal reservoirs;
- distance-dependent entanglement generation through bosonic baths;
- threshold times for entanglement generation in interacting systems.

For example, Zell, Queisser & Klesse (2008, arXiv:0812.3782) analyze distance-dependent entanglement generated through a bosonic heat bath and find strong distance suppression.

These are conceptually related but are not the same operational problem as a controlled branch-dependent propagating mode arriving at a separately modeled receiver and being captured against a thermal EB threshold.

---

## 4. Current novelty boundary

### Established / do not claim

- finite quantum communication range caused by loss and thermal/background noise;
- aperture/diffraction dependence of free-space quantum links;
- entanglement sudden birth after finite interaction time;
- distance-dependent bath-mediated entanglement;
- thermal bosonic-channel entanglement-breaking thresholds.

### Potentially distinctive

The exact **retarded receiver NPT-front law**

$$
T_{\rm NPT}^{\min}(R)
=
R/c-\kappa_{\rm tot}^{-1}(R)
\ln[1-\Gamma_{\rm th}/\kappa_\Delta(R)]
$$

and its finite-aperture specialization with a logarithmically divergent front at $R_Q$, especially when combined with the exact binary coherent Gaussian-channel theorem and gravitational spin-2 mode overlap.

This remains **novelty unverified**.

---

## 5. Safest paper wording

Do not say:

> We predict that thermal noise gives gravitational quantum communication a finite range.

That is too broad and overlaps standard noisy-channel physics.

Prefer:

> Within a retarded, mode-matched gravitational receiver model, we derive the waveform-optimal **earliest source-receiver NPT time** as a function of range. Finite aperture makes the source-matched coupling decay as $R^{-2}$, causing the NPT front to bend away from the ordinary light cone and diverge logarithmically at the receiver's local entanglement-breaking radius.

This isolates the potentially distinctive result from established free-space quantum-channel range limitations.
