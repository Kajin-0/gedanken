# Standalone Gaussian-Theorem Branch — Adversarial Novelty Verdict

**Date:** 2026-08-07  
**Status:** **STOP AS A STANDALONE THEOREM PAPER; RETAIN AS LEMMAS/TOOLS FOR THE GRAVITY APPLICATION**

## 1. Purpose

The Gaussian-channel branch emerged from Experiment 01 and briefly appeared strong enough to support an independent continuous-variable quantum-information paper.

After adversarial proof review and prior-art search, that publication path should now be stopped.

The mathematics remains useful. The headline novelty does not.

---

## 2. What survived mathematically

### Rank-two Fock determinant

For

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}},
$$

one selected partial-transpose block has

$$
\boxed{
\det M_s
=\frac{s^2}{(1+s^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

### Binary coherent exact principal minor

For symmetric $|\pm a\rangle$,

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

### Absolute selected-block negativity bound

For

$$
M_v=\begin{pmatrix}p_0&z_v^*\\z_v&p_v\end{pmatrix},
$$

$$
\boxed{
G(v)=\frac12
\max\left\{0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}
}
$$

is a rigorous lower bound on the full output negativity.

### Weak-link optimized asymptotic

For

$$
\tau,m\ll1,
\qquad
m/\tau<1,
$$

joint optimization over source amplitude and coherent analysis displacement gives

$$
\boxed{
G_{\rm abs}^{\rm opt}
=\frac{W(e^{-1})}{2}
(\tau-m)+O(\tau^2),
}
$$

with

$$
\frac{W(e^{-1})}{2}
\simeq0.1392322714,
$$

and

$$
\boxed{
a_*
\simeq0.565346\sqrt\tau.}
$$

These calculations remain internally useful and have survived the current algebraic audits.

---

## 3. Why the original standalone novelty case died

### Collision 1 — Mele–Lami–Giovannetti

The phase-insensitive finite Schmidt-rank-two Fock survival result was already contained in their finite-Fock-pair protocol.

See:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

### Collision 2 — Filippov–Ziman

Their 2014 weighted coherent-state witness implies the one-sided all-finite-binary-coherent survival result after specialization and an invertible local filter on the untouched two-dimensional coherent-state support.

See:

- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`

### Collision 3 — matched coherent scale and exponential factor are already encoded in Filippov–Ziman

Choosing their witness parameter

$$
\boxed{
1-\lambda=t=\frac{m}{\sqrt\tau}
}
$$

makes their exact one-sided witness expectation proportional to

$$
1-
\exp\left[
\frac{|\gamma|^2}{m}(\tau-m)
\right].
$$

With

$$
|\gamma|=2a,
$$

this is exactly

$$
1-
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
$$

Their weighted EPR kernel maps

$$
\gamma\mapsto\gamma^*/t,
$$

so the same choice gives

$$
\frac{\gamma}{t}
=\frac{2\sqrt\tau a}{m}
=v_*.
$$

Thus even the matched coherent displacement and exact exponential resource factor are already algebraically implicit in the 2014 witness family.

See:

- `THREE_ELEMENT_WITNESS_VS_FILIPPOV.md`

---

## 4. What may still be technically original

The following specific packaging may not have appeared explicitly in the literature searched so far:

1. one literal $2\times2$ principal minor of the actual partial transpose;
2. the statement that two selected populations plus one coherence suffice for this exact known-channel state family;
3. the explicit selected-block negative eigenvalue as a negativity lower bound;
4. the weak-link Lambert-$W$ optimization coefficient
   $$W(e^{-1})/2.$$

No exact prior-art collision for the Lambert-$W$ coefficient was found in targeted searches.

However, these are now best regarded as **proof compression and quantitative corollaries of known entanglement-survival structure**, not a new channel theorem.

The $2\times2$ eigenvalue formula and negativity interlacing argument are elementary once the compression is chosen. The remaining novelty is therefore too narrow to support the original standalone-paper ambition without a substantial new operational implementation or a stronger quantitative theorem.

---

## 5. Publication decision

### Do not write

Do not write a standalone manuscript whose central claim is any of the following:

- Schmidt-rank-two sufficiency for one-mode Gaussian non-EB channels;
- every finite binary coherent pair survives iff the channel is non-EB;
- discovery of the matched displacement $v_*$ or the exponential sign factor as new underlying physics.

### Retain

Retain the repository derivations as

- short independent proofs;
- exact lemmas;
- low-dimensional witnesses;
- quantitative lower bounds;
- tools for the source→receiver gravitational calculation.

### Possible later note

Only revisit a standalone quantum-information note if a genuinely new operational result emerges, for example an experimentally realistic protocol that recovers $z_v$ with a provably minimal measurement set and materially outperforms known coherent-state/witness schemes.

---

## 6. Why the gravity application should now regain priority

The generic Gaussian-channel statements are heavily occupied by prior art.

The gravity application contains project-specific structure that the prior-art collisions do not remove:

- explicit conserved branch-dependent source history;
- quantized quadrupole emission;
- retarded source→receiver mode overlap;
- finite-aperture/state-storage normalization;
- thermal receiver capability window;
- causal spacetime certification bubble;
- source-strength versus uncollected-which-branch-information tradeoffs.

The strongest unresolved gravity-specific technical vulnerability is still:

> **the complete conserved stress-energy of the branch-dependent actuator/control system that drives the explicit four-mass quadrupole source.**

Until that is closed, the source model can be attacked on the ground that an unspecified actuator may carry compensating branch-dependent stress-energy and alter or cancel the claimed gravitational radiation/coupling.

That is now the highest-value technical problem in the repository.

---

## 7. Next action

Return to the gravity branch and construct an explicit, internally conserved source-plus-actuator model satisfying

$$
\boxed{\partial_\mu T^{\mu\nu}_{\rm total}=0}
$$

throughout the complete branch history.

Then recompute the radiative branch-difference quadrupole and source→receiver coupling using the **total** conserved $T^{\mu\nu}$ rather than only the endpoint masses.

The goal is adversarial:

1. determine whether the control stress-energy modifies the claimed radiation at leading order;
2. identify any exact conservation cancellation;
3. establish the minimal source architecture whose branch-dependent radiative multipole survives after the actuator is included;
4. only then rebuild the gravity paper around the conserved total source.
