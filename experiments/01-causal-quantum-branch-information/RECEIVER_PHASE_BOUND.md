# Dimensionless Receiver Phase Bound

**Timestamp:** 2026-08-07 15:55 EDT  
**Status:** Active derivation for Experiment 01

This note combines the quadrupole oscillator-strength ceiling with the thermal channel thresholds to produce a receiver-level necessary condition that is independent of detailed mode engineering.

---

## 1. Receiver dimensionless parameters

Let

$$
L_B^2=\frac{I}{M}
$$

be the receiver rms mass radius defined by its ground-state mass second moment.

Define receiver compactness

$$
\boxed{
\mathcal C_B
=\frac{r_{s,B}}{L_B}
=\frac{2GM}{c^2L_B},
}
$$

and the internal dynamical-speed parameter

$$
\boxed{
\beta_B
=\frac{\omega_BL_B}{c}.
}
$$

For a nonrelativistic receiver,

$$
\beta_B\ll1.
$$

---

## 2. Sum-rule ceiling on radiative participation

The quadrupole sum rule gives

$$
\kappa_g
\le
\frac{4G}{3c^5}I\omega_B^4.
$$

Using

$$
I=ML_B^2
$$

and

$$
r_{s,B}=2GM/c^2,
$$

we obtain

$$
\boxed{
\frac{\kappa_g}{\omega_B}
\le
\frac23
\mathcal C_B\beta_B^3.
}
$$

This is a receiver-independent upper bound within the stated nonrelativistic Hamiltonian class.

---

## 3. Maximum gravitational-to-internal linewidth ratio

Let

$$
\kappa_i=\frac{\omega_B}{Q_B}.
$$

Then

$$
\frac{\kappa_g}{\kappa_i}
=Q_B\frac{\kappa_g}{\omega_B}
$$

obeys

$$
\boxed{
\frac{\kappa_g}{\kappa_i}
\le
\mathfrak R_B
\equiv
\frac23Q_B\mathcal C_B\beta_B^3.
}
$$

The dimensionless quantity

$$
\boxed{
\mathfrak R_B
=\frac23Q_B\mathcal C_B\beta_B^3
}
$$

is therefore an upper bound on how strongly gravitational radiation can participate relative to ordinary receiver loss.

---

## 4. Thermal NPT necessary condition

The fundamental weak-cat thermal condition is

$$
\kappa_g>\bar n_i\kappa_i.
$$

Since the actual $\kappa_g/\kappa_i$ cannot exceed $\mathfrak R_B$, a necessary condition for **any** receiver in the nonrelativistic quadrupole class to support a weak-cat NPT front is

$$
\boxed{
\mathfrak R_B>\bar n_i.
}
$$

Equivalently,

$$
\boxed{
Q_B
>
\frac{3\bar n_i}
{2\mathcal C_B\beta_B^3}.
}
$$

If this inequality fails, no redistribution of quadrupole oscillator strength among internal modes can push a single transition across the thermal entanglement-breaking boundary under the assumptions of the sum-rule derivation.

---

## 5. Global fidelity-history necessary condition

The simple global history witness requires

$$
\kappa_g>(2\bar n_i+1)\kappa_i.
$$

Therefore a necessary receiver-level condition is

$$
\boxed{
\mathfrak R_B>2\bar n_i+1.
}
$$

or

$$
\boxed{
Q_B
>
\frac{3(2\bar n_i+1)}
{2\mathcal C_B\beta_B^3}.
}
$$

At zero temperature this becomes

$$
\boxed{
Q_B
>
\frac{3}{2\mathcal C_B\beta_B^3}
}
$$

as a necessary condition for the $>50\%$ strong-history capture regime.

Again, this is not a zero-temperature condition for the mere existence of arbitrarily small entanglement through a pure-loss channel.

---

## 6. Receiver phase regions

The sum-rule ceiling produces three receiver-level regions.

### Region I — thermally impossible within the assumed receiver class

$$
\boxed{
\mathfrak R_B\le\bar n_i.
}
$$

Even the maximum allowed quadrupole transition strength cannot make gravitational capture beat thermal decoherence.

### Region II — NPT transfer is not excluded, but the strong global witness is

$$
\boxed{
\bar n_i<\mathfrak R_B\le2\bar n_i+1.
}
$$

A sufficiently optimized quadrupole transition may cross the fundamental thermal channel boundary, but cannot reach the simple global history-fidelity regime under the sum-rule ceiling.

### Region III — strong-history capture is not excluded

$$
\boxed{
\mathfrak R_B>2\bar n_i+1.
}
$$

The sum rule alone does not prevent a receiver from entering the strong global-witness regime.

These are **necessary**, not sufficient, conditions because a real transition may use only a small fraction of the available quadrupole oscillator strength.

---

## 7. High-temperature form

When

$$
\bar n_i\simeq\frac{k_BT}{\hbar\omega_B},
$$

introduce the thermal relativistic length

$$
\boxed{
\lambda_T=\frac{\hbar c}{k_BT}.
}
$$

Since

$$
\omega_B=\frac{c\beta_B}{L_B},
$$

$$
\bar n_i\simeq
\frac{L_B}{\lambda_T\beta_B}.
$$

The maximum possible thermal quantum cooperativity obeys

$$
\frac{\kappa_g}{\bar n_i\kappa_i}
\le
\boxed{
\frac23
Q_B\mathcal C_B
\beta_B^4
\frac{\lambda_T}{L_B}
}.
$$

Thus high-temperature gravitational quantum reception is suppressed by four powers of the internal relativistic speed parameter.

The necessary NPT condition becomes

$$
\boxed{
\frac23
Q_B\mathcal C_B
\beta_B^4
\frac{\lambda_T}{L_B}
>1.
}
$$

---

## 8. Why ordinary matter fails so badly

Ordinary material receivers simultaneously have

$$
\mathcal C_B\ll1,
$$

$$
\beta_B\ll1,
$$

and finite $Q_B$.

At nonzero temperature the additional factor

$$
\lambda_T/L_B
$$

generally does not compensate the severe $\beta_B^4$ and compactness penalties.

For the meter-scale niobium bar discussed in the associated parameter note, a realistic $Q$ would leave

$$
\mathfrak R_B/\bar n_i
$$

tens of orders of magnitude below unity.

This explains the practical wave-zone difficulty in a form that does not depend on one particular resonator design.

---

## 9. How a genuinely favorable receiver would look

The phase bound says that a good gravitational quantum receiver wants all of

1. large compactness $\mathcal C_B$;
2. relativistic internal dynamics $\beta_B$ approaching unity;
3. large quality factor $Q_B$;
4. low occupation $\bar n_i$.

Ordinary nonrelativistic matter is bad on the first two simultaneously.

A receiver approaching

$$
\mathcal C_B\sim1,
\qquad
\beta_B\sim1
$$

is no longer a conventional laboratory mechanical object. It lies in a strongly gravitating/relativistic regime where the assumptions used to derive the bound themselves begin to fail.

That failure is physically informative: the analysis points naturally toward astrophysical or field-theoretic quantum receivers rather than simply larger versions of ordinary bars.

---

## 10. Conceptual role in Experiment 01

The causal Gedankenexperiment has now separated two questions:

### Can a branch-dependent gravitational field propagate quantum information?

This is the foundational question.

### Can ordinary matter coherently receive enough of that information to demonstrate it in the wave zone?

The sum-rule phase bound says that, for ordinary nonrelativistic matter, the second problem is independently severe.

This is important because failure of a laboratory wave-zone experiment would not imply gravity lacks quantum channel capacity; it may simply reflect the receiver's tiny gravitational radiative participation.

---

## 11. Novelty discipline

The energy-weighted sum rule, graviton quadrupole rate, and compactness variables are established ingredients. The phase inequalities are direct consequences of combining them and therefore should not be presented as fundamentally new mathematical physics without a literature review.

Potentially useful synthesis:

$$
\boxed{
\text{receiver oscillator-strength ceiling}
+\text{thermal entanglement boundary}
\Rightarrow
\text{necessary phase diagram for causal gravitational quantum reception}.
}
$$

---

## 12. Immediate next step

The next question is whether field-theoretic or relativistic collective receivers can evade the nonrelativistic sum-rule ceiling, and if so, what replaces $\mathcal C_B\beta_B^3$ as the controlling dimensionless coupling.