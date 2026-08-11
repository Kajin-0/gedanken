# Countably Infinite Passive Extension and Reduced-Memory Boundary

**Stage:** E  
**Status:** validated operator extension for the declared retained model.  
**Scope:** separable endpoint Hilbert spaces with a well-posed local-in-time passive realization, bounded selected port maps in the direct proof below, and Hilbert--Schmidt retained gravitational observation. Unbounded system-node realizations and reduced non-Markovian descriptions require the additional qualifications in Secs. 8--9.

## 1. Purpose

The finite-dimensional passive-cut proof must not make modal count a hidden resource assumption. A bounded elastic body has countably many continuum normal modes, and a reduced mechanical description may also acquire memory after internal or environmental degrees of freedom are eliminated.

The operator question is therefore twofold:

1. does the passive Gramian cut survive a countably infinite retained modal space? yes, under the stated bounded-port / finite-trace hypotheses;
2. does every non-Markovian or unbounded continuum model automatically satisfy those hypotheses? no.

## 2. Passive Hilbert-space realization

Let the internal state space `X` be a separable Hilbert space and the total port space `Y` another Hilbert space. Let

```math
K:X\to Y
```

be bounded, with selected port blocks `K_u`, `K_y`, and retained gravitational block `K_g` obtained by orthogonal projections in `Y`.

Let `H` be self-adjoint, possibly unbounded on its natural domain, and suppose

```math
A=-iH-\frac12K^\dagger K
```

generates a passive contraction semigroup

```math
\mathcal T(t)=e^{At}.
```

The proof needs the passive energy inequalities

```math
\boxed{
\mathcal T(\tau)\mathcal T^\dagger(\tau)
+
\int_0^\tau
\mathcal T(t)K^\dagger K\mathcal T^\dagger(t)dt
\le I,
}
```

and dually

```math
\boxed{
\mathcal T^\dagger(\tau)\mathcal T(\tau)
+
\int_0^\tau
\mathcal T^\dagger(t)K^\dagger K\mathcal T(t)dt
\le I.
}
```

Equality holds for the ideal lossless Markov dilation; the inequality form permits extra passive dissipation.

## 3. Selected-input Gramian

Define

```math
P_u(\tau)
=
\int_0^\tau
\mathcal T(t)K_u^\dagger K_u\mathcal T^\dagger(t)dt.
```

Since

```math
0\le K_u^\dagger K_u\le K^\dagger K,
```

passivity gives

```math
\boxed{
0\le P_u(\tau)
\le I-\mathcal T(\tau)\mathcal T^\dagger(\tau)
\le I.
}
```

`P_u(τ)` is monotone in positive-operator order and uniformly bounded, so

```math
P_u=\operatorname{s-lim}_{\tau\to\infty}P_u(\tau)
```

exists with

```math
\boxed{0\le P_u\le I.}
```

No finite matrix dimension and no decay of every dark internal mode is needed for this inequality.

## 4. Weighted infinite-dimensional H2 cut

Let `L:X->Z` be any bounded Hilbert--Schmidt observation into a Hilbert space `Z`. The selected-input impulse response is

```math
h_L(t)=L\mathcal T(t)K_u^\dagger.
```

Because the Hilbert--Schmidt operators form a two-sided ideal,

```math
\begin{aligned}
\int_0^\infty\|h_L(t)\|_{\rm HS}^2dt
&=\operatorname{Tr}(LP_uL^\dagger)\\
&\le\operatorname{Tr}(LL^\dagger)
=\|L\|_{\rm HS}^2.
\end{aligned}
```

Hilbert-space Plancherel then yields

```math
\boxed{
\frac1{2\pi}\int_{-\infty}^{\infty}
\|L(i\nu I-A)^{-1}K_u^\dagger\|_{\rm HS}^2d\nu
\le
\|L\|_{\rm HS}^2.
}
```

The dual output-Gramian argument gives the same cut from the receiver side.

This is the infinite-dimensional version of the weighted passive inequality used in the submission manuscript.

## 5. Sector-resolved gravitational observation is Hilbert--Schmidt

Choose the source--receiver direction `Rhat` and decompose the STF quadrupole space into `m=0`, `|m|=1`, and `|m|=2` sectors. Let `Q_{m,n}` denote the corresponding mass-normalized projection amplitude of mode `n`.

The sector completeness bounds are

```math
\sum_n\frac{Q_{2,n}^2}{\mu_n}\le4I_{\hat R},
```

```math
\sum_n\frac{Q_{1,n}^2}{\mu_n}
\le2I_{\hat R}+4Z_{\hat R},
```

and

```math
\sum_n\frac{Q_{0,n}^2}{\mu_n}
\le\frac23 I_{\hat R}+\frac83 Z_{\hat R}.
```

For the retained sector `omega_n<=Omega`, the on-shell gravitational coupling weight supplies at most `Omega^4` in every sector. Therefore each sector observation operator `L_m` has finite Hilbert--Schmidt norm bounded by

```math
\|L_m\|_{\rm HS}^2
\le
\frac{G\Omega^4}{5c^5}\,S_m,
```

where

```math
S_2=4I_{\hat R},
S_1=2I_{\hat R}+4Z_{\hat R},
S_0=\frac23 I_{\hat R}+\frac83 Z_{\hat R}.
```

Thus the finite-trace regularity needed in Sec. 4 follows from the retained gravitational resource itself.

## 6. Propagation weighting and two-ended closure

Let the compact outgoing TT propagation operator at physical frequency `omega(nu)` be diagonal in the three STF sectors with sector power singular values

```math
eta_m[omega(nu)R/c].
```

Define the measured-band suprema

```math
\bar\eta_m(R)
=
\sup_{\nu\in\mathcal B_\nu}
\eta_m[\omega(\nu)R/c].
```

Applying the weighted passive cut to the sector observations before summing gives, independently at either endpoint,

```math
\Gamma_{\rm coh}
\le
\frac{G\Omega^4}{5c^5}
\left[
4\bar\eta_2 I_{\hat R}
+
\bar\eta_1(2I_{\hat R}+4Z_{\hat R})
+
\bar\eta_0\left(\frac23I_{\hat R}+\frac83Z_{\hat R}\right)
\right].
```

Taking the smaller endpoint therefore gives the finite-band geometry-resolved theorem

```math
\boxed{
\Gamma_{\rm coh}
\le
\frac{G\Omega^4}{5c^5}
\min[\mathcal G_A(R),\mathcal G_B(R)],
}
```

with `G_X(R)` equal to the bracketed sector resource for endpoint `X`.

In the far zone only the `|m|=2` propagation sector survives at order `R^-2`, giving

```math
\boxed{
\limsup_{R\to\infty}R^2\Gamma_{\rm coh}
\le
\frac{5G\Omega^4}{4c^3\omega_-^2}
\min(I_{\hat R,A},I_{\hat R,B}).
}
```

The transparent narrowband carrier form is

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{5G\omega_0^2}{4c^3R^2}
\min(I_{\hat R,A},I_{\hat R,B}).
}
```

This supersedes the older scalar `25/12 * I_2` closure in this derivation file.

## 7. High-frequency limitation remains independent

The modal rate

```math
\kappa_{g,n}
=
\frac{G\omega_n^4}{5c^5}\frac{q_n:q_n}{\mu_n}
```

is an on-shell linewidth at the mode's own resonance frequency. It must not be inserted unchanged as the low-frequency coupling of a far-detuned mode.

However, unweighted completeness does not by itself bound

```math
\sum_n\omega_n^4\frac{Q_{m,n}^2}{\mu_n}.
```

Therefore the retained-frequency ceiling cannot be removed merely by passing to an infinite-dimensional Hilbert space. A whole-spectrum inertia-only theorem still requires additional constitutive regularity, a microscopic cutoff, or a different frequency-domain sum rule.

## 8. Reduced non-Markovian dynamics are not automatically excluded

A non-Markovian reduced equation can arise by exactly eliminating passive degrees of freedom from a larger local-in-time system. Generalized-Langevin models of solids provide explicit examples in which projecting out a harmonic environment produces a memory kernel even though the enlarged system is Hamiltonian/passive.

For the present theorem the relevant question is therefore not whether a chosen reduced coordinate has memory. The relevant question is whether there exists an enlarged state space on which:

1. the dynamics is well posed and passive;
2. the selected drive/readout maps are bounded or otherwise admissible;
3. the retained gravitational observation is admissible and Hilbert--Schmidt;
4. the sector resource of Sec. 5 is finite.

If those conditions are established, the Gramian proof can be run on the enlarged state rather than on the reduced memory equation. Non-Markovianity of the reduced coordinate is then a representation effect, not a loophole.

A primary physical example of exact harmonic-environment elimination is:

- L. Stella, C. D. Lorenz, and L. Kantorovich, *Generalized Langevin equation: An efficient approach to nonequilibrium molecular dynamics of open systems*, Phys. Rev. B **89**, 134303 (2014), DOI `10.1103/PhysRevB.89.134303`.

## 9. Unbounded distributed systems require admissibility, not blanket rejection

The bounded-operator proof above does not automatically cover boundary-controlled PDEs or singular continuum couplings. But infinite-dimensional systems with unbounded internal/boundary operators can still be scattering passive and well posed.

A directly relevant systems reference is:

- O. J. Staffans and G. Weiss, *A Physically Motivated Class of Scattering Passive Linear Systems*, SIAM J. Control Optim. **50**, 3083--3112 (2012), DOI `10.1137/110846403`.

That work includes beam and Maxwell-type examples and proves energy-balance relations in a system-node framework.

Accordingly, the current theorem does **not** assert that every unbounded PDE or hereditary continuum is covered, but neither does it identify unboundedness or reduced memory with a violation of passivity. The missing work is an admissibility/trace proof for the particular gravitational observation and retained resource.

For bounded ideal linear elasticity, the normal-mode spectrum is discrete under standard free or clamped boundary conditions; see M. Capoferri, L. Friedlander, M. Levitin, and D. Vassiliev, *Two-Term Spectral Asymptotics in Linear Elasticity*, J. Geom. Anal. **33**, 242 (2023), DOI `10.1007/s12220-023-01269-y`. Only the standard discreteness statement is used here.

## 10. Canonical scope statement

The infinite-dimensional result should be summarized as follows:

> The sector-resolved passive cut holds for finite or countably infinite retained endpoint realizations on a separable Hilbert space when the chosen local-in-time representation is well posed and passive and the gravitational observation has the required finite trace. Reduced non-Markovianity does not by itself evade the bound if it can be lifted to such a realization. Arbitrary hereditary models, singular continuum baths, and unbounded boundary-control systems remain outside the proved class until admissibility and gravitational trace/resource closure are established.

This statement changes no numerical theorem coefficient.