# Minimal Qubit Ancilla for One-Mode Gaussian Entanglement-Breaking Tests

**Date:** 2026-08-07  
**Status:** Immediate operational corollary of the Schmidt-rank-two theorem.

## 1. Ancilla-assisted EB test

An entanglement-breaking channel is defined by whether it destroys entanglement between the channel input and an untouched reference system.

An ancilla-assisted entanglement test therefore prepares

$$
\rho_{RA}
$$

and checks whether

$$
(I_R\otimes\mathcal N_A)(\rho_{RA})
$$

remains entangled.

---

## 2. Dimension one is impossible for an entanglement-preservation test

If

$$
\dim\mathcal H_R=1,
$$

there is no nontrivial bipartite entanglement between $R$ and $A$.

Thus a one-dimensional reference cannot witness the defining property

$$
\text{“this channel preserves entanglement with a reference.”}
$$

Therefore any entanglement-based EB witness requires

$$
\boxed{
\dim\mathcal H_R\ge2.
}
$$

This is a trivial lower bound, but it fixes the absolute minimum possible ancilla size.

---

## 3. Dimension two is sufficient for every non-EB one-mode Gaussian channel

The theorem in `TRUNCATED_TMSV_RANK_TWO_THEOREM.md` and `ONE_MODE_GAUSSIAN_CANONICAL_CLASS_PROOF_AUDIT.md` gives:

For every non-entanglement-breaking one-mode Gaussian channel $\mathcal N$, there exists a pure input

$$
\boxed{
|\Psi\rangle
=\sqrt p|0\rangle_R|\psi_0\rangle_A
+e^{i\phi}\sqrt{1-p}|1\rangle_R|\psi_1\rangle_A
}
$$

with a two-dimensional reference and Schmidt rank exactly two such that

$$
\boxed{
(I_R\otimes\mathcal N_A)(|\Psi\rangle\langle\Psi|)
\text{ is NPT}.
}
$$

Hence

$$
\boxed{
\dim\mathcal H_R=2
}
$$

is sufficient.

Combining necessity and sufficiency gives

$$
\boxed{
\dim\mathcal H_R^{\min}=2
}
$$

for ancilla-assisted entanglement-preservation detection of non-EB behavior in the one-mode Gaussian channel class.

---

## 4. Stronger phase-insensitive statement

For the phase-insensitive canonical family $\Phi_{\tau,m}$, no channel-dependent bosonic basis matching is required.

The single fixed Bell state

$$
\boxed{
|\Phi_2\rangle
=\frac{|0\rangle_R|0\rangle_A
+|1\rangle_R|1\rangle_A}{\sqrt2}
}
$$

satisfies

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Phi_2\rangle\langle\Phi_2|)
\text{ NPT}
\iff
\Phi_{\tau,m}\text{ non-EB}.
}
$$

Thus, in canonical coordinates, the test requires only

- one reference qubit;
- the vacuum–one-photon bosonic subspace;
- one fixed maximally entangled two-qubit-like input.

---

## 5. Important scope qualification

This does **not** mean a qubit ancilla is the experimentally simplest possible way to benchmark every Gaussian channel.

Coherent-state ensemble benchmarks can certify quantum-domain behavior without an entangled ancilla.

The statement is specifically about the minimal reference dimension for an **entanglement-preservation / EB-definition-style test**.

---

## 6. Strongest concise theorem wording

If novelty survives review, the cleanest operational statement may be:

> **One reference qubit is necessary and sufficient to witness that a one-mode Gaussian channel is not entanglement breaking.**

For phase-insensitive channels this can be strengthened to:

> **The fixed vacuum–one-photon Bell state is a complete entanglement-breaking test state.**