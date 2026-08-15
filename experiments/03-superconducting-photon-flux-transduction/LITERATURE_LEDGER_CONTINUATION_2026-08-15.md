# Experiment 03 — Literature Ledger Continuation — 2026-08-15

This file continues `LITERATURE_LEDGER.md`. Until consolidation, both files form the active literature boundary.

## I. Graphene thermal transport — direct design prior art

### Fried et al., Phys. Rev. Applied 21, 014006 (2024)

**Title:** Performance limits due to thermal transport in graphene single-photon bolometers  
**DOI:** 10.1103/PhysRevApplied.21.014006

Primary result relevant to Experiment 03:

- models graphene calorimetric single-photon detection including electronic diffusion and electron-phonon dissipation;
- treats clean, supercollision and resonant-scattering cooling regimes;
- explicitly studies the input-to-readout thermal transport tradeoff;
- affirms superconducting readout of MIR/NIR photon heating without requiring direct Cooper-pair breaking at the readout;
- predicts an intrinsic timing-jitter scale around 2.7 ps in its modeled architecture.

**Collision implication:** generic graphene thermal-propagation optimization, absorber/readout spacing tradeoffs and timing-jitter optimization are prior art. Experiment 03 cannot claim novelty merely from coupling a graphene heat-transport model to a superconducting readout.

Experiment-03 distinction, if any, must come from the persistent-flux fold capture / cold-stability / dynamic closure rather than graphene thermal transport itself.

## J. Huang thermal-fit interpretation clarification

### Huang et al., Nature Communications 17, 3845 (2026)

**Title:** Thermal detection of single photons using Dirac fermions  
**DOI:** 10.1038/s41467-026-70648-0

Additional interpretation notes beyond the original ledger entry:

- the paper models efficiency with a clean-graphene exponent `delta=4`;
- it reports a best-fit `tau_ep=75 ns` and `T_1p=2.5 K` at `T0=20 mK`;
- when modeling base-temperature dependence, it uses `tau_ep propto T0^(2-delta)`, hence `tau_ep propto T0^-2` for `delta=4`;
- the published fit does **not** directly establish that the same 75-ns number is a temperature-independent local relaxation time at every hot-electron temperature;
- the device uses an RCSJ switching picture with plasma frequency above roughly 100 GHz;
- the heat-diffusion length is about 230 um, much larger than the sample;
- direct contact heat leakage is discussed when `k_B T_e` exceeds the MoRe parent gap scale near 1.3 meV.

**Experiment-03 discipline:** the `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md` mapping from the 75-ns fit to `gamma/(4 Sigma T^2)` is explicitly conditional and must not be cited as an experimental hot-state lifetime measurement.

## K. General detector thermodynamic tradeoffs

### Schwarzhans et al., PRX Quantum 7, 033001 (2026)

**Title:** Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition  
**DOI:** 10.1103/wm5p-tjtg

The paper formulates a minimal autonomous quantum particle detector and studies efficiency, gain, jitter, dead time and dark counts. It finds that improved temporal performance requires increased dissipation in its model and, specifically, that reducing detection jitter or dead time increases dark counts.

**Major collision:** the generic proposition

```text
faster response / shorter dead time <-> increased dark-count cost
```

is not available as an Experiment-03 novelty claim.

The remaining possible theoretical contribution must be more specific, for example a superconducting-fold/calorimetric relation that connects wavelength, metastable barrier, MQT, dynamic saddle-node passage and persistent flux capture with explicit constitutive coefficients.

## L. Updated collision target

The next literature search should focus narrowly on whether prior work already derives any of the following **specific conjunctions**:

1. saddle-node critical slowing as a single-photon detection threshold in an rf-SQUID / Josephson calorimeter;
2. an explicit photon-wavelength / MQT-dark-rate / finite-fold-passage bound;
3. elimination of junction capacitance into a dark-stability timescale of the `tau_Q` type in a detector optimization;
4. a finite scalar-admittance window for photon-triggered persistent-flux capture;
5. frequency-selective damping jointly optimized for capture and dissipative MQT in a calorimetric flux latch;
6. patents claiming the same persistent-fold operating principle with a graphene/SNS absorber.

No priority claim is authorized.
