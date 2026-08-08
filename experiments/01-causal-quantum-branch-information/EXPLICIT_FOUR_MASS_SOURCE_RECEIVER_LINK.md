# Explicit Four-Mass Source-to-Receiver Link

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Complete leading-order parameter chain using the quantized four-mass plus mode as both source and receiver. Intended as a Gedanken benchmark, not an experimental proposal.

## 1. Receiver mode

Take the four-mass plus receiver from `QUANTIZED_PLUS_MODE_SOURCE.md`.

Let the total moving endpoint mass be

$$
\boxed{M=4\mu.}
$$

Its plus-mode graviton linewidth is

$$
\kappa_g
=\frac{8G\mu L^2\omega^4}{5c^5},
$$

or

$$
\boxed{
\kappa_g
=\frac{2GM L^2\omega^4}{5c^5}.
}
$$

---

## 2. Useful source-mode loading rate

For aligned plus source and receiver modes in the wave zone,

$$
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g,
$$

with

$$
k=\omega/c.
$$

Substituting the explicit receiver linewidth gives

$$
\boxed{
\kappa_\Delta(R)
=\frac{5\mathcal O}{8}
\frac{GM L^2\omega^2}
{c^3R^2}.
}
$$

Equivalently, in endpoint-mass notation,

$$
\boxed{
\kappa_\Delta(R)
=\frac{5\mathcal O}{2}
\frac{G\mu L^2\omega^2}
{c^3R^2}.
}
$$

This is the receiver's useful coupling rate to **one normalized incoming source branch mode**.

The source strength does not appear here. Source strength determines the coherent-state distance $N_\Delta$ carried by that normalized mode.

---

## 3. Receiver linewidth and quality factor

Let ordinary receiver loss dominate over gravitational spontaneous emission,

$$
\kappa\simeq\kappa_i.
$$

Write

$$
\boxed{
\kappa_i=\omega/Q.
}
$$

Then the useful gravitational branching fraction is

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=\frac{5\mathcal O}{8}
\frac{GM L^2\omega Q}
{c^3R^2}.
}
$$

This is the small parameter controlling coherent state transfer in the explicit receiver.

---

## 4. Compactness form

Define receiver compactness

$$
\boxed{
\mathcal C
=\frac{r_s}{L}
=\frac{2GM}{c^2L},
}
$$

and internal relativistic parameter

$$
\boxed{
\beta
=\frac{\omega L}{c}.
}
$$

At wave-zone distance

$$
\boxed{kR=\zeta,}
$$

so

$$
R=\zeta c/\omega.
$$

Then

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=\frac{5\mathcal O}{16\zeta^2}
Q\mathcal C\beta^3.
}
$$

This recovers the expected passive scaling

$$
\boxed{
Q\mathcal C\beta^3.
}
$$

---

## 5. Maximum capture of the explicit $\sin^4$ source

For the mechanically consistent normalized source pulse

$$
f_4(t)
=\sqrt{\frac{128}{35T}}
\sin^4(\pi t/T),
$$

the maximum signal loading over receiver bandwidth and pulse time occurs at

$$
\kappa T\simeq6.40192
$$

for the vacuum **absolute signal-strength** optimization, with

$$
S_{4,*}
\simeq0.7980213.
$$

Thus the maximum pure coherent capture fraction is

$$
\boxed{
\eta_{\max}
\equiv
\tau_{\max}
\simeq
S_{4,*}
\frac{\kappa_\Delta}{\kappa}.
}
$$

At wave-zone radius $kR=\zeta$,

$$
\boxed{
\eta_{\max}^{\rm WZ}
\simeq
\frac{5S_{4,*}}{16}
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
}
$$

Numerically,

$$
\boxed{
\eta_{\max}^{\rm WZ}
\simeq
0.249382
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
}
$$

---

## 6. Maximum full source-receiver negativity in vacuum

For a pure-loss link with

$$
\eta\ll1,
$$

the exact binary-cat negativity optimized over emitted branch distance satisfies

$$
\mathcal N_{\max}
=\eta-2\eta^{3/2}+O(\eta^2).
$$

Therefore the explicit four-mass link gives

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\simeq
0.249382
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3
}
$$

at leading order in weak capture.

This is stronger and more concrete than the earlier generic passive ceiling because it corresponds to one explicit normal mode and one explicit source pulse.

---

## 7. Minimal three-element witness strength

The optimized weak-link absolute principal-minor witness satisfies

$$
G_{\rm abs}^{\rm opt}
\simeq
c_0\eta,
$$

where

$$
c_0
=\frac12W(e^{-1})
\simeq0.1392323.
$$

Therefore

$$
\boxed{
G_{\rm abs,max}^{\rm WZ}
\simeq
0.0347220
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
}
$$

So the minimal three-element witness captures a fixed leading fraction of the already tiny weak-link entanglement.

---

## 8. Thermal capability condition

For the same $\sin^4$ pulse, optimizing receiver bandwidth for **non-EB capability** gives

$$
H_{4,*}\simeq0.8136763.
$$

A ground-state-prepared receiver coupled to a thermal Markov bath has a non-EB window only if

$$
\boxed{
\Gamma_{\rm th}
< H_{4,*}\kappa_\Delta.
}
$$

For one dominant internal bath,

$$
\Gamma_{\rm th}
=\bar n\frac{\omega}{Q}.
$$

At $kR=\zeta$,

$$
\boxed{
\bar n
<
\frac{5H_{4,*}}{16}
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
}
$$

Numerically,

$$
\boxed{
\bar n
<
0.254274
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
}
$$

Thus the same dimensionless receiver figure controls both

1. whether a thermal non-EB window can exist;
2. how much vacuum entanglement can ever be transferred.

---

## 9. Temperature form

For a Bose mode,

$$
\bar n
=\frac1{
\exp(\hbar\omega/k_BT)-1
}.
$$

Define the maximum allowed occupation

$$
\bar n_{\max}
=0.254274
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
$$

Then

$$
\boxed{
T
<
\frac{\hbar\omega}
{k_B\ln(1+\bar n_{\max}^{-1})}.
}
$$

This is the temperature required merely for the mathematical non-EB window to exist in the explicit receiver model.

Finite absolute certification is stricter.

---

## 10. Source strength is a separate resource

The explicit four-mass source has emitted branch coherent-state distance

$$
\boxed{
N_\Delta
\simeq
\frac72
\frac{G\mu_A^2L_A^2u_0^2\omega^5T}
{\hbar c^5}.
}
$$

The normalized receiver capture fraction $\eta$ does not grow when $N_\Delta$ grows.

Instead, for a pure-loss link, the exact source-receiver negativity contains two competing records:

- receiver branch separation;
- uncollected environmental branch separation.

At weak capture, the full negativity is maximized when

$$
\boxed{
N_\Delta^{\rm opt}
\simeq4\sqrt\eta.
}
$$

Thus making the source arbitrarily stronger is counterproductive: almost all of the branch record goes into uncollected gravitational modes and decoheres the retained source from the small receiver.

---

## 11. Optimal mechanical source excursion in vacuum

Set

$$
N_\Delta
=N_\Delta^{\rm opt}
\simeq4\sqrt\eta.
$$

Then the source displacement amplitude required to optimize full negativity is

$$
\boxed{
u_{0,\rm opt}^2
\simeq
\frac{8\hbar c^5}
{7G\mu_A^2L_A^2\omega^5T}
\sqrt\eta.
}
$$

or

$$
\boxed{
u_{0,\rm opt}
\propto
\eta^{1/4}.
}
$$

As the link becomes weaker, the optimal emitted branch record becomes weaker too.

This is a central information-flow result:

> **If the distant receiver captures only a tiny fraction of the gravitational branch record, emitting a huge branch record mainly informs the rest of the universe and destroys source–receiver entanglement.**

---

## 12. Aggressive Gedanken parameter example

Take an intentionally generous nonrelativistic receiver:

$$
M=4\,\mathrm{kg},
$$

$$
L=1\,\mathrm m,
$$

$$
f=1\,\mathrm{MHz},
$$

$$
Q=10^{12},
$$

$$
\mathcal O=1,
$$

and place it at

$$
kR=10.
$$

Then

$$
\mathcal C
\simeq5.94\times10^{-27},
$$

$$
\beta
\simeq2.10\times10^{-2}.
$$

The combination controlling vacuum reception is

$$
\frac{Q\mathcal C\beta^3}{\zeta^2}
\simeq5.47\times10^{-22}.
$$

Therefore

$$
\boxed{
\eta_{\max}
\simeq1.36\times10^{-22},
}
$$

$$
\boxed{
\mathcal N_{\max}
\simeq1.36\times10^{-22},
}
$$

and the optimized three-element witness reaches only

$$
\boxed{
G_{\rm abs,max}
\simeq1.90\times10^{-23}.
}
$$

These values already assume

- an extreme quality factor;
- perfect tensor/mode matching;
- no thermal occupation for the vacuum values;
- a source pulse optimized to the receiver bandwidth.

The example is not a proposed device. It demonstrates the severity of the passive laboratory receiver bottleneck even under deliberately favorable assumptions.

---

## 13. Thermal occupation in the same Gedanken example

The non-EB window requires

$$
\bar n
\lesssim1.39\times10^{-22}.
$$

At

$$
f=1\,\mathrm{MHz},
$$

$$
\hbar\omega/k_B
\simeq4.80\times10^{-5}\,\mathrm K.
$$

The corresponding ideal Bose-temperature condition is approximately

$$
\boxed{
T\lesssim9.5\times10^{-7}\,\mathrm K.
}
$$

The temperature itself is not the only challenge; the receiver must simultaneously maintain the assumed macroscopic mode, quality factor, and quantum coherence.

---

## 14. What dominates

For this explicit passive receiver, the decisive dimensionless factor is

$$
\boxed{
\mathfrak F
=\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
}
$$

The penalties are transparent:

1. **compactness**
   $$
   \mathcal C\ll1;
   $$
2. **nonrelativistic quadrupole radiation**
   $$
   \beta^3\ll1;
   $$
3. **finite memory** through $Q$;
4. **free-space wave-zone separation** through $\zeta^{-2}$;
5. imperfect tensor/temporal overlap through $\mathcal O$.

For ordinary laboratory matter, tiny compactness is the largest fundamental suppression.

---

## 15. Strongest interpretation

> **Once the source and receiver are both written as explicit quantum quadrupole modes, increasing the source amplitude is not the main solution. The receiver can only catch a fraction of one normalized gravitational branch mode, and that fraction is limited by its gravitational branching ratio and free-space overlap. In the weak-link regime the best possible source–receiver entanglement is approximately that capture fraction. A stronger source mostly leaves a clearer which-branch record in the gravitational field that the receiver did not catch.**

This is currently the clearest end-to-end physical interpretation of Experiment 01.

---

## 16. Next strongest step

The central theory is now sufficiently explicit that the next work should return to novelty and theorem audit rather than adding more hardware examples:

1. update the claim ledger and paper core with the fixed-waveform and 2026 prior-art corrections;
2. citation-forward search for the exact binary coherent NPT/EB theorem;
3. independently verify the source-to-receiver $25/16$ storage normalization in a second field convention;
4. only then decide whether the gravity result is publishable as a standalone paper or whether the binary coherent theorem should be separated as the primary mathematical result.