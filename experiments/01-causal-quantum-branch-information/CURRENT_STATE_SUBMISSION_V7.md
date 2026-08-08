# Current State — V7 Submission Preflight

**Date:** 2026-08-08  
**Status:** **SCIENCE FROZEN; CLEAN SOURCE PACKAGE COMPILES; SUBMISSION EDITORIAL PREFLIGHT ACTIVE**

> Live `main` is authoritative. This file supersedes `CURRENT_STATE_MANUSCRIPT_V7.md` for submission-stage work.

---

## 1. Paper identity

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Current manuscript directory:

`manuscript_v7/`

Recommended first journal:

**Physical Review D**

Fallback order:

1. Classical and Quantum Gravity;
2. Physical Review Research.

The paper is a source-resolved gravitational quantum-link normalization/capability paper, not a new Gaussian-channel theorem or near-term detector proposal.

---

## 2. Central post-handoff link

$$
\boxed{
\tau_c(t)
=
\beta_{g,A}\eta_{\rm store}(R)\beta_{g,B}\mathcal T_f(t),
}
$$

with

$$
\beta_{g,A}=\kappa_{g,A}/\kappa_A,
$$

$$
\boxed{
\eta_{\rm store}=
\frac{25\mathcal O}{16(kR)^2},
}
$$

$$
\beta_{g,B}=\kappa_{g,B}/\kappa_B,
$$

$$
\mathcal T_f(t)
=\kappa_B
\left|\int_0^t ds\,e^{-\kappa_B(t-s)/2}f(s)\right|^2
\le1.
$$

Define

$$
\eta_Q^{\rm link}
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}.
$$

---

## 3. Local controller source model

The literal controller completion is now part of the manuscript.

Controller bus:

$$
H_\Phi
=\sum_a\int_0^L dx
\left[
\frac{\Pi_a^2}{2\rho_c}
+\frac{\rho_cv_c^2}{2}(\partial_x\Phi_a)^2
\right],
\qquad v_c\le c.
$$

Branch-conditioned retarded command:

$$
\Phi_a^{(s)}(x,t)
=sX_C(t-x/v_c).
$$

Local elastic coupling:

$$
\boxed{
\mathcal E_a
=\frac12EA_s
\left[
\partial_x\xi_a-
\epsilon_a\lambda\chi\Phi_a
\right]^2.
}
$$

For

$$
\xi_a^{(s)}=\epsilon_a s u f_q,
$$

the correct branch expression is

$$
\boxed{
\partial_x\xi_a^{(s)}-
\epsilon_a\lambda\chi\Phi_a^{(s)}
=
\epsilon_as
\left[u f_q'-\lambda\chi X_C(t-x/v_c)\right].
}
$$

### Important copyedit correction

A semantic copyedit found the accidental TeX-valid typo

$$
\nu f_q'
$$

in the source section and charge appendix. It has been corrected to

$$
\boxed{u f_q'}
$$

on live `main`.

A clean submission-package semantic guard now fails if `\\nu f_q` reappears.

---

## 4. Notation cleanup completed

The manuscript now avoids the main symbol collisions:

- spoke cross-sectional area:
  $$A_s$$
- finite-spoke inertia function:
  $$\mathcal A(q)=\frac12+\frac{q}{\sin2q}$$
- virtual coherent branch amplitude:
  $$A$$
- compact work mode:
  $$w$$
- controller overlap weight:
  $$W_c(x)$$

The controller form factor is

$$
F_c(\omega)
=\int_0^Ldx\,W_c(x)e^{i\omega x/v_c}.
$$

---

## 5. Equal-charge code

The full encoded system satisfies, to the audited working order,

$$
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}
=p^\mu I_{\mathcal C},
$$

$$
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}
=m^{\mu\nu}I_{\mathcal C}.
$$

Use this code-matrix statement, not an unnecessary claim that each coherent codeword is an exact global charge eigenstate.

---

## 6. Handoff wording

The abstract and conclusion now use

> controller-clear handoff

rather than an unqualified

> exact controller-empty handoff.

An exact controller-empty time exists only in the explicitly scoped projected modal model.

The literal local controller has

$$
T_*^{\rm local}
=T_*^{\rm modal}+O(L/v_c).
$$

---

## 7. Memory and readout

$$
\Delta_{\rm mem}=\tau_c-m_c,
$$

and a readout channel $(\tau_r,m_r)$ gives

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_{\rm mem}-m_r.
}
$$

Do not equate memory capture with accessible quantum reception.

---

## 8. Weak-link entanglement

For vacuum pure loss:

$$
\boxed{
\mathcal N(\eta,A)
=\frac{\sqrt{(1+s_E)^2-4s_Es_B^2}-(1-s_E)}{4},
}
$$

$$
s_B=e^{-2\eta A^2},
\qquad
s_E=e^{-2(1-\eta)A^2}.
$$

Weak optimum:

$$
A_{\rm opt}^2\sim\sqrt\eta,
$$

$$
\boxed{
\mathcal N_{\max}
=\eta-2\eta^{3/2}
+\frac{13}{3}\eta^2
+O(\eta^{5/2}).
}
$$

---

## 9. Benchmark

For the aggressive ordinary-matter benchmark,

$$
\beta_g=1.09386\times10^{-20},
$$

$$
\eta_{\rm store}=1.5625\times10^{-2},
$$

$$
\boxed{
\eta_Q^{\rm link}=1.86958\times10^{-42}.}
$$

Matched passive exponential:

$$
\boxed{
\tau_{\max}=1.01208\times10^{-42}.}
$$

One ideal interface:

$$
1.70916\times10^{-22}.
$$

Both ideal interfaces:

$$
1.5625\times10^{-2}.
$$

---

## 10. APS submission-policy checks completed

Current official APS guidance was checked on 2026-08-08.

For initial PRD peer review:

- a PDF is sufficient;
- REVTeX/LaTeX source is preferred but not an initial-review gate.

Therefore a REVTeX conversion is optional submission/production polish, not a blocker.

A Data Availability statement has been added.

It states that no experimental data were created or analyzed, numerical values are reproducible from the equations, and the manuscript source/supporting notes/scripts are available in the public repository.

Repository bibliography entry:

`manuscript_v7/data.bib`

The main bibliography now uses

```tex
\bibliography{references,data}
```

---

## 11. Clean submission package

A manuscript-only package was built from a fresh download of live `main`:

`/mnt/data/gedanken-prd-v7-source.zip`

It contains only

- `main.tex`;
- `references.bib`;
- `data.bib`;
- `sections/*.tex`;
- `figures/*.tex`;
- `SUBMISSION_MANIFEST.txt`.

Research scratch notes and CI configuration are excluded.

The clean package was compiled independently with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

and the unresolved-reference/citation check passed.

A hard semantic guard also passed for

- accidental `\\nu f_q`;
- priority phrases such as `first ever` / `for the first time`;
- unqualified universal-theorem language;
- stale controller-overlap notation;
- presence of Data Availability / repository citation.

Thus

$$
\boxed{
\text{clean submission-source compile: PASS.}
}
$$

---

## 12. Visual QA

The stable figure-bearing manuscript was previously rendered at 180 dpi.

The final page-2 design has

- a two-line chain equation that fits the page;
- four full-size link boxes;
- plain arrows with no label collisions;
- the link equation below the diagram;
- legible source geometry.

Later semantic edits change notation/prose and add Data Availability but do not alter the approved main figure geometry.

---

## 13. Editorial decisions

### Keep

The passive-source-broadening appendix remains because it directly supports the speed--efficiency claim:

$$
\tau_{A\to B}^{\max}(r)
=4\frac{\kappa_{g,A}\kappa_\Delta}{\kappa_B^2}
r^{2r/(1-r)},
$$

with strictly decreasing source-resolved optimum under added dissipative broadening.

### Intended small trim

The source-specific main-text line

$$
\mathcal T_{\sin^4}^{\max}\simeq0.7980213
$$

is no longer necessary for the V7 general argument and should be removed on the next safe whole-file edit of `sections/03_virtual_link.tex`.

This is cosmetic/editorial only and is **not a physics or submission blocker**.

---

## 14. Remaining submission work

Only submission polish remains:

1. final bibliography DOI/journal metadata pass;
2. final complete prose copyedit;
3. remove the orphaned $\sin^4$ main-text number when safely editing that file;
4. add acknowledgments/funding as appropriate;
5. replace `Anonymous` with actual submission metadata;
6. finalize the PRD cover letter;
7. optionally test REVTeX if desired;
8. tag the final submission commit.

Do not reopen theory unless a concrete defect is found during one of these tasks.
