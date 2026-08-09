# Material-Response Bridge for Passive Linear Matter Networks

## 1. Purpose

`PASSIVE_NETWORK_CUTSET_THEOREM.md` bounds the end-to-end coherent-transfer integral by

```math
\operatorname{Tr}(K_g^\dagger K_g),
```

the total gravitational coupling rate of each passive endpoint network.

This note connects that network quantity to the microscopic positive mass-quadrupole spectral weight for a broad class of passive **linear bosonic matter networks**.

The result does not yet claim arbitrary nonlinear/interacting matter.

---

## 2. Internal normal-mode basis

Let the isolated linear endpoint Hamiltonian be

```math
H=\mathbf a^\dagger\Omega\mathbf a,
\qquad
\Omega=\Omega^\dagger>0.
```

Choose a unitary matrix `U` that diagonalizes the internal Hamiltonian,

```math
U^\dagger\Omega U
=\operatorname{diag}(\omega_1,\ldots,\omega_N),
```

and define normal modes

```math
\mathbf c=U^\dagger\mathbf a.
```

The gravitational coupling matrix transforms as

```math
\widetilde K_g=K_gU.
```

Because `U` is unitary,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
=
\operatorname{Tr}(\widetilde K_g^\dagger\widetilde K_g)
=
\sum_n\sum_\alpha
|\widetilde K_{g,\alpha n}|^2.
}
```

Here `alpha` labels orthogonal gravitational output channels.

---

## 3. Gravitational linewidth of each normal mode

In standard Markov input-output normalization, the total spontaneous gravitational linewidth of normal mode `n` is

```math
\boxed{
\kappa_{g,n}
=\sum_\alpha
|\widetilde K_{g,\alpha n}|^2.
}
```

Therefore

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}.
}
```

This equality is basis independent. Internal coherent mixing cannot create additional total gravitational coupling trace; it redistributes the same coupling resource among dressed modes.

---

## 4. Microscopic quadrupole identification

For weak linearized gravity, the one-graviton quadrupole decay rate for a one-quantum matter transition `|1_n> -> |0>` is

```math
\boxed{
\kappa_{g,n}
=
\frac{2G\omega_n^5}{5\hbar c^5}
Q_{ij}^{0n}Q_{ij}^{n0},
}
```

with the same STF tensor normalization used in the V7 EWSR derivation.

Thus the input-output linewidth is not a free phenomenological parameter once the matter mode and its mass-quadrupole matrix element are fixed.

For all retained normal modes with

```math
0<\omega_n\le\Omega,
```

we obtain

```math
\operatorname{Tr}(K_g^\dagger K_g)
=
\frac{2G}{5\hbar c^5}
\sum_{\omega_n\le\Omega}
\omega_n^5
Q_{ij}^{0n}Q_{ij}^{n0}.
```

For a ground-state endpoint this is exactly the cumulative positive gravitational transition-rate weight `K_g(Omega)` defined in `SPECTRAL_GENERALIZATION.md`.

Hence

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
K_g(\Omega).
}
```

Equality holds when the retained linear mode set contains all positive quadrupole transitions below `Omega` that couple to the gravitational bath.

---

## 5. EWSR closure

The passive quadrupole EWSR gives

```math
K_g(\Omega)
\le
\frac{4G}{3c^5}
\langle I\rangle\Omega^4.
```

Therefore any passive linear bosonic matter endpoint in the retained band obeys

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}
\langle I\rangle\Omega^4.
}
```

Combining with the passive-network cut-set theorem gives

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\frac{4G\Omega^4}{3c^5}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

This is now a closed theorem for the stated class:

```text
compact passive nonrelativistic linear bosonic matter endpoints
+ weak quadrupole coupling to linearized gravity
+ stable passive linear Markov input/output dynamics
+ one-way contractive gravitational propagation.
```

It is independent of the number of matter modes and of coherent mode mixing inside either endpoint.

---

## 6. Compactness form

Define the endpoint length scale from its inertia moment,

```math
L_j^2
\equiv
\frac{\langle I_j\rangle}{M_j},
```

and

```math
\mathcal C_j
=\frac{2GM_j}{c^2L_j},
\qquad
\beta_j(\Omega)
=\frac{\Omega L_j}{c}.
```

Then

```math
\frac{4G}{3c^5}
\langle I_j\rangle\Omega^4
=
\frac23\Omega\mathcal C_j\beta_j^3.
```

Thus

```math
\boxed{
\Gamma_{\rm coh}
\le
\frac23\eta_{\max}\Omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

This is the many-mode linear-network generalization of the V7 narrowband passive linewidth ceiling.

---

## 7. What ordinary damping and high Q can do

Ordinary damping changes the full passive matrix `K` and therefore changes resonance widths, peak conversion, and internal mode shapes.

It does **not** increase

```math
\operatorname{Tr}(K_g^\dagger K_g)
```

unless the physical gravitational quadrupole coupling itself changes.

Conversely, eliminating ordinary damping can make selected gravitational branching fractions approach unity, but then the endpoint response bandwidth becomes controlled by the same small gravitational coupling matrix. The cut-set theorem converts this into an integrated statement rather than a qualitative tradeoff.

---

## 8. Thermal passive states

The microscopic EWSR in V7 was written for a passive diagonal state

```math
\rho=\sum_m p_m|m\rangle\langle m|,
```

with positive net absorptive weights `(p_m-p_n)`.

For a linear harmonic endpoint, the coherent small-signal transfer matrix is state independent while thermal occupation appears as added output noise. The coupling matrix `K_g` still describes the one-quantum gravitational damping constants of the modes.

However, identifying `Tr(K_g^dagger K_g)` with the **thermal net absorptive** spectral sum requires care because the latter carries population-difference weights. Therefore the cleanest theorem statement uses the ground-state/vacuum coupling resource for the coherent-transfer ceiling and treats thermal occupation separately in the capacity/noise analysis.

Do not claim the thermal population-weighted EWSR makes the coherent coupling matrix itself smaller without an explicit derivation.

---

## 9. Beyond linear bosonic matter

A general interacting passive quantum system still has a Lehmann spectral representation and positive absorptive quadrupole spectral measure. That strongly suggests a more general susceptibility formulation.

What is not yet established is that an arbitrary interacting endpoint can be represented, for the purpose of the end-to-end coherent-transfer integral, by a passive linear scattering realization whose coupling trace is exactly the same cumulative quadrupole spectral resource.

That extension should be proved through linear response / passive dilation rather than assumed.

---

## 10. Strongest current statement

Allowed:

> For arbitrary stable passive **linear bosonic** source and receiver networks with compact nonrelativistic matter and quadrupole coupling to propagating linearized gravity, the frequency-integrated coherent transfer is bounded by the smaller endpoint mass-quadrupole oscillator-strength resource. The bound is unaffected by adding modes or coherent internal mode mixing.

Not yet allowed:

- arbitrary nonlinear matter;
- arbitrary relativistic quantum fields;
- active/inverted networks;
- nonstationary parametrically driven networks;
- a propagation-independent universal numerical coefficient;
- a noisy quantum-capacity theorem beyond the explicitly treated channel class.
