# Hirakawa–Narihara–Fujimoto 1976 Collision Audit

## Source

H. Hirakawa, K. Narihara, and M.-K. Fujimoto, **“Theory of Antennas for Gravitational Radiation,”** *Journal of the Physical Society of Japan* **41**, 1093–1101 (1976), DOI `10.1143/JPSJ.41.1093`.

Primary full text inspected directly.

---

## 1. Executive verdict

This paper is substantially closer prior art to Experiment 02 than the earlier abstract-only audit established.

It already contains, in one compact resonant-antenna framework,

```text
compact mechanical eigenmodes
-> quadrupole-defined gravitational oscillator strength
-> gravitational emission
-> gravitational reception
-> emission/reception reciprocity
-> directivity
-> Q-independent short-pulse response.
```

It therefore eliminates novelty for several ingredients that had previously been treated only as generic historical background.

However, it does **not** state the Experiment 02 end-to-end theorem

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[\operatorname{Tr}\Gamma_{g,A},
     \operatorname{Tr}\Gamma_{g,B}],
```

nor does it close both endpoint resources by a cumulative mass-quadrupole EWSR and insert a normalized free-space TT singular channel between two separated passive endpoint networks.

**Collision verdict:** strong ingredient-level collision; no full theorem collision found.

---

## 2. Scope is already close to the compact mechanical regime

The paper explicitly restricts itself to resonant antennas and assumes the antenna linear dimension `l` is sufficiently small compared with the gravitational wavelength,

```text
l / lambda_G << 1.
```

The antenna is expanded in elastic eigenmodes `w_n`, each with eigenfrequency `omega_n` and a reduced mode mass. Thus the source/receiver object is already a compact mechanical normal-mode system rather than an extended electromagnetic Hertz radiator.

This is much closer to the material regime of Experiment 02 than Grishchuk–Sazhin's active, wavelength-scale electromagnetic source.

---

## 3. The same mode oscillator strength controls emission

For a vibration in mode `n`, Hirakawa et al. define the dynamic STF quadrupole tensor `q_{n alpha beta}` and a gravitational effective area

```math
A_{Gn}
=
\frac{2\sum_{\alpha\beta}q_{n\alpha\beta}^{2}}
{M\int\rho\sum_\alpha w_{n\alpha}^{2}dV}.
```

Their differential radiated gravitational power is

```math
p(\theta,\phi)d\Omega
=
\frac{G}{20\pi c^5}
A_{Gn}T_nM\omega_n^4
f_n(\theta,\phi)d\Omega,
```

where `T_n` is the mode kinetic energy and the directivity is normalized by

```math
\int f_n(\theta,\phi)d\Omega=4\pi.
```

The total radiated power is

```math
P
=
\frac{G}{5c^5}
A_{Gn}T_nM\omega_n^4.
```

Therefore the combination `M A_Gn` is already a mode-level gravitational oscillator-strength resource built directly from the dynamic mass quadrupole.

This is conceptually very close to the mode resource represented in Experiment 02 by a one-quantum gravitational linewidth `kappa_{g,n}`.

---

## 4. Reception uses the same quadrupole resource

For a monochromatic incident gravitational field, the paper derives the driven mode amplitude and the resonant stored energy. At resonance,

```math
E
=
\frac{2\pi G}{5c^3}
M Q_n^2 A_{Gn}
f_n(\theta,\phi)S\gamma,
```

where `S` is the incident gravitational energy flux and `gamma` is the polarization matching factor.

Thus the same `A_Gn` that fixes gravitational emission also fixes reception.

This is not merely analogy: Sec. 6 proves a gravitational reciprocity theorem and explicitly states that the emitting and receiving directivity patterns are the same.

Consequently the claim that a compact resonant matter mode has one common gravitational coupling resource governing both emission and reception is historical prior art.

---

## 5. The short-pulse formula is already a Q-independent integrated-response result

This is the most important collision.

For a short unpolarized gravitational pulse with spectral energy density `F(nu)`, Hirakawa et al. obtain

```math
\boxed{
E
=
\frac{\pi^3G}{5c^3}
M\nu_n^2A_{Gn}
f_n(\theta,\phi)F(\nu_n).
}
```

There is **no quality factor `Q_n` in this expression**.

Because `F(nu_n)` is incident pulse energy per unit area per unit frequency, the coefficient

```math
\Sigma_n(\theta,\phi)
\equiv
\frac{E}{F(\nu_n)}
=
\frac{\pi^3G}{5c^3}
M\nu_n^2A_{Gn}f_n(\theta,\phi)
```

is precisely an integrated-absorption / oscillator-strength-type quantity for the mode.

So Experiment 02 must not claim novelty for any of the following:

```text
Q-independent integrated gravitational response
compact-mode gravitational oscillator strength
using one quadrupole resource for emission and reception
pulse response controlled by spectral energy density rather than peak resonance.
```

This historical result is closer than a generic resonant-bar citation because it is derived in the same unified emission/reception eigenmode framework.

---

## 6. The directivity value 5/2 is also already present

Hirakawa et al. derive explicit directivity patterns for compact quadrupole antenna modes.

For their B-mode family,

```math
f(\theta,\phi)
=
\frac52
-\frac52\sin^2\theta
+\frac58\sin^4\theta\cos^22\phi.
```

Along the symmetry axis,

```math
f(0,\phi)=\frac52.
```

Thus the numerical compact-quadrupole directivity value `D = 5/2` is not a new observation of Experiment 02.

Experiment 02 still contributes a cleaner operator statement for arbitrary complex STF transition tensors,

```math
D_Q(\hat n)
=
\frac52
\frac{Q^*:\Lambda(\hat n):Q}{Q^*:Q}
\le\frac52,
```

and converts this to the normalized one-graviton propagation singular-value ceiling

```math
\|P_g\|_{\rm op}^2
\le
\frac{25}{16(kR)^2}.
```

But the underlying maximum directivity value itself must be treated as historical antenna physics, not novelty.

---

## 7. What Hirakawa et al. do **not** do

Despite the strong ingredient overlap, several load-bearing Experiment 02 steps are absent.

### No separated source-to-receiver transfer function

The paper treats the emission and reception characteristics of a gravitational antenna and proves reciprocity, but it does not construct a local-input-to-local-output transfer matrix for two separated passive material endpoints linked through free propagation.

There is no analogue of

```math
T(\omega)
=
S_{v\leftarrow g}^{(B)}(\omega)
P_g(\omega)
S_{g\leftarrow u}^{(A)}(\omega).
```

### No passive selected-port H2 cut set

There is no frequency-integrated matrix inequality of the form

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[\operatorname{Tr}\Gamma_{g,A},
     \operatorname{Tr}\Gamma_{g,B}].
```

The paper does not prove that arbitrary passive internal coherent mixing, overlapping resonances, or local port matching cannot exceed the smaller endpoint gravitational coupling trace.

### No cumulative EWSR closure across all passive modes

`A_Gn` is a single-mode quantity. The paper classifies many possible GR-active eigenmodes, but it does not derive a basis-independent cumulative resource ceiling such as

```math
\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
```

Thus it does not close the many-parallel-resonance loophole by a total oscillator-strength sum rule.

### No normalized free-space singular channel between two radiative subspaces

Emission/reception reciprocity and directivity are derived, but the paper does not factor two microscopic matter-field couplings as

```math
G_B^\dagger U_RG_A
=
\Gamma_{g,B}^{1/2}
P_g
\Gamma_{g,A}^{1/2}
```

or prove a separated source-to-receiver singular-value ceiling for `P_g`.

### No quantum-information corollaries

There is no channel-capacity or entanglement-distribution interpretation.

---

## 8. Revised novelty boundary

After full-text inspection, the following are definitively **not** novelty claims for Experiment 02:

- compact resonant gravitational antenna eigenmode theory;
- quadrupole-controlled gravitational emission strength;
- the same oscillator-strength parameter governing emission and reception;
- gravitational antenna reciprocity;
- Q-independent short-pulse / integrated resonant response;
- compact quadrupole directivity reaching `5/2`;
- optimization of mechanical readout loading and thermal noise.

The surviving candidate contribution is narrower:

> **A many-mode end-to-end passive resource theorem:** established passive selected-port H2 identities are combined with microscopic gravitational coupling traces at two separated compact matter endpoints, a cumulative mass-quadrupole EWSR closure of both traces, and a normalized free-space TT singular channel to bound the frequency-integrated local-port-to-local-port coherent transfer.

Symbolically,

```text
historical compact antenna oscillator strength + reciprocity
                         ↓
known passive H2 cut-set machinery
                         ↓
source gravitational coupling trace
                         ↓
normalized propagating TT singular channel
                         ↓
receiver gravitational coupling trace
                         ↓
cumulative EWSR closure at both endpoints
                         ↓
end-to-end integrated transfer ceiling.
```

No equivalent theorem was found in the inspected Hirakawa paper.

---

## 9. Publication-significance risk after this audit

The risk is no longer that the theorem is algebraically wrong.

The sharper referee objection is now:

> The paper may be a technically correct synthesis of known gravitational antenna oscillator-strength/reciprocity physics, known passive H2 mathematics, and a known quadrupole sum rule, rather than a fundamentally new physical principle.

That objection cannot be answered by claiming that emission, reception, integrated response, or `D=5/2` are new; they are not.

The manuscript must instead make clear that its candidate contribution is the **architecture-independent two-ended closure** that removes `Q`, mode count, internal coherent mixing, and compact orientation from the final integrated ceiling.

Whether that synthesis is significant enough for publication is a referee/editor judgment, not something the internal audit can settle.

---

## 10. Updated decision

```text
PHYSICS THEOREM:                    GO WITH DECLARED SCOPE
HIRAKAWA FULL-TEXT COLLISION:       STRONG INGREDIENT COLLISION
COMPACT EMISSION/RECEPTION THEORY:  HISTORICAL
Q-INDEPENDENT PULSE RESPONSE:       HISTORICAL
D = 5/2 DIRECTIVITY VALUE:          HISTORICAL
PASSIVE H2 TWO-END CUT SET:         NO COLLISION FOUND HERE
CUMULATIVE BOTH-END EWSR CLOSURE:   NO COLLISION FOUND HERE
NORMALIZED TT RESOURCE SANDWICH:    NO COLLISION FOUND HERE
EXACT FULL THEOREM COLLISION:       NOT FOUND
NOVELTY:                            PROVISIONAL GO, NARROWER CLAIM
PRIORITY LANGUAGE:                  NO
V7 MODIFICATION:                    NO
THEOREM BROADENING:                 NO
```

---

## 11. Required manuscript correction

Before external specialist review, manuscript v1 should explicitly cite Hirakawa et al. and state that compact gravitational antennas with common emission/reception oscillator strength, reciprocity, Q-independent pulse response, and directivity up to `5/2` are historical.

The introduction should no longer contrast the present problem with a purely “receiver-only” historical literature. Older generator-detector calculations and unified emission/reception antenna theory both exist.

The paper should lead with the actual new candidate object:

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int
\operatorname{Tr}[T^\dagger T]d\omega
```

bounded by the smaller of two **cumulatively EWSR-limited** gravitational endpoint coupling resources through a normalized free-space TT channel.
