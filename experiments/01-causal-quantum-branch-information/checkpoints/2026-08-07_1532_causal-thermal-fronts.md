# Checkpoint — 2026-08-07 15:32 EDT

## Canonical new results

### Minimal weak-cat PPT witness

Measure

$$
P_{+,1}=\langle +,1|\rho|+,1\rangle,
\qquad
P_{-,0}=\langle -,0|\rho|-,0\rangle,
$$

and

$$
Z_0=\langle -,1|\rho|+,0\rangle.
$$

Every PPT source-receiver state obeys

$$
\boxed{|Z_0|^2\le P_{+,1}P_{-,0}}.
$$

For the weak source-cat after a thermal attenuator this turns on at the exact entanglement-breaking boundary

$$
\boxed{\eta>\frac{\bar n}{\bar n+1}}.
$$

Thus the fundamental thermal entanglement threshold is operationally reachable without full tomography.

### Causal thermal fronts

For normalized gravitational difference-mode envelope $f$ and eventual coherent efficiency $\eta_\infty$,

$$
\eta(T,R)=\eta_\infty F(T-R/c),
\qquad
F(s)=\int_{-\infty}^{s}|f(t)|^2dt.
$$

Classical signal front:

$$
T_c=R/c.
$$

Weak-cat NPT front:

$$
\boxed{
T_{\rm NPT}
=\frac Rc+F^{-1}\left(\frac{\eta_{\rm ent}}{\eta_\infty}\right),
\quad
\eta_{\rm ent}=\frac{\bar n}{\bar n+1}.
}
$$

Global fidelity-history front:

$$
\boxed{
T_F
=\frac Rc+F^{-1}\left(\frac{\eta_F}{\eta_\infty}\right),
\quad
\eta_F=\frac{2\bar n+1}{2\bar n+2}.
}
$$

When all exist,

$$
\boxed{T_c\le T_{\rm NPT}<T_F.}
$$

Finite temperature therefore creates a genuine post-light-cone delay between arrival of a classical gravitational response and survival of gravitationally transported entanglement.

## Immediate next task

Derive the same front structure directly from the matched receiver Langevin/input-output equations and determine the critical slowing near

$$
\kappa_g=\bar n_i\kappa_i.
$$