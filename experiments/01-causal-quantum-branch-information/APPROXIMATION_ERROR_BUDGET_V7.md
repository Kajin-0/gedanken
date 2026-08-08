# Approximation / Error Budget for V7

**Date:** 2026-08-08  
**Status:** **CENTRAL REFEREE TABLE — COLLECTS THE CONTROL PARAMETERS THAT WERE PREVIOUSLY DISTRIBUTED THROUGH THE MANUSCRIPT**

## 1. Purpose

The V7 calculation is controlled by several independent small parameters. None is individually obscure, but leaving them distributed across source, propagation, receiver, and causality sections makes it unnecessarily difficult to judge the approximation hierarchy.

This note collects them in one place and distinguishes

1. corrections already retained exactly or explicitly;
2. leading omitted corrections;
3. architecture-dependent design parameters.

---

# 2. Master table

| Effect | Control parameter | Leading effect / omitted order | Status in V7 |
|---|---:|---:|---|
| Small source deformation | $\epsilon_u\equiv |u|/L\ll1$ | branch-symmetric nonlinear source corrections typically relative $O(\epsilon_u^2)$ | linear plus mode retained; endpoint $X^2-Y^2=4Lu$ is exactly linear |
| Finite spoke inertia / sound speed | $q\equiv\omega L/c_s\ll1$ | endpoint-only approximation differs by $O(q^2)$ | finite-spoke factor $\tan q/q$ and $M_{\rm eff}(q)$ retained explicitly |
| Finite controller propagation | $q_c\equiv\omega L/v_c\ll1$ | phase delay $O(q_c)$; coupling strength $|F_c|^2=1-q_c^2\operatorname{Var}(x/L)+O(q_c^4)$ | leading delay + $O(q_c^2)$ form factor explicit |
| Finite gravitational wavelength across source | $\beta\equiv\omega L/c\ll1$ | leading quadrupole-rate correction $O(\beta^2)$; for $q\to0$, $\kappa_g/\kappa_g^{(Q)}=1-\beta^2/21+O(\beta^4)$ | correction audited; main link uses compact-source leading term |
| Nonrelativistic internal energy | $v/c\sim\omega u/c=\beta\epsilon_u$ | branch-quadrupole correction $O[(v/c)^2]=O(\beta^2\epsilon_u^2)$ | explicitly bounded in finite hub/controller residual audit |
| Weak gravity / nonlinear GR | $\mathcal C\equiv2GM/(c^2L)\ll1$ | next metric order is absolute $O(\mathcal C^2)$, relative $O(\mathcal C)$ to the linearized field | linearized gravity only; no all-orders claim |
| Rotating-wave approximation | $g/\omega\ll1$ | dropped generator terms $O(g/\omega)$; observable error protocol dependent | explicitly scoped to resonant narrowband encoder/receiver |
| Narrowband / Markov approximation | $B/\omega\ll1$, $B\equiv\max(g,\kappa_A,\kappa_B,1/T)$ | spectral-coupling variation generically $O(B/\omega)$ for a smooth bath | frequency-weighted $\beta_{g,A}[\alpha]$ given when scalar branching fails |
| Wave-zone propagation | $z^{-1}=(kR)^{-1}\ll1$ | TT amplitude has $O(z^{-1})$ subleading phase/reactive terms; storage probability relative correction begins $-2/z^2+O(z^{-4})$ | exact TT polynomial and Green-function polynomial known; link uses leading $25/(16z^2)$ |
| Reciprocal source--receiver feedback | $\epsilon_{\rm fb}\equiv4\eta_{\rm store}\beta_{g,A}\beta_{g,B}\ll1$ | relative transfer-amplitude correction $O(\epsilon_{\rm fb})$; first controlled echo at $3R/c$ | explicitly audited |
| Finite hub deformation | $\epsilon_h\equiv(M_h/\mu)(r_h/L)(u_h/u)$ | $|\Delta Q_h|/Q_0\lesssim(C_h/8)\epsilon_h$ | explicit design bound; vanishes for ideal rigid central hub |
| Compact controller energy asymmetry | $\delta_E$, $r_c/L$ | $O[\delta_E\beta^2\epsilon_u(r_c/L)^2]$ if asymmetry energy is bounded by mechanical excitation energy | explicit residual bound |
| Controller bus which-branch leakage | physical controller loss | not a perturbative quadrupole correction; becomes an explicit source loss/dephasing channel | must be included in $\beta_{g,A}$ or source-coherence map |
| Gravitational dressing/locality | weak-field perturbative order | common exterior dressing established only at first perturbative order on equal-charge code | deliberately restricted; no exact tensor-factor locality claim |
| Passive-matter oscillator-strength bound | passivity + nonrelativistic matter | does not apply to inverted/active or relativistic/strong-gravity matter | scope stated explicitly |

---

# 3. Source hierarchy

The source calculation is controlled by

$$
\boxed{
\epsilon_u\ll1,
\qquad
q\ll1,
\qquad
q_c\ll1,
\qquad
\beta\ll1,
\qquad
\mathcal C\ll1.
}
$$

The first three refer to different physics:

- $\epsilon_u$ controls deformation nonlinearity;
- $q$ controls elastic support inertia and internal propagation;
- $q_c$ controls controller-bus propagation.

If the controller propagates at approximately the material sound speed,

$$
v_c\sim c_s,
$$

then

$$
q_c\sim q.
$$

But the two are kept conceptually distinct because an electromagnetic or other controller bus could satisfy

$$
v_c>c_s.
$$

The retained source quadrupole is

$$
Q_0
=8\mu Lu\frac{\tan q}{q}.
$$

Thus finite support inertia is **not** simply an omitted $O(q^2)$ uncertainty: its leading effect is already included exactly within the linear longitudinal-spoke model.

---

# 4. Propagation hierarchy

Let

$$
z=kR.
$$

The independent TT mode-overlap audit gives the exact causal normalized amplitude

$$
t_{BA}^{\rm TT}(z)
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5},
$$

$$
P(z)=3-3iz-3z^2+2iz^3+z^4.
$$

Therefore

$$
|t_{BA}^{\rm TT}|^2
=\frac{25}{16z^2}
\left[
1-\frac{2}{z^2}
+\frac{3}{z^4}
-\frac{9}{z^6}
+\frac{9}{z^8}
\right].
$$

This makes the wave-zone error unusually transparent:

$$
\boxed{
\frac{|t|^2}
{25/(16z^2)}-1
=-\frac{2}{z^2}+O(z^{-4}).
}
$$

Thus the leading **probability** correction is relative $O[(kR)^{-2}]$, even though the complex amplitude contains $O[(kR)^{-1}]$ subleading terms.

For the benchmark

$$
kR=10,
$$

the exact polynomial predicts a propagation-only relative correction

$$
-\frac{2}{100}
+\frac{3}{10^4}
-\frac{9}{10^6}
+\frac{9}{10^8}
\simeq
-1.9709\%.
$$

This is much larger than most source relativistic corrections but still irrelevant to the qualitative $10^{-42}$ conclusion.

---

# 5. Encoder / receiver narrowband hierarchy

Define the largest dynamical bandwidth

$$
\boxed{
B
=\max\left(
 g,
 \kappa_A,
 \kappa_B,
 1/T
\right).
}
$$

The common narrowband/RWA requirement is

$$
\boxed{
B/\omega\ll1.
}
$$

Two distinct approximations live inside this statement:

1. counter-rotating terms are suppressed by $g/\omega$;
2. frequency dependence of the bath/port coupling is suppressed by the fractional bandwidth over which the spectral density varies.

If the latter is not negligible, the scalar source branching

$$
\beta_{g,A}
=\frac{\kappa_{g,A}}{\kappa_A}
$$

must be replaced by the waveform-weighted spectral ratio already given in V7:

$$
\beta_{g,A}[\alpha]=
\frac{
\int d\Omega\,
\kappa_g(\omega+\Omega)|\widetilde\alpha(\Omega)|^2
}{
\int d\Omega\,
\kappa_{\rm tot}(\omega+\Omega)|\widetilde\alpha(\Omega)|^2
}.
$$

---

# 6. Finite hub / controller hierarchy

The explicit residual audit gives

$$
\boxed{
\frac{|\Delta Q_h|}{Q_0}
\lesssim
\frac{C_h}{8}
\epsilon_h,
}
$$

with

$$
\boxed{
\epsilon_h
=\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{u_h}{u}.
}
$$

This parameter is architecture dependent rather than universal.

Internal kinetic/elastic energies satisfy parametrically

$$
\boxed{
\frac{|\Delta Q_E|}{Q_0}
=O(\beta^2\epsilon_u^2).
}
$$

The symmetric controller bus itself satisfies

$$
\boxed{
\Delta Q^{\rm ctrl}=0
}
$$

at the retained quadratic order.

---

# 7. Weak-gravity hierarchy

The manuscript uses linearized gravity.

If the leading metric response scales as

$$
h^{(1)}=O(\mathcal C),
$$

then schematically

$$
h^{(2)}=O(\mathcal C^2).
$$

Thus the first nonlinear-GR correction is

$$
\boxed{
O(\mathcal C)
}

**relative to the leading linearized field**.

The same order statement applies to the first-order gravitational-splitting/dressing construction: the manuscript's common-dressing argument is not promoted to a nonperturbative theorem.

---

# 8. Link-level hierarchy

The post-handoff coherent link is

$$
\tau_c
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f.
$$

A useful schematic fractional uncertainty budget is therefore

$$
\frac{\delta\tau_c}{\tau_c}
\sim
\frac{\delta\beta_{g,A}}{\beta_{g,A}}
+
\frac{\delta\eta_{\rm store}}{\eta_{\rm store}}
+
\frac{\delta\beta_{g,B}}{\beta_{g,B}}
+
\frac{\delta\mathcal T_f}{\mathcal T_f},
$$

provided the corrections are small and independent.

The dominant controlled model corrections in the intended regime are bounded by combinations of

$$
\boxed{
q^2,
\quad
q_c^2,
\quad
\beta^2,
\quad
B/\omega,
\quad
\mathcal C,
\quad
(kR)^{-2},
\quad
\epsilon_h,
\quad
\epsilon_{\rm fb}.
}
$$

This is the compact approximation hierarchy a referee should see before evaluating any benchmark number.

---

# 9. Recommended manuscript table

The main paper does not need all derivations above. A compact table should be inserted near the start of the limitations section with columns

1. approximation;
2. control parameter;
3. leading correction;
4. where it is treated.

The full derivations can remain in the source, controller, finite-size, feedback, and present audit notes.

---

# 10. Verdict

The model is not controlled by a single unspecified ``weak coupling'' assumption.

It has a separable hierarchy of source, propagation, dynamical, and gravitational expansion parameters.

The strongest concise statement is

$$
\boxed{
\epsilon_u,
q,
q_c,
\beta,
B/\omega,
\mathcal C,
(kR)^{-1},
\epsilon_h,
\epsilon_{\rm fb}
\ll1,
}
$$

with the leading corrections quantified above.

This table should replace the previous situation in which the same information was correct but dispersed across many sections and audit notes.
