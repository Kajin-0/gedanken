# Checkpoint — 2026-08-07 17:30 EDT

## Strongest new quantum-information result

For any nontrivial finite binary coherent hybrid state

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
\quad
0<p<1,\quad\alpha\neq\beta,
$$

and any one-mode gauge-covariant phase-insensitive Gaussian channel $\Phi_{\tau,m}$ with intensity gain/transmission $\tau$ and vacuum-output occupation $m$,

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
m<\tau.
}
$$

The condition $m<\tau$ is exactly the non-entanglement-breaking region of this channel family. Thus every nontrivial binary coherent hybrid input is a complete EB probe for thermal attenuators, thermal amplifiers, and additive Gaussian noise.

The exact sign parameter is

$$
q=
\exp\left[
\frac{|\alpha-\beta|^2}{2m}(\tau-m)
\right].
$$

Full theorem: `../PHASE_INSENSITIVE_GAUSSIAN_BINARY_PROBE_THEOREM.md`.

## Exact three-element witness

For the symmetric representation $|\pm a\rangle$, choose

$$
v_*=2\sqrt\tau a/m.
$$

Then

$$
\frac{|z_v|^2}{p_0p_v}
=\exp\left[
\frac{N_\Delta}{m}(\tau-m)
\right],
\qquad N_\Delta=4|a|^2.
$$

Therefore

$$
|z_v|^2>p_0p_v
$$

is exactly equivalent to NPT for this family.

## Gravitational source strength

The outgoing branch-difference graviton mode has

$$
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5|\Delta\widetilde Q_{ij}(\omega)|^2.
$$

For a narrow-band plus quadrupole,

$$
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}{5\hbar c^5}.
$$

This controls witness/entanglement magnitude but not the exact NPT sign boundary.

## Finite-strength front

Define

$$
\Lambda
=\ln\frac{|z_v|^2}{p_0p_v}.
$$

For a stationary passive receiver,

$$
\Lambda_{\max}(\tau)
=\frac{N_\Delta}{\Gamma_{\rm th}}
[\kappa_\Delta(1-e^{-\kappa_{\rm tot}\tau})-\Gamma_{\rm th}].
$$

The earliest exact margin $\Lambda_{\rm req}>0$ is

$$
T_\Lambda^{\min}
=
\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{\Gamma_{\rm th}}{\kappa_\Delta}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right)
\right].
$$

## Finite-aperture quantum reception cone

For the plus quadrupole, an ideal polar-cap receiver accesses

$$
\beta_{\rm cap}
=\frac12-rac{5c+10c^3+c^5}{32},
\qquad c=\cos\theta_0.
$$

For small aperture radius $a_R$ at range $R$,

$$
\beta_{\rm cap}\simeq\frac58\frac{a_R^2}{R^2}.
$$

Define

$$
K=\frac58a_R^2\mathcal O\kappa_g,
\qquad
R_Q=\sqrt{K/\Gamma_{\rm th}}.
$$

Then

$$
T_{\rm NPT}^{\min}(R)
=
\frac Rc-
\frac1{\kappa_0+K/R^2}
\ln[1-(R/R_Q)^2],
\qquad R<R_Q.
$$

There is no NPT front for $R\ge R_Q$ at nonzero stationary thermal noise in this finite-aperture model. The front diverges logarithmically as $R\to R_Q^-$.

Finite witness margin gives a smaller nested range

$$
R_\Lambda
=R_Q/\sqrt{1+\Lambda_{\rm req}/N_\Delta}.
$$

## Passive nonrelativistic wave-zone necessary condition

Combining the passive quadrupole oscillator-strength ceiling with finite aperture and $R_{\rm WZ}=\zeta c/\omega_B$ gives

$$
\boxed{
\mathfrak W_B
=\frac{5\mathcal O}{12}
\frac{Q_B\mathcal C_B\beta_B^5}{\bar n_B}
>\zeta^2,
}
$$

where

$$
\mathcal C_B=r_s/L_B,
\qquad
\beta_B=\omega_BL_B/c.
$$

At high temperature,

$$
\mathfrak W_B
\simeq
\frac{5\mathcal O}{12}
Q_B\mathcal C_B\beta_B^6\frac{\lambda_T}{L_B}.
$$

This is a passive receiver-class feasibility bound, not a universal no-go theorem.

## Prior-art status

Established:
- two-coherent-state effective-entanglement channel tests;
- symmetric hybrid coherent cats through thermal beam-splitter noise;
- Gaussian-channel EB thresholds;
- entanglement distribution through every non-EB phase-insensitive Gaussian channel using other protocols.

Not located in targeted searches:
- all finite nontrivial binary coherent hybrid states being NPT iff every gauge-covariant phase-insensitive Gaussian channel is non-EB;
- exact three-element witness saturating that boundary;
- gravity-specific retarded NPT/certification reception cone.

Novelty remains unverified.

## Next strongest path

1. Search for a hidden general theorem implying binary coherent probe completeness.
2. Evaluate passive wave-zone figure of merit for receiver classes.
3. Analyze phase-sensitive/non-Gaussian receiver loopholes.
4. If robust, reorganize main Experiment 01 around the exact Gaussian lemma and causal gravitational reception cone.