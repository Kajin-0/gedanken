# Finite-Source Causal Support and Internal-Control Audit

**Date:** 2026-08-07  
**Status:** **CAUSAL FRONT CLARIFIED — USE SUPPORT-TO-SUPPORT DISTANCE FOR A DISTRIBUTED OPERATION; CENTER-TO-RECEIVER $R/c$ REMAINS AN EXACT LOWER BOUND FOR A CENTRALLY TRIGGERED CAUSAL ENCODER**

## 1. Purpose

Many Experiment 01 formulas write the causal delay as

$$
R/c,
$$

where $R$ is the source–receiver center separation.

The explicit source is not pointlike. It contains four finite spokes, endpoint masses, and a distributed actuator. A finite receiver can also occupy a nonzero spatial region.

Therefore a strict causal statement must distinguish

1. an arbitrary operation supported over an extended source region; from
2. an operation generated from a localized source origin by causal internal dynamics.

The two cases give different but compatible front statements.

---

# 2. General support-to-support causal distance

Let the source operation have spacetime support

$$
\mathcal O_A
$$

and the receiver observable/readout have support

$$
\mathcal O_B.
$$

For simultaneous source operations on a spatial source region $A$ at coordinate time $t=0$, define

$$
\boxed{
D_{AB}
=
\inf_{\mathbf x\in A,\,\mathbf y\in B}
|\mathbf y-\mathbf x|.
}
$$

Microcausality implies that source-operation dependence of the receiver cannot begin before

$$
\boxed{
T_{\rm front}
\ge
D_{AB}/c.
}
$$

This is the exact finite-region version of the point-source bound.

Therefore a manuscript should not use center-to-center $R/c$ as an exact geometric theorem for an arbitrary spatially extended instantaneous source operation unless

$$
D_{AB}=R
$$

for the chosen geometry.

---

# 3. Why a centrally triggered causal encoder is different

Let

$$
\mathbf x_0
$$

be the localized causal origin of the source encoding.

Suppose a source point $\mathbf x$ can become branch dependent only after a control influence reaches it.

Causality gives

$$
\boxed{
t_A(\mathbf x)
\ge
\frac{|\mathbf x-\mathbf x_0|}{c}.}
$$

If the actual internal control speed is

$$
v_c<c,
$$

then the stronger condition is

$$
t_A(\mathbf x)
\ge
\frac{|\mathbf x-\mathbf x_0|}{v_c}.
$$

A signal emitted from $\mathbf x$ at that earliest allowed time can reach receiver point $\mathbf y$ no earlier than

$$
t_{\rm arr}(\mathbf x,\mathbf y)
\ge
 t_A(\mathbf x)
+
\frac{|\mathbf y-\mathbf x|}{c}.
$$

Using the causal bound on $t_A$,

$$
t_{\rm arr}
\ge
\frac{|\mathbf x-\mathbf x_0|+|\mathbf y-\mathbf x|}{c}.
$$

By the triangle inequality,

$$
|\mathbf x-\mathbf x_0|+|\mathbf y-\mathbf x|
\ge
|\mathbf y-\mathbf x_0|.
$$

Therefore

$$
\boxed{
 t_{\rm arr}(\mathbf x,\mathbf y)
\ge
\frac{|\mathbf y-\mathbf x_0|}{c}.}
$$

Taking the earliest source point gives the exact result

$$
\boxed{
T_{\rm front}
\ge
\inf_{\mathbf y\in B}
rac{|\mathbf y-\mathbf x_0|}{c}.}
$$

For a pointlike receiver centered a distance $R$ from the local source origin,

$$
\boxed{T_{\rm front}\ge R/c.}
$$

Thus finite source extent cannot advance the front ahead of the light cone of the localized encoding origin if the source itself is activated causally.

---

# 4. Internal control slower than light only delays the source

If the source control propagates through the source at speed

$$
v_c\le c,
$$

then

$$
t_A(\mathbf x)
\ge
\frac{|\mathbf x-\mathbf x_0|}{v_c}
\ge
\frac{|\mathbf x-\mathbf x_0|}{c}.
$$

Therefore the center-origin lower bound remains valid and is generally not saturated by radiation sourced far from the trigger.

For the elastic four-spoke architecture a natural internal scale is

$$
\boxed{
T_{\rm int}
\sim L/c_s,
}
$$

with

$$
c_s<c.
$$

A microscopic central actuator therefore develops the global plus mode over a finite preparation interval rather than instantaneously.

This modifies the early source waveform, not the fundamental remote causal bound.

---

# 5. Distributed pre-positioned control is also allowed, but changes the geometric origin

An alternative Gedanken protocol may pre-position branch-common local controller degrees of freedom throughout the bounded source region.

At $t=0$ they can act in parallel using a pre-established internal logical encoding.

In that case the source operation itself has extended support

$$
A,
$$

and the exact causal distance is the support-to-support value

$$
D_{AB}.
$$

There is no causality violation: the quantum information needed for the distributed operation was already localized within the source region before $t=0$.

However, the correct front is then measured from the extended source operation, not from a fictitious point at its center.

---

# 6. The aligned four-spoke geometry is unusually favorable

The canonical source lies approximately in the

$$
xy
$$

plane and the receiver is placed on the symmetry

$$
+z
$$

axis at center distance $R$.

A source material point at transverse radius

$$
\rho
$$

has propagation distance to the receiver center

$$
\boxed{
rho_R(\rho)
=\sqrt{R^2+\rho^2}.}
$$

Therefore

$$
\rho_R(\rho)\ge R.
$$

Transverse source extent cannot produce a source point that is closer than the center/hub along this viewing geometry.

For

$$
\rho\ll R,
$$

$$
\boxed{
\sqrt{R^2+\rho^2}
=R+
\frac{\rho^2}{2R}
-
\frac{\rho^4}{8R^3}
+\cdots.}
$$

Thus the source-size propagation-time spread begins at

$$
\boxed{
\Delta t_{\rm geom}
\sim
\frac{L^2}{2Rc},}
$$

not at

$$
L/c.
$$

This is the time-domain version of the same Fresnel correction controlled by

$$
\boxed{
\frac{kL^2}{R}}
$$

in the finite-size field expansion.

---

# 7. Connection to the exact on-axis form factor

`FINITE_SIZE_FORM_FACTOR_COEFFICIENT.md` found that for the planar source observed on axis,

$$
\boxed{
\mathcal F_q(\beta n_x)
=
\mathcal F_q(\beta n_y)
=1
}
$$

at leading Fraunhofer order because

$$
n_x=n_y=0.
$$

The absence of a transverse

$$
kL
$$

phase correction is equivalent to the absence of a first-order

$$
L/c
$$

arrival-time spread in the aligned geometry.

The first geometric wavefront-curvature correction instead scales as

$$
\boxed{
 kL^2/R.}
$$

This gives a consistent frequency-domain and time-domain picture.

---

# 8. Finite receiver support

Let receiver region $B$ have finite spatial support around center

$$
\mathbf R.
$$

For a distributed receiver observable, the exact causal front from a point source origin $\mathbf x_0$ is

$$
\boxed{
T_{\rm front}
\ge
\frac1c
\inf_{\mathbf y\in B}
|\mathbf y-\mathbf x_0|.}
$$

If the receiver has radial half-depth

$$
a_{B,\parallel}
$$

along the line of sight and

$$
a_{B,\parallel}\ll R,
$$

then

$$
\boxed{
T_{\rm front}
\gtrsim
\frac{R-a_{B,\parallel}}{c}.}
$$

A point-receiver model instead uses the center event and therefore the exact center delay

$$
R/c.
$$

The paper should say which receiver observable/support is being used before calling either expression the exact front.

---

# 9. Source worldtube version

The clean invariant statement is not fundamentally about a scalar distance $R$.

Let

$$
\mathcal W_A
$$

be the spacetime support where the source operation differs between control and signal histories.

Let

$$
x_B
$$

be a receiver event.

Then the source-controlled receiver response vanishes whenever

$$
\boxed{
x_B\notin J^+(\mathcal W_A),}
$$

where

$$
J^+(\mathcal W_A)
$$

is the causal future of the source-operation worldtube.

The familiar

$$
R/c
$$

formula is the special flat-spacetime point-origin representation of this statement.

This should be the theorem-level wording.

---

# 10. Implication for the local sign-controlled encoder

`DISTRIBUTED_EIGENSTRAIN_ENCODER_REALIZATION.md` writes an effective projected coupling in which a common logical sign appears in the eigenstrain field over the spokes.

That continuum expression should not be interpreted as a point qubit instantaneously changing material strain everywhere at the same coordinate time.

Two physically causal interpretations are allowed.

### Interpretation A — central trigger

The logical control originates near the hub and propagates through a local actuator field at finite speed.

Then

$$
\boxed{T_{\rm front}\ge R/c}
$$

from the hub origin, while the global source waveform acquires an internal preparation delay/shape correction of order

$$
L/v_c.
$$

### Interpretation B — distributed source register

Branch-common control degrees of freedom are already distributed throughout the bounded source laboratory and a local extended operation acts across that region.

Then the strict front uses

$$
\boxed{D_{AB}/c.}
$$

Both are consistent with microcausality.

---

# 11. Which version should lead the paper

For the strongest conceptual claim, use the worldtube statement:

> The receiver cannot depend on the source-controlled operation outside the causal future of the complete source-operation worldtube.

For the explicit aligned benchmark, choose one of two clearly labeled simplifications.

### Point-origin / centrally triggered benchmark

Use

$$
\boxed{t_{\rm ret}=t-R/c}
$$

and treat internal source formation as part of the local encoder waveform.

### Extended simultaneous source benchmark

Use the exact support separation

$$
D_{AB}
$$

rather than center distance.

Do not silently mix the two.

---

# 12. Consequence for the NPT front

The abstract capability time should be written invariantly as

$$
\boxed{
T_{\rm NPT}(B)
=
\inf\left\{
 t_B:
 \mathcal A_{B,t_B}
 \text{ is non-EB}
\right\},
}
$$

subject to

$$
\boxed{
T_{\rm NPT}(B)
\ge
T_{\rm causal}(\mathcal W_A,B).
}
$$

For a centrally triggered source and point receiver at center distance $R$,

$$
\boxed{
T_{\rm NPT}(R)
\ge R/c.}
$$

For the actual loading model,

$$
T_{\rm NPT}(R)
=
\frac Rc
+
T_{\rm load}
$$

only after the locally generated source waveform has been defined relative to that central origin.

---

# 13. Error scale relative to the carrier dynamics

For the aligned planar source, the purely geometric source path spread is

$$
\Delta t_{\rm geom}
\sim
\frac{L^2}{2Rc}.
$$

Relative to one carrier period scale

$$
1/\omega,
$$

$$
\boxed{
\omega\Delta t_{\rm geom}
\sim
\frac{kL^2}{2R}.}
$$

Thus the same Fraunhofer criterion

$$
\boxed{
\frac{kL^2}{R}\ll1
}
$$

controls whether the compact-source temporal waveform can be treated as arriving with one common delay

$$
R/c.
$$

This is stronger and more geometrically precise than an unspecified finite-source timing error.

---

# 14. Adversarial verdict

Finite source extent does not invalidate the causal front.

The correct hierarchy is:

### General theorem

$$
\boxed{
\text{receiver source-dependence}=0
\quad\text{outside }J^+(\mathcal W_A).}
$$

### Arbitrary simultaneous extended source operation

$$
\boxed{
T_{\rm front}\ge D_{AB}/c.}
$$

### Centrally triggered causal source

$$
\boxed{
T_{\rm front}\ge R/c}
$$

for a point receiver at distance $R$, by the triangle inequality regardless of source extent.

### Canonical planar four-spoke benchmark

Transverse source-size arrival spread begins only at

$$
\boxed{
\Delta t\sim L^2/(2Rc),}
$$

consistent with the existing Fresnel/finite-size expansion.

The manuscript should therefore promote the source-operation **worldtube** as the fundamental causal object and reserve bare $R/c$ for explicitly defined point-origin or aligned compact-source benchmarks.
