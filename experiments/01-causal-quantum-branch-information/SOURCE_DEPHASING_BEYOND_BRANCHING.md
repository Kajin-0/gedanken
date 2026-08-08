# Source Dephasing Beyond the Gravitational Branching Fraction

**Date:** 2026-08-08  
**Status:** **SCOPE CORRECTION — THE FOUR-FACTOR LINK IS A COHERENT-TRANSFER BUDGET, NOT A COMPLETE NOISE MODEL FOR NON-GAUSSIAN SOURCE DEPHASING**

## 1. Motivation

The V6 coherent link factor is

$$
\boxed{
\tau_{A\to B}(t)
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).}
$$

In the ideal linear amplitude-damping network,

$$
\beta_{g,A}=\kappa_{g,A}/\kappa_A
$$

has a precise interpretation: it is the fraction of the complete branch-difference coherent-state norm emitted into the gravitational source port.

It is tempting to call

$$
\beta_{g,A}
$$

the complete ``source quantum efficiency.''

That would be too strong.

A source can preserve energy perfectly while losing the phase coherence required to transfer entanglement. Pure dephasing, stochastic frequency noise, and nonlinear phase diffusion do not appear as ordinary amplitude-loss branching fractions.

The four-factor V6 equation must therefore be understood as a **coherent amplitude-transfer coefficient**, supplemented by a separate source-noise/dephasing channel when such mechanisms are present.

---

# 2. Amplitude damping versus phase noise

For linear amplitude damping, source loss ports obey

$$
\Delta b_j^{\rm out}(t)
=2\sqrt{\kappa_j}\,\alpha(t),
$$

so

$$
N_{\Delta,j}
=4\kappa_j\int dt\,|\alpha(t)|^2.
$$

The gravitational fraction is therefore

$$
\boxed{
\beta_{g,A}
=\frac{N_{\Delta,g}}
{N_{\Delta,{\rm all}}}
=\frac{\kappa_{g,A}}{\kappa_A}.}
$$

This describes redistribution of a coherent displacement among output ports.

Pure dephasing is different. A simple bosonic phase-diffusion channel has the form

$$
\boxed{
\mathcal D_p(\rho)
=\int d\theta\,p(\theta)
 e^{-i\theta n}
\rho
 e^{+i\theta n},
}
$$

where

$$
n=a^\dagger a.
$$

It can leave

$$
\langle n\rangle
$$

unchanged while suppressing phase-sensitive coherences.

Thus energy branching and quantum phase coherence are independent resources.

---

# 3. Exact counterexample: perfect branching but zero entanglement

Consider the ideal binary-coherent reference/source state

$$
\boxed{
|\Psi\rangle
=\frac{
|0\rangle_R|+a\rangle
+|1\rangle_R|-a\rangle
}{\sqrt2}.}
$$

Suppose the source has

$$
\beta_{g,A}=1,
$$

so no amplitude is lost into nongravitational ports.

Now apply **complete phase randomization**,

$$
\boxed{
p(\theta)=\frac1{2\pi},
\qquad0\le\theta<2\pi.}
$$

For a real coherent amplitude,

$$
|\pm a e^{-i\theta}\rangle
=e^{-a^2/2}
\sum_{n=0}^\infty
\frac{(\pm a)^n e^{-in\theta}}
{\sqrt{n!}}
|n\rangle.
$$

The phase-randomized reference/source state is

$$
\rho_{RA}^{\rm pd}
=\int_0^{2\pi}\frac{d\theta}{2\pi}
|\Psi_\theta\rangle
\langle\Psi_\theta|,
$$

where

$$
|\Psi_\theta\rangle
=\frac{
|0\rangle|+a e^{-i\theta}\rangle
+|1\rangle|-a e^{-i\theta}\rangle
}{\sqrt2}.
$$

The phase integral removes all terms with unequal Fock number.

Define

$$
\boxed{
 p_n=e^{-a^2}\frac{a^{2n}}{n!}}
$$

and the normalized parity-dependent qubit states

$$
\boxed{
|\chi_n\rangle_R
=\frac{|0\rangle+(-1)^n|1\rangle}{\sqrt2}.}
$$

Then the fully phase-randomized state is exactly

$$
\boxed{
\rho_{RA}^{\rm pd}
=\sum_{n=0}^\infty
p_n
|\chi_n\rangle\langle\chi_n|_R
\otimes
|n\rangle\langle n|_A.}
$$

This is manifestly separable.

Therefore

$$
\boxed{
\beta_{g,A}=1
\quad\not\Rightarrow\quad
\text{entanglement-capable source}.}
$$

Complete phase diffusion destroys the source-reference entanglement without any energy loss at all.

---

# 4. Why the four-factor coherent transfer can remain unchanged

For a quasi-static random phase

$$
\theta,
$$

the emitted normalized mode is simply multiplied by

$$
e^{-i\theta}.
$$

The receiver temporal loading magnitude

$$
\left|
\int ds\,
K(t,s)f(s)e^{-i\theta}
\right|^2
$$

is unchanged for each realization because the phase is global over the pulse.

Thus the scalar coherent intensity coefficient

$$
\tau_{A\to B}
$$

can remain numerically unchanged while the ensemble-averaged reference–receiver state loses entanglement.

This is a decisive counterexample to interpreting

$$
\tau
$$

or

$$
\beta_g
$$

alone as a complete quantum-capability metric outside the phase-insensitive Gaussian model.

---

# 5. Gaussian thermal noise and non-Gaussian dephasing are different

The scalar noise parameter

$$
m
$$

used throughout the phase-insensitive Gaussian channel model describes the vacuum-output occupation of a Gaussian attenuation/amplification process.

A phase-diffusion channel is generally non-Gaussian.

It cannot, in general, be represented by replacing

$$
m\to m+m_\phi
$$

for one scalar

$$
m_\phi.
$$

Therefore the clean Gaussian condition

$$
\tau>m
$$

must be applied only after confirming that the source/receiver noise model remains within the phase-insensitive Gaussian family.

If appreciable phase diffusion is present, the full channel should be written schematically as

$$
\boxed{
\mathcal A_{\rm full}
=\Phi_{\rm link}
\circ
\mathcal D_{A},}
$$

or with the dephasing placed at its actual dynamical location.

The entanglement-breaking/NPT condition then requires a separate analysis of the composite non-Gaussian channel.

---

# 6. Finite phase diffusion

For a phase distribution

$$
p(\theta),
$$

the Fock-basis matrix elements transform as

$$
\boxed{
|n\rangle\langle m|
\longrightarrow
\varphi_{n-m}
|n\rangle\langle m|,}
$$

where

$$
\boxed{
\varphi_k
=\int d\theta\,p(\theta)e^{-ik\theta}}
$$

is the characteristic function of the phase noise.

For Gaussian phase diffusion with variance

$$
\sigma_\phi^2,
$$

$$
\boxed{
\varphi_k
=e^{-k^2\sigma_\phi^2/2}.}
$$

Thus high-order Fock coherences decay faster than low-order ones even though the phonon-number distribution is unchanged.

The complete-randomization limit has

$$
\varphi_k=\delta_{k0}
$$

and produces the manifestly separable state above.

A finite-noise NPT threshold may depend on

- branch amplitude;
- phase-noise distribution;
- downstream loss/noise;

and is not encoded by

$$
\beta_{g,A}.
$$

---

# 7. Stochastic frequency noise as a temporal-mode problem

A time-dependent source frequency fluctuation

$$
\delta\omega(t)
$$

produces a stochastic phase

$$
\theta(t)
=\int^t ds\,\delta\omega(s).
$$

The source waveform becomes

$$
 f(t)
\to
 f(t)e^{-i\theta(t)}.
$$

Unlike a constant random phase, time-dependent phase noise also reduces temporal overlap with the receiver.

Then

$$
\mathcal T_f(t)
$$

itself becomes stochastic:

$$
\boxed{
\mathcal T_{f,\theta}(t)
=\kappa_B
\left|
\int_0^t ds\,
e^{-\kappa_B(t-s)/2}
f(s)e^{-i\theta(s)}
\right|^2.}
$$

The mean classical loading

$$
\mathbb E[\mathcal T_{f,\theta}]
$$

still does not by itself determine the entanglement of the averaged quantum state.

Therefore frequency noise affects both

1. coherent temporal mode matching;
2. quantum phase coherence.

A rigorous noisy-source treatment must keep both effects.

---

# 8. Narrowband frequency-dependent amplitude loss

The simple branching identity

$$
\beta_{g,A}=\kappa_{g,A}/\kappa_A
$$

also assumes the relevant port ratios are approximately constant across the source bandwidth.

For frequency-dependent linear couplings, a controlled source spectrum

$$
\widetilde\alpha(\Omega)
$$

produces branch-distance weight

$$
\boxed{
N_{\Delta,j}
=4\int\frac{d\Omega}{2\pi}
\kappa_j(\omega_0+\Omega)
|\widetilde\alpha(\Omega)|^2.}
$$

The waveform-weighted gravitational branch fraction becomes

$$
\boxed{
\beta_{g,A}[\alpha]
=\frac{
\int d\Omega\,
\kappa_g(\omega_0+\Omega)
|\widetilde\alpha(\Omega)|^2
}{
\int d\Omega\,
\kappa_{\rm tot}(\omega_0+\Omega)
|\widetilde\alpha(\Omega)|^2
}.}
$$

Only in the narrowband Markov limit does this reduce to

$$
\boxed{
\beta_{g,A}[\alpha]
\simeq
\frac{\kappa_g(\omega_0)}
{\kappa_{\rm tot}(\omega_0)}.}
$$

The V6 controlled hierarchy

$$
\kappa_A,\kappa_B,g,1/T
\ll\omega_0
$$

is precisely the regime in which this simplification is appropriate.

---

# 9. Spectral correction scale for gravitational radiation

For the leading quadrupole channel,

$$
\kappa_g(\omega)
$$

has a steep power-law dependence near the mechanical resonance.

The free-space quadrupole transition formula carries the familiar

$$
\omega^5
$$

spectral factor before the source matrix-element normalization is inserted.

Therefore an envelope with fractional bandwidth

$$
\Delta\omega/\omega_0
$$

can produce non-negligible spectral corrections if driven outside the narrowband regime.

For a source spectrum centered symmetrically about

$$
\omega_0,
$$

the first odd spectral correction to an integrated norm vanishes, leaving a leading correction schematically of order

$$
\boxed{
O\!\left(
\frac{\Delta\omega^2}{\omega_0^2}
\right)}
$$

provided the nongravitational rates are equally smooth.

This is another reason the manuscript should preserve

$$
g\ll\omega_0
$$

and

$$
\kappa_{A,B}\ll\omega_0
$$

rather than advertising arbitrarily short broadband source pulses.

---

# 10. Revised interpretation of the source interface

The source interface should be described by two conceptually distinct objects.

## coherent amplitude branching

$$
\boxed{
\beta_{g,A}}
$$

or its waveform-weighted generalization;

## source coherence/noise channel

$$
\boxed{
\mathcal D_A
}
$$

collecting phase diffusion, stochastic frequency noise, nonlinear dephasing, or other non-amplitude-damping processes.

The clean V6 benchmark sets

$$
\mathcal D_A=I
$$

or includes only Gaussian thermal amplitude-damping noise through

$$
m_A.
$$

This is a model assumption that should be stated explicitly.

---

# 11. Correct link hierarchy beyond the ideal model

The most general schematic architecture is not merely

$$
\beta_{g,A}
\times
\eta_{\rm store}
\times
\beta_{g,B}
\times
\mathcal T_f.
$$

It is

$$
\boxed{
\text{logical source}
\xrightarrow{\ \mathcal D_A\ }
\text{coherent source mode}
\xrightarrow{\beta_{g,A}}
\text{gravitational wavepacket}
\xrightarrow{\eta_{\rm store}}
\text{receiver input}
\xrightarrow{\beta_{g,B},\,\mathcal T_f}
\text{receiver memory}
\xrightarrow{\text{noise/readout}}
\text{accessible output}.}
$$

For the linear coherent/vacuum source model,

$$
\mathcal D_A=I
$$

and the four-factor scalar equation is exact.

For more realistic sources,

$$
\mathcal D_A
$$

can become the dominant limitation even when

$$
\beta_{g,A}
$$

is large.

---

# 12. Manuscript consequence

The V6 main text should include one explicit caveat near the central link equation:

> The factorization below is exact for the coherent-transfer coefficient of the linear narrowband amplitude-damping network. It does not subsume phase diffusion or other non-Gaussian source decoherence. Such processes act as additional source channels and can destroy entanglement even at unit gravitational energy branching; complete phase randomization of a binary coherent branch state is a simple example.

This caveat prevents the benchmark from being mistaken for a universal statement that energy branching alone determines quantum coherence.

---

# 13. Adversarial verdict

The four-factor link budget survives this attack, but its meaning is narrower and clearer.

It is exactly the **coherent-transfer budget** of the linear source→gravity→receiver network.

It is not a complete quantum-capability formula for arbitrary source noise.

The clean counterexample is

$$
\boxed{
\beta_{g,A}=1
\quad+\quad
\text{complete phase diffusion}
\quad\Rightarrow\quad
\rho_{RA}\text{ separable}.}
$$

Therefore future proposals for a high-efficiency gravitational source must demonstrate both

1. strong gravitational branching;
2. preservation of source phase coherence.

For the controlled Gedanken benchmark, the latter is assumed through the coherent/vacuum linear source model and separately bounded thermal/controller corrections.
