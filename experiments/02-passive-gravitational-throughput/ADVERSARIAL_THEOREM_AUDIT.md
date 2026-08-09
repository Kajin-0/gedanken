# Adversarial Theorem Audit — Experiment 02

## Verdict at this checkpoint

The current narrowband theorem appears internally coherent for the declared class,

```text
compact passive nonrelativistic linear bosonic endpoints
+ quadrupole coupling to linearized gravity
+ stable band-local passive Markov dynamics
+ direct weak one-way wave-zone propagation.
```

No fatal algebraic inconsistency has been identified in this audit. The main remaining risks are **scope creep**, a hidden collision with more general passive-network/scattering literature, and extending the microscopic material step beyond the regime actually justified.

The theorem should not yet be called universal.

---

## 1. Attack: `Gamma_coh` is just an arbitrary bandwidth convention

### Objection

A referee could argue that multiplying efficiency by a linewidth merely trades one arbitrary definition for another.

### Resolution

The mature result no longer uses a chosen linewidth. It uses

```math
\Gamma_{\rm coh}
=\frac1{2\pi}
\int d\omega\,
\operatorname{Tr}[T^\dagger T].
```

This is a frequency-integrated scattering quantity with fixed traveling-field normalization. In the one-pole model it reproduces an exact Lorentzian area.

### Residual caveat

The envelope model is narrowband. Extending the detuning integral formally to infinity is exact only inside that rotating-frame Markov model; physically, its remote tails lie outside the approximation. Corrections are negligible only when the retained linewidths are small compared with the carrier and the integral is dominated by the modeled band.

**Status: CLOSED WITH NARROWBAND SCOPE.**

---

## 2. Attack: high Q still makes gravitational branching approach unity

### Objection

Let ordinary loss vanish so `beta_g -> 1`; then the efficiency suppression disappears.

### Resolution

The integrated two-port result is

```math
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
```

As ordinary damping is removed, the useful linewidth collapses toward the intrinsic gravitational linewidth. The passive-network theorem generalizes the same result without referring to Q.

**Status: CLOSED.**

---

## 3. Attack: stack arbitrarily many passive resonances

### Objection

Even if each resonance has tiny area, a sufficiently dense forest of resonances could make the total throughput arbitrarily large.

### Resolution

The endpoint cut-set depends on the basis-invariant total gravitational coupling trace,

```math
\operatorname{Tr}(K_g^\dagger K_g),
```

and the quadrupole EWSR bounds the cumulative positive gravitational transition-rate weight below the operating ceiling:

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
```

Adding modes redistributes a finite spectral resource unless it also increases the physical inertia/matter resource or leaves the assumed class.

**Status: CLOSED FOR LINEAR BOSONIC MATTER.**

---

## 4. Attack: coherent mode mixing or superradiant bright modes beat the sum

### Objection

Collective interference can produce bright modes with decay rates much larger than those of the uncoupled components.

### Resolution

The gravitational damping matrix is a Gram matrix. Internal unitary mixing can change its eigenvalues but not its trace:

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}.
```

A superradiant bright mode is accompanied by dark/subradiant combinations inside the same passive linear resource budget.

### Residual caveat

Genuinely prepared many-body correlated states that alter the microscopic transition spectral weight, inversion, or active pumping are outside the passive linear ground-state resource statement.

**Status: CLOSED WITH PASSIVITY/LINEARITY SCOPE.**

---

## 5. Attack: linewidth and propagation geometry have been double counted

### Objection

The gravitational linewidth already comes from integrating over radiation directions. Multiplying it by an angular capture factor might count the same coupling twice.

### Resolution

The microscopic matter-field coupling operator has polar decomposition

```math
G=V\Gamma_g^{1/2},
\qquad
\Gamma_g=G^\dagger G.
```

`Gamma_g` contains only coupling magnitude/linewidth, while the partial isometry `V` contains the normalized angular-polarization mode shape. Between two endpoints,

```math
G_B^\dagger U_R G_A
=
\Gamma_{g,B}^{1/2}
P_g
\Gamma_{g,A}^{1/2},
```

with

```math
P_g=V_B^\dagger U_RV_A.
```

Thus the endpoint coupling resource and normalized free-space overlap are mathematically distinct factors.

Canonical note: `GRAVITATIONAL_PORT_FACTORIZATION.md`.

**Status: CLOSED.**

---

## 6. Attack: nonorthogonal radiation patterns invalidate the multimode port model

### Objection

Different matter modes generally radiate overlapping graviton angular patterns, so assigning each mode an independent gravitational port is wrong.

### Resolution

No independent-port assumption is needed. The microscopic coupling vectors `g_n` form a Gram matrix

```math
(\Gamma_g)_{mn}=\langle g_m,g_n\rangle.
```

The polar-decomposition port basis spans only the gravitationally bright radiative subspace. Off-diagonal collective damping is retained.

**Status: CLOSED.**

---

## 7. Attack: `25/16` is an artifact of the four-spoke plus mode

### Objection

Another compact quadrupole tensor might beam more strongly and produce a larger free-space singular channel.

### Resolution

For arbitrary complex STF quadrupole `Q`,

```math
D_Q(\hat n)
=\frac52
\frac{Q^*:\Lambda(\hat n):Q}{Q^*:Q}
\le\frac52
```

because the TT tensor `Lambda` is an orthogonal projector. The normalized one-graviton translated overlap gives

```math
t_{BA}^{\rm TT}
=-\frac{5i}{4kR}e^{ikR}
\frac{Q_B^*:\Lambda Q_A}{\|Q_A\|\|Q_B\|}
+O((kR)^{-2}),
```

so

```math
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}
```

at leading wave-zone order. Matched plus/cross TT tensors saturate the projector inequality.

**Status: CLOSED FOR COMPACT QUADRUPOLES IN THE WAVE ZONE.**

---

## 8. Attack: an extended phased aperture can beam much more strongly

### Objection

Large gravitational antennas can achieve directivity much greater than `5/2`.

### Resolution

Correct. The `5/2` theorem is a compact `l=2` result. An aperture with appreciable spatial phase across its physical extent is outside the compact approximation and must be bounded using its actual aperture/multipole content.

The theorem must never be advertised as a bound on all gravitational antennas.

**Status: OUTSIDE SCOPE, NOT A DEFECT.**

---

## 9. Attack: use the near field instead of radiative propagation

### Objection

Reactive gravitational coupling can scale differently with distance and may evade `1/R^2` power loss.

### Resolution

Yes. Experiment 02 concerns **propagating one-way wave-zone transfer**. Near-field virtual exchange is a different channel and should be analyzed separately.

**Status: OUTSIDE SCOPE.**

---

## 10. Attack: passive relays or intermediate scatterers invalidate the direct-link geometry bound

### Objection

Insert additional material systems between source and receiver so the link is no longer one free-space hop of length `R`.

### Resolution

The current theorem is for a direct source-to-receiver free-space link with no intermediate material relay. A relay creates additional gravitational interfaces and propagation segments and must be included as another passive subsystem.

For a chain of compact passive relays, each additional hop introduces another contractive propagation factor and each relay introduces its own interface resource. A formal multi-hop cut-set theorem is plausible but has not yet been written.

**Status: DECLARED ARCHITECTURE SCOPE; GENERALIZATION OPEN.**

---

## 11. Attack: curved spacetime or gravitational lensing can focus the wave

### Objection

The flat-space diffraction factor need not hold in a curved background.

### Resolution

Correct. The geometry theorem assumes Minkowski-background linearized gravity and direct wave-zone propagation. Lensing, curved-background Green functions, or strongly self-gravitating endpoints are outside scope.

**Status: OUTSIDE SCOPE.**

---

## 12. Attack: the EWSR is not valid for arbitrary matter Hamiltonians

### Objection

The coordinate-space double-commutator identity can change when the microscopic Hamiltonian contains relativistic, velocity-dependent, gauge-field, or other nonstandard terms.

### Resolution

The material theorem is restricted to ordinary compact nonrelativistic matter with the same coordinate-quadrupole commutator assumptions used in V7. The headline should not say “all passive matter.”

For more general systems, the correct resource is the actual positive quadrupole spectral measure; a different microscopic sum rule may replace the `4G<I>Omega^4/(3c^5)` ceiling.

**Status: CLOSED BY EXPLICIT MATERIAL SCOPE.**

---

## 13. Attack: the inertia moment depends on origin

### Objection

`I=sum m r^2` can be increased arbitrarily by translating the coordinate origin.

### Resolution

The internal mass quadrupole and its sum rule must be referred to the endpoint center-of-mass / center-of-energy frame used for the internal multipole expansion. The relevant `I` is the internal inertia moment about that origin.

A translated laboratory origin may make a looser algebraic bound but cannot increase the physical internal quadrupole transition resource.

**Action before manuscript:** state the center-of-mass convention explicitly in the material theorem.

**Status: MINOR CLARIFICATION REQUIRED.**

---

## 14. Attack: a single constant Markov gravitational coupling cannot describe a broad spectrum

### Objection

Quadrupole graviton coupling scales strongly with frequency, so a frequency-independent `K_g` is not valid across widely separated modes.

### Resolution

Correct. The network theorem is band-local. Widely separated resonances are treated as a direct sum of sufficiently narrow Markov sectors; the EWSR bounds the cumulative resource across sectors. A full non-Markov susceptibility realization is a later extension.

The broad-band theorem must retain `omega_-` for the propagation supremum and `omega_+` for the EWSR ceiling rather than using one carrier frequency.

**Status: CLOSED FOR NARROWBAND / LOCAL-SECTOR THEOREM; FULL SUSCEPTIBILITY EXTENSION OPEN.**

---

## 15. Attack: thermal population invalidates the material bridge

### Objection

The passive finite-temperature EWSR carries population differences `(p_m-p_n)`, whereas the harmonic damping constants in `K_g` do not.

### Resolution

The clean coherent-transfer material theorem uses the ground-state/vacuum one-quantum coupling resource. Thermal population is treated as added channel noise. Do not claim the thermal population-weighted net EWSR directly reduces the coherent coupling matrix.

**Status: CLOSED BY GROUND-STATE COHERENT-RESOURCE INTERPRETATION; THERMAL CAPACITY EXTENSION OPEN.**

---

## 16. Attack: `Gamma_coh` is not quantum throughput

### Objection

An integrated transmissivity is not a quantum capacity. In particular, pure-loss channels below `1/2` have zero unassisted quantum capacity.

### Resolution

The project explicitly distinguishes the physical response theorem from capacity. For vacuum pure loss,

```math
Q_1=0
```

when every transfer eigenvalue is at most `1/2`, while

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2(1-\eta_{\max})}
```

provides a two-way-assisted operational corollary.

**Status: CLOSED.**

---

## 17. Attack: zero unassisted capacity contradicts V7's nonzero negativity

### Objection

V7 found nonzero reference-receiver negativity for arbitrarily small pure-loss transmissivity.

### Resolution

There is no contradiction. A channel may transmit some entanglement in a finite use while having zero asymptotic unassisted quantum capacity because it is antidegradable below the pure-loss `1/2` threshold.

**Status: CLOSED.**

---

## 18. Attack: the chained upper bounds may not be simultaneously saturable

### Objection

The passive-network cut set, EWSR material ceiling, and TT propagation maximum might each be saturable separately but not by one physical device simultaneously.

### Resolution

Agreed. The current theorem is an upper bound, not a claim of global sharpness. The explicit V7 long-wavelength four-spoke mode reaches the same scaling and lies only a factor `10/3` below the EWSR linewidth ceiling before additional link factors, while its plus tensor saturates the compact TT directivity ceiling. This is encouraging but does not prove simultaneous saturation of the complete theorem.

Do not call the final coefficient globally optimal until a constructive saturability analysis is performed.

**Status: BOUND VALID; GLOBAL SHARPNESS OPEN.**

---

## 19. Attack: direct local-to-gravity feedthrough bypasses the Gramian resource

### Objection

A general passive scattering system may include a static unitary scattering matrix with a local-input to gravitational-output block.

### Resolution

Such a block is an additional physical conversion element. The current theorem assumes the local/gravity conversion is mediated by the modeled material degrees of freedom. Any genuine direct converter must be included explicitly and assigned its own physical gravitational resource.

This assumption is now stated in the canonical current state.

**Status: CLOSED BY SYSTEM BOUNDARY DEFINITION.**

---

## 20. Attack: the theorem is mathematically standard H2 theory dressed in gravity notation

### Objection

The passive Gramian/H2 inequality may be standard control/network theory, so the result could still be “bookkeeping.”

### Resolution

The passive-network inequality by itself is not the intended novelty. The possible physics contribution is the closed chain

```text
passive network cut set
+ microscopic graviton quadrupole coupling
+ mass-quadrupole EWSR
+ compact TT propagation singular-value ceiling
+ operational pure-loss capacity corollary.
```

Whether that conjunction is publication-level novel remains a literature question, not an algebra question.

**Status: SIGNIFICANCE/NOVELTY RISK REMAINS.**

---

# Overall audit assessment

### Strongest parts

- exact spectral-area formulation removes the arbitrary-bandwidth objection;
- passive Gramian theorem removes dependence on a particular resonator architecture;
- coupling-operator polar decomposition cleanly separates linewidth resource from mode geometry;
- EWSR closes the many-mode passive resource budget;
- TT projector closes compact quadrupole orientation/directivity freedom;
- pure-loss capacity statements are separated correctly from coherent-transfer response.

### Remaining publication-critical tasks

1. state the center-of-mass convention for `I` explicitly;
2. perform a deeper prior-art search in general passive H2/scattering-sum-rule theory and gravitational antenna bounds;
3. independently rederive/check the stationary-phase TT coefficient and coupling-operator factorization;
4. decide whether a manuscript should stop at the strong linear-bosonic theorem rather than risk overextending to arbitrary interacting susceptibility.

### Recommendation

Do **not** chase the fully general interacting susceptibility theorem yet. The current compact passive linear-bosonic theorem is already broad, physically interpretable, and much less vulnerable than the original source-specific result. The highest-value next step is to harden and present this theorem cleanly, then let any later susceptibility generalization become an extension rather than a prerequisite.
