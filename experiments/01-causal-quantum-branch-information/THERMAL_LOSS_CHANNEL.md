# Thermal and Lossy Wave-Zone Receiver

**Timestamp:** 2026-08-07 15:19 EDT  
**Status:** Active derivation for Experiment 01

This note extends the ideal wave-zone difference-mode receiver to finite thermal occupation and internal loss.

---

## 1. Stronger separability bound using fidelity

For a balanced source-path state

$$
\rho_{AB}=\frac12
\begin{pmatrix}
\rho_L & \Xi\\
\Xi^\dagger & \rho_R
\end{pmatrix},
$$

define

$$
C_\Xi=\|\Xi\|_1.
$$

If the state is separable,

$$
\rho_{AB}=\sum_k p_k\,\tau_A^{(k)}\otimes\sigma_B^{(k)},
$$

with

$$
\tau_A^{(k)}=
\begin{pmatrix}
a_k&c_k\\
c_k^*&b_k
\end{pmatrix},
\qquad a_k+b_k=1,
$$

then positivity implies

$$
|c_k|\le\sqrt{a_kb_k}.
$$

Balanced normalization gives

$$
\rho_L=2\sum_kp_ka_k\sigma_k,
\qquad
\rho_R=2\sum_kp_kb_k\sigma_k,
$$

and

$$
\Xi=2\sum_kp_kc_k\sigma_k.
$$

Therefore

$$
C_\Xi\le2\sum_kp_k\sqrt{a_kb_k}.
$$

Using joint concavity and homogeneity of the root Uhlmann fidelity,

$$
F_B\equiv F(\rho_L,\rho_R)
\ge2\sum_kp_k\sqrt{a_kb_k}.
$$

Hence every balanced separable source-probe state obeys

$$
\boxed{C_\Xi\le F_B.}
$$

Define the fidelity history margin

$$
\boxed{
\mathcal M_F\equiv\ln\frac{C_\Xi}{F_B}.
}
$$

Then

$$
\boxed{\mathcal M_F>0}
$$

certifies source-probe entanglement.

This bound is stronger than the earlier trace-distance witness because the Fuchs-van de Graaf relation implies

$$
F_B\le\sqrt{1-D_B^2}.
$$

The underlying coherence/fidelity mathematics is not claimed as novel; its role here is to make the thermal gravitational receiver analytically tractable.

---

## 2. Ideal controlled displacement with a thermally occupied receiver

Let the receiver begin in a thermal state with mean occupation $\bar n_0$ and let the two source branches produce opposite displacements whose difference is

$$
\Delta\alpha.
$$

The conditional receiver states are displaced thermal states with identical covariance. Their root fidelity is

$$
\boxed{
F_B
=\exp\left[-\frac{|\Delta\alpha|^2}{2(2\bar n_0+1)}\right].
}
$$

For an otherwise isolated controlled unitary,

$$
\Xi=U_L\rho_{\rm th}U_R^\dagger,
$$

so unitary invariance of the trace norm gives

$$
\boxed{C_\Xi=1.}
$$

Thus

$$
\boxed{
\mathcal M_F
=\frac{|\Delta\alpha|^2}{2(2\bar n_0+1)}>0
}
$$

for every finite $\bar n_0$ and every nonzero branch-dependent displacement.

Interpretation: **initial thermal occupation suppresses the measurable size of the witness but does not by itself impose an entanglement threshold.** Continuous coupling to an uncontrolled bath is qualitatively different because that bath can acquire a branch record.

---

## 3. Thermal-loss channel for the captured gravitational difference mode

Model the incoming branch-difference graviton mode as coherent states separated by

$$
|\Delta|^2=N_\Delta.
$$

Let the coherent capture channel be a thermal attenuator with transmissivity $\eta$. The unused input port is thermal with mean occupation $\bar n$.

The receiver obtains displacement separation

$$
|\Delta_B|^2=\eta N_\Delta,
$$

while its conditional covariance corresponds to output thermal occupation

$$
\bar n_B=(1-\eta)\bar n.
$$

Define

$$
D\equiv1+2(1-\eta)\bar n.
$$

The root fidelity of the two receiver states is

$$
\boxed{
F_B
=\exp\left[-\frac{\eta N_\Delta}{2D}\right].
}
$$

To compute $C_\Xi$, purify the thermal loss port by a two-mode squeezed ancilla and use the complementary Gaussian channel. The two complementary outputs have the same covariance and differ only by a displacement. The resulting complementary fidelity is

$$
\boxed{
C_\Xi
=\exp\left[
-\frac{(1-\eta)(2\bar n+1)N_\Delta}{2D}
\right].
}
$$

For $\bar n=0$, these reduce to the ideal pure-loss results

$$
F_B=e^{-\eta N_\Delta/2},
\qquad
C_\Xi=e^{-(1-\eta)N_\Delta/2}.
$$

---

## 4. Exact thermal fidelity-history margin

The fidelity margin is

$$
\boxed{
\mathcal M_F
=\ln\frac{C_\Xi}{F_B}
=
\frac{N_\Delta}{2D}
\left[
2(\bar n+1)\eta-(2\bar n+1)
\right].
}
$$

Therefore the strong thermal witness is positive iff

$$
\boxed{
\eta>\eta_c(\bar n)
=\frac{2\bar n+1}{2\bar n+2}.
}
$$

Checks:

$$
\bar n=0\Rightarrow\eta_c=\frac12,
$$

while

$$
\bar n\to\infty\Rightarrow\eta_c\to1.
$$

Equivalently,

$$
\boxed{
\bar n<\frac{2\eta-1}{2(1-\eta)}
}
$$

for $\eta>1/2$.

Since $\bar n_B=(1-\eta)\bar n$, the same condition can be written

$$
\boxed{
\bar n_B<\eta-\frac12.
}
$$

This is a compact physical statement: **the captured branch-information fraction must exceed one half plus the receiver's added thermal occupation measured in quanta of the matched mode.**

---

## 5. Input-output memory with internal thermal loss

For the matched receiver memory

$$
\dot c
=-\frac{\kappa_g+\kappa_i}{2}c
+\sqrt{\kappa_g}\,b_{\rm in}
+\sqrt{\kappa_i}\,\xi_{\rm in},
$$

an optimally shaped rising-exponential gravitational input maps the selected incoming mode to the memory with

$$
\eta_{\max}
=\frac{\kappa_g}{\kappa_g+\kappa_i}.
$$

If the internal bath has occupation $\bar n_i$, the thermal strong-witness condition becomes

$$
\frac{\kappa_g}{\kappa_g+\kappa_i}
>
\frac{2\bar n_i+1}{2\bar n_i+2}.
$$

This simplifies exactly to

$$
\boxed{
\kappa_g>(2\bar n_i+1)\kappa_i.
}
$$

Define the thermal history cooperativity

$$
\boxed{
\mathcal C_{\rm hist}^{(T)}
\equiv
\frac{\kappa_g}{(2\bar n_i+1)\kappa_i}.
}
$$

Then

$$
\boxed{
\mathcal C_{\rm hist}^{(T)}>1
}
$$

is the matched-memory threshold for the fidelity history witness.

At zero temperature this reduces to

$$
\kappa_g>\kappa_i,
$$

the previously derived vacuum result.

At high temperature,

$$
2\bar n_i+1\simeq2\bar n_i,
$$

so the tolerated internal loss rate decreases inversely with thermal occupation.

---

## 6. Continuous thermal damping of a branch-driven oscillator

For a receiver oscillator damped at rate $\kappa$ into a Markovian thermal bath of occupation $\bar n_b$, let

$$
\Delta\alpha(t)
$$

be the separation of the two conditional oscillator trajectories.

The receiver covariance remains branch-independent. If its occupation at the measurement time is $\bar n_B(T)$, then

$$
\boxed{
F_B(T)
=\exp\left[
-\frac{|\Delta\alpha(T)|^2}{2(2\bar n_B(T)+1)}
\right].
}
$$

The same thermal bath acquires a continuous branch record. In the Markovian Gaussian limit the corresponding history-coherence loss is

$$
\boxed{
\Gamma_{\rm bath}(T)
=\frac{\kappa}{2}(2\bar n_b+1)
\int_0^Tdt\,|\Delta\alpha(t)|^2.
}
$$

Thus

$$
\boxed{
\mathcal M_F(T)
=
\frac{|\Delta\alpha(T)|^2}{2(2\bar n_B(T)+1)}
-
\frac{\kappa}{2}(2\bar n_b+1)
\int_0^Tdt\,|\Delta\alpha(t)|^2.
}
$$

This formula exposes the distinction between two thermal effects:

1. **initial thermal occupation** broadens the receiver and reduces branch distinguishability;
2. **continuous thermal damping** additionally exports branch information into an uncontrolled bath and directly reduces recoverable history coherence.

For an initially equilibrated receiver, $\bar n_B=\bar n_b=\bar n$.

---

## 7. Constant resonant branch drive: finite witness window

For a resonant constant drive with steady conditional separation $\Delta\alpha_{\rm ss}$,

$$
\Delta\alpha(t)
=\Delta\alpha_{\rm ss}
\left(1-e^{-\kappa t/2}\right).
$$

Let

$$
x=\kappa T.
$$

Then

$$
\mathcal M_F(T)
=\frac{|\Delta\alpha_{\rm ss}|^2}{2}
\left[
\frac{(1-e^{-x/2})^2}{2\bar n+1}
-(2\bar n+1)
\left(
 x-4(1-e^{-x/2})+(1-e^{-x})
\right)
\right].
$$

The sign is independent of drive amplitude. Thermal damping therefore creates a finite time window during which coherent branch transfer can beat exported bath records.

For $x\ll1$,

$$
\mathcal M_F>0
$$

approximately requires

$$
\boxed{
\kappa T
\lesssim
\frac{3}{(2\bar n+1)^2}.
}
$$

At zero temperature the exact first nontrivial crossing is

$$
\kappa T\approx2.303.
$$

For $\bar n\gg1$, the crossing approaches

$$
\kappa T\simeq\frac{3}{(2\bar n+1)^2}.
$$

Thus high thermal occupation not only reduces the witness amplitude; with continuous bath contact it sharply compresses the available coherent-history time window.

---

## 8. Relation to current literature

The fidelity of displaced thermal Gaussian states is established Gaussian-state theory (e.g. Marian & Marian, PRA 76, 054307 (2007), and later general Gaussian fidelity formulas). The general fact that thermal initial states and continuous thermal baths degrade spin/oscillator entanglement witnesses is also established; Premawardhana, Bowman, and Taylor explicitly analyze both effects for an interferometer-mechanical-oscillator architecture and show the importance of the oscillator quality factor.

No novelty is claimed for those ingredients.

The potentially distinctive result for this project is the way they enter the **causal gravitational history-transfer framework**, particularly the compact matched-memory threshold

$$
\boxed{
\kappa_g>(2\bar n_i+1)\kappa_i
}
$$

and its interpretation as a competition between coherent capture of the gravitational difference mode and thermal export of the branch record.

---

## 9. Immediate next step

The next calculation should determine whether the thermal fidelity witness is merely sufficient or becomes exact for the specific source-qubit + Gaussian thermal-loss family. This requires calculating the partial-transpose spectrum / exact negativity of the qubit-mode output under a thermal attenuator.

That will answer a sharp question:

> **At finite temperature, is there a true minimum gravitational capture efficiency for source-receiver entanglement, or only a minimum efficiency for our low-cost fidelity witness?**
