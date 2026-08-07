# Current State — Experiment 01

**Last updated:** 2026-08-07 14:09 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

Canonical recovery point. Detailed derivations: `SCALAR_MATCHED_HISTORY.md`, `GRAVITY_QUADRUPOLE_LIMIT.md`, `TIDAL_RECEIVER.md`, `PROGRESS_LOG.md`, and `checkpoints/`.

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
\qquad
\chi_B=-\ln(1-D_B^2),
\quad
\Gamma_\Xi=-\ln C_\Xi.
}
$$

$$
\boxed{\mathcal M_\Xi>0\Rightarrow A\text{-}B\text{ entanglement}.}
$$

For pure conditional global histories,

$$
C_\Xi=F(\rho_E^L,\rho_E^R),
$$

so $C_\Xi$ is the fidelity of the unobserved complementary records. The final formulation therefore does not require a literal $A\otimes g\otimes B$ factorization.

## Causality

For a source-controlled operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0
\qquad T<R/c.
$$

Define

$$
T_*(R)=\inf\{T:\mathcal M_\Xi(T,R)>0\}.
$$

A local theory requires

$$
T_*(R)\ge R/c.
$$

## Scalar matched-history result

For source history $u(t)$,

$$
\chi_B=\langle u,K_Bu\rangle,
\qquad
2\Gamma_\Xi=\langle u,N_Tu\rangle,
$$

so

$$
\boxed{
\mathcal M_\Xi[u]=\langle u,(K_B-N_T)u\rangle.
}
$$

With $K_B=|r_T\rangle\langle r_T|$,

$$
\boxed{
\eta_T=\langle r_T,N_T^{-1}r_T\rangle>1
}
$$

is equivalent to the existence of an optimized positive-margin history in the toy model. The optimal complex envelope is

$$
u_{\rm opt}\propto N_T^{-1}r_T.
$$

In the narrow-band limit,

$$
\gamma_{\rm hist}=rac{|\mathcal R_B|^2}{S_E},
\qquad
T_*\simeq\frac Rc+\gamma_{\rm hist}^{-1}.
$$

With receiver damping $\kappa_B$,

$$
\boxed{
\mathcal C_{\rm hist}=\frac{|\mathcal R_B|^2}{\kappa_BS_E}>1
}
$$

is the strong-witness cooperativity threshold.

## Critical GR correction: receiver must be tidal

The previous single-mass force receiver is not the cleanest local GR observable. A self-contained freely falling receiver cannot detect a uniform gravitational acceleration. In Fermi normal coordinates its leading local coupling is to curvature,

$$
H_{\rm curv}
=\frac{\mu_Bc^2}{2}R_{0i0j}\xi^i\xi^j.
$$

For a one-dimensional differential quantum mode with equilibrium baseline $L_B$ and quantum displacement $x_B$,

$$
\boxed{
H_{\rm drive}
=\mu_BL_B\mathcal E_{nn}(t)x_B,
\qquad
\mathcal E_{ij}=c^2R_{0i0j}.
}
$$

This is the gauge-invariant geodesic-deviation receiver used from this point forward.

## Conserved source quadrupole

Use

$$
\Delta Q_{ij}(t)
=q(t)\left(n_in_j-\frac13\delta_{ij}\right).
$$

On-axis,

$$
\Delta\Phi_Q=\frac{Gq}{R^3},
$$

so the radial tidal field is

$$
\boxed{
|\Delta\mathcal E_{nn}^{\rm NZ}|
=\frac{12G|q|}{R^5}.
}
$$

The differential receiver force is therefore

$$
\boxed{
|\Delta F_B^{\rm NZ}|
=\frac{12G\mu_BL_B}{R^5}|q(t-R/c)|.
}
$$

This **supersedes the earlier $R^{-4}$ supported-force receiver scaling** for the clean free local receiver.

## Corrected near-zone gravity efficiency

Using

$$
S_G(\omega)\simeq\frac{2G}{15\hbar c^5}\omega^5
$$

for the clean outgoing quadrupolar graviton record in the stated convention,

$$
\boxed{
\gamma_{\rm hist,tidal}^{\rm NZ}
\simeq
540\frac{G\mu_BL_B^2c^5}{R^{10}\omega_B^6}.
}
$$

With $Q_B=\omega_B/\kappa_B$,

$$
\boxed{
\mathcal C_{\rm hist,tidal}^{\rm NZ}
\simeq
540\frac{G\mu_BL_B^2c^5Q_B}{R^{10}\omega_B^7}.
}
$$

Define

$$
\epsilon=\frac{\omega_BR}{c},
\qquad
\nu_G=\frac{G\mu_BL_B^2Q_B\omega_B^3}{c^5}.
$$

Then

$$
\boxed{
\mathcal C_{\rm hist,tidal}^{\rm NZ}
\simeq540\nu_G\epsilon^{-10}.
}
$$

For laboratory systems $\nu_G\ll1$, so the local strong-witness regime is parametrically deep in the near zone.

## Wave-zone local receiver

The radiative curvature is

$$
\mathcal E_{ij}^{\rm GW}
=-\frac{G}{c^4R}Q_{ij}^{(4),TT}.
$$

For a transverse differential receiver with angular/polarization projection $\mathcal A$,

$$
\boxed{
\mathcal C_{\rm hist,tidal}^{\rm WZ}
\simeq
\frac{15\mathcal A^2}{4}
\nu_G\epsilon^{-2}.
}
$$

At the dynamical crossover $\epsilon\sim1$, the efficiency is therefore only $O(\nu_G)$, which is extraordinarily small for laboratory receivers.

### Interpretation

This is a **strong-witness local-receiver tradeoff**, not a no-go theorem for entanglement:

- deep near zone: reactive coherent transfer can dominate clean radiative leakage, but retardation is dynamically tiny;
- wave zone: retardation is obvious, but a single local receiver captures only a tiny fraction of the outgoing branch record.

The strong witness is sufficient, not necessary, and the current $S_G$ includes only the clean radiative graviton contribution. Dressing/soft/technical records must be treated consistently in the complete theory.

## Ideal enclosing receiver

An ideal quantum receiver mode-matched to the outgoing quadrupolar radiation can conceptually avoid the local-mode-capture problem. In the pure-loss benchmark, if fraction $\tau_{\rm ch}$ of the branch-distinguishing outgoing mode is coherently captured,

$$
\mathcal M_\Xi=(2\tau_{\rm ch}-1)|\Delta|^2,
$$

so the strong witness requires $\tau_{\rm ch}>1/2$.

Thus Experiment 01 currently has two clean limits:

1. **free differential near-field receiver:** optimized for coherent nonclassical transfer;
2. **mode-matched enclosing wave-zone receiver:** optimized for explicit causal propagation.

## Literature boundary added today

Fermi-normal quantum mechanics gives the leading curvature coupling proportional to $mR_{0i0j}x^ix^j/2$. Gravitational-wave detectors fundamentally measure geodesic deviation. A July 8, 2026 PRD paper by Hirotani and Matsumura studies classical-quantum gravity specifically through geodesic deviation and predicted strain spectra. Therefore the tidal receiver itself is established physics, not a novelty claim.

## Immediate frontier

Derive the exact retarded **electric-Weyl quadrupole transfer function**

$$
\mathcal E_{ij}(\omega,R)
=\frac{Gq(\omega)}{R^5}\mathcal P_{ij}(\epsilon,\Omega)
$$

through the near/induction/wave crossover. The expected structure contains terms through $\epsilon^4$ and must reproduce

$$
R^{-5}
$$

in the static tidal limit and

$$
\omega^4/(c^4R)
$$

in the wave zone.

Use the same conserved stress-energy history to derive the complementary TT/soft record kernel. Then calculate one gauge-invariant

$$
\mathcal C_{\rm hist}^{(G)}(\epsilon)
$$

across the full crossover and determine whether a rigorous relation exists between resolvable retardation and local quantum-history capture.

## Current conceptual compression

> **A freely falling quantum receiver does not measure gravity as a force; it measures curvature through geodesic deviation. Once that Einstein-level correction is imposed, the useful near-field branch signal of a conserved source quadrupole falls as $R^{-5}$. The outgoing gravitational record is quadrupolar and radiative. Their competition makes the local strong-history witness overwhelmingly a near-field phenomenon, while obvious retardation is a wave-zone phenomenon. The emerging question is whether this tension is merely technological mode capture or reflects a deeper information-theoretic constraint on how gravity can carry quantum branch information through spacetime.**
