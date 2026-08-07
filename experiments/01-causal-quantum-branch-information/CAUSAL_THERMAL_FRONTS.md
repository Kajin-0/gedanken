# Causal Thermal Entanglement Fronts

**Timestamp:** 2026-08-07 15:32 EDT  
**Status:** Active derivation for Experiment 01

This note turns the thermal channel thresholds into explicit spacetime onset times for a finite gravitational wavepacket.

---

## 1. Time-dependent coherent capture

Let the branch-dependent gravitational difference mode have normalized temporal envelope

$$
f(t),
\qquad
\int_{-\infty}^{\infty}dt\,|f(t)|^2=1.
$$

Let the receiver's eventual coherent capture efficiency be

$$
\eta_\infty.
$$

For a source operation whose earliest influence reaches the receiver at $R/c$, define the cumulative captured mode fraction

$$
\boxed{
\eta(T,R)
=\eta_\infty
F(T-R/c),
}
$$

where

$$
F(s)=\int_{-\infty}^{s}dt\,|f(t)|^2.
$$

Thus

$$
\eta(T,R)=0
$$

before the wavepacket support reaches the receiver.

---

## 2. Three distinct onset times

At finite thermal occupation $\bar n$, three logically different fronts appear.

### Classical signal front

The earliest source-controlled receiver response begins at

$$
\boxed{T_c=R/c}
$$

for an ideal wavepacket with support beginning at the causal front.

### Fundamental entanglement front

The thermal attenuator ceases to be entanglement-breaking once

$$
\eta(T,R)>
\eta_{\rm ent}
=\frac{\bar n}{\bar n+1}.
$$

Therefore, provided

$$
\eta_\infty>\eta_{\rm ent},
$$

the weak-cat source-receiver state becomes NPT at

$$
\boxed{
T_{\rm NPT}(R)
=\frac{R}{c}
+F^{-1}\!\left(
\frac{\eta_{\rm ent}}{\eta_\infty}
\right).
}
$$

If

$$
\eta_\infty\le\eta_{\rm ent},
$$

then no weak-cat NPT front ever occurs.

### Low-cost fidelity-history front

The stronger fidelity witness requires

$$
\eta(T,R)>
\eta_F
=\frac{2\bar n+1}{2\bar n+2}.
$$

If $\eta_\infty>\eta_F$,

$$
\boxed{
T_F(R)
=\frac{R}{c}
+F^{-1}\!\left(
\frac{\eta_F}{\eta_\infty}
\right).
}
$$

Otherwise the source and receiver may become entangled without this simple history witness ever turning positive.

---

## 3. Front hierarchy

Whenever all three exist,

$$
\boxed{
T_c\le T_{\rm NPT}<T_F.
}
$$

At zero temperature,

$$
\eta_{\rm ent}=0,
$$

so the entanglement front begins with the first nonzero coherent capture after causal arrival.

At finite temperature,

$$
\eta_{\rm ent}>0,
$$

and the receiver must first accumulate a finite fraction of the gravitational difference mode before source-receiver entanglement can survive the thermal channel.

Thus temperature creates a genuine **post-light-cone entanglement delay**.

---

## 4. Example: causal exponential wavepacket

Take

$$
f(s)=\sqrt\gamma\,e^{-\gamma s/2}\Theta(s),
$$

so

$$
F(s)=
\begin{cases}
0,&s<0,\\
1-e^{-\gamma s},&s\ge0.
\end{cases}
$$

Then

$$
\boxed{
T_{\rm NPT}
=\frac{R}{c}
-\frac1\gamma
\ln\left(
1-\frac{\eta_{\rm ent}}{\eta_\infty}
\right)
}
$$

when $\eta_\infty>\eta_{\rm ent}$.

Similarly,

$$
\boxed{
T_F
=\frac{R}{c}
-\frac1\gamma
\ln\left(
1-\frac{\eta_F}{\eta_\infty}
\right)
}
$$

when $\eta_\infty>\eta_F$.

---

## 5. Near-threshold delay divergence

If

$$
\eta_\infty
=\eta_{\rm ent}+\delta,
\qquad
0<\delta\ll\eta_{\rm ent},
$$

then for the exponential wavepacket

$$
T_{\rm NPT}-R/c
\sim
\frac1\gamma
\ln\left(\frac{\eta_{\rm ent}}{\delta}\right).
$$

Thus as the eventual receiver efficiency approaches the entanglement-breaking boundary from above, the entanglement front can be delayed arbitrarily far behind the classical light-cone arrival even though the gravitational signal itself is already present.

This is a useful conceptual distinction:

> **causal influence can arrive before enough coherent quantum information has accumulated to survive thermal classicalization.**

---

## 6. Matched-memory condition

For

$$
\eta_\infty
=\frac{\kappa_g}{\kappa_g+\kappa_i},
$$

the NPT front exists iff

$$
\boxed{
\kappa_g>\bar n_i\kappa_i.
}
$$

The fidelity-history front exists only if

$$
\boxed{
\kappa_g>(2\bar n_i+1)\kappa_i.
}
$$

Therefore the receiver can lie in one of three dynamical regimes:

1. **classicalized:** no NPT front;
2. **quantum but hard to certify:** NPT front exists, fidelity front does not;
3. **strong-history regime:** both fronts exist.

---

## 7. Minimal PPT front

The low-cost Fock-sector witness from `LOW_COST_PPT_WITNESS.md` reaches the same weak-cat threshold as exact NPT:

$$
|Z_0(T)|^2>P_{+,1}(T)P_{-,0}(T).
$$

Thus, in the weak-cat limit, an experimentally targeted principal-minor measurement can locate

$$
T_{\rm NPT}(R)
$$

without full state tomography.

This gives a direct operational definition of the **causal entanglement front**.

---

## 8. Current Einstein/Feynman statement

> **The light cone tells us when the first gravitational influence can arrive. Temperature asks a second question: has enough of the coherent branch-dependent wave arrived to survive the receiver's thermal noise? Those are not the same time. A warm receiver can see a perfectly causal gravitational signal while the corresponding quantum channel is still entanglement-breaking. Only after a sufficient fraction of the branch-difference mode has been coherently captured does the receiver cross into the quantum regime. Thus the Gedanken experiment predicts a hierarchy of fronts: signal arrival, entanglement arrival, and simple-witness certification.**

---

## 9. Immediate next step

The next step is to derive the same front structure from the explicit Markovian input-output equations of the matched receiver, including the time dependence of the thermal mode and the source-receiver coherence, rather than inserting a phenomenological $\eta(T)$.