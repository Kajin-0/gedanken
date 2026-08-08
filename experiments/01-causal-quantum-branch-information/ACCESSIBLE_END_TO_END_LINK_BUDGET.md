# Accessible End-to-End Gravitational Quantum Link Budget

**Date:** 2026-08-08  
**Status:** **FINAL-INTERFACE EXTENSION — THE FOUR-FACTOR V6 LINK ENDS AT THE RECEIVER MEMORY; ACCESSIBLE READOUT IS A SEPARATE CHANNEL**

## 1. Why the four-factor link is not yet the final accessible channel

The V6 coherent-transfer backbone is

$$
\boxed{
\tau_{A\to B}(t)
=
\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).}
$$

Together with source/receiver noise it defines a channel

$$
\boxed{
\Phi_{\rm mem}
=\Phi_{\tau_c,m_c}}
$$

from the virtual source difference mode to the **receiver memory mode**.

That is the correct object for asking whether the gravitational field can load a quantum memory while preserving entanglement.

It is not automatically the same as the channel to an experimentally accessible output register.

A receiver may

- absorb strongly;
- store a non-EB state;
- yet have a noisy or lossy readout that destroys the remaining entanglement before it becomes accessible.

Therefore append a separate readout channel.

---

# 2. Capture/memory channel

Write the gravitational source→memory channel as

$$
\boxed{
\Phi_c
=\Phi_{\tau_c,m_c}.}
$$

For V6,

$$
\boxed{
\tau_c(t)
=\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t).}
$$

In the thermal Gaussian source/receiver model,

$$
\boxed{
m_c(t)
=m_B(t)
+\eta_{\rm store}\beta_{g,B}\mathcal T_f(t)m_A.}
$$

Define the memory quantum excess

$$
\boxed{
\Delta_{\rm mem}(t)
\equiv
\tau_c(t)-m_c(t).}
$$

For a phase-insensitive one-mode Gaussian channel,

$$
\boxed{
\Delta_{\rm mem}>0
}
$$

is exactly the non-entanglement-breaking condition in the repository convention.

---

# 3. Readout channel

Let the memory be converted into an accessible quantum register by a second phase-insensitive Gaussian channel

$$
\boxed{
\Phi_r
=\Phi_{\tau_r,m_r}.}
$$

Here

- \(\tau_r\) is the coherent readout transmissivity/gain parameter in the same channel convention;
- \(m_r\) is the readout vacuum-output occupation/noise parameter.

The complete accessible channel is

$$
\boxed{
\Phi_{\rm acc}
=\Phi_r\circ\Phi_c.}
$$

---

# 4. Exact Gaussian composition

For the vacuum-output-occupation convention used throughout the repository,

$$
\tau_{2\circ1}
=\tau_2\tau_1,
$$

$$
m_{2\circ1}
=m_2+\tau_2m_1.
$$

Therefore

$$
\boxed{
\tau_{\rm acc}
=\tau_r\tau_c,}
$$

and

$$
\boxed{
m_{\rm acc}
=m_r+\tau_r m_c.}
$$

The accessible channel is non-EB iff

$$
\tau_{\rm acc}>m_{\rm acc}.
$$

Hence

$$
\boxed{
\tau_r\tau_c
>
m_r+\tau_r m_c.}
$$

Equivalently,

$$
\boxed{
\tau_r(\tau_c-m_c)>m_r.}
$$

---

# 5. Accessible quantum excess

Using

$$
\Delta_{\rm mem}=\tau_c-m_c,
$$

define

$$
\boxed{
\Delta_{\rm acc}
\equiv
\tau_{\rm acc}-m_{\rm acc}.}
$$

Then

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_{\rm mem}-m_r.}
$$

Thus the entire readout stage acts on the one scalar memory margin by

1. attenuating/amplifying it by
   $$
   \tau_r;
   $$
2. subtracting the readout's own added-noise budget
   $$
   m_r.
   $$

This gives the clean final capability criterion

$$
\boxed{
\Delta_{\rm acc}>0.}
$$

---

# 6. Pure-loss readout

If the readout is quantum-limited pure loss,

$$
\boxed{m_r=0,}
$$

then

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_{\rm mem}.}
$$

Therefore every nonzero pure-loss readout transmissivity preserves the **sign** of the non-EB margin:

$$
\boxed{
\Delta_{\rm mem}>0,
\quad
\tau_r>0
\Longrightarrow
\Delta_{\rm acc}>0.}
$$

However the absolute entanglement amount and certification signal still shrink with

$$
\tau_r.
$$

Thus a pure-loss readout can make the quantum effect arbitrarily hard to observe without changing the mathematical EB sign.

---

# 7. Noisy readout can destroy a quantum memory

If

$$
m_r>0,
$$

then a memory channel can be non-EB while the accessible channel is EB.

The readout requirement is

$$
\boxed{
\tau_r
>
\frac{m_r}{\Delta_{\rm mem}}.}
$$

For an extremely weak gravitational memory link,

$$
\Delta_{\rm mem}\ll1,
$$

the required readout added noise becomes correspondingly severe.

This is especially important for the ordinary/ordinary benchmark where even the ideal vacuum coherent-transfer scale is

$$
\sim10^{-42}.
$$

A readout with any fixed positive

$$
m_r
\gg10^{-42}
$$

would make the final accessible Gaussian channel entanglement breaking, regardless of how cleanly the gravitational memory itself was loaded.

---

# 8. Link-budget form with readout appended

The capture transmissivity is

$$
\tau_c(t)
=
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t).
$$

Therefore

$$
\boxed{
\tau_{\rm acc}(t)
=
\tau_r
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t).}
$$

For pure-loss readout this simply appends one additional efficiency factor.

For noisy readout, however, the complete capability condition is additive in noise:

$$
\boxed{
\tau_r
\left[
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t)
-m_c(t)
\right]
>m_r.}
$$

Thus the full end-to-end architecture is better represented as

$$
\boxed{
\text{source coherence}
\to
\text{source branching}
\to
\text{propagation/mode capture}
\to
\text{receiver branching/loading}
\to
\text{memory noise}
\to
\text{readout channel}.}
$$

---

# 9. Distinguish three different questions

The project should now keep three operational levels separate.

## 9.1 Travelling-mode reception

Given a normalized incoming gravitational wavepacket, how much enters the receiver?

This is approximately

$$
\eta_{\rm store}\beta_{g,B}\mathcal T_f.
$$

## 9.2 Source→memory link

Given a physical source mode, how much coherent branch amplitude reaches the receiver memory?

This is

$$
\boxed{
\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f.}
$$

## 9.3 Accessible source→output link

After receiver readout, does an experimentally accessible quantum register remain non-EB with the source/reference?

This requires

$$
\boxed{
\tau_r\Delta_{\rm mem}>m_r.}
$$

Conflating these three questions is exactly how optimistic receiver-local estimates can be mistaken for complete experimental capability.

---

# 10. Relation to strong absorbers

The same logic applies to exotic strong gravitational absorbers.

A compact object, collective resonance, or strongly self-gravitating mode may achieve a large capture rate or gravitational branching fraction.

That alone does not guarantee a useful quantum receiver.

If its accessible readout is highly noisy or effectively traces over the absorbed quantum state, then

$$
\Delta_{\rm acc}
\le0
$$

can still hold.

Thus

$$
\boxed{
\text{strong absorption}\ne\text{accessible quantum memory}.}
$$

This is why black-hole-like or astrophysical receivers cannot be promoted as solutions to the interface problem without specifying a quantum-coherent accessible output.

---

# 11. Non-Gaussian generalization

The scalar

$$
\Delta=\tau-m
$$

is convenient only for the phase-insensitive Gaussian family.

For a general capture map

$$
\mathcal C
$$

and readout map

$$
\mathcal R,
$$

the accessible channel is

$$
\boxed{
\mathcal A
=\mathcal R\circ\mathcal C.}
$$

Any entanglement monotone between an untouched reference and the receiver cannot increase under the local readout map.

Likewise any reasonable distance/resource relative to the EB set is nonincreasing under post-processing.

Thus the qualitative conclusion is general:

> readout cannot restore source-reference entanglement that capture has already destroyed, and a noisy readout can destroy entanglement that capture preserved.

The Gaussian formula above simply gives the exact scalar condition for the present model.

---

# 12. Manuscript consequence

The V6 main paper currently ends its central link budget at the receiver memory. That is acceptable if stated explicitly.

Recommended wording:

> ``Equation (...) is the source-to-memory quantum-link budget. An experimentally accessible output requires an additional readout channel. For a phase-insensitive Gaussian readout \((\tau_r,m_r)\), the accessible non-EB margin is \(\Delta_{\rm acc}=\tau_r\Delta_{\rm mem}-m_r\). We therefore do not identify strong gravitational capture with an accessible quantum communication channel unless the readout stage is also specified.''

Do not silently call

$$
\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f
$$

the complete measurable communication efficiency if readout is not included.

---

# 13. Strongest final interface statement

For the Gaussian version of the V6 architecture, define

$$
\boxed{
\Delta_{\rm mem}(t)
=
\tau_c(t)-m_c(t),}
$$

with

$$
\tau_c(t)
=eta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).
$$

After readout,

$$
\boxed{
\Delta_{\rm acc}(t)
=	au_r\Delta_{\rm mem}(t)-m_r.}
$$

The complete accessible quantum-capability condition is

$$
\boxed{
\Delta_{\rm acc}(t)>0.}
$$

This is the natural final stage of the end-to-end gravitational quantum link budget.
