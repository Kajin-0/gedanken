# Checkpoint — 2026-08-07 16:21 EDT

## Tight causal NPT speed limit

For a stationary multiport receiver with useful source-mode coupling $\kappa_\Delta$, total damping $\kappa_{\rm tot}$, and thermal injection

$$
\Gamma_{\rm th}=\sum_a\bar n_a\kappa_a,
$$

any normalized incoming branch-difference waveform obeys

$$
\boxed{
\eta_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau}),
\qquad
\tau=t-R/c.
}
$$

Therefore a weak-cat NPT front exists only if

$$
\boxed{\kappa_\Delta>\Gamma_{\rm th}.}
$$

When it exists,

$$
\boxed{
T_{\rm NPT}
\ge
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}.
}
$$

The time-reversed matched receiver kernel saturates the ideal Markov bound.

Define

$$
\epsilon_Q=1-\Gamma_{\rm th}/\kappa_\Delta.
$$

Then

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
=-\kappa_{\rm tot}^{-1}\ln\epsilon_Q.
}
$$

The same $\epsilon_Q$ controls the post-front coherent growth rate.

## Relativistic QFT correction

The nonrelativistic passive quadrupole compactness ceiling is not universal in QFT. A free-field stress test shows that spatial smearing alone still permits arbitrarily energetic back-to-back excitations, so the UV-integrated stress response is not bounded by a simple finite geometric sum rule.

For a passive Gibbs receiver, however, KMS gives the universal mode-resolved relation

$$
\boxed{
S_H(\omega)
=\hbar\coth\left(\frac{\hbar\omega}{2k_BT}\right)\chi''(\omega).
}
$$

Thus relativistic QFT can evade the nonrelativistic absolute-response ceiling but not the equilibrium noise-to-response ratio.

The general multiport thermal condition remains

$$
\boxed{
\kappa_\Delta>\sum_a\bar n_a\kappa_a.
}
$$

## Source-mode overlap

The useful rate is

$$
\kappa_\Delta=\mathcal O_{SB}\kappa_g,
$$

where, for complete angular access,

$$
\boxed{
\mathcal O_Q
=\frac{|Q_B^{ij*}Q^S_{ij}|^2}
{(Q_B^{ij*}Q^B_{ij})(Q_S^{ij*}Q^S_{ij})}.
}
$$

For rotated plus quadrupoles,

$$
\mathcal O_Q=\cos^2(2\psi).
$$

## Numerical finite-cat status

`numerics/thermal_cat_scan.py` reproduces the thermal attenuator explicitly. Initial scans suggest that above the thermal EB boundary the binary coherent source-cat remains NPT for every finite branch separation tested, while negativity peaks at an intermediate branch separation and tends toward zero for very large cats. This is numerical evidence only.

## Novelty status

A preliminary search found related work on the opposite problem—time for a dynamical channel to become entanglement breaking—and established gravity-induced thermal EB thresholds, but not the exact waveform-optimal retarded entanglement-onset bound above. Promising but unverified.

## Next target

Formalize the causal-front speed-limit theorem and continue searching for a finite-cat analytic proof.