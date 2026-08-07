# Mode-Matched Passive Receiver Phase Diagram

**Timestamp:** 2026-08-07 16:12 EDT  
**Status:** Active derivation for Experiment 01

This note combines the passive quadrupole oscillator-strength ceiling with the explicit source–receiver graviton mode overlap.

---

## 1. Two independent receiver resources

The receiver has a total gravitational radiative linewidth

$$
\kappa_g
$$

and a normalized overlap with the source branch-difference mode

$$
\mathcal O_{SB}\in[0,1].
$$

The useful source-mode rate is

$$
\boxed{
\kappa_\Delta
=\mathcal O_{SB}\kappa_g.
}
$$

Thus two conceptually distinct quantities matter:

1. **oscillator strength** — how strongly the receiver couples to gravity in total;
2. **mode match** — what fraction of that coupling points into the source's actual causal branch-difference mode.

---

## 2. Passive total-rate ceiling

For a passive stationary nonrelativistic receiver,

$$
\frac{\kappa_g}{\kappa_i}
\lesssim
\mathfrak R_B,
$$

with

$$
\boxed{
\mathfrak R_B
=\frac23Q_B\mathcal C_B\beta_B^3,
}
$$

$$
\mathcal C_B=\frac{r_{s,B}}{L_B},
\qquad
\beta_B=\frac{\omega_BL_B}{c}.
$$

Therefore the useful-mode coupling obeys

$$
\boxed{
\frac{\kappa_\Delta}{\kappa_i}
\lesssim
\mathcal O_{SB}\mathfrak R_B.
}
$$

This is the mode-matched passive receiver ceiling.

---

## 3. Necessary condition for a thermal NPT front

Weak-cat source-receiver entanglement requires

$$
\kappa_\Delta>\bar n_i\kappa_i.
$$

Hence any passive receiver in the assumed class must satisfy the necessary condition

$$
\boxed{
\mathcal O_{SB}\mathfrak R_B>\bar n_i.
}
$$

Equivalently, for a receiver with given total passive capability $\mathfrak R_B$,

$$
\boxed{
\mathcal O_{SB}>
\frac{\bar n_i}{\mathfrak R_B}.
}
$$

If

$$
\mathfrak R_B\le\bar n_i,
$$

no amount of mode matching can help.

If

$$
\mathfrak R_B>\bar n_i,
$$

mode engineering can decide whether the receiver actually crosses the quantum threshold.

---

## 4. Necessary condition for the global history witness

The global fidelity-history witness requires

$$
\kappa_\Delta
>
\kappa_\perp+(2\bar n_i+1)\kappa_i.
$$

Since

$$
\kappa_\perp=(1-\mathcal O_{SB})\kappa_g,
$$

this becomes

$$
(2\mathcal O_{SB}-1)\kappa_g
>(2\bar n_i+1)\kappa_i.
$$

Applying the passive ceiling gives the necessary condition

$$
\boxed{
(2\mathcal O_{SB}-1)\mathfrak R_B
>2\bar n_i+1.
}
$$

Thus

$$
\boxed{
\mathcal O_{SB}
>
\frac12
\left[
1+
\frac{2\bar n_i+1}{\mathfrak R_B}
\right].
}
$$

The right-hand side is always greater than $1/2$.

Therefore a passive receiver cannot enter the simple global-history regime unless **more than half of the entire branch-difference gravitational mode is coherently accessible**, even in the limit of very large total gravitational oscillator strength.

---

## 5. Geometric consequences

For the plus quadrupole, one ideal hemisphere contains exactly

$$
\mathcal O_{\rm aperture}=1/2
$$

of the total angular mode.

Therefore a receiver restricted to one hemisphere can at best reach the boundary of the vacuum global-history witness. Any internal loss, thermal noise, orientation mismatch, or temporal mismatch pushes it below threshold.

By contrast, the weak-cat NPT condition can be satisfied with less than half-mode access provided

$$
\mathcal O_{SB}\mathfrak R_B>\bar n_i.
$$

At zero temperature, arbitrarily small nonzero useful-mode overlap can in principle transfer an arbitrarily small amount of entanglement.

---

## 6. Orientation penalty

For two otherwise identical plus quadrupoles rotated by $\psi$ around their common axis,

$$
\mathcal O_Q=\cos^22\psi.
$$

If aperture and temporal matching are ideal, the passive NPT condition becomes

$$
\boxed{
\cos^22\psi\,\mathfrak R_B>\bar n_i.
}
$$

The allowed orientation range is therefore

$$
|\cos2\psi|>
\sqrt{\frac{\bar n_i}{\mathfrak R_B}}.
$$

Near the quadrupole-orthogonal orientation

$$
\psi=\pi/4,
$$

the causal source-receiver quantum channel closes continuously.

This provides a clean null/control geometry.

---

## 7. Random orientation benchmark

For a uniformly random relative orientation,

$$
\langle\mathcal O_Q\rangle=1/5.
$$

Thus an unaligned receiver loses, on average, a factor of five in the useful gravitational rate even with complete angular and temporal access.

More importantly,

$$
1/5<1/2,
$$

so random orientation cannot support the simple vacuum global-history witness in the high-oscillator-strength limit unless additional spatial-mode engineering compensates the tensor mismatch.

This makes deliberate spin-2 alignment essential for low-cost certification.

---

## 8. Temporal mismatch penalty

For normalized Lorentzian/exponential source and receiver radiative modes,

$$
\mathcal O_t
=
\frac{4\kappa_S\kappa_B}
{(\kappa_S+\kappa_B)^2+4\Delta^2}.
$$

With otherwise perfect matching,

$$
\mathcal O_{SB}=\mathcal O_t.
$$

The weak-cat thermal condition becomes

$$
\boxed{
\frac{4\kappa_S\kappa_B}
{(\kappa_S+\kappa_B)^2+4\Delta^2}
\,\mathfrak R_B
>\bar n_i.
}
$$

Thus linewidth mismatch and detuning enter identically to orientation/aperture loss: they reduce the useful source-mode rate rather than the total receiver gravitational linewidth.

---

## 9. Phase diagram in $(\mathfrak R_B,\mathcal O_{SB})$

For fixed thermal occupation $\bar n_i$, define three regions.

### Region I — NPT excluded by passive ceiling

$$
\boxed{
\mathcal O_{SB}\mathfrak R_B\le\bar n_i.
}
$$

### Region II — NPT not excluded, global witness excluded

$$
\boxed{
\mathcal O_{SB}\mathfrak R_B>\bar n_i
}
$$

but

$$
\boxed{
(2\mathcal O_{SB}-1)\mathfrak R_B
\le2\bar n_i+1.
}
$$

### Region III — global history witness not excluded

$$
\boxed{
(2\mathcal O_{SB}-1)\mathfrak R_B
>2\bar n_i+1.
}
$$

This is a two-resource receiver phase diagram: **oscillator strength horizontally, mode selectivity vertically**.

---

## 10. Which resource is more valuable?

If

$$
\mathfrak R_B\ll\bar n_i,
$$

improving mode overlap cannot rescue the receiver because $\mathcal O_{SB}\le1$. One must first increase the gravitational oscillator-strength/noise ratio.

If

$$
\mathfrak R_B\gg\bar n_i,
$$

then mode matching becomes the dominant bottleneck. In that regime increasing total coupling further gives diminishing returns unless the receiver also points that coupling into the desired branch-difference mode.

Thus the optimal engineering sequence is

1. reach adequate total gravitational cooperativity;
2. then maximize source-mode overlap.

---

## 11. Active collective interpretation

An active collective state may enhance total gravitational rates by a large factor $A$,

$$
\mathfrak R_B\to A\mathfrak R_B,
$$

while subwavelength collectivity leaves $\mathcal O_{SB}$ essentially unchanged.

Therefore active enhancement moves the receiver horizontally across this phase diagram, not vertically.

A phased array or enclosing geometry changes $\mathcal O_{SB}$ and therefore moves it vertically.

This cleanly separates

$$
\boxed{\text{collective rate engineering}}
$$

from

$$
\boxed{\text{gravitational mode engineering}}.
$$

Both may be required.

---

## 12. Current conceptual statement

> **A good gravitational quantum receiver needs two things that ordinary sensitivity discussions mix together: enough quadrupole oscillator strength to interact with gravity at all, and enough spin-2 mode overlap to make that interaction belong to the source's actual branch-difference wave. The first controls how fast the receiver can exchange gravitons; the second controls whether those gravitons carry the quantum information we care about. Increasing one cannot compensate indefinitely for absence of the other.**

---

## 13. Immediate next step

Construct the relativistic analogue of this two-resource diagram using a smeared stress-energy spectral density rather than the nonrelativistic quadrupole sum-rule ceiling.