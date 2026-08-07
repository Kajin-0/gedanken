# Exact Finite-Cat Thermal Entanglement Witness

**Timestamp:** 2026-08-07 17:00 EDT  
**Status:** Analytic consequence of `EXACT_FINITE_CAT_THERMAL_THEOREM.md`; independently checked against a direct truncated beam-splitter thermal dilation.

## 1. Purpose

The exact finite-cat theorem proves that

$$
\rho_{AB}\text{ is NPT}
\iff
\eta>m,
\qquad
m=(1-\eta)\bar n,
$$

for every finite nonzero coherent branch amplitude in

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle+|1\rangle|-a\rangle}{\sqrt2}.
$$

The proof also supplies an explicit negative vector of the partial transpose. Turning that vector back into an entanglement witness gives a single parameter-matched observable that detects the state **everywhere in the non-entanglement-breaking region**.

This is directly relevant to the 2012 Kreis–van Loock analysis of the same state and thermal channel, where a finite-order moment witness detects only part of the non-EB region.

---

## 2. Definitions

Assume $a>0$ real without loss of generality. Define

$$
\boxed{m=(1-\eta)\bar n,}
$$

and, for $m>0$,

$$
\boxed{
A
=\exp\left(\frac{2\eta a^2}{m^2}\right),
}
$$

$$
\boxed{
v
=\frac{2\sqrt\eta\,a}{m}.
}
$$

Also define

$$
P
=\frac1{m+1}
\exp\left[-\frac{\eta a^2}{m+1}\right],
$$

and

$$
q
=\exp\left[
\frac{2a^2}{m}(\eta-m)
\right].
$$

---

## 3. Exact negative vector

The domain-safe proof of the finite-cat theorem gives the unnormalized vector

$$
|x\rangle
=P^{-1/2}
\left(
|0\rangle_A|0\rangle_B
-
A|1\rangle_A|v\rangle_B
\right).
$$

Its norm is

$$
\langle x|x\rangle
=P^{-1}(1+A^2).
$$

Therefore define the normalized hybrid witness vector

$$
\boxed{
|\omega\rangle
=
\frac{
|0\rangle_A|0\rangle_B
-A|1\rangle_A|v\rangle_B
}
{\sqrt{1+A^2}}.
}
$$

Directly from the factorized partial-transpose proof,

$$
\boxed{
\langle\omega|
\rho_{AB}^{\Gamma_A}
|\omega\rangle
=
\frac{P(1-q)}{1+A^2}.
}
$$

Hence

$$
\boxed{
\langle\omega|ho^{\Gamma_A}|\omega\rangle<0
\iff
q>1
\iff
\eta>m.
}
$$

Using $m=(1-\eta)\bar n$,

$$
\boxed{
\langle\omega|ho^{\Gamma_A}|\omega\rangle<0
\iff
\eta>\frac{\bar n}{\bar n+1}.
}
$$

This detects the exact finite-cat NPT boundary.

---

## 4. Ordinary entanglement-witness operator

Define

$$
\boxed{
W_{a,\eta,\bar n}
=
\left(
|\omega\rangle\langle\omega|
\right)^{\Gamma_A}.
}
$$

For every separable state $\sigma_{AB}$,

$$
\operatorname{Tr}
[W_{a,\eta,\bar n}\sigma_{AB}]
\ge0,
$$

because $\sigma_{AB}^{\Gamma_A}\succeq0$ for every separable state.

For the thermal-channel output of the finite hybrid cat,

$$
\boxed{
\operatorname{Tr}
[W_{a,\eta,\bar n}\rho_{AB}]
=
\frac{P(1-q)}{1+A^2}.
}
$$

Therefore this single parameter-matched witness is negative **if and only if** the output is on the NPT side of the thermal-channel boundary.

For this state family, it closes the entire gap between a sufficient witness and the exact channel threshold.

---

## 5. Rigorous negativity lower bound

Because the minimum eigenvalue of $\rho^{\Gamma_A}$ cannot exceed any normalized Rayleigh quotient,

$$
\lambda_{\min}(\rho^{\Gamma_A})
\le
\frac{P(1-q)}{1+A^2}.
$$

Whenever $q>1$, the negativity therefore obeys

$$
\boxed{
\mathcal N(\rho_{AB})
\ge
\frac{P(q-1)}{1+A^2}.
}
$$

Explicitly,

$$
\boxed{
\mathcal N
\ge
\frac{
\dfrac1{m+1}
\exp[-\eta a^2/(m+1)]
\left\{
\exp[2a^2(\eta-m)/m]-1
\right\}
}
{
1+\exp[4\eta a^2/m^2]
}.
}
$$

This lower bound is generally not tight—especially for large cat amplitudes—but it is analytic, strictly positive everywhere above the exact NPT threshold, and vanishes continuously at the boundary.

Near the boundary, write

$$
\delta=\eta-m>0.
$$

Then

$$
q-1
=\frac{2a^2}{m}\delta+O(\delta^2),
$$

so the witness certifies at least linear onset,

$$
\boxed{
\mathcal N
\gtrsim
\frac{2a^2P}
{m(1+A^2)}
\delta.
}
$$

The exact negativity can turn on more strongly than this lower bound; the formula here is only a guaranteed amount.

---

## 6. Independent numerical audit

The analytic expectation above was independently checked using a direct finite-Fock simulation of:

1. the input hybrid cat;
2. a thermal environment state;
3. the exact beam-splitter unitary implementing the attenuator;
4. tracing out the environment;
5. direct partial transpose of the source qubit.

Representative comparisons of

$$
\langle\omega|\rho^{\Gamma_A}|\omega\rangle
$$

with the analytic formula agreed to numerical precision for multiple cat amplitudes, thermal occupations, and transmissivities on both sides of the EB boundary. Below the exact EB boundary, tiny apparent negative eigenvalues at insufficient Fock cutoffs disappear with convergence and are expected because the exact channel is entanglement breaking.

The existing reproducible thermal-cat scan remains in `numerics/thermal_cat_scan.py`; a dedicated witness-check script can be added if needed for the paper supplement.

---

## 7. Relation to prior hybrid-entanglement witnessing

Kreis & van Loock (Phys. Rev. A 85, 032307, 2012) consider the same ideal hybrid state

$$
\frac{|0\rangle|\alpha\rangle+|1\rangle|-\alpha\rangle}{\sqrt2}
$$

and the same one-sided thermal beam-splitter channel.

Their Shchukin–Vogel determinant gives a sufficient region of thermal entanglement detection and has an amplitude-dependent optimum. Their footnote [47] explicitly observes that comparison with the thermal entanglement-breaking boundary shows their witness may miss entangled states below that boundary.

The present witness is designed from the exact partial-transpose structure rather than a fixed low-order moment determinant and, if the proof survives independent review, detects the complete non-EB region for every finite cat amplitude.

This is the clearest current mathematical distinction from the closest known predecessor.

---

## 8. Gravity interpretation

At receiver time $t$, substitute

$$
\eta\rightarrow\eta_f(t),
\qquad
m\rightarrow m(t).
$$

Then the witness becomes a time-dependent source-receiver observable

$$
W(t)
=
\left(|\omega(t)\rangle\langle\omega(t)|\right)^{\Gamma_A}
$$

whose expectation changes sign exactly at the NPT front in the ideal thermal receiver model:

$$
\boxed{
\operatorname{Tr}[W(t)\rho_{AB}(t)]<0
\iff
\eta_f(t)>m(t).
}
$$

Thus the causal-front theorem has, in principle, a matched witness rather than requiring complete state tomography.

The practical cost is that $|\omega(t)\rangle$ depends on channel parameters and may involve a large coherent receiver displacement near low thermal occupation. It is therefore an exact theoretical witness, not yet an optimized experimental measurement protocol.

---

## 9. Next step

1. Search for an equivalent exact parameter-matched hybrid witness in prior literature.
2. Derive a more experimentally economical witness that approaches this exact boundary without requiring projection onto a large coherent superposition.
3. Optimize the analytic negativity lower bound over test vectors $|\phi\rangle$ in the factorized proof.
4. Map $a,\eta,m$ explicitly onto the gravitational source difference-mode amplitude, causal receiver capture, and receiver bath parameters.
