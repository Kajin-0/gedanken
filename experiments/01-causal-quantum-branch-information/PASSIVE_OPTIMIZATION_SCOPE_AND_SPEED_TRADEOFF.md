# Passive Optimization Scope and the Source Speed–Efficiency Tradeoff

**Date:** 2026-08-08  
**Status:** **MANUSCRIPT-SCOPE CORRECTION — RECEIVER-LOCAL LINEWIDTH MATCHING IS NOT THE GLOBAL PASSIVE OPTIMUM OF A FIXED PHYSICAL RADIATOR**

## 1. Why this note is necessary

Two exact passive optimization results coexist in the repository and answer different questions.

### Result A — normalized incident mode / fixed branching fractions

For a normalized exponential source waveform and a constant-coupling receiver, the temporal overlap is globally maximized when

$$
\boxed{\kappa_A=\kappa_B,}
$$

with

$$
\boxed{
\tau_{\rm rec}^{\max}
=4e^{-2}\frac{\kappa_\Delta}{\kappa_B}.
}
$$

Equivalently, if the source and receiver gravitational branching fractions

$$
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A},
\qquad
\beta_{g,B}=\frac{\kappa_{g,B}}{\kappa_B}
$$

are treated as fixed architectural parameters while the common linewidth is varied, the matched end-to-end expression is

$$
\boxed{
\tau_{A\to B}^{\max}
=4e^{-2}\eta_{\rm store}\beta_{g,A}\beta_{g,B}.
}
$$

### Result B — fixed physical source radiator

If the intrinsic gravitational source rate

$$
\kappa_{g,A}
$$

is fixed and the source linewidth is increased by adding ordinary passive loss, then

$$
\beta_{g,A}=\kappa_{g,A}/\kappa_A
$$

decreases.

The exact source-resolved optimization in `PASSIVE_BROADENING_NO_GO.md` proves that **any added passive nongravitational source damping strictly reduces the maximum end-to-end transfer**.

Therefore the manuscript must not call linewidth matching the unrestricted global passive optimum of a fixed physical source.

---

# 2. Exact receiver-local exponential result

Let

$$
\boxed{r=\frac{\kappa_A}{\kappa_B}.}
$$

For

$$
f_A(t)=\sqrt{\kappa_A}e^{-\kappa_A t/2},
$$

the optimized receiver-local transfer from an **already normalized incident gravitational mode** is

$$
\boxed{
\tau_f^{\max}(r)
=\frac{\kappa_\Delta}{\kappa_B}
S_{\exp}(r),
}
$$

where

$$
\boxed{
S_{\exp}(r)
=4r^{(1+r)/(1-r)}.
}
$$

It is symmetric under

$$
r\leftrightarrow1/r
$$

and has its unique maximum at

$$
\boxed{r=1,}
$$

with

$$
\boxed{S_{\exp}(1)=4e^{-2}.}
$$

This is a **temporal-mode matching theorem**.

---

# 3. Full source-resolved passive transfer

A physical source first has to put its excitation into the gravitational output port.

For vacuum nongravitational source loss,

$$
\boxed{
\eta_g
=\frac{\kappa_{g,A}}{\kappa_A}
=\frac{\kappa_{g,A}}{r\kappa_B}.}
$$

Hence the optimized end-to-end coherent transfer is

$$
\tau_{A\to B}^{\max}
=\eta_g\tau_f^{\max}.
$$

Substituting gives

$$
\boxed{
\tau_{A\to B}^{\max}(r)
=4\frac{\kappa_{g,A}\kappa_\Delta}
{\kappa_B^2}
F(r),
}
$$

with

$$
\boxed{
F(r)=r^{2r/(1-r)}.}
$$

The logarithmic derivative is

$$
\boxed{
\frac{d}{dr}\ln F(r)
=
\frac{2(\ln r+1-r)}{(1-r)^2}.}
$$

Since

$$
\ln r\le r-1
$$

with equality only at

$$
r=1,
$$

we have

$$
\boxed{
\frac{dF}{dr}<0
\qquad(r>0).}
$$

Thus

$$
\boxed{
\text{at fixed }\kappa_{g,A},\kappa_\Delta,\kappa_B,
\text{ increasing }\kappa_A
\text{ by passive loss always worsens transfer.}
}
$$

---

# 4. True passive source optimum at fixed radiator

The optimum is therefore the smallest physically available total source linewidth.

If all nongravitational source loss can be removed,

$$
\boxed{
\kappa_A=\kappa_{g,A}.}
$$

This gives

$$
\boxed{\beta_{g,A}=1.}
$$

but generally produces a source waveform much narrower and longer than the receiver response.

For

$$
r=\frac{\kappa_{g,A}}{\kappa_B}\to0,
$$

$$
F(r)\to1,
$$

and therefore

$$
\boxed{
\tau_{A\to B}^{\max}
\to
4\frac{\kappa_{g,A}\kappa_\Delta}
{\kappa_B^2}.}
$$

Using

$$
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B},
$$

$$
\boxed{
\tau_{A\to B}^{\max}
\to
4\eta_{\rm store}
\left(\frac{\kappa_{g,A}}{\kappa_B}\right)
\left(\frac{\kappa_{g,B}}{\kappa_B}\right).}
$$

For identical intrinsic source and receiver gravitational rates,

$$
\kappa_{g,A}=\kappa_{g,B}=\kappa_g,
$$

and a receiver with total linewidth

$$
\kappa_B\gg\kappa_g,
$$

this reduces to

$$
\boxed{
\tau_{A\to B}^{\max}
\simeq
4\eta_{\rm store}\beta_{g,B}^2.}
$$

---

# 5. Why matched passive linewidths still matter

The matched expression

$$
\boxed{
4e^{-2}\eta_{\rm store}\beta_{g,A}\beta_{g,B}
}
$$

remains useful, but its scope must be explicit.

It is the optimum of the family in which

- the source waveform is exponential;
- the receiver coupling is constant;
- the **gravitational branching fractions are treated as fixed independent architectural parameters**;
- one optimizes only the relative source/receiver temporal linewidths.

It is also the correct result for comparing two hypothetical devices whose total linewidths can be varied without changing their gravitational branching ratios.

It is **not** the optimum obtained by taking one fixed weak gravitational radiator and adding ordinary source damping until

$$
\kappa_A=\kappa_B.
$$

That latter operation destroys gravitational branching faster than it improves temporal overlap.

---

# 6. A matched-family speed–strength relation

For the matched exponential family,

$$
\kappa_A=\kappa_B=\kappa,
$$

and fixed intrinsic rates

$$
\kappa_{g,A},\kappa_{g,B},
$$

$$
\boxed{
\tau_{A\to B}^{\max}
=4e^{-2}\eta_{\rm store}
\frac{\kappa_{g,A}\kappa_{g,B}}{\kappa^2}.}
$$

The peak receiver time is

$$
\boxed{t_*=2/\kappa.}
$$

Therefore

$$
\boxed{
\tau_{A\to B}^{\max}
=e^{-2}\eta_{\rm store}
\kappa_{g,A}\kappa_{g,B}t_*^2.}
$$

This is a useful **speed–transfer-strength relation** for the matched passive family.

At fixed intrinsic gravitational rates, a faster passive matched link necessarily has a smaller peak transfer probability as

$$
\boxed{\tau_{\max}\propto t_*^2.}
$$

The relation is not a universal quantum-gravity bound; it is a consequence of the passive Markov exponential architecture.

---

# 7. The more general passive speed–efficiency tension

The fixed-radiator no-go gives a stronger qualitative statement.

### Suppress ordinary source loss

Then

$$
\beta_{g,A}\to1,
$$

but

$$
\kappa_A\to\kappa_{g,A},
$$

so the natural source duration becomes

$$
\boxed{T_A\sim1/\kappa_{g,A}.}
$$

For weak laboratory gravitational radiators, this can be fantastically long.

### Broaden the source dissipatively

Then

$$
T_A\sim1/\kappa_A
$$

becomes shorter, but

$$
\boxed{
\beta_{g,A}
=\frac{\kappa_{g,A}}{\kappa_A}
}
$$

falls in direct proportion.

The exact monotonicity result shows that temporal overlap never compensates for this lost gravitational branching in the passive source-resolved problem.

Therefore:

$$
\boxed{
\text{passive speed is purchased by diverting quantum amplitude away from gravity.}
}
$$

This is the physical reason coherent waveform engineering is a distinct resource from passive broadening.

---

# 8. Dimensionless link budget

For the passive architecture, the relevant dimensionless quantities are

$$
\boxed{
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A},
\qquad
\beta_{g,B}=\frac{\kappa_{g,B}}{\kappa_B},
\qquad
\eta_{\rm store}=\frac{25\mathcal O}{16(kR)^2},
\qquad
n_{{\rm th},B}.
}
$$

The receiver-local normalized-mode problem can look substantially less impossible than the true source-resolved problem because it effectively sets the source branching stage to unity by assumption.

This distinction should be visible in any feasibility table.

---

# 9. Aggressive laboratory benchmark revisited

Use the deliberately optimistic historical benchmark

$$
\boxed{
M_e=4\ {\rm kg},
\quad
L=1\ {\rm m},
\quad
f=1\ {\rm MHz},
\quad
Q=10^{12},
\quad
kR=10,
\quad
\mathcal O=1.
}
$$

The endpoint compactness is

$$
\boxed{
\mathcal C_e
=\frac{2GM_e}{c^2L}
\simeq5.94093\times10^{-27}.}
$$

The mechanical size parameter is

$$
\boxed{
\beta=\frac{\omega L}{c}
\simeq2.09585\times10^{-2}.}
$$

At leading endpoint order,

$$
\frac{\kappa_g}{\omega}
=\frac{\mathcal C_e\beta^3}{5},
$$

so with

$$
\kappa=\omega/Q,
$$

the gravitational branching fraction of either ordinarily damped device is

$$
\boxed{
\beta_g
=Q\frac{\mathcal C_e\beta^3}{5}
\simeq1.09386\times10^{-20}.}
$$

At

$$
kR=10,
$$

$$
\boxed{
\eta_{\rm store}
=\frac{25}{1600}
=1.5625\times10^{-2}.}
$$

---

# 10. Old receiver-local number versus true end-to-end number

The previous source-receiver file quotes, for the optimized \(\sin^4\) receiver-local capture of an already normalized incoming gravitational mode,

$$
\boxed{
\eta_{\rm rec}^{\rm old}
\simeq1.36\times10^{-22}.}
$$

That number is not the transmissivity from an ordinarily damped mechanical source excitation all the way to the receiver.

It omits the source gravitational branching stage.

For matched exponential source and receiver with the same

$$
\beta_g\simeq1.09386\times10^{-20},
$$

the end-to-end passive peak is

$$
\tau_{A\to B}^{\max}
=4e^{-2}\eta_{\rm store}\beta_g^2,
$$

which gives

$$
\boxed{
\tau_{A\to B}^{\max}
\simeq1.01\times10^{-42}.}
$$

Thus the source-resolved link is roughly twenty orders of magnitude weaker than the old receiver-local normalized-mode benchmark for this parameter choice.

This is not an inconsistency. The two numbers answer different operational questions.

---

# 11. Removing ordinary source loss

Keep the receiver unchanged but set the source total linewidth to its intrinsic gravitational rate:

$$
\boxed{
\kappa_A=\kappa_{g,A}.}
$$

Then

$$
\beta_{g,A}=1,
$$

but the source linewidth ratio becomes

$$
r
=\frac{\kappa_{g,A}}{\kappa_B}
\simeq1.09386\times10^{-20}.
$$

The exact fixed-radiator passive formula approaches

$$
4\eta_{\rm store}\beta_{g,B}^2.
$$

Numerically,

$$
\boxed{
\tau_{A\to B}^{\max}
\simeq7.48\times10^{-42}.}
$$

Removing source ordinary loss therefore improves the matched-damped benchmark by approximately

$$
e^2,
$$

but does not change the basic conclusion: the passive laboratory link remains fantastically weak because the receiver's gravitational branching is itself tiny.

---

# 12. The timescale cost of gravitational branching

For the historical benchmark,

$$
\kappa_B
=\frac\omega Q
\simeq6.28319\times10^{-6}\ {m s^{-1}}.
$$

The intrinsic gravitational linewidth is

$$
\boxed{
\kappa_g
=\beta_g\kappa_B
\simeq6.87293\times10^{-26}\ {m s^{-1}}.}
$$

Therefore a purely gravitational passive source has characteristic decay time

$$
\boxed{
\kappa_g^{-1}
\simeq4.61\times10^{17}\ {m yr}.}
$$

This makes the speed–efficiency tradeoff impossible to hide behind a large quality factor:

- ordinary damping gives a manageable mechanical ringdown but almost zero gravitational branching;
- eliminating ordinary damping restores gravitational branching but makes the natural passive emission time cosmological.

If both source and receiver were hypothetically pure gravitational single-port systems,

$$
\beta_{g,A}=\beta_{g,B}=1,
$$

then at

$$
kR=10
$$

the matched passive peak could reach

$$
\boxed{
4e^{-2}\eta_{\rm store}
\simeq8.46\times10^{-3}.}
$$

But the loading time would be controlled by

$$
1/\kappa_g,
$$

which is the same astronomical scale.

---

# 13. What this changes in the paper

## V5 wording that must be scoped

Statements such as

> “matched linewidths are globally optimal for the passive link”

must be changed to

> “matched linewidths maximize temporal capture for the exponential family at fixed gravitational branching fractions.”

Or more explicitly:

> “At fixed \(\beta_{g,A}\), \(\beta_{g,B}\), and \(\eta_{\rm store}\), matching \(\kappa_A=\kappa_B\) maximizes the constant-coupling temporal-overlap factor and gives \(4e^{-2}\). For a fixed physical radiator \(\kappa_{g,A}\), however, adding passive source loss to achieve that match strictly reduces the end-to-end transfer.”

## Passive feasibility discussion

The paper should distinguish three levels:

1. **receiver-local capture:** normalized incoming graviton mode → receiver;
2. **matched architectural link:** fixed gravitational branch fractions × temporal matching;
3. **fixed-radiator physical passive source:** source branching and duration optimized together.

## Stronger conceptual result

The practical discussion should elevate the passive source speed–efficiency tradeoff:

$$
\boxed{
\text{shorter passive source lifetime}
\Longleftrightarrow
\text{smaller gravitational branching fraction}.}
$$

The exact no-go theorem shows that dissipative broadening cannot solve the temporal-matching problem.

---

# 14. Implication for active coherent control

The passive no-go points directly at the only route worth studying if one wants a faster source without throwing away branch information:

> **coherent source-mode shaping rather than dissipative broadening.**

An internal branch-common controller could, in principle, reshape the gravitational emission temporal mode while keeping the total evolution coherent.

The active \(\sin^4\) protocol and the local resonant encoder should be viewed through this lens.

The next theoretical question is no longer

> “Should the passive source be broadened to match the receiver?”

because the answer is exactly no.

The correct question is

> “Can a closed coherent controller synthesize a receiver-matched gravitational temporal mode without exporting comparable branch information into its own degrees of freedom or generating a dominant controller quadrupole?”

That is a genuinely different control problem.

---

# 15. Adversarial verdict

The passive source-resolved analysis is now sharper than the simple factorized matched formula suggests.

1. The familiar
   $$
   4e^{-2}
   $$
   factor is the temporal-overlap optimum at fixed branching fractions.
2. At fixed intrinsic gravitational source rate, passive nongravitational broadening **always reduces** end-to-end transfer.
3. The true passive source optimum removes ordinary source loss, but then the source emission time approaches
   $$
   1/\kappa_{g,A}.
   $$
4. For the aggressive kilogram–meter–MHz benchmark, including source branching pushes the end-to-end passive transfer from the old receiver-local
   $$
   \sim10^{-22}
   $$
   scale down to
   $$
   \sim10^{-42}.
   $$
5. The resulting speed–efficiency tension is a more physically informative conclusion than the older receiver-local feasibility estimate.

This correction should be propagated into `PAPER_CORE_V5_LOCAL_END_TO_END.md` before manuscript drafting.
