# Pure-Loss Edge Case for the Direct Binary Coherent Proof

**Timestamp:** 2026-08-07 18:18 EDT  
**Status:** Completes the $m=0$ edge case omitted by the finite optimum $v_*=2\sqrt\tau a/m$ in `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`.

For the symmetric binary coherent hybrid state and the coherent-state principal-minor ratio

$$
R(v)=\frac{|z_v|^2}{p_0p_v},
$$

the general expression before optimizing is

$$
\ln R(v)
=
-4a^2-v^2
+
\frac{4\tau a^2+4\sqrt\tau av+v^2}{m+1}.
$$

For

$$
m=0,
$$

this becomes

$$
\boxed{
\ln R(v)
=4a^2(\tau-1)+4\sqrt\tau\,a\,v.
}
$$

A physical phase-insensitive Gaussian channel with $m=0$ must satisfy $0\le\tau\le1$; this is the quantum-limited pure-loss family (including identity at $\tau=1$).

If

$$
\tau=0,
$$

the output is a replacer/vacuum channel and is entanglement breaking.

If

$$
\tau>0,
$$

choose any finite real coherent analysis amplitude satisfying

$$
\boxed{
v>
\frac{a(1-\tau)}{\sqrt\tau}.
}
$$

Then

$$
\ln R(v)>0,
$$

so

$$
R(v)>1.
$$

Therefore the corresponding finite $2\times2$ principal minor of the partial transpose is negative and the output is NPT.

Hence the direct theorem includes the pure-loss boundary exactly:

$$
\boxed{
 m=0:\qquad
\rho_{AB}\text{ NPT}
\iff
\tau>0.
}
$$

This is exactly the non-entanglement-breaking region of the pure-loss channel.

The apparent divergence

$$
v_*=2\sqrt\tau a/m\to\infty
$$

as $m\to0^+$ means only that the **maximizing** coherent test state moves outward in phase space. It does not mean that an infinite-amplitude test state is required to certify NPT: any finite $v$ above the threshold above is sufficient.

This closes the only singular edge case in the direct coherent-matrix-element proof.