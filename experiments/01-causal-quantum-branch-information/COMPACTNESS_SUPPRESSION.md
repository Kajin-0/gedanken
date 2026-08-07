# Compactness–Velocity Suppression of a Material Gravitational Quantum Receiver

**Timestamp:** 2026-08-07 15:50 EDT  
**Status:** Active derivation for Experiment 01

This note rewrites the explicit acoustic-bar graviton linewidth in dimensionless form. The result identifies why ordinary laboratory matter is intrinsically a very poor coherent receiver of a propagating gravitational quantum mode.

---

## 1. Start from the explicit bar-resonator linewidth

For the $l$th odd longitudinal mode of the cylindrical bar analyzed by Tobar et al.,

$$
\boxed{
\kappa_g
=\frac{8GML^2\omega_l^4}{l^4\pi^4c^5}.
}
$$

For an acoustic mode with sound speed $v_s$,

$$
\omega_l=\frac{l\pi v_s}{L}.
$$

Substituting gives

$$
\boxed{
\kappa_g
=\frac{8GMv_s^4}{L^2c^5}.
}
$$

For this ideal acoustic dispersion the explicit mode number cancels from the gravitational radiative linewidth.

---

## 2. Rewrite using compactness

Define the Schwarzschild radius of the receiver mass,

$$
\boxed{r_s=\frac{2GM}{c^2}.}
$$

Then

$$
\boxed{
\kappa_g
=4\frac{c}{L}
\left(\frac{r_s}{L}\right)
\left(\frac{v_s}{c}\right)^4.
}
$$

Dividing by the mechanical frequency,

$$
\boxed{
\frac{\kappa_g}{\omega_l}
=
\frac{4}{l\pi}
\left(\frac{r_s}{L}\right)
\left(\frac{v_s}{c}\right)^3.
}
$$

This is the key dimensionless suppression law.

---

## 3. Physical meaning

Two small parameters multiply:

### Weak gravitational compactness

$$
\frac{r_s}{L}\ll1
$$

for ordinary laboratory objects.

### Nonrelativistic internal motion

$$
\frac{v_s}{c}\ll1.
$$

The latter enters cubed in $\kappa_g/\omega$.

Thus the gravitational quantum radiative linewidth of an ordinary mechanical mode is suppressed not merely by Newton's constant in isolation but by

$$
\boxed{
\text{compactness}\times
(\text{internal velocity}/c)^3.
}
$$

For a material receiver this is an extraordinarily severe combination.

---

## 4. Strong coherent-capture quality factor

The internal mechanical linewidth is

$$
\kappa_i=\frac{\omega_l}{Q_i}.
$$

The condition

$$
\kappa_g>\kappa_i
$$

corresponds to gravitational radiative coupling dominating vacuum internal loss and is also the zero-temperature threshold of the simple $>50\%$ history-capture witness.

Using the dimensionless ratio above,

$$
\boxed{
Q_i
>
\frac{l\pi}{4}
\frac{L}{r_s}
\left(\frac{c}{v_s}\right)^3.
}
$$

This is **not** the zero-temperature threshold for the mere existence of any source-receiver entanglement: a pure-loss channel with arbitrarily small nonzero transmissivity can preserve an arbitrarily small amount of entanglement. It is the scale required for order-unity gravitational radiative capture relative to internal vacuum loss / the simple strong-history witness.

---

## 5. Finite-temperature NPT threshold

The fundamental weak-cat thermal condition is

$$
\kappa_g>\bar n_i\kappa_i.
$$

Therefore

$$
\boxed{
Q_i
>
\bar n_i
\frac{l\pi}{4}
\frac{L}{r_s}
\left(\frac{c}{v_s}\right)^3.
}
$$

At high temperature,

$$
\bar n_i\simeq\frac{k_BT}{\hbar\omega_l},
$$

which is equivalent to

$$
\boxed{
Q_i>\frac{k_BT}{\hbar\kappa_g}.
}
$$

Thus finite temperature multiplies the already enormous compactness/velocity penalty by the thermal occupation.

---

## 6. Representative niobium-bar scale

Take the geometry quoted in the 2024 single-graviton sensing analysis:

- density $\rho\simeq8570\,\mathrm{kg/m^3}$;
- length $L=1\,\mathrm m$;
- radius $0.5\,\mathrm m$;
- sound speed $v_s\simeq5\times10^3\,\mathrm{m/s}$.

The mass is approximately

$$
M\simeq6.7\times10^3\,\mathrm{kg}.
$$

For the fundamental longitudinal mode,

$$
f\simeq2.5\,\mathrm{kHz},
$$

and

$$
\boxed{
\kappa_g\simeq9.3\times10^{-34}\,\mathrm{s^{-1}},
}
$$

consistent with the order-$10^{-33}\,$Hz spontaneous-emission rate quoted in that work.

The dimensionless gravitational linewidth is

$$
\boxed{
\frac{\kappa_g}{\omega}
\simeq5.9\times10^{-38}.
}
$$

Thus gravitational radiative loss would dominate ordinary vacuum internal loss only at roughly

$$
\boxed{Q_i\gtrsim1.7\times10^{37}.}
$$

At $T=10\,$mK the fundamental mode has thermal occupation

$$
\bar n\simeq8.3\times10^4,
$$

so the weak-cat NPT condition would require approximately

$$
\boxed{Q_i\gtrsim1.4\times10^{42}.}
$$

These values are not proposed experimental targets; they expose the scale of the wave-zone coherent-capture problem.

---

## 7. Ideal lossless capture time

Even if all nongravitational loss were removed,

$$
\kappa_i=0,
$$

the characteristic gravitational memory time is

$$
\tau_g\sim\kappa_g^{-1}.
$$

For the bar scale above,

$$
\boxed{
\tau_g\sim10^{33}\,\mathrm s
\sim10^{25}\text{--}10^{26}\,\mathrm{yr}.
}
$$

This does not prevent a large **stimulated classical response** to an intense coherent gravitational wave. It limits coherent quantum state capture of the branch-difference mode.

The vacuum optimization derived in `VACUUM_CAPTURE_OPTIMIZATION.md` makes this precise:

$$
\mathcal N_{\max}(t)\simeq\kappa_gt
$$

at short times even after optimizing the source branch-wave amplitude.

---

## 8. What would remove the suppression?

The dimensionless ratio

$$
\frac{\kappa_g}{\omega}
\sim
\left(\frac{r_s}{L}\right)
\left(\frac{v}{c}\right)^3
$$

suggests two routes:

1. **relativistic internal dynamics:** $v\sim c$;
2. **strong compactness:** $r_s/L$ no longer tiny.

Both point away from ordinary condensed matter and toward relativistic/astrophysical systems.

In the formal limit

$$
\frac{r_s}{L}\sim1,
\qquad
\frac{v}{c}\sim1,
$$

the gravitational radiative linewidth can become an appreciable fraction of the dynamical frequency.

This is not surprising physically—strongly self-gravitating relativistic systems radiate efficiently—but it gives the Gedankenexperiment a useful bridge between tabletop weak gravity and genuinely strong quantum-gravitational receivers.

---

## 9. Design lesson

For a laboratory wave-zone quantum receiver, simply increasing the source gravitational-wave amplitude is not enough. The receiver itself must have a sufficiently large **gravitational radiative participation ratio**.

The relevant quantity is

$$
\boxed{
\epsilon_G
\equiv
\frac{\kappa_g}{\omega}
}
$$

rather than raw force sensitivity.

For ordinary acoustic matter,

$$
\epsilon_G
\sim
\text{compactness}\times(v_s/c)^3
$$

is catastrophically small.

This explains why a device can be an excellent classical gravitational-wave sensor yet still be an extremely poor coherent receiver of gravitational quantum information.

---

## 10. Novelty discipline

The bar linewidth and quadrupole radiation formula are established. Rewriting them in compactness variables is algebra, not a new physical law.

The potentially useful contribution to Experiment 01 is the interpretation:

> **the causal quantum-information receiver problem is controlled by gravitational radiative participation, which for ordinary matter is suppressed by compactness and relativistic internal speed, even when classical stimulated sensing is feasible.**

This strengthens the distinction between gravitational-wave detection and gravitational quantum-state capture.

---

## 11. Immediate next step

Explore whether a distributed collective receiver can evade the material suppression by making the relevant quadrupole matrix element scale coherently with many constituents. The key question is whether $Q_{ij}^{10}Q_{ij}^{01}$ can achieve $N^2$-type enhancement without the internal decoherence rate scaling equally fast.