# AGENTS.md — Canonical Research Recovery Point

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Checkpoint:** 2026-08-07, after the standalone Gaussian branch was adversarially closed and an explicit conserved four-spoke source-plus-actuator model was constructed.

This is the first file a new agent should read.

---

## 1. Operating rule

Try to kill every claim before trying to publish it.

Attack by

1. counterexample;
2. hidden assumption;
3. convention or normalization error;
4. singular limit;
5. stronger prior art under different terminology;
6. a general theorem that makes the result an immediate corollary;
7. numerical truncation artifacts;
8. omitted parts of a supposedly closed physical system;
9. scope inflation.

If a claim dies, update the documentation immediately.

---

## 2. Standalone Gaussian-channel branch: STOP

The Gaussian-channel work produced correct and useful mathematics, but the broad novelty claims collided with prior art.

### Rank-two Fock survival — prior art

Mele–Lami–Giovannetti already contain the finite Schmidt-rank-two Fock-pair survival result.

Read:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

### All finite binary coherent-pair survival — prior art in substance

A one-sided specialization of Filippov–Ziman's 2014 coherent-state witness, plus an invertible local filter on the untouched two-dimensional coherent-state support, implies the same all-finite-pair survival boundary.

Read:

- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`

### Matched coherent scale and exponential sign factor — already encoded in Filippov–Ziman

With their witness parameter

$$
1-\lambda=\frac{m}{\sqrt\tau},
$$

their one-sided witness contains exactly

$$
1-
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right]
$$

and generates the same matched coherent amplitude

$$
\frac{2\sqrt\tau a}{m}.
$$

Read:

- `THREE_ELEMENT_WITNESS_VS_FILIPPOV.md`
- `STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`

### Retain as tools

Keep the repository's compact Fock determinant, coherent-dyad proof, exact $2\times2$ PT compression, and weak-link absolute witness bound as lemmas/tools for the gravity calculation.

Do **not** restart a standalone Gaussian theorem paper unless a genuinely new operational result appears.

---

## 3. Current project priority: a genuinely closed gravitational source

The previous four-endpoint-mass source had a real vulnerability: prescribed accelerated masses alone do not define conserved stress-energy. An unspecified actuator might carry branch-dependent energy/stress and modify or cancel the claimed radiation.

That loophole has now been attacked with an explicit isolated source architecture.

Read first:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`

---

## 4. Explicit four-spoke source-plus-actuator model

Use

- one central hub;
- four identical finite-mass longitudinal elastic spokes of reference length $L$;
- endpoint mass $\mu$ on each spoke;
- one spoke pair along $x$ and one along $y$;
- spoke rest mass $m_r$ per spoke;
- longitudinal sound speed $c_s$;
- mirrored plus-mode motion between source branches.

The complete source is

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

For a compact conserved source define

$$
I_{ij}
=\frac1{c^2}\int d^3x\,T^{00}_{\rm tot}x_i x_j.
$$

Then

$$
\boxed{
\ddot I_{ij}=2\int d^3x\,T^{ij}_{\rm tot}.
}
$$

Thus internal stresses are required for conservation but are not an independent leading TT radiation term. Any real cancellation must appear in the **total energy quadrupole**.

---

## 5. Exact finite-spoke normal mode

Define

$$
\boxed{q\equiv\frac{\omega L}{c_s}.}
$$

For one spoke, normalized to endpoint displacement,

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
\frac{m_r}{\mu}
=q^2+\frac{q^4}{3}+O(q^6).
$$

No massless support is required.

---

## 6. Main conserved-source result: the actuator does not cancel the quadrupole

For branch $s=\pm1$, let the $x$ spokes move as

$$
\xi_x^{(s)}=s u_c(t)f_q(x),
$$

and the $y$ spokes as

$$
\xi_y^{(s)}=-s u_c(t)f_q(x).
$$

Including both endpoint masses and spoke rest mass, the exact leading branch-difference quadrupole is

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

For $0<q<\pi/2$,

$$
\frac{\tan q}{q}>1.
$$

Therefore the finite support **reinforces** rather than cancels the endpoint quadrupole.

For $q\ll1$,

$$
\boxed{
\frac{\tan q}{q}
=1+\frac{q^2}{3}+\frac{2q^4}{15}+O(q^6).
}
$$

The previous endpoint-only result is the controlled $q\to0$ limit.

---

## 7. Correct finite-spoke mode mass and quantum matrix element

The exact generalized mode mass is

$$
\boxed{
M_{\rm eff}(q)
=4\mu
\left[
\frac12+\frac{q}{\sin2q}
\right].
}
$$

Define

$$
\boxed{
A(q)=\frac12+\frac{q}{\sin2q}.
}
$$

Then

$$
A(q)
=1+\frac{q^2}{3}+\frac{7q^4}{45}+O(q^6).
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
=4\mu L\frac{\tan q}{q}u,
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

## 8. Correct finite-spoke graviton linewidth

For a plus mode, the repository convention gives

$$
\kappa_g
=\frac{4G\omega^5}{5\hbar c^5}|q_{01}|^2.
$$

Therefore

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\mathcal C_\kappa(q),
}
$$

where

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

Thus the endpoint-only linewidth

$$
\frac{8G\mu L^2\omega^4}{5c^5}
$$

is again the controlled $q\to0$ limit.

---

## 9. Causal-support lower bound

Let

$$
\beta=\frac{\omega L}{c}.
$$

Causality requires

$$
c_s\le c,
$$

hence

$$
q\ge\beta.
$$

For $\beta\ll1$, the stiffest causal support has parametrically

$$
\boxed{
\frac{m_r}{\mu}\gtrsim\beta^2
}
$$

and the minimum support correction to the classical quadrupole is

$$
\boxed{
\frac{\Delta Q}{\Delta Q_{\rm end}}-1
\gtrsim\frac{\beta^2}{3}.
}
$$

The physically relevant endpoint approximation criterion is therefore

$$
q=\omega L/c_s\ll1,
$$

not an unphysical massless actuator.

---

## 10. Controller does not need to become a which-branch record

Use an autonomous source-control Hamiltonian

$$
\boxed{
H=H_m(u,p_u)+H_c(q_c,p_c)-\sigma_z g(q_c)u,
}
$$

with $H_m$ parity even.

For branch $s$,

$$
u_s=s u_c.
$$

The controller backreaction contains

$$
\sigma_z u_s=u_c,
$$

which is branch independent.

More strongly, with mechanical parity $P_u$, define

$$
U_P
=|+\rangle\langle+|\otimes I
+|-\rangle\langle-|\otimes P_u.
$$

Then

$$
U_P^\dagger uU_P=\sigma_z u,
$$

and

$$
\boxed{
U_P^\dagger H U_P
=H_m+H_c-g(q_c)u.
}
$$

Before gravitational coupling is included, the controller/work reservoir can therefore follow identical quantum dynamics in both source branches. The actuator need not acquire a hidden classical branch record.

---

## 11. Controlled approximation regime

Use

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

Finite spoke inertia is included explicitly. Remaining kinetic/internal-energy corrections to $T^{00}$ are relativistically suppressed and branch-even at first order under the mirrored source symmetry.

---

## 12. Immediate next tasks

A new agent should **not** restart the Gaussian novelty branch.

Proceed in this order:

### Priority 1 — propagate finite-spoke corrections through the source formulas

Update the legacy endpoint-only source notes so that

- endpoint expressions are explicitly labeled as $q\to0$ limits;
- $M_{\rm eff}(q)$;
- $q_{01}^{\rm tot}(q)$;
- $\kappa_g(q)$;
- $\Delta Q(q)$

are used in the current source model.

### Priority 2 — re-audit emitted coherent-graviton distance

For a prescribed outer displacement $u_c(t)$, the classical branch quadrupole amplitude acquires

$$
\frac{\tan q}{q}.
$$

Therefore the emitted branch-distance formula should acquire

$$
\left(\frac{\tan q}{q}\right)^2
$$

relative to the endpoint-only prescribed-displacement expression, modulo the same narrowband assumptions.

For a quantum single-mode normalization, use the corrected $q_{01}$ and $\kappa_g(q)$ consistently.

### Priority 3 — re-audit source→receiver link

Every downstream expression that uses $\kappa_{g,A}$ or $\kappa_{g,B}$ should be corrected by the appropriate

$$
\mathcal C_\kappa(q_A),
\qquad
\mathcal C_\kappa(q_B)
$$

factors.

Check whether any qualitative scaling changes. The expectation is no: only controlled multiplicative $1+O(q^2)$ corrections in the endpoint-dominated regime.

### Priority 4 — attack the hub/controller residual

The next source-level adversarial question is finite hub/control extent and branch-dependent internal energy beyond the ideal parity-symmetric model. Bound its contribution in powers of

$$
r_h/L,
\qquad
v^2/c^2,
\qquad
\mathcal C.
$$

### Priority 5 — gravity paper, not another generic Gaussian paper

Once the corrected source→receiver formulas are propagated, re-evaluate `PAPER_CORE_V3.md` around the conserved total source.

---

## 13. Canonical reading order

1. `AGENTS.md`
2. `experiments/01-causal-quantum-branch-information/CONSERVED_SOURCE_ACTUATOR_AUDIT.md`
3. `experiments/01-causal-quantum-branch-information/STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
4. `experiments/01-causal-quantum-branch-information/CURRENT_STATE_RANK2_UPDATE.md`
5. `experiments/01-causal-quantum-branch-information/CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`
6. `experiments/01-causal-quantum-branch-information/QUANTIZED_PLUS_MODE_SOURCE.md`
7. `experiments/01-causal-quantum-branch-information/EXPLICIT_FOUR_MASS_SOURCE_RECEIVER_LINK.md`
8. `experiments/01-causal-quantum-branch-information/PAPER_CORE_V3.md`

---

## 14. Stop/go

### STOP

- standalone rank-two Fock theorem paper;
- standalone all-binary-coherent survival theorem paper;
- attempts to manufacture generic Gaussian novelty from the three-element witness alone.

### GO

- finite-support conserved source;
- corrected source-mode quantization;
- corrected source→receiver coupling;
- full gravity-specific adversarial audit.
