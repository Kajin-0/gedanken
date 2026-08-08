# Numerical Audit — Thermal Amplifier and Additive Gaussian Noise

**Date:** 2026-08-07  
**Status:** **REPRODUCIBLE INDEPENDENT NUMERICAL AUDIT — EXECUTABLE IMPLEMENTATIONS COMMITTED**

## 1. Purpose

The direct analytic theorem states that for every finite nontrivial binary coherent hybrid input,

$$
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
$$

is NPT iff

$$
\tau>m.
$$

The thermal attenuator case is independently checked with a beam-splitter dilation.

This note audits two other canonical phase-insensitive channels:

1. thermal amplification;
2. unit-gain additive Gaussian noise.

The calculations use explicit Stinespring/random-displacement constructions rather than the coherent-state matrix-element formula used in the proof.

### Committed implementations

- `numerics/thermal_cat_scan.py` — thermal attenuator via beam splitter + thermal environment;
- `numerics/amplifier_cat_scan.py` — thermal amplifier via two-mode-squeezing Stinespring dilation;
- `numerics/additive_noise_cat_scan.py` — additive Gaussian noise via direct random-displacement integration;
- `numerics/README.md` — run instructions, regression values, and convergence rules.

The amplifier and additive-noise calculations were previously documented only as tables. Their actual implementations are now part of the repository.

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

The committed script `numerics/amplifier_cat_scan.py` works in a truncated Fock basis.

For each input bosonic dyad in the hybrid state it

1. tensors with a truncated thermal environment;
2. applies the finite-matrix two-mode-squeezing unitary;
3. traces the environment;
4. assembles the qubit–bosonic output;
5. partially transposes the qubit;
6. computes the full PT spectrum.

A representative non-EB test uses

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

the minimum partial-transpose eigenvalue converges with Fock cutoff $N$ as

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

The newly committed implementation reproduces these values.

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

Thus the above-threshold control behaves as expected from truncation error.

This control is important: a small negative eigenvalue from a finite bosonic truncation is **not** evidence of physical NPT unless it is stable under increasing resolution.

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

The committed script `numerics/additive_noise_cat_scan.py` evaluates this channel directly as a two-dimensional Gaussian integral over displacement operators using tensor-product Gauss–Hermite quadrature, followed by Fock truncation and partial-transpose diagonalization.

This construction is independent of both the coherent-dyad analytic kernel and the amplifier/attenuator dilation code.

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

and sufficiently converged quadrature order, representative minimum PT eigenvalues are

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

Above the exact threshold, the residual negative eigenvalue is reduced to the few-$10^{-6}$ quadrature/truncation floor.

For example at

$$
m=1.3,
$$

raising the Gauss–Hermite integration order reduces a low-order spurious value of approximately

$$
-3.4\times10^{-3}
$$

to

$$
O(10^{-6})
$$

once the displacement integral is converged.

The committed implementation reproduces this behavior.

---

## 7. What the audit establishes

This is not a proof, but it substantially reduces the chance that the coherent theorem is an artifact of

- the thermal-attenuator representation;
- a mistaken amplifier convention;
- the additive-noise edge;
- the coherent-state principal-minor algebra alone.

The phase-insensitive coherent theorem is now supported by

1. direct analytic coherent-kernel proof;
2. separate pure-loss edge proof;
3. an independent line-by-line analytic rederivation in `COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`;
4. thermal attenuator beam-splitter dilation;
5. thermal amplifier two-mode-squeezer simulation;
6. additive random-displacement simulation.

All checked channels behave consistently with

$$
\boxed{
\rho_{\rm binary}^{\rm out}\text{ NPT}
\iff
\tau>m.
}
$$

---

## 8. Reproducibility caution

No finite-dimensional simulation can establish exact positivity at an infinite-dimensional EB boundary by itself.

In particular:

- finite Fock cutoffs can create small false-negative PT eigenvalues;
- high thermal occupation requires larger cutoffs;
- finite Gauss–Hermite order can mimic weak NPT in an additive-noise EB channel;
- near $\tau=m$, the physical witness gap is small and numerical convergence becomes demanding.

Therefore the correct numerical observable is not merely the sign at one cutoff/order, but its **convergence trajectory** as numerical resolution increases.

---

## 9. Updated remaining vulnerability

The previous version of this note identified Schmidt-rank-two prior art as the main unresolved question. That is obsolete: the Fock rank-two novelty was killed by Mele–Lami–Giovannetti prior art.

The dominant remaining uncertainty is now much narrower:

> **Has the exact all-finite-binary-coherent actual-output NPT/EB equivalence, or an algebraically equivalent matched three-element coherent-state PT witness, already been proved elsewhere?**

Current equation-level literature audits of Rigas–Gühne–Lütkenhaus, Namiki, Häseler/Lütkenhaus, Killoran–Häseler–Lütkenhaus, and Kreis–van Loock have found very close predecessors but not this exact completion.

See:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `COHERENT_PRIOR_ART_DEEP_AUDIT.md`
- `CLAIM_LEDGER_POST_MELE_ADDENDUM.md`

---

## 10. Next numerical step

The useful next numerical task is a **controlled near-boundary convergence suite**, not another isolated example.

Recommended offsets are

$$
\epsilon=10^{-1},10^{-2},10^{-3},10^{-4}
$$

on both sides of the exact boundary, with several coherent separations and at least one unequal branch-weight case.

The goal is to map the numerical resolution needed for a stable physical negative eigenvalue as the analytic witness gap tends to zero.
