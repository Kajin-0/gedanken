# Experiment 03 — Thermal Similarity and Dwell Saturation — 2026-08-15

## Purpose

The dynamical capture-lobe scan showed that the detector response is non-monotonic in wavelength at fixed thermal area. Two exact properties of the retained clean graphene thermal model sharpen the interpretation:

1. the thermal trajectory depends on photon wavelength and active area through the product `A lambda`;
2. the cooling-side fold-reformation time has a finite high-energy limit.

These are exact statements **inside the retained lumped thermal model**. They are not material-independent detector theorems.

---

## 1. Thermal similarity variable

The retained graphene model uses

```math
C_e=\gamma A T
```

and

```math
P_{e-ph}=\Sigma A(T^4-T_0^4).
```

Define

```math
u=T^2.
```

Then

```math
\frac{du}{dt}
=S_u(t)
-\frac{u^2-u_0^2}{2\tau_0u_0},
```

with `u_0=T_0^2` and the current calibrated `tau_0`.

For one absorbed photon,

```math
E_\gamma=hc/\lambda.
```

Because the electronic heat capacity is proportional to area,

```math
\Delta u
\propto
\frac{E_\gamma}{A}
\propto
\frac{1}{A\lambda}.
```

The retained exponential deposition source is

```math
S_u(t)
=\frac{\Delta u}{\tau_r}e^{-t/\tau_r}.
```

Therefore, at fixed `tau_r`, `tau_0`, absorptance and circuit model,

```math
\boxed{
T(t;A,\lambda)
=T(t;A',\lambda')
\quad\text{whenever}\quad
A\lambda=A'\lambda'.
}
```

The natural calorimetric control variable is

```math
\boxed{\Xi=A\lambda}
```

or equivalently absorbed energy density `E_gamma/A`.

---

## 2. Consequence for the full phase trajectory

In the current reduced detector model, the Josephson force depends on wavelength/area only through the temperature history:

```math
F=F[x,T(t)].
```

If the circuit parameters `L,C,Y(omega)` and initial state are held fixed, identical `T(t)` implies identical deterministic phase dynamics.

Hence, **inside this model**, every deterministic capture lobe and tangent-map result obeys the similarity

```math
\boxed{
\mathcal R(A,\lambda)
=\mathcal R(A',\lambda')
\quad\text{for}\quad
A\lambda=A'\lambda',
}
```

where `mathcal R` can denote the phase trajectory, reformation point, tangent map, or deterministic basin classification.

This does not yet prove the same scaling for physical detector efficiency because changing area can alter optical absorptance, spatial heat flow, Josephson geometry, circuit capacitance, and other quantities omitted from the reduced model.

---

## 3. Immediate LWIR implication

The favorable phase-only tangent points found at `A=100 um^2` can be translated to the same thermal trajectory at `14 um` by reducing thermal active area:

```text
8 um at 100 um^2
 -> 14 um at A = 100*(8/14) ~57.1 um^2.

9 um at 100 um^2
 -> 14 um at A ~64.3 um^2.

10 um at 100 um^2
 -> 14 um at A ~71.4 um^2.

11 um at 100 um^2
 -> 14 um at A ~78.6 um^2.
```

Thus the short-wavelength tangent improvement is **not automatically a loss of LWIR reach**. It can represent a smaller thermally active volume at the same LWIR photon energy.

This is especially relevant because earlier spatial-rise analysis already favored localizing absorbed energy near the Josephson-sensitive region.

However, the scaling is only useful if optical collection can be decoupled from thermally active/Josephson area, e.g. by antenna/cavity concentration or another geometry that preserves the circuit while reducing the electronic heat capacity seen by one photon.

---

## 4. Exact cooling time after instantaneous deposition

After the deposition source has ended, the clean model is

```math
\dot u
=-\frac{u^2-u_0^2}{2\tau_0u_0}.
```

Cooling from `u_h` to a lower target `u_f` gives

```math
\boxed{
 t(u_h\to u_f)
=\tau_0
\ln\!\left[
\frac{(u_h-u_0)(u_f+u_0)}
{(u_h+u_0)(u_f-u_0)}
\right].
}
```

For fold reformation take

```math
u_f=T_f^2.
```

The cooling time grows with initial energy but has the finite limit

```math
\boxed{
 t_{f,\infty}
=\tau_0
\ln\!\left(
\frac{u_f+u_0}{u_f-u_0}
\right).
}
```

For the current `rDelta=.6` scales

```text
T0 = 0.020 K
Tf ~0.694428 K
tau0 = 75 ns
```

this gives

```math
\boxed{t_{f,\infty}\approx124.4\;ps.}
```

The finite-20-ps-rise numerical scan approaches this scale from below:

```text
8 um  -> reformation ~107.2 ps
9     -> ~100.1 ps
10    -> ~92.8 ps
11    -> ~85.3 ps
12    -> ~77.3 ps
13    -> ~68.6 ps
14    -> ~57.7 ps.
```

---

## 5. Physical interpretation of capture lobes

The underdamped phase/filter system accumulates dynamical phase while the left well is absent or strongly softened.

Increasing deposited energy therefore changes

```text
quench depth
+
hot-state dwell time.
```

But the dwell time cannot diverge: it approaches `~124 ps` in the clean cooling model.

Therefore the energy-dependent capture lobes are confined to a finite dynamical window. In a rough sense the maximum number of coherent phase-space rotations is limited by the ratio

```math
N_{rot}\sim t_{f,\infty}/T_{phase},
```

although the instantaneous phase frequency is strongly time dependent and this ratio is only an orientation scale, not a quantitative lobe-count theorem.

This is preferable to the earlier intuition that arbitrarily high energy could generate arbitrarily many capture/retrapping bands.

---

## 6. Design implication

The detector should be optimized in the control space

```text
absorbed energy density E_gamma/A
x deposition rise time
x causal environment Y(omega)
```

rather than wavelength alone.

A useful experimental-style spectral specification would ultimately require restoring the map

```text
wavelength
 -> absorptance
 -> deposited energy density
 -> thermal trajectory
 -> open-system capture probability.
```

Until then, the current lobe locations should be called **thermal-energy-density lobes**, not intrinsic wavelength resonances.

---

## 7. Strongest conclusion

Inside the retained thermal model,

```math
\boxed{A\lambda=\mathrm{const}}
```

is an exact trajectory-similarity line, while the hot dwell to fold reformation has a finite high-energy ceiling.

This gives a concrete route to move a favorable short-wavelength lobe into the 14-um band by shrinking the thermally active area, without changing the photon wavelength itself.

Whether that route survives realistic spatial heat flow, absorptance, junction geometry and the full stationary open-system FDT calculation is now the decisive question.

**GO for continued theory. NO-GO for manuscript.**
