# Independent Cascaded-Network Check of the Four-Factor Link Budget

**Date:** 2026-08-08  
**Status:** **NO-DOUBLE-COUNTING CHECK — FACTORIZATION RECOVERED WITHOUT USING THE GRAVITATIONAL SELF-ENERGY**

## 1. Question

The V6 central equation is

$$
\boxed{
\tau_{A\to B}(t)
=
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t).}
$$

Because

$$
\eta_{\rm store}
$$

was originally derived from a source-receiver retarded self-energy containing both

$$
\kappa_{g,A}
\quad\text{and}\quad
\kappa_{g,B},
$$

a natural concern is whether multiplying by the source and receiver gravitational branching fractions later **double counts** either coupling.

This note derives the same result from an independent cascaded bosonic network with four explicit stages:

1. source decay splitter;
2. free-space mode beamsplitter;
3. receiver gravitational input port;
4. receiver total damping.

The gravitational self-energy is not used in the derivation.

---

# 2. Source emission as a beamsplitter

Let

$$
A
$$

denote the virtual normalized source branch mode whose initial state contains the information to be emitted.

For vacuum nongravitational source ports, the complete source emission stage is a pure-loss channel of transmissivity

$$
\boxed{
\beta_{g,A}
=\frac{\kappa_{g,A}}{\kappa_A}.}
$$

Therefore the normalized emitted gravitational mode can be written

$$
\boxed{
G
=\sqrt{\beta_{g,A}}\,A
+\sqrt{1-\beta_{g,A}}\,V_A,}
$$

where

$$
V_A
$$

is an environmental vacuum mode chosen to complete the canonical transformation.

Thus

$$
[G,G^\dagger]=1.
$$

At the level of coherent amplitudes,

$$
\alpha_G
=\sqrt{\beta_{g,A}}\,\alpha_A.
$$

Nothing about free-space propagation or the receiver has entered yet.

---

# 3. Propagation/source-mode projection as a second beamsplitter

Let the normalized source gravitational mode reach the one normalized travelling mode accepted by the receiver with transmissivity

$$
\boxed{
\eta_{\rm store}.}
$$

Define the normalized receiver-incident mode

$$
\boxed{
H
=\sqrt{\eta_{\rm store}}\,G
+\sqrt{1-\eta_{\rm store}}\,V_P,}
$$

where

$$
V_P
$$

collects the orthogonal free-space gravitational modes.

Substituting the source splitter,

$$
\boxed{
H
=\sqrt{\beta_{g,A}\eta_{\rm store}}\,A
+\sqrt{\eta_{\rm store}(1-\beta_{g,A})}\,V_A
+\sqrt{1-\eta_{\rm store}}\,V_P.}
$$

Again,

$$
[H,H^\dagger]=1.
$$

Thus the amplitude coefficient of the original source mode at the receiver input is already

$$
\boxed{
\sqrt{\beta_{g,A}\eta_{\rm store}}.}
$$

The propagation factor is therefore distinct from the source branching factor.

---

# 4. Receiver input-output equation

Let

$$
b(t)
$$

be the receiver memory mode.

Its total linewidth is

$$
\boxed{
\kappa_B
=\kappa_{g,B}+\sum_r\kappa_r,}
$$

where

$$
\kappa_{g,B}
$$

is the total receiver coupling to the gravitational continuum and the

$$
\kappa_r
$$

are nongravitational ports.

Assume the selected incident travelling mode has temporal envelope

$$
f(t),
\qquad
\int_0^\infty dt\,|f(t)|^2=1.
$$

The incident field in the selected gravitational channel is

$$
b_{g,B}^{\rm in}(t)
=f(t)H
+\text{orthogonal vacuum modes}.
$$

The receiver Langevin equation is

$$
\boxed{
\dot b
=-\frac{\kappa_B}{2}b
+\sqrt{\kappa_{g,B}}\,
 b_{g,B}^{\rm in}(t)
+\sum_r\sqrt{\kappa_r}\,v_r^{\rm in}(t).}
$$

Ignoring only the branch-independent noise terms for the moment, the source-dependent receiver amplitude is

$$
\boxed{
b(t)\big|_A
=
\sqrt{\beta_{g,A}\eta_{\rm store}\kappa_{g,B}}
\left[
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}f(s)
\right]A.}
$$

---

# 5. Source→receiver coherent parameter

The squared coefficient multiplying

$$
A
$$

is therefore

$$
\tau_{A\to B}(t)
=
\beta_{g,A}\eta_{\rm store}\kappa_{g,B}
\left|
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}f(s)
\right|^2.
$$

Define

$$
\boxed{
\beta_{g,B}
=\frac{\kappa_{g,B}}{\kappa_B}}
$$

and

$$
\boxed{
\mathcal T_f(t)
=\kappa_B
\left|
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}f(s)
\right|^2.}
$$

Then

$$
\boxed{
\tau_{A\to B}(t)
=
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t).}
$$

This is exactly the V6 link-budget factorization.

No gravitational self-energy was used in this derivation.

---

# 6. Why receiver branching is not already inside \(\eta_{\rm store}\)

The distinction is visible directly in the network.

### \(\eta_{\rm store}\)

specifies how much of the normalized source gravitational wavepacket occupies the one normalized travelling input mode geometrically/mode matched to the receiver.

### \(\kappa_{g,B}\)

specifies how strongly the receiver memory couples to the total gravitational bath once that field arrives.

### \(\beta_{g,B}\)

compares the receiver's gravitational coupling to all of its loss channels:

$$
\beta_{g,B}
=\frac{\kappa_{g,B}}
{\kappa_{g,B}+\kappa_i+\cdots}.
$$

Thus

$$
\eta_{\rm store}
$$

does not contain the receiver's competition with ordinary internal loss.

This is why multiplying by

$$
\beta_{g,B}
$$

is necessary rather than double counting.

---

# 7. Why source branching is not already inside \(\eta_{\rm store}\)

Likewise,

$$
\eta_{\rm store}
$$

is defined **conditional on the normalized gravitational source output mode**.

The retarded self-energy expression

$$
\Sigma_{BA}^R
\propto
\sqrt{\kappa_{g,A}\kappa_{g,B}}
$$

is divided by

$$
\sqrt{\kappa_{g,A}\kappa_{g,B}}
$$

when converted into the normalized travelling-mode amplitude

$$
t_{BA}^{\rm store}.
$$

Therefore the source intrinsic graviton matrix element cancels from

$$
\eta_{\rm store}=|t_{BA}^{\rm store}|^2.
$$

The probability that a physical source excitation enters the gravitational bath in the first place is a separate factor

$$
\beta_{g,A}.
$$

The independent beamsplitter derivation makes this separation explicit.

---

# 8. Vacuum noise and complete positivity

The omitted vacuum terms are not optional bookkeeping; they are required to preserve the receiver commutator.

The receiver mode has contributions from

- source nongravitational vacuum
  $$
  V_A;
  $$
- orthogonal propagating gravitational vacuum
  $$
  V_P;
  $$
- receiver orthogonal gravitational input vacuum;
- receiver nongravitational vacuum ports;
- the receiver initial mode.

When all of those baths are in vacuum, they produce attenuation but no positive vacuum-output occupation

$$
m
$$

in the repository phase-insensitive Gaussian convention.

Thus

$$
\beta_{g,A},
\quad
\eta_{\rm store},
\quad
\beta_{g,B},
\quad
\mathcal T_f
$$

are all pure coherent-transfer penalties in the ideal vacuum link.

---

# 9. Thermal source noise

Now let the source gravitational output mode have the Gaussian form

$$
G
=\sqrt{\beta_{g,A}}\,A
+N_A,
$$

where

$$
\langle N_A^\dagger N_A\rangle
=m_A.
$$

After propagation and receiver loading, that source-noise occupation is multiplied by the downstream coherent transmissivity

$$
\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).
$$

Therefore

$$
\boxed{
m_{A\to B}(t)
=m_B(t)
+\eta_{\rm store}\beta_{g,B}\mathcal T_f(t)m_A.}
$$

This independently reproduces the Gaussian composition rule used in V6.

The complete non-EB condition is

$$
\boxed{
\eta_{\rm store}\beta_{g,B}\mathcal T_f(t)
[\beta_{g,A}-m_A]
>m_B(t).}
$$

Thus the thermal link budget follows from the same explicit network.

---

# 10. Friis form

Using

$$
\eta_{\rm store}
=\mathcal O
G_AG_B
\left(
\frac{\lambda}{4\pi R}
\right)^2,
$$

the independently checked network result becomes

$$
\boxed{
\tau_{A\to B}(t)
=\beta_{g,A}
\mathcal O
G_AG_B
\left(
\frac{\lambda}{4\pi R}
\right)^2
\beta_{g,B}
\mathcal T_f(t).}
$$

For the aligned plus-quadrupole channel,

$$
G_A=G_B=5/2.
$$

This is precisely the expected serial quantum-interface structure:

$$
\boxed{
\text{source quantum efficiency}
\times
\text{free-space antenna link}
\times
\text{receiver quantum efficiency}
\times
\text{temporal mode loading}.}
$$

---

# 11. Adversarial verdict

The four-factor V6 link budget does **not** double count gravitational coupling.

The factors refer to four different canonical transformations:

1. source mode → total gravitational output;
2. total source gravitational output → one receiver-incident travelling mode;
3. incident gravitational field → receiver memory versus receiver loss channels;
4. finite-time temporal projection into the memory.

The exact same product is obtained without using the retarded self-energy derivation.

This makes the link factorization structurally robust within the one-way linear Markov model.
