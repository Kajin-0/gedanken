# Checkpoint — 2026-08-07 15:40 EDT

## Direct receiver dynamics

For causal arrival at $t_0=R/c$,

$$
\dot c
=-\frac{\kappa_g+\kappa_i}{2}c
+\sqrt{\kappa_g}b_{\rm in}
+\sqrt{\kappa_i}\xi_{\rm in}.
$$

For a fixed normalized gravitational difference-mode envelope $f$,

$$
\eta_f(t)
=\kappa_g
\left|
\int_{R/c}^{t}ds\,
e^{-(\kappa_g+\kappa_i)(t-s)/2}f(s)
\right|^2.
$$

The branch-independent receiver thermal occupation is

$$
m(t)
=e^{-\kappa\tau}\bar n_0
+\frac{\kappa_i\bar n_i}{\kappa}(1-e^{-\kappa\tau}),
\qquad
\kappa=\kappa_g+\kappa_i.
$$

Weak-cat source-receiver entanglement occurs exactly when

$$
\boxed{\eta_f(t)>m(t)}.
$$

The global fidelity-history witness requires

$$
\boxed{\eta_f(t)>m(t)+1/2}.
$$

For a pre-equilibrated receiver,

$$
m_*=\kappa_i\bar n_i/\kappa,
$$

and an optimally matched pulse gives

$$
T_{\rm NPT}^{\rm opt}
=R/c+
\kappa^{-1}
\ln\frac{\kappa_g}{\kappa_g-\bar n_i\kappa_i}.
$$

As $\kappa_g\to\bar n_i\kappa_i^+$ the post-light-cone delay diverges logarithmically.

## Linearized-gravity coupling

The gravitational input-output rate is the spontaneous quadrupole graviton-emission linewidth,

$$
\boxed{
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

Thus the same matrix element governs spontaneous graviton emission, time-reversed graviton absorption, and the causal rate of branch-information transfer into the receiver.

For the cylindrical acoustic bar geometry of Tobar et al. (2024),

$$
\boxed{
\kappa_g
=\frac{8GML^2\omega_l^4}{l^4\pi^4c^5}.
}
$$

## Important correction

Finite temperature does not universally imply a finite post-light-cone entanglement delay. For a receiver freshly ground-state prepared at causal arrival, signal capture and thermal bath noise initially grow with the same factor, so the weak-cat state is either NPT immediately after arrival when $\kappa_g>\bar n_i\kappa_i$, or never in the ideal matched model. A finite delay arises from a pre-existing thermal floor or from a fixed/mismatched physical wavepacket.

## Next target

Evaluate the gravitational cooperativity and front times for representative receiver families, then identify which scalings are fundamentally favorable.