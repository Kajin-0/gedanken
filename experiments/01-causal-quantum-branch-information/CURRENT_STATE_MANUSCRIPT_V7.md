# Current State — Manuscript V7

**Date:** 2026-08-08  
**Status:** **THEORY COMPLETE AT STATED WORKING ORDER; MANUSCRIPT COMPILES AND FINAL VISUAL QA PASSED**

> Live `main` remains authoritative. Check recent commits before future writes.

---

## 1. Publication target

The active paper is

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Current manuscript directory:

`manuscript_v7/`

The project should now be treated as being in **submission-polish mode**, not open-ended theorem-discovery mode.

No new theoretical branch should be opened unless a copyedit, journal-format conversion, or external-style referee review reveals a concrete defect.

---

## 2. Central result

After the physical local source/controller handoff, the completed logical code defines one fixed virtual bosonic difference mode. Its coherent transfer to the receiver memory is

$$
\boxed{
\tau_c(t)
=
\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
\mathcal T_f(t).}
$$

Here

$$
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A},
$$

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2},}
$$

$$
\beta_{g,B}=\frac{\kappa_{g,B}}{\kappa_B},
$$

and

$$
\mathcal T_f(t)
=
\kappa_B
\left|
\int_0^t ds\,
e^{-\kappa_B(t-s)/2}f(s)
\right|^2
\le1.
$$

Define

$$
\boxed{
\eta_Q^{\rm link}
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}.}
$$

This is the coherent-transfer backbone of the paper.

---

## 3. Local source/controller architecture

The finite-support source is the four-spoke plus mode with

$$
\frac{m_r}{\mu}=q\tan q,
\qquad
q=\frac{\omega L}{c_s},
$$

$$
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx},
$$

and

$$
\kappa_g(q)
=
\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}
{\frac12+q/\sin2q}.
$$

The effective encoder

$$
H_{\rm enc}
=\hbar g\sigma_z(a^\dagger w+a w^\dagger)
$$

is now explicitly interpreted as the low-frequency normal-mode reduction of a **literal local controller-field architecture**.

The controller bus obeys

$$
H_\Phi
=\sum_a\int_0^Ldx
\left[
\frac{\Pi_a^2}{2\rho_c}
+\frac{\rho_cv_c^2}{2}(\partial_x\Phi_a)^2
\right],
\qquad v_c\le c,
$$

and in branch $s$ launches

$$
\Phi_a^{(s)}(x,t)
=sX_C(t-x/v_c).
$$

Each spoke couples only to its local controller field:

$$
\mathcal E_a
=\frac12EA
\left[
\partial_x\xi_a
-\epsilon_a\lambda\chi(x)\Phi_a(x,t)
\right]^2.
$$

The projected causal control form factor is

$$
F_c(\omega)
=\int_0^Ldx\,w(x)e^{i\omega x/v_c}.
$$

For

$$
q_c=\omega L/v_c\ll1,
$$

$$
\arg F_c
=\omega\bar x/v_c+O(q_c^3),
$$

$$
\boxed{
|F_c|^2
=1-q_c^2\operatorname{Var}_w(x/L)+O(q_c^4).}
$$

A physical cleared handoff satisfies

$$
\boxed{
T_*^{\rm local}
=T_*^{\rm modal}+O(L/v_c).}
$$

Thus the encoder is local and causal; finite controller propagation shifts/reshapes the waveform but does not create a new serial gravitational link factor.

Canonical notes:

- `LOCAL_CONTROLLER_FIELD_COMPLETION_V7.md`
- `FINITE_SPEED_LOCAL_ENCODER_AUDIT_V7.md`

---

## 4. Equal-Poincare-charge gravitational code

The full encoded system includes

- reference doublet;
- endpoints;
- spokes;
- hub;
- compact work system;
- propagating controller bus;
- graviton field;
- other linear output ports.

At the retained order, every total Poincare generator has code matrix proportional to the identity:

$$
\boxed{
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}
=p^\mu I_{\mathcal C},}
$$

$$
\boxed{
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}
=m^{\mu\nu}I_{\mathcal C}.}
$$

This is the correct statement. Do not replace it by the stronger and generally unnecessary claim that each coherent codeword is an exact global charge eigenstate.

The paper uses this only to motivate a **common first-order asymptotic gravitational dressing**, consistent with perturbative gravitational splitting. It does not claim exact nonperturbative tensor-factor locality.

Canonical note:

`EQUAL_POINCARE_CHARGE_AUDIT_V7.md`

---

## 5. Encoder interval versus fixed channel

The causal intervention begins at

$$
t_s.
$$

The fixed logical-to-bosonic channel exists only after the controller bus is cleared/recombined.

Encoder precursor gravitational radiation is **not** discarded.

At small source--receiver separation, a receiver may respond to precursor radiation before the physical handoff. That early state is a direct controlled qubit-to-multimode state-generation problem.

Once the source/controller system has passed its handoff, the complete coherent branch-distance norm is fixed and all branch dependence can be compressed into the virtual difference mode.

Do not compare a receiver-local convolution variable directly with the source handoff time. The manuscript proposition is now phrased in event order rather than by writing a potentially ambiguous condition such as $t\ge T_*$.

---

## 6. Virtual difference mode

After handoff, remove common displacements and write

$$
|\Psi_s\rangle=|s\boldsymbol\alpha\rangle.
$$

Let

$$
A=\|\boldsymbol\alpha\|,
$$

$$
\boxed{
d
=\frac1A\sum_j\alpha_j^*b_j.}
$$

Then

$$
|s\boldsymbol\alpha\rangle
\to
|sA\rangle_d\otimes|0\rangle_\perp.
$$

Any selected receiver mode is exactly a pure-loss projection of this virtual mode in the vacuum linear network:

$$
\boxed{
\eta_B
=\frac{|\alpha_B|^2}{A^2}
=\frac{N_{\Delta,B}}{N_{\Delta,\rm all}}.}
$$

This is the physical bridge from local source preparation to the standard binary-coherent bosonic-channel analysis.

---

## 7. Noise and accessible readout

For the phase-insensitive Gaussian memory model,

$$
\tau_c
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f,
$$

$$
m_c
=m_B
+\eta_{\rm store}\beta_{g,B}\mathcal T_f m_A.
$$

Define

$$
\boxed{
\Delta_{\rm mem}=\tau_c-m_c.}
$$

Then

$$
\Delta_{\rm mem}>0
$$

is the non-EB/NPT capability condition for the retained phase-insensitive model.

A separate readout channel $(\tau_r,m_r)$ gives

$$
\tau_{\rm acc}=\tau_r\tau_c,
$$

$$
m_{\rm acc}=m_r+\tau_r m_c,
$$

and

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_{\rm mem}-m_r.}
$$

Thus memory capture is not equated with accessible quantum reception.

---

## 8. Exact vacuum entanglement amount

For pure loss with transmissivity

$$
\eta=\tau_c,
$$

and virtual branch amplitude $A$,

$$
s_B=e^{-2\eta A^2},
\qquad
s_E=e^{-2(1-\eta)A^2},
$$

$$
\boxed{
\mathcal N(\eta,A)
=\frac{
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
}{4}.}
$$

Weak-link optimum:

$$
A_{\rm opt}^2\sim\sqrt\eta,
$$

$$
\boxed{
\mathcal N_{\max}(\eta)
=\eta-2\eta^{3/2}
+\frac{13}{3}\eta^2
+O(\eta^{5/2}).}
$$

This was checked numerically down to

$$
\eta=10^{-6}.
$$

The maximum delivered negativity is therefore asymptotically linear in the complete weak-link transmissivity.

---

## 9. Passive-matter corollary

Established EWSR/double-commutator machinery is used to derive the passive nonrelativistic mass-quadrupole response bound

$$
\boxed{
\frac{\kappa_g}{\omega}
\lesssim\frac23\mathcal C\beta^3.}
$$

Then

$$
\beta_g
\lesssim
\min\left[
1,
\frac23Q\mathcal C\beta^3
\right].
$$

For two passive nonrelativistic interfaces,

$$
\boxed{
\eta_Q^{\rm link}
\lesssim
\frac{25\mathcal O}{16(kR)^2}
\prod_{j=A,B}
\min\left[
1,
\frac23Q_j\mathcal C_j\beta_j^3
\right].}
$$

In the unsaturated regime,

$$
\boxed{
\eta_Q^{\rm link}
\lesssim
\frac{25\mathcal O}{36(kR)^2}
Q_AQ_B\mathcal C_A\mathcal C_B\beta_A^3\beta_B^3.}
$$

Novelty discipline:

- EWSR formalism is established;
- severe ordinary-matter graviton absorption difficulty is established;
- this is retained as a gravity-specific passive-response/link corollary, not a title-level theorem claim.

---

## 10. Benchmark

For

$$
M_e=4\,\mathrm{kg},
\quad
L=1\,\mathrm m,
\quad
f=1\,\mathrm{MHz},
\quad
Q=10^{12},
\quad
kR=10,
\quad
\mathcal O=1,
$$

$$
\beta_g=1.09386\times10^{-20},
$$

$$
\eta_{\rm store}=1.5625\times10^{-2}.
$$

Then

### ordinary source + ordinary receiver

$$
\boxed{
\eta_Q^{\rm link}
=1.86958\times10^{-42}.}
$$

### matched passive exponential

$$
\boxed{
\tau_{\max}
=1.01208\times10^{-42}.}
$$

### one ideal gravitational interface

$$
1.70916\times10^{-22}.
$$

### both ideal interfaces

$$
1.5625\times10^{-2}.
$$

The intrinsic gravitational linewidth is

$$
\kappa_g\simeq6.87\times10^{-26}\,\mathrm{s}^{-1},
$$

with lifetime

$$
\kappa_g^{-1}\simeq4.61\times10^{17}\,\mathrm{yr}.
$$

The old receiver-local $10^{-22}$ scale is therefore not the end-to-end ordinary-matter result; source gravitational branching contributes another approximately $10^{-20}$ factor.

---

## 11. Manuscript build state

Current modular manuscript files:

- `manuscript_v7/main.tex`
- `manuscript_v7/references.bib`
- `manuscript_v7/sections/01_introduction.tex`
- `manuscript_v7/sections/02_source_encoding.tex`
- `manuscript_v7/sections/03_virtual_link.tex`
- `manuscript_v7/sections/04_noise_negativity.tex`
- `manuscript_v7/sections/05_bounds_benchmark.tex`
- `manuscript_v7/sections/06_discussion_conclusion.tex`
- `manuscript_v7/sections/appendices.tex`
- `manuscript_v7/figures/link_budget.tex`
- `manuscript_v7/figures/source_geometry.tex`

CI workflow:

`.github/workflows/latex-v7.yml`

It automatically

1. installs TeX;
2. compiles with `latexmk`;
3. fails on unresolved references/citations;
4. uploads the compiled PDF.

The current final-figure manuscript head

$$
\boxed{83fb4443e6765416e473daeaf70ebfd2dd53fe8f}
$$

passed all CI steps in workflow run

$$
\boxed{31257875656}.
$$

The resulting 20-page PDF was downloaded and rendered at 180 dpi.

Final visual QA result:

- chain equation fits page;
- serial link diagram is legible at full-page scale;
- no arrow-label collisions remain;
- source geometry figure is clean;
- no known page-overflow or unresolved-reference defect remains.

Thus

$$
\boxed{
\text{V7 manuscript compile + visual QA: PASS.}
}
$$

---

## 12. Audit status

See:

- `MANUSCRIPT_V7_REFEREE_AUDIT.md`
- `MANUSCRIPT_V7_AUDIT_RESOLUTION.md`

All previously identified medium-risk structural theory items are closed at the stated approximation order:

- passive EWSR provenance;
- equal-charge code/dressing;
- encoder precursor and handoff;
- finite-speed local controller;
- serial-link no-double-counting;
- memory versus readout;
- quantitative weak-link negativity.

No known structural theory gap remains inside the paper's declared weak-field, nonrelativistic, narrowband linear regime.

---

## 13. Submission strategy

Current strategy files:

- `SUBMISSION_STRATEGY_V7.md`
- `PRD_COVER_LETTER_DRAFT_V7.md`
- `PRD_SUBMISSION_CHECKLIST_V7.md`

Recommended order:

1. Physical Review D;
2. Classical and Quantum Gravity;
3. Physical Review Research.

The manuscript should be sold as a **source-resolved gravitational quantum-link normalization/capability paper**, not as a new Gaussian theorem or a near-term detector proposal.

---

## 14. Next work

The next work is editorial/submission work only:

1. complete prose copyedit;
2. scan all uses of `first`, `new`, `exact`, `universal`, and `optimal`;
3. final symbol-consistency audit;
4. final bibliography DOI/journal metadata pass;
5. decide whether $\sin^4$ and passive-broadening material stay in main/appendix;
6. add data/code availability statement;
7. convert/test a REVTeX/PRD submission branch;
8. produce clean submission source archive;
9. finalize cover letter;
10. tag final submission commit.

Do not reopen physics derivations unless one of these steps finds a specific problem.
