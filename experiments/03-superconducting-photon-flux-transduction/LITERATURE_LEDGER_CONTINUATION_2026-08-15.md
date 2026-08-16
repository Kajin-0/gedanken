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

Experiment-03 distinction, if any, must come from persistent-flux metastable capture / cold-stability / dynamic closure rather than graphene thermal transport itself.

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

## L. Ultrafast electronic thermalization relevant to the new rise-time constraint

### Mihnev et al., Nature Communications 7, 11617 (2016)

**Title:** Microscopic origins of the terahertz carrier relaxation and cooling dynamics in graphene  
**DOI:** 10.1038/ncomms11617

The combined ultrafast experiment and microscopic theory finds:

- efficient carrier-carrier scattering maintains a thermalized hot-carrier distribution;
- electron and hole quasi-Fermi distributions merge into a single uniform hot Fermi-Dirac distribution on roughly `100–200 fs` timescales in the studied regimes;
- carrier cooling then proceeds through carrier-optical-phonon scattering continuously rethermalized by carrier-carrier collisions;
- highly doped samples show approximately `1–3 ps` relaxation in the reported room-temperature THz experiments, while lightly doped/cryogenic behavior can be much slower.

**Experiment-03 implication:** a scalar electronic temperature can become meaningful much faster than the current `~9–30 ps` deterministic rise thresholds in some graphene regimes, but these data are not a cryogenic low-energy GJJ calibration.

### Yadav, Trushin, and Pauly, Phys. Rev. B 99, 155410 (2019)

**Title:** Photocarrier thermalization bottleneck in graphene  
**DOI:** 10.1103/PhysRevB.99.155410

First-principles electron-phonon calculations show that reducing excitation energy from eV scale toward approximately `100 meV` can increase photocarrier thermalization time by orders of magnitude. The paper reports femtosecond thermalization when optical-phonon emission is efficient but picosecond-scale thermalization once excitation energies approach the optical-phonon energy scale, with strong temperature dependence in that regime.

**Experiment-03 implication:** LWIR photon energies (`~89 meV` at 14 um, `~124 meV` at 10 um) lie precisely in the regime where assuming instantaneous conversion into a thermal electron distribution deserves explicit scrutiny.

This work does not directly specify the rise time of a proximity-Josephson CPR after single-photon absorption.

### Pettinger et al., arXiv:2603.13457 (2026 preprint)

**Title:** Ultrafast photo-thermoelectric currents in graphene junctions in the mid-infrared

The 2026 primary preprint reports room-temperature mid-IR graphene-junction pump-probe photocurrent relaxation around

```text
~2 ps below 8–9 um
~3 ps at longer mid-IR wavelength.
```

The authors find no pronounced loss of ultrafast response when moving below the graphene optical-phonon energy in their room-temperature junctions.

**Experiment-03 discipline:** this is useful evidence that few-ps mid-IR response is physically plausible, but it is a preprint and not a low-temperature superconducting-GJJ calibration.

## M. Current transport/rise-time interpretation

Combining the primary literature above with the Huang characteristic scale gives a useful hierarchy:

```text
intrinsic carrier redistribution / thermalization: potentially sub-ps to few ps
spatial delivery from absorption site to weak link: geometry dependent
low-temperature energy decay: much slower in the Huang bolometric device.
```

The new full dynamic solver is sensitive to the first two quantities through an effective `tau_rise`.

The current cross-device estimate

```text
D_char ~0.705 m^2/s
```

from `l_D~230 um` and `tau~75 ns` gives characteristic `d^2/D` times of approximately

```text
0.6 um ->0.5 ps
1.7 um ->4 ps
4 um   ->23 ps
25 um  ->0.9 ns.
```

Therefore optical absorption location relative to the Josephson transducer is now a first-order design issue.

## N. Updated collision target

The next literature search should focus narrowly on whether prior work already derives any of the following **specific conjunctions**:

1. nonadiabatic / rate-induced sub-fold switching as a single-photon threshold in an rf-SQUID or Josephson calorimeter;
2. an explicit photon-wavelength / MQT-dark-rate / finite-pulse metastable-capture bound;
3. the sudden-quench energy threshold `U(x_cold,T)=U(x_saddle,T)` as an optical detector design criterion;
4. elimination of junction capacitance into a dark-stability timescale of the `tau_Q` type in detector optimization;
5. a finite scalar-admittance window for photon-triggered persistent-flux capture;
6. frequency-selective damping jointly optimized for capture and dissipative MQT in a calorimetric flux latch;
7. patents claiming the same persistent-flux metastable switching principle with a graphene/SNS absorber.

The general mathematical literature on **rate-induced tipping / basin instability under fast parameter change** also needs a dedicated collision pass. Do not present rapid sub-fold tipping itself as new before that is completed.

## O. Selective dissipation / frequency-dependent Josephson damping — direct collision

### Hassel, Seppä, and Helistö, arXiv:cond-mat/0510189; related DOI 10.1063/1.2382733 (2005/2006)

**Title:** RSFQ devices with selective dissipation for quantum information processing

Primary result relevant to Experiment 03:

- explicitly proposes **frequency-dependent/selective dissipation** in Josephson/RSFQ circuits;
- replaces a plain resistive shunt with an RC shunt;
- shows stable RSFQ switching can coexist with reduced dissipation/decoherence;
- derives stability criteria and discusses optimization of the frequency-selective environment.

**Major collision:** Experiment 03 cannot claim novelty for the generic proposition

```text
engineer a frequency-dependent Josephson environment so that useful switching remains stable while unwanted dissipation is reduced
```

or for the term/concept `selective dissipation` itself.

### Männik et al., Phys. Rev. B 71, 220509(R) (2005)

**Title:** Crossover from Kramers to phase-diffusion switching in moderately damped Josephson junctions

Relevant result:

- switching statistics in hysteretic dc SQUIDs are strongly modified by **retrapping**;
- the retrapping process depends on the **frequency-dependent impedance of the environment**.

### Stornaiuolo et al., Phys. Rev. B 87, 134517 (2013)

**Title:** Resolving the effects of frequency-dependent damping and quantum phase diffusion in YBaCuO Josephson junctions

Relevant result:

- fits Josephson phase dynamics using a two-quality-factor / frequency-dependent damping model;
- combines transport data with Monte Carlo phase-dynamics simulations;
- shows that frequency-dependent damping and quantum phase diffusion materially modify switching behavior.

**Experiment-03 surviving distinction, if any:** the current candidate contribution is narrower than selective dissipation itself. It concerns a **photon-triggered metastable flux latch with explicitly time-separated launch and capture/reformation stages**, where the environment's stage-resolved dissipation allocation can be computed from a passive energy identity and combined with a calorimetric drive-similarity law, persistent-flux requirement, and dark-stability/open-quantum constraints.

The newly observed near-coincidence between a high-fidelity capture boundary and the deterministic crossover

```text
H_eff,launch^2 / H_eff,capture^2 ~ 1
```

is **not** a novelty claim. It must first survive a cross-parameter stress test and a dedicated literature/patent search for analogous stage-resolved damping criteria.

No priority claim is authorized.
