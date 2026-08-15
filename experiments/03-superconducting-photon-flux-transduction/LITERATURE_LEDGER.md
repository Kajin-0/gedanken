# Experiment 03 — LITERATURE_LEDGER

**Purpose:** primary-literature boundary for architecture and novelty work. This is a living collision ledger, not a completed novelty audit.

## A. Single-photon superconducting detectors in the MIR/LWIR/FIR

### Verma et al., APL Photonics 6, 056101 (2021)

**Title:** Single-photon detection in the mid-infrared up to 10 µm wavelength using tungsten silicide superconducting nanowire detectors  
**DOI:** 10.1063/5.0048049

Relevant result: WSi SNSPDs showed saturated internal detection efficiency out to 10 µm. Experiment 03 must not claim LWIR superconducting single-photon detection itself as new.

### Day et al., Phys. Rev. X 14, 041005 (2024)

**Title:** A 25-micrometer Single-Photon-Sensitive Kinetic Inductance Detector  
**DOI:** 10.1103/PhysRevX.14.041005

Relevant result: individual 25-µm photons were resolved in pulse-counting mode; integrating operation reached the photon-noise-limited regime over a broad absorbed-power range. This is a benchmark against any claim that superconductivity alone gives a distinct low-energy-photon advantage.

## B. Photon-triggered Josephson calorimetry and engineered thermal critical-current response

### Huang et al., Nature Communications 17, 3845 (2026)

**Title:** Thermal detection of single photons using Dirac fermions  
**DOI:** 10.1038/s41467-026-70648-0

Relevant results:

- a graphene hybrid Josephson junction detects absorbed 1550-nm photons through the very low heat capacity of Dirac electrons and thermally triggered Josephson switching;
- reported intrinsic quantum efficiency is about 87% with dark count below 1 s^-1 and about 75% with dark count below one per week;
- graphene active area is approximately 4 µm × 25 µm = 100 µm^2;
- a thermal model gives T_1p ≈ 2.5 K and electron-phonon relaxation time tau_ep ≈ 75 ns at a 20 mK base temperature;
- the measured single-photon response is consistent with escape over a Josephson barrier of order Delta U/k_B ≈ 8 K;
- dark switching in the lowest-temperature regime is associated with macroscopic quantum tunneling rather than ordinary Johnson noise.

Collision implication: `photon -> hot graphene electrons -> Josephson escape` is explicit prior art. Experiment 03 cannot claim that transduction chain.

### Jung et al., Phys. Rev. Applied 26, 014078 (2026)

**Title:** Engineering Andreev bound states for thermal sensing in proximity Josephson junctions  
**DOI:** 10.1103/9lsg-mdb8

Relevant result: temperature sensitivity of graphene Josephson critical current can be engineered through channel length, transparency, carrier density, and superconducting material. The reported Al-based threshold-readout sensitivity reaches width-normalized |dJ_c/dT| ≈ 0.2 µA K^-1 µm^-1 at 0.1 K; Ti-based devices reach a maximum relative |(dI_c/dT)/I_c| ≈ 0.6 K^-1 at 50 mK.

Implication for Experiment 03: a thermal photon pulse producing a substantial transient reduction of I_c is not obviously unrealistic, but these metrics are cross-device benchmarks and must not be inserted as a quantitative I_c(T_e) law for the proposed device.

## C. Single-photon / optical conversion into persistent superconducting flux

### Onen et al., Nano Letters 20, 664–668 (2020)

**Title:** Single-Photon Single-Flux Coupled Detectors  
**DOI:** 10.1021/acs.nanolett.9b04440

Relevant result: an SNSPD-derived device was combined with superconducting multilevel memory and experimentally demonstrated single-photon-to-single-flux conversion. Electrical characterization showed single-flux-quantum-separated memory states, and optical tests distinguished single-photon detection from multiphoton and thermal activation processes.

**Major collision:** the broad architecture

```text
single photon -> superconducting detection event -> persistent flux memory
```

is prior art. Persistent superconducting flux storage of photon detections is therefore not a novelty route for Experiment 03.

### Rochet et al., Nano Letters 20, 6488–6493 (2020)

**Title:** On-Demand Optical Generation of Single Flux Quanta  
**DOI:** 10.1021/acs.nanolett.0c02166

Relevant result: a focused optical pulse locally quenches a superconducting film and generates permanent, pinned single Abrikosov vortices / flux quanta. This is not the same circuit architecture as Experiment 03, but it further removes any broad claim that optical excitation of a superconductor producing persistent quantized flux is new.

## D. rf-SQUID barrier control by transient critical-current suppression

### Zhou, Habif, Bocko, and Feldman (2001)

**Title:** A "Tipping Pulse" Scheme for rf-SQUID Qubits  
**arXiv:** quant-ph/0102090  
**Conference version DOI:** 10.1364/ICQI.2001.PB21  
**Related IEEE Trans. Appl. Supercond. 11, 1018–1021 (2001), DOI:** 10.1109/77.919522

Relevant result: SFQ pulses magnetically coupled to an rf-SQUID junction were proposed to momentarily suppress its critical current, lower the double-well barrier, accelerate transfer between flux wells, and then restore the barrier to freeze the resulting flux state.

**Major collision:** transient `I_c` suppression as a means of lowering an rf-SQUID barrier and subsequently freezing a flux state is prior art. Experiment 03 cannot claim this generic control principle.

What remains distinct in the present research question is whether a *single absorbed LWIR photon* can provide the calorimetric `I_c` suppression needed for reliable, directionally selected classical flux capture with a quantitatively useful dark-count/efficiency closure.

## E. Superconducting photogalvanic / phase-battery theory

### Mironov, Mel'nikov, and Buzdin, Phys. Rev. B 109, L220503 (2024)

**Title:** Photogalvanic phenomena in superconductors supporting intrinsic diode effect

Relevant result: phenomenological theory predicts an electromagnetic wave can generate a superconducting phase difference in a material/structure with intrinsic diode effect. Closing it into a superconducting loop generates a dc circulating supercurrent; increasing illumination can switch loop states with different vorticities.

Collision implication: `illumination -> superconducting phase battery -> circulating loop current/vorticity switching` is already explicit prior art. Experiment 03 cannot claim that broad chain as new.

## F. Field-free Josephson/superconducting diode directionality

### Wu et al., Nature 604, 653–656 (2022)

**Title:** The field-free Josephson diode in a van der Waals heterostructure  
**DOI:** 10.1038/s41586-022-04504-8

Relevant result: NbSe2/Nb3Br8/NbSe2 heterostructures exhibit field-free nonreciprocal Josephson critical currents / superconducting diode behavior due to inversion-symmetry breaking.

Collision implication: field-free superconducting directionality is prior art. Experiment 03 must not claim the Josephson diode effect itself.

### Bauriedl et al., Nature Communications 13, 4266 (2022)

**Title:** Supercurrent diode effect and magnetochiral anisotropy in few-layer NbSe2  
**DOI:** 10.1038/s41467-022-31954-5

Relevant result: substantial supercurrent rectification was demonstrated in few-layer NbSe2 under symmetry-breaking conditions. Useful for understanding achievable nonreciprocity and possible directional phase-escape landscapes.

## G. Remaining collision categories

A full audit must still search at least:

1. photon-triggered *Josephson* flux trapping rather than SNSPD-derived flux memory;
2. rf-SQUID bolometers/calorimeters and optical bifurcation detectors;
3. Josephson escape detectors / Josephson photomultipliers;
4. phi0-junction rf-SQUIDs and anomalous phase batteries;
5. superconducting diode photon detectors;
6. graphene/SNS bolometers and calorimeters from microwave through MIR;
7. metastable-loop dark-count theory including dissipative MQT actions;
8. antenna/cavity coupling into micron-scale graphene absorbers at 8–14 µm;
9. reset/readout architectures for persistent-flux photon counters;
10. prior patents covering calorimetric Josephson-to-flux latching.

## Current literature verdict

The novelty corridor is substantially narrower than at project start. The following are already prior art individually or in broad combinations:

```text
LWIR superconducting single-photon detection
photon -> hot electrons -> Josephson switching
single photon -> persistent superconducting flux memory
optical heating -> permanent superconducting flux/vortex
transient I_c suppression -> lowered rf-SQUID barrier -> frozen flux state
field-free Josephson directionality
illumination-driven superconducting phase batteries / vorticity switching
```

The research branch remains justified only if something survives in the more specific conjunction or mathematics:

```text
single absorbed LWIR photon
-> engineered calorimetric suppression of Josephson I_c
-> deterministic or high-fidelity directional rf-SQUID bifurcation
-> persistent superconducting readout state
```

and/or a rigorous performance closure relating photon heat capacity, bifurcation threshold, cold-state barrier/MQT, damping, stored signal, and reset/readout cost.

No priority claim is authorized.