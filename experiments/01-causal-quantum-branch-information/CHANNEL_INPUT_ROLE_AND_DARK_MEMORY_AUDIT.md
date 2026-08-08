# Channel-Input Role and Gravitationally Dark Memory Audit

**Date:** 2026-08-07  
**Status:** **CONCEPTUAL SCOPE CORRECTION — DISTINGUISH THE DOWNSTREAM GAUSSIAN CHANNEL FROM THE LOCAL PREPARATION OPERATION**

## 1. Why this clarification is necessary

Two local source constructions are now available:

1. `EXACT_LOCAL_GAUSSIAN_SOURCE_ENCODER.md` — a degenerate source qubit controls the sign of a swap from a branch-common work mode into the mechanical source;
2. `LOCAL_BOSONIC_INPUT_SWAP_CHANNEL.md` — an arbitrary local bosonic memory mode is swapped directly into the mechanical source.

Both are mathematically useful, but they answer different operational questions.

The strongest paper should not blur them.

---

# 2. The downstream Gaussian channel

The physically important propagation/capture map is the bosonic channel

$$
\boxed{
\Phi_{A\to B}(t)
}
$$

from the radiating source/gravitational input mode $A$ to the receiver mode $B$.

For the passive source with vacuum ordinary loss, its source-resolved transmissivity is schematically

$$
\tau_{A\to B}(t)=\eta_g\tau_f(t),
$$

with receiver noise

$$
m_B(t).
$$

This channel is non-entanglement-breaking iff

$$
\boxed{
\eta_g\tau_f(t)>m_B(t)
}
$$

or the corresponding full-waveform version with $\tau_{\rm full}$.

The Gaussian EB statement belongs to this bosonic propagation channel.

---

# 3. The source qubit is a retained reference, not the Gaussian channel input

In the sign-controlled encoder, start with a source qubit

$$
R
$$

in a superposition and create

$$
\boxed{
|\Psi\rangle_{RA}
\propto
|0\rangle_R|+\alpha\rangle_A
+|1\rangle_R|-\alpha\rangle_A.
}
$$

The qubit remains at the source.

It is the **reference system** used to test whether the downstream bosonic channel preserves entanglement.

One should not call the reduced map

$$
R\to B
$$

the same Gaussian non-EB channel.

Indeed, for a purely $\sigma_z$-controlled preparation, tracing out the retained qubit removes its off-diagonal coherences from the receiver-alone state. The reduced qubit→receiver map is therefore not the object whose Gaussian EB boundary is being used.

The correct statement is

$$
\boxed{
(I_R\otimes\Phi_{A\to B})
(|\Psi\rangle\langle\Psi|)
\text{ can remain entangled}
}
$$

when the downstream bosonic channel is non-EB.

---

# 4. Why the sign-controlled encoder is physically attractive

Before the local encoder starts, choose

- a degenerate internal source qubit whose logical states have the same local energy/stress profile to the accuracy of the model;
- finite-spoke mechanical vacuum;
- a branch-common energetic work/controller mode;
- branch-independent gravitational/environment state.

The local sign-controlled swap then creates the branch-dependent mechanical quadrupole.

Thus the **gravitational source difference begins with the local encoding operation** rather than being assumed as a pre-existing branch-displaced mass configuration.

All encoding-stage graviton radiation is explicitly counted.

This is a clean causal entanglement-distribution protocol:

$$
\boxed{
\text{local preparation of }R\!:\!A
\to
\Phi_{A\to B}
\to
R\!:\!B\text{ entanglement test}.
}
$$

---

# 5. Arbitrary local bosonic memory: mathematically stronger, physically more demanding

`LOCAL_BOSONIC_INPUT_SWAP_CHANNEL.md` begins with an arbitrary bosonic memory state

$$
\rho_d
$$

and swaps it into the finite-spoke source.

At the level of local quantum input-output theory this is ideal: it defines a genuine arbitrary bosonic Gaussian input and gives an exact matched gravitational output channel

$$
\mathcal L_{\eta_g}
$$

when the full encoder-plus-tail temporal mode is retained.

However, a physical arbitrary bosonic state generally has state-dependent

- energy;
- stress-energy fluctuations;
- gravitational charges/multipoles.

Therefore it is too strong to assume, without further construction, that the **full gravitational environment before the swap is independent of every possible state of $d$**.

This does not invalidate the Gaussian channel algebra. It narrows the strict causal interpretation of an arbitrary pre-existing bosonic input.

---

# 6. Equal energy is not enough for arbitrary-state gravitational darkness

For the binary coherent pair

$$
|+\alpha\rangle,
\qquad
|-\alpha\rangle,
$$

the mean oscillator energy is equal.

That fact is helpful, but by itself it does not prove that a microscopic memory has exactly branch-independent

$$
T^{\mu\nu}(x)
$$

or identical gravitational dressing for every superposition in its logical span.

Likewise, an arbitrary Gaussian input includes states with different mean excitation number, so no fixed gravitational field can generally be independent of all possible inputs if the memory's own stress-energy is included exactly.

Therefore “arbitrary local bosonic input” should be understood as an **effective source-laboratory channel input** unless an explicit gravitationally dark memory encoding is supplied.

---

# 7. Gravitationally dark memory as an optional stronger construction

A stricter physical implementation could encode information into an internal degenerate subspace whose states share the same external gravitational charges/multipoles to the working perturbative order.

Examples conceptually include

- degenerate internal states;
- phase/polarization-like degrees of freedom with branch-common macroscopic stress-energy;
- encoded subspaces designed so the relevant low-order stress moments are identical.

The local encoder would then convert that hidden/internal information into the radiating mechanical quadrupole only after the causal clock starts.

This idea is consistent with the perturbative gravitational-splitting viewpoint: localized information can be arranged so that, outside a region, only the relevant global gravitational charges are exposed to leading order.

A complete microscopic dark-memory construction is not presently derived in the repository.

---

# 8. Recommended paper hierarchy

Use the following hierarchy to avoid a category error.

## A. Fundamental local causality statement

A localized source intervention cannot change receiver observables outside its future light cone.

This is the role of

- `MICROCAUSAL_REPLACER_THEOREM.md`;
- `CAUSAL_SOURCE_INTERVENTION_PROTOCOL.md`.

## B. Explicit local entangled-probe preparation

Use the sign-controlled encoder to create

$$
R\!:\!A
$$

entanglement from a branch-common controller and initially nonradiating mechanical source.

This gives a concrete causal origin for the branch-dependent quadrupole.

## C. Downstream Gaussian channel

Apply the source/emission/propagation/receiver map

$$
\Phi_{A\to B}
$$

and test whether it preserves the locally prepared entanglement.

This is where the non-EB condition belongs.

## D. Arbitrary bosonic communication channel

`LOCAL_BOSONIC_INPUT_SWAP_CHANNEL.md` gives the exact effective Gaussian construction.

Advertise it as a fully physical arbitrary-input gravitational communication channel only after the input memory's own gravitational distinguishability has been controlled.

---

# 9. Causal clock for the entangled-probe protocol

For the clean sign-controlled preparation, define

$$
\boxed{t=0}
$$

as the beginning of the localized encoder coupling.

Before that time,

- the mechanical source is branch common;
- the work mode is branch common;
- the internal reference qubit can be chosen degenerate/gravitationally indistinguishable at the working order.

During encoding,

- opposite mechanical amplitudes develop;
- precursor gravitational radiation is emitted;
- that precursor is included in the complete source waveform.

Therefore the earliest possible receiver dependence on the local preparation remains

$$
\boxed{R/c}
$$

from the first spacetime support of the encoder.

---

# 10. What the experiment actually demonstrates

The strongest current operational question is not

> can an arbitrary hidden bosonic memory be teleported into the receiver with no prior gravitational dressing?

It is

> can a **locally prepared entangled source-mode probe** retain entanglement with its source reference after the radiating mode propagates gravitationally to a distant noisy receiver?

For the covered Gaussian receiver channel, this is equivalent to asking whether the downstream source-mode→receiver channel is non-entanglement-breaking.

That question is both sufficient for the paper's core physics and cleaner than overextending the arbitrary-memory interpretation.

---

# 11. Consequence for novelty language

The paper should say

> We construct a local source preparation that creates a branch-dependent conserved quadrupole with a branch-common controller, then propagate the resulting bosonic source mode through a normalized gravitational channel to a noisy receiver and determine when the downstream channel preserves source-reference entanglement.

Avoid the stronger unqualified statement

> We construct an arbitrary gravitationally isolated bosonic communication input whose complete prehistory is independent of its quantum state.

The latter has not been established.

---

# 12. Verdict

### Sign-controlled local probe preparation

$$
\boxed{\text{GO}}
$$

at the normal-mode level, with coupler stress-energy retained in the controller error budget.

### Downstream source-mode→receiver Gaussian channel

$$
\boxed{\text{GO}}
$$

with the existing source branching, storage, thermal-noise, and finite-size corrections.

### Arbitrary pre-existing bosonic input as an exactly gravitationally dark register

$$
\boxed{\text{NOT YET ESTABLISHED}}
$$

and not needed for the central entanglement-distribution claim.

---

## Related files

- `EXACT_LOCAL_GAUSSIAN_SOURCE_ENCODER.md`
- `LOCAL_BOSONIC_INPUT_SWAP_CHANNEL.md`
- `PASSIVE_SOURCE_INITIALIZATION_CAUSALITY_AUDIT.md`
- `MICROCAUSAL_REPLACER_THEOREM.md`
- `CAUSAL_SOURCE_INTERVENTION_PROTOCOL.md`
- `PASSIVE_END_TO_END_CHANNEL.md`
