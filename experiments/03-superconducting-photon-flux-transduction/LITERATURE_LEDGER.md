# Experiment 03 — LITERATURE_LEDGER

**Purpose:** primary-literature boundary for architecture and novelty work. This is a living collision ledger, not a completed novelty audit.

## A. Single-photon superconducting detectors in the MIR/LWIR/FIR

### Verma et al., APL Photonics 6, 056101 (2021)

**Title:** Single-photon detection in the mid-infrared up to 10 µm wavelength using tungsten silicide superconducting nanowire detectors  
**DOI:** 10.1063/5.0048049

WSi SNSPDs showed saturated internal detection efficiency out to 10 µm. Experiment 03 must not claim LWIR superconducting single-photon detection itself as new.

### Day et al., Phys. Rev. X 14, 041005 (2024)

**Title:** A 25-micrometer Single-Photon-Sensitive Kinetic Inductance Detector  
**DOI:** 10.1103/PhysRevX.14.041005

Individual 25-µm photons were resolved in pulse-counting mode; integrating operation reached the photon-noise-limited regime over a broad absorbed-power range.

## B. Photon-triggered Josephson calorimetry / SQUID detection

### Walsh et al., Science 372, 409–412 (2021)

**Title:** Josephson junction infrared single-photon detector  
**DOI:** 10.1126/science.abf5539

Graphene Josephson-junction infrared single-photon detection predates the 2026 Dirac-fermion bolometer. This closes any broad claim that an infrared photon thermally triggering a graphene Josephson element is new.

### Huang et al., Nature Communications 17, 3845 (2026)

**Title:** Thermal detection of single photons using Dirac fermions  
**DOI:** 10.1038/s41467-026-70648-0

Relevant results:

- a graphene hybrid Josephson junction detects absorbed 1550-nm photons through low Dirac-electron heat capacity and thermally triggered Josephson switching;
- intrinsic quantum efficiency is about 87% with dark count below 1 s^-1 and about 75% with dark count below one per week;
- graphene active area is approximately 4 µm × 25 µm = 100 µm^2;
- thermal fitting gives `T_1p ≈ 2.5 K` and `tau_ep ≈ 75 ns` at a 20 mK base temperature;
- measured single-photon response is compatible with escape over a Josephson barrier of order `Delta U/k_B ≈ 8 K`;
- dark switching in the lowest-temperature regime is dominated by MQT;
- the junction channel is 600 nm long and 1.7 µm wide, with MoRe electrodes; the paper quotes a MoRe gap scale around 1.3 meV;
- the heat-diffusion length is reported near 230 µm;
- measured switching-current scale decreases by about 30% between 20 mK and 1.2 K.

Collision implication: `photon -> hot graphene electrons -> Josephson escape` is explicit prior art.

### Solinas, Giazotto, and Pepe (2017/2018)

**Title:** Proximity SQUID single photon detector via temperature-to-voltage conversion  
**arXiv:** 1711.10846

A superconducting interferometer with SNS weak links was proposed as a single-photon calorimeter: one weak link is antenna-coupled and photon heating suppresses its critical current, creating SQUID asymmetry and a measurable voltage pulse.

**Collision implication:** `photon heating -> suppression of a proximity-JJ critical current -> SQUID-level electrical detection` is prior art.

### Jung et al., Phys. Rev. Applied 26, 014078 (2026)

**Title:** Engineering Andreev bound states for thermal sensing in proximity Josephson junctions  
**DOI:** 10.1103/9lsg-mdb8

Temperature sensitivity of graphene Josephson critical current can be engineered through channel length, transparency, carrier density and superconducting material. The work explicitly analyzes the short-to-long ballistic-junction crossover through the Andreev spectrum.

## C. Single-photon / optical conversion into persistent superconducting flux

### Onen et al., Nano Letters 20, 664–668 (2020)

**Title:** Single-Photon Single-Flux Coupled Detectors  
**DOI:** 10.1021/acs.nanolett.9b04440

An SNSPD-derived device was combined with superconducting multilevel memory and experimentally demonstrated single-photon-to-single-flux conversion.

**Major collision:** broad `single photon -> superconducting detection event -> persistent flux memory` is prior art.

### Rochet et al., Nano Letters 20, 6488–6493 (2020)

**Title:** On-Demand Optical Generation of Single Flux Quanta  
**DOI:** 10.1021/acs.nanolett.0c02166

A focused optical pulse locally quenches a superconducting film and generates permanent, pinned individual Abrikosov vortices / flux quanta.

Collision implication: broad optical writing of persistent quantized superconducting flux is prior art.

## D. rf-SQUID barrier control by transient critical-current suppression

### Zhou, Habif, Bocko, and Feldman (2001)

**Title:** A "Tipping Pulse" Scheme for rf-SQUID Qubits  
**arXiv:** quant-ph/0102090  
**Conference DOI:** 10.1364/ICQI.2001.PB21  
**Related IEEE Trans. Appl. Supercond. 11, 1018–1021 (2001), DOI:** 10.1109/77.919522

SFQ pulses magnetically coupled to an rf-SQUID junction were proposed to transiently suppress critical current, lower the double-well barrier, accelerate transfer between flux wells, then restore the barrier and freeze the resulting flux state.

**Major collision:** transient `I_c` suppression as an rf-SQUID tipping/freeze mechanism is prior art.

## E. Graphene current-phase relation, arbitrary length, interfaces and self-consistency

### Titov and Beenakker, Phys. Rev. B 74, 041401(R) (2006)

**Title:** Josephson effect in ballistic graphene

The Dirac–Bogoliubov–de Gennes treatment gives the closed-form short-junction graphene Andreev spectrum/current and the pseudodiffusive Dirac-point CPR. Its stated regime requires junction length small compared with both width and superconducting coherence length.

Use in Experiment 03: sensitivity benchmark only unless the final device satisfies the short-junction limit.

### Hagymási, Kormányos, and Cserti, Phys. Rev. B 82, 134516 (2010)

**Title:** Josephson current in ballistic superconductor-graphene systems

The paper derives a Matsubara/secular-equation method valid for arbitrary junction length and explicitly distinguishes the closed-form short-junction limit `L << xi` from the general problem. This is the basis of the current ideal arbitrary-length Experiment-03 CPR calculation.

Important limitation: the superconducting pair potential is still treated through rigid boundary conditions rather than self-consistently.

### Black-Schaffer and Linder, Phys. Rev. B 82, 184522 (2010)

**Title:** Strongly anharmonic current-phase relation in ballistic graphene Josephson junctions  
**DOI:** 10.1103/PhysRevB.82.184522  
**arXiv:** 1008.2619

This is a major model-boundary source for Experiment 03.

The paper solves the graphene Josephson problem self-consistently with tight-binding Bogoliubov–de Gennes theory and contrasts it with non-self-consistent rigid-boundary treatments. Relevant findings:

- rigid boundary conditions ignore suppression of the superconducting order parameter near the SG interface, inverse-proximity depletion in the superconductors, and current depairing;
- self-consistency significantly lowers the current relative to rigid-boundary calculations;
- for short `L < xi` junctions, current depairing can alter the CPR enough that the critical phase becomes smaller than `pi/2`, producing negative skewness over substantial parameter ranges;
- for longer `L > xi` junctions, positive or only weakly negative skewness survives more readily, but self-consistent CPRs approach harmonic form more rapidly with temperature;
- proximity depletion remains relevant even when depairing is less severe.

**Implication:** the favorable steep near-`pi` tail of the current rigid-boundary arbitrary-length Experiment-03 model may be substantially rounded or qualitatively altered by self-consistency. High-doping stability conclusions are conditional until this is tested.

### Nanda et al., Nano Letters 17, 3396–3401 (2017)

**Title:** Current-Phase Relation of Ballistic Graphene Josephson Junctions  
**DOI:** 10.1021/acs.nanolett.7b00097

Direct asymmetric-SQUID measurements on ballistic MoRe/graphene JJs show a forward-skewed, gate-tunable CPR at low temperature. They define

```math
S=(2\phi_{max}-\pi)/\pi.
```

Relevant quantitative results:

```text
strong p doping: average S ~0.23
strong n doping: average S ~0.27
near charge-neutrality point: measured S ~0.1
```

Their realistic-interface tight-binding calculation explicitly includes graphene–superconductor interface/contact effects. The paper reports that:

- skewness depends sensitively on the number of graphene channels and SG interface transparency/contact resistance;
- decreasing interface transparency reduces skewness;
- higher temperature suppresses higher harmonics, and the CPR is approximately sinusoidal by 4.2 K;
- the realistic-interface model still overestimates measured `I_c` by about a factor of 2.5, plausibly because self-consistency/current-depairing effects are not fully captured;
- earlier self-consistent theory predicted approximately `S~0.15` for n-doped `L<xi` junctions, versus roughly `S~0.42` from a non-self-consistent ABS-only calculation.

**Implication for Experiment 03:** global skewness itself is prior-art characterization, but more importantly the measured realistic CPR is much less sawtooth-like than the current high-doping rigid-boundary model. Full CPR tail information is required for the rf-SQUID fold.

### Borzenets et al., Phys. Rev. Lett. 117, 237002 (2016)

**Title:** Ballistic Graphene Josephson Junctions from the Short to the Long Junction Regimes

Ballistic graphene JJs have been experimentally studied across the short/long crossover; junction length relative to coherence/Thouless scales materially changes `I_c(T)` and the CPR.

## F. Superconducting photogalvanic / phase-battery theory

### Mironov, Mel'nikov, and Buzdin, Phys. Rev. B 109, L220503 (2024)

**Title:** Photogalvanic phenomena in superconductors supporting intrinsic diode effect

Theory predicts electromagnetic illumination can generate a superconducting phase difference in a structure with intrinsic diode effect. Closing it into a loop generates dc circulating supercurrent; illumination can switch loop vorticity.

Collision implication: `illumination -> superconducting phase battery -> circulating loop current/vorticity switching` is prior art.

## G. Field-free Josephson/superconducting diode directionality

### Wu et al., Nature 604, 653–656 (2022)

**Title:** The field-free Josephson diode in a van der Waals heterostructure  
**DOI:** 10.1038/s41586-022-04504-8

NbSe2/Nb3Br8/NbSe2 heterostructures exhibit field-free nonreciprocal Josephson critical currents / superconducting diode behavior.

### Bauriedl et al., Nature Communications 13, 4266 (2022)

**Title:** Supercurrent diode effect and magnetochiral anisotropy in few-layer NbSe2  
**DOI:** 10.1038/s41467-022-31954-5

Substantial supercurrent rectification was demonstrated in few-layer NbSe2 under symmetry-breaking conditions.

## H. Remaining collision / validation categories

A full audit must still search at least:

1. photon-triggered *Josephson* persistent-flux trapping beyond Onen-type SNSPD memory;
2. rf-SQUID bolometers/calorimeters and optical bifurcation detectors;
3. Josephson escape detectors / Josephson photomultipliers;
4. phi0-junction rf-SQUIDs and anomalous phase batteries;
5. superconducting diode photon detectors;
6. metastable-loop dark-count optimization including dissipative MQT actions;
7. antenna/cavity coupling into micron-scale graphene absorbers at 8–14 µm;
8. reset/readout architectures for persistent-flux photon counters;
9. prior patents covering calorimetric Josephson-to-flux latching;
10. any prior theory deriving an explicit photon-energy / fold / MQT / capacitance / damping feasibility closure;
11. measured or self-consistent CPR **tail slope near `phi=pi`**, not only conventional skewness `S`.

## Current literature verdict

The novelty corridor is substantially narrower than at project start. The following are prior art individually or in broad combinations:

```text
LWIR superconducting single-photon detection
infrared photon -> hot graphene -> Josephson switching
photon heating -> SNS critical-current suppression -> SQUID voltage detection
single photon -> persistent superconducting flux memory
optical heating -> permanent superconducting flux/vortex
transient I_c suppression -> lowered rf-SQUID barrier -> frozen flux state
field-free Josephson directionality
illumination-driven superconducting phase batteries / vorticity switching
non-sinusoidal and thermally evolving graphene CPRs
interface- and self-consistency-induced modification of graphene CPR skewness.
```

The current ideal high-doping arbitrary-length model is now known to be an aggressive CPR-shape limit. Its very low fold relies on a steep near-`pi` tail that is substantially more sawtooth-like than representative realistic-interface measurements.

The research branch remains justified only if something survives in the narrower conjunction or mathematics:

```text
single absorbed LWIR photon
-> realistic thermal evolution of the full proximity-JJ CPR tail
-> directional rf-SQUID fold crossing
-> persistent superconducting readout state
```

and/or a genuinely new performance closure relating photon heat capacity, CPR-tail/load-line fold, cold barrier/MQT, capacitance, damping, stored signal and reset/readout cost.

No priority claim is authorized.