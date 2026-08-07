# KMS Mode Efficiency: The Relativistic Thermal Limit

**Timestamp:** 2026-08-07 16:21 EDT  
**Status:** Active theoretical derivation for Experiment 01

The free-field stress test showed that relativistic QFT does not possess a universal UV-integrated oscillator-strength ceiling analogous to the nonrelativistic quadrupole bound. This note asks what **does** remain universal for a passive thermal receiver. The answer is a mode-by-mode response/noise relation fixed by KMS equilibrium.

---

## 1. Unsymmetrized stress-energy spectrum

For a Hermitian smeared receiver operator

$$
F_u
=\int d^3x\,
u_{\mu\nu}(\mathbf x)T^{\mu\nu}(\mathbf x),
$$

define the unsymmetrized equilibrium spectrum

$$
\boxed{
S_u^>(\omega)
=\int_{-\infty}^{\infty}dt\,
e^{i\omega t}
\langle F_u(t)F_u(0)\rangle.
}
$$

For a Gibbs state at inverse temperature

$$
\beta=(k_BT)^{-1},
$$

the KMS condition gives

$$
\boxed{
S_u^>(-\omega)
=e^{-\beta\hbar\omega}S_u^>(+\omega).
}
$$

---

## 2. Response spectrum

The commutator spectrum is

$$
A_u(\omega)
=S_u^>(\omega)-S_u^>(-\omega).
$$

With the Kubo convention

$$
\chi_u(t)
=\frac{i}{\hbar}\Theta(t)
\langle[F_u(t),F_u(0)]\rangle,
$$

one has

$$
\boxed{
A_u(\omega)=2\hbar\chi_u''(\omega).
}
$$

For positive frequency, KMS therefore implies

$$
S_u^>(\omega)
=
\frac{2\hbar\chi_u''(\omega)}
{1-e^{-\beta\hbar\omega}}.
$$

---

## 3. Symmetrized noise and fluctuation-dissipation theorem

Define the symmetrized/Hadamard spectrum

$$
S_{u,H}(\omega)
=\frac12
\left[
S_u^>(\omega)+S_u^>(-\omega)
\right].
$$

Then

$$
\boxed{
S_{u,H}(\omega)
=
\hbar
\coth\left(\frac{\beta\hbar\omega}{2}\right)
\chi_u''(\omega).
}
$$

This is the mode-resolved fluctuation-dissipation relation.

Equivalently,

$$
\boxed{
\frac{\hbar\chi_u''(\omega)}{S_{u,H}(\omega)}
=
\tanh\left(\frac{\beta\hbar\omega}{2}\right).
}
$$

Thus increasing a passive thermal receiver's absorptive stress-energy response necessarily increases its equilibrium stress-energy noise by the same spectral factor.

---

## 4. Effective bosonic thermal occupation

Using

$$
\bar n_T(\omega)
=\frac1{e^{\beta\hbar\omega}-1},
$$

$$
\coth\left(\frac{\beta\hbar\omega}{2}\right)
=2\bar n_T+1.
$$

Therefore

$$
\boxed{
S_{u,H}
=\hbar(2\bar n_T+1)\chi_u''.
}
$$

The relativistic stress-energy receiver has exactly the same thermal response/noise factor that appeared earlier in the oscillator and Gaussian-channel models.

This is important: the factor

$$
2\bar n+1
$$

is not a peculiarity of a mechanical oscillator model. It is the universal KMS factor of any passive equilibrium quantum receiver mode.

---

## 5. What KMS does and does not bound

KMS gives no universal upper bound on

$$
\chi_u''(\omega)
$$

at one selected frequency. A relativistic field theory can possess large narrowband spectral weight, and the free-field UV example showed why a global oscillator-strength ceiling need not exist.

But KMS fixes the ratio

$$
\boxed{
\text{equilibrium noise}
\,/\,
\text{absorptive response}
}
$$

at every frequency.

Thus a passive receiver cannot make its thermal noise arbitrarily small relative to its absorptive gravitational response without lowering its effective temperature.

---

## 6. Multiport receiver generalization

Let the desired source-matched gravitational port have coupling rate

$$
\kappa_\Delta.
$$

Let all uncontrolled ports be labeled $a$, with rates

$$
\kappa_a
$$

and thermal occupations

$$
\bar n_a.
$$

The total damping is

$$
\kappa_{\rm tot}
=\kappa_\Delta+
\sum_a\kappa_a.
$$

Assume the desired source port is in vacuum apart from the coherent branch-dependent input.

The stationary branch-independent receiver occupation is

$$
\boxed{
 m_*
=\frac{\sum_a\kappa_a\bar n_a}
{\kappa_{\rm tot}}.
}
$$

The maximum coherent capture fraction from the desired port is

$$
\eta_\Delta^{\max}
=\frac{\kappa_\Delta}{\kappa_{\rm tot}}.
$$

---

## 7. Universal multiport weak-cat NPT criterion

The weak-cat thermal channel becomes NPT when

$$
\eta_\Delta^{\max}>m_*.
$$

Therefore

$$
\boxed{
\kappa_\Delta
>
\sum_a\bar n_a\kappa_a.
}
$$

This is the multiport form of the fundamental thermal receiver condition.

Vacuum loss channels have

$$
\bar n_a=0
$$

and therefore do not move the entanglement-breaking boundary, although they reduce the amount and speed of entanglement transfer.

Thermally occupied uncontrolled channels do move the boundary because they inject branch-independent noise into the receiver.

---

## 8. Universal multiport global-history criterion

The global fidelity-history witness requires

$$
\eta_\Delta^{\max}>m_*+\frac12.
$$

Thus

$$
2\kappa_\Delta
>
\kappa_{\rm tot}
+2\sum_a\bar n_a\kappa_a.
$$

Since

$$
\kappa_{\rm tot}
=\kappa_\Delta+\sum_a\kappa_a,
$$

we obtain

$$
\boxed{
\kappa_\Delta
>
\sum_a(2\bar n_a+1)\kappa_a.
}
$$

This is the natural multiport KMS generalization of the earlier single-bath result.

At zero temperature,

$$
\boxed{
\kappa_\Delta>\sum_a\kappa_a
}
$$

is the $>50\%$ useful-mode requirement of the simple global history witness.

---

## 9. Mode-resolved quantum cooperativity

Define

$$
\boxed{
\mathcal C_{u}^{\rm NPT}
=\frac{\kappa_\Delta}
{\sum_a\bar n_a\kappa_a}.
}
$$

Then

$$
\boxed{
\mathcal C_u^{\rm NPT}>1
}
$$

is the weak-cat entanglement-transfer condition.

For the global history witness define

$$
\boxed{
\mathcal C_u^F
=\frac{\kappa_\Delta}
{\sum_a(2\bar n_a+1)\kappa_a}.
}
$$

Then

$$
\boxed{\mathcal C_u^F>1.}
$$

These definitions remain meaningful for relativistic QFT receivers because they require only mode-resolved coupling/noise rates, not a nonrelativistic quadrupole sum-rule ceiling.

---

## 10. KMS version of the receiver phase diagram

The earlier nonrelativistic receiver phase diagram separated

- total gravitational oscillator strength;
- source-mode overlap.

The relativistic version replaces the oscillator-strength ceiling by a directly measurable/source-computable mode cooperativity.

The two key resources are now

$$
\boxed{
\text{source-matched absorptive spectral weight}
}
$$

and

$$
\boxed{
\text{thermal occupation of all uncontrolled response channels}.
}
$$

Passivity/KMS fixes the minimum equilibrium noise associated with each uncontrolled absorptive channel.

---

## 11. Causal front in the multiport relativistic receiver

For a stationary receiver with total damping $\kappa_{\rm tot}$ and time-reversal-matched source mode, the coherent desired-port capture by time

$$
\tau=t-R/c
$$

is

$$
\eta_\Delta(\tau)
=\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau}).
$$

The stationary thermal floor is

$$
m_*=\frac{\sum_a\bar n_a\kappa_a}
{\kappa_{\rm tot}}.
$$

Therefore the NPT front is

$$
\boxed{
T_{\rm NPT}
=\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-
\sum_a\bar n_a\kappa_a}
\right]
}
$$

provided

$$
\kappa_\Delta>\sum_a\bar n_a\kappa_a.
$$

This is the relativistic multiport continuation of the causal quantum front.

---

## 12. High-temperature limit

For channels equilibrated at a common high temperature,

$$
\bar n_a
\simeq
\frac{k_BT}{\hbar\omega_a}.
$$

If the relevant channels are narrowband near $\omega_B$,

$$
\sum_a\bar n_a\kappa_a
\simeq
\frac{k_BT}{\hbar\omega_B}
\sum_a\kappa_a.
$$

Then NPT requires

$$
\boxed{
\frac{\kappa_\Delta}
{\sum_a\kappa_a}
>
\frac{k_BT}{\hbar\omega_B}.
}
$$

For an ordinary high-temperature passive receiver the right-hand side is generally much larger than unity, so a quantum front is impossible unless the uncontrolled channels are extraordinarily suppressed or cooled.

This reproduces the severe thermal requirement in a form independent of a nonrelativistic material model.

---

## 13. Important conceptual conclusion

The relativistic QFT analysis has separated two fundamentally different kinds of bounds:

### Nonrelativistic passive matter

A sum rule can bound the **absolute response strength** through mass, size, and internal speed.

### General passive relativistic QFT

No universal UV-integrated response ceiling survives without bandwidth/microscopic assumptions, but KMS universally fixes the **noise-to-response ratio** of every thermal mode.

Thus relativistic field theory can evade the nonrelativistic oscillator-strength ceiling while still obeying a strict quantum-statistical response/noise tradeoff.

---

## 14. Einstein/Feynman compression

> **Relativity removes the simple material oscillator-strength ceiling because a quantum field has arbitrarily high-frequency internal excitations. But thermodynamics puts back a different restriction. A passive receiver cannot have absorption without fluctuations: the same spectral function that lets it absorb the gravitational branch mode fixes its equilibrium noise through the KMS relation. So the relativistic receiver problem is not bounded by a universal amount of oscillator strength; it is bounded mode by mode by quantum efficiency. The source-receiver entanglement front appears only when the useful gravitational mode coupling exceeds the thermally occupied response of every uncontrolled channel.**

---

## 15. Novelty discipline

KMS, fluctuation-dissipation theory, multiport bosonic input-output channels, and thermal entanglement-breaking thresholds are established physics.

Potentially distinctive is the causal-gravity synthesis:

$$
\boxed{
\kappa_\Delta
>
\sum_a\bar n_a\kappa_a
}
$$

as the mode-resolved relativistic weak-cat condition for a causal gravitational entanglement front, together with the explicit history-coherence interpretation.

This should not be claimed as novel until checked against the quantum communication / relativistic detector literature.

---

## 16. Immediate next step

Use the exact source–receiver quadrupole mode overlap to express $\kappa_\Delta$ for a real source/receiver pair, then evaluate whether any known active collective or field-theoretic receiver can make

$$
\mathcal C_u^{\rm NPT}>1
$$

without relying on unrealistic full-$4\pi$ mode access.