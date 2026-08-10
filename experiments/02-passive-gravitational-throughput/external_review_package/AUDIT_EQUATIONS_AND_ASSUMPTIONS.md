# Audit Equations and Assumptions

This file contains the minimum mathematical chain a specialist needs to audit the paper without first reading every appendix.

## A. Quantity being bounded

```math
\boxed{
\Gamma_{\rm coh}
=\frac{1}{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]\,d\omega.
}
```

For a scalar transfer function this is the frequency integral of the power transmissivity. Units: inverse time.

**Audit question:** Is this the correct invariant spectral-area object for the claimed passive transfer problem, including all factors of `2 pi` and the one-sided/two-sided frequency convention?

---

## B. Passive selected-port cut

For

```math
A=-iH-\frac12K^\dagger K,
```

passivity implies the selected controllability Gramian satisfies `0 <= P_u <= I`, hence

```math
\boxed{
\|S_{g\leftarrow u}\|_2^2
\le \operatorname{Tr}(K_g^\dagger K_g).
}
```

For the complete two-ended link,

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

For a countably infinite bounded-port Markov modal Hilbert space, the finite-time identity

```math
P_u(\tau)
\le I-\mathcal T(\tau)\mathcal T^\dagger(\tau)
\le I
```

and Hilbert--Schmidt `K_g` give the same result by operator-valued Plancherel.

**Audit question:** Does the physical gravitational endpoint really satisfy the bounded-port/passive realization assumed here, or is there a hidden unbounded/non-Markov continuum issue that invalidates the selected-port trace bound?

---

## C. Coupling-magnitude / radiation-geometry separation

For the matter-to-gravity coupling operator,

```math
\Gamma_g=G^\dagger G,
\qquad
G=V\Gamma_g^{1/2},
```

so between source and receiver

```math
\boxed{
G_B^\dagger U_R G_A
=\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2},
\qquad
P_g=V_B^\dagger U_RV_A.
}
```

This is intended to prevent double counting of linewidth/oscillator strength and directional overlap.

**Audit question:** Are `G`, `V`, and `U_R` normalized on the correct on-shell radiation Hilbert space so that `Gamma_g` is exactly the gravitational decay/damping Gram operator and `P_g` is a dimensionless normalized propagation operator?

---

## D. Cumulative compact-matter resource

For mass-orthogonal elastic modes,

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I.
}
```

Using Hirakawa's historical gravitational effective area,

```math
A_{Gn}=\frac{2q_n:q_n}{M\mu_n},
```

this becomes

```math
\boxed{
\sum_n M A_{Gn}
\le\frac{40}{3}I.
}
```

**Audit question:** Is the STF contraction/normalization consistent with historical antenna conventions, and does the modal completeness step omit any physical degrees of freedom that can add positive quadrupole oscillator strength inside the stated linear-harmonic class?

---

## E. Effective area to gravitational linewidth

Hirakawa's classical emitted power gives

```math
\boxed{
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
}
```

The quantized one-graviton formula independently gives the same coefficient,

```math
\kappa_{g,n}
=\frac{2G\omega_n^5}{5\hbar c^5}
Q^{01}:Q^{10}.
```

Therefore for retained modes `omega_n <= Omega`,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
}
```

**Audit question:** Is `Tr(K_g^dagger K_g) = sum kappa_g,n` still correct with degenerate/overlapping bright modes and nonorthogonal radiation patterns, or does the physical continuum introduce off-diagonal terms that change the trace resource?

---

## F. Compact TT propagation

For normalized compact STF quadrupole radiation spaces,

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le
\frac{25}{16[k(\omega)R]^2}
\left[1+O((kR)^{-1})\right].
}
```

The leading coefficient agrees with the classical reciprocal-antenna result using `D_A = D_B = 5/2`.

**Audit question:** Does the stationary-phase/on-shell normalization correspond to the same temporal/frequency channel normalization used in the `H2` integral, or is there a hidden density-of-states or retarded/advanced factor?

---

## G. Passive recurrence

For exact passive endpoint reflection blocks,

```math
P_{\rm eff}
=(I-P_{BA}R_AP_{AB}R_B)^{-1}P_{BA}.
```

For reciprocal one-hop power factor `eta`,

```math
\boxed{
\eta_{\rm rec}
\le\frac{\eta}{(1-\eta)^2}
=\eta+O((kR)^{-4}).
}
```

**Audit question:** Does this exhaust all passive two-endpoint recurrent scattering at the retained order, or can common-bath collective effects produce an `O((kR)^-2)` modification not represented by the separated scattering blocks?

---

## H. Final narrowband closure

Using `k = omega/c` and `Omega ~= omega`,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

The paper does **not** claim the coefficient is globally saturable.

---

# Assumptions that must remain explicit

1. Weak linearized gravity.
2. Separated endpoints in the wave zone (`kR >> 1` for the retained asymptotics).
3. Compact source and receiver relative to the gravitational wavelength; no phased-aperture enhancement.
4. Leading nonrelativistic mass-quadrupole interaction.
5. Linear-harmonic matter with positive mass density and an orthogonal modal representation.
6. Passive time-invariant endpoint dynamics.
7. Finite or countably infinite **bounded-port Markov** modal sector; no unqualified claim for arbitrary PDE boundary ports or non-Markov continua.
8. No active gain, inversion, parametric pumping, external relay/mirror network, near-field exchange, or curved-background focusing.
9. Narrowband replacement of the material cutoff `Omega` by the operating `omega` in the headline form.
10. Quantum-capacity statements apply only after quantization and, where stated, to stationary vacuum pure-loss channels.
