# Current State — Experiment 02

**Checkpoint:** recent gravity-communication literature collision audit and manuscript framing patch.  
**Status:** **PHYSICS THEOREM REMAINS FROZEN; NOVELTY/MANUSCRIPT FREEZE NARROWLY REOPENED PENDING FRESH EXACT-HEAD CI.**

The pre-reopen fully validated science/manuscript SHA is

```text
d05a1e5d5f2f8b4c352f058de73194519c1015e1
```

The reopen is literature/claim discipline only. No theorem broadening or coefficient rederivation is authorized.

## 1. Current theorem

Use

```text
omega_0   absolute carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
a_A,a_B   endpoint radii, k_0 a_A,k_0 a_B << 1
R         separation, k_0 R >> 1
Omega     upper physical frequency of retained endpoint modal sector,
          Omega=omega_0[1+O(B/omega_0)]
I_2       int rho r^2 dV about endpoint COM
```

Define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

For separated compact passive nonrelativistic linear-harmonic endpoints in weak leading mass-quadrupole gravity, with finite or countably infinite bounded-port Markov retained modal sectors,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
}
```

`Gamma_coh` has units `s^-1` and is a coherent-transfer spectral area, not an information capacity.

The carrier-scale resource does not automatically cover uncontrolled modes with `omega_n >> omega_0`; off-resonant higher-frequency sectors require a separate bound.

## 2. Proof spine

### Passive cut

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

The band integral is bounded by the full-line selected-port `H2` norm because the integrand is nonnegative.

File: `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`.

### Endpoint resource

```math
\sum_n\frac{q_n:q_n}{\mu_n}\le\frac{20}{3}I_2,
```

and, for `omega_n <= Omega`,

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le\frac{4G}{3c^5}I_2\Omega^4
\lesssim\frac{4G}{3c^5}I_2\omega_0^4.
```

File: `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`.

### Compact TT propagation

```math
\limsup_{kR\to\infty}(kR)^2\|P_g\|_{\rm op}^2
\le\frac{25}{16}.
```

File: `TT_PROPAGATION_BOUND_DERIVATION.md`.

### Assembly

```math
(25/16)\times(4/3)=25/12,
```

with `k_0=omega_0/c`.

File: `FINITE_TWO_ENDED_INERTIA_BOUND.md`.

## 3. Infinite modal and recurrence closure

Countably infinite separable **bounded-port Markov** modal sectors are covered when the gravitational port is Hilbert--Schmidt; the retained endpoint resource supplies the required finite trace.

File: `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`.

Same-two-endpoint passive recurrence obeys

```math
\|P_{\rm eff}\|^2\le\frac{\eta}{(1-\eta)^2},
```

so recurrence changes only subleading terms in the leading `1/R^2` upper ceiling. This is not equality for actual recurrent transfer.

File: `PASSIVE_TWO_ENDPOINT_RECURRENCE.md`.

## 4. Novelty reopen — recent gravity-communication literature

A concrete audit defect was identified after the first internal freeze: the earlier hostile literature review did not directly close against several of the most semantically adjacent modern gravity-as-communication papers.

Canonical new audit:

`RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`

It explicitly analyzes

- Kafri, Milburn & Taylor (2015), *Bounds on quantum communication via Newtonian gravity*;
- Lami, Pedernales & Plenio (2024), *Testing the Quantumness of Gravity without Entanglement*;
- Toccacelo, Andersen & Brask (2025), *Benchmarks for quantum communication via gravity*;
- Mari, Zippilli & Vitali (2026), *Can gravity mediate the transmission of quantum information?*.

Revised claim discipline:

```text
gravity as a communication mediator:                         HISTORICAL
classical-channel/noise and LOCC communication bounds:       HISTORICAL
state-transfer benchmarks between gravitational oscillators: HISTORICAL
narrowband gravity-induced optomechanical channel:            HISTORICAL
complete passive wave-zone I_2 + TT spectral-area closure:    NO EXACT COLLISION FOUND
priority claim:                                               NO
```

The recent papers are major conceptual near-collisions, but the audit found no inspected paper stating the Experiment-02 frequency-integrated passive wave-zone theorem with both endpoints reduced to `I_2` and the compact TT `25/16` propagation ceiling.

## 5. Manuscript patch

Active manuscript source:

`manuscript_v1/`

Title:

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

The current patch adds the four recent communication papers to the bibliography and explicitly disclaims novelty for gravity-mediated communication or state-transfer bounds in general. It distinguishes those Newtonian/oscillator and optomechanical communication settings from the present passive separated-TT spectral-area closure.

This is a literature-framing correction, not a theorem correction.

## 6. Last fully validated checkpoint

Pre-reopen authoritative SHA:

```text
d05a1e5d5f2f8b4c352f058de73194519c1015e1
```

All seven gates passed there:

```text
passive cut        run 31429984820 — PASS
endpoint resource  run 31429984888 — PASS
TT propagation     run 31429984826 — PASS
combined bound     run 31429984854 — PASS
infinite modal     run 31429984786 — PASS
recurrence         run 31429984808 — PASS
manuscript         run 31429984776, job 93590769191 — PASS
```

The current literature/manuscript patch must now receive fresh exact-head CI before a replacement canonical freeze SHA is recorded.

## 7. Historical / novelty boundary

Most ingredients are historical. No standalone novelty claim is made for resonant-mass integrated response, gravitational-antenna modal theory/directivity, arbitrary-body multimode response, material sum rules, generic passive `H2`, generic wave-channel bounds, multiple scattering, gravity-mediated communication in general, or the `20/3` and `4/3` lemmas.

No inspected source states the exact complete two-ended inertia closure. This is a negative search result, not proof of priority.

## 8. Explicit exclusions

No claim is made for

- broad absolute-frequency operation with one carrier coefficient;
- uncontrolled higher-frequency off-resonant endpoint sectors;
- arbitrary unbounded PDE boundary-control ports;
- genuinely non-Markov continua;
- added relays, external mirrors/cavities, or extended phased apertures;
- reactive near-field exchange;
- active gain/pumping/feedback;
- higher-multipole-dominated, relativistic, nonlinear, or strong-field regimes.

## 9. Current research mode

Do not broaden or rederive the theorem.

Immediate sequence:

1. commit the recent-literature collision audit and manuscript citation/framing patch;
2. require fresh exact-head manuscript plus Experiment-02 theorem regressions;
3. if all pass, record a docs-only replacement freeze checkpoint;
4. after that, further technical work again requires a concrete contradiction or external specialist/journal objection.
