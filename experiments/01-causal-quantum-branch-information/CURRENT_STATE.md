# Current State — Experiment 01

**Last updated:** 2026-08-07 14:15 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

Canonical recovery point. Detailed derivations: `SCALAR_MATCHED_HISTORY.md`, `GRAVITY_QUADRUPOLE_LIMIT.md`, `TIDAL_RECEIVER.md`, `EXACT_WEYL_CROSSOVER.md`, `PROGRESS_LOG.md`, and `checkpoints/`.

## Core witness

For the balanced source-path qubit,

$$
\rho_{AB}=\frac12
\begin{pmatrix}
\rho_L & \Xi\\
\Xi^\dagger & \rho_R
\end{pmatrix},
$$

define

$$
C_\Xi=\|\Xi\|_1,
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1.
$$

Every balanced separable state obeys

$$
C_\Xi^2+D_B^2\le1.
$$

Preferred logarithmic form:

$$
\boxed{
\mathcal M_\Xi
=\chi_B-2\Gamma_\Xi,
\quad
\chi_B=-\ln(1-D_B^2),
\quad
\Gamma_\Xi=-\ln C_\Xi.
}
$$

$$
\mathcal M_\Xi>0
$$

certifies source-probe entanglement. For pure conditional global histories,

$$
C_\Xi=F(\rho_E^L,\rho_E^R),
$$

so $C_\Xi$ is the fidelity of the unobserved complementary records.

## Causality

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0
\qquad T<R/c.
$$

Define

$$
T_*(R)=\inf\{T:\mathcal M_\Xi(T,R)>0\};
$$

locality requires $T_*(R)\ge R/c$.

## Scalar matched-history result

For a source control history $u$,

$$
\mathcal M_\Xi[u]
=\langle u,(K_B-N_T)u\rangle,
\qquad
K_B=|r_T\rangle\langle r_T|.
$$

If $N_T$ is invertible on the relevant support,

$$
\boxed{
\eta_T=\langle r_T,N_T^{-1}r_T\rangle>1
}
$$

is equivalent to the existence of an optimized positive-margin history in the toy model, with

$$
u_{\rm opt}\propto N_T^{-1}r_T.
$$

In the narrow-band damped limit,

$$
\boxed{
\mathcal C_{\rm hist}
=\frac{|\mathcal R_B|^2}{\kappa_BS_E}>1
}
$$

is the strong-history cooperativity threshold.

## Clean GR receiver: geodesic deviation

A self-contained freely falling receiver does not measure uniform gravitational acceleration. In Fermi normal coordinates the leading local coupling is

$$
H_{\rm curv}
=\frac{\mu_Bc^2}{2}R_{0i0j}\xi^i\xi^j.
$$

For a differential mode with equilibrium baseline $L_B$ and quantum coordinate $x_B$,

$$
\boxed{
H_{\rm drive}
=\mu_BL_B\mathcal E_{nn}x_B,
\qquad
\mathcal E_{ij}=c^2R_{0i0j}.
}
$$

This supersedes the earlier single-force receiver as the canonical local GR detector.

## Exact retarded quadrupole crossover

Choose the plus-type source quadrupole

$$
\Delta Q_{xx}=q(t),
\qquad
\Delta Q_{yy}=-q(t),
$$

place the receiver on the $z$ axis, and orient its differential baseline along $x$.

Direct evaluation of the gauge-invariant linearized Riemann tensor gives

$$
\boxed{
\Delta\mathcal E_{xx}(t,R)
=
-\frac{G}{R^5}
\left[
3q
+\frac{3R}{c}\dot q
+\frac{3R^2}{c^2}\ddot q
+\frac{2R^3}{c^3}q^{(3)}
+\frac{R^4}{c^4}q^{(4)}
\right]_{t-R/c}.
}
$$

For $q(t)=q_\omega e^{-i\omega t}$ and

$$
\epsilon=\frac{\omega R}{c},
$$

$$
\boxed{
\Delta\mathcal E_{xx}(\omega,R)
=-\frac{Gq_\omega}{R^5}
P(\epsilon)e^{i\omega R/c},
}
$$

with

$$
\boxed{
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
}
$$

and

$$
\boxed{
|P(\epsilon)|^2
=\epsilon^8-2\epsilon^6+3\epsilon^4-9\epsilon^2+9.
}
$$

This is the first single analytic transfer function covering static near field, induction zone, and gravitational-wave curvature.

Consistency limits:

$$
\epsilon\ll1:
\quad
\mathcal E_{xx}\to-3Gq/R^5,
$$

$$
\epsilon\gg1:
\quad
\mathcal E_{xx}\to-Gq^{(4)}/(c^4R).
$$

## Exact local history cooperativity for this geometry

For this plus quadrupole,

$$
Q_{ij}Q_{ij}=2q^2,
$$

so the clean coherent outgoing-graviton record spectrum is

$$
S_G(\omega)
\simeq
\frac{2G}{5\hbar c^5}\omega^5
$$

within the stated Fourier convention.

Define

$$
\nu_G
=\frac{G\mu_BL_B^2Q_B\omega_B^3}{c^5}.
$$

Then the complete near-to-wave local-receiver strong-history cooperativity is

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}(\epsilon)
=
\frac54\nu_G
\frac{|P(\epsilon)|^2}{\epsilon^{10}}.
}
$$

Therefore

$$
\epsilon\ll1:
\quad
\mathcal C_{\rm hist}^{(G)}
\simeq\frac{45}{4}\nu_G\epsilon^{-10},
$$

while

$$
\epsilon\gg1:
\quad
\mathcal C_{\rm hist}^{(G)}
\simeq\frac54\nu_G\epsilon^{-2}.
$$

At the dynamical causal crossover,

$$
|P(1)|^2=2,
$$

so

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}(1)
=\frac52\nu_G.
}
$$

For laboratory receivers, $\nu_G$ is fantastically small. Example: two approximately $1\,\mathrm g$ receiver masses ($\mu_B\simeq0.5\,\mathrm g$), $L_B=0.1\,\mathrm m$, $f_B=1\,\mathrm{Hz}$, $Q_B=10^8$ give

$$
\nu_G\approx3.4\times10^{-48},
$$

hence

$$
\mathcal C_{\rm hist}^{(G)}(\epsilon=1)
\sim8.5\times10^{-48}.
$$

The radiation-only strong-witness threshold occurs deep in the near zone, around

$$
\epsilon_c\sim2.3\times10^{-5}
$$

for this illustrative parameter set.

## Interpretation: local strong-witness limitation

This is **not a no-go theorem for gravity-mediated entanglement**. $\mathcal M_\Xi>0$ is a sufficient strong witness, and the current complement model counts clean outgoing radiation but does not yet fully resolve dressing/soft sectors.

What is now quantitatively established in this model is:

- deep near zone: a local differential receiver can outperform clean radiative branch leakage because the field is mainly reactive;
- around $\epsilon\sim1$: order-unity retardation is dynamically available, but a local receiver captures only an $O(\nu_G)$ fraction in the strong-history sense;
- wave zone: local capture remains inefficient while branch information is distributed into outgoing gravitational modes.

An ideal mode-matched enclosing quantum receiver can evade the **local mode-capture** issue. In a pure-loss benchmark the strong witness requires collection efficiency $\tau_{\rm ch}>1/2$.

## Literature boundary

The following ingredients are established and are not novelty claims:

- Fermi-normal curvature coupling of localized quantum systems;
- geodesic-deviation GW detection;
- canonical retarded multipole fields;
- quadrupole radiation;
- coherence/distinguishability and pure-loss channel bounds;
- retarded gravitationally induced entanglement;
- geodesic-deviation tests of classical-quantum gravity (Hirotani & Matsumura, PRD 114, 026014, published July 8, 2026).

Potentially distinctive physics remains the **history-transfer synthesis** and the quantified causal/local-capture tradeoff.

## Immediate frontier

1. Independently cross-check the polynomial $P(\epsilon)$ using a second gauge-invariant derivation.
2. Replace the radiation-only complementary spectrum with an operational complement that handles soft/dressing sectors consistently.
3. Derive the quantum channel of an enclosing mode-matched gravitational receiver and calculate its capture fraction explicitly.
4. Determine whether a general bound exists between receiver compactness/angular coverage, $\epsilon$, and achievable history-transfer margin.
5. Compare this exact crossover result with current retarded-GIE and geodesic-deviation literature before any novelty claim.

## Current conceptual compression

> **The equivalence principle forces the local receiver to measure curvature, not force. For a conserved quadrupolar source, the complete retarded curvature field is one analytic object: static tidal, induction, and radiation terms are merely different powers of $\omega R/c$ in the same transfer polynomial. That polynomial exposes the central tension quantitatively. A local quantum receiver can capture branch information very coherently in the reactive near field, but by the time retardation becomes dynamically obvious, the information is spread through propagating gravitational modes and the local receiver's strong-history efficiency is suppressed to an extraordinarily small dimensionless gravitational parameter. The next question is whether an appropriately mode-matched quantum receiver can recover that information and turn the causal propagation itself into a nonclassical witness.**
