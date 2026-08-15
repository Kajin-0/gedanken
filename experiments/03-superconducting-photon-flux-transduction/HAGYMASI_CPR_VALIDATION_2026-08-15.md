# Hagymasi Intermediate-Length CPR Validation — 2026-08-15

## Purpose

Validate the canonical arbitrary-length ballistic graphene CPR implementation against a published **intermediate-length** parameter set, not only against the analytic short-junction limit.

Primary source:

- I. Hagymasi, A. Kormanyos, J. Cserti, *Josephson current in ballistic superconductor-graphene systems*, Phys. Rev. B **82**, 134516 (2010), arXiv:1006.3228.

The paper's Fig. 1(c,d) uses

```text
xi/L = 0.91  -> L/xi = 1.098901...
mu/Delta0 = 0 and 20
T/Tc = 0, 0.18, 0.35
xi/W = 0.05
```

The paper defines skewness

```math
S=2\phi_{max}/\pi-1.
```

Its stated intermediate-junction behavior is:

1. low-temperature CPRs are positively forward skewed;
2. the doped `mu/Delta0=20` CPR at `L/xi~1.1` is already approaching a rounded sawtooth;
3. increasing temperature drives the CPR toward a sinusoid and reduces skewness.

The wide-junction continuum used by the code is compatible with this benchmark because the paper's geometry has `W/L=(xi/L)/(xi/W)~18.2`.

## Canonical implementation tested

```text
calculations/arbitrary_length_graphene_cpr.py
```

Regression driver:

```text
calculations/validate_hagymasi_intermediate_cpr.py
```

The regression uses `T/Tc=0.01` as a numerical low-temperature proxy for the plotted `T=0` curve.

## Central numerical result

Using

```text
qmax = 30
nq   = 500
wmax = 20
L/xi = 1/0.91
```

gives approximately:

| mu/Delta0 | T/Tc | phi_max [rad] | skewness S |
|---:|---:|---:|---:|
| 0 | 0.01 | 2.0882 | 0.3294 |
| 0 | 0.18 | 1.8791 | 0.1963 |
| 0 | 0.35 | 1.6701 | 0.0632 |
| 20 | 0.01 | 2.4279 | 0.5456 |
| 20 | 0.18 | 1.9627 | 0.2495 |
| 20 | 0.35 | 1.6910 | 0.0765 |

Therefore the implementation reproduces the full published **ordering and trend structure** at the paper's own intermediate-junction parameters:

```math
S(T\to0)>S(0.18T_c)>S(0.35T_c)>0,
```

for both dopings, and

```math
S_{\mu/\Delta_0=20}(T\to0)>S_{\mu=0}(T\to0).
```

The very large low-T doped value `S~0.546` is consistent with the paper's qualitative statement that its `L/xi~1.1`, `mu/Delta0=20` CPR is already transitioning toward the long-junction sawtooth form.

## Numerical convergence

Three integration settings were compared:

```text
(qmax,nq,wmax) = (25,400,15)
                  (30,500,20)
                  (35,700,25)
```

At the 601-point phase grid used for the benchmark, all six reported skewness values are unchanged between these settings to the phase-grid resolution. The arbitrary current amplitudes are likewise stable; the largest visible sensitivity is the low-temperature highly doped amplitude and is only at the ~1e-4 relative scale between the coarse and high settings.

This removes transverse cutoff/Matsubara truncation as a plausible explanation for the strong intermediate-length skewness found in the current model.

## What this validates

This checkpoint materially strengthens the implementation validation:

- short-junction analytic limit: already passed against Titov–Beenakker;
- intermediate-length regime `L/xi~1.1`: now reproduces the published Hagymasi qualitative CPR structure at the same temperature and doping parameters;
- numerical integration is converged at the level relevant to the fold calculation.

## What this does NOT validate

This is **not** a point-by-point digitization of Fig. 1 and therefore is not yet a high-precision reproduction of the published plotted curves.

More importantly, it does not validate the ideal model against a fabricated MoRe/graphene photon detector. Hagymasi et al. explicitly use rigid superconducting boundaries and highly doped ideal superconducting electrodes; their model neglects band bending and other contact-induced effects. Those are the next important uncertainty for Experiment 03.

The 2016/2017 ballistic graphene CPR work by Nanda et al. found that realistic tight-binding models including graphene-superconductor interfaces are needed for good qualitative agreement with measured gate-dependent CPRs. This supports moving next to **interface transparency/contact doping**, rather than doing more ideal-CPR algebra.

## Disposition

**PASS — ideal arbitrary-length CPR implementation gains a parameter-level intermediate-junction validation.**

This does not change publication status. Experiment 03 remains **GO for continued theory / NO-GO for manuscript**.

## Next falsification step

Introduce a controlled interface-nonideality parameterization and determine how robust the apparent `mu/Delta0=20`, `beta_cold~0.8` stability advantage is to reduced Andreev transparency/contact mismatch.

The quantity to watch is not merely `I_c`; recompute the full chain

```text
interface model
 -> I_s(phi,T)
 -> fold T_f
 -> cold barrier and curvature
 -> state separation
 -> MQT/stability diagnostic
 -> optical fold energy / dwell requirement.
```
