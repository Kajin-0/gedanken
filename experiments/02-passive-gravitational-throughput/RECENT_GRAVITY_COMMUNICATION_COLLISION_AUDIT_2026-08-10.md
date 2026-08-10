# Recent Gravity-Communication Collision Audit — 2026-08-10

**Experiment:** `02-passive-gravitational-throughput`  
**Mode:** novelty-only reopen after a concrete literature-audit defect was identified.  
**Physics status:** the `25/12` theorem derivation is not reopened by this audit.  
**Question:** do the most directly adjacent gravity-as-communication papers already contain the complete two-ended passive wave-zone inertia closure?

## 1. Why this audit was required

The earlier hostile prior-art review concentrated on resonant-mass antennas, gravitational Hertz experiments, material-response sum rules, generic passive `H2` bounds, and wave-channel mathematics. That was useful but incomplete: several modern papers explicitly formulate gravity as a communication channel or derive communication/classicality bounds for gravitationally interacting systems.

The omission matters because Experiment 02 must not imply that any of the following broad ideas are new:

```text
gravity as a communication mediator
quantum/classical communication tests for gravity
state-transfer bounds between gravitationally coupled oscillators
narrowband gravity-induced transduction channels
```

This audit therefore attacks the novelty claim against the closest modern communication literature before allowing the internal freeze to remain canonical.

## 2. Sources inspected

### Kafri, Milburn & Taylor (2015)

D. Kafri, G. J. Milburn, J. M. Taylor, **“Bounds on quantum communication via Newtonian gravity,”** *New Journal of Physics* **17**, 015006 (2015), DOI `10.1088/1367-2630/17/1/015006`, arXiv:`1404.3214`.

Core result relevant here: if a Newtonian `1/r` interaction is restricted so that it cannot convey quantum information, a minimum noise/decoherence cost is required. This is direct prior art for asking what communication properties gravity can or cannot possess.

### Lami, Pedernales & Plenio (2024)

L. Lami, J. S. Pedernales, M. B. Plenio, **“Testing the Quantumness of Gravity without Entanglement,”** *Physical Review X* **14**, 021022 (2024), DOI `10.1103/PhysRevX.14.021022`.

Core result relevant here: a general upper bound on LOCC simulation fidelity is specialized to systems of harmonic oscillators interacting through a quantum Newtonian Hamiltonian. This is direct prior art for bounding the classical simulability / communication performance of gravitationally coupled oscillators.

### Toccacelo, Andersen & Brask (2025)

K. Toccacelo, U. L. Andersen, J. B. Brask, **“Benchmarks for quantum communication via gravity,”** *Physical Review A* **112**, 022218 (2025), DOI `10.1103/7tfb-k2xh`, arXiv:`2503.03585`.

Core result relevant here: limitations and benchmarks for transmission of quantum states between gravitationally interacting mechanical oscillators under different models of gravity, including coherent-state/LOCC benchmarks and squeezing-transfer tests.

### Mari, Zippilli & Vitali (2026)

A. Mari, S. Zippilli, D. Vitali, **“Can gravity mediate the transmission of quantum information?”** *Physical Review D* **113**, L021905 (2026), DOI `10.1103/pfvz-fd54`, arXiv:`2504.05998`.

Core result relevant here: two laser-driven optomechanical systems are weakly coupled by gravity; under a quadratic interaction such as a linearized Newtonian force the induced optical link is a frequency-dependent Gaussian thermal attenuator. The work analyzes entanglement-breaking/nonclassicality conditions and quantum-information transmission through that gravity-induced optical channel.

## 3. Collision matrix

| Source | Interaction / architecture | Quantity bounded or tested | What it establishes | Exact collision with Experiment 02? |
|---|---|---|---|---|
| Kafri–Milburn–Taylor 2015 | Newtonian long-range interaction; classical-channel hypothesis | minimum noise/decoherence required when the interaction cannot transmit quantum information | gravity-as-communication and communication/noise bounds are historical | **NO** |
| Lami–Pedernales–Plenio 2024 | gravitationally interacting quantum systems; prominent harmonic-oscillator Newtonian application | maximal LOCC simulation fidelity | classical-simulation bounds for gravitational dynamics are historical | **NO** |
| Toccacelo–Andersen–Brask 2025 | gravitationally interacting mechanical oscillators under several gravity models | state-transfer / coherent-state LOCC benchmarks; squeezing transfer | explicit quantum-state communication benchmarks through gravity are historical | **NO** |
| Mari–Zippilli–Vitali 2026 | two laser-driven optomechanical systems with weak gravitational coupling; explicit quadratic/linearized-Newtonian model | frequency-dependent transmissivity, thermal noise, entanglement-breaking / nonclassicality and capacity criteria | a narrowband gravity-induced transduction channel is historical | **NO** |
| Experiment 02 | two separated compact **passive** matter endpoints coupled by propagating TT linearized gravity in the wave zone | `Gamma_coh=(1/2pi) int Tr(T^dag T) dnu` | cumulative passive spectral-area ceiling reduced to endpoint `I_2` resources and compact TT propagation | target theorem |

## 4. Why these papers are major near-collisions

They are much closer semantically than the older resonant-bar literature. They use the language of channels, communication, state transfer, classical simulation, transmissivity, and quantum information. Therefore the manuscript must not claim or imply

```text
"first bound on communication through gravity"
"first gravity-mediated communication theorem"
"first use of gravity as a quantum channel"
"first bound on state transfer between gravitationally coupled oscillators"
```

Those claims are false or at minimum indefensible after this literature line is included.

## 5. Why no exact theorem collision was found

The Experiment-02 theorem is a different physical and mathematical object:

```math
Gamma_coh
= (1/2pi) int_Bnu Tr[T^dag(nu) T(nu)] dnu
```

with the compact-wave-zone passive closure

```math
Gamma_coh
lesssim
[25 G omega_0^2/(12 c^3 R^2)] min(I_2A,I_2B).
```

The inspected recent communication papers do not state this object or this closure.

### 5.1 Mediator / propagation regime

Experiment 02 requires

```text
k_0 a_A, k_0 a_B << 1
k_0 R >> 1
```

and explicitly factors a propagating transverse-traceless quadrupole channel with leading power-transfer ceiling

```math
25/[16(k_0 R)^2].
```

The recent communication papers instead analyze gravitational interaction between localized systems in Newtonian / oscillator or optomechanical settings. They do not derive the compact far-zone TT singular-value ceiling used here.

### 5.2 Endpoint resource

Experiment 02 eliminates the detailed passive modal architectures at **both** endpoints through

```math
sum_n (q_n:q_n)/mu_n <= (20/3) I_2
```

and therefore

```math
Tr(K_g^dag K_g)
<= (4G/3c^5) I_2 Omega^4.
```

No inspected recent gravity-communication paper derives or uses a two-ended scalar second-mass-moment resource of this form.

### 5.3 Metric

Kafri et al. bound noise under a classical-communication restriction. Lami et al. bound LOCC simulation fidelity. Toccacelo et al. benchmark state transfer and squeezing/coherent-state performance. Mari et al. analyze transmissivity/noise and channel nonclassicality/capacity conditions.

Experiment 02 instead bounds the **frequency-integrated coherent power-transfer spectral area** before any capacity or entanglement-breaking functional is applied.

### 5.4 Passivity / architecture class

Experiment 02 is deliberately restricted to passive bounded-port endpoint dynamics. Mari et al. use laser-driven optomechanical systems and an effective pump-enhanced optomechanical coupling, which lies outside the present passive endpoint class. The other recent papers address direct gravitationally interacting oscillator dynamics rather than an endpoint-resource-plus-propagating-TT cut set.

This distinction narrows Experiment 02; it does not make the modern communication papers irrelevant. They remain mandatory conceptual prior art.

## 6. Revised novelty classification

```text
gravity as a communication channel:                         HISTORICAL
classical-channel/noise bounds for Newtonian gravity:       HISTORICAL
LOCC/classical-simulation bounds for gravitational dynamics: HISTORICAL
state-transfer benchmarks between gravitating oscillators:   HISTORICAL
narrowband gravity-induced optical transduction channel:      HISTORICAL
passive integrated-response / high-Q cancellation:           HISTORICAL
compact TT directivity / wave-channel ingredients:            HISTORICAL
complete two-ended I_2 + TT spectral-area closure:            NO EXACT COLLISION FOUND
priority claim for that closure:                              NO
```

The safe manuscript statement is therefore not that communication through gravity has lacked bounds. It is:

> Existing work bounds or benchmarks gravity-mediated communication in Newtonian and oscillator/optomechanical settings. The present result addresses a different question: a passive far-zone TT link, integrated over frequency and closed at both compact matter endpoints by a scalar inertia resource.

## 7. Publication consequence

The recent literature does **not** reopen the internal coefficient derivation. It does require a literature-framing patch.

Required manuscript changes:

1. cite Kafri 2015, Lami 2024, Toccacelo 2025, and Mari 2026 near the opening statement of the question;
2. explicitly disclaim novelty for gravity-mediated communication or state-transfer bounds in general;
3. distinguish the present passive far-zone TT spectral-area / inertia closure from their Newtonian/oscillator and optomechanical communication metrics;
4. retain the existing no-priority language for the exact complete closure.

## 8. Verdict

**PHYSICS THEOREM:** unchanged.  
**EARLIER NOVELTY AUDIT:** materially incomplete.  
**RECENT-LITERATURE COLLISION:** strong conceptual near-collision, **no exact theorem collision found**.  
**PRIORITY:** unproved.  
**ACTION:** patch manuscript and canonical claim ledger; require fresh exact-head CI before restoring the final internal freeze.
