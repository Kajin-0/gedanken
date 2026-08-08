# Numerical Audit — Thermal Amplifier and Additive Gaussian Noise

**Date:** 2026-08-07  
**Status:** Independent finite-dimensional numerical audit of the phase-insensitive binary coherent NPT/EB theorem. This is not part of the proof; it is a check against implementation-independent failure modes.

## 1. Purpose

The direct analytic theorem states that for every finite nontrivial binary coherent hybrid input,

$$
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
$$

is NPT iff

$$
\tau>m.
$$

The thermal attenuator case had already been checked independently using a beam-splitter dilation.

This note audits two other canonical phase-insensitive channels:

1. thermal amplification;
2. unit-gain additive Gaussian noise.

The calculations use direct Stinespring/random-displacement simulations rather than the coherent-state matrix-element formula used in the proof.

---

## 2. Thermal amplifier dilation

A thermal amplifier of gain $G>1$ can be represented by a two-mode squeezer acting on

- the signal mode;
- an environment mode in a thermal state of occupation $n_E$.

The Heisenberg transformation is

$$
a_{\rm out}
=\sqrt G\,a_{\rm in}
+\sqrt{G-1}\,e^\dagger.
$$

The vacuum-output occupation is

$$
\boxed{
m=(G-1)(n_E+1).}
$$

Since

$$
\tau=G,
$$

the EB boundary is

$$
(G-1)(n_E+1)\ge G,
$$

or

$$
\boxed{
n_E\ge\frac1{G-1}.}
$$

---

## 3. Amplifier simulation

The simulation was performed in a truncated Fock basis.

For each input bosonic dyad in the hybrid state,

1. tensor with a truncated thermal environment;
2. apply the exact finite-matrix two-mode-squeezing unitary;
3. trace the environment;
4. assemble the qubit–bosonic output;
5. partially transpose the qubit;
6. compute the minimum eigenvalue.

A representative non-EB test used

$$
G=1.5,
$$

$$
n_E=0.5,
$$

for which the EB threshold is

$$
n_E^{\rm EB}=2.
$$

With coherent branches

$$
|\pm0.4\rangle,
$$

the minimum partial-transpose eigenvalue converged with Fock cutoff $N$ as

$$
\begin{array}{c|c}
N&\lambda_{\min}(\rho^{T_A})\\
\hline
10&-0.0585654\\
12&-0.0585734\\
14&-0.0585749\\
16&-0.0585752\\
18&-0.0585752
\end{array}
$$

The negative value is stable and rapidly converged.

---

## 4. Above-threshold amplifier control

For

$$
G=1.5,
$$

$$
n_E=3,
$$

the exact infinite-dimensional channel is EB because

$$
3>2.
$$

The truncated simulation initially produces a small spurious negative PT eigenvalue because a finite Fock truncation of a high-occupation two-mode-squeezing dilation does not preserve the exact infinite-dimensional EB structure.

The residual decreases monotonically as the cutoff increases:

$$
\begin{array}{c|c}
N&\lambda_{\min}(\rho^{T_A})\\
\hline
10&-6.22\times10^{-3}\\
12&-3.79\times10^{-3}\\
14&-2.53\times10^{-3}\\
16&-1.68\times10^{-3}\\
18&-1.11\times10^{-3}
\end{array}
$$

The trend is toward the exact EB value

$$
\lambda_{\min}\to0^-.
$$

Thus the above-threshold control behaves exactly as expected from truncation error.

---

## 5. Additive Gaussian noise simulation

For the unit-gain additive-noise channel,

$$
\tau=1,
$$

and

$$
\boxed{
\Phi_m(\rho)
=\int\frac{d^2z}{\pi m}
e^{-|z|^2/m}
D(z)\rho D^\dagger(z).
}
$$

The output occupation generated from vacuum is

$$
m.
$$

The EB boundary is therefore

$$
\boxed{m=1.}
$$

The channel was simulated directly as a two-dimensional Gaussian integral over displacement operators using Gauss–Hermite quadrature, followed by Fock truncation and partial-transpose diagonalization.

---

## 6. Additive-noise results

For coherent branches

$$
|\pm0.35\rangle,
$$

Fock cutoff

$$
N=16,
$$

and sufficiently converged quadrature order, representative minimum PT eigenvalues were

$$
\begin{array}{c|c|c}
m&\text{exact EB status}&\lambda_{\min}(\rho^{T_A})\\
\hline
0.70&\text{non-EB}&-2.228\times10^{-2}\\
0.95&\text{non-EB}&-2.581\times10^{-3}\\
1.05&\text{EB}&-2.74\times10^{-6}\\
1.30&\text{EB}&-4.89\times10^{-6}
\end{array}
$$

The below-threshold negative eigenvalues are orders of magnitude above numerical error.

Above the exact threshold, the residual negative eigenvalue is reduced to the few-$10^{-6}$ numerical quadrature/truncation floor.

For example at

$$
m=1.3,
$$
raising the Gauss–Hermite integration order changed the spurious value from approximately

$$
-3.4\times10^{-3}
$$

at low integration order to

$$
O(10^{-6})
$$

once the displacement integral was converged.

---

## 7. What the audit establishes

This is not a proof, but it substantially reduces the chance that the analytic theorem is an artifact of

- the thermal-attenuator representation;
- a mistaken amplifier convention;
- the additive-noise edge;
- the coherent-state principal-minor algebra alone.

The phase-insensitive theorem is now supported by

1. direct analytic coherent-kernel proof;
2. explicit pure-loss edge analysis;
3. independent thermal attenuator dilation;
4. independent thermal amplifier Stinespring simulation;
5. independent additive random-displacement simulation.

All checked channels behave consistently with

$$
\boxed{
\rho_{\rm binary}^{\rm out}\text{ NPT}
\iff
\tau>m.
}
$$

---

## 8. Remaining vulnerability

The main unresolved issue is now **prior art**, not internal consistency.

The strongest next step remains a deep literature review of Schmidt-rank-two / finite-ancilla sufficiency for one-mode Gaussian entanglement-breaking tests.