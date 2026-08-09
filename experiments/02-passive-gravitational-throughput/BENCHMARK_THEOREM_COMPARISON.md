# Benchmark Comparison — Explicit V7 Mode vs Experiment 02 Ceiling

## 1. Purpose

The Experiment 02 theorem is useful only if its material and propagation ceilings are not arbitrarily loose compared with an explicit conserved source. The frozen V7 four-spoke plus mode provides a concrete check.

This note compares the long-wavelength V7 mode to the new material EWSR and TT geometry bounds. It does **not** claim global saturation of the full throughput theorem.

---

## 2. V7 long-wavelength mode

The explicit source has four endpoint masses `mu` at radius `L`. In the long-wavelength spoke limit,

```math
q\to0,
```

the spoke mass vanishes relative to the endpoints at leading order and

```math
M_{\rm eff}\to4\mu.
```

The explicit plus-mode spontaneous gravitational linewidth tends to

```math
\boxed{
\kappa_g^{\rm V7}
\to
\frac{8G\mu L^2\omega^4}{5c^5}.
}
```

The internal endpoint inertia moment about the hub/center of mass is

```math
\boxed{
I_{\rm end}=4\mu L^2.
}
```

Spoke and compact hub corrections can be included at finite `q`, but they do not change the leading comparison below.

---

## 3. Material EWSR ceiling

The Experiment 02 material theorem gives

```math
\kappa_{g,\Sigma}
\le
\frac{4G}{3c^5}I\omega^4.
```

Using the endpoint-dominated inertia,

```math
\boxed{
\kappa_{g,\rm EWSR}^{\max}
=
\frac{16G\mu L^2\omega^4}{3c^5}.
}
```

Therefore

```math
\boxed{
\frac{\kappa_{g,\rm EWSR}^{\max}}
{\kappa_g^{\rm V7}}
=
\frac{10}{3}
\simeq3.333.
}
```

So the explicit conserved V7 mode carries about

```math
\boxed{
\frac{3}{10}=30\%
}
```

of the endpoint-only EWSR gravitational linewidth ceiling at leading long-wavelength order.

This is a useful scale check: the EWSR bound is not separated from the explicit mechanical mode by many orders of magnitude.

---

## 4. Geometry comparison

The V7 plus quadrupole has

```math
Q\propto\operatorname{diag}(1,-1,0).
```

Along the `z` axis this tensor lies entirely in the TT subspace, so

```math
D=\frac52.
```

It therefore saturates the compact quadrupole directivity ceiling derived in `TT_PROPAGATION_BOUND.md`.

For a matched reciprocal receiver, the leading wave-zone normalized propagation factor is

```math
\boxed{
\eta_{\rm prop}
=\frac{25}{16(kR)^2},
}
```

which is also the maximal compact-quadrupole singular-channel coefficient at the retained order.

Thus the explicit V7 source is **geometry-optimal inside the compact quadrupole class** even though its material oscillator strength does not saturate the EWSR.

---

## 5. Full throughput sharpness is a different question

For one symmetric source and receiver pole with identical intrinsic gravitational linewidth `kappa_g`, the exact passive two-port spectral-area optimum is

```math
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
```

If the V7 mode is used at both endpoints, then relative to the fully combined material-plus-geometry theorem ceiling,

```math
\Gamma_{\rm theorem}
=\eta_{\rm prop}\kappa_{g,\rm EWSR}^{\max},
```

the symmetric two-port optimum is

```math
\frac{\Gamma_{\rm EBP}^{\rm sym,max}}
{\Gamma_{\rm theorem}}
=
\frac8{27}\frac{3}{10}
=
\boxed{\frac4{45}}
\simeq0.0889.
```

Equivalently, the combined theorem ceiling is about

```math
\boxed{11.25}
```

times the symmetric two-port optimum for this explicit long-wavelength mode.

This distinction matters:

- the **material linewidth bound** is only `10/3` above the V7 mode;
- the **geometry bound** is saturated by the V7 plus tensor;
- the **full integrated throughput bound** includes additional passive matching/cut-set looseness and is not yet shown globally sharp.

Do not describe the final theorem coefficient as saturable without a separate constructive optimization.

---

## 6. Why this comparison is encouraging

The explicit V7 construction already demonstrates three useful properties:

1. a fully conserved compact mechanical source exists in the required regime;
2. its quadrupole tensor saturates the compact TT geometry ceiling;
3. its intrinsic gravitational linewidth reaches the correct EWSR scaling and lies within an order-unity factor of the material ceiling.

Therefore the Experiment 02 theorem is not merely a dimensional upper bound detached from known source physics.

At the same time, the `4/45` full-throughput comparison prevents overclaiming sharpness.

---

## 7. Benchmark rate scale

Using the frozen V7 numerical values

```math
\kappa_g\simeq6.87\times10^{-26}\;\mathrm{s}^{-1},
```

```math
\eta_{\rm prop}=0.015625,
```

the simple interface cut-set scale is

```math
\eta_{\rm prop}\kappa_g
\simeq1.0734\times10^{-27}\;\mathrm{s}^{-1}.
```

The symmetric two-port EBP optimum for that explicit mode would be

```math
\boxed{
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac8{27}\eta_{\rm prop}\kappa_g
\simeq3.18\times10^{-28}\;\mathrm{s}^{-1}.
}
```

Its inverse is approximately

```math
\boxed{
1.0\times10^{20}\;\mathrm{yr}.
}
```

This remains an inverse spectral coherent-transfer scale, not a literal “time per qubit.”

---

## 8. Current conclusion

The explicit V7 source is close enough to the material ceiling to make the general bound physically informative, and it exactly saturates the compact quadrupole geometry ceiling. The remaining factor between the explicit symmetric transducer and the final theorem is primarily the difference between an upper cut-set resource bound and a simultaneously optimized end-to-end passive device.

That simultaneous-saturability problem is useful future work but is not required for validity of the theorem.
