# Adversarial Referee Pass on V7 — 2026-08-08

**Scope:** current V7 manuscript after the main derivations and normalization audits were integrated.  
**Question:** do strong referee-style objections expose a new physics failure, or mainly framing, scope, and feasibility limitations?

## Review provenance

This is a **repository-level adversarial review record**, not formal journal peer review. The critiques came from independent AI-agent review passes and were then checked against the manuscript, supporting derivations, primary literature, and numerical tests. No external physicist, journal, or institution is represented as having endorsed the work.

## Overall verdict

No new algebraic or structural physics failure was found.

The review passes did identify several real vulnerabilities that were worth making explicit in the manuscript:

1. the four-factor result could be mistaken for a bookkeeping identity;
2. the passive benchmark could be misread as a universal gravitational bound;
3. macroscopic source coherence was not initially stated prominently enough as a prerequisite;
4. the approximation hierarchy needed an explicit statement about mixed higher-order corrections.

Those points are now stated directly in V7.

---

## 1. Is the central factorization only bookkeeping?

Central result:

```math
\tau_c(t)=
\beta_{g,A}\,
\eta_{\rm store}(R)\,
\beta_{g,B}\,
\mathcal T_f(t).
```

### Concern

A product of emission, propagation, absorption, and temporal-overlap efficiencies is structurally familiar. If each factor were independently assumed, the multiplication would not itself be a new physical result.

### V7 answer

Agreed. The product form is explicitly described as standard.

The contribution is the **common operational normalization** connecting the stages without inserting an already normalized incoming graviton wavepacket:

- source branching is measured relative to the complete locally prepared branch-distance norm;
- propagation is normalized as a reciprocal one-graviton source-to-receiver mode overlap;
- receiver branching is normalized to the physical receiver linewidth;
- memory capture and later readout are kept distinct.

**Status: CLOSED as a framing vulnerability.**

The remaining publication question is whether this integration is sufficiently consequential for the journal.

---

## 2. Is source gravitational branching a fundamental tiny number?

```math
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A}.
```

If nongravitational damping vanished,

```math
\kappa_A=\kappa_{g,A}
\quad\Rightarrow\quad
\beta_{g,A}=1.
```

Therefore the small benchmark branching fraction cannot be a universal gravitational bound.

### V7 answer

Correct. The small benchmark value is a **finite-bandwidth passive operating point**.

For the benchmark, the intrinsic gravitational lifetime is about

```math
4.6\times10^{17}\ \mathrm{yr}.
```

Reducing nongravitational loss can raise the gravitational branching fraction toward unity, but then emission occurs on the extremely slow intrinsic gravitational timescale.

**Status: CLOSED.**

---

## 3. How universal is the four-spoke source result?

The explicit finite-spoke elastic source demonstrates a consistent conserved architecture. It does not prove that every gravitational quantum emitter has the same microscopic branching behavior.

V7 treats the construction as an explicit controlled source model, not a universal theorem about all possible matter or transducers. The passive spectral-weight arguments are likewise restricted to their stated passive, nonrelativistic regime.

**Status: CLOSED by scope.**

---

## 4. Does the one-way product survive reciprocal dynamics?

A complete source-field-receiver system is reciprocal and can contain reabsorption and delayed feedback.

V7 uses the one-way result as the leading term of a controlled weak-feedback regime. The audited loop amplitude obeys

```math
|L(\nu)|
\le
4\eta_{\rm store}\beta_{g,A}\beta_{g,B},
```

and the first source-controlled round-trip echo appears only after approximately `3R/c`.

**Status: CLOSED at the stated weak one-way order.**

---

## 5. What exactly is the `25/16` quantity?

Classical emitted power, extinction, scattering, absorption, coherent mode overlap, and stored quantum probability are not automatically interchangeable.

The V7 storage coefficient is supported by three conceptually distinct calculations:

1. retarded conserved-source field;
2. reciprocal radiation / critical quadrupole absorption;
3. canonical transverse-traceless one-graviton mode overlap.

The third route gives the operational chain

```math
\text{normalized emitted one-graviton mode}
\to
\text{reciprocal receiver amplitude}
\to
|t_{BA}|^2
\to
\eta_{\rm store}
```

in the weak one-way wave zone and reproduces the complete radial polynomial

```math
P(z)=3-3iz-3z^2+2iz^3+z^4.
```

Thus

```math
|t|^2=
\frac{25}{16z^2}
\left(1-\frac{2}{z^2}+\frac{3}{z^4}-\frac{9}{z^6}+\frac{9}{z^8}\right).
```

The reactive near zone is outside this storage-probability interpretation.

**Status: CLOSED at the stated wave-zone order.**

---

## 6. Is gravitational splitting being asked to prove too much?

First-order gravitational splitting does not prove exact tensor-factor locality or absence of all exterior gravitational fields.

V7 requires only

```math
V_{\mathcal C}^{\dagger}Q_A V_{\mathcal C}=q_A I_{\mathcal C}
```

for the total Poincare generators at the retained perturbative order.

A common long-range gravitational dressing may remain. The claim is that the logical branch is absent from the first-order charge data, while later branch-dependent multipole radiation carries the causal signal.

**Status: CLOSED at first perturbative order.**

---

## 7. Is the virtual difference mode a new physical oscillator?

No.

The collective coordinate

```math
d=\frac{1}{A}\sum_j\alpha_j^*b_j
```

is a basis-defined compression of the coherent displacement vector. It is not a newly postulated localized oscillator or an additional physical particle mode.

Its physical content is the complete branch-dependent coherent norm and its projection onto the receiver-coupled modes.

**Status: CLOSED as an interpretation vulnerability.**

---

## 8. What about macroscopic source coherence?

The link coefficient is conditional on successfully preparing and preserving source-reference coherence during the relevant protocol interval.

The kilogram-scale benchmark does **not** include a device-specific calculation of thermal, vibrational, material, controller, or measurement-induced decoherence for realizing such a macroscopic coherent mechanical source.

A real experiment would require

```math
T_{\rm coherence}>T_{\rm protocol}.
```

This practical requirement may be more restrictive than the already tiny gravitational transfer coefficient.

**Status: explicit limitation, not solved experimental engineering.**

---

## 9. Do the separate approximations hide dangerous cross terms?

V7 uses several controlled small parameters. In the regular perturbative regime, simultaneous independent corrections enter at higher product order, schematically including terms such as

```math
O(q^2\beta^2),
\qquad
O\!\left(q_c^2\frac{B}{\omega}\right),
```

while some mixed structure is already explicit, for example

```math
O(\beta^2\epsilon_u^2).
```

The manuscript does **not** claim a universal all-orders remainder bound. If a small parameter ceases to be small or a singular/resonant regime is approached, the separated expansion must be replaced by the corresponding coupled calculation.

**Status: controlled at the stated perturbative order; no all-orders claim.**

---

## Final referee-level assessment

The strongest surviving criticism is not a demonstrated normalization error or inconsistent source. It is the higher-level publication question:

> Is the common source-to-readout normalization a sufficiently important conceptual advance beyond the already known individual ingredients?

V7's physical distinction is

```math
\boxed{
\text{receiver-local gravitational quantum sensitivity}
\neq
\text{end-to-end source-resolved quantum transfer}
}
```

because the source must first place its branch-dependent quantum record into the gravitational radiation channel.

The passive value near `10^-42` quantifies that distinction for one aggressive ordinary-matter operating point. It is not the theorem and not a universal gravitational bound.

## Publication verdict

**No new publication-blocking physics defect was found in these adversarial review passes.**

That statement is an internal research assessment, not peer review. The remaining uncertainty is normal referee judgment about conceptual significance, generality, and presentation.
