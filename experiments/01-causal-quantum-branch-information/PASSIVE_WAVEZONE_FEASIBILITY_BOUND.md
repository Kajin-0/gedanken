# Geometric-Aperture-Limited Passive Wave-Zone Feasibility Bound

**Updated:** 2026-08-07 17:25 EDT  
**Status:** Model-specific necessary condition. **Superseded as a general passive wave-zone bound:** the $\beta_B^5$ scaling applies only when coherent collection is limited by a literal physical aperture $a_R\lesssim L_B$. A resonant quantum receiver can have an effective cross-section much larger than its geometric area, so the extra $\beta_B^2$ penalty is not universal.

## 1. Critical scope correction

The earlier derivation combined

1. the passive nonrelativistic quadrupole oscillator-strength ceiling,
2. a geometric spherical-cap collection fraction,
3. the assumption
   $$
   a_R\le L_B.
   $$

That last step is stronger than a generic quantum-receiver assumption.

A resonant quantum absorber can have an effective coherent cross-section of order the wavelength squared even when its material dimensions are much smaller than the wavelength. The optical analogue is a small resonant atom whose scattering/absorption cross-section exceeds its geometric area.

Therefore the result below is valid for a **geometric screen/cap-limited receiver**, not for every passive resonant quantum receiver.

The more general passive oscillator-strength difficulty remains the earlier

$$
\boxed{
\frac{\kappa_g}{\omega_B}
\lesssim
\frac23\mathcal C_B\beta_B^3,
}
$$

with source-mode overlap treated independently.

---

## 2. Ingredients of the geometric-aperture model

For a small ideal coherent absorbing cap of radius $a_R$ at distance $R$ from the source,

$$
\beta_{\rm cap}
\simeq\frac58\frac{a_R^2}{R^2}.
$$

Let $\mathcal O$ collect tensor, temporal, and other normalized mode matching. Then

$$
\kappa_\Delta(R)
\simeq
\frac58\frac{a_R^2}{R^2}\mathcal O\kappa_g.
$$

For a stationary thermal bath,

$$
\Gamma_{\rm th}=\bar n_B\kappa_i,
\qquad
\kappa_i=\omega_B/Q_B.
$$

A wave-zone NPT region requires

$$
\kappa_\Delta(R)>\Gamma_{\rm th}
$$

for some

$$
R\gtrsim\zeta c/\omega_B.
$$

---

## 3. Passive nonrelativistic graviton-linewidth ceiling

For the passive nonrelativistic receiver class,

$$
\frac{\kappa_g}{\omega_B}
\le
\frac23\mathcal C_B\beta_B^3,
$$

where

$$
\mathcal C_B=\frac{r_{s,B}}{L_B},
\qquad
\beta_B=\frac{\omega_BL_B}{c}.
$$

Hence

$$
\frac{\kappa_g}{\Gamma_{\rm th}}
\le
\frac23
\frac{Q_B\mathcal C_B\beta_B^3}{\bar n_B}.
$$

---

## 4. Additional geometric-aperture assumption

Only now impose

$$
\boxed{a_R\le L_B.}
$$

Then requiring an NPT region at

$$
R\ge\zeta c/\omega_B
$$

gives

$$
\boxed{
\frac{5\mathcal O}{12}
\frac{Q_B\mathcal C_B\beta_B^5}{\bar n_B}
>\zeta^2.
}
$$

Define

$$
\boxed{
\mathfrak W_B^{\rm geom}
=\frac{5\mathcal O}{12}
\frac{Q_B\mathcal C_B\beta_B^5}{\bar n_B}.
}
$$

Then

$$
\mathfrak W_B^{\rm geom}>\zeta^2
$$

is a necessary condition for this **geometrically aperture-limited** receiver.

---

## 5. Origin of the extra $\beta_B^2$

The passive graviton oscillator-strength ceiling contributes

$$
\beta_B^3.
$$

The geometric assumption contributes

$$
\left(\frac{a_R\omega_B}{c}\right)^2
\lesssim\beta_B^2.
$$

Hence

$$
\beta_B^3\to\beta_B^5.
$$

This extra factor should **not** be attributed to gravitational quantum reception universally. It is the price of insisting that effective coherent collection area is bounded by the receiver's literal geometric area.

---

## 6. Resonant-receiver alternative

For a compact resonant receiver, the far-field source-to-receiver overlap is instead expected to have the generic form

$$
\boxed{
\mathcal O_{SB}(R)
\sim
\frac{C_{\rm ang}}{(kR)^2},
\qquad
k=\omega/c,
}
$$

where $C_{\rm ang}$ contains tensor/polarization/directivity factors.

This corresponds to an effective coherent cross-section of order

$$
A_{\rm eff}\sim C_{\rm ang}/k^2,
$$

which can exceed the physical material area when $kL_B\ll1$.

In this model the condition for a wave-zone NPT region is controlled by

$$
\frac{\kappa_g}{\Gamma_{\rm th}}
$$

and angular mode overlap, without the additional universal $\beta_B^2$ penalty.

This is consistent with the earlier local far-zone response calculation, whose coupling decayed as $(kR)^{-2}$ rather than $(L_B/R)^2$.

---

## 7. What remains robust

The correction does **not** remove the severe passive-matter limitation

$$
\boxed{
\frac{\kappa_g}{\kappa_i}
\lesssim
\frac23Q_B\mathcal C_B\beta_B^3.
}
$$

It only says that finite wave-zone access does not necessarily multiply that difficulty by another $\beta_B^2$.

Thus the robust passive question is:

> Can source-matched resonant coupling $\mathcal O_{SB}\kappa_g$ exceed thermal injection $\Gamma_{\rm th}$?

The answer still looks extremely unfavorable for ordinary matter, but the correct scaling must be evaluated with the receiver's **effective quantum cross-section**, not automatically its geometric area.

---

## 8. Status of the temperature examples

The numerical temperature ceilings derived by inserting the $\beta_B^5$ geometric-aperture bound remain valid only for that literal aperture-limited model. They should not be quoted as universal passive receiver requirements.

See `PASSIVE_WAVEZONE_TEMPERATURE_BOUND.md`; its scope must be read as geometric-aperture limited unless/until a receiver-specific effective cross-section is inserted.

---

## 9. Next strongest calculation

Derive the effective source-to-receiver coherent cross-section directly from the same quadrupole input-output coupling that gives $\kappa_g$, rather than imposing a geometric area by hand. This should reconcile

- the local far-zone curvature receiver,
- the finite-cap enclosing receiver,
- resonant scattering/absorption,
- distributed coherent arrays

within one source-mode-overlap formalism.