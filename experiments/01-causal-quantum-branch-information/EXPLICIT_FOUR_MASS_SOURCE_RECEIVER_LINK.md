# Explicit Conserved Four-Spoke Source-to-Receiver Link

**Updated:** 2026-08-07  
**Status:** Current leading-order source→receiver parameter chain with finite-support conservation corrections.

This file supersedes the endpoint-only normalization previously used here. The old formulas are recovered in the controlled

$$
q_A,q_B\to0
$$
limit.

Canonical source derivations:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`
- `QUANTIZED_PLUS_MODE_SOURCE.md`

---

## 1. Finite-spoke correction functions

For each plus mode define

$$
\boxed{
q\equiv\frac{\omega L}{c_s},
}
$$

and

$$
\boxed{
A(q)=\frac12+\frac{q}{\sin2q}.
}
$$

The quadrupole transition-matrix correction is

$$
\boxed{
\mathcal C_Q(q)
=\frac{\tan q/q}{\sqrt{A(q)}}.
}
$$

The gravitational linewidth correction is

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

The endpoint-only source/receiver corresponds to

$$
\mathcal C_\kappa\to1.
$$

---

## 2. Receiver gravitational linewidth

Let the receiver endpoint mass be

$$
\mu_B
$$

and define the total endpoint mass

$$
\boxed{M_{e,B}=4\mu_B.}
$$

Do not confuse $M_{e,B}$ with the full mechanical rest mass including spokes, hub, and control system.

The corrected receiver plus-mode graviton linewidth is

$$
\boxed{
\kappa_{g,B}(q_B)
=
\frac{8G\mu_BL_B^2\omega^4}{5c^5}
\mathcal C_\kappa(q_B).
}
$$

Equivalently,

$$
\boxed{
\kappa_{g,B}(q_B)
=
\frac{2GM_{e,B}L_B^2\omega^4}{5c^5}
\mathcal C_\kappa(q_B).
}
$$

---

## 3. Useful loading rate from one normalized incoming source mode

For aligned plus source and receiver modes in the wave zone,

$$
\boxed{
\kappa_\Delta(R)
=
\frac{25\mathcal O}{16(kR)^2}
\kappa_{g,B}(q_B),
}
$$

where

$$
k=\omega/c
$$

and $\mathcal O$ contains tensor/temporal/polarization mode overlap.

Therefore

$$
\boxed{
\kappa_\Delta(R,q_B)
=
\frac{5\mathcal O}{8}
\frac{GM_{e,B}L_B^2\omega^2}
{c^3R^2}
\mathcal C_\kappa(q_B).
}
$$

In endpoint notation,

$$
\boxed{
\kappa_\Delta(R,q_B)
=
\frac{5\mathcal O}{2}
\frac{G\mu_BL_B^2\omega^2}
{c^3R^2}
\mathcal C_\kappa(q_B).
}
$$

### Important separation of resources

The source finite-spoke correction does **not** enter this loading rate separately once the incoming source branch mode has been normalized.

Source strength determines the coherent distance carried by that normalized mode. Receiver loading depends on the receiver's own gravitational linewidth and spatial/mode overlap.

This prevents double-counting the source support correction.

---

## 4. Receiver quality-factor form

Let ordinary receiver loss dominate,

$$
\kappa\simeq\omega/Q_B.
$$

Then

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=
\frac{5\mathcal O}{8}
\frac{GM_{e,B}L_B^2\omega Q_B}
{c^3R^2}
\mathcal C_\kappa(q_B).
}
$$

Define the endpoint-mass compactness parameter

$$
\boxed{
\mathcal C_{e,B}
=\frac{2GM_{e,B}}{c^2L_B},
}
$$

and

$$
\boxed{
\beta_B=\frac{\omega L_B}{c}.
}
$$

At

$$
kR=\zeta,
$$

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=
\frac{5\mathcal O}{16\zeta^2}
Q_B\mathcal C_{e,B}\beta_B^3
\mathcal C_\kappa(q_B).
}
$$

The core passive scaling remains

$$
Q\mathcal C\beta^3,
$$

with only a controlled finite-support multiplier.

---

## 5. Relation to total mechanical mass

The four spokes contribute total rest mass

$$
4m_{r,B}
=4\mu_Bq_B\tan q_B.
$$

Ignoring a central hub/control mass for the moment,

$$
M_{\rm mech,B}
=4\mu_B[1+q_B\tan q_B].
$$

Thus

$$
M_{e,B}
=\frac{M_{\rm mech,B}}
{1+q_B\tan q_B}.
$$

If one wants to express the coupling using the total spoke+endpoint mechanical compactness

$$
\mathcal C_{\rm mech,B}
=\frac{2GM_{\rm mech,B}}{c^2L_B},
$$

then

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=
\frac{5\mathcal O}{16\zeta^2}
Q_B\mathcal C_{\rm mech,B}\beta_B^3
\frac{\mathcal C_\kappa(q_B)}
{1+q_B\tan q_B}.
}
$$

For $q_B\ll1$,

$$
\frac{\mathcal C_\kappa(q_B)}{1+q_B\tan q_B}
=1-\frac{2q_B^2}{3}+O(q_B^4).
$$

This is an important bookkeeping distinction: at fixed endpoint mass, spoke inertia slightly raises the quadrupole linewidth; at fixed **total** mechanical mass, allocating mass into the support instead of endpoints produces a small reduction.

---

## 6. Maximum capture of the normalized $\sin^4$ source mode

For

$$
f_4(t)
=\sqrt{\frac{128}{35T}}
\sin^4(\pi t/T),
$$

the previously derived vacuum signal optimization gives

$$
S_{4,*}\simeq0.7980213.
$$

Therefore

$$
\boxed{
\eta_{\max}
\simeq
S_{4,*}\frac{\kappa_\Delta}{\kappa}.
}
$$

At $kR=\zeta$,

$$
\boxed{
\eta_{\max}^{\rm WZ}
\simeq
0.249382
\frac{\mathcal O}{\zeta^2}
Q_B\mathcal C_{e,B}\beta_B^3
\mathcal C_\kappa(q_B).
}
$$

Thus the finite-support correction does not change the weak-capture scaling; it multiplies it by

$$
1+O(q_B^2).
$$

---

## 7. Weak-capture source–receiver negativity

For a pure-loss link with

$$
\eta\ll1,
$$

the exact binary-cat source–receiver negativity optimized over emitted branch distance has leading behavior

$$
\mathcal N_{\max}
=\eta+O(\eta^{3/2}).
$$

Hence

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\simeq
0.249382
\frac{\mathcal O}{\zeta^2}
Q_B\mathcal C_{e,B}\beta_B^3
\mathcal C_\kappa(q_B)
}
$$

at leading order.

The previously derived subleading term

$$
-2\eta^{3/2}
$$

is unchanged because it belongs to the pure-loss information-flow problem after the capture fraction has been specified.

---

## 8. Minimal selected-block witness strength

The retained Gaussian lemma gives, in the weak-link limit,

$$
G_{\rm abs}^{\rm opt}
\simeq
\frac12W(e^{-1})\eta.
$$

Therefore

$$
\boxed{
G_{\rm abs,max}^{\rm WZ}
\simeq
0.0347220
\frac{\mathcal O}{\zeta^2}
Q_B\mathcal C_{e,B}\beta_B^3
\mathcal C_\kappa(q_B).
}
$$

This is retained as a quantitative witness bound, not a standalone Gaussian novelty claim.

---

## 9. Thermal non-EB capability condition

For the $\sin^4$ waveform, the receiver optimization gives

$$
H_{4,*}\simeq0.8136763.
$$

A non-EB interval requires

$$
\boxed{
\Gamma_{\rm th}
< H_{4,*}\kappa_\Delta.
}
$$

For one dominant bath with

$$
\Gamma_{\rm th}
=\bar n\frac{\omega}{Q_B},
$$

we obtain

$$
\boxed{
\bar n
<
0.254274
\frac{\mathcal O}{\zeta^2}
Q_B\mathcal C_{e,B}\beta_B^3
\mathcal C_\kappa(q_B).
}
$$

Again, finite receiver support produces a controlled multiplicative correction, not a new threshold structure.

---

## 10. Correct source strength

For the finite-spoke source $A$, with prescribed outer branch amplitude $u_0$, define

$$
q_A=\frac{\omega L_A}{c_{s,A}}.
$$

The emitted branch coherent-state distance is

$$
\boxed{
N_\Delta(q_A)
\simeq
\frac72
\frac{G\mu_A^2L_A^2u_0^2\omega^5T}
{\hbar c^5}
\left(\frac{\tan q_A}{q_A}\right)^2.
}
$$

This source factor is separate from the receiver loading factor

$$
\mathcal C_\kappa(q_B).
$$

The end-to-end problem therefore has two independent finite-support parameters:

$$
\boxed{q_A=\omega L_A/c_{s,A},}
$$

$$
\boxed{q_B=\omega L_B/c_{s,B}.}
$$

---

## 11. Optimal source excursion in weak capture

The pure-loss information-flow optimization gives

$$
N_\Delta^{\rm opt}
\simeq4\sqrt\eta.
$$

Set this equal to the corrected source expression. Then

$$
\boxed{
u_{0,\rm opt}^2
\simeq
\frac{8\hbar c^5}
{7G\mu_A^2L_A^2\omega^5T}
\left(\frac{q_A}{\tan q_A}\right)^2
\sqrt\eta.
}
$$

Thus finite support slightly reduces the outer displacement needed to generate a specified branch record at fixed endpoint mass, because the spoke rest mass contributes coherently to the quadrupole.

For $q_A\ll1$,

$$
\left(\frac{q_A}{\tan q_A}\right)^2
=1-\frac{2q_A^2}{3}+O(q_A^4).
$$

---

## 12. Qualitative verdict after conservation correction

The previously derived source→receiver scaling survives.

The conserved finite-support source does **not** introduce

- a cancellation of the branch quadrupole;
- a new power of compactness;
- a new power of $\beta$;
- a new free-space distance law.

Instead it produces controlled multiplicative corrections:

### source branch strength

$$
\boxed{
N_\Delta
\to
N_\Delta^{\rm end}
\left(\frac{\tan q_A}{q_A}\right)^2,
}
$$

### normalized receiver loading

$$
\boxed{
\kappa_\Delta
\to
\kappa_\Delta^{\rm end}
\mathcal C_\kappa(q_B).
}
$$

For

$$
q_A,q_B\ll1,
$$

both are

$$
1+O(q^2)
$$
corrections.

This is the main end-to-end result of the actuator conservation audit.

---

## 13. Remaining source-level correction

The finite spokes are now included analytically. The remaining source uncertainty is the finite hub/control subsystem.

The next adversarial goal is to bound its branch-difference quadrupole by parameters such as

$$
\frac{r_h}{L},
\qquad
\frac{E_{\rm ctrl}}{Mc^2},
\qquad
\frac{v^2}{c^2}.
$$

If the controller follows the exact controlled-parity symmetry and its total energy is branch common, its leading branch quadrupole vanishes; only finite-extent/internal-energy corrections remain.

Those should be bounded before the gravity paper is considered complete.
