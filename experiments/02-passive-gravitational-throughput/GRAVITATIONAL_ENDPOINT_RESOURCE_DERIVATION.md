# Gravitational Endpoint Resource — Independent Stage-B Derivation

**Stage:** B  
**Status:** analytic derivation; automated validation to be run on the real repository head.  
**Scope:** compact nonrelativistic linear-harmonic matter in leading mass-quadrupole gravity.

## 1. Objective

Stage A reduced the finite-dimensional passive link to the gravitational coupling traces of the two endpoints. Stage B asks whether one endpoint obeys a matter-only resource bound of the form

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le C\,\frac{G}{c^5}I\Omega^4,
```

without assuming the inherited coefficient `C=4/3`.

The derivation below starts from the continuum mass quadrupole and mass-weighted normal modes. It does not use Experiment 01's link normalization.

## 2. Mass-weighted modes

Let the equilibrium body have density `rho(x)` and center of mass at the origin. For a small displacement field write

```math
u(\mathbf x,t)=\sum_n \xi_n(t)\,w_n(\mathbf x).
```

Use the mass inner product

```math
\langle u,v\rangle_\rho
=\int_V \rho(\mathbf x)\,u(\mathbf x)\cdot v(\mathbf x)\,d^3x,
```

and choose elastic modes satisfying

```math
\langle w_n,w_m\rangle_\rho
=\mu_n\delta_{nm}.
```

Here `w_n` is dimensionless, `xi_n` has dimensions of length, and `mu_n` is the generalized modal mass. For one undamped mode

```math
\xi_n(t)=\xi_{0n}\cos\omega_n t,
```

its conserved mechanical energy is

```math
E_n=\frac12\mu_n\omega_n^2\xi_{0n}^2.
```

Only orthogonality/Bessel completeness is needed below; a complete basis is not required for the inequality.

## 3. Linearized STF mass quadrupole

Take the trace-free mass quadrupole

```math
Q_{ij}
=\int_V\rho\left(x_ix_j-\frac13\delta_{ij}r^2\right)d^3x.
```

To first order in displacement,

```math
\delta Q_{ij}
=\int_V\rho\left(
 u_i x_j+u_jx_i
-\frac23\delta_{ij}\,\mathbf x\cdot\mathbf u
\right)d^3x.
```

For mode `n`, define the STF modal quadrupole coefficient

```math
q_{n,ij}
\equiv
\int_V\rho\left(
 w_{n,i}x_j+w_{n,j}x_i
-\frac23\delta_{ij}\,\mathbf x\cdot w_n
\right)d^3x.
```

Then

```math
\delta Q_{ij}(t)=\xi_n(t)q_{n,ij}.
```

The tensor `q_n` has units of mass times length.

## 4. Gravitational energy-decay rate of one mode

At leading quadrupole order, the standard gravitational radiation power is

```math
P_g
=\frac{G}{5c^5}
\left\langle
\dddot Q_{ij}\dddot Q_{ij}
\right\rangle.
```

For the harmonic mode above,

```math
\left\langle
\dddot Q_{ij}\dddot Q_{ij}
\right\rangle
=\frac12\omega_n^6\xi_{0n}^2(q_n:q_n),
```

so

```math
P_{g,n}
=\frac{G\omega_n^6\xi_{0n}^2}{10c^5}(q_n:q_n).
```

Define the gravitational energy-decay rate by

```math
\kappa_{g,n}\equiv \frac{P_{g,n}}{E_n}.
```

The oscillation amplitude cancels, yielding

```math
\boxed{
\kappa_{g,n}
=\frac{G\omega_n^4}{5c^5}
\frac{q_n:q_n}{\mu_n}.
}
```

This is an energy linewidth: in a passive amplitude equation `dot a=-(kappa/2)a+...`, the energy decays at rate `kappa`. Therefore the input-output normalization used in Stage A identifies the total gravitational damping Gramian with `K_g^dagger K_g`, whose diagonal entries in an energy-normalized modal basis are the total gravitational energy-decay rates.

## 5. Tensor influence fields

Introduce, for every tensor component `ij`, the vector field

```math
(g^{ij})_k(\mathbf x)
=\delta_{ik}x_j+\delta_{jk}x_i
-\frac23\delta_{ij}x_k.
```

Then

```math
q_{n,ij}=\langle w_n,g^{ij}\rangle_\rho.
```

A direct tensor contraction gives the pointwise identity

```math
\boxed{
\sum_{i,j,k=1}^{3}
|(g^{ij})_k|^2
=\frac{20}{3}r^2.
}
```

One transparent check is to write

```math
A_{ijk}=\delta_{ik}x_j+\delta_{jk}x_i,
\qquad
B_{ijk}=\frac23\delta_{ij}x_k,
```

so `g=A-B`. Summing all indices gives

```math
\sum A^2=8r^2,
\qquad
\sum B^2=\frac43r^2,
\qquad
-2\sum AB=-\frac83r^2,
```

and hence `20 r^2/3`.

## 6. Bessel bound on total quadrupole oscillator strength

Normalize the modes as

```math
\phi_n=\frac{w_n}{\sqrt{\mu_n}},
```

so `phi_n` is orthonormal in the mass inner product. For each `ij`, Bessel's inequality gives

```math
\sum_n
\frac{|q_{n,ij}|^2}{\mu_n}
\le
\|g^{ij}\|_\rho^2.
```

Summing over all tensor components and using the pointwise identity,

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le
\int_V\rho
\sum_{ijk}|(g^{ij})_k|^2d^3x
=\frac{20}{3}\int_V\rho r^2d^3x.
```

Define the scalar mass second moment about the center of mass

```math
\boxed{
I_2\equiv\int_V\rho r^2d^3x.
}
```

This notation is chosen deliberately: `I_2` is not the moment of inertia about one particular axis. The trace of the ordinary inertia tensor is `2 I_2`.

Therefore

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I_2.
}
```

For a complete displacement basis the Bessel inequality becomes Parseval equality for the influence-field subspace. Rigid translations do not contribute when the origin is at the center of mass; rigid rotations likewise carry no changing mass quadrupole at linear order.

## 7. Cumulative gravitational resource

For retained modes satisfying

```math
0\le\omega_n\le\Omega,
```

combine the single-mode linewidth with the Bessel bound:

```math
\sum_n\kappa_{g,n}
=\frac{G}{5c^5}
\sum_n\omega_n^4
\frac{q_n:q_n}{\mu_n}
```

and hence

```math
\sum_n\kappa_{g,n}
\le
\frac{G\Omega^4}{5c^5}
\sum_n\frac{q_n:q_n}{\mu_n}
\le
\frac{G\Omega^4}{5c^5}\frac{20}{3}I_2.
```

Thus the independently reconstructed coefficient is

```math
\boxed{
\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}I_2\Omega^4.
}
```

Within an energy-normalized finite-dimensional Markov modal sector,

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n},
```

so

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}I_2\Omega^4.
}
```

The inherited `4/3` coefficient therefore reappears from an independent derivation. It should not be treated as established until the repository regression and normalization audit pass.

## 8. Basis mixing and off-diagonal radiation damping

The trace statement does not require the gravitational damping matrix to be diagonal in an arbitrary internal basis. If `U` is a unitary change of energy-normalized modal coordinates,

```math
K_g\rightarrow K_gU,
```

then

```math
\operatorname{Tr}[(K_gU)^\dagger(K_gU)]
=\operatorname{Tr}(K_g^\dagger K_g).
```

Passive coherent mixing can redistribute bright and dark combinations but cannot change this trace. This is a basis-invariance statement; it does not yet address active pumping or frequency-dependent non-Markov mixing.

## 9. Historical boundary checked so far

This Stage-B construction deliberately does not claim novelty for elastic-mode gravitational coupling.

Primary literature checked during reconstruction includes:

- H. Hirakawa, K. Narihara, and M.-K. Fujimoto, *Theory of Antennas for Gravitational Radiation*, J. Phys. Soc. Jpn. **41**, 1093–1101 (1976), DOI `10.1143/JPSJ.41.1093`. Its abstract explicitly treats gravitational antenna emission/reception using an eigenmode system and structure symmetry.
- J. Alberto Lobo, *What can we learn about gravitational wave physics with an elastic spherical antenna?*, Phys. Rev. D **52**, 591 (1995), arXiv:`gr-qc/0006102`, DOI `10.1103/PhysRevD.52.591`. Its abstract states a general formalism for the response of an arbitrary solid elastic body to arbitrary metric gravitational-wave perturbations, including multimode transfer and absorption cross sections.

Those sources establish that eigenmode gravitational-antenna response and arbitrary-body modal coupling are historical ingredients. The exact `20/3` Bessel contraction, its `4/3` linewidth consequence, and especially its later use at both endpoints must still be checked against the detailed literature before any novelty statement is made.

## 10. Scope and unresolved issues

Established analytically in this file only for the stated model:

- small nonrelativistic displacements;
- leading STF mass-quadrupole radiation;
- mass-orthogonal linear modes;
- finite retained modal sector, or a summation for which Bessel's inequality is well defined;
- a hard upper frequency `Omega` for the retained modes;
- energy-normalized Markov gravitational ports when translating the modal rates into `Tr(K_g^dagger K_g)`.

Not established here:

- unbounded PDE boundary-control ports;
- genuinely non-Markov matter/radiation continua;
- a globally sharp/saturable body achieving the bound at one common frequency;
- the Experiment-02 TT propagation coefficient;
- the final two-ended `25/12` theorem;
- novelty of the cumulative resource identity.

## 11. Required validation

`numerics/verify_gravitational_endpoint_resource.py` should independently test:

1. the `20/3` pointwise tensor identity for random positions;
2. Bessel/Parseval saturation for complete discrete displacement bases;
3. the inequality for random truncated mass-orthonormal mode sets;
4. invariance under random unitary modal mixing;
5. the `4/3` cumulative linewidth coefficient for random mode frequencies below `Omega`.

Only after that workflow passes should the `4/3` resource be promoted in `CLAIM_LEDGER.md`.
