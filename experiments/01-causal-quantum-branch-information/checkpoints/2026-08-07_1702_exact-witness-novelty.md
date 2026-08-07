# Checkpoint — 2026-08-07 17:02 EDT

## Closed result

For

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle+|1\rangle|-a\rangle}{\sqrt2},
\qquad 0<|a|<\infty,
$$

sent through a thermal attenuator with transmissivity $\eta$ and environment occupation $\bar n$, define

$$
m=(1-\eta)\bar n.
$$

The source-receiver output is NPT iff

$$
\boxed{\eta>m}
$$

for every finite nonzero cat amplitude.

This was independently audited against a direct finite-Fock beam-splitter thermal dilation.

## Exact three-element witness

Choose

$$
v_*=\frac{2\sqrt\eta\,a}{m}.
$$

Define

$$
p_0=\langle0,0|\rho|0,0\rangle,
$$

$$
p_v=\langle1,v_*|\rho|1,v_*\rangle,
$$

and

$$
z_v=\langle1,0|\rho|0,v_*\rangle.
$$

Then

$$
\boxed{
\frac{|z_v|^2}{p_0p_v}
=\exp\left[
\frac{4a^2}{m}(\eta-m)
\right]
}
$$

and therefore

$$
\boxed{
|z_v|^2>p_0p_v
\iff
\rho\text{ is NPT}
\iff
\eta>\frac{\bar n}{\bar n+1}.
}
$$

This requires only two populations and one joint source-receiver coherence.

Detailed derivation: `../EXACT_THREE_ELEMENT_WITNESS.md`.

## Key literature boundary

Kreis & van Loock, PRA 85, 032307 (2012), arXiv:1111.0478, analyze the exact same hybrid input and thermal beam-splitter channel. They obtain the exact noisy output but use a finite-order Shchukin–Vogel moment witness. Their Eq. (41) provides only a sufficient amplitude-dependent detection region. Their footnote [47] explicitly notes that comparison with the thermal entanglement-breaking boundary implies their witness may miss entangled states below that boundary.

The current theorem appears to close precisely that unresolved detection gap for the full finite-amplitude family, and the new three-element principal-minor witness detects the whole non-EB region.

This is promising evidence of novelty but **not yet a novelty claim**.

Detailed note: `../NOVELTY_CHECK_FINITE_CAT.md`.

## Causal front consequence

The exact finite-cat theorem upgrades the receiver front to

$$
\rho_{AB}(t)\text{ NPT}
\iff
\eta_f(t)>m(t)
$$

for all finite source cats within the thermal single-mode model.

For a stationary Markov receiver,

$$
T_{\rm NPT}^{\min}
=
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right]
$$

when $\kappa_\Delta>\Gamma_{\rm th}$; otherwise no finite-cat NPT front exists.

## Strongest next path

1. Search for an indirect general theorem implying the exact finite-cat result.
2. Derive a more practical measurement protocol for the exact three-element witness.
3. Derive tight near-threshold entanglement magnitude for finite cat amplitude.
4. If novelty/proof survive, reorganize the main Experiment 01 paper around this exact causal-front theorem.
