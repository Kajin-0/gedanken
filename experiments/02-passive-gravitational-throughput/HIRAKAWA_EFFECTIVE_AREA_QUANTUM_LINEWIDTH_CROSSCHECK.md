# Hirakawa Effective Area ↔ Quantum Gravitational Linewidth Cross-Check

## Purpose

Use the full 1976 Hirakawa–Narihara–Fujimoto compact-antenna formulas as an independent classical normalization check on the one-quantum gravitational linewidth used in Experiment 02.

This is a validation bridge, not a novelty claim.

---

## 1. Hirakawa single-mode definitions

Write one compact elastic eigenmode as

```math
\bm u(\bm r,t)=x_n(t)\bm w_n(\bm r).
```

Define the modal mass

```math
\mu_n=\int \rho |\bm w_n|^2 dV.
```

Hirakawa et al. define the STF dynamic-quadrupole coefficient

```math
q_{n,ij}
=\int\rho\left(
 w_{n,i}r_j+w_{n,j}r_i
-\frac23\delta_{ij}\bm w_n\cdot\bm r
\right)dV,
```

so that to linear order in the mode coordinate

```math
\delta Q_{ij}=q_{n,ij}x_n.
```

Their gravitational effective area is

```math
\boxed{
A_{Gn}
=\frac{2\,q_n:q_n}{M\mu_n}.
}
```

Their total radiated gravitational power for the mode is

```math
P
=\frac{G}{5c^5}A_{Gn}T_nM\omega_n^4.
```

---

## 2. Quantize the same normal coordinate

For a harmonic normal mode,

```math
\hat x_n
=x_{\rm zpf}(a_n+a_n^\dagger),
\qquad
x_{\rm zpf}
=\sqrt{\frac{\hbar}{2\mu_n\omega_n}}.
```

Therefore the ground-to-one-quantum quadrupole matrix element is

```math
Q_{ij}^{01}
=q_{n,ij}
\sqrt{\frac{\hbar}{2\mu_n\omega_n}}.
```

Its STF norm is

```math
Q^{01}:Q^{10}
=
(q_n:q_n)
\frac{\hbar}{2\mu_n\omega_n}.
```

Using Hirakawa's effective-area definition,

```math
q_n:q_n
=\frac12M\mu_n A_{Gn},
```

so

```math
\boxed{
Q^{01}:Q^{10}
=\frac{\hbar M A_{Gn}}{4\omega_n}.
}
```

---

## 3. Recover the Experiment 02 one-graviton linewidth

Experiment 02 uses the standard quadrupole one-graviton spontaneous-emission rate

```math
\kappa_{g,n}
=
\frac{2G\omega_n^5}{5\hbar c^5}
Q^{01}:Q^{10}.
```

Substitution gives

```math
\boxed{
\kappa_{g,n}
=
\frac{G M A_{Gn}\omega_n^4}{10c^5}.
}
```

Thus the quantum gravitational linewidth is exactly the quantized form of Hirakawa's classical mode oscillator-strength parameter.

No additional normalization factor, factor of two, or `2 pi` conversion appears.

---

## 4. Independent short-pulse check

For a short unpolarized gravitational pulse, Hirakawa et al. give

```math
E
=
\frac{\pi^3G}{5c^3}
M\nu_n^2A_{Gn}
f_n(\hat n)F(\nu_n),
```

where `F(nu)` is incident gravitational pulse energy per unit area per Hz.

Using

```math
\omega_n=2\pi\nu_n,
\qquad
k_n=\omega_n/c,
```

and the linewidth relation above,

```math
\boxed{
\frac{E}{F(\nu_n)}
=
\frac{\pi}{2}
\frac{\kappa_{g,n}}{k_n^2}
f_n(\hat n).
}
```

The left-hand side has units of integrated absorption cross section (`area x Hz`). Thus the historical Q-independent pulse response is controlled directly by the same `kappa_g` that appears as the endpoint resource in Experiment 02.

This makes the conceptual identification precise:

```text
Hirakawa mode gravitational effective area
             <->
one-quantum gravitational linewidth
             <->
integrated single-mode gravitational oscillator strength.
```

---

## 5. Directivity cross-check

Hirakawa Eq. (15) is algebraically identical to the real-STF restriction of

```math
D_Q(\hat n)
=\frac52\frac{Q:\Lambda(\hat n):Q}{Q:Q}.
```

Therefore both the classical oscillator-strength normalization and the angular directivity normalization used in Experiment 02 have direct historical antecedents.

The new candidate theorem cannot rest on either ingredient by itself.

---

## 6. What this validates

This cross-check independently supports the microscopic material bridge

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
```

by showing that each diagonal one-mode rate has the expected classical antenna normalization when written in Hirakawa's effective-area variables.

It also reinforces the interpretation of `kappa_g` as **oscillator-strength resource**, rather than merely a chosen open-system linewidth convention.

---

## 7. What remains distinctive, if novel

After this normalization match, the candidate Experiment 02 contribution is even more sharply isolated:

```text
historical single-mode gravitational oscillator strength
+ historical reciprocity/directivity
+ established passive H2 theory
+ cumulative EWSR across all retained passive quadrupole modes at BOTH endpoints
+ normalized separated TT propagation operator
-> many-mode end-to-end integrated coherent-transfer cut set.
```

The historical paper validates the single-mode normalization but does not supply the cumulative two-ended cut set.

---

## Verdict

```text
HIRAKAWA A_G ↔ kappa_g NORMALIZATION:  EXACT MATCH
FACTOR-OF-TWO ISSUE:                  NONE FOUND
2pi ISSUE:                            NONE FOUND
SHORT-PULSE OSCILLATOR-STRENGTH SCALE: CONSISTENT
MATERIAL-BRIDGE CONFIDENCE:           INCREASED
NOVELTY OF SINGLE-MODE NORMALIZATION: NO — HISTORICAL
EXACT MANY-MODE TWO-END CLOSURE:      STILL PROVISIONAL
```
