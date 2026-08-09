# Independent Check of the TT Wave-Zone Coefficient

## Purpose

`TT_PROPAGATION_BOUND.md` derives the compact quadrupole propagation ceiling using the general STF TT projector and stationary phase. This note checks the numerical coefficient `5/4` independently in the **maximizing aligned plus channel**, reducing the full angular overlap to an elementary one-dimensional integral.

The result reproduces both the leading wave-zone amplitude and the full outgoing polynomial used in frozen V7.

---

## 1. Maximizing plus tensor

Take propagation along `z` and

```math
Q=\operatorname{diag}(1,-1,0),
\qquad
Q:Q=2.
```

Use the standard transverse basis

```math
\mathbf e_\theta
=(\cos\theta\cos\phi,
  \cos\theta\sin\phi,
 -\sin\theta),
```

```math
\mathbf e_\phi
=(-\sin\phi,\cos\phi,0)
```

and unit-normalized polarization tensors

```math
\epsilon_+
=\frac{\mathbf e_\theta\mathbf e_\theta
      -\mathbf e_\phi\mathbf e_\phi}{\sqrt2},
```

```math
\epsilon_\times
=\frac{\mathbf e_\theta\mathbf e_\phi
      +\mathbf e_\phi\mathbf e_\theta}{\sqrt2}.
```

Direct contraction gives

```math
Q:\epsilon_+
=\frac{1+\cos^2\theta}{\sqrt2}\cos2\phi,
```

```math
Q:\epsilon_\times
=-\sqrt2\cos\theta\sin2\phi.
```

Therefore

```math
\sum_\lambda|Q:\epsilon_\lambda|^2
=
\frac12(1+x^2)^2\cos^22\phi
+2x^2\sin^22\phi,
\qquad x=\cos\theta.
```

---

## 2. Normalized angular overlap

For the normalized one-graviton angular mode

```math
u_{Q,\lambda}(\hat n)
=\sqrt{\frac{5}{8\pi}}
\frac{Q:\epsilon_\lambda}{\sqrt{Q:Q}},
```

the azimuthally integrated probability density is

```math
\sum_\lambda\int_0^{2\pi}
d\phi\,|u_{Q,\lambda}|^2
=
\boxed{
\frac{5}{32}(1+6x^2+x^4).
}
```

Normalization is immediate:

```math
\frac5{32}
\int_{-1}^{1}(1+6x^2+x^4)dx
=1.
```

For a translation by `R z-hat`, `z=kR`, the exact fixed-frequency mode overlap is therefore

```math
\boxed{
S(z)
=
\frac5{32}
\int_{-1}^{1}
(1+6x^2+x^4)e^{izx}dx.
}
```

No antenna or retarded-field formula has been used.

---

## 3. Leading endpoint asymptotics

Let

```math
f(x)=\frac5{32}(1+6x^2+x^4).
```

Since

```math
f(1)=f(-1)=\frac54,
```

one integration by parts gives

```math
S(z)
=
\left.
\frac{f(x)e^{izx}}{iz}
\right|_{-1}^{1}
+O(z^{-2}).
```

Thus

```math
S(z)
=
\frac54
\frac{e^{iz}-e^{-iz}}{iz}
+O(z^{-2})
=
\frac{5}{2z}\sin z
+O(z^{-2}).
```

The two endpoint contributions are the outgoing and time-reversed stationary directions. The `+z` outgoing piece is

```math
\boxed{
S_+(z)
=-\frac{5i}{4z}e^{iz}
+O(z^{-2}).
}
```

Therefore

```math
\boxed{
|S_+(z)|^2
=\frac{25}{16z^2}
+O(z^{-3}).
}
```

This independently confirms the compact-quadrupole maximum amplitude coefficient

```math
\frac{5}{4kR}
```

and transfer coefficient

```math
\frac{25}{16(kR)^2}.
```

---

## 4. Exact polynomial integral

Because the angular weight is only a fourth-order polynomial, the integral can be evaluated exactly. Splitting the result into `e^{+iz}` and `e^{-iz}` pieces gives

```math
S(z)=S_+(z)+S_-(z),
```

with

```math
\boxed{
S_+(z)
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5},
}
```

```math
P(z)
=3-3iz-3z^2+2iz^3+z^4.
```

For real `z`, `S_-(z)=S_+^*(z)`.

Thus

```math
\boxed{
|S_+(z)|^2
=
\frac{25}{16z^2}
\left(
1-\frac2{z^2}
+\frac3{z^4}
-\frac9{z^6}
+\frac9{z^8}
\right).
}
```

This is exactly the frozen V7 outgoing TT radial polynomial, obtained here from a direct normalized angular integral rather than from V7's retarded-source or reciprocal-receiver routes.

---

## 5. What this check establishes

The `5/4` wave-zone amplitude coefficient is fixed independently by:

1. normalized STF one-graviton angular modes;
2. the explicit maximizing plus tensor;
3. elementary azimuthal integration;
4. endpoint asymptotics of a one-dimensional Fourier integral.

The exact same calculation reproduces the complete finite-`z` outgoing polynomial.

This sharply lowers the risk that the Experiment 02 TT coefficient was inherited circularly from the V7 antenna normalization.

---

## 6. Remaining geometry scope

This check says nothing beyond the declared compact `l=2` quadrupole channel. It does not constrain extended phased apertures, higher multipoles, relativistic beaming, near-field exchange, or curved-background propagation.
