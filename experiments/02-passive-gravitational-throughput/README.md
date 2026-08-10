# Experiment 02 — Passive Gravitational Throughput

## Question

What frequency-integrated coherent transfer can a **direct passive gravitational link** support when both compact matter interfaces and the propagating TT channel are treated explicitly?

Experiment 01 / V7 is frozen. This branch develops a separate theorem and does not modify V7.

---

## Headline theorem

For compact passive nonrelativistic linear-harmonic source and receiver networks in weak one-pass quadrupolar wave-zone gravity,

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega
```

obeys

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

The ceiling contains no endpoint quality factor, no assumed number of passive resonances, no coherent internal-mixing parameter, and no four-spoke-specific quantity.

The physical bound is **classical** within this linear-harmonic class. Quantum mechanics reproduces the same oscillator-strength normalization and gives later pure-loss channel/capacity corollaries.

---

## Proof skeleton

### Passive selected-port cut set

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
```

This is established passive H2/Gramian algebra applied to the gravitational port resources.

### Classical cumulative material resource

For mass-weighted elastic normal modes,

```math
(g^{ij})_k
=\delta_{ik}x_j+\delta_{jk}x_i
-\frac23\delta_{ij}x_k
```

satisfies

```math
\sum_{ijk}|(g^{ij})_k|^2
=\frac{20}{3}r^2.
```

Standard modal-participation/Bessel completeness therefore gives the gravitational specialization

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I
}
```

and, using Hirakawa's historical gravitational effective area,

```math
\boxed{
\sum_n M A_{Gn}\le\frac{40}{3}I.
}
```

For retained modes below `Omega`,

```math
\boxed{
\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
}
```

### Normalized compact TT propagation

```math
G_B^\dagger U_RG_A
=\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2},
```

with

```math
\boxed{
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}
}
```

at leading wave-zone order.

The same `25/16` has both a normalized TT angular-mode derivation and a classical reciprocal-antenna interpretation from `D_A=D_B=5/2`.

---

## Historical normalization cross-check

Hirakawa, Narihara, and Fujimoto's 1976 compact-antenna effective area satisfies

```math
A_{Gn}=\frac{2q_n:q_n}{M\mu_n}.
```

Their radiated power and the harmonic modal energy give

```math
\boxed{
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
}
```

Quantizing the same normal coordinate gives

```math
Q^{01}:Q^{10}
=\frac{\hbar M A_{Gn}}{4\omega_n}
```

and reproduces exactly

```math
\kappa_{g,n}
=\frac{2G\omega_n^5}{5\hbar c^5}Q^{01}:Q^{10}.
```

No factor-of-two or `2 pi` mismatch was found.

---

## Exact resonator and quantum corollaries

For one source and receiver pole,

```math
\Gamma_{\rm EBP}
\le\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
```

For the symmetric lossless family,

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
\qquad
\Gamma_{\rm EBP}^{\rm max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
```

After quantization, for a stationary vacuum pure-loss realization,

```math
\eta_{\max}\le\frac12\Rightarrow Q_1=0,
```

and

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
```

These are downstream channel-specific consequences, not the origin of the physical throughput bound.

---

## Prior-art boundary

The audit explicitly rejects novelty for

- gravitational generator--receiver calculations;
- compact gravitational antenna eigenmodes;
- gravitational reciprocity and compact quadrupole directivity;
- `Q`-independent integrated gravitational response;
- gravitational material-response sum-rule methodology;
- passive H2/Gramian mathematics;
- generic singular source--receiver wave channels and Green-operator transfer bounds;
- modal participation / effective-modal-mass completeness;
- generic use of sum rules to constrain integrated passive response.

The only surviving candidate contribution is the **gravity-specific cumulative two-ended closure**:

```text
passive selected-port spectral-area cut set
-> smaller source/receiver gravitational resource
-> STF quadrupole modal-participation specialization
-> cumulative effective-area/inertia ceiling at BOTH endpoints
-> normalized compact one-pass TT propagation
-> explicit inertia-only end-to-end throughput bound.
```

No inspected primary source has been found stating this exact theorem. That is a negative search result, not a priority claim.

---

## Scope

The theorem is restricted to

- weak linearized gravity;
- direct retarded one-pass/Born wave-zone transfer;
- compact nonrelativistic quadrupole source and receiver matter;
- stable passive linear-harmonic endpoint dynamics in finite band-local sectors;
- no active gain, inversion, parametric drive, extended phased aperture, higher-multipole beaming, near-field exchange, recurrent multiple scattering, strong common-bath hybridization, or intermediate relay.

For an infinite elastic spectrum, the finite-sector resource bound is uniform in mode count; extension of the H2 transfer requires the corresponding trace-class limit.

---

## Validation

Latest complete physics regression:

```text
run 31344642352
job 93324206747
PASS
```

All five stages passed, including the new classical modal-sum regression.

Latest complete manuscript validation:

```text
run 31344642351
job 93324206692
PASS
```

LaTeX compilation, unresolved citation/reference scan, and PDF artifact upload all passed.

---

## Read next

1. `CURRENT_STATE.md`
2. `HOSTILE_REFEREE_REPORT_2026-08-09.md`
3. `CLASSICAL_MODAL_SUM_RULE_AND_QUANTUM_SCOPE_AUDIT_2026-08-09.md`
4. `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`
5. `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`
6. `SRIVASTAVA_WIDOM_PIZZELLA_2003_SUM_RULE_COLLISION_AUDIT.md`
7. `STRUCTURAL_DYNAMICS_MODAL_PARTICIPATION_COLLISION_AUDIT.md`
8. `GENERIC_WAVE_TRANSFER_COLLISION_AUDIT_2026-08-09.md`
9. `PASSIVE_NETWORK_CUTSET_THEOREM.md`
10. `GRAVITATIONAL_PORT_FACTORIZATION.md`
11. `TT_PROPAGATION_BOUND.md`
12. `CAPACITY_COROLLARIES.md`

## Current status

**Physics theorem: GO within the declared passive compact linear-harmonic one-pass class.**

**Exact novelty: provisional only for the final gravity-specific inertia closure.**

**Main remaining risk: publication significance, not a known algebraic defect.**

**Next step: actual external gravitational-antenna / passive-wave specialist review. Do not broaden this paper further internally.**
