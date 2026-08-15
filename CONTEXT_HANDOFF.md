# CONTEXT_HANDOFF.md — Live Agent Continuity Pointer

**Repository:** `Kajin-0/gedanken`  
**Active research experiment:** `experiments/03-superconducting-photon-flux-transduction/`  
**Updated:** 2026-08-15  
**Mode:** Experiment 03 exploratory theory / falsification-first

> **LIVE `main` ALWAYS WINS.** Other agents may edit concurrently. Before every write, fetch current HEAD, inspect relevant intervening commits, fetch the exact current target blob, and never write from a stale SHA.

## Recovery order

1. root `AGENTS.md` — repository-wide integrity and frozen-track rules;
2. `experiments/03-superconducting-photon-flux-transduction/AGENTS.md`;
3. `experiments/03-superconducting-photon-flux-transduction/CURRENT_STATE.md`;
4. `experiments/03-superconducting-photon-flux-transduction/DERIVATION_LOG.md`;
5. `experiments/03-superconducting-photon-flux-transduction/CLAIM_LEDGER.md`;
6. `experiments/03-superconducting-photon-flux-transduction/ASSUMPTIONS.md`;
7. `experiments/03-superconducting-photon-flux-transduction/LITERATURE_LEDGER.md`;
8. `experiments/03-superconducting-photon-flux-transduction/NOVELTY_GATES.md`;
9. `experiments/03-superconducting-photon-flux-transduction/calculations/`.

## One-sentence current state

The preferred Generation-A mechanism is now a **single-LWIR-photon calorimetric rf-SQUID fold trigger**: the optical pulse transiently changes the Josephson CPR until a metastable flux well disappears, the phase moves into the externally favored basin, and the recovered superconducting circuit stores the event as persistent flux.

## Strongest analytic checkpoint

For an arbitrary temperature-dependent CPR, define

```math
I_* = \Phi_0/(2\pi L),
\qquad
\mathcal I(x,T)=I_s(x,T)/I_*.
```

With

```math
F(x,T)=x-\delta-\mathcal I(x,T),
```

a static fold satisfies

```math
\boxed{\mathcal I(x_c,T_c)=x_c-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_c,T_c)=1.}
```

If `mathcal I=beta(T) f(x)`, then

```math
\boxed{\beta_c=1/f'(x_c),}
\qquad
\boxed{\delta=x_c-f(x_c)/f'(x_c).}
```

For the sinusoidal benchmark this reduces to

```math
\delta=\tan a-a,
\qquad
\beta_c=\sec a.
```

The universal local fold barrier scales as

```math
\Delta U\propto|p-p_c|^{3/2},
```

while the small-oscillation frequency scales as `|p-p_c|^(1/4)`, so the basic quantum-action scale behaves as `|p-p_c|^(5/4)`. This is the central trigger-vs-dark-stability tradeoff.

## Current numerical checkpoint

For the sinusoidal illustrative point

```text
delta       = 0.05 rad
beta_cold   = 1.5
Ic,cold     = 3 uA
C           = 200 fF
```

we obtain

```text
beta_c                    = 1.14712
required Ic suppression   = 23.53 %
L                         = 164.55 pH
cold metastable barrier   = 9.443 k_B K
local plasma frequency    = 24.80 GHz
state separation          = 0.4753 Phi0 = 5.97 uA
sqrt(LC)                  = 5.74 ps
```

A square pulse to `beta_hot=1.05` crosses the central phase coordinate on roughly a 20-ps scale in the deterministic RCSJ diagnostic.

Important: `23.5%` is not universal. A normalized illustrative second-harmonic CPR changes the required suppression from about 6.6% to 43.6% over the tested shape range. A real device requires measured or microscopic `I_s(phi,T)`.

## Optical / thermal checkpoint

For `C_e=gamma_S A T`, define the scalar-amplitude threshold by

```math
I_c(Tcrit)/I_c(T0)=beta_c/beta_cold.
```

Then

```math
\eta_{th}h\nu
\ge
\frac{\gamma_S A}{2}(Tcrit^2-T0^2).
```

Conditionally using the published 2026 graphene thermal scale and the observation that its switching-current scale drops by about 30% between 20 mK and 1.2 K, the benchmark 23.5% threshold would occur by `Tcrit <= 1.2 K` if a comparable monotonic nonequilibrium `I_c(T_e)` applies.

At `lambda=10 um`, using the published reference calorimeter:

```text
photon energy                  = 123.98 meV
A_max at eta_th=1, Tcrit=1.2K = 67.29 um^2
working target area            = 15.50 um^2
heat-capacity margin           = 4.34 x
eta_th,min at 15.5 um^2        = 0.230
required retained heat         = 28.56 meV
```

This is a **conditional plausibility bound**, not a validated device prediction. The immediate bottleneck is now the actual nonequilibrium CPR / `I_c(T_e)`, not simple photon energy.

## Major prior-art collisions found

Do not claim novelty for:

```text
LWIR superconducting single-photon detection
photon -> hot graphene -> Josephson switching
single photon -> persistent superconducting single-flux memory
optically generated permanent superconducting flux/vortices
transient Ic suppression -> rf-SQUID barrier lowering/freeze
field-free Josephson/superconducting diode directionality
illumination-driven superconducting phase battery/vorticity switching
```

Most important new collisions:

- Onen et al. 2020 — experimentally demonstrated single-photon-to-single-flux conversion with superconducting multilevel memory;
- Rochet et al. 2020 — optically wrote permanent single vortices;
- Zhou/Habif/Bocko/Feldman 2001 — transient critical-current suppression used to lower an rf-SQUID barrier and then freeze a flux state.

The novelty corridor is therefore narrow. Candidate surviving routes are a quantitatively distinct single-LWIR calorimetric fold regime, a new general efficiency/dark-count/heat-capacity closure, or a genuinely self-directed zero-external-flux mechanism.

## Immediate next task

Do **not** spend more time on the static sinusoidal potential unless testing robustness. The next decisive chain is

```text
absorbed 8–14 um photon
 -> T_e(t), including diffusion + electron-phonon cooling
 -> physically defensible I_s(phi,T_e)
 -> time-dependent general-CPR fold crossing
 -> stochastic/damped basin capture
 -> P_capture, P_wrong, P_no-switch
```

Then compute cold thermal escape and dissipative MQT separately, followed by optical coupling, readout and reset.

## Reproducible scripts

```text
calculations/rfsquid_bifurcation_scan.py
calculations/general_cpr_fold.py
calculations/thermal_bifurcation_margin.py
```

These are exploratory reproducibility scripts, not a validated CI suite.

## Publication state

**GO for continued theory. NO-GO for manuscript.** `NOVELTY_GATES.md` remains authoritative.

Experiments 01 and 02 remain frozen/submission tracks; do not modify their science while working Experiment 03.
