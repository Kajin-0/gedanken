# Research Question — Experiment 02

## Primary question

For two separated compact passive nonrelativistic matter systems coupled only through propagating weak-field gravity, is there a useful frequency-integrated upper bound on coherent source-to-receiver transfer that is independent of passive quality factor, resonance count, and internal mode mixing?

The quantity to be investigated is a selected-port transfer matrix `T(omega)` and a spectral-area metric of the form

```math
\Gamma_{\rm coh}
=\frac{1}{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]\,d\omega.
```

This definition itself must be checked for normalization, physical interpretation, and the precise conditions under which it is the right throughput metric.

## Candidate target

A prior conversational exploration suggested, without reliable repository provenance, the candidate scaling

```math
\Gamma_{\rm coh}
\stackrel{?}{\lesssim}
C\,\frac{G\omega^2}{c^3R^2}\min(I_A,I_B),
```

with a possible narrowband coefficient `C = 25/12`.

This is a **target to test, not a theorem to reproduce**.

## Questions that must be answered independently

1. Can passivity reduce the integrated end-to-end transfer to a cut involving only the gravitational coupling resources of the two endpoints?
2. Does compact quadrupolar matter possess a cumulative gravitational coupling resource bounded by a simple mass-inertia functional?
3. What is the correctly normalized operator norm of separated compact TT propagation, including all factors of `2`, `pi`, polarization normalization, and the distinction between field amplitude and stored/absorbed power?
4. Does combining the endpoint and propagation statements actually yield an inertia-only two-ended bound?
5. Can countably many passive modes, degeneracies, coherent mode mixing, or repeated passive returns evade the proposed ceiling?
6. Is any resulting statement already contained, explicitly or implicitly, in gravitational-antenna, resonant-mass, passive-network, or general wave-channel literature?

## Success criterion

Experiment 02 becomes a real theorem project only if an independent derivation produces a precise statement with explicit assumptions and the result survives:

- independent normalization checks;
- hostile counterexample attempts;
- numerical tests where applicable;
- primary-source prior-art comparison;
- a second derivation or equivalent physical normalization.

## Failure criterion

A clean failure is scientifically acceptable and should be recorded if any of the following occurs:

- no finite inertia-only bound exists in the stated class;
- the candidate coefficient or scaling is wrong;
- the result depends irreducibly on additional material/port parameters;
- an allowed passive architecture produces a counterexample;
- the complete theorem is already established prior art;
- the required assumptions become so restrictive that the result loses physical significance.

The objective is to learn which statement is true, not to preserve the candidate formula.
