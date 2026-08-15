# CONTEXT_HANDOFF.md — Live Agent Continuity Pointer

**Repository:** `Kajin-0/gedanken`  
**Active research experiment:** `experiments/03-superconducting-photon-flux-transduction/`  
**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first

> **LIVE `main` ALWAYS WINS.** Before every write, fetch current HEAD, inspect intervening commits, fetch the exact target blob, and never overwrite a stale SHA.

## Recovery order

1. root `AGENTS.md`;
2. Experiment 03 `AGENTS.md`;
3. `CURRENT_STATE.md`;
4. `ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md`;
5. `FEASIBILITY_CLOSURE_2026-08-15.md`;
6. `DERIVATION_LOG.md`;
7. `CLAIM_LEDGER.md`;
8. `ASSUMPTIONS.md`;
9. `LITERATURE_LEDGER.md`;
10. `NOVELTY_GATES.md`;
11. `calculations/`.

## One-sentence state

Generation A is a **single-LWIR-photon calorimetric rf-SQUID fold latch**: photon heating changes the full Josephson CPR until a metastable CPR/load-line intersection disappears; the phase should settle into the externally favored basin and remain as persistent superconducting flux after recovery.

Generation A is externally flux tilted and is not photovoltaic.

## Canonical fold formulation

```math
I_* = \Phi_0/(2\pi L),
\qquad
\mathcal I(x,T)=I_s(x,T)/I_*,
\qquad
F=x-\delta-\mathcal I.
```

Fold:

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

Near any smooth fold:

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto|p-p_f|^{5/4}.
```

## Current arbitrary-length graphene checkpoint

The short-junction CPR has been replaced by an ideal arbitrary-length ballistic graphene SNS calculation based on the Titov–Beenakker secular equation plus the Hagymási–Kormányos–Cserti Matsubara-current method.

Validation:

- short-limit `ell=0.01`, `mu=0` converges toward Titov–Beenakker Eq.20 at sub-percent-to-percent normalized-CPR level on current finite grids;
- `ell~1.1` develops strongly forward-skewed low-T CPR and thermal softening;
- finite-doping fold needs `Qmax~30` for convergence.

Model checkpoint:

```text
Delta0=1.3 meV
ell=L_JJ/xi0=1.1
delta=0.05
T0=20 mK.
```

Cold normalized fold:

```text
mu/Delta0=0     beta_fold~0.463
mu/Delta0=10    beta_fold~0.325
mu/Delta0=20    beta_fold~0.200.
```

Strong illustrative point:

```text
ell=1.1
mu/Delta0=20
beta_cold=0.8
Ic0 physical scale=3 uA
T_fold~1.118 K
reference thermal-energy fraction~0.200
cold barrier/k_B~16.70 K
L~87.76 pH
provisional C_min,Q~71 fF
state separation~0.2535 Phi0
current-state gap~5.97 uA.
```

At the same `beta=0.8`, changing `mu/Delta0` from `0` to `20` leaves `T_fold` near `1.1 K` but raises the cold barrier from roughly `7.0 K` to `16.7 K` and reduces provisional `C_min,Q` from roughly `262 fF` to `71 fF`. In the ideal model, doping mainly buys cold stability.

**Critical caveat:** this is ballistic, rigid-boundary, ideal-interface equilibrium theory. It is not calibrated to the 600-nm MoRe/graphene detector. `ell~O(1)` is only the correct regime scale.

Canonical script:

```text
calculations/arbitrary_length_graphene_cpr.py
```

## Feasibility closure retained

Static optical threshold:

```math
\boxed{
E_{fold}=\eta_{th}^{-1}\int_{T_0}^{T_f}C_e(T)dT.
}
```

Time above fold:

```math
\boxed{
t_>(E_\gamma)=\int_{T_f}^{T_{pk}(E_\gamma)}\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

Inside the current provisional MQT model:

```math
\boxed{
C_{min,Q}
=\frac{\hbar^2\kappa_c}{\alpha_Q^2\Delta U_c^2L}
\left[W\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right)\right]^2.
}
```

Necessary write-time scale:

```math
\boxed{
t_{req}^*=\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}].
}
```

Necessary chain:

```math
E_\gamma\ge E_{fold},
\qquad
t_>(E_\gamma)\ge t_{req}^*,
\qquad
\Delta U_c\gtrsim k_BT_0\ln(\Omega_T/D).
```

For the idealized clean-graphene `T^4` cooling model there is a finite maximum time above a fixed fold:

```math
\boxed{
t_{>,max}=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right).
}
```

If `t_req >= t_>,max`, no larger photon energy rescues the design **within that thermal model**.

## Prior-art boundary

Do not claim novelty for:

```text
LWIR superconducting single-photon detection
photon-heated graphene -> Josephson switching
photon heating -> proximity-JJ Ic suppression -> SQUID detection
single photon -> persistent superconducting flux memory
optically written persistent superconducting flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven superconducting phase battery/vorticity switching
non-sinusoidal temperature-dependent graphene CPRs.
```

No novelty claim is authorized.

## Immediate next task

Do not return to the short-junction toy model except for regression. Attack the assumptions that now dominate uncertainty:

```text
1. quantitatively validate arbitrary-length CPR/skewness against published curves;
2. introduce finite/nonideal SG interface transparency and realistic contact doping;
3. calibrate ell, mu/Delta0, Delta(T), Ic to a plausible photon-sensitive junction;
4. test whether early photon absorption is sufficiently thermal to use I_s(phi,T_e);
5. compute dissipative MQT for the full-CPR cold potential;
6. solve stochastic finite-rate fold passage/retrapping with R_hot(T);
7. add 8–14 um optical coupling and reset/readout.
```

## Reproducible scripts

```text
rfsquid_bifurcation_scan.py
general_cpr_fold.py
thermal_bifurcation_margin.py
thermal_diffusion_margin.py
dynamic_margin.py
short_dirac_cpr_fold.py
capacitance_stability_window.py
arbitrary_length_graphene_cpr.py
```

These are exploratory calculations, not validated CI.

## Publication state

**GO for continued theory. NO-GO for manuscript.** The strongest surviving candidate contribution is a quantitative feasibility/optimality or impossibility closure, not the broad device concept.

Experiments 01 and 02 remain frozen/submission tracks.
