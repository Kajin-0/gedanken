# Coherent Source Shaping — What It Can and Cannot Beat

**Date:** 2026-08-08  
**Status:** **CONTROLLED-WAVEFORM RESULT — COHERENT SHAPING CAN REMOVE TEMPORAL MISMATCH BUT CANNOT CHANGE SOURCE BRANCHING**

## 1. Motivation

`PASSIVE_OPTIMIZATION_SCOPE_AND_SPEED_TRADEOFF.md` shows that passive source broadening is fundamentally the wrong cure for a source/receiver linewidth mismatch.

At fixed intrinsic gravitational source rate

$$
\kappa_{g,A},
$$

adding ordinary damping increases

$$
\kappa_A
$$

but reduces the gravitational branching fraction

$$
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A}
$$

faster than the improved temporal matching can compensate.

The natural next question is:

> Can a coherent branch-common controller shape the radiating source trajectory directly, rather than broadening it dissipatively, and thereby obtain a receiver-matched gravitational wavepacket without sacrificing source coherence?

The answer is:

1. **yes** for temporal mode shaping in the ideal linear controlled source;
2. **no** for the source branching ratio;
3. coherent shaping therefore changes only the temporal factor of the end-to-end link unless it also changes the physical port couplings themselves.

---

# 2. General controlled source trajectory

Work in the rotating frame of the finite-spoke source mode.

Let the two reference branches generate mirrored coherent amplitudes

$$
\boxed{
\alpha_s(t)=s\alpha(t),
\qquad s=\pm1.
}
$$

Assume the controller is designed so that

$$
\alpha(0)=\alpha(T)=0,
$$

and the controller/work subsystem is branch common at the beginning and end of the pulse.

This is the closed-loop version of the sign-controlled encoder already used in the repository.

Let the source oscillator couple to independent Markov output ports

$$
j=g,1,2,\ldots
$$

with amplitude-decay contributions

$$
\kappa_j,
$$

where

- \(g\) is the gravitational output port;
- the other \(j\)'s are nongravitational loss channels.

The total source linewidth is

$$
\boxed{
\kappa_A=\sum_j\kappa_j.}
$$

---

# 3. Exact branch-distance partition among output ports

For port \(j\), the branch-dependent output amplitude is

$$
b_{j,s}^{\rm out}(t)
=\text{branch-common input}
+s\sqrt{\kappa_j}\,\alpha(t).
$$

Therefore the difference between the two output coherent histories is

$$
\boxed{
\Delta b_j^{\rm out}(t)
=2\sqrt{\kappa_j}\,\alpha(t).}
$$

The coherent-state distance carried by that entire temporal output is

$$
\boxed{
N_{\Delta,j}
=4\kappa_j
\int_0^Tdt\,|\alpha(t)|^2.}
$$

Summing over all source ports,

$$
\boxed{
N_{\Delta,{\rm tot}}
=4\kappa_A
\int_0^Tdt\,|\alpha(t)|^2.}
$$

Hence the fraction of the emitted branch record that enters gravity is exactly

$$
\boxed{
\frac{N_{\Delta,g}}
{N_{\Delta,{\rm tot}}}
=\frac{\kappa_{g,A}}{\kappa_A}
=\beta_{g,A}.}
$$

This is independent of

- pulse duration;
- pulse shape;
- peak source amplitude;
- controller drive strength.

### Main control no-go

$$
\boxed{
\text{coherent temporal shaping cannot alter the source branching ratio if the physical output couplings }\kappa_j\text{ are unchanged.}
}
$$

Ordinary damping is not rendered harmless by making the pulse shorter: increasing \(|\alpha|^2\) to keep the gravitational output fixed increases every other branch-dependent output in the same proportion.

---

# 4. Normalized gravitational waveform is controllable

The gravitational branch-distance is

$$
N_{\Delta,g}
=4\kappa_{g,A}
\int_0^Tdt\,|\alpha(t)|^2.
$$

Define the normalized gravitational temporal mode

$$
\boxed{
 f_g(t)
=\frac{\alpha(t)}
{\sqrt{\int_0^Tds\,|\alpha(s)|^2}}.
}
$$

Then

$$
\int_0^T|f_g(t)|^2dt=1.
$$

Thus, within the source-mode/RWA model, a coherent controller that can synthesize the complex source amplitude

$$
\alpha(t)
$$

can independently choose

1. the normalized emitted temporal shape \(f_g\);
2. the total gravitational branch distance \(N_{\Delta,g}\), through the overall scale of \(\alpha\).

What it cannot change is the relative branch distance emitted into the other source ports.

---

# 5. Receiver-optimal waveform

For a fixed receiver with total linewidth

$$
\kappa_B
$$

and useful source-mode loading rate

$$
\kappa_\Delta,
$$

the receiver-local coherent transfer at target time \(t\) is

$$
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
e^{-\kappa_B(t-s)/2}f(s)
\right|^2.
$$

For a normalized input mode, Cauchy–Schwarz gives

$$
\boxed{
\tau_f(t)
\le
\frac{\kappa_\Delta}{\kappa_B}
(1-e^{-\kappa_B t}).}
$$

Equality is obtained for the time-reversed receiver impulse response on the chosen interval,

$$
\boxed{
f_t(s)
=\sqrt{
\frac{\kappa_B}
{1-e^{-\kappa_Bt}}
}
e^{-\kappa_B(t-s)/2},
\qquad0<s<t.}
$$

Equivalently, the source amplitude rises exponentially toward the target time.

Define the receiver useful branching fraction

$$
\boxed{
\beta_\Delta
=\frac{\kappa_\Delta}{\kappa_B}
=\eta_{\rm store}\beta_{g,B}.}
$$

Then

$$
\boxed{
\tau_{B}^{\rm env}(t)
=\beta_\Delta
(1-e^{-\kappa_Bt}).}
$$

This is the familiar target-time-optimized envelope, now interpreted as an **actively synthesizable source-mode target** rather than a universal fixed passive waveform.

---

# 6. Source-resolved controlled-waveform ceiling

If the source branch stage is represented by its gravitational branching factor

$$
\beta_{g,A},
$$

then the end-to-end coherent parameter obeys

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}(t)
\le
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
(1-e^{-\kappa_Bt}).}
$$

As

$$
t\to\infty,
$$

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\le
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}.}
$$

Therefore coherent temporal control cannot beat the three multiplicative bottlenecks

1. source gravitational branching;
2. free-space/source-mode overlap;
3. receiver gravitational branching.

It can only optimize the remaining temporal loading factor.

---

# 7. Maximum gain over the matched passive exponential

For the matched passive exponential architecture at fixed branch fractions,

$$
\tau_{A\to B}^{\rm pass,max}
=4e^{-2}
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}.
$$

The asymptotic target-time-optimized controlled envelope is

$$
\tau_{A\to B}^{\rm ctrl,max}
=\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}.
$$

Thus at fixed branching fractions

$$
\boxed{
\frac{
\tau_{A\to B}^{\rm ctrl,max}
}{
\tau_{A\to B}^{\rm pass,max}
}
\le
\frac{e^2}{4}
\simeq1.84726.}
$$

So active waveform engineering is an order-unity improvement **once the branch fractions have already been specified**.

It is not a cure for poor gravitational branching.

---

# 8. Why coherent shaping can nevertheless beat the natural fixed-radiator passive waveform by a huge factor

There is a different comparison that must not be confused with Sec. 7.

Suppose the physical source has essentially no nongravitational loss,

$$
\beta_{g,A}\simeq1,
$$

so its natural passive linewidth is

$$
\kappa_A\simeq\kappa_{g,A}
\ll\kappa_B.
$$

The natural passive source waveform is then badly mismatched to the receiver. Its optimized end-to-end transfer approaches

$$
\tau_{A\to B}^{\rm natural}
\simeq
4\eta_{\rm store}
\frac{\kappa_{g,A}}{\kappa_B}
\beta_{g,B}.
$$

If

$$
\kappa_{g,A}=\kappa_{g,B}
$$

and

$$
\beta_{g,B}\ll1,
$$

$$
\tau_{A\to B}^{\rm natural}
\simeq
4\eta_{\rm store}\beta_{g,B}^2.
$$

A coherent controller can instead keep the source **lossless** while driving a receiver-matched source trajectory. The asymptotic controlled ceiling becomes

$$
\boxed{
\tau_{A\to B}^{\rm ctrl,max}
\simeq
\eta_{\rm store}\beta_{g,B}.}
$$

For identical intrinsic gravitational linewidths the ratio is

$$
\boxed{
\frac{	au^{\rm ctrl,max}}
{\tau^{\rm natural}}
\simeq
\frac1{4\beta_{g,B}}.}
$$

This can be enormous when

$$
\beta_{g,B}\ll1.
$$

There is no contradiction with the branching no-go:

- the source branching remains unity in both cases;
- the controller changes the **source temporal mode without adding dissipative source loss**;
- the improvement comes from eliminating passive source/receiver bandwidth mismatch, not from increasing the gravitational output fraction.

The price is a coherent control resource, quantified next.

---

# 9. Pulse energy–duration cost

Let

$$
\alpha(t)=\alpha_{\rm pk}g(t),
$$

where

$$
\max_t|g(t)|=1
$$

and define

$$
\boxed{
C_g
=\frac1T
\int_0^Tdt\,|g(t)|^2.}
$$

The gravitational branch distance is

$$
N_{\Delta,g}
=4\kappa_{g,A}
|\alpha_{\rm pk}|^2
C_gT.
$$

The peak coherent excitation energy of one source branch is

$$
\boxed{
E_{\rm pk}
=\hbar\omega|\alpha_{\rm pk}|^2
=\frac12M_{\rm eff}\omega^2u_{\rm pk}^2.}
$$

Therefore

$$
\boxed{
E_{\rm pk}T
=
\frac{\hbar\omega}
{4\kappa_{g,A}C_g}
N_{\Delta,g}.}
$$

This is an exact resource relation for a specified pulse shape within the linear Markov/RWA source model.

A shorter coherent gravitational pulse is possible, but the required transient source energy grows as

$$
\boxed{E_{\rm pk}\propto1/T}
$$

for fixed emitted branch distance.

This is not claimed as a universal quantum speed limit; it is the source-energy cost of the present controlled quadrupole architecture.

---

# 10. \(\sin^4\) pulse cost

For

$$
g(t)=\sin^4(\pi t/T),
$$

$$
\boxed{
C_g
=\int_0^1dx\,\sin^8(\pi x)
=\frac{35}{128}.}
$$

Hence

$$
\boxed{
E_{\rm pk}T
=\frac{32}{35}
\frac{\hbar\omega}{\kappa_{g,A}}
N_{\Delta,g}.}
$$

Equivalently, using the finite-spoke displacement amplitude

$$
u_{\rm pk}=u_0,
$$

this reproduces

$$
N_{\Delta,g}
=\frac72
\frac{G\mu^2L^2u_0^2\omega^5T}
{\hbar c^5}
\left(\frac{\tan q}{q}\right)^2.
$$

Thus the previously derived classical quadrupole result is the same active-control energy–duration relation written in mechanical coordinates.

---

# 11. Small-strain lower bound on pulse duration

Suppose the controlled linear-elastic regime requires

$$
\boxed{
|u_{\rm pk}|\le\varepsilon L,
\qquad \varepsilon\ll1.}
$$

Then

$$
|\alpha_{\rm pk}|^2
\le
\frac{\varepsilon^2L^2}
{4u_{\rm zpf}^2}.
$$

For the \(\sin^4\) pulse, solving the finite-spoke \(N_\Delta\) formula gives

$$
\boxed{
T
\ge
\frac{2}{7}
\frac{\hbar c^5}
{G\mu^2L^4\omega^5\varepsilon^2}
\left(\frac q{\tan q}\right)^2
N_{\Delta,g}.}
$$

This is only one source-model bound; the narrowband/RWA condition

$$
\omega T\gg1
$$

and controller bandwidth/energy constraints may be stronger.

The important scaling is that coherent acceleration of the protocol is paid for by increasing source excursion/energy rather than by sacrificing gravitational branching.

---

# 12. Receiver-matched rising exponential energy

For a target time

$$
T
$$

choose the Cauchy-saturating source shape

$$
g(t)=e^{-\kappa_B(T-t)/2},
\qquad0<t<T,
$$

normalized here to unit peak amplitude rather than unit mode norm.

Then

$$
\int_0^Tdt\,|g(t)|^2
=\frac{1-e^{-\kappa_BT}}
{\kappa_B}.
$$

For a desired gravitational branch distance,

$$
\boxed{
E_{\rm pk}
=
\frac{\hbar\omega N_{\Delta,g}}{4}
\frac{\kappa_B}
{\kappa_{g,A}}
\frac1{1-e^{-\kappa_BT}}.}
$$

For

$$
\kappa_BT\gg1,
$$

$$
\boxed{
E_{\rm pk}
\to
\frac{\hbar\omega N_{\Delta,g}}{4}
\frac{\kappa_B}{\kappa_{g,A}}.}
$$

Thus receiver matching can be obtained without dissipative source broadening, but the coherent source occupation required to radiate a fixed branch distance is enhanced by the bandwidth ratio

$$
\kappa_B/\kappa_{g,A}.
$$

---

# 13. Aggressive benchmark implication

For the historical kilogram–meter–MHz receiver benchmark,

$$
\beta_{g,B}
\simeq1.09\times10^{-20},
$$

and at

$$
kR=10,
\qquad
\mathcal O=1,
$$

$$
\eta_{\rm store}=1.5625\times10^{-2}.
$$

If a hypothetical source can be made nearly purely gravitational,

$$
\beta_{g,A}\simeq1,
$$

while a coherent controller synthesizes the receiver-optimal temporal mode, then the asymptotic link ceiling is

$$
\boxed{
\tau_{A\to B}^{\rm ctrl,max}
\simeq
\eta_{\rm store}\beta_{g,B}
\simeq1.71\times10^{-22}.}
$$

This is back at the old **receiver-local** scale rather than the

$$
10^{-42}
$$

passive source-resolved scale.

But the assumption

$$
\beta_{g,A}\simeq1
$$

is itself extraordinarily demanding for an ordinary mechanical radiator. If the source has the same

$$
\beta_{g,A}\sim10^{-20}
$$

as the receiver, the controlled ceiling is again

$$
\sim10^{-42}.
$$

Therefore coherent control can cure temporal mismatch; it cannot cure a lossy gravitational source.

---

# 14. Consequence for the paper

The source/receiver story should now be stated in three layers.

## Passive dissipative source

Dissipative broadening never improves end-to-end transfer at fixed intrinsic gravitational source rate.

## Closed coherent source controller

Temporal mode shape can be changed without introducing the **additional** branching loss that dissipative broadening would create.

## Irreducible physical bottlenecks

Even with ideal temporal shaping,

$$
\boxed{
\tau_{A\to B}
\le
\beta_{g,A}\eta_{\rm store}\beta_{g,B}
}
$$

for the present passive receiver/capture architecture.

Thus the deepest bottlenecks are not the \(4e^{-2}\) waveform coefficient. They are

1. source gravitational branching;
2. receiver gravitational branching;
3. geometric/mode capture.

The temporal coefficient is secondary.

---

# 15. Adversarial verdict

Coherent waveform engineering is a real resource, but its power is sharply limited.

It can:

- synthesize a receiver-matched gravitational temporal mode;
- avoid adding dissipative source broadening solely for waveform matching;
- shorten a closed source trajectory at an energy/excursion cost;
- remove the order-unity \(4e^{-2}\) passive temporal penalty.

It cannot:

- change \(\kappa_{g,A}/\kappa_A\) if the physical output couplings are unchanged;
- prevent ordinary loss ports from acquiring branch information;
- change the wave-zone mode-overlap factor;
- change the receiver gravitational branching fraction;
- make the end-to-end channel strong when both physical devices have tiny gravitational branching.

The clean controlled-waveform ceiling is

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}(t)
\le
\beta_{g,A}\eta_{\rm store}\beta_{g,B}
(1-e^{-\kappa_Bt}).}
$$

That should replace vague claims that active source shaping can evade the end-to-end gravitational weakness.
