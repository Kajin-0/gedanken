# Passive Nonrelativistic Wave-Zone Feasibility Bound

**Timestamp:** 2026-08-07 17:28 EDT  
**Status:** Necessary-condition synthesis combining the passive quadrupole sum-rule ceiling with finite-aperture quantum reception. Not a universal quantum-gravity no-go theorem.

## 1. Ingredients

Three previously derived results are combined.

### A. Finite-aperture quantum range

For a small coherent receiver aperture of radius $a_R$,

$$
R_Q
\simeq
 a_R
\sqrt{
\frac{5\mathcal O\kappa_g}
{8\Gamma_{\rm th}}
},
$$

where

- $\kappa_g$ is total gravitational linewidth;
- $\mathcal O$ is the remaining source–receiver tensor/temporal mode overlap;
- $\Gamma_{\rm th}$ is thermal excitation injected by uncontrolled receiver channels.

An NPT wave-zone region requires

$$
R_Q>R_{\rm WZ}.
$$

### B. Wave-zone lower radius

Define

$$
R_{\rm WZ}
=\zeta\frac{c}{\omega_B},
$$

where $\zeta\gtrsim1$ specifies the desired degree of radiation-zone separation.

### C. Passive nonrelativistic graviton-linewidth ceiling

For an ordinary passive nonrelativistic quadrupole receiver,

$$
\frac{\kappa_g}{\omega_B}
\le
\frac23
\mathcal C_B\beta_B^3,
$$

where

$$
\boxed{
\mathcal C_B
=\frac{r_{s,B}}{L_B}
}
$$

is receiver compactness and

$$
\boxed{
\beta_B
=\frac{\omega_BL_B}{c}
}
$$

is the receiver's internal relativistic-speed parameter.

With internal quality factor $Q_B$,

$$
\kappa_i=\frac{\omega_B}{Q_B}.
$$

For a single dominant thermal internal bath of occupation $\bar n_B$,

$$
\Gamma_{\rm th}=\bar n_B\kappa_i.
$$

Therefore

$$
\boxed{
\frac{\kappa_g}{\Gamma_{\rm th}}
\le
\frac23
\frac{Q_B\mathcal C_B\beta_B^3}{\bar n_B}.
}
$$

---

## 2. Geometry assumption

For a single coherent material receiver, take its effective aperture radius to be no larger than its characteristic size,

$$
\boxed{a_R\le L_B.}
$$

This is the step that turns the channel bound into a material-receiver feasibility condition.

A distributed externally phased array can violate this simple identification and must be analyzed separately as a larger composite receiver.

---

## 3. Necessary wave-zone condition

The requirement

$$
R_Q>\zeta c/\omega_B
$$

implies

$$
 a_R
\sqrt{
\frac{5\mathcal O}{8}
\frac{\kappa_g}{\Gamma_{\rm th}}
}
>
\zeta\frac{c}{\omega_B}.
$$

Using

$$
a_R\le L_B
$$

and

$$
\frac{\omega_BL_B}{c}=\beta_B,
$$

we need

$$
\beta_B
\sqrt{
\frac{5\mathcal O}{8}
\frac{\kappa_g}{\Gamma_{\rm th}}
}
>\zeta.
$$

Now insert the passive sum-rule ceiling:

$$
\boxed{
\frac{5\mathcal O}{12}
\frac{Q_B\mathcal C_B\beta_B^5}{\bar n_B}
>\zeta^2.
}
$$

Define the dimensionless passive wave-zone figure of merit

$$
\boxed{
\mathfrak W_B
\equiv
\frac{5\mathcal O}{12}
\frac{Q_B\mathcal C_B\beta_B^5}{\bar n_B}.
}
$$

Then

$$
\boxed{
\mathfrak W_B>\zeta^2
}
$$

is a **necessary condition** for a nonempty NPT wave-zone interval in this receiver class.

---

## 4. Why five powers of $\beta_B$ appear

The passive graviton oscillator-strength ceiling contributes

$$
\beta_B^3.
$$

The need to intercept a finite fraction of a propagating spherical wave with a receiver no larger than $L_B$ contributes an additional

$$
(a_R\omega_B/c)^2
\lesssim\beta_B^2.
$$

Thus the true wave-zone receiver problem is parametrically harder than the already severe local gravitational-coupling problem:

$$
\boxed{
\beta_B^3
\rightarrow
\beta_B^5.
}
$$

For ordinary mechanical systems with

$$
\beta_B\ll1,
$$

this suppression is enormous.

---

## 5. High-temperature form

At

$$
k_BT\gg\hbar\omega_B,
$$

$$
\bar n_B
\simeq
\frac{k_BT}{\hbar\omega_B}.
$$

Define the thermal length

$$
\boxed{
\lambda_T
=\frac{\hbar c}{k_BT}.
}
$$

Since

$$
\frac1{\bar n_B}
\simeq
\frac{\hbar\omega_B}{k_BT}
=\beta_B\frac{\lambda_T}{L_B},
$$

we obtain

$$
\boxed{
\mathfrak W_B^{(\rm high\,T)}
\simeq
\frac{5\mathcal O}{12}
Q_B\mathcal C_B\beta_B^6
\frac{\lambda_T}{L_B}.
}
$$

Thus high-temperature passive wave-zone quantum reception is suppressed simultaneously by

1. tiny compactness $\mathcal C_B$;
2. six powers of internal relativistic speed parameter $\beta_B$;
3. small thermal-length ratio $\lambda_T/L_B$;
4. finite quality factor;
5. imperfect mode overlap.

---

## 6. Relation to the earlier receiver phase bound

The earlier full-mode passive NPT feasibility condition was

$$
\frac23
\frac{Q_B\mathcal C_B\beta_B^3}{\bar n_B}>1.
$$

The finite-aperture wave-zone condition is stronger:

$$
\frac{5\mathcal O}{12}
\frac{Q_B\mathcal C_B\beta_B^5}{\bar n_B}
>\zeta^2.
$$

The difference is precisely the geometric price of accessing enough of a **propagating** branch-difference mode from a finite physical receiver.

---

## 7. What this does and does not rule out

The bound applies to a receiver satisfying all of the following:

- stationary/passive;
- nonrelativistic particle-coordinate dynamics;
- quadrupolar gravitational coupling;
- oscillator-strength sum-rule assumptions;
- finite physical size/aperture $a_R\le L_B$;
- stationary thermal internal noise;
- linear coherent wave-zone capture.

It does **not** rule out

- active/inverted collective receivers;
- relativistic field-theoretic receivers;
- strongly self-gravitating/compact receivers;
- enormous distributed coherent arrays whose aperture is treated as a larger composite system;
- phase-sensitive/non-Gaussian receiver protocols;
- the near-field gravitational-entanglement regime.

Therefore this is a receiver-class feasibility bound, not a universal no-go theorem for gravitational quantum communication.

---

## 8. Physical reading

> **Ordinary matter is disadvantaged twice. First, its passive gravitational transition strength is suppressed by compactness and nonrelativistic internal motion. Second, a wave-zone experiment must physically collect a finite fraction of a spherical spin-2 mode, introducing another aperture penalty. Combining the two converts the already severe $\beta^3$ receiver suppression into a $\beta^5$ wave-zone suppression, or $\beta^6$ in the high-temperature form.**

This strengthens the conclusion that the central challenge may not be whether gravity possesses quantum channel capacity, but whether ordinary laboratory matter can couple to that channel strongly and coherently enough in the radiation zone.

---

## 9. Strongest next step

1. Evaluate $\mathfrak W_B$ for representative mechanical, atomic, electromagnetic, and hypothetical compact receivers.
2. Ask whether a relativistic QFT receiver has an analogous finite-aperture/KMS bound that replaces the nonrelativistic $\beta^5$ law.
3. Determine whether distributed arrays can improve aperture access without paying an equivalent many-body oscillator-strength/noise penalty.
