# Active Receiver: Quantum-Limited Amplification Does Not Give Free Entanglement Gain

**Timestamp:** 2026-08-07 16:03 EDT  
**Status:** Active derivation for Experiment 01

This note tests the active-receiver loophole suggested by collective states with gravitational transition rates beyond the passive quadrupole sum-rule ceiling. The simplest favorable model is a phase-insensitive **quantum-limited amplifier**.

---

## 1. First distinction: amplification after capture cannot increase entanglement

Suppose the gravitational interaction first produces a source-receiver state $\rho_{AB}$ and an active device then performs a local deterministic channel $\mathcal A_B$ on the receiver:

$$
\rho_{AB}'
=(I_A\otimes\mathcal A_B)(\rho_{AB}).
$$

Any bona fide entanglement monotone cannot increase under such a local CPTP operation.

Therefore:

> **Post-capture amplification may improve readout or classical signal-to-noise, but it cannot increase the amount of source-receiver entanglement that gravity already transferred.**

Any genuine improvement of the transfer rate must therefore come from active physics **during the gravitational coupling itself**, not from local amplification applied after the fact.

---

## 2. Favorable active-channel toy model

Model active enhancement as a quantum-limited phase-insensitive amplifier of power gain $G\ge1$ acting on the incoming gravitational difference mode, followed by coherent collection with efficiency $\eta$.

The quantum-limited amplifier transformation can be written

$$
a_1
=\sqrt G\,a_{\rm in}
+\sqrt{G-1}\,v^\dagger,
$$

where $v$ is an ancillary vacuum mode.

The collection stage is

$$
a_B
=\sqrt\eta\,a_1
+\sqrt{1-\eta}\,w,
$$

with vacuum $w$.

Thus the total phase-insensitive Gaussian channel has amplitude parameter

$$
\boxed{\tau=\eta G}
$$

and, for vacuum input, output thermal occupation

$$
\boxed{m=\eta(G-1)}.
$$

The branch-dependent coherent amplitude is enlarged by

$$
\sqrt{\eta G}.
$$

So the **classical response** can be made large by increasing $G$.

---

## 3. Gaussian-channel distance from the entanglement-breaking boundary

For a phase-insensitive one-mode Gaussian channel written in quadrature form

$$
V_{\rm out}=\tau V_{\rm in}+yI,
$$

the entanglement-breaking boundary is

$$
y\ge\frac{1+\tau}{2}
$$

in the convention where vacuum covariance is $I/2$.

For amplifier followed by pure collection loss,

$$
y
=\frac12\left[\eta(G-1)+(1-\eta)\right]
=\frac{1+\tau-2\eta}{2}.
$$

Hence

$$
\boxed{
\frac{1+\tau}{2}-y=\eta.
}
$$

So for every nonzero collection efficiency $\eta>0$, a **quantum-limited** active channel remains non-entanglement-breaking for every finite gain.

But the absolute gap to the entanglement-breaking noise boundary is fixed by the tiny bare collection efficiency, not by the gain.

As $G\to\infty$,

$$
\tau\to\infty,
\qquad
y\sim\tau/2,
$$

so the channel becomes arbitrarily close *relatively* to the entanglement-breaking boundary even while its classical amplitude gain diverges.

---

## 4. Weak-cat NPT law for a general phase-insensitive channel

Any gauge-covariant phase-insensitive channel can be parameterized by

- coherent amplitude factor $\sqrt\tau$;
- output thermal occupation $m$ for vacuum input.

Its entanglement-breaking boundary is simply

$$
\boxed{\tau=m.}
$$

For the weak source cat

$$
|\Psi\rangle
=|+\rangle|0\rangle+a|-\rangle|1\rangle+O(a^2),
\qquad N_\Delta=4|a|^2,
$$

the same Fock-block calculation used for the thermal attenuator gives, for $m>0$,

$$
\boxed{
\mathcal N_{AB}
=\frac{N_\Delta}{4}
\frac{\tau-m}{m}
+O(N_\Delta^2).
}
$$

Thus only the channel's distance above the entanglement-breaking line matters at leading weak-cat order.

---

## 5. Apply the law to quantum-limited active enhancement

For the active channel,

$$
\tau=\eta G,
$$

$$
m=\eta(G-1).
$$

Therefore

$$
\tau-m=\eta.
$$

For $G>1$ and finite $m$,

$$
\boxed{
\mathcal N_{AB}
=\frac{N_\Delta}{4(G-1)}
+O(N_\Delta^2).
}
$$

The striking feature is that the large classical amplification factor has disappeared from the numerator.

Increasing $G$ makes the classical branch signal larger,

$$
|\Delta\alpha_B|^2
=\eta G N_\Delta,
$$

but simultaneously creates the quantum-limited spontaneous noise

$$
m=\eta(G-1).
$$

At large gain,

$$
\boxed{
\mathcal N_{AB}\propto G^{-1}.
}
$$

So high gain drives the weak-cat source-receiver entanglement **down**, not up.

---

## 6. The apparent $\eta$ cancellation and its meaning

The expression

$$
\mathcal N\simeq N_\Delta/[4(G-1)]
$$

is obtained for fixed nonzero output thermal occupation and is nonuniform in the joint limit

$$
\eta\to0,
\qquad G\to1.
$$

It must not be interpreted as saying an arbitrarily disconnected receiver can acquire finite entanglement.

A useful scaling is to choose gain large enough to produce an order-unity classical amplitude transfer,

$$
\tau=\eta G=O(1).
$$

Then

$$
G\sim\eta^{-1},
$$

and the weak-cat negativity scales as

$$
\boxed{
\mathcal N_{AB}
\sim\frac{N_\Delta}{4}\eta.
}
$$

Thus using active gain to compensate a tiny gravitational collection efficiency restores the same small parameter $\eta$ in the quantum entanglement transfer.

The active channel can hide weak coupling from a classical amplitude measurement, but not from quantum-information bookkeeping.

---

## 7. Amplifier after loss is even less favorable

If the order is reversed—first weak gravitational capture with efficiency $\eta$, then a quantum-limited amplifier of gain $G$ applied locally to the receiver—the amplification is a local channel performed after the entanglement was transferred.

It therefore cannot increase any proper source-receiver entanglement monotone.

At sufficiently large gain the composed Gaussian channel can even become entanglement-breaking, illustrating that aggressive post-amplification can destroy the quantum correlation while improving classical readout.

---

## 8. Relation to $N^2$ collective gravitational rates

Known correlated-atom proposals can exhibit $N^2$ gravitational decay/excitation rates in selected states. Such enhancement is a genuine modification of the matter-gravity coupling dynamics and should not be equated literally with the amplifier toy model above.

However, the toy model establishes an important warning:

> **An enhanced transition rate or amplified receiver signal is not sufficient to establish an enhanced entanglement-transfer rate.**

If the enhancement is supplied by an active quantum medium, the spontaneous fluctuations associated with that active resource must be included in the source-receiver channel.

The relevant quantity is not the raw rate alone but the channel's distance from its entanglement-breaking boundary.

---

## 9. New receiver figure of merit

For a general active phase-insensitive receiver channel, define

$$
\boxed{
\Delta_{\rm EB}
\equiv
\tau-m.
}
$$

In the weak-cat regime,

$$
\boxed{
\mathcal N_{AB}
\simeq
\frac{N_\Delta}{4}
\frac{\Delta_{\rm EB}}{m}.
}
$$

A large classical gain $\tau$ is useful only if it also increases

$$
\Delta_{\rm EB},
$$

rather than increasing signal and spontaneous noise together.

For the ideal amplifier-plus-loss construction,

$$
\boxed{\Delta_{\rm EB}=\eta,}
$$

so the active gain does not increase this fundamental quantum margin at all.

---

## 10. Einstein/Feynman interpretation

> **An active receiver can shout the gravitational signal louder, but quantum mechanics makes the amplifier shout some noise at the same time. If the gain simply enlarges both the branch signal and the unavoidable spontaneous fluctuations, it has not made the gravitational channel more quantum. The relevant question is how far the complete channel lies from becoming a measure-and-prepare channel, not how large the output displacement looks.**

---

## 11. Literature boundary

Quantum-limited phase-insensitive amplification and its minimum added noise are established quantum-optics results, as are the entanglement-breaking conditions for bosonic Gaussian channels. Quantum-limited attenuator and amplifier channels are known not to be entanglement-breaking for finite parameters.

No novelty is claimed for this Gaussian-channel mathematics.

The gravity-specific lesson is its application to the active-receiver loophole opened by collective gravitational transition enhancement: **classical transition-rate enhancement must not be conflated with quantum branch-information transfer enhancement.**

---

## 12. Immediate next step

The amplifier toy model suggests the correct quantity to compute for an actual active collective gravitational receiver:

1. derive both its enhanced coherent gravitational susceptibility and its spontaneous quantum-noise kernel;
2. construct the effective source-receiver channel;
3. determine whether the distance to the entanglement-breaking boundary grows with $N$, stays fixed, or shrinks.

This is the decisive test of whether $N^2$ active collective enhancement is a real escape route for the Gedankenexperiment.