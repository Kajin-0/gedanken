# Conserved Quadrupole Gravity Limit

**Timestamp:** 2026-08-07 14:05 EDT  
**Status:** First gravity-specific reduction; coefficients are tied to the stated quadrupole convention and the coherent-radiation approximation

This note replaces the scalar current by a compact, conserved gravitational source whose branch difference is quadrupolar. It is the first bridge from the scalar matched-history model to linearized gravity.

---

## 1. Why use a quadrupole source?

A lone translating point mass is conceptually useful but not a complete isolated relativistic source: total stress-energy conservation requires the support/actuator to participate. For a compact isolated source, mass and momentum conservation remove time-dependent monopole and mass-dipole radiation. The leading radiative multipole is the mass quadrupole.

Use a branch-difference STF quadrupole

$$
\Delta Q_{ij}(t)
=q(t)\left(n_in_j-\frac13\delta_{ij}\right),
$$

where $\mathbf n$ points from the source toward the probe.

Then

$$
\Delta Q_{ij}\Delta Q_{ij}=\frac23q^2.
$$

The control function $q(t)$ is the difference between the two source histories' quadrupole amplitudes.

---

## 2. Near-zone branch-dependent gravitational force

For the STF quadrupole convention

$$
Q_{ij}=\int d^3x\,\rho(\mathbf x)
\left(x_ix_j-\frac13r^2\delta_{ij}\right),
$$

the Newtonian potential outside a compact source contains

$$
\Phi_Q(R,t)
=\frac{3G}{2R^3}Q_{ij}(t)n_in_j
$$

up to the overall potential-sign convention.

For the axisymmetric branch difference above,

$$
n_in_j\Delta Q_{ij}=\frac23q,
$$

so the branch-dependent potential difference on-axis has magnitude

$$
\boxed{
|\Delta\Phi_Q(R,t)|
=\frac{G|q(t)|}{R^3}.
}
$$

For a probe mass $m_B$ moving radially by the small quantum coordinate $x_B$, the branch-to-branch force difference is therefore

$$
\boxed{
|\Delta F_B(t)|
=\frac{3Gm_B}{R^4}|q(t_R)|,
\qquad
t_R=t-R/c,
}
$$

in the retarded near-zone approximation.

The conditional coherent displacement difference of a harmonic probe is

$$
\boxed{
\Delta\alpha_B(T)
=\frac{3iGm_Bx_{\rm zpf}}{\hbar R^4}
\int_0^{T-R/c}dt\,q(t)e^{i\omega_B(t+R/c)}
}
$$

up to an irrelevant overall phase/sign.

Thus the narrow-band response coefficient per quadrupole amplitude is

$$
\boxed{
|\mathcal R_B^{(G)}|
=\frac{3Gm_Bx_{\rm zpf}}{\hbar R^4}.
}
$$

---

## 3. Complementary graviton record spectrum

The classical quadrupole radiation formula is

$$
P_{\rm GW}
=\frac{G}{5c^5}\dddot Q_{ij}\dddot Q_{ij}.
$$

For the axisymmetric control,

$$
P_{\rm GW}
=\frac{2G}{15c^5}\dddot q^{\,2}.
$$

For coherent radiation, the difference between the two branch-conditioned outgoing graviton states is itself a coherent gravitational-wave displacement. Mode by mode, dividing radiated energy by $\hbar\omega$ gives the mean number of branch-distinguishing gravitons. With the stated positive-frequency/Fourier convention,

$$
\boxed{
N_g
=\frac{2G}{15\hbar c^5}
\int\frac{d\omega}{2\pi}
\omega^5|\widetilde q(\omega)|^2
}
$$

up to convention-dependent factors of order unity associated with one-sided versus two-sided spectra.

For coherent branch-conditioned graviton states,

$$
C_\Xi^2=e^{-N_g},
$$

so

$$
2\Gamma_\Xi=N_g.
$$

Therefore the gravity record spectrum is

$$
\boxed{
S_G(\omega)
\simeq
\frac{2G}{15\hbar c^5}\omega^5
}
$$

for this normalized axisymmetric quadrupole control.

The robust physics is the super-Ohmic $\omega^5$ dependence, not the precise order-unity spectral convention.

---

## 4. Gravity history-transfer rate

Use the scalar-model narrow-band definition

$$
\gamma_{\rm hist}^{(G)}
=\frac{|\mathcal R_B^{(G)}|^2}{S_G(\omega_B)}.
$$

Substitution gives

$$
\gamma_{\rm hist}^{(G)}
\simeq
\frac{135}{2}
\frac{Gm_B^2x_{\rm zpf}^2c^5}
{\hbar R^8\omega_B^5}.
$$

Using

$$
x_{\rm zpf}^2=\frac{\hbar}{2m_B\omega_B},
$$

one obtains

$$
\boxed{
\gamma_{\rm hist}^{(G)}
\simeq
\frac{135}{4}
\frac{Gm_Bc^5}
{R^8\omega_B^6}
}
$$

within the stated convention.

The important invariant scaling is

$$
\boxed{
\gamma_{\rm hist}^{(G)}
\propto
\frac{Gm_Bc^5}{R^8\omega_B^6}.
}
$$

### Key result

The source quadrupole amplitude cancels from this ideal transfer-efficiency ratio. It controls how large the measurable witness is, but not the fundamental ratio of useful branch information received by $B$ to branch information radiated into the gravitational complement.

---

## 5. Gravity history cooperativity

Include probe amplitude damping rate $\kappa_B$. Define

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\equiv
\frac{\gamma_{\rm hist}^{(G)}}{\kappa_B}.
}
$$

Then

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\simeq
\frac{135}{4}
\frac{Gm_Bc^5}
{\kappa_BR^8\omega_B^6}.
}
$$

Equivalently, with mechanical quality factor

$$
Q_B=\frac{\omega_B}{\kappa_B},
$$

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\simeq
\frac{135}{4}
\frac{Gm_Bc^5Q_B}
{R^8\omega_B^7}.
}
$$

The optimized strong history-transfer witness can be positive against **graviton-radiation leakage plus probe damping alone** only if

$$
\boxed{\mathcal C_{\rm hist}^{(G)}>1.}
$$

This is not a complete experimental criterion; technical/environmental decoherence must be added to the denominator in a real system.

---

## 6. Radiation-limited critical radius

Define $R_c$ by

$$
\mathcal C_{\rm hist}^{(G)}(R_c)=1.
$$

Then

$$
\boxed{
R_c
\simeq
\left[
\frac{135}{4}
\frac{Gm_Bc^5}
{\kappa_B\omega_B^6}
\right]^{1/8}.
}
$$

or

$$
\boxed{
R_c
\simeq
\left[
\frac{135}{4}
\frac{Gm_Bc^5Q_B}
{\omega_B^7}
\right]^{1/8}.
}
$$

Because of the eighth root, $R_c$ depends only weakly on probe parameters.

Illustrative radiation-only values from this scaling:

- $m_B=1\,\mathrm{g}$, $f_B=1\,\mathrm{Hz}$, $Q_B=10^8$: $R_c\sim14\,\mathrm{km}$.
- $m_B=1\,\mathrm{kg}$, $f_B=100\,\mathrm{Hz}$, $Q_B=10^6$: $R_c\sim330\,\mathrm{m}$.

These numbers **do not imply measurability at those distances**. They only show that fundamental graviton radiation is an extraordinarily weak information leak compared with the coherent near-field channel; absolute signal strength can still be negligible.

---

## 7. Near-zone versus retardation parameter

Define

$$
\epsilon
=\frac{\omega_BR}{c}.
$$

Substituting

$$
R=\frac{\epsilon c}{\omega_B}
$$

into the cooperativity gives

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\simeq
\frac{135}{4}
\frac{Gm_B\omega_B^2}{\kappa_Bc^3}
\epsilon^{-8}.
}
$$

Using $Q_B=\omega_B/\kappa_B$,

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\simeq
\frac{135}{4}
\frac{Gm_BQ_B\omega_B}{c^3}
\epsilon^{-8}.
}
$$

The small dimensionless parameter

$$
\mu_G
\equiv
\frac{Gm_BQ_B\omega_B}{c^3}
$$

is extraordinarily tiny for laboratory systems.

Therefore the condition $\mathcal C_{\rm hist}^{(G)}>1$ occurs, in this near-zone model, only for

$$
\boxed{
\epsilon
\lesssim
\left(\frac{135}{4}\mu_G\right)^{1/8}\ll1.
}
$$

### Conceptual consequence

The regime in which the intended local probe dominates over graviton leakage is parametrically a **near-field regime**, while dynamically resolvable propagation delay pushes toward $\epsilon\sim1$.

This quantifies a causality-versus-coupling tension:

- near zone: strong reactive/coherent branch transfer, tiny retardation phase;
- wave zone: retardation is visible, but information is carried away in propagating gravitational modes and a local receiver captures only a fraction.

The near-zone formula must not be extrapolated quantitatively to $\epsilon\sim1$; a full retarded TT calculation is required there. The scaling nevertheless identifies the crossover problem that the next calculation should address.

---

## 8. Ideal shell-receiver Gedanken limit

The above tension is not a logical prohibition. It is largely a **mode-capture problem**.

As an idealized Gedanken experiment, replace the local oscillator by a spherical quantum receiver matched to the outgoing quadrupolar gravitational mode. If the receiver coherently captures a fraction $\tau_{\rm ch}$ of the branch-distinguishing outgoing mode, the pure-loss benchmark gives

$$
\mathcal M_\Xi
=(2\tau_{\rm ch}-1)|\Delta|^2.
$$

A strong positive history-transfer witness requires

$$
\tau_{\rm ch}>1/2.
$$

An ideal mode-matched enclosing receiver could approach $\tau_{\rm ch}\to1$ in the Gedanken limit, making the causal arrival of quantum branch information conceptually clean even though such a gravitational receiver is far beyond current technology.

This suggests two distinct versions of Experiment 01:

1. **near-field local-probe version:** experimentally closer in spirit, optimized for nonclassicality but poor for direct retardation;
2. **wave-zone enclosing-receiver Gedanken version:** optimized for conceptual demonstration of causal quantum-information transport.

---

## 9. Novelty discipline

The Newtonian quadrupole potential, quadrupole radiation formula, coherent-state graviton counting, cooperativity concepts, and pure-loss channel threshold are established ingredients.

Potentially distinctive physics lies in combining them into the **history-transfer** framework and identifying the near-field/wave-zone tradeoff in terms of a single source-independent quantum-information efficiency.

The next technical task is a full linearized-gravity calculation of the retarded and complementary kernels for a conserved quadrupole source, including the crossover from near zone to wave zone. That calculation will determine whether the scaling above survives as a rigorous statement and whether a useful causal-history inequality emerges beyond the toy limits.
