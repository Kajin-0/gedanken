# Exact Thermal Occupancy Bound for Passive Wave-Zone Receivers

**Timestamp:** 2026-08-07 17:25 EDT  
**Status:** Consequence of `PASSIVE_WAVEZONE_FEASIBILITY_BOUND.md`; illustrative numerical examples are intentionally hypothetical, not engineering proposals.

## 1. Starting condition

For a passive nonrelativistic receiver whose coherent aperture does not exceed its characteristic size, a necessary condition for a nonempty wave-zone NPT interval is

$$
\frac{5\mathcal O}{12}
\frac{Q_B\mathcal C_B\beta_B^5}{\bar n_B}
>\zeta^2,
$$

where

$$
\mathcal C_B=\frac{r_{s,B}}{L_B},
\qquad
\beta_B=\frac{\omega_BL_B}{c},
$$

and

$$
R_{\rm WZ}=\zeta\frac{c}{\omega_B}.
$$

---

## 2. Maximum allowed thermal occupation

Solve directly for the Bose occupation:

$$
\boxed{
\bar n_B
<\bar n_{\max}
\equiv
\frac{5\mathcal O}{12\zeta^2}
Q_B\mathcal C_B\beta_B^5.
}
$$

This form is preferable to the high-temperature approximation when $\bar n_{\max}\ll1$, which is precisely the regime produced by ordinary weakly compact matter.

The physical interpretation is sharp:

> **The relevant receiver mode must be cold enough that its mean thermal occupation is below the tiny fraction of gravitational branch-mode coupling accessible in the wave zone.**

---

## 3. Exact temperature ceiling

For a Bose mode,

$$
\bar n_B
=
\frac1{
\exp(\hbar\omega_B/k_BT)-1
}.
$$

Therefore the necessary temperature condition is

$$
\boxed{
T<T_{\max}
\equiv
\frac{\hbar\omega_B}
{k_B\ln(1+\bar n_{\max}^{-1})}.
}
$$

This expression remains valid in both the high- and low-occupation regimes.

When

$$
\bar n_{\max}\ll1,
$$

$$
\boxed{
T_{\max}
\simeq
\frac{\hbar\omega_B}
{k_B|\ln\bar n_{\max}|}.
}
$$

Thus extremely small admissible occupation translates into a temperature requirement that is logarithmically below the mode's quantum temperature $\hbar\omega_B/k_B$.

---

## 4. Equivalent minimum quality factor

At fixed temperature,

$$
\boxed{
Q_B
>
Q_{\min}
=
\frac{12\zeta^2}{5\mathcal O}
\frac{\bar n_B}
{\mathcal C_B\beta_B^5}.
}
$$

This makes clear why increasing mechanical quality factor alone is generally not enough: $Q_B$ must compensate simultaneously for

- tiny compactness;
- five powers of the internal relativistic-speed parameter;
- thermal occupation;
- imperfect source–receiver mode matching.

---

## 5. Hypothetical scaling examples

The following examples are **not proposed devices**. They are deliberately generous numerical substitutions intended only to show the scale of the passive bound. Take

$$
\mathcal O=1,
\qquad
\zeta=1.
$$

### Example A — kilogram, meter, kilohertz

Take

$$
M=1\,\mathrm{kg},
\quad
L_B=1\,\mathrm m,
\quad
f_B=1\,\mathrm{kHz},
\quad
Q_B=10^{12}.
$$

Then

$$
\mathcal C_B
\simeq1.49\times10^{-27},
$$

$$
\beta_B
\simeq2.10\times10^{-5},
$$

and

$$
\boxed{
\bar n_{\max}
\simeq2.5\times10^{-39}.
}
$$

The mode quantum temperature is

$$
\frac{\hbar\omega_B}{k_B}
\simeq4.8\times10^{-8}\,\mathrm K,
$$

so the necessary temperature ceiling is approximately

$$
\boxed{
T_{\max}
\simeq5.4\times10^{-10}\,\mathrm K.
}
$$

Again, this is only the necessary bound under the idealized receiver model; it does not claim such a kilogram mode with $Q=10^{12}$ exists.

### Example B — extremely aggressive massive MHz mode

Take

$$
M=10^3\,\mathrm{kg},
\quad
L_B=1\,\mathrm m,
\quad
f_B=1\,\mathrm{MHz},
\quad
Q_B=10^{12}.
$$

Then

$$
\mathcal C_B
\simeq1.49\times10^{-24},
$$

$$
\beta_B
\simeq2.10\times10^{-2},
$$

and

$$
\boxed{
\bar n_{\max}
\simeq2.5\times10^{-21}.
}
$$

The corresponding temperature ceiling is still only roughly

$$
\boxed{
T_{\max}
\simeq1.0\times10^{-6}\,\mathrm K.
}
$$

This parameter combination is intentionally fantastical for a coherent material mode; it illustrates how hard the compactness and $\beta^5$ factors are to overcome.

### Example C — pushing toward relativistic internal dynamics

Formally take

$$
M=1\,\mathrm{kg},
\quad
L_B=1\,\mathrm{cm},
\quad
f_B=1\,\mathrm{GHz},
\quad
Q_B=10^{12}.
$$

Then

$$
\beta_B\simeq0.21,
$$

which is already outside the comfortable nonrelativistic-mechanical regime underlying the passive sum-rule interpretation.

The formal substitution gives

$$
\bar n_{\max}\sim2.5\times10^{-17},
$$

and

$$
T_{\max}\sim1.3\times10^{-3}\,\mathrm K.
$$

This should **not** be read as a valid mechanical design. Its purpose is the opposite: it shows that substantial relief occurs only as $\beta_B$ approaches relativistic values, precisely where the nonrelativistic receiver model stops being trustworthy.

---

## 6. Main physical lesson

For ordinary mechanical matter,

$$
\mathcal C_B\ll1,
\qquad
\beta_B\ll1.
$$

Consequently

$$
Q_B\mathcal C_B\beta_B^5
$$

is extraordinarily small even for very large assumed quality factors.

The wave-zone passive receiver is therefore driven toward one of three escape routes:

1. **extremely low mode occupation**;
2. **relativistic internal dynamics / field-theoretic receiver modes**;
3. **much larger compactness or a distributed receiver architecture outside the single-material-object bound.**

This is a sharper statement than merely saying that gravity is weak.

---

## 7. Acoustic-bar specialization

For a longitudinal acoustic mode with

$$
\omega_l=\frac{l\pi v_s}{L},
$$

$$
\beta_l=l\pi\frac{v_s}{c}.
$$

The explicit bar graviton linewidth is

$$
\frac{\kappa_g}{\omega_l}
=
\frac{4}{l\pi}
\mathcal C_B
\left(\frac{v_s}{c}\right)^3.
$$

Combining this specific rate with a receiver aperture $a_R\lesssim L$ gives a stricter bar-specific wave-zone condition than the generic sum-rule ceiling:

$$
\boxed{
\frac{5\mathcal O}{2}
\frac{Q_B\mathcal C_B}{\bar n_B}
(l\pi)
\left(\frac{v_s}{c}\right)^5
>\zeta^2.
}
$$

The ordinary sound-speed suppression is therefore explicitly fifth order in the wave-zone problem.

---

## 8. Important caveat: zero-temperature pure loss

At exactly zero thermal occupation,

$$
\bar n_B=0,
$$

the thermal EB range disappears: pure loss with any nonzero transmissivity is not entanglement breaking.

Therefore the strict mathematical NPT range can become unbounded at $T=0$ even though the transferred entanglement becomes vanishingly small with distance.

In that regime, the more physical object is the **finite-certification cone**, which retains explicit dependence on source strength and measurement margin.

Thus finite range is a thermal/noise statement, not a fundamental vacuum range limit on quantum gravity.

---

## 9. Strongest next step

The passive mechanical wave-zone receiver appears parametrically hopeless under generous assumptions. The strongest remaining receiver loopholes are therefore

1. relativistic field-theoretic modes;
2. distributed coherent arrays;
3. genuinely non-Gaussian/heralded reception.

These should be analyzed before elevating the passive bound into any broader no-go claim.
