# Experiment 03 — Causal Filter Noise–Memory Closure — 2026-08-15

## Purpose

The passive two-pole environment introduced in `CAUSAL_FDT_ENVIRONMENT_CHECKPOINT_2026-08-15.md` allows its spectral cutoff, time-domain memory and integrated zero-point force scale to be eliminated exactly against one another.

This is a derived closure for this particular realizable quartic-rolloff network family. It is **not** asserted as a universal theorem for arbitrary passive admittances.

---

## 1. Admittance in normalized form

The network

```text
port -- L_f --+-- R -- ground
              |
              C_f
              |
            ground
```

has

```math
Z(s)=sL_f+\frac{R}{1+sRC_f}.
```

Choose

```math
L_f=\frac{\sqrt2R}{\omega_D},
\qquad
C_f=\frac{1}{\sqrt2R\omega_D}.
```

Then

```math
\boxed{
Y(s)
=\frac1R
\frac{1+s/(\sqrt2\omega_D)}
{1+\sqrt2s/\omega_D+(s/\omega_D)^2}.
}
```

The dissipative spectrum is

```math
\boxed{
\operatorname{Re}Y(\omega)
=\frac{1/R}{1+(\omega/\omega_D)^4}.
}
```

---

## 2. Exact causal memory time

The poles are

```math
s_{\pm}
=-\frac{\omega_D}{\sqrt2}
\pm i\frac{\omega_D}{\sqrt2}.
```

Therefore the causal impulse kernel has the form

```math
\boxed{
y(t)
=\frac{\omega_D}{\sqrt2R}
 e^{-\omega_D t/\sqrt2}
\left[
\cos\!\left(\frac{\omega_Dt}{\sqrt2}\right)
+\sin\!\left(\frac{\omega_Dt}{\sqrt2}\right)
\right]H(t).
}
```

Its envelope memory time is

```math
\boxed{
\tau_D=\frac{\sqrt2}{\omega_D}.
}
```

Eliminating `omega_D`, the physical filter components become especially simple:

```math
\boxed{
L_f=R\tau_D,
\qquad
C_f=\frac{\tau_D}{2R}.
}
```

Thus lowering the dissipative cutoff necessarily lengthens the causal memory of this filter family.

---

## 3. Integrated zero-point force scale

At `T -> 0`, the symmetrized current-noise variance is

```math
\langle I_N^2\rangle
=\frac{1}{\pi}
\int_0^\infty
\hbar\omega\operatorname{Re}Y(\omega)d\omega.
```

For the quartic rolloff,

```math
\langle I_N^2\rangle
=\frac{\hbar\omega_D^2}{4R}.
```

Using `omega_D=sqrt(2)/tau_D` gives

```math
\boxed{
\sigma_I^2
=\frac{\hbar}{2R\tau_D^2}.
}
```

Therefore

```math
\boxed{
\sigma_I\tau_D
=\sqrt{\frac{\hbar}{2R}}.
}
```

This is the central noise–memory product for this environment family.

Reducing the integrated zero-point force by lowering `omega_D` does not come for free: the bath memory grows inversely.

---

## 4. Detector-normalized form

Define

```math
n=\frac{LI_N}{\bar\Phi},
\qquad
\bar\Phi=\Phi_0/(2\pi).
```

The cold harmonic phase width is `sigma_x`, the cold curvature is `kappa_c`, and

```math
\omega_c=\sqrt{\frac{\kappa_c}{LC}}.
```

For the quartic filter define

```math
\alpha=\omega_D/\omega_c,
\qquad
g=\frac{1}{RC\omega_c}.
```

Earlier reduction gives

```math
\frac{\sigma_n}{\kappa_c\sigma_x}
=\alpha\sqrt{\frac{g}{2}}
```

at `T -> 0` in the isolated-harmonic normalization.

Since

```math
\omega_c\tau_D=\frac{\sqrt2}{\alpha},
```

we obtain exactly

```math
\boxed{
\left(
\frac{\sigma_n}{\kappa_c\sigma_x}
\right)
(\omega_c\tau_D)
=\sqrt g.
}
```

Thus at fixed `R,C,omega_c`, the normalized bath-force scale and normalized bath memory cannot both be reduced by tuning the cutoff.

---

## 5. Finite-time implication

Suppose the detector requires the dissipative environment to respond on a timescale no slower than `t_cap`, so a necessary engineering condition is roughly

```math
\tau_D\lesssim t_{cap}.
```

Then the exact product implies the family-specific lower bound

```math
\boxed{
\sigma_I
\gtrsim
\frac{1}{t_{cap}}
\sqrt{\frac{\hbar}{2R}}.
}
```

or in the detector-normalized variables

```math
\boxed{
\frac{\sigma_n}{\kappa_c\sigma_x}
\gtrsim
\frac{\sqrt g}{\omega_ct_{cap}}.
}
```

This does **not** yet prove a detector-fidelity floor, because:

- `t_cap` must be defined from the nonlinear basin/retrapping dynamics;
- the relevant transient curvature can be much smaller than `kappa_c`;
- symmetrized zero-point fluctuations cannot be treated as ordinary classical activation;
- other passive admittance families may realize different numerical tradeoffs.

It does, however, demonstrate concretely that the strategy

```text
lower cutoff -> arbitrarily low quantum force with unchanged rapid retrapping
```

is impossible within this realizable filter family.

---

## 6. Current numerical scale

For the retained `rDelta=.6`, `C~215 fF`, `omega_c/2pi~27.25 GHz` case and `R=250 ohm`,

```text
g ~0.109
sqrt(g) ~0.33.
```

At

```text
alpha=.35:
  tau_D ~23.6 ps
  sigma_n/(kappa_c sigma_x) ~0.082.
```

At

```text
alpha=.20:
  tau_D ~41 ps
  sigma_n/(kappa_c sigma_x) ~0.047.
```

The lower-cutoff environment therefore reduces the integrated cold force scale, but its memory becomes comparable to or longer than the current `20 ps` photon-energy rise and the relevant nonadiabatic capture times.

This is precisely the regime where a finite-time capture/noise optimization, rather than a static cutoff optimization, is required.

---

## Next step

Map capture/retrapping time against `tau_D` and determine the minimum causal bandwidth that still produces a robust target basin. Combining that nonlinear timing requirement with the exact noise–memory product is the most direct route toward a genuine environment-imposed lower bound.

**Status: GO for continued theory; no novelty claim; NO-GO for manuscript.**
