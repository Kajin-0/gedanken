# Wave-Zone Branch Mode and Enclosing Quantum Receiver

**Timestamp:** 2026-08-07 14:40 EDT  
**Status:** Active derivation / Gedanken limit

This note develops the wave-zone version of Experiment 01. The goal is to isolate the branch-dependent gravitational radiation into the minimal quantum channel that carries the $L/R$ distinction, then ask how efficiently an enclosing quantum receiver must capture that channel to transfer recoverable branch coherence from the field into matter.

---

## 1. Branch-dependent gravitational radiation reduces to one difference mode

In linearized quantum gravity, a classical source history drives the graviton field into a multimode coherent state. Let the two source branches produce coherent amplitudes

$$
\{\beta^{L}_{\mathbf k\lambda}\},
\qquad
\{\beta^{R}_{\mathbf k\lambda}\}.
$$

Define the mode-space difference

$$
\Delta\beta_{\mathbf k\lambda}
=\beta^{L}_{\mathbf k\lambda}-\beta^{R}_{\mathbf k\lambda},
$$

and its squared norm

$$
\boxed{
N_\Delta
=\sum_\lambda\int d^3k\,|\Delta\beta_{\mathbf k\lambda}|^2.
}
$$

For vacuum gravitons, $N_\Delta$ is the mean graviton number associated with the **difference source** and the branch-state overlap is

$$
|\langle\beta_R|\beta_L\rangle|
=e^{-N_\Delta/2}.
$$

Define the normalized branch-difference mode

$$
\boxed{
 b_\Delta
 =\frac{1}{\sqrt{N_\Delta}}
 \sum_\lambda\int d^3k\,
 \Delta\beta_{\mathbf k\lambda}^*\,a_{\mathbf k\lambda}.
}
$$

A passive change of mode basis can always choose $b_\Delta$ as one canonical mode. After removing the branch-common coherent displacement, the two radiation states become

$$
|\Psi_L\rangle_g
=|+\sqrt{N_\Delta}/2\rangle_\Delta\otimes|\mathrm{common}\rangle_\perp,
$$

$$
|\Psi_R\rangle_g
=|-\sqrt{N_\Delta}/2\rangle_\Delta\otimes|\mathrm{common}\rangle_\perp.
$$

Thus **all branch distinguishability in coherent gravitational radiation lives in one bosonic difference mode**. The apparent multimode problem reduces exactly to a single quantum channel for the purpose of discriminating $L$ from $R$.

---

## 2. Ideal enclosing receiver as a beam-splitter channel

Let $c$ be a collective quantum memory mode of an enclosing receiver. Assume it is perfectly mode matched to $b_\Delta$ and begins in vacuum. The most general lossless linear capture transformation is a beam splitter,

$$
 c_{\rm out}=\sqrt\eta\,b_{\Delta,{\rm in}}+\sqrt{1-\eta}\,c_{\rm in},
$$

$$
 b_{\Delta,{\rm out}}=\sqrt{1-\eta}\,b_{\Delta,{\rm in}}-\sqrt\eta\,c_{\rm in},
$$

where $0\le\eta\le1$ is the coherent capture fraction.

The receiver branch amplitudes therefore differ by

$$
\boxed{
|\Delta\alpha_B|^2=\eta N_\Delta,
}
$$

while the unobserved outgoing field retains

$$
\boxed{
|\Delta\beta_E|^2=(1-\eta)N_\Delta.
}
$$

The receiver branch-state overlap is

$$
s_B=e^{-\eta N_\Delta/2},
$$

so

$$
\boxed{
D_B^2=1-e^{-\eta N_\Delta}.
}
$$

The complementary history-coherence norm is

$$
C_\Xi=e^{-(1-\eta)N_\Delta/2},
$$

hence

$$
\boxed{
C_\Xi^2=e^{-(1-\eta)N_\Delta}.
}
$$

---

## 3. Exact history witness for the captured radiation mode

The operational witness

$$
\mathcal W_\Xi=C_\Xi^2+D_B^2-1
$$

becomes

$$
\boxed{
\mathcal W_\Xi(\eta,N_\Delta)
=e^{-(1-\eta)N_\Delta}-e^{-\eta N_\Delta}.
}
$$

Therefore

$$
\boxed{
\mathcal W_\Xi>0
\iff
\eta>\frac12
}
$$

for any finite $N_\Delta>0$.

The logarithmic history-transfer margin is

$$
\boxed{
\mathcal M_\Xi
=(2\eta-1)N_\Delta.
}
$$

Interpretation:

> The strong witness becomes positive exactly when the intended receiver holds more of the coherent branch-distinguishing mode than the unobserved output does.

This $50\%$ threshold is a property of this **specific strong witness**, not the threshold for entanglement itself.

---

## 4. Source-receiver entanglement exists below the 50% witness threshold

Let

$$
s_E=e^{-(1-\eta)N_\Delta/2},
\qquad
s_B=e^{-\eta N_\Delta/2}.
$$

For the pure tripartite coherent-state model, tracing out the residual radiation gives source-receiver negativity

$$
\boxed{
\mathcal N_{AB}
=\frac14
\left[
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
\right].
}
$$

For every finite $N_\Delta>0$,

$$
\boxed{
\eta>0
\quad\Rightarrow\quad
\mathcal N_{AB}>0.
}
$$

Thus an arbitrarily small coherent capture transfers some entanglement from the radiation field into the receiver. The condition $\eta>1/2$ is only the point at which the simple history-coherence witness certifies that entanglement without requiring a more sensitive state reconstruction.

For $\eta<1$ and $N_\Delta\to\infty$, the residual field approaches a perfect branch record and $\mathcal N_{AB}\to0$. Stronger radiation does not monotonically improve source-receiver entanglement when some fraction escapes.

---

## 5. Ordinary source visibility is blind to coherent information transfer

The source-only visibility after radiation emission is

$$
V_A=s_Bs_E.
$$

Using the expressions above,

$$
\boxed{
V_A=e^{-N_\Delta/2},
}
$$

which is **independent of $\eta$**.

Therefore coherent transfer of branch information from the gravitational field into the receiver can occur without changing the source-only interference contrast at all.

At $\eta=0$:

- all branch information resides in the radiation field;
- the receiver is uncorrelated with the source.

At $\eta=1$:

- the residual field carries no branch record;
- all of the lost source visibility is recoverable as source-receiver entanglement.

This sharply distinguishes ordinary visibility from the history-coherence quantity $C_\Xi$.

---

## 6. Optimal branch-radiation strength for the simple witness

For fixed $\eta>1/2$, the directly measurable witness

$$
\mathcal W_\Xi(N)
=e^{-(1-\eta)N}-e^{-\eta N}
$$

is not maximized by arbitrarily large branch radiation. Its optimum satisfies

$$
\boxed{
N_\Delta^{\rm opt}
=\frac{\ln[\eta/(1-\eta)]}{2\eta-1}.
}
$$

As $\eta\to1/2^+$,

$$
N_\Delta^{\rm opt}\to2.
$$

As $\eta\to1$, the optimum moves to arbitrarily large $N_\Delta$ and the witness approaches unity.

This is operationally important: the logarithmic margin $\mathcal M_\Xi$ grows linearly with $N_\Delta$, but the raw experimentally accessible contrast $\mathcal W_\Xi$ can become exponentially small when substantial radiation remains unobserved.

---

## 7. Causal wavepacket capture

Let $f(t)$ be the normalized temporal envelope of the branch-difference radiation mode at the enclosing receiver,

$$
\int dt\,|f(t)|^2=1.
$$

Let $\eta_\infty$ be the eventual coherent capture efficiency and define the cumulative captured fraction

$$
\boxed{
\eta(T)
=\eta_\infty
\int_{-\infty}^{T-R/c}dt\,|f(t)|^2.
}
$$

Then

$$
D_B^2(T)=1-e^{-\eta(T)N_\Delta},
$$

$$
C_\Xi^2(T)=e^{-[1-\eta(T)]N_\Delta},
$$

and

$$
\boxed{
\mathcal W_\Xi(T)
=e^{-[1-\eta(T)]N_\Delta}-e^{-\eta(T)N_\Delta}.
}
$$

Before causal arrival,

$$
T<R/c
\quad\Rightarrow\quad
\eta(T)=0,
$$

so the receiver contains no source-controlled branch information.

The strong witness turns positive when

$$
\boxed{
\eta(T)>\frac12.
}
$$

If $\eta_\infty\le1/2$, this particular witness never becomes positive. If $\eta_\infty>1/2$, its onset is

$$
\boxed{
T_W
=\frac{R}{c}
+F^{-1}\!\left(\frac{1}{2\eta_\infty}\right),
}
$$

where

$$
F(t)=\int_{-\infty}^{t}ds\,|f(s)|^2.
$$

By contrast, exact source-receiver entanglement begins as soon as any nonzero part of the coherent mode is causally captured.

Thus the wave-zone Gedanken experiment contains two distinct fronts:

1. the **entanglement-transfer front**, beginning with the first nonzero coherent capture after causal arrival;
2. the **strong history-witness front**, appearing only once more than half of the branch-distinguishing mode has been coherently transferred into the receiver.

---

## 8. A physically local matched receiver

Model the enclosing collective receiver mode $c$ using standard input-output dynamics,

$$
\dot c(t)
=-\frac{\kappa_{\rm tot}}{2}c(t)
+\sqrt{\kappa_g}\,b_{\rm in}(t)
+\sqrt{\kappa_i}\,\xi_{\rm in}(t),
$$

with

$$
\kappa_{\rm tot}=\kappa_g+\kappa_i.
$$

Here

- $\kappa_g$ is coherent coupling to the gravitational radiation mode;
- $\kappa_i$ is all internal/non-gravitational loss.

For a normalized incoming mode $f(t)$, the amplitude stored at target time $T$ is

$$
A(T)
=\sqrt{\kappa_g}
\int_{-\infty}^{T}dt\,
 e^{-\kappa_{\rm tot}(T-t)/2}f(t).
$$

By Cauchy-Schwarz,

$$
\boxed{
\eta_{\max}=|A|^2\le\frac{\kappa_g}{\kappa_{\rm tot}}.
}
$$

Equality is reached by the matched rising-exponential mode

$$
\boxed{
 f_{\rm opt}(t)
 =\sqrt{\kappa_{\rm tot}}
 e^{\kappa_{\rm tot}(t-T)/2}\,\Theta(T-t),
}
$$

up to an overall phase.

Therefore

$$
\boxed{
\eta_{\max}=\frac{\kappa_g}{\kappa_g+\kappa_i}.
}
$$

The strong history witness is possible in this one-port model iff

$$
\boxed{
\kappa_g>\kappa_i.
}
$$

If $\kappa_i=0$, then $\eta_{\max}=1$: an ideal mode-matched receiver can in principle capture the entire branch-difference mode. Weak gravitational coupling does not impose a fundamental efficiency ceiling; it instead makes the matched pulse duration of order

$$
\boxed{\tau_{\rm cap}\sim\kappa_g^{-1}}
$$

astronomically long.

---

## 9. Gravitational radiative coupling rate of a quadrupole memory

Let the receiver quadrupole coordinate be

$$
q_B=\Lambda_B x_B
$$

with effective mechanical mass $\mu_B$ and resonance frequency $\omega_B$. For the plus-type STF quadrupole

$$
Q_{xx}=q_B,
\qquad
Q_{yy}=-q_B,
$$

the standard quadrupole radiation formula gives, for harmonic motion,

$$
P_g=\frac{G\omega_B^6q_0^2}{5c^5}.
$$

With mechanical energy

$$
E_B=\frac12\mu_B\omega_B^2x_0^2,
$$

the gravitational radiative linewidth is

$$
\boxed{
\kappa_g
=\frac{2G\Lambda_B^2\omega_B^4}{5\mu_Bc^5}.
}
$$

If $\Lambda_B=\mu_BL_B$,

$$
\boxed{
\kappa_g
=\frac{2G\mu_BL_B^2\omega_B^4}{5c^5}.
}
$$

This is fantastically small for laboratory masses and frequencies. The Gedanken conclusion is therefore not that coherent capture is forbidden, but that an almost perfectly isolated receiver must interact for an enormous time to act as the time reverse of a gravitational emitter.

---

## 10. Einstein/Feynman compression

> A branch-dependent gravitational wave may occupy many plane-wave modes, but all information distinguishing the two source histories is concentrated in one normalized difference mode. An enclosing quantum receiver that is matched to that mode can coherently transfer the branch record from radiation into matter. Source interference alone cannot reveal this transfer: it stays unchanged while the record moves from field to receiver. A perfect receiver converts field-held which-path information into recoverable source-receiver entanglement. Any nonzero capture transfers some entanglement, while the simple history-coherence witness turns positive only after the receiver holds more than half of the branch-distinguishing mode. In an ideal lossless receiver, arbitrarily weak gravitational coupling can still give perfect capture; the price is not reduced fidelity but an enormous interaction time. Thus the wave-zone question is not whether gravity can carry a signal at light speed, but whether a causally arriving gravitational mode can be coherently caught rather than irreversibly measured.

---

## 11. Current theoretical target

The next step is to replace the phenomenological capture fraction $\eta$ by the explicit quantum input-output channel of a conserved quadrupolar gravitational source and a conserved quadrupolar receiver, including:

1. the retarded propagation phase and wavepacket envelope;
2. gravitational radiative linewidth $\kappa_g$;
3. internal receiver loss $\kappa_i$;
4. finite thermal occupation;
5. the source-path off-diagonal history map $\Xi_T$;
6. comparison with the most general classical stochastic gravitational-wave channel that reproduces the same received waveform.

The potentially distinctive gravity-specific result is the **causal coherent-capture protocol and its history-witness front**, not the underlying beam-splitter mathematics.