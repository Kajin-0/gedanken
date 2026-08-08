# Reciprocal Receiver Backaction / One-Way Cascade Audit

**Date:** 2026-08-07  
**Status:** **ONE-WAY CASCADE JUSTIFIED AS LEADING WAVE-ZONE TERM — RECIPROCAL FEEDBACK ENTERS THROUGH A ROUND-TRIP LOOP OF ORDER $\eta_{\rm store}$ AND CHANGES ABSOLUTE FORWARD TRANSFER ONLY AT $O(\eta_{\rm store}^2)$**

## 1. Purpose

The source→receiver calculations are often written as a one-way cascade:

$$
\text{source output}
\longrightarrow
\text{retarded free-space field}
\longrightarrow
\text{receiver input}.
$$

But the gravitational Green function is reciprocal. Once receiver $B$ is driven by source $A$, $B$ also radiates back toward $A$, which can then re-radiate toward $B$.

A referee can therefore ask whether the source waveform used in the one-way channel has been altered by receiver backaction strongly enough to invalidate the cascade factorization.

The answer in the intended wave-zone weak-link regime is no.

The exact linear two-mode response is a geometric feedback series. One round trip contains **two** source–receiver propagation amplitudes, so the loop gain is proportional to

$$
\eta_{\rm store}=|t_{AB}^{\rm store}|^2.
$$

Consequently

- the relative correction to the forward **amplitude** is $O(\eta_{\rm store})$;
- the absolute correction to a forward transfer **probability** that is itself $O(\eta_{\rm store})$ is $O(\eta_{\rm store}^2)$.

---

# 2. Reciprocal delayed equations

Work with slowly varying source and receiver amplitudes around carrier frequency $\omega_0$.

Let

$$
T\equiv R/c.
$$

The reciprocal linearized/RWA equations are

$$
\boxed{
\dot a_A(t)
=-\frac{\kappa_A}{2}a_A(t)
-i\Sigma_{AB}^{R}a_B(t-T)
+F_A(t),
}
$$

$$
\boxed{
\dot a_B(t)
=-\frac{\kappa_B}{2}a_B(t)
-i\Sigma_{BA}^{R}a_A(t-T)
+F_B(t).
}
$$

Here

- $\kappa_A$ and $\kappa_B$ are total local linewidths;
- $F_A,F_B$ collect local input/noise terms;
- the carrier propagation phase is already contained in $\Sigma_{AB}^{R}$ and $\Sigma_{BA}^{R}$;
- the explicit delay acts on envelope detuning frequencies.

For reciprocal aligned quadrupoles,

$$
\Sigma_{AB}^{R}=\Sigma_{BA}^{R}
$$

up to the chosen transpose/phase convention, and in any case

$$
|\Sigma_{AB}^{R}|=|\Sigma_{BA}^{R}|.
$$

---

# 3. Frequency-domain solution

Let $\nu$ denote detuning from the carrier and define local susceptibilities

$$
\boxed{
\chi_j(\nu)
=\frac{1}{\kappa_j/2-i\nu}.
}
$$

The receiver equation gives

$$
a_B
=\chi_B
\left[
F_B
-i\Sigma_{BA}^{R}e^{i\nu T}a_A
\right].
$$

Substituting into the source equation gives

$$
a_A
=\chi_A
\left[
F_A
-i\Sigma_{AB}^{R}e^{i\nu T}\chi_BF_B
-
\Sigma_{AB}^{R}\Sigma_{BA}^{R}
\chi_Be^{2i\nu T}a_A
\right].
$$

Define the round-trip loop gain

$$
\boxed{
L(\nu)
=\Sigma_{AB}^{R}\Sigma_{BA}^{R}
\chi_A(\nu)\chi_B(\nu)
e^{2i\nu T}.
}
$$

Then

$$
\boxed{
a_A(\nu)
=
\frac{\chi_A(\nu)}{1+L(\nu)}
\left[
F_A
-i\Sigma_{AB}^{R}e^{i\nu T}\chi_BF_B
\right].
}
$$

The source-input contribution to the receiver is

$$
\boxed{
G_{BA}(\nu)
=
\frac{
-i\Sigma_{BA}^{R}e^{i\nu T}
\chi_A(\nu)\chi_B(\nu)
}{1+L(\nu)}.
}
$$

The one-way/Born result is simply

$$
\boxed{
G_{BA}^{(1)}(\nu)
=
-i\Sigma_{BA}^{R}e^{i\nu T}
\chi_A(\nu)\chi_B(\nu).
}
$$

Therefore

$$
\boxed{
\frac{G_{BA}}{G_{BA}^{(1)}}
=\frac1{1+L}.
}
$$

The cascade approximation is the first term of an exact multiple-scattering series.

---

# 4. Relation to the audited storage coefficient

`DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md` gives

$$
\boxed{
t_{BA}^{\rm store}
=
\frac{-i\Sigma_{BA}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}.
}
$$

Hence

$$
\boxed{
|\Sigma_{BA}^{R}|^2
=
\kappa_{g,A}\kappa_{g,B}
\eta_{\rm store}.
}
$$

Define the gravitational branching fractions

$$
\boxed{
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A},
\qquad
\beta_{g,B}=\frac{\kappa_{g,B}}{\kappa_B}.
}
$$

Since

$$
|\chi_j(\nu)|
\le\frac2{\kappa_j},
$$

we obtain the uniform narrowband bound

$$
\boxed{
|L(\nu)|
\le
4\eta_{\rm store}
\beta_{g,A}\beta_{g,B}.
}
$$

Define

$$
\boxed{
\ell
\equiv
4\eta_{\rm store}
\beta_{g,A}\beta_{g,B}.
}
$$

Then

$$
|L(\nu)|\le\ell.
$$

---

# 5. Wave-zone bound

At leading compact-source aligned wave-zone order,

$$
\eta_{\rm store}
=
\frac{25\mathcal O}{16(kR)^2}.
$$

Therefore

$$
\boxed{
\ell
=
\frac{25\mathcal O}{4(kR)^2}
\beta_{g,A}\beta_{g,B}.
}
$$

Since

$$
0\le\mathcal O,\beta_{g,A},\beta_{g,B}\le1,
$$

$$
\boxed{
\ell
\le
\frac{25}{4(kR)^2}.
}
$$

Thus the weak-feedback condition

$$
\ell<1
$$

is automatically satisfied deep in the wave zone.

For example, even the maximally coupled ideal case gives

$$
\ell\le0.0625
$$

at

$$
kR=10.
$$

The actual gravitational Gedanken links are normally much weaker because the branching fractions are far below unity for ordinary matter.

---

# 6. Rigorous transfer-amplitude error bound

If

$$
\ell<1,
$$

then

$$
|1+L|\ge1-|L|\ge1-\ell.
$$

Therefore

$$
\boxed{
\left|
\frac{G_{BA}-G_{BA}^{(1)}}
{G_{BA}^{(1)}}
\right|
=
\left|
\frac{-L}{1+L}
\right|
\le
\frac{\ell}{1-\ell}.
}
$$

So the relative coherent-transfer amplitude error is controlled directly by the round-trip loop gain.

---

# 7. Transfer-probability bound

The exact/one-way spectral transfer ratio is

$$
\boxed{
\frac{|G_{BA}|^2}
{|G_{BA}^{(1)}|^2}
=
\frac1{|1+L|^2}.
}
$$

For

$$
|L|\le\ell<1,
$$

$$
\boxed{
\frac1{(1+\ell)^2}
\le
\frac{|G_{BA}|^2}
{|G_{BA}^{(1)}|^2}
\le
\frac1{(1-\ell)^2}.
}
$$

The loop phase can therefore either enhance or suppress the transfer slightly.

For small $\ell$,

$$
\frac{|G_{BA}|^2}
{|G_{BA}^{(1)}|^2}
=1-2\operatorname{Re}L+O(\ell^2).
$$

Because the one-way forward transfer probability is already

$$
O(\eta_{\rm store}),
$$

and

$$
\ell=O(\eta_{\rm store}),
$$

the **absolute** feedback correction is

$$
\boxed{
\delta\tau_{A\to B}
=O(\eta_{\rm store}^2).
}
$$

In the wave zone this is

$$
\boxed{
O((kR)^{-4}).
}
$$

Thus the leading

$$
1/(kR)^2
$$

source→receiver transmissivity is unaffected by reciprocal rescattering.

---

# 8. Relation to the optimal passive link

`OPTIMAL_PASSIVE_LINEWIDTH_MATCHING.md` gives the best one-way constant-coupling exponential-link transmissivity

$$
\boxed{
\tau_{\rm passive}^{\max}
=4e^{-2}
\eta_{\rm store}
\beta_{g,A}\beta_{g,B}.
}
$$

Therefore

$$
\boxed{
\ell
=e^2\tau_{\rm passive}^{\max}.
}
$$

This provides a compact self-consistency relation:

> whenever the passive gravitational link transmissivity is perturbatively small, its neglected reciprocal feedback loop is perturbatively small as well.

---

# 9. Time-domain path counting

The delay structure gives a stronger causal statement for the source-controlled signal response.

Let the localized source preparation begin at

$$
t=0.
$$

The direct path is

$$
A\to B,
$$

so the first source-controlled receiver signal can arrive at

$$
\boxed{t=T=R/c.}
$$

The first feedback correction requires the path

$$
A\to B\to A\to B.
$$

Its earliest arrival is therefore

$$
\boxed{t=3T=3R/c.}
$$

Hence the source-input contribution to the receiver is **exactly one-way** in the interval

$$
\boxed{
R/c<t<3R/c
}
$$

within the delayed linear model.

This statement concerns dependence on the source input. Branch-independent receiver/environment fluctuations can have their own round-trip echoes, but they do not create an earlier source-input signal in a linear system.

---

# 10. Receiver-noise feedback

The coherent signal is not the only quantity affected by reciprocity.

Receiver bath fluctuations can radiate toward the source and return to the receiver after a round trip

$$
B\to A\to B,
$$

whose earliest delay is

$$
2R/c.
$$

Therefore the simple local expression

$$
m_B(t)
$$

is also a leading one-way/Born description once times long enough for round-trip noise feedback are included.

However:

1. the full source+receiver+field problem remains a **linear Gaussian passive network** at the retained order;
2. vacuum input ports remain vacuum under the exact passive network;
3. thermal-noise transfer functions acquire the same feedback denominator structure;
4. their relative corrections are controlled by the same small loop gain $\ell$ in the stable wave-zone regime.

Thus reciprocal backaction does not invalidate Gaussianity or introduce an uncontrolled new noise mechanism. It produces a controlled $O(\ell)$ correction to the one-way thermal/noise parameters.

A fully exact thermal delayed-channel covariance can be derived if needed for a submission-level error bar.

---

# 11. Small-gain stability criterion

The reciprocal delayed network can exhibit strong delay-dependent collective resonances only when repeated round trips are not perturbative.

The present wave-zone regime has the uniform bound

$$
\sup_\nu|L(\nu)|\le\ell.
$$

If

$$
\boxed{\ell<1,}
$$

the geometric multiple-scattering series converges uniformly in the narrowband model:

$$
\frac1{1+L}
=1-L+L^2-\cdots.
$$

This is the natural passive small-gain condition for the source–receiver feedback loop.

Time-delayed coherent-feedback systems outside this regime can show non-Markovian collective resonances and must be treated as a genuine bidirectional network rather than a cascade.

That is not the parameter regime of the current wave-zone Gedanken link.

---

# 12. Near-zone warning

The argument above uses the propagating wave-zone interpretation of

$$
\eta_{\rm store}.
$$

Near-zone reactive coupling is contained in the full retarded self-energy

$$
\Sigma_{AB}^{R},
$$

but should not be interpreted as a pure-loss free-space transmission coefficient.

If

$$
kR\sim1
$$

or smaller, the exact reciprocal two-oscillator Green-function problem should be retained from the start.

The one-way storage-channel picture is intended for

$$
\boxed{kR\gg1.}
$$

---

# 13. Consequence for the NPT capability condition

The leading one-way local-preparation result is

$$
\boxed{
\eta_g\tau_{\rm full}(t)>m_B(t).
}
$$

Reciprocal rescattering changes both the coherent transfer and, at finite thermal occupation, the effective noise only at controlled relative order

$$
O(\ell).
$$

Therefore the exact bidirectional condition can be written schematically as

$$
\boxed{
\eta_g\tau_{\rm full}(t)
[1+O(\ell)]
>
m_B(t)[1+O(\ell)]
}
$$

in the stable wave-zone weak-link regime.

The leading one-way EB/NPT boundary is therefore asymptotically controlled, not an uncontrolled cascade assumption.

---

# 14. Relation to standard delayed quantum networks

Time-delayed reciprocal coupling and coherent feedback are standard sources of non-Markovian dynamics in waveguide/cavity QED. Exact treatments resum repeated propagation paths and recover precisely the kind of delay-loop structure used above.

Representative primary literature includes

- S. Arranz Regidor, G. Crowder, H. Carmichael, and S. Hughes, *Phys. Rev. Research* **3**, 023030 (2021), on waveguide-QED retardation and time-delayed feedback;
- P.-O. Guimond, M. Pletyukhov, H. Pichler, and P. Zoller, arXiv:1706.07844, on delayed coherent quantum feedback and scattering resummation;
- H. Pichler and collaborators, *Phys. Rev. X* **14**, 031043 (2024), on continuous coherent quantum feedback with time delays.

Those works supply general delayed-network context. The gravitational loop-gain normalization above follows from the repository's specific audited quadrupole self-energy and storage coefficient.

---

# 15. Adversarial verdict

The one-way gravitational source→receiver cascade survives the reciprocity attack in its intended domain.

The exact reciprocal response differs by the feedback factor

$$
\boxed{
\frac1{1+L(\nu)},
}
$$

with

$$
\boxed{
|L(\nu)|
\le
4\eta_{\rm store}
\beta_{g,A}\beta_{g,B}.
}
$$

In the aligned compact-source wave zone,

$$
\boxed{
|L|
\le
\frac{25\mathcal O}{4(kR)^2}
\beta_{g,A}\beta_{g,B}.
}
$$

Therefore

- first reciprocal source backaction is a round-trip $O((kR)^{-2})$ amplitude correction;
- the leading $O((kR)^{-2})$ forward transfer probability changes only at absolute $O((kR)^{-4})$;
- the direct source-controlled receiver signal is exactly one-way before the first $3R/c$ feedback echo;
- full delayed dynamics remain Gaussian and can be retained if one deliberately leaves the weak-link regime.

The cascade model is therefore a controlled leading-order approximation rather than an assumption of fundamental gravitational directionality.
