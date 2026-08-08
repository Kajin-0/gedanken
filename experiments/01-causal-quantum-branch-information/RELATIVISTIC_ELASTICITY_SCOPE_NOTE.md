# Relativistic Elasticity Scope Note for the Four-Spoke Source

**Date:** 2026-08-07  
**Status:** **SCOPE CORRECTION — THE FINITE-SPOKE SOURCE IS CONTROLLED IN A NONRELATIVISTIC ELASTIC REGIME; THE $c_s\to c$ MASS BOUND IS ONLY PARAMETRIC UNTIL A COVARIANT ELASTIC ACTION IS SPECIFIED**

## 1. Why this correction is needed

The conserved-source audit uses the linear longitudinal rod equation

$$
\rho A\ddot\xi
=EA\,\xi'',
$$

with

$$
c_s^2=E/\rho.
$$

For a spoke of rest mass

$$
m_r=\rho AL
$$

and endpoint mass $\mu$, the exact boundary condition inside this model gives

$$
\boxed{
\frac{m_r}{\mu}=q\tan q,
\qquad
q=\frac{\omega L}{c_s}.
}
$$

This is exact for the linear nonrelativistic elastic-spoke model.

Earlier notes combined it with

$$
c_s\le c
$$

to write the stiff-limit estimate

$$
m_r/\mu\gtrsim\beta^2,
\qquad
\beta=\omega L/c.
$$

The scaling is plausible, but calling the numerical coefficient a universal relativistic lower bound would overreach the model.

---

## 2. What is rigorous inside the current model

Choose a material/ideal elastic medium satisfying

$$
\boxed{c_s\ll c}
$$

so that ordinary linear elasticity is self-consistent.

Require simultaneously

$$
\boxed{
\beta=\frac{\omega L}{c}\ll q=\frac{\omega L}{c_s}\ll1.
}
$$

This hierarchy is possible because

$$
c_s/c\ll1.
$$

In this regime

1. the mechanical support is nonrelativistic;
2. the exact spoke mode relation
   $$m_r/\mu=q\tan q$$
   is valid within the model;
3. the endpoint-dominated expansion is controlled;
4. the gravitational compact-source expansion is even better controlled because
   $$\beta\ll q\ll1.$$

No relativistically stiff material is required for the Gedanken construction.

---

## 3. Controlled small-$q$ result

Within the nonrelativistic spoke model,

$$
\boxed{
\frac{m_r}{\mu}
=q^2+\frac{q^4}{3}+O(q^6).
}
$$

The support correction to the branch quadrupole is

$$
\boxed{
\frac{\Delta Q}{\Delta Q_{\rm end}}
=
1+\frac{q^2}{3}+O(q^4).
}
$$

The linewidth correction is

$$
\boxed{
\mathcal C_\kappa(q)
=1+\frac{q^2}{3}+O(q^4).
}
$$

These are the source results that should be used in the paper.

---

## 4. What causality alone implies

Independently of the Newtonian rod model, a physically causal longitudinal signal speed obeys

$$
\boxed{c_s\le c.}
$$

Therefore

$$
\boxed{q\ge\beta.}
$$

This is the robust causal statement.

It implies that a source satisfying

$$
q\ll1
$$
nautomatically satisfies

$$
\beta\ll1.
$$

Thus the elastic endpoint-dominated regime is compatible with the gravitational long-wavelength regime.

---

## 5. What is not yet a rigorous universal bound

The expression

$$
\frac{m_r}{\mu}=q\tan q
$$

should **not** be extrapolated all the way to

$$
c_s=c
$$

and then advertised as an exact universal relativistic minimum support mass unless the same boundary-value problem has been derived from a covariant relativistic elastic action.

Near relativistic stiffness,

- inertial mass density includes relativistic energy/stress contributions;
- the relation between elastic modulus, energy density, and signal speed is model dependent;
- endpoint traction/inertia matching should be derived from the full relativistic stress-energy tensor.

The parametric expectation

$$
m_r/\mu=O(\beta^2)
$$

for an endpoint-dominated maximally stiff support may survive, but its exact coefficient is not established by the current Newtonian rod derivation.

---

## 6. Relativistic completion is available in principle

Relativistic elasticity and relativistic rod/string models provide covariant actions and conserved stress-energy tensors with causal characteristic speeds.

A future refinement can replace the Newtonian spoke Lagrangian by a relativistic elastic action and repeat

1. the mode-shape calculation;
2. endpoint traction matching;
3. total energy-quadrupole integration;
4. small-$q$ expansion.

This is a refinement, not a prerequisite for the current controlled regime, because the paper can stay inside

$$
\boxed{
\beta\ll q\ll1,
\qquad
c_s\ll c.
}
$$

---

## 7. Recommended manuscript language

Use:

> We model each support as a finite-mass linear elastic spoke with longitudinal sound speed $c_s$ in the controlled nonrelativistic regime $c_s\ll c$ and $\beta\ll q=\omega L/c_s\ll1$. The exact spoke model gives $m_r/\mu=q\tan q$ and finite-support corrections $1+O(q^2)$. Causality independently implies $q\ge\beta$, so this elastic regime automatically lies inside the gravitational compact-source regime.

Do not use:

> Causality universally forces $m_r/\mu\ge\beta^2$ with exact coefficient one.

without a separate covariant relativistic-elastic derivation.

---

## 8. Adversarial verdict

This scope correction does not damage the main conserved-source result.

The source does not require a support with

$$
c_s\sim c.
$$

It only requires a hierarchy such as

$$
\boxed{
\beta\ll q\ll1,
}

which can be realized within a nonrelativistic elastic model by making the gravitational source sufficiently compact relative to its radiation wavelength.

The exact cancellation test and finite-spoke quadrupole formulas remain valid inside that controlled regime.
