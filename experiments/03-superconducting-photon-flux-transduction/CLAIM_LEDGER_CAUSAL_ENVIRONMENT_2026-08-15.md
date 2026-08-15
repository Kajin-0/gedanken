# Experiment 03 — Causal Environment Claim Ledger — 2026-08-15

This ledger continues `CLAIM_LEDGER_DYNAMIC_2026-08-15.md` after the initial-Wigner / exact-quench stage. Live `main` wins over older summaries.

| Claim | Status | Notes |
|---|---|---|
| The coarse `rDelta=.6`, `R~160–400 ohm` scan establishes a broad `>99%` initial-Wigner capture plateau | **REJECTED / NUMERICAL-RESOLUTION ARTIFACT** | full nested refinement gives ~0.9801 (160 ohm), ~0.9901 (250 ohm), ~0.9871 (400 ohm) |
| `rDelta=.6`, `rise=20 ps`, `R=250 ohm` has initial-Wigner capture probability ~0.9901 in the scalar-R / classical-propagation model | **DERIVED NUMERICAL MODEL RESULT** | before pulse-time bath noise and exact open-system quantum evolution |
| `rDelta=.8` remains competitive in initial-state basin robustness | **DISFAVORED** | refined probabilities near candidate damping points are only ~0.80–0.81 |
| An infinite-bandwidth scalar resistor is a physically adequate final environment | **REJECTED** | damping, FDT noise, reactive loading and dissipative quantum escape must come from one causal spectral environment |
| A passive two-pole network can realize `ReY=(1/R)/[1+(omega/omega_D)^4]` | **DERIVED EXACTLY** | choose `Lf=sqrt(2)R/omega_D`, `Cf=1/[sqrt(2)R omega_D]` |
| The passive two-pole filter simply acts like a frequency-dependent effective R without changing basin topology | **REJECTED** | deterministic center-state outcome is non-monotonic in cutoff at some R; filter memory/reactance reshapes trajectory |
| The passive-filter total energy satisfies `d(E/E_L)/dt=U_T Tdot-(L/R)w^2` | **DERIVED EXACTLY** | filter L/C store energy reversibly; only resistor term dissipates |
| Useful finite-band filtering necessarily causes large cold phase-coordinate broadening | **NOT SEEN IN CURRENT LINEAR FDT SCREEN** | at r=.6, R=250 ohm, alpha=.2–1, sigma_x changes only at percent scale |
| The reduced phase coordinate and velocity variances remain UV divergent for the quartic-rolloff environment | **REJECTED** | `ReY~omega^-4` makes both reduced variances UV convergent |
| Sampling arbitrary auxiliary lumped bath coordinates from their apparent equal-time Gaussian covariance gives a representation-independent physical initial detector state | **REJECTED** | auxiliary capacitor-voltage variance is logarithmically UV/cutoff sensitive for ideal quantum resistor realization |
| The completed 4D auxiliary-state GH capture scout can be interpreted as physical detector efficiency | **REJECTED / PROVENANCE ONLY** | its probabilities depend on a noncanonical UV-sensitive auxiliary covariance representation |
| For the quartic-rolloff bath at T->0, `<I_N^2>=hbar omega_D^2/(4R)` | **DERIVED EXACTLY** | follows from the symmetrized FDT integral and `integral x/(1+x^4)=pi/4` |
| For this bath, `sigma_I tau_D=sqrt[hbar/(2R)]` with `tau_D=sqrt(2)/omega_D` | **DERIVED EXACTLY FOR THIS FILTER FAMILY** | explicit noise-memory product; not asserted universal for all passive Y |
| Lowering omega_D can reduce integrated bath-force scale without any time-domain penalty | **REJECTED FOR THIS FILTER FAMILY** | lower force scale is exactly accompanied by longer causal memory |
| For a prescribed voltage waveform in a linear equilibrium bath, `Var(W_N)=epsilon_eff Q_diss` | **DERIVED EXACTLY** | `epsilon_eff` is dissipation-weighted `hbar|omega|coth(...)`; use symmetrized FDT convention |
| At fixed prescribed waveform and fixed dissipated energy, moving dissipation to lower frequencies reduces FDT work variance per dissipated energy | **DERIVED FROM MONOTONICITY OF hbar|omega|coth(...)** | does not imply same ordering after trajectory itself changes with Y |
| The first 1.5-ns FDT work-noise numbers were fully converged | **REJECTED** | strongly filtered cases retained significant finite-window energy/memory |
| Full-recovery `R=250 ohm` FDT work scale converges to sigma_W/kB ~2.3–2.45 K across alpha=.2–.5 | **DERIVED PRESCRIBED-TRAJECTORY DIAGNOSTIC** | 20–80 ns spectral/time dissipation agrees; not an activation probability |
| Full-recovery sigma_W should be compared directly to the metastable left cold barrier to infer capture failure | **REJECTED / OVERLY PESSIMISTIC** | most late dissipation occurs after the phase is in favored state; wrong-way barrier is directionally larger |
| At rDelta=.6 cold state, left-to-saddle barrier is ~6.91 K while right-to-saddle barrier is ~12.20 K | **DERIVED NUMERICAL MODEL RESULT** | same full-CPR tilted loop |
| As the metastable left well approaches its fold, both directional barriers vanish | **REJECTED FOR CURRENT TILTED LOOP** | left barrier ->0, but right-to-saddle barrier remains ~3.8–3.9 K near fold |
| At 14 um, rise=20 ps, R=250 ohm and alpha=.2–.5, the deterministic causal-filter phase reaches the favored side before left-well reformation | **DERIVED NUMERICAL MODEL RESULT** | one x=0 crossing at ~44.6–46.9 ps; reformation at ~57.75 ps |
| The deterministic phase repeatedly crosses back before recovery in those three causal-filter points | **REJECTED** | one sign crossing only in tested deterministic trajectories |
| At left-well reformation, the favored-state return barrier is already finite ~3.83 k_B K | **DERIVED NUMERICAL MODEL RESULT** | current r=.6 tilted topology; phase is already x~+0.42 to +0.62 |
| Symmetrized zero-point FDT noise may be sampled as an ordinary classical random force to obtain physical 20-mK capture probabilities | **REJECTED** | would not preserve quantum detailed balance; can spuriously turn vacuum fluctuations into activation |
| Symmetrized FDT work/adjoint covariance can still be used as a linear quantum susceptibility diagnostic | **CONDITIONAL / ACCEPTED SCREEN** | does not itself equal an error probability |
| Current causal-environment model is a calibrated device prediction | **REJECTED** | optical/spatial thermal model, exact open-system dynamics, physical Y, dissipative MQT and readout remain incomplete |
| Manuscript is justified now | **NO-GO** | quantitative and novelty gates remain open |

## Current interpretation

The dominant environment question has narrowed from

```text
How large is total bath noise during the full recovery?
```

to

```text
Can the phase reach the favored side before the metastable left well reforms,
under a single causal Y(omega) that also satisfies FDT and dark-stability constraints?
```

The directional tilted topology helps: the left escape barrier collapses, but the favored-state return barrier is already finite when bistability returns.

**GO for continued theory. NO-GO for manuscript.**
