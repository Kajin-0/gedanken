# Checkpoint — Rank-Two Gaussian Theorem + Storage Audit

**Date:** 2026-08-07

## 1. Strongest standalone theorem candidate

For every non-entanglement-breaking one-mode Gaussian channel $\mathcal N$, there exists a finite Schmidt-rank-two pure input

$$
|\Psi_G\rangle
=\sqrt p|0\rangle|\psi_0\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\psi_1\rangle,
$$

where $|\psi_0\rangle$ and $|\psi_1\rangle$ are distinct displaced copies of one finite-covariance pure Gaussian state, such that

$$
(I\otimes\mathcal N)(|\Psi_G\rangle\langle\Psi_G|)
$$

is NPT.

Conversely EB channels cannot produce such an output by definition.

### Canonical-class audit

- $\det K=0$: every physical one-mode Gaussian channel is EB by the Gaussian EB decomposition criterion.
- $\det K<0$: every physical orientation-reversing/phase-conjugating channel is EB; explicit noise splitting was derived.
- $\det K>0$, full-rank noise: Gaussian-unitarily equivalent to a phase-insensitive canonical channel, so the direct binary-coherent theorem applies.
- Gaussian unitary boundary: trivial.
- singular $B_1$ rank-one noise: covered by a finite post-processing regularization plus PPT monotonicity.

### Constructive $B_1$

For

$$
Y_{B_1}=\operatorname{diag}(b,0),
$$

choose any

$$
0<y<1,
$$

add finite noise

$$
\epsilon=y^2/b
$$

in the clean quadrature, and canonicalize the regularized channel to unit-gain isotropic additive noise $yI$.

The required matched input squeeze is

$$
\boxed{
r=\frac12\ln(b/y),
}
$$

finite for every finite $b$ and $y$.

The regularized output is NPT for a finite binary coherent canonical input. Since local post-processing cannot turn a PPT state into NPT, the original $B_1$ output was already NPT for the pulled-back finite squeezed-coherent pair.

Files:

- `../COMPLETE_ONE_MODE_GAUSSIAN_TWO_BRANCH_PROBE_THEOREM.md`
- `../ONE_MODE_GAUSSIAN_CANONICAL_CLASS_PROOF_AUDIT.md`
- `../CONSTRUCTIVE_B1_FINITE_PROBE.md`
- `../PAPER_CORE_SCHMIDT_RANK_TWO_GAUSSIAN_EB.md`

## 2. Prior-art boundary for the rank-two result

Finite-energy Gaussian EB testing is established prior art. De Pasquale et al. show that any finite nonzero TMSV can replace the formal infinite-energy maximally entangled state as a Gaussian EB test.

However every finite-squeezing TMSV has infinite Schmidt rank.

The present candidate reduction is therefore specifically

$$
\boxed{
\text{infinite-Schmidt-rank finite-energy Gaussian test}
\to
\text{Schmidt-rank-two matched Gaussian-branch test}.
}
$$

Targeted searches have not located an equivalent one-mode Gaussian theorem, but novelty remains unverified.

File:

- `../NOVELTY_AUDIT_SCHMIDT_RANK_TWO_GAUSSIAN_PROBE.md`

## 3. $25/16$ gravitational storage normalization

The aligned plus-quadrupole far-zone state-storage coefficient is now supported by three routes:

### Retarded Green function

$$
\Sigma_{AB}^{R}
\to
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_{g,A}\kappa_{g,B}},
$$

so

$$
\eta_{\rm store}=25/[16(kR)^2].
$$

### Power-flow / partial-wave audit

The plus quadrupole has on-axis angular power fraction

$$
5/(8\pi),
$$

and one critically coupled $l=2$ channel has

$$
\sigma_{\rm abs,max}^{(2)}=5\pi/(2k^2).
$$

Therefore

$$
\frac{5}{8\pi R^2}\frac{5\pi}{2k^2}
=\frac{25}{16(kR)^2}.
$$

### Electromagnetic dipole control

The analogous electric-dipole result is

$$
\frac{3}{8\pi R^2}\frac{3\pi}{2k^2}
=\frac{9}{16(kR)^2},
$$

matching the standard normalized far-zone electromagnetic Green coupling.

The four-times-larger gravitational coefficient corresponds to the unitary scattering cross section, not coherent storage.

File:

- `../STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`

## 4. Current publication split

The project now naturally separates into two possible papers.

### Paper A — quantum information

**Schmidt-Rank-Two Probes Suffice to Detect Entanglement Breaking in One-Mode Gaussian Channels**

This is mathematically cleaner and independent of gravity.

### Paper B — gravitational application

Use the binary/rank-two theorem as a lemma in the explicit source-resolved retarded gravitational receiver problem.

## 5. Strongest next actions

1. deeper Schmidt-number / ancilla-dimension literature audit for Paper A;
2. independent expert/theorem rederivation;
3. canonical TT-mode normalization audit for the gravity $25/16$ coefficient if further confidence is required;
4. source actuator stress-energy conservation audit;
5. only then convert either paper core to a manuscript.