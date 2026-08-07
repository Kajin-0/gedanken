# Checkpoint — 2026-08-07 17:43 EDT

## Main correction closed

The coherent source-output $\rightarrow$ receiver-input **storage amplitude** is

$$
\boxed{
t_{BA}^{\rm store}
=\frac{-i\Sigma_{BA}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}
}
$$

(up to global phase convention), obtained directly by eliminating the common graviton continuum and comparing the delayed source drive in the receiver equation with standard input-output normalization.

For aligned plus quadrupoles,

$$
\Sigma_{BA}^{R}
=\frac54\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
$$

so

$$
\boxed{
t_{BA}^{\rm store}
=-\frac{5i}{4}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5}.
}
$$

Wave zone:

$$
\boxed{
\eta_{\rm store}
=|t|^2
\simeq
\frac{25\mathcal O}{16(kR)^2}.
}
$$

The factor two in

$$
\Gamma_{AB}=2\operatorname{Im}\Sigma_{AB}^{R}
$$

converts self-energy amplitude to cross damping/scattering rate and does **not** double the stored field amplitude.

Consistency:

$$
\sigma_{\rm abs,max}^{(l=2)}=\frac{5\pi}{2k^2},
$$

whereas

$$
\sigma_{\rm sca,max}^{(l=2)}=\frac{10\pi}{k^2}.
$$

The quantum-memory problem uses absorption/storage.

## Receiver bookkeeping correction

The receiver's intrinsic total gravitational linewidth is range independent:

$$
\boxed{
\kappa_{\rm tot}=\kappa_{g,B}+\kappa_i+\cdots.
}
$$

Distance changes only the desired source-mode fraction,

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_{g,B}.
}
$$

Therefore the corrected resonant thermal NPT range is

$$
\boxed{
R_Q^{\rm res}
=\frac{5}{4k}
\sqrt{
\frac{\mathcal O\kappa_{g,B}}
{\Gamma_{\rm th}}
}.
}
$$

and the exact finite-cat front is

$$
\boxed{
T_{\rm NPT}^{\min}(R)
=\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln[1-(R/R_Q^{\rm res})^2],
\qquad R<R_Q^{\rm res}.
}
$$

Within range and in the wave zone, the post-light-cone build delay scales as $R^2$; it diverges logarithmically as $R\to R_Q^{\rm res-}$.

## Passive resonant necessary condition

Combining the corrected free-space storage overlap with the passive nonrelativistic quadrupole oscillator-strength ceiling gives

$$
\boxed{
\frac{25\mathcal O}{24}
\frac{Q_B\mathcal C_B\beta_B^3}{\bar n_B}
>\zeta^2
}
$$

as a necessary condition for a nonempty passive nonrelativistic **resonant** wave-zone NPT interval.

The earlier $\beta_B^5$ result applies only to a literal geometric-aperture-limited absorber and is not universal.

## Canonical files updated

- `../DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md`
- `../RESONANT_FREE_SPACE_RECEPTION_CONE.md`
- `../PASSIVE_WAVEZONE_FEASIBILITY_BOUND.md`
- `../CURRENT_STATE.md`

## Next strongest path

1. Numerically evaluate the corrected passive resonant criterion for receiver classes.
2. Test genuinely non-Gaussian/heralded receiver loopholes.
3. If no structural failure appears, reorganize the main Experiment 01 paper around the exact Gaussian probe theorem + gravitational causal NPT front.