# General Causal Quantum-Channel Front

**Timestamp:** 2026-08-07 18:06 EDT  
**Status:** General operational framework. The channel/resource-theory ingredients are established; the gravitational front synthesis is the active research direction.

## 1. Why “first entanglement” is not the most general causal definition

Quantum fields can contain spacelike vacuum correlations. Two local quantum systems can, in principle, harvest pre-existing field entanglement without either system causally signalling to the other.

Therefore a statement such as

$$
\text{“source and receiver can never be entangled before }R/c\text{”}
$$

is too strong in a fully relativistic field theory.

The correct causal question is narrower:

> **When does the source-controlled propagating branch mode become capable of carrying quantum information into the receiver?**

This is a channel question, not a statement that every possible source-receiver correlation vanishes outside the light cone.

---

## 2. Time-resolved accessible receiver channel

Fix

- a source-controlled outgoing gravitational branch-mode wavepacket;
- receiver location/separation $R$;
- all environmental/input states other than that selected mode;
- a controllable accessible receiver output register $C$.

Define

$$
\boxed{
\mathcal A_{R,t}:
\text{incoming branch-mode state}
\longrightarrow
\text{accessible receiver state at time }t.
}
$$

All internal capture, storage, scrambling, transduction, and readout stages are included in $\mathcal A_{R,t}$.

This is the complete operational receiver channel.

Before the relevant source-controlled disturbance can causally reach the receiver, locality requires the receiver output to be independent of the selected incoming source mode. Thus, for the source-controlled contribution,

$$
\boxed{
\mathcal A_{R,t}(\rho)
=\sigma_{R,t}
\qquad
\text{for all }\rho,
\quad t<R/c.
}
$$

That is a **replacer channel**.

Every replacer channel is entanglement breaking.

Hence

$$
\boxed{
R_{\rm EB}(\mathcal A_{R,t})=0
\qquad t<R/c.
}
$$

This is the correct channel-level causal statement.

---

## 3. General quantum-capability front

Using the EB robustness from `GENERAL_ACCESSIBLE_QUANTUM_MEMORY_RESOURCE.md`, define

$$
\boxed{
T_{\rm cap}(R)
=
\inf\left\{
 t:
 R_{\rm EB}(\mathcal A_{R,t})>0
\right\}.
}
$$

Then locality gives

$$
\boxed{
T_{\rm cap}(R)
\ge
R/c.
}
$$

Interpretation:

> $T_{\rm cap}$ is the earliest time at which the complete accessible receiver channel is no longer entanglement breaking.

This is more general than an oscillator, Gaussian channel, thermal bath, or even a bosonic receiver.

---

## 4. State-specific entanglement front

Now choose one particular source encoding. Let

$$
|\Psi\rangle_{SG}
$$

be an entangled state between source branch register $S$ and the outgoing gravitational input mode $G$.

For Experiment 01 the canonical encoding is binary coherent,

$$
|\Psi\rangle_{SG}
=
\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle.
$$

At time $t$, the accessible source-receiver state is

$$
\rho_{SC}(t)
=(I_S\otimes\mathcal A_{R,t})
(|\Psi\rangle\langle\Psi|).
$$

For an entanglement monotone $E$, define

$$
\boxed{
T_{\Psi,E}(R)
=
\inf\left\{
 t:
 E[\rho_{SC}(t)]>0
\right\}.
}
$$

If $\mathcal A_{R,t}$ is EB, no input entanglement can survive. Therefore

$$
\boxed{
T_{\Psi,E}(R)
\ge
T_{\rm cap}(R)
\ge
R/c.
}
$$

A channel may become non-EB before a poorly chosen source encoding reveals it.

Thus the general hierarchy is

$$
\boxed{
R/c
\le
T_{\rm cap}(R)
\le
T_{\Psi,E}(R).
}
$$

---

## 5. Front-faithful probe families

Call a family of entangled source-mode inputs $\mathscr P$ **front faithful** for a channel family $\mathscr C$ if every nontrivial member detects the EB/non-EB transition exactly:

$$
\boxed{
\mathcal N
\text{ non-EB}
\iff
(I\otimes\mathcal N)(\Psi)
\text{ entangled}
}
$$

for every nontrivial

$$
\Psi\in\mathscr P
$$

and every

$$
\mathcal N\in\mathscr C.
$$

For a front-faithful probe,

$$
\boxed{
T_{\Psi,E}(R)
=T_{\rm cap}(R).
}
$$

No input optimization is needed to locate the capability front.

---

## 6. Binary coherent states are front faithful for the current Gaussian receiver family

The theorem in `PHASE_INSENSITIVE_GAUSSIAN_BINARY_PROBE_THEOREM.md` says that every nontrivial finite binary coherent hybrid input

$$
\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle
$$

is NPT after a gauge-covariant one-mode phase-insensitive Gaussian channel $\Phi_{\tau,m}$ iff

$$
\tau>m.
$$

But

$$
\tau>m
$$

is exactly the channel's non-EB region.

Therefore

$$
\boxed{
\text{finite binary coherent hybrid probes are front faithful for this Gaussian family.}
}
$$

For Experiment 01 this means

$$
\boxed{
T_{\rm binary\,cat}^{\rm NPT}(R)
=T_{\rm cap}(R)
}
$$

within the phase-insensitive Gaussian receiver model.

This is the strongest conceptual role of the binary coherent theorem: it does not merely prove survival of one special cat state. It gives a **minimal faithful probe of the receiver's exact quantum-capability front**.

---

## 7. Exact matched witness is also front faithful

For the same Gaussian family, the exact three-element witness obeys

$$
\Lambda
=\ln\frac{|z_v|^2}{p_0p_v}
=\frac{N_\Delta}{m}(\tau-m).
$$

Hence

$$
\boxed{
\Lambda>0
\iff
\tau>m
\iff
R_{\rm EB}(\Phi_{\tau,m})>0.
}
$$

Therefore the zero-margin matched witness front also coincides with the capability front:

$$
\boxed{
T_{\rm witness}(R)
=T_{\rm cap}(R)
}
$$

within the ideal model.

A finite experimental margin

$$
\Lambda\ge\Lambda_{\rm req}>0
$$

produces the later finite-certification front.

Thus the clean hierarchy becomes

$$
\boxed{
R/c
\le
T_{\rm cap}
=T_{\rm NPT}
=T_{\rm exact\ witness}
<
T_{\rm finite\ certificate}
}
$$

for the Gaussian binary coherent model when all fronts exist.

---

## 8. Why spacelike entanglement harvesting does not invalidate this front

The front is defined for the **source-controlled input-to-accessible-output channel** $\mathcal A_{R,t}$.

Pre-existing vacuum correlations may allow separately coupled local systems to harvest entanglement in spacelike configurations. That does not imply that the receiver output depends on the controllable source branch-mode input outside the future light cone.

Before causal contact, the source-controlled receiver channel remains a replacer:

$$
\mathcal A_{R,t}(\rho)=\sigma_{R,t}.
$$

Therefore it is EB regardless of any source-independent background correlations.

Experimentally, the corresponding quantity should be defined relative to a control protocol so that pre-existing/background correlations are not mistaken for transported branch information.

---

## 9. Internal versus accessible capability fronts

Let

$$
\mathcal C_{R,t}
$$

be the channel from the incoming gravitational mode to an **internal gravitationally active receiver degree of freedom**, and

$$
\mathcal R_t
$$

be the channel from that internal degree of freedom to an accessible register.

Then

$$
\mathcal A_{R,t}
=\mathcal R_t\circ\mathcal C_{R,t}.
$$

Define

$$
T_{\rm int}(R)
=\inf\{t:R_{\rm EB}(\mathcal C_{R,t})>0\},
$$

and

$$
T_{\rm acc}(R)
=\inf\{t:R_{\rm EB}(\mathcal A_{R,t})>0\}.
$$

Because EB robustness cannot increase under readout post-processing,

$$
R_{\rm EB}(\mathcal A_{R,t})
\le
R_{\rm EB}(\mathcal C_{R,t}),
$$

so

$$
\boxed{
T_{\rm acc}(R)
\ge
T_{\rm int}(R)
\ge
R/c.
}
$$

This is the general strong-gravity accessibility hierarchy.

A black-hole-like system could, in principle, have a very early internal capture front but a very late or nonexistent accessible front.

---

## 10. Gaussian front recovered

For the stationary passive Gaussian receiver,

$$
\mathcal A_{R,t}
=\Phi_{\tau(t),m(t)}.
$$

The channel leaves the EB set exactly when

$$
\tau(t)>m(t).
$$

Using the waveform-optimal capture ceiling gives

$$
\boxed{
T_{\rm cap}(R)
=
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right]
}
$$

when

$$
\kappa_\Delta>\Gamma_{\rm th}.
$$

Thus the previously derived logarithmic NPT front is now understood as an explicit solvable example of the **general EB-capability front**.

---

## 11. Resonant gravity specialization

For the aligned resonant plus-quadrupole wave-zone receiver,

$$
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_{g,B}.
$$

Therefore the compact-resonant front

$$
T_{\rm cap}(R)
=
\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln[1-(R/R_Q^{\rm res})^2]
$$

is not merely a cat-state entanglement curve. It is the **accessible quantum-capability front of the receiver channel** within the Gaussian model.

Binary coherent gravitational branches happen to detect it exactly.

---

## 12. Strongest conceptual compression

> **Relativity fixes the earliest possible influence front. Channel theory fixes a second front: when the complete receiver map first becomes capable of preserving entanglement at all. A particular source state can reveal that capability only at or after that time. The binary coherent gravitational branches used in Experiment 01 are unusually powerful because, for the full phase-insensitive Gaussian receiver family, they reveal the capability immediately: their NPT front is exactly the channel's entanglement-breaking front.**

This formulation cleanly separates causal transport from pre-existing field entanglement and from source-state optimization.

---

## 13. Strongest next question

The remaining deep theoretical target is:

> **Does linearized quantum gravity plus a physically defined accessible receiver admit a non-Gaussian/front-faithful probe family or channel resource whose causal onset can be calculated without assuming a Gaussian memory?**

A parallel practical target is to determine whether the general EB robustness $R_{\rm EB}(\mathcal A_{R,t})$ can be bounded experimentally from a small set of source branch preparations and receiver observables, extending the exact three-element Gaussian witness.