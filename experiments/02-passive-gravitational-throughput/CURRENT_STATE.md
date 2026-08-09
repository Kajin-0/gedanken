# Current State — Experiment 02

**Status:** **MANUSCRIPT V1 THEOREM CHECKPOINT CLOSED; PHYSICS GO WITH DECLARED SCOPE; NOVELTY PROVISIONAL GO; FURTHER BROADENING PAUSED**

## 1. Headline result

For a direct narrowband link between compact passive nonrelativistic **linear bosonic** source and receiver networks, coupled through quadrupolar linearized gravity in the weak one-way wave zone, define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
```

The current theorem gives

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

where `I_A` and `I_B` are internal mass inertia moments about each endpoint center of mass.

The result contains no endpoint quality factor, no assumed number of passive internal modes, and no four-spoke-specific parameter. It is a frequency-integrated coherent-transfer / efficiency-bandwidth bound, **not itself a quantum capacity**.

Experiment 01 / V7 remains frozen at its submission-ready scientific state and is not modified by this branch.

---

## 2. Proof chain

### A. Passive-network cut set

For a stable completely passive endpoint,

```math
A=-iH-\frac12K^\dagger K.
```

Using established passive-system Gramian identities,

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

Arbitrary finite-dimensional passive coherent mode mixing and overlapping resonances are allowed. The underlying Gramian/H2 mathematics is established prior art; the candidate contribution is the gravity-specific end-to-end closure.

Canonical file: `PASSIVE_NETWORK_CUTSET_THEOREM.md`.

### B. Microscopic gravitational-port factorization

For the narrowband matter-to-graviton coupling operator,

```math
G=V\Gamma_g^{1/2},
\qquad
\Gamma_g=G^\dagger G,
```

so that

```math
\boxed{
G_B^\dagger U_RG_A
=
\Gamma_{g,B}^{1/2}
P_g
\Gamma_{g,A}^{1/2}.
}
```

This separates endpoint coupling magnitude from normalized gravitational mode geometry and prevents double counting. Nonorthogonal radiation patterns are retained through the gravitational Gram matrix.

Canonical file: `GRAVITATIONAL_PORT_FACTORIZATION.md`.

### C. Passive mass-quadrupole resource

For passive linear bosonic matter,

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n},
```

with one-quantum quadrupole rate

```math
\kappa_{g,n}
=
\frac{2G\omega_n^5}{5\hbar c^5}
Q_{ij}^{0n}Q_{ij}^{n0}.
```

The mass-quadrupole EWSR then gives, for retained modes below operating ceiling `Omega`,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
}
```

The inertia moment is defined internally about the endpoint center of mass.

Canonical files: `MATERIAL_RESPONSE_BRIDGE.md`, `SPECTRAL_GENERALIZATION.md`.

### D. Compact TT propagation ceiling

For arbitrary complex STF quadrupole `Q`,

```math
D_Q(\hat n)
=\frac52\frac{Q^*:\Lambda Q}{Q^*:Q}
\le\frac52.
```

The normalized one-graviton stationary-phase overlap gives

```math
\boxed{
t_{BA}^{\rm TT}
=-\frac{5i}{4kR}e^{ikR}
\frac{Q_B^*:\Lambda(\hat R):Q_A}
{\sqrt{Q_A^*:Q_A}\sqrt{Q_B^*:Q_B}}
+O((kR)^{-2}),
}
```

and therefore

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le
\frac{25}{16[k(\omega)R]^2}
}
```

at leading wave-zone order.

Canonical files: `TT_PROPAGATION_BOUND.md`, `INDEPENDENT_TT_COEFFICIENT_CHECK.md`.

---

## 3. Exact two-resonator specialization

For explicit source and receiver local ports,

```math
\boxed{
\Gamma_{\rm EBP}
=
\frac{4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
}
```

For symmetric intrinsic gravitational rates with no internal loss, the integrated spectral-area optimum occurs at

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
```

with

```math
\boxed{
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
}
```

Thus peak-optimal critical coupling and throughput-optimal coupling are different objectives.

Canonical file: `TWO_PORT_SPECTRAL_BOUND.md`.

---

## 4. Quantum-information corollaries

`Gamma_coh` is not a capacity. For a stationary vacuum pure-loss realization, however, every transmission eigenvalue satisfies

```math
\tau_n(\omega)\le\eta_{\max}.
```

If `eta_max <= 1/2`, then

```math
\boxed{Q_1=0}
```

for unassisted asymptotic pure-loss quantum capacity.

For `eta_max < 1`,

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}
}
```

for the two-way-assisted pure-loss rate.

These are channel-specific corollaries, not universal noisy-gravity capacity statements.

Canonical file: `CAPACITY_COROLLARIES.md`.

---

## 5. Explicit realization and sharpness

The frozen V7 long-wavelength plus mode reaches 30% of the endpoint-only EWSR gravitational-linewidth ceiling and saturates the compact TT geometry ceiling. The combined theorem is an upper bound and is **not** claimed globally sharp; simultaneous saturation of the passive cut set, EWSR ceiling, and propagation ceiling remains open.

Canonical file: `BENCHMARK_THEOREM_COMPARISON.md`.

---

## 6. Prior-art boundary

The easy novelty story is explicitly rejected.

Historical resonant-mass gravitational-wave antenna theory already contains integrated absorption-response physics in which increasing Q raises peak response while narrowing bandwidth. Susceptibility/Kubo descriptions of gravitational absorption are also established. Passive linear quantum-network Gramian theory and modern continuous-time transducer capacity/efficiency-bandwidth metrics are established as well.

Therefore Experiment 02 does **not** claim novelty for

- Q-independent integrated gravitational response;
- integrated gravitational absorption cross sections;
- susceptibility-based gravitational absorption;
- passive Gramian/H2 mathematics;
- generic efficiency-bandwidth transducer metrics.

The candidate contribution is the narrower **two-ended direct far-field closure**:

```text
source passive gravitational spectral resource
-> normalized propagating TT channel
-> receiver passive gravitational spectral resource
-> integrated end-to-end coherent-transfer cut set
-> pure-loss quantum-information corollaries.
```

Targeted searches have not yet found an inspected source stating the same theorem. This is a negative search result, not proof of priority.

Canonical files: `INITIAL_NOVELTY_SWEEP.md`, `LITERATURE_MAP.md`.

---

## 7. Validation checkpoint

Four independent numerical regression layers are present:

1. exact two-pole spectral area and random passive rate sets;
2. random multimode passive Gramians and directly integrated cascades;
3. random complex STF quadrupoles, TT directivity, angular normalization, and the `25/16` wave-zone coefficient;
4. microscopic gravitational-port factorization with deliberately overlapping radiation patterns.

GitHub Actions run `31311724347`, job `93240439026`, completed successfully with all four layers passing.

The theorem also passed a written adversarial audit without a fatal internal gap inside the declared class. Remaining risks are novelty collision and global sharpness rather than an identified algebraic inconsistency.

Canonical file: `ADVERSARIAL_THEOREM_AUDIT.md`.

---

## 8. Manuscript v1 checkpoint

A theorem-first manuscript now exists at

```text
manuscript_v1/
```

with working title

**Passive Throughput Bounds for Propagating Gravitational Quantum Transduction**.

Its structure is deliberately independent of V7:

1. historical one-sided gravitational absorption as prior physics;
2. passive-network cut set;
3. microscopic gravitational-port normalization;
4. mass-quadrupole spectral resource;
5. compact TT propagation ceiling;
6. combined theorem;
7. exact two-resonator example;
8. pure-loss capacity corollaries;
9. scope and routes around the theorem.

The V7 four-spoke realization appears only as a late sanity check.

Final manuscript-v1 compile after visual cleanup:

- workflow run: `31312356701`
- job: `93241979746`
- head SHA: `f3f09bf977f61b304082ac727cb26752cc264a11`
- LaTeX compilation: **PASS**
- unresolved reference/citation scan: **PASS**
- PDF artifact upload: **PASS**

Rendered PDF QA:

- 13 pages;
- all pages open/render correctly;
- no clipping, broken equations, or obvious overflow;
- hyperlink boxes removed with `hidelinks`;
- no personal identity or repository-name leakage detected in extracted PDF text.

---

## 9. Publication decision

Current formal decision:

```text
PHYSICS THEOREM:       GO WITH DECLARED SCOPE
NUMERICAL VALIDATION:  GO
MANUSCRIPT V1:         GO
NOVELTY:               PROVISIONAL GO, NARROW CLAIM
V7 MODIFICATION:       NO
THEOREM BROADENING:    PAUSED FOR THIS PAPER
```

Do **not** broaden this manuscript to arbitrary interacting/non-Markov matter unless an external criticism makes that necessary.

---

## 10. Hard stop / next trigger

Experiment 02 should now be treated as a frozen manuscript-v1 theorem checkpoint.

Reopen the physics only for one of the following:

1. a concrete counterexample or proof defect;
2. a prior-art collision with the two-ended theorem;
3. an external specialist/referee objection;
4. a clearly separable extension paper on active/nonpassive resources, extended apertures, near-field channels, or interacting susceptibility theory.

### Forbidden claims

- “first gravitational efficiency-bandwidth bound”;
- “new Q-independent gravitational response law”;
- “universal gravitational quantum capacity bound”;
- “all passive matter”;
- first/unique/unprecedented language without much stronger priority evidence;
- applying `25/16` to extended arrays, higher multipoles, or the near field;
- claiming the final coefficient is globally saturable;
- merging Experiment 02 physics into frozen V7.
