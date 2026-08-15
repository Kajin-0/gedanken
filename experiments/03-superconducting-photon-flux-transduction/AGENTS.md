# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** none; do not create one until `NOVELTY_GATES.md` is passed.

## Recovery order

Read, in order:

1. `CURRENT_STATE.md`
2. `DERIVATION_LOG.md`
3. `CLAIM_LEDGER.md`
4. `ASSUMPTIONS.md`
5. `LITERATURE_LEDGER.md`
6. `NOVELTY_GATES.md`
7. `README.md`
8. reproducible scripts in `calculations/`

Conversation history is not authoritative when it conflicts with repository state.

## Current objective

Determine whether a **single absorbed LWIR photon** can calorimetrically drive a Josephson/rf-SQUID fold transition with high capture probability, low wrong-way capture and extremely low cold false-switch probability, while producing a persistent superconducting readout state.

Generation A uses a small external flux tilt. Generation B may later seek zero-external-flux directionality through a `phi0`, Josephson-diode or other symmetry-breaking element.

## Current strongest checkpoints

### General fold criterion

Use the dimensionless phase force

```math
F(x,T)=x-\delta-\mathcal I(x,T),
\qquad
\mathcal I=I_s/I_*,
\qquad
I_*=\Phi_0/(2\pi L).
```

A static fold satisfies

```math
\mathcal I(x_c,T_c)=x_c-\delta,
\qquad
\partial_x\mathcal I(x_c,T_c)=1.
```

For a separable CPR `mathcal I=beta(T) f(x)`, this becomes

```math
\beta_c=1/f'(x_c),
\qquad
\delta=x_c-f(x_c)/f'(x_c).
```

The sinusoidal benchmark gives `delta=tan(a)-a`, `beta_c=sec(a)`.

### Benchmark

```text
delta       = 0.05
beta_cold   = 1.5
Ic,cold     = 3 uA
C           = 200 fF
beta_c      = 1.14712
Ic drop     = 23.53 %
L           = 164.55 pH
cold barrier= 9.443 k_B K
readout gap = 0.4753 Phi0 = 5.97 uA
local fp    = 24.80 GHz
```

A deterministic square pulse below the fold crosses the phase barrier on a ~20-ps scale in the current RCSJ diagnostic, far faster than the ~75-ns graphene thermal benchmark.

### Thermal threshold closure

In the scalar-amplitude approximation,

```math
I_c(T_{crit})/I_c(T_0)=\beta_c/\beta_{cold}.
```

For `C_e=gamma_S A T`,

```math
\eta_{th}h\nu\ge\frac{\gamma_S A}{2}(T_{crit}^2-T_0^2).
```

Conditionally using the published graphene thermal scale and `Tcrit<=1.2 K`, a 10-um photon in a 15.5-um^2 absorber has an estimated heat-capacity margin of ~4.34x and requires ~23% retained electronic energy. This is not a validated nonequilibrium `I_c(T_e)` model.

## Mandatory discipline

1. Separate established background, derived model results, numerical extrapolations and novelty hypotheses.
2. Update `DERIVATION_LOG.md` after every important logical step, failed path, correction or collision.
3. Synchronize strengthened/weakened/falsified/collision-tested claims to `CLAIM_LEDGER.md`.
4. Synchronize preferred equations, architecture and immediate next task to `CURRENT_STATE.md`.
5. Add primary literature to `LITERATURE_LEDGER.md`; do not use conversation memory as prior-art evidence.
6. Do not use priority language before a dedicated paper-and-patent collision audit.
7. Do not equate zero DC resistance with zero total fluctuations or zero dark counts.
8. Do not treat the cubic `7.2 DeltaU/(hbar omega)` MQT form as an exact DCR for this device.
9. Do not assume a sinusoidal CPR for the final graphene/proximity design; use measured or microscopic `I_s(phi,T)`.
10. Do not assume adjacent fluxoid states differ by exactly `Phi0` in measured loop flux.
11. Do not call Generation A photovoltaic; it is externally flux tilted.
12. Do not create a manuscript because a parameter window looks promising.

## Major prior-art collisions already found

Do not claim novelty for:

```text
LWIR superconducting single-photon detection
photon -> hot graphene -> Josephson switching
single photon -> persistent superconducting single-flux memory
optically generated persistent superconducting flux/vortices
transient Ic suppression -> rf-SQUID barrier lowering/freeze
field-free Josephson/superconducting diode effects
illumination-driven superconducting phase battery/vorticity switching
```

Particularly important: Onen et al. 2020 closes the broad photon-to-persistent-flux-memory route; Zhou/Habif/Bocko/Feldman 2001 closes generic transient-`I_c` rf-SQUID tipping as a novelty route.

## Immediate work queue

1. Obtain or derive a physically defensible `I_s(phi,T_e)` / `I_c(T_e)` for a realistic photon-sensitive proximity junction.
2. Solve the 8–14-um photon thermal pulse including electronic heat capacity, diffusion to contacts and electron-phonon cooling.
3. Drive the **full CPR** through the fold conditions rather than only scaling a sinusoidal `I_c`.
4. Solve finite-rate stochastic RCSJ passage through the fold, including damping and hot-state conductance, to obtain `P_capture`, `P_wrong`, `P_no-switch`.
5. Compute cold thermal escape and **dissipative** MQT from the exact metastable potential.
6. Add optical coupling / absorptance and readout/backaction to obtain system-level rather than absorbed-photon metrics.
7. Quantify reset energy, dead time and stored-state SNR.
8. Search narrower paper/patent collisions only after a realistic nonempty region survives.

## Reproducible calculations

```text
calculations/rfsquid_bifurcation_scan.py
    exact sinusoidal roots/barriers, fold benchmark, RCSJ tipping diagnostic

calculations/general_cpr_fold.py
    general CPR fold equations and second-harmonic sensitivity

calculations/thermal_bifurcation_margin.py
    photon-energy / heat-capacity threshold margin
```

These scripts are exploratory regressions, not a validated CI suite.

## Stop conditions

Stop or reformulate if any of the following is robustly established:

- realistic `I_s(phi,T_e)` cannot be driven through the fold by one LWIR photon at usable optical efficiency;
- required optical perturbation destroys the ability to re-form and retain the intended flux state;
- exact thermal/MQT dark rates close the operating window for all plausible parameters;
- finite-rate capture produces unacceptable wrong-way/retrapping probability;
- reset/readout burden removes the claimed operating distinction;
- prior art contains the same narrow architecture and no independent theorem/performance result survives.

A negative result remains valuable if it produces a clean bound. Record it rather than forcing the architecture to survive.
