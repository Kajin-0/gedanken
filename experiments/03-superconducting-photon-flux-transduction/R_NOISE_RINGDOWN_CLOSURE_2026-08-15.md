# Experiment 03 — Resistance Noise–Ringdown Closure — 2026-08-15

## Purpose

The nonlinear causal-bath optimization is now scanning low-frequency resistance `R` as well as filter cutoff `alpha=omega_D/omega_c`. Within the retained quartic-rolloff passive environment, changing `R` reduces the bath-current fluctuation scale but simultaneously weakens passive damping of the cold phase mode.

This checkpoint eliminates `R` between those two effects in the weak-damping cold-mode approximation.

This is a closure for the retained filter family, not a universal theorem for arbitrary passive environments.

---

## 1. Integrated zero-point current scale

At `T -> 0`,

```math
\boxed{
\sigma_I^2
=\frac{\hbar\omega_D^2}{4R}.
}
```

At fixed `omega_D`,

```math
\sigma_I\propto R^{-1/2}.
```

---

## 2. Cold phase-mode ringdown

The dissipative loading at the phase frequency is

```math
\operatorname{Re}Y(\omega_c)
=\frac{1/R}{1+\alpha^{-4}},
\qquad
\alpha=\frac{\omega_D}{\omega_c}.
```

For a weakly damped phase oscillator,

```math
\Gamma_\phi
\simeq
\frac{\operatorname{Re}Y(\omega_c)}{2C},
```

hence

```math
\boxed{
\tau_\phi
\simeq
2RC(1+\alpha^{-4}).
}
```

At fixed `alpha,C,omega_c`,

```math
\tau_\phi\propto R.
```

---

## 3. Eliminate R

Using `omega_D=alpha omega_c`,

```math
\sigma_I^2\tau_\phi
=\frac{\hbar\alpha^2\omega_c^2}{4R}
\,2RC(1+\alpha^{-4}).
```

Therefore

```math
\boxed{
\sigma_I^2\tau_\phi
\simeq
\frac{\hbar C\omega_c^2}{2}
\left(
\alpha^2+\alpha^{-2}
\right).
}
```

The leading weak-damping product is independent of `R`.

Thus increasing resistance does not produce a free reduction of bath force. It exchanges

```text
smaller instantaneous/current fluctuation scale
for
longer passive phase relaxation.
```

---

## 4. Dimensionless form

Earlier define

```math
r_n
=\frac{\sigma_n}{\kappa_c\sigma_x},
\qquad
n=\frac{LI_N}{\bar\Phi},
```

and

```math
g=\frac{1}{RC\omega_c}.
```

For the quartic-rolloff environment,

```math
r_n^2=\frac{\alpha^2g}{2}.
```

The weak-damping phase ringdown satisfies

```math
\omega_c\tau_\phi
\simeq
\frac{2}{g}(1+\alpha^{-4}).
```

Hence

```math
\boxed{
r_n^2(\omega_c\tau_\phi)
\simeq
\alpha^2+\alpha^{-2}.
}
```

Again `R` and `g` cancel.

The right-hand side has minimum

```math
\alpha=1
```

with value

```math
2.
```

This minimum concerns only the product of integrated cold force scale and passive cold ringdown. It does **not** mean `alpha=1` optimizes detector capture, because nonadiabatic launch, reformation phase matching, target-basin geometry and FDT work all depend on the full spectral response.

---

## 5. Detector interpretation

The resistance scan can still improve detector fidelity because the latch does not necessarily require full passive equilibration before a valid persistent target state forms.

Current deterministic ordering is

```text
favored-side crossing ~45 ps
reformation ~58 ps
energetic lock only ~4–9 ps later
passive cold ringdown ~ns–tens of ns.
```

Therefore a larger `R` may be useful if

```text
lower bath forcing during the vulnerable write interval
```

matters more than

```text
slower passive ringing after energetic lock.
```

The nonlinear TWA/GLE `R-alpha` workflow is testing exactly that possibility.

If capture fails because weak damping allows return before lock, the product closure explains why simply increasing `R` cannot continue helping indefinitely.

---

## 6. Active reset implication

If a high-`R` write environment proves favorable, the long passive `tau_phi` need not become the detector dead time if a separate controlled reset/environment is switched in after readout.

That would move the architecture from

```text
one fixed passive environment for write + retention + reset
```

to

```text
low-noise weakly dissipative write environment
+
persistent flux latch
+
separate active reset/rethermalization channel.
```

Such a time-dependent environment must be modeled causally and include the fluctuations introduced during switching/reset, but it is not ruled out by the fixed-passive tradeoff above.

---

## Status

**Derived weak-damping filter-family closure.**

No novelty claim. No physical efficiency claim.

**GO for continued theory. NO-GO for manuscript.**
