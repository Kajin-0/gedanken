# Paper Core V3 — Source-Resolved Quantum Windows in Gravitational Reception

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Current paper architecture after the 2026 prior-art audit and fixed-waveform correction. This supersedes `PAPER_CORE_V2.md` as the preferred structure.

## Working title

**Source-Resolved Quantum Windows in Gravitational Reception**

Alternative:

**From a Coherent Quadrupole Source to a Noisy Gravitational Quantum Receiver**

More technical:

**Binary-Coherent Entanglement-Breaking Witnesses for a Retarded Gravitational Source–Receiver Link**

---

## 1. What the paper is *not* claiming

The paper should begin from the fact that the following already exist:

- gravity-mediated entanglement;
- local/retarded gravity-mediated entanglement;
- gravity-induced non-entanglement-breaking channels;
- coherent-state gravitational channel benchmarks;
- noisy gravitational oscillator state transfer;
- quantized gravitational-wave modes coupled to quantum detectors;
- relativistic sender→receiver channel causality.

Therefore the paper does **not** ask the broad question

> Can gravity carry quantum information?

The paper asks the narrower source-resolved question:

> **For one explicitly specified coherent gravitational source history, what quantum wavepacket is emitted, how does it propagate to a distant receiver, and during what spacetime interval does the complete source-mode→receiver map remain non-entanglement-breaking?**

---

## 2. Paper thesis in one equation

For one fixed emitted temporal branch mode $f_R(t)$ arriving at a receiver,

$$
\boxed{
\text{quantum-capable receiver at time }t
\iff
\tau_f(t,R)>m(t),
}
$$

where

$$
\tau_f(t,R)
=\kappa_\Delta(R)
\left|
\int_0^t ds\,
e^{-\kappa(t-s)/2}f_R(s)
\right|^2
$$

is the coherent branch-mode transfer probability and

$$
m(t)
=n_0e^{-\kappa t}
+\frac{\Gamma_{\rm th}}{\kappa}(1-e^{-\kappa t})
$$

is the receiver's vacuum-output occupation.

The gravity problem is to derive

1. $f_R$ from a controlled source branch history;
2. $\kappa_\Delta(R)$ from the retarded gravitational Green function;
3. an operational entanglement witness for the resulting channel.

---

# Part I — Exact quantum-information lemma

## Theorem 1 — coherent dyad through a phase-insensitive Gaussian channel

For

$$
\Phi_{\tau,m},
$$

$$
\boxed{
\langle u|
\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)
|v\rangle
=
\frac{\langle\beta|\alpha\rangle\langle u|v\rangle}{m+1}
\exp\left[
\frac{(\sqrt\tau\beta^*-u^*)(v-\sqrt\tau\alpha)}{m+1}
\right].
}
$$

This follows from one Weyl Gaussian integral.

---

## Theorem 2 — binary coherent probe detects the exact EB boundary

For every finite nontrivial hybrid state

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

But

$$
\Phi_{\tau,m}\text{ is non-EB}
\iff
\tau>m.
$$

Thus the binary coherent hybrid state detects the channel EB transition exactly.

The proof uses one finite $2\times2$ principal minor; pure loss is handled separately without a singular limiting argument.

**Novelty language:** candidate result only; no originality claim until broader literature search is complete.

---

## Corollary — exact three-element boundary witness

For symmetric $|\pm a\rangle$,

$$
\boxed{
|z_v|^2>p_0p_v
}
$$

is sufficient for NPT.

For $m>0$, choosing

$$
v_*=2\sqrt\tau a/m
$$

gives

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

The witness therefore reaches the exact EB boundary.

---

## Absolute version

Define the negative eigenvalue of the selected partial-transpose block:

$$
\boxed{
G(v)
=\frac12
\max\left\{
0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
}
$$

Then

$$
\boxed{
\mathcal N(\rho)\ge G(v).
}
$$

In the weak-link regime,

$$
\boxed{
G_{\rm abs}^{\rm opt}
=\frac12W(e^{-1})(\tau-m)+O(\tau^2).
}
$$

This is the practical finite-strength variable used later.

---

# Part II — Explicit coherent gravitational source

## Source geometry

Use four equal endpoint masses in a cross.

For branch $s=\pm1$,

$$
X_s^2=L^2+s\,d(t),
$$

$$
Y_s^2=L^2-s\,d(t).
$$

Then the center of mass is fixed and

$$
X_s^2+Y_s^2=2L^2.
$$

The exact STF branch difference is

$$
\boxed{
\Delta Q_{xx}=4\mu d(t),
\qquad
\Delta Q_{yy}=-4\mu d(t),
\qquad
\Delta Q_{zz}=0.
}
$$

Thus the source emits a clean plus quadrupole without a moving dipole.

---

## Quantized plus normal mode

For small deformation,

$$
X\simeq L+u,
\qquad
Y\simeq L-u.
$$

The effective mass is

$$
\boxed{M_{\rm eff}=4\mu.}
$$

The quadrupole coordinate is

$$
\boxed{
\delta Q_{xx}=4\mu Lu,
\qquad
\delta Q_{yy}=-4\mu Lu.
}
$$

Quantize

$$
u
=u_{\rm zpf}(a+a^\dagger),
$$

$$
u_{\rm zpf}
=\sqrt{\frac{\hbar}{8\mu\omega}}.
$$

A state-dependent internal force

$$
H_F=-\sigma_zF(t)u
$$

creates the coherent mechanical branches

$$
|+\alpha(t)\rangle,
\qquad
|-\alpha(t)\rangle.
$$

---

## Closed source excursion

Choose

$$
\boxed{
u_c(t)
=u_0
\sin^4(\pi t/T)
\cos\omega t,
\qquad0<t<T.
}
$$

The inverse-engineered force is

$$
F(t)
=M_{\rm eff}[\ddot u_c+\omega^2u_c].
$$

Because the envelope and its first several derivatives vanish at the boundaries, the source begins and ends in the same mechanical phase-space point.

The branch difference is

$$
\boxed{
\Delta Q_{xx}=8\mu Lu_c(t),
\qquad
\Delta Q_{yy}=-8\mu Lu_c(t).
}
$$

---

## Emitted graviton branch distance

For a conserved narrowband quadrupole,

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega'\,
\omega'^5
|\Delta\widetilde Q_{ij}(\omega')|^2.
}
$$

For the $\sin^4$ source,

$$
\boxed{
N_\Delta
\simeq
\frac72
\frac{G\mu^2L^2u_0^2\omega^5T}
{\hbar c^5}.
}
$$

The same result follows from graviton input-output theory using the mechanical mode's spontaneous graviton linewidth, providing an internal normalization check.

---

# Part III — Retarded propagation to the receiver

## Receiver graviton linewidth

For the same four-mass plus normal mode,

$$
\boxed{
\kappa_g
=\frac{8G\mu L^2\omega^4}{5c^5}
}
$$

or, with total moving endpoint mass $M=4\mu$,

$$
\boxed{
\kappa_g
=\frac{2GM L^2\omega^4}{5c^5}.
}
$$

---

## Retarded cross response

For aligned plus source and receiver quadrupoles,

$$
\boxed{
\Sigma_{AB}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}
{\epsilon^5},
}
$$

where

$$
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
$$

$$
\epsilon=\omega R/c.
$$

In the wave zone,

$$
\Sigma_{AB}^{R}
\simeq
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
$$

---

## Storage amplitude

The delayed source-output→receiver-input amplitude is

$$
\boxed{
t_{AB}^{\rm store}
=-i\Sigma_{AB}^{R}/
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

Thus

$$
\boxed{
\eta_{\rm store}(R)
\simeq
\frac{25\mathcal O}{16(kR)^2}.
}
$$

This is the coefficient that converts the normalized emitted source mode into the useful incoming receiver mode.

**Audit item:** independently rederive the numerical coefficient in a second field convention before submission.

---

# Part IV — Fixed source pulse through a noisy receiver

The normalized emitted temporal mode is

$$
\boxed{
f_4(t)
=\sqrt{\frac{128}{35T}}
\sin^4(\pi t/T),
\qquad0<t<T.
}
$$

For receiver linewidth $\kappa$,

$$
\boxed{
\tau_4(t,R)
=\kappa_\Delta(R)
\left|
\int_0^t ds\,
e^{-\kappa(t-s)/2}f_4(s)
\right|^2.
}
$$

With ground-state initial receiver and thermal injection $\Gamma_{\rm th}$,

$$
\boxed{
m(t)
=\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-\kappa t}).
}
$$

Therefore

$$
\boxed{
\text{source→receiver channel non-EB}
\iff
\tau_4(t,R)>m(t).
}
$$

---

## Dimensionless response

Let

$$
x=t/T,
$$

$$
q=\kappa T.
$$

Define

$$
S_{4,q}(x)
=\frac{128q}{35}
e^{-qx}J_{4,q}^2[\min(x,1)],
$$

$$
N_q(x)=1-e^{-qx}.
$$

Then

$$
\tau_4
=\frac{\kappa_\Delta}{\kappa}S_{4,q},
$$

$$
m
=\frac{\Gamma_{\rm th}}{\kappa}N_q.
$$

The channel is non-EB when

$$
\boxed{
\frac{\kappa_\Delta}{\Gamma_{\rm th}}
\frac{S_{4,q}(x)}{N_q(x)}>1.
}
$$

---

## Source-specific capability threshold

Optimizing over receiver bandwidth and time gives

$$
\boxed{
\max_{q,x}
\frac{S_{4,q}(x)}{N_q(x)}
\simeq0.8136763.
}
$$

Thus the fixed mechanical pulse can produce a non-EB interval only if

$$
\boxed{
\kappa_\Delta
>1.22899\,\Gamma_{\rm th}.
}
$$

The receiver evolves

$$
\boxed{
\mathrm{EB}
\to
\mathrm{non\!-\!EB}
\to
\mathrm{EB}.
}
$$

The result is a finite quantum-capability **window**, not a permanent front.

---

# Part V — Spacetime bubble

In the wave zone,

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g.
}
$$

For each distance $R$, solve

$$
\boxed{
\frac{S_{4,q}(x)}{N_q(x)}
=
\frac{\Gamma_{\rm th}}
{\kappa_\Delta(R)}
}
$$

for the two roots

$$
x_-(R)<x_+(R).
$$

Then the source-to-receiver channel is non-EB only for

$$
\boxed{
\frac Rc+Tx_-(R)
<T_{\rm lab}<
\frac Rc+Tx_+(R).
}
$$

This is the central gravity-specific prediction: a finite **quantum-capability bubble** nested inside the ordinary future light cone.

---

## Wavefront smoothness law

Because

$$
f_4(t)\propto t^4
$$

at the leading edge,

$$
\tau_4(t)\propto t^{10}.
$$

Thermal Markov occupation grows as

$$
m(t)\propto t.
$$

Therefore the early capability crossing obeys

$$
\boxed{
\frac{t_-}{T}
\simeq
\left[
\frac{875}{128\pi^8}
\frac{\Gamma_{\rm th}}
{\kappa_\Delta}
\right]^{1/9}.
}
$$

This makes a key conceptual point:

> **The post-light-cone quantum delay depends on the smoothness/history of the source, not only on distance and receiver noise.**

---

# Part VI — Absolute certification bubble

In the weak gravitational link,

$$
\boxed{
G_{\rm abs}^{\rm opt}(t,R)
\simeq
\frac{W(e^{-1})}{2}
[\tau_4(t,R)-m(t)]_+.
}
$$

Thus a finite requirement

$$
G_{\rm abs}^{\rm opt}\ge G_{\rm req}
$$

defines a smaller bubble than the bare EB/non-EB bubble.

With

$$
K_G
=\frac{25\mathcal O}{16k^2}\kappa_g,
$$

$$
\boxed{
R^2
\le
\frac{
K_GS_{4,q}(x)
}{
\Gamma_{\rm th}N_q(x)
+\kappa G_{\rm req}/c_0
},
}
$$

where

$$
c_0=\frac12W(e^{-1}).
$$

Even in vacuum, $\Gamma_{\rm th}=0$, a finite $G_{\rm req}$ gives a finite certification range.

This cleanly separates

- mathematical channel capability;
- finite observable quantum strength.

---

# Part VII — End-to-end explicit scaling

For the four-mass receiver with total endpoint mass $M$,

$$
\boxed{
\kappa_\Delta(R)
=\frac{5\mathcal O}{8}
\frac{GM L^2\omega^2}
{c^3R^2}.
}
$$

At

$$
kR=\zeta,
$$

and

$$
\kappa\simeq\omega/Q,
$$

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=\frac{5\mathcal O}{16\zeta^2}
Q\mathcal C\beta^3.
}
$$

For the optimized $\sin^4$ pulse in vacuum,

$$
\boxed{
\mathcal N_{\max}
\simeq
0.249382
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3
}
$$

in the weak-capture limit.

This exposes the passive laboratory bottleneck directly.

---

# Part VIII — Source strength is not the same as link quality

The source emits coherent branch distance

$$
N_\Delta
\propto
\mu_A^2L_A^2u_0^2\omega^5T.
$$

But receiver capture fraction $\eta$ is independent of $N_\Delta$.

For pure loss and $\eta\ll1$,

$$
\boxed{
N_\Delta^{\rm opt}
\simeq4\sqrt\eta.
}
$$

A much larger branch record mainly goes into uncollected gravitational modes, creating a strong which-branch environment and reducing source–receiver entanglement.

This is one of the clearest Feynman-level consequences of the complete link.

---

# Part IX — Relation to prior work

The paper must explicitly position itself relative to:

- BMV and one-source gravity-entanglement proposals;
- Christodoulou et al. on retarded local mediation;
- Mari–Zippilli–Vitali on non-EB gravitational channels;
- Lami–Pedernales–Plenio and Toccacelo–Andersen–Brask on gravitational channel benchmarks;
- Miki–Li–Chen on thermal entanglement/EB bounds in pulsed Newtonian oscillator dynamics;
- Toccacelo–Beitel–Andersen–Pikovski on quantized incident GW state transfer into a detector;
- Cliche–Kempf on relativistic field-mediated sender→receiver channels;
- Kreis–van Loock and related hybrid-entanglement literature.

The paper's narrow claimed synthesis is:

> **start from one controlled coherent gravitational source branch history, derive its emitted normalized quantum branch mode, propagate it over explicit distance, capture it in a noisy receiver, and calculate the resulting source-specific EB/non-EB and finite-certification spacetime windows.**

---

# Part X — Claims to make cautiously

Pending independent review, the strongest candidate contributions are:

1. exact binary coherent NPT/EB equivalence for the phase-insensitive Gaussian family;
2. exact three-element principal-minor witness reaching that boundary;
3. weak-link absolute witness law
   $$
   G_{\rm abs}^{\rm opt}\simeq\tfrac12W(e^{-1})(\tau-m);
   $$
4. explicit closed four-mass quantum quadrupole source and emitted branch-mode normalization;
5. source-resolved gravitational EB/non-EB spacetime bubble;
6. explicit end-to-end passive scaling and optimal source-strength tradeoff.

Do not use “first” or “novel” in the manuscript until the citation-forward audit is complete.

---

# Part XI — Figures

## Figure 1 — complete causal link

Source qubit → plus mechanical cat → emitted branch-difference graviton mode → distance $R$ → noisy receiver.

## Figure 2 — binary coherent theorem

Channel plane $(\tau,m)$ with EB boundary $m=\tau$ and exact principal-minor witness.

## Figure 3 — explicit four-mass source

Cross geometry showing branch $+$ and branch $-$ deformations.

## Figure 4 — temporal pulse and receiver loading

Plot $f_4(t)$, $\tau_4(t)$, $m(t)$.

## Figure 5 — spacetime bubble

Plot ordinary light cone and source-specific non-EB birth/death boundaries $T_\pm(R)$.

## Figure 6 — absolute-certification bubble

Show smaller $G_{\rm req}>0$ region nested inside the non-EB bubble.

## Figure 7 — source-strength tradeoff

At fixed tiny capture $\eta$, plot negativity versus $N_\Delta$ to show the optimum and the decay at large source branch record.

---

# Part XII — Next submission-critical checks

1. independent rederivation of the binary coherent theorem by a second method or external reviewer;
2. broader citation-forward search for an equivalent exact hybrid theorem;
3. independent field-convention check of the $25/16$ storage coefficient;
4. conservation audit of the state-dependent source actuator/control stress-energy;
5. numerical validation of the full source-specific bubble beyond the narrowband approximation.

Only after these survive should this be converted into a conventional manuscript draft.