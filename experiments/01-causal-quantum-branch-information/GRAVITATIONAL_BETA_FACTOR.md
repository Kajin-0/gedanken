# Gravitational Beta Factor: Total Collective Rate vs Useful Quantum Mode

**Timestamp:** 2026-08-07 16:09 EDT  
**Status:** Active derivation for Experiment 01

This note makes the active-collective receiver problem mode-selective. The quantity that matters for causal branch-information transfer is not merely the total gravitational transition rate but the fraction of that coupling accessible to the intended incoming/outgoing branch-difference mode.

---

## 1. Define a gravitational beta factor

Decompose the receiver's total gravitational radiative coupling into

$$
\kappa_g
=\kappa_\Delta+\kappa_\perp,
$$

where

- $\kappa_\Delta$ couples to the selected source branch-difference mode that the receiver can coherently access;
- $\kappa_\perp$ couples to gravitational modes that remain inaccessible/unobserved in the protocol.

Including nongravitational internal loss $\kappa_i$, define

$$
\boxed{
\beta_G
=\frac{\kappa_\Delta}
{\kappa_\Delta+\kappa_\perp+\kappa_i}.
}
$$

For an ideal time-reversal-matched receiver with no internal loss and complete access to the full emitted mode,

$$
\beta_G\to1.
$$

For restricted angular coverage or imperfect polarization/spatial mode matching,

$$
\beta_G<1.
$$

---

## 2. Free-space quadrupole radiation pattern

Take the same plus-type STF quadrupole used throughout Experiment 01,

$$
Q_{ij}
=q\,\operatorname{diag}(1,-1,0).
$$

For radiation direction

$$
\mathbf n
=(\sin\theta\cos\phi,
\sin\theta\sin\phi,
\cos\theta),
$$

the two polarization amplitudes are proportional to

$$
\boxed{
A_+
=q(1+\cos^2\theta)\cos2\phi,
}
$$

$$
\boxed{
A_\times
=-2q\cos\theta\sin2\phi.
}
$$

Thus the angular power weight is proportional to

$$
\boxed{
W(\theta,\phi)
=(1+\cos^2\theta)^2\cos^22\phi
+4\cos^2\theta\sin^22\phi.
}
$$

Integrating over azimuth,

$$
\boxed{
\int_0^{2\pi}d\phi\,W
=\pi(\cos^4\theta+6\cos^2\theta+1).
}
$$

The full-sphere normalization is

$$
\boxed{
\int d\Omega\,W
=\frac{32\pi}{5}.
}
$$

---

## 3. Ideal polar-cap capture fraction

Suppose an ideal mode-matched receiver has complete polarization and phase control over a polar cap

$$
0\le\theta\le\theta_0
$$

around the $+z$ direction.

Let

$$
u_0=\cos\theta_0.
$$

The maximum angular fraction of the quadrupolar difference mode accessible through that one cap is

$$
\boxed{
\beta_{\rm cap}(\theta_0)
=\frac12
-\frac{u_0^5+10u_0^3+5u_0}{32}.
}
$$

For small aperture angle,

$$
\boxed{
\beta_{\rm cap}
=\frac58\theta_0^2
-\frac{35}{96}\theta_0^4
+O(\theta_0^6).
}
$$

A single hemisphere captures

$$
\boxed{\beta_{\rm cap}(\pi/2)=1/2.}
$$

Two symmetric caps of half-angle $\theta_0$ capture

$$
\boxed{
\beta_{2\rm cap}
=1-
\frac{u_0^5+10u_0^3+5u_0}{16}.
}
$$

For $\theta_0=\pi/2$, the two hemispheres cover the full radiation mode and

$$
\beta_{2\rm cap}=1.
$$

---

## 4. Interpretation of the ideal enclosing receiver

A localized quadrupole transition emits one normalized one-graviton wavepacket: a coherent superposition of directions and polarizations with the angular pattern above and a definite temporal envelope.

If a receiver controls the **complete time-reversed spatial, polarization, and temporal mode**, unit capture is possible in the ideal lossless Gedanken limit.

Thus weak gravitational coupling does not impose an intrinsic free-space branching-ratio ceiling. It imposes an enormous interaction time.

The beta factor becomes less than unity when the experiment gives up access to part of the outgoing mode—for example through limited angular coverage, polarization mismatch, or internal loss.

---

## 5. What $N^2$ collective enhancement does to $\beta_G$

For a subwavelength correlated ensemble, all constituents radiate with essentially the same phase over the gravitational wavelength. The collective matrix element can scale as

$$
Q_{\rm coll}\sim NQ_1
$$

for favorable active states, so the total transition rate can scale as

$$
\kappa_g^{\rm coll}\sim N^2\kappa_{g,1}.
$$

But the normalized angular radiation pattern remains the same.

Therefore, for fixed receiver aperture/mode access,

$$
\boxed{
\kappa_\Delta\to N^2\kappa_\Delta,
\qquad
\kappa_\perp\to N^2\kappa_\perp,
}
$$

so the **purely gravitational branching fraction**

$$
\frac{\kappa_\Delta}{\kappa_\Delta+\kappa_\perp}
$$

is unchanged.

Thus

$$
\boxed{
N^2\text{ enhancement speeds the interaction but does not by itself improve mode selectivity.}
}
$$

---

## 6. Collective enhancement can still beat nongravitational loss

Including an internal loss rate $\kappa_i$ that does not receive the same collective enhancement,

$$
\beta_G(N)
=
\frac{N^2\kappa_\Delta^{(1)}}
{N^2[\kappa_\Delta^{(1)}+\kappa_\perp^{(1)}]+\kappa_i}.
$$

As $N\to\infty$,

$$
\boxed{
\beta_G(N)
\to
\beta_{\rm geom}
=\frac{\kappa_\Delta^{(1)}}
{\kappa_\Delta^{(1)}+\kappa_\perp^{(1)}}.
}
$$

So active collective enhancement can overcome ordinary material loss and reduce the gravitational capture time, but it cannot exceed the geometry/mode-access ceiling.

This gives a precise role for the known $N^2$ effect.

---

## 7. Strong-history threshold becomes a geometry requirement

In the vacuum pure-loss benchmark, the simple history witness requires total coherent capture fraction

$$
\eta>1/2.
$$

If collective enhancement makes internal loss negligible, then asymptotically

$$
\eta\to\beta_{\rm geom}.
$$

Therefore the simple global witness requires

$$
\boxed{
\beta_{\rm geom}>1/2.
}
$$

For the plus quadrupole, one ideal hemisphere gives exactly the limiting value

$$
\beta_{\rm geom}=1/2,
$$

while access to more than a hemisphere of the properly mode-matched radiation is required for a strict strong-witness violation.

This is a Gedanken-level geometric interpretation of the earlier $50\%$ channel threshold.

Exact entanglement transfer still requires only nonzero coherent mode overlap at zero temperature; the $50\%$ condition belongs to the simple global history witness.

---

## 8. Extended phased arrays

If the collective receiver becomes comparable to a gravitational wavelength, different constituents acquire propagation phases. The radiation pattern can then become directional, analogous to a phased antenna array.

In that regime collective engineering can alter not only the total rate but also the angular mode function, potentially increasing $\beta_{\rm geom}$ for a chosen direction.

However, this is no longer the subwavelength Dicke limit. Directionality is purchased with spatial extent of order the wavelength and should obey the usual wave-optics/antenna aperture constraints.

Thus there are two logically distinct collective resources:

1. **superradiant rate enhancement** — increases total coupling;
2. **phased-array mode engineering** — changes where the coupling goes.

Only the second directly increases the gravitational beta factor at fixed total gravitational rate.

---

## 9. Source-receiver reciprocity

The ideal source branch-difference wavepacket and receiver spontaneous-emission mode should be matched by time reversal.

Let $u_S$ be the normalized source difference mode and $u_B$ the normalized receiver emission mode. The coherent mode-overlap efficiency contains

$$
\boxed{
\mathcal O_{SB}
=|\langle u_B|u_S\rangle|^2.
}
$$

The effective useful gravitational coupling is then schematically

$$
\boxed{
\kappa_\Delta
=\mathcal O_{SB}\,\kappa_g
}
$$

when all other geometric/access factors are absorbed into the mode definition.

This makes the next design problem explicit:

> **Match the receiver's time-reversed spontaneous graviton wavepacket to the source's branch-difference graviton wavepacket.**

That is the gravitational analogue of optimal single-photon absorption.

---

## 10. Current conceptual conclusion

> **Collective enhancement and quantum efficiency are different resources. An active ensemble can make the gravitational transition happen $N^2$ faster, but if it radiates into the same angular pattern, the useful and useless gravitational channels are both accelerated together. To improve actual branch-information transfer, one must engineer the gravitational mode itself—spatially, polarization-wise, and temporally—so that the enhanced coupling points into the one causal mode shared by source and receiver.**

---

## 11. Immediate next step

The next clean object is the source-receiver mode overlap

$$
\mathcal O_{SB}=|\langle u_B|u_S\rangle|^2.
$$

For the exact retarded plus-quadrupole source developed earlier, derive its normalized outgoing one-graviton mode and calculate the overlap with a candidate receiver quadrupole. Then determine how misalignment, finite aperture, and frequency mismatch enter the causal entanglement-transfer rate.