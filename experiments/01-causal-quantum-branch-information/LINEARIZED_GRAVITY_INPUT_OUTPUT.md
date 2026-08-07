# Linearized-Gravity Input-Output Coupling

**Timestamp:** 2026-08-07 15:39 EDT  
**Status:** Active derivation for Experiment 01

This note removes the phenomenological gravitational receiver rate $\kappa_g$ by deriving it from the linearized quantum-gravity quadrupole interaction.

---

## 1. Gauge-invariant quadrupole interaction

For a compact nonrelativistic quantum system in linearized gravity, a clean gauge-invariant long-wavelength interaction is

$$
\boxed{
H_I=-\frac12 Q_{ij}\,E_{ij},
}
$$

where

$$
E_{ij}=C_{i0j0}
$$

is the electric part of the Weyl tensor and $Q_{ij}$ is the trace-free mass quadrupole operator.

This interaction is standard in quantum-gravity calculations of quadrupolar transitions and avoids the gauge ambiguity of using a bare metric perturbation without the associated stress-energy constraints.

---

## 2. Quadrupole spontaneous-graviton rate

For a transition $|1\rangle\to|0\rangle$ at angular frequency $\omega_B$, let

$$
Q_{ij}^{10}=\langle1|Q_{ij}|0\rangle.
$$

The standard quadrupole transition rate obtained from linearized quantum gravity is

$$
\boxed{
\Gamma_g
=
\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

A useful way to see the coefficient is to start from the gauge-invariant atomic energy-loss result written in terms of trace-free quadrupole matrix elements. For an STF quadrupole, the tensor combination reduces to three times $Q_{ij}^{10}Q_{ij}^{01}$, and dividing the emitted power by $\hbar\omega_B$ gives the expression above.

For a harmonic receiver mode, the $n\to n-1$ rate is proportional to $n$, so the mean occupation decays at the one-quantum rate. Therefore the gravitational radiative linewidth in the Markov input-output equation is

$$
\boxed{\kappa_g=\Gamma_g.}
$$

This is the key reciprocity identification: **the rate at which the receiver emits a graviton into its matched quadrupolar continuum is the same coupling rate governing absorption from the time-reversed incoming mode.**

---

## 3. Harmonic quadrupole receiver

Let the receiver quadrupole be linear in a mechanical mode coordinate,

$$
Q_{ij}=\Lambda_B e_{ij}x_B,
$$

where $e_{ij}$ is a fixed STF geometry tensor and

$$
x_{\rm zpf}=\sqrt{\frac{\hbar}{2\mu_B\omega_B}}.
$$

Then

$$
Q_{ij}^{10}Q_{ij}^{01}
=\Lambda_B^2x_{\rm zpf}^2\,e_{ij}e_{ij},
$$

so

$$
\boxed{
\kappa_g
=
\frac{G\Lambda_B^2\omega_B^4}{5\mu_Bc^5}
(e_{ij}e_{ij}).
}
$$

For the unnormalized plus tensor

$$
e_{ij}=\operatorname{diag}(1,-1,0),
$$

$$
e_{ij}e_{ij}=2,
$$

and therefore

$$
\boxed{
\kappa_g
=
\frac{2G\Lambda_B^2\omega_B^4}{5\mu_Bc^5}.
}
$$

If $\Lambda_B=\mu_BL_B$,

$$
\boxed{
\kappa_g
=
\frac{2G\mu_BL_B^2\omega_B^4}{5c^5}.
}
$$

The exact numerical prefactor is geometry/convention dependent; the invariant expression in terms of $Q_{ij}^{10}Q_{ij}^{01}$ is the preferred paper-level formula.

---

## 4. Connection to explicit bar-resonator calculations

Tobar, Manikandan, Beitel, and Pikovski (Nature Communications 15, 7229, 2024) derive the full quantized interaction of a cylindrical acoustic bar with gravitons. For the $l$th odd longitudinal mode they obtain

$$
\boxed{
\Gamma_{\rm spon}
=
\frac{8GML^2\omega_l^4}
{l^4\pi^4c^5}.
}
$$

For that specific geometry one should simply set

$$
\boxed{\kappa_g=\Gamma_{\rm spon}}
$$

rather than map through the abstract $\Lambda_B$ parameter.

Their niobium example gives a spontaneous gravitational linewidth of order

$$
\kappa_g\sim10^{-33}\ {\rm Hz},
$$

illustrating the extreme weakness of the receiver-graviton coupling.

---

## 5. Fully gravitational thermal entanglement condition

The stationary thermal receiver derived in `INPUT_OUTPUT_THERMAL_FRONTS.md` transfers weak-cat entanglement iff

$$
\kappa_g>\bar n_i\kappa_i.
$$

Substituting the quadrupole rate gives

$$
\boxed{
\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}
>
\bar n_i\kappa_i.
}
$$

If

$$
\kappa_i=\frac{\omega_B}{Q_i},
$$

then the required mechanical quality factor is

$$
\boxed{
Q_i
>
\frac{5\hbar c^5\bar n_i}
{2G\omega_B^4Q_{ij}^{10}Q_{ij}^{01}}.
}
$$

The low-cost global fidelity-history witness instead requires

$$
\boxed{
\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}
>
(2\bar n_i+1)\kappa_i.
}
$$

---

## 6. Quantum gravitational cooperativity

Define

$$
\boxed{
\mathcal C_G^{\rm ent}
\equiv
\frac{\kappa_g}{\bar n_i\kappa_i}.
}
$$

For $\bar n_i>0$,

$$
\boxed{
\mathcal C_G^{\rm ent}>1
}
$$

is the fundamental weak-cat entanglement-transfer condition for the matched thermal receiver.

The stronger history-fidelity cooperativity is

$$
\boxed{
\mathcal C_G^{F}
\equiv
\frac{\kappa_g}{(2\bar n_i+1)\kappa_i},
}
$$

with

$$
\mathcal C_G^{F}>1
$$

for the simple global witness.

These are gravity-specific versions of familiar quantum-cooperativity ratios; no novelty is claimed for the general concept of cooperativity.

---

## 7. High-temperature form

When

$$
k_BT\gg\hbar\omega_B,
$$

$$
\bar n_i\simeq\frac{k_BT}{\hbar\omega_B}.
$$

The fundamental condition becomes

$$
\boxed{
\kappa_gQ_i
>
\frac{k_BT}{\hbar}.
}
$$

Equivalently,

$$
\boxed{
Q_i
>
\frac{k_BT}{\hbar\kappa_g}.
}
$$

This form is especially revealing: the receiver's gravitational spontaneous-emission rate must beat its thermal decoherence scale after multiplication by its storage quality factor.

For the low-cost fidelity witness, the high-temperature requirement is approximately twice as strong,

$$
Q_i\gtrsim\frac{2k_BT}{\hbar\kappa_g}.
$$

---

## 8. Direct front time in gravitational parameters

For a pre-equilibrated receiver, the optimized NPT front is

$$
T_{\rm NPT}^{\rm opt}(R)
=
\frac{R}{c}
+\frac{1}{\kappa_g+\kappa_i}
\ln\left(
\frac{\kappa_g}
{\kappa_g-\bar n_i\kappa_i}
\right).
$$

Substituting

$$
\kappa_g
=
\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}
$$

turns this into a prediction containing only

- source-to-receiver light travel time $R/c$;
- receiver quadrupole matrix element;
- receiver transition frequency;
- internal loss rate;
- thermal occupation.

Near the quantum/classical boundary,

$$
\delta
=\kappa_g-\bar n_i\kappa_i\to0^+,
$$

$$
\boxed{
T_{\rm NPT}^{\rm opt}-R/c
\sim
\frac{1}{\kappa_g+\kappa_i}
\ln(\kappa_g/\delta).
}
$$

Thus the **critical slowing of the causal entanglement front is now written directly in linearized-gravity coupling parameters.**

---

## 9. Reciprocity as the Einstein/Feynman insight

The same receiver matrix element appears in three descriptions:

1. spontaneous graviton emission by the receiver;
2. absorption of the time-reversed gravitational wavepacket;
3. the causal rate at which source branch information can be transferred into the receiver.

Therefore the receiver can be understood without inventing a separate gravitational-information coupling constant:

> **Ask how slowly the receiver would radiate one graviton if excited. Turn that process around in time. The inverse of that same tiny linewidth is the natural time scale on which an ideally mode-matched gravitational branch record can be coherently caught.**

This gives a direct physical meaning to $\kappa_g$.

---

## 10. Literature boundary

Established ingredients:

- gauge-invariant quadrupole coupling $-Q_{ij}E_{ij}/2$;
- spontaneous graviton emission from quantum transitions;
- graviton absorption/stimulated transitions in massive resonators;
- Markov input-output reciprocity.

Primary references relevant here include Boughn & Rothman (Class. Quantum Grav. 23, 5839, 2006), Hu & Yu (EPJC 81, 504, 2021), and Tobar et al. (Nature Communications 15, 7229, 2024).

Potential novelty remains the use of this rate inside the **causal branch-information front** developed in Experiment 01, not the emission formula itself.

---

## 11. Immediate next step

The next useful calculation is numerical rather than formal: evaluate the fully gravitational front and cooperativity for representative idealized receiver families (bar resonator, differential mechanical mode, and collective/enclosing mode) to determine which parameter scalings are fundamentally favorable and which are dead ends.