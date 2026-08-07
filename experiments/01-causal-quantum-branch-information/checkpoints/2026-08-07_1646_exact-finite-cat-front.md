# Checkpoint — 2026-08-07 16:46 EDT

## Exact finite-cat thermal result

The previous finite-cat numerical conjecture is now analytically closed within the single-mode phase-insensitive thermal-attenuator model.

For

$$
|\Psi_a\rangle
=\frac{|L\rangle|a\rangle+|R\rangle|-a\rangle}{\sqrt2},
\qquad 0<|a|<\infty,
$$

sent through a thermal attenuator with coherent transmissivity $\eta$ and environment occupation $\bar n$, define

$$
m=(1-\eta)\bar n.
$$

Then

$$
\boxed{
\rho_{AB}\text{ is NPT}
\iff
\eta>m
\iff
\eta>\frac{\bar n}{\bar n+1}
}
$$

for **every finite nonzero cat amplitude**.

The proof writes the bosonic output blocks in Gaussian normal-ordered form and factorizes the partial transpose. After block-diagonal congruence the relevant operator becomes

$$
\frac12
\begin{pmatrix}
I&qD(-u)\\
qD(u)&I
\end{pmatrix},
$$

with $D(u)$ unitary and

$$
\boxed{
q=\exp\left[
\frac{2|a|^2}{m}(\eta-m)
\right].
}
$$

Hence a negative direction exists exactly when $q>1$, i.e. $\eta>m$. Below threshold the channel is entanglement breaking, so the output is separable for every input.

Full proof: `../EXACT_FINITE_CAT_THERMAL_THEOREM.md`.

## Causal-front upgrade

At fixed time, the passive linear thermal receiver is an effective thermal attenuator from the selected incoming gravitational difference mode to the stored receiver mode. Therefore

$$
\boxed{
\rho_{AB}(t)\text{ is NPT for every finite cat}
\iff
\eta_f(t)>m(t).
}
$$

For a stationary multiport receiver,

$$
\Gamma_{\rm th}=\sum_a\bar n_a\kappa_a,
\qquad
m_*=\Gamma_{\rm th}/\kappa_{\rm tot}.
$$

Any normalized incoming waveform obeys

$$
\eta_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau}),
\qquad
\tau=t-R/c.
$$

Thus the exact finite-cat NPT front satisfies

$$
\boxed{
T_{\rm NPT}
\ge
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right]
}
$$

when $\kappa_\Delta>\Gamma_{\rm th}$, and no finite-cat NPT front exists in the model when $\kappa_\Delta\le\Gamma_{\rm th}$.

The time-reversed receiver kernel saturates the coherent-capture inequality, so the front bound is tight within the Markov model.

Updated theorem: `../CAUSAL_FRONT_THEOREM.md`.

## Important interpretation

The NPT **boundary and earliest front are independent of finite cat amplitude**. Increasing branch separation can change the amount and measurability of entanglement, but cannot open an entanglement-breaking receiver channel and cannot shift the exact thermal boundary.

## Novelty discipline

The thermal attenuator EB threshold itself is established. Targeted searches found prior studies of entangled coherent states in thermal/noisy channels and non-Gaussian robustness, but not this exact hybrid finite-cat iff theorem or its use in a retarded waveform-optimal causal NPT front.

Novelty remains unverified.

## Immediate next step

Independently verify the infinite-dimensional factorization/domain argument and broaden the literature search for equivalent hybrid-cat theorems. If both survive, reorganize Experiment 01 around the exact causal-front theorem.