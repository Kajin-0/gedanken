# Current State Addendum — Conserved Source Checkpoint

**Date:** 2026-08-07  
**Status:** Canonical recovery point after adversarial closure of the standalone Gaussian branch and construction of an explicit conserved four-spoke gravity source.  
**Read first:** root `AGENTS.md`.

## 1. Executive verdict

The project has returned to the gravity problem.

Two broad Gaussian-channel novelty claims were mathematically correct but collided with prior art:

1. finite rank-two Fock survival — Mele–Lami–Giovannetti;
2. all-finite-binary-coherent survival — Filippov–Ziman.

The remaining three-element Gaussian witness and weak-link negativity formulas are retained as compact lemmas/quantitative tools, not as the center of a standalone theorem paper.

Read:

- `STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
- `NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `THREE_ELEMENT_WITNESS_VS_FILIPPOV.md`

The highest-value open issue was then the gravity source itself: **does a complete conserved actuator/support stress-energy modify or cancel the branch-dependent quadrupole derived from four prescribed endpoint masses?**

An explicit finite-mass source model now answers that question at leading controlled order.

---

## 2. Explicit isolated four-spoke source

Use

- a central hub;
- four identical elastic spokes of reference length $L$;
- one endpoint mass $\mu$ on each spoke;
- one spoke pair along $x$ and one along $y$;
- one-spoke rest mass $m_r$;
- longitudinal sound speed $c_s$.

The complete isolated source contains endpoints, spokes, hub, and controller:

$$
T^{\mu\nu}_{\rm tot}
=T^{\mu\nu}_{\rm end}
+T^{\mu\nu}_{\rm spokes}
+T^{\mu\nu}_{\rm hub}
+T^{\mu\nu}_{\rm ctrl},
$$

with

$$
\boxed{\partial_\mu T^{\mu\nu}_{\rm tot}=0.}
$$

For the total energy quadrupole

$$
I_{ij}=\frac1{c^2}\int T^{00}_{\rm tot}x_ix_j\,d^3x,
$$

conservation gives

$$
\boxed{
\ddot I_{ij}=2\int T^{ij}_{\rm tot}\,d^3x.
}
$$

Thus the internal stresses required to accelerate the endpoints are already encoded consistently in the total quadrupole representation of the leading far-zone source. A cancellation can occur only through the total $T^{00}$ quadrupole itself.

Canonical derivation:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`

---

## 3. Exact longitudinal spoke mode

Define

$$
\boxed{q=\frac{\omega L}{c_s}.}
$$

The normalized longitudinal spoke mode is

$$
\boxed{
f_q(x)=\frac{\sin(qx/L)}{\sin q}.}
$$

The endpoint traction boundary condition gives

$$
\boxed{
\frac{m_r}{\mu}=q\tan q.
}
$$

For the endpoint-dominated fundamental mode,

$$
q\ll1,
$$

$$
\boxed{
\frac{m_r}{\mu}=q^2+\frac{q^4}{3}+O(q^6).
}
$$

The old endpoint approximation therefore does not require a massless support. It requires a finite support whose inertia is parametrically small because $q\ll1$.

---

## 4. Main source result: no leading actuator cancellation

For source branch $s=\pm1$, choose mirrored plus-mode displacements

$$
\xi_x^{(s)}=s u_c(t)f_q(x),
$$

$$
\xi_y^{(s)}=-s u_c(t)f_q(x).
$$

Including endpoint rest mass and spoke rest mass, the exact leading branch-difference quadrupole is

$$
\boxed{
\Delta Q_{xx}
=8\mu L u_c\frac{\tan q}{q},
}
$$

$$
\boxed{
\Delta Q_{yy}
=-8\mu L u_c\frac{\tan q}{q}.
}
$$

For the fundamental interval

$$
0<q<\pi/2,
$$

$$
\frac{\tan q}{q}>1.
$$

Therefore the finite support does **not** cancel the endpoint quadrupole. It reinforces it.

For $q\ll1$,

$$
\boxed{
\frac{\tan q}{q}
=1+\frac{q^2}{3}+\frac{2q^4}{15}+O(q^6).
}
$$

The previous endpoint result

$$
\Delta Q_{xx}=8\mu L u_c
$$

is the controlled $q\to0$ limit.

---

## 5. Correct mode inertia and quadrupole transition matrix element

Define

$$
\boxed{
A(q)=\frac12+\frac{q}{\sin2q}.
}
$$

Then the exact generalized mode mass is

$$
\boxed{
M_{\rm eff}(q)=4\mu A(q).
}
$$

Its small-$q$ expansion is

$$
\boxed{
A(q)
=1+\frac{q^2}{3}+\frac{7q^4}{45}+O(q^6).
}
$$

The zero-point coordinate is

$$
\boxed{
u_{\rm zpf}(q)
=\sqrt{\frac{\hbar}{2M_{\rm eff}(q)\omega}}.
}
$$

The one-branch quadrupole operator is

$$
\delta Q_{xx}
=4\mu L\frac{\tan q}{q}\,u,
$$

so

$$
\boxed{
q_{01}^{\rm tot}(q)
=4\mu L\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}(q)\omega}}.
}
$$

Relative to the endpoint-only matrix element,

$$
\boxed{
\mathcal C_Q(q)
=\frac{\tan q/q}{\sqrt{A(q)}}
=1+\frac{q^2}{6}+\frac{q^4}{24}+O(q^6).
}
$$

---

## 6. Correct gravitational linewidth

The plus-mode spontaneous graviton linewidth becomes

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\mathcal C_\kappa(q),
}
$$

with

$$
\boxed{
\mathcal C_\kappa(q)
=\frac{(\tan q/q)^2}{A(q)}.
}
$$

For $q\ll1$,

$$
\boxed{
\mathcal C_\kappa(q)
=1+\frac{q^2}{3}+\frac{q^4}{9}+O(q^6).
}
$$

Thus all endpoint-only linewidth formulas remain correct as the leading $q\to0$ term.

---

## 7. Causal support requirement

Let

$$
\beta=\frac{\omega L}{c}.
$$

Causality implies

$$
c_s\le c,
$$

so

$$
q\ge\beta.
$$

For $\beta\ll1$, a maximally stiff causal support has parametrically

$$
\boxed{
\frac{m_r}{\mu}\gtrsim\beta^2
}
$$

and the unavoidable support correction to the classical quadrupole is only

$$
\boxed{
\frac{\Delta Q}{\Delta Q_{\rm end}}-1
\gtrsim\frac{\beta^2}{3}.
}
$$

The correct small parameter is therefore

$$
q=\omega L/c_s,
$$

not an assumption of an infinitely rigid or massless actuator.

---

## 8. Controller can remain branch common

Use the autonomous projected Hamiltonian

$$
\boxed{
H=H_m(u,p_u)+H_c(q_c,p_c)-\sigma_zg(q_c)u,
}
$$

with $H_m$ parity even.

For branch $s$, the mirrored mechanical solution is

$$
u_s=s u_c.
$$

The force back on the controller contains

$$
\sigma_z u_s=u_c,
$$

which is branch independent.

With controlled mechanical parity

$$
U_P
=|+\rangle\langle+|\otimes I
+|-\rangle\langle-|\otimes P_u,
$$

one finds

$$
\boxed{
U_P^\dagger H U_P
=H_m+H_c-g(q_c)u.
}
$$

Thus before gravitational coupling is included, the work reservoir need not acquire a hidden which-branch record. Gravitational coupling is the intended sector that carries the branch sign.

---

## 9. Controlled approximation regime

The explicit source is controlled when

$$
\boxed{|u|/L\ll1,}
$$

$$
\boxed{q=\omega L/c_s\ll1,}
$$

$$
\boxed{\beta=\omega L/c\ll1,}
$$

$$
\boxed{\mathcal C=2GM/(c^2L)\ll1.}
$$

Finite spoke inertia is already included exactly at linear order. Remaining kinetic/elastic contributions to $T^{00}$ are relativistically small and branch-even at first order under the mirror symmetry.

---

## 10. Immediate technical work

The next task is propagation, not invention of another source architecture.

Update all downstream formulas that used the endpoint-only source:

1. `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md` — identify endpoint formulas as $q\to0$ limits;
2. `QUANTIZED_PLUS_MODE_SOURCE.md` — replace $M_{\rm eff}$, $q_{01}$, and $\kappa_g$ by the finite-spoke forms;
3. emitted coherent-graviton distance — include $(\tan q/q)^2$ for a fixed prescribed outer displacement;
4. source→receiver link — include $\mathcal C_\kappa(q_A)$ and $\mathcal C_\kappa(q_B)$ wherever the source/receiver gravitational linewidth appears;
5. paper core — formulate the gravitational source through total conserved stress-energy rather than accelerated point masses.

The expected result is a controlled multiplicative correction

$$
1+O(q^2),
$$

not a qualitative change. This must be checked rather than assumed.

---

## 11. Remaining gravity-specific vulnerability

The leading actuator cancellation loophole is closed for the explicit four-spoke architecture.

The next adversarial source question is the finite spatial extent and branch-dependent internal energy of the hub/controller beyond the ideal controlled-parity model.

The target is a bound on its branch quadrupole contribution in powers of

$$
r_h/L,
\qquad
v^2/c^2,
\qquad
\mathcal C.
$$

If those corrections are parametrically below the explicit plus quadrupole, the source will be publication-grade at the level appropriate to a Gedanken calculation.

---

## 12. Publication priority

Do not return to the standalone Gaussian theorem paper.

The publication path is now the gravity application built around

- a conserved finite-support source;
- quantized plus-mode emission;
- retarded free-space propagation;
- a noisy receiver channel;
- a finite NPT/EB witness retained from the Gaussian lemmas;
- explicit source and receiver error budgets.
