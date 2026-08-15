# Experiment 03 — Superconducting Photon-to-Flux Transduction

**Status:** exploratory theory track  
**Started:** 2026-08-15  
**No manuscript exists yet. No novelty or priority claim is authorized.**

## Research question

Can an absorbed optical photon be converted into a persistent, directionally selected superconducting flux state with negligible detector-added equilibrium dissipation?

The working target is LWIR single-photon operation, especially around 8–14 µm, but the derivation should remain wavelength-parametric wherever possible.

## Working architecture

The current candidate is not a bulk "superconducting photovoltaic material." It is a functional chain:

```text
LWIR photon
  -> antenna / resonant absorber
  -> low-heat-capacity photon-sensitive Josephson element
  -> transient suppression of the Josephson/phase barrier
  -> directionally favored phase escape
  -> fluxoid transition n -> n+1
  -> persistent superconducting flux/current state
  -> SQUID or equivalent nondissipative readout
```

A graphene Josephson calorimeter is the current benchmark photon-sensitive element because single-photon Josephson switching has experimental support at shorter wavelength. A phi0 / Josephson-diode element or small external flux bias is the current candidate for directional capture. These are starting points, not locked material choices.

## Central distinction

The desired detector is not required to absorb a photon without any dissipation. The current concept is:

```text
brief nonequilibrium / dissipative write event
    -> persistent dissipationless superconducting memory state
```

The sensing/storage channel may therefore avoid an ordinary broadband Johnson floor even though photon absorption, quasiparticle generation, and phase switching are nonequilibrium processes.

## Current quantitative targets

Initial design target:

```text
lambda                 ~ 10 um
single-photon P_det     > 0.9
preferred direction     > 0.9 initially, ultimately > 0.99
intrinsic dark rate     < 1e-6 s^-1 exploratory target
persistent output       one or more fluxoid states
Johnson floor           absent from ideal superconducting storage channel
```

These are research targets, not demonstrated device specifications.

## Canonical recovery order

A new agent should read:

1. `AGENTS.md`
2. `CURRENT_STATE.md`
3. `DERIVATION_LOG.md`
4. `CLAIM_LEDGER.md`
5. `ASSUMPTIONS.md`
6. `LITERATURE_LEDGER.md`
7. `NOVELTY_GATES.md`

Do not reconstruct the science from conversation history when repository records exist.

## Manuscript gate

Do **not** create `manuscript_v1/` merely because the device concept is interesting. A manuscript starts only after:

1. the exact time-dependent stochastic model survives quantitative falsification;
2. realistic material/device parameters leave a nonempty operating region;
3. a hostile literature-collision audit is complete;
4. at least one contribution survives as genuinely nontrivial rather than a recombination of standard SNSPD/KID/Josephson-calorimeter/rf-SQUID physics.

See `NOVELTY_GATES.md`.

## Public-disclosure note

This repository is public. Technical details committed here should be treated as public disclosure. No patentability judgment is made by this repository; preserve that distinction in future work.
