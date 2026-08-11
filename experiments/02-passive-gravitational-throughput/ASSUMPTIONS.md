# Assumptions and Scope — Experiment 02

These assumptions define the theorem currently established in the validated PRD manuscript. They are part of the claim boundary, not optional prose.

## Included theorem class

- weak linearized gravity on an approximately flat background;
- nonrelativistic endpoint matter;
- leading mass-quadrupole coupling;
- passive, linear endpoint dynamics;
- complex-envelope operation with physical frequency

```math
\omega(\nu)=\omega_0+\nu;
```

- a measured detuning band `B_nu` with

```math
\omega_- = \inf_{\nu\in B_\nu}\omega(\nu)>0,
\qquad
\omega_+ = \sup_{\nu\in B_\nu}\omega(\nu);
```

- compact endpoints across the complete measured band,

```math
\omega_+ a_A/c \ll 1,
\qquad
\omega_+ a_B/c \ll 1;
```

- separated outgoing propagation across the measured band,

```math
\omega_- R/c \gg 1;
```

- retained endpoint physical modal frequencies satisfying

```math
\omega_n\le\Omega;
```

- arbitrary passive internal unitary mode mixing within the retained realization;
- all unobserved passive loss/radiation channels retained in the physical model rather than silently discarded;
- same-two-endpoint passive gravitational recurrence whenever the stated resolvent exists (`p_+p_-<1`).

The direct finite/countably-infinite proof is formulated on a well-posed local-in-time passive realization with bounded selected port maps and a Hilbert--Schmidt retained gravitational observation. Reduced non-Markovian dynamics can remain inside the theorem logic if the eliminated passive degrees of freedom can be restored to an enlarged well-posed passive realization for which the selected maps are bounded or otherwise admissible and the gravitational observation retains the required finite trace.

## Frequency convention

```text
omega_0   reference carrier angular frequency
nu        complex-envelope detuning
omega     physical frequency = omega_0 + nu
omega_-   minimum physical frequency in the measured band
omega_+   maximum physical frequency in the measured band
Omega     upper physical frequency of the retained endpoint modal sector
```

The passive spectral-area integration is over detuning `nu`. The **rigorous finite-band theorem does not freeze propagation at `omega_0`**: it retains the exact outgoing compact-TT sector weights at `omega(nu)` through measured-band suprema.

For a carrier-scale narrow band with `B/omega_0 << 1` and `Omega = omega_0[1+O(B/omega_0)]`, the rigorous theorem reduces to the transparent carrier form

```math
\Gamma_{\rm coh}
\lesssim
\frac{5G\omega_0^2}{4c^3R^2}
\min(I_{\hat R,A},I_{\hat R,B}).
```

The `lesssim` belongs to this final narrowband/far-zone reduction; it is not a strict finite-distance inequality for arbitrary extended bodies.

## Retained-frequency limitation

The modal gravitational rate

```math
\kappa_{g,n}
=\frac{G\omega_n^4}{5c^5}\frac{q_n:q_n}{\mu_n}
```

is an **on-shell linewidth at the mode's own frequency**. It must not be assigned unchanged to the low-frequency tail of a far-detuned high-frequency mode.

Scalar and sector completeness control unweighted quadrupole projection sums, not the unrestricted fourth frequency moment. Therefore the current inertia-controlled theorem does **not** remove `Omega` from the complete endpoint spectrum. A whole-spectrum result would require additional elastic/constitutive regularity, a microscopic cutoff, or a different frequency-domain sum rule.

## Not assumed

The proof does not require

- single-mode endpoints;
- equal source and receiver linewidths;
- critical coupling;
- identical source/receiver geometries;
- high-`Q` or low-`Q` limits;
- saturation of any intermediate inequality;
- a finite resonance count;
- a particular passive internal basis;
- memoryless reduced coordinates.

## Explicit exclusions / unproved classes

The current theorem does not establish a universal result for

- uncontrolled whole-spectrum endpoint dynamics under the same inertia-only trace closure;
- arbitrary hereditary constitutive laws or singular continuum baths for which no admissible passive enlargement and finite gravitational trace have been proved;
- unbounded PDE boundary-control/observation ports without a system-node/admissibility analysis;
- active gain, inversion, parametric pumping, or externally powered feedback;
- extended phased apertures outside the compact regime;
- added gravitational relays, mirrors, or external cavities;
- reactive/near-field exchange outside the separated-wave regime;
- relativistic or strongly nonlinear matter motion;
- higher-multipole-dominated operation;
- strong-field or curved-background focusing;
- quantum-gravity corrections beyond the linearized weak-field model.

A bounded finite crystal is **not** excluded merely because continuum elasticity or microscopic damping is used. What must be justified for a concrete device is the retained passive representation over the measured band.

## Canonical resource definitions

```math
I_{\hat R}=\int\rho[r^2-(\hat R\cdot x)^2]d^3x,
\qquad
Z_{\hat R}=\int\rho(\hat R\cdot x)^2d^3x,
\qquad
I_2=I_{\hat R}+Z_{\hat R}.
```

The strongest leading theorem uses `I_Rhat`. The former scalar `25/12 * I_2` result remains a valid looser fallback obtained after discarding STF-sector information.

## Novelty discipline

Do not claim novelty for generic passive `H2` machinery, gain-bandwidth principles, resonant-mass gravitational response, material sum rules, directivity, multiple scattering, infinite-dimensional passive-system theory, or gravity as a communication mediator. No priority claim has been established for the complete closure.
