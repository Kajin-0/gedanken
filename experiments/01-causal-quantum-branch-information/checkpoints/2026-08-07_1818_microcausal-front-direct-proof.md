# Checkpoint — 2026-08-07 18:18 EDT

## Two strongest developments after the 18:00 canonical state

### 1. General channel-capability front

Define the complete source-controlled accessible receiver channel

$$
\mathcal A_{R,t}:
\text{incoming gravitational branch mode}
\to
\text{accessible receiver register at time }t.
$$

Microcausality implies that before causal contact this map is a replacer channel:

$$
\boxed{
\mathcal A_{R,t}(\rho)
=\sigma_{R,t}\operatorname{Tr}\rho,
\qquad t<R/c.
}
$$

Therefore

$$
\mathcal A_{R,t}\in\mathrm{EB}
\qquad t<R/c.
$$

Define the general channel-capability front

$$
\boxed{
T_{\rm cap}(R)
=\inf\{t:\mathcal A_{R,t}\notin\mathrm{EB}\}.
}
$$

Then

$$
\boxed{T_{\rm cap}(R)\ge R/c.}
$$

This avoids the incorrect statement that all source-receiver entanglement must vanish outside the light cone; spacelike vacuum correlations/entanglement harvesting are compatible with the theorem because the theorem concerns the **source-controlled communication channel**.

For any particular entangled source-mode input $\Psi$,

$$
T_{\Psi}(R)\ge T_{\rm cap}(R).
$$

Call a probe family **front faithful** when its entanglement onset equals the channel-capability onset.

The finite binary coherent hybrid family is front faithful for the current phase-insensitive Gaussian receiver family:

$$
\boxed{
T_{\rm binary\ coherent}^{\rm NPT}(R)
=T_{\rm cap}(R).
}
$$

Files:

- `../GENERAL_CAUSAL_QUANTUM_CHANNEL_FRONT.md`
- `../MICROCAUSAL_REPLACER_THEOREM.md`

### 2. Direct finite-minor proof of the Gaussian theorem

For the gauge-covariant phase-insensitive Gaussian channel $\Phi_{\tau,m}$,

$$
\chi_{\Phi(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp[-(2m+1-\tau)|\xi|^2/2],
$$

an arbitrary coherent dyad has exact output matrix element

$$
\boxed{
\langle u|
\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)
|v\rangle
=
\frac{\langle\beta|\alpha\rangle\langle u|v\rangle}{m+1}
\exp\left[
\frac{(\sqrt\tau\beta^*-u^*)(v-\sqrt\tau\alpha)}{m+1}
\right].
}
$$

For the symmetric binary coherent branches $|\pm a\rangle$, the partial-transpose principal-minor ratio is

$$
\ln R(v)
=-4a^2-v^2
+
\frac{4\tau a^2+4\sqrt\tau av+v^2}{m+1}.
$$

For $m>0$ the optimum is

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and

$$
\boxed{
R(v_*)
=
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

Thus

$$
\tau>m
\Rightarrow
R(v_*)>1
\Rightarrow
\rho^{T_A}\not\succeq0.
$$

Conversely $m\ge\tau$ is the established channel EB region, so

$$
\boxed{
\rho_{AB}\text{ NPT}
\iff
\tau>m.
}
$$

This proof applies directly to attenuators, amplifiers, and additive Gaussian noise and does not depend on a thermal-loss dilation or an unbounded inverse congruence.

#### Pure-loss edge case

At $m=0$,

$$
\boxed{
\ln R(v)
=4a^2(\tau-1)+4\sqrt\tau av.
}
$$

For every physical pure-loss channel with $\tau>0$, choose finite

$$
\boxed{
v>a(1-\tau)/\sqrt\tau}
$$

to obtain $R(v)>1$. Therefore pure loss is included rigorously.

Files:

- `../DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `../PURE_LOSS_EDGE_CASE.md`

## Current strongest paper logic

The clean theorem stack is now:

1. **Microcausal replacer theorem:** the source-controlled receiver channel is EB before $R/c$.
2. **Binary coherent Gaussian theorem:** every finite nontrivial binary coherent probe is NPT iff the phase-insensitive receiver channel is non-EB.
3. **Exact three-element witness:** a $2\times2$ matched principal minor detects that same boundary.
4. **Causal receiver theorem:** receiver dynamics determine the earliest time the channel leaves EB.
5. **Linearized-GR input-output map:** the useful source-mode coupling is fixed by the retarded gravitational Green function.
6. **Master front equation:** these ingredients combine into a quantitative spacetime NPT/certification front.

## Strongest next path

Stop expanding the receiver zoo unless a theorem forces it. Next:

1. perform a theorem-level adversarial review of assumptions and notation;
2. broaden the citation-forward novelty check around the direct finite-minor result;
3. reorganize the main Experiment 01 paper around the theorem stack above;
4. leave compact-object/non-Gaussian receiver extensions as discussion/future work unless needed to defend the central result.