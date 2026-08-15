# Interface / Skewness Sensitivity Checkpoint — 2026-08-15

## Question

The ideal arbitrary-length ballistic model at `ell~1.1`, `mu/Delta0=20` gives a very strongly forward-skewed cold CPR (`S~0.55`). Real ballistic graphene Josephson junctions with explicit graphene-superconductor interfaces show materially smaller skewness. Does reducing that ideal skewness immediately destroy the proposed fold-trigger / persistent-flux corridor?

## Experimental/theoretical anchor

Nanda et al., *Current-phase relation of ballistic graphene Josephson junctions* (arXiv:1612.06895), measured ballistic MoRe/graphene junction CPRs and modeled them using tight-binding BdG calculations with explicit interfaces.

Important reported facts:

- realistic interface modeling was required for good qualitative agreement;
- their top-contact model had an average high-n-doping transparency around `Tr=0.82`;
- a finite quasiparticle broadening `eta=0.17 Delta` reduced calculated skewness;
- representative average skewness values were approximately:

```text
hard-gap nn'n calculation:       Sbar ~0.27
soft-gap nn'n calculation:       Sbar ~0.22
soft-gap npn calculation:        Sbar ~0.19
measured nn'n scale:             Sexp ~0.28
measured npn scale:              Sexp ~0.20
```

They also report that interface hopping, contact-doping profile and transition smoothness alter skewness. Therefore the present rigid-boundary ideal CPR is expected to be optimistic in shape.

## Controlled shape-only stress test

This checkpoint does **not** pretend to replace the tight-binding interface model.

Define a one-parameter deformation

```math
f_\lambda(\phi,T)=
\operatorname{norm}\left[(1-\lambda)\sin\phi+\lambda f_{ideal}(\phi,T)\right],
```

while retaining the ideal arbitrary-length model's `Ic(T)` amplitude ratio.

Thus:

```text
lambda=1 -> ideal arbitrary-length CPR
lambda=0 -> sinusoidal shape
```

Choose `lambda` so the cold skewness approximately reaches the Nanda realistic-interface scales.

Canonical script:

```text
calculations/interface_skewness_sensitivity.py
```

This is a **CPR-shape sensitivity envelope**, not a microscopic SG-interface prediction.

## Fixed circuit point

Use the current illustrative checkpoint:

```text
ell=1.1
mu/Delta0=20
delta=0.05
beta_cold=0.8
Ic physical scale=3 uA
T0=20 mK
D target=1e-6 s^-1 in the provisional MQT diagnostic.
```

The inductance remains

```text
L = 87.76 pH
```

because `beta_cold` and the physical `Ic` scale are held fixed.

## Result

| cold S target | lambda | cold beta_fold | T_fold | cold barrier/kB | state separation | provisional C_min,Q |
|---:|---:|---:|---:|---:|---:|---:|
| ~0.548 ideal | 1.000 | 0.201 | 1.118 K | 16.70 K | 0.2535 Phi0 | 71 fF |
| ~0.270 | 0.590 | 0.298 | 0.905 K | 9.12 K | 0.2401 Phi0 | 160 fF |
| ~0.220 | 0.515 | 0.335 | 0.841 K | 7.14 K | 0.2303 Phi0 | 230 fF |
| ~0.190 | 0.468 | 0.364 | 0.794 K | 5.89 K | 0.2225 Phi0 | 307 fF |

## Interpretation

This is a meaningful correction to the ideal-model optimism.

Moving from the ideal `S~0.55` shape to experimentally realistic `S~0.19–0.27` scales:

1. lowers the fold temperature by roughly **19–29%**;
2. lowers the cold barrier by roughly **45–65%**;
3. increases the provisional MQT capacitance floor by about **2.3–4.3x**;
4. reduces the state separation only modestly, from about `0.254 Phi0` to `0.223–0.240 Phi0`.

Therefore the principal damage from realistic interface-induced harmonic suppression is **cold-state stability**, not disappearance of the persistent-state readout gap.

Most importantly, the selected `beta_cold=0.8` point remains above the cold fold in all stressed cases:

```text
beta_fold,cold ~0.30–0.36 < beta_cold=0.8.
```

The fold-trigger architecture therefore survives this first empirically anchored CPR-shape stress test.

## What cannot be concluded

The result is not yet sufficient to claim realistic feasibility because the deformation holds the ideal `Ic(T)` amplitude ratio fixed. A real interface changes simultaneously:

```text
absolute Ic
Ic(T)
induced gap
CPR harmonics
contact heat out-diffusion
normal resistance/damping
quasiparticle spectrum.
```

Nanda et al. explicitly found that the induced graphene gap can be smaller than bulk MoRe and that realistic contacts are needed to reproduce the measured temperature dependence. A microscopic or calibrated nonideal model could therefore damage the corridor more strongly than this shape-only test.

## New strongest lesson

The ideal high-doping result should no longer be summarized as

> doping gives a 16.7-K cold barrier at beta=0.8.

The defensible statement is now:

> In the rigid-boundary ideal model the barrier is ~16.7 K, but CPR-shape deformation to realistic measured/interface-model skewness scales reduces it to roughly 6–9 K while retaining the fold and a ~0.22–0.24 Phi0 state separation.

This is the appropriate uncertainty range until a microscopic interface model is solved.

## Next step

The next falsification target is no longer generic 'interface transparency' by itself. The highest-value correction is to include a reduced **induced gap / temperature scale** together with interface-induced CPR harmonic suppression, because this directly controls `Ic(T)` and therefore the optical fold temperature.

A practical next model should sweep an induced-gap ratio

```math
r_\Delta=\Delta_{ind}(0)/\Delta_{MoRe}(0)
```

and recompute the full fold/stability chain under the empirically anchored CPR-shape envelope.

If modest `r_Delta<1` collapses the capacitance/dwell window, the architecture is fragile. If a broad window survives, a full TB-BdG/interface calculation becomes worth the computational cost.
