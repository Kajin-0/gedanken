# Classical Modal Sum Rule and Quantum-Scope Audit — 2026-08-09

## Purpose

Determine whether the Experiment 02 headline throughput ceiling is intrinsically quantum, or whether it already follows from classical passive linear elasticity plus wave propagation.

The answer is decisive:

> **Within the present compact linear-harmonic matter class, the cumulative endpoint resource bound has a purely classical normal-mode completeness proof. The headline throughput ceiling is therefore a classical passive gravitational-transduction bound. Quantum theory supplies an equivalent oscillator-strength normalization and operational capacity/entanglement corollaries; it is not required to obtain the ceiling itself.**

This strengthens the physics while narrowing the quantum claim.

---

## 1. Classical compact elastic normal modes

Let a compact nonrelativistic elastic body be described by a mass density `rho(r)` and real displacement fields. Use the mass-weighted Hilbert-space inner product

```math
\langle \bm u,\bm v\rangle_\rho
=\int_V\rho(\bm r)\,\bm u(\bm r)\cdot\bm v(\bm r)\,dV.
```

Choose mutually orthogonal elastic normal modes `w_n`, with

```math
\langle \bm w_n,\bm w_m\rangle_\rho
=\mu_n\delta_{nm}.
```

The mode coordinate is defined by

```math
\bm u(\bm r,t)=x_n(t)\bm w_n(\bm r)
```

for a pure mode.

Take the spatial origin at the body center of mass.

---

## 2. Linearized STF quadrupole map

For a small displacement field `u`, the first-order change of the STF mass quadrupole is

```math
\delta Q_{ij}[\bm u]
=\int\rho\left(
 u_i x_j+u_j x_i
-\frac23\delta_{ij}\bm u\cdot\bm x
\right)dV.
```

Define five-tensor-equivalent component fields

```math
(g^{ij})_k(\bm r)
=\delta_{ik}x_j+\delta_{jk}x_i
-\frac23\delta_{ij}x_k.
```

Then

```math
\delta Q_{ij}[\bm u]
=\langle \bm u,\bm g^{ij}\rangle_\rho.
```

For normal mode `n`, define

```math
q_{n,ij}
=\langle \bm w_n,\bm g^{ij}\rangle_\rho.
```

This is precisely the dynamic quadrupole coefficient used in the compact-antenna formalism of Hirakawa, Narihara, and Fujimoto.

---

## 3. Pointwise tensor norm identity

The key algebraic identity is

```math
\boxed{
\sum_{i,j,k=1}^3
|(g^{ij})_k|^2
=\frac{20}{3}r^2.
}
```

One direct expansion is

```math
\sum_{ijk}
\left(
\delta_{ik}x_j+\delta_{jk}x_i
-\frac23\delta_{ij}x_k
\right)^2
=\frac{20}{3}(x^2+y^2+z^2).
```

This coefficient is the classical origin of the same `10/3` STF energy-weighted sum-rule coefficient that appears after quantization.

---

## 4. Bessel/completeness inequality

Normalize the displacement modes as

```math
\bm e_n=\bm w_n/\sqrt{\mu_n}.
```

For each Cartesian STF component field `g^{ij}`, Bessel's inequality gives

```math
\sum_n
|\langle \bm e_n,\bm g^{ij}\rangle_\rho|^2
\le
\|\bm g^{ij}\|_\rho^2.
```

Summing over `i,j`,

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le
\sum_{ij}\int\rho|\bm g^{ij}|^2dV.
```

Using the pointwise identity,

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le
\frac{20}{3}I,
}
```

where

```math
I=\int\rho r^2dV
```

is the internal mass inertia moment about the center of mass.

### Equality condition

Equality holds if the chosen orthonormal normal-mode set is complete for the displacement-field components of every `g^{ij}` relevant to the unconstrained displacement space. For any retained subset of modes, constrained mechanical subspace, or band truncation, the Bessel form is the safe statement and remains an upper bound.

Rigid translations do not create a problem when the origin is the center of mass because the quadrupole-gradient fields are orthogonal to constant translations. Infinitesimal rigid rotations are different: for an anisotropic body they generally rotate the static quadrupole and therefore need not be orthogonal to the quadrupole-gradient fields. If free-body rotational zero modes are omitted from the retained positive-frequency elastic sector, the Bessel bound only becomes looser. If rotational motion is constrained into a finite-frequency mode, it belongs in the retained modal sum in the usual way.

---

## 5. Classical gravitational effective-area sum rule

Hirakawa et al. define the single-mode gravitational effective area

```math
A_{Gn}
=\frac{2\,q_n:q_n}{M\mu_n}.
```

Therefore

```math
M A_{Gn}
=2\frac{q_n:q_n}{\mu_n}.
```

The Bessel inequality immediately yields the classical modal oscillator-strength sum rule

```math
\boxed{
\sum_n M A_{Gn}
\le
\frac{40}{3}I.
}
```

For a retained subset `S`, including all quadrupole-active modes below an operating ceiling,

```math
\boxed{
\sum_{n\in S} M A_{Gn}
\le
\frac{40}{3}I.
}
```

No Planck constant and no quantum commutator is required.

---

## 6. Recover the gravitational linewidth resource classically

The independently checked Hirakawa-to-quantum normalization is

```math
\kappa_{g,n}
=\frac{G M A_{Gn}\omega_n^4}{10c^5}.
```

The same quantity is the classical modal gravitational energy-decay rate. Hirakawa's emitted power is

```math
P_n=\frac{G}{5c^5}M A_{Gn}\omega_n^4\,\langle T_n\rangle,
```

and for a harmonic mode the total cycle-averaged energy is `E_n=2<T_n>`, giving `P_n/E_n = G M A_Gn omega_n^4/(10c^5)`.

For retained modes with

```math
0<\omega_n\le\Omega,
```

we have

```math
\sum_n\kappa_{g,n}
=\frac{G}{10c^5}
\sum_n M A_{Gn}\omega_n^4
\le
\frac{G\Omega^4}{10c^5}
\sum_n M A_{Gn}.
```

Hence

```math
\boxed{
\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}I\Omega^4.
}
```

This is exactly the Experiment 02 endpoint resource ceiling previously obtained from the quantum mass-quadrupole EWSR.

---

## 7. Equivalence to the quantum EWSR

Quantizing each harmonic coordinate gives

```math
Q_{ij}^{01}
=q_{n,ij}\sqrt{\frac{\hbar}{2\mu_n\omega_n}}.
```

Therefore

```math
\omega_n Q^{01}:Q^{10}
=\frac{\hbar}{2}\frac{q_n:q_n}{\mu_n}.
```

Summing the classical completeness relation yields

```math
\sum_n\omega_nQ^{01}:Q^{10}
\le
\frac{10}{3}\hbar I.
```

For a complete normal-mode basis this is the same coefficient as the coordinate-quadrupole double-commutator EWSR.

Thus, in the linear-harmonic class,

```text
classical modal completeness
<-> classical gravitational effective-area sum rule
<-> quantum quadrupole EWSR
```

are three representations of the same oscillator-strength constraint.

The EWSR remains useful because it connects naturally to a broader quantum spectral-measure language, but it is not required to prove the present linear-bosonic endpoint ceiling.

---

## 8. Classical status of the passive H2 cut set

The selected-port H2 inequality used in Experiment 02 is algebraic passive linear-systems theory. The energy-normalized complex-envelope equations

```math
A=-iH-\frac12K^\dagger K
```

and the Lyapunov identity underlying

```math
\|S_{g\leftarrow u}\|_2^2
\le\operatorname{Tr}(K_g^\dagger K_g)
```

apply equally to a classical passive coupled-mode realization. Bosonic input-output notation is convenient but not essential to the inequality.

Therefore the endpoint cut set is also not intrinsically quantum.

---

## 9. Classical status of the `25/16` propagation ceiling

Hirakawa's compact gravitational antenna directivity law is historical and reaches

```math
D_{\max}=\frac52.
```

For two matched reciprocal compact quadrupole antennas, the standard far-field normalized antenna-transfer factor is

```math
D_A D_B
\left(\frac{\lambda}{4\pi R}\right)^2.
```

Using

```math
D_A=D_B=\frac52,
\qquad
\lambda=\frac{2\pi}{k},
```

gives

```math
\boxed{
D_A D_B
\left(\frac{\lambda}{4\pi R}\right)^2
=\frac{25}{16(kR)^2}.
}
```

This is the same leading compact TT propagation ceiling obtained from normalized one-graviton angular modes.

The TT derivation remains valuable because it fixes the gravitational polarization/tensor normalization directly and extends naturally to complex transition tensors, but the leading propagation ceiling is not intrinsically quantum either.

---

## 10. Consequence for the headline theorem

All three ingredients of the physical ceiling now possess classical derivations:

```text
passive H2 cut set                  classical linear systems
endpoint cumulative resource       classical modal completeness
25/16 propagation ceiling           classical reciprocal antenna transfer
```

Therefore

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B)
}
```

is fundamentally a **classical passive gravitational-transduction throughput bound** within the present linear-harmonic compact wave-zone class.

There is no `\hbar` in the final theorem because no quantum resource is required to establish it.

---

## 11. What remains quantum

Quantum theory remains essential for several downstream statements:

1. interpreting the same classical oscillator-strength rate as a one-graviton spontaneous-emission linewidth;
2. embedding the passive scattering transfer into a bosonic quantum channel;
3. distinguishing finite-use entanglement transfer from asymptotic capacity;
4. deriving the stationary vacuum pure-loss corollaries

```math
Q_1=0
```

when all transmission eigenvalues are at most `1/2`, and

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2(1-\eta_{\max})}.
```

These should be presented as **quantum-information consequences of a classical physical throughput bound**, not as the foundation of the bound itself.

---

## 12. Publication consequence

The manuscript title and framing should change.

Recommended title:

> **Passive Throughput Bounds for Propagating Gravitational Transduction**

The abstract should state explicitly that the main theorem is classical and that quantum-channel consequences are corollaries.

The material-resource section should lead with the classical modal completeness theorem and present the EWSR as an equivalent quantum representation/cross-check rather than the sole derivation.

This reframing strengthens the paper because

- it removes unnecessary dependence on quantum-system formalism from the headline physics;
- it connects directly to historical gravitational antenna theory;
- it makes the disappearance of `\hbar` conceptually transparent rather than accidental;
- it isolates exactly where genuinely quantum claims begin.

---

## 13. Novelty implication

This result further narrows the novelty boundary.

Do not claim novelty for

- the EWSR coefficient as a specifically quantum constraint;
- a quantum origin of the passive throughput ceiling;
- quantization as necessary to derive the endpoint bound.

The remaining candidate contribution is instead

> **the classical gravity-specific cumulative two-ended closure itself:** a passive end-to-end spectral-area bound whose endpoint gravitational oscillator strengths are simultaneously bounded by total mechanical inertia and whose direct wave-zone propagation is bounded by compact quadrupole geometry.

No inspected source has yet been found stating the complete final inertia-controlled two-ended theorem.

---

## Verdict

```text
CLASSICAL MODAL SUM RULE:             PROVED
SUM_n M A_Gn <= (40/3) I:             PROVED
EWSR ENDPOINT CEILING:                CLASSICALLY REPRODUCED
25/16 LEADING PROPAGATION CEILING:    CLASSICAL RECIPROCAL INTERPRETATION
HEADLINE THROUGHPUT THEOREM:          CLASSICAL WITHIN DECLARED CLASS
QUANTUM CAPACITY/ENTANGLEMENT:        DOWNSTREAM COROLLARIES
"QUANTUM" IN PAPER TITLE:             REMOVE
PHYSICS CONFIDENCE:                   INCREASED
NOVELTY BOUNDARY:                     NARROWER
THEOREM BROADENING:                   DO NOT DO
```
