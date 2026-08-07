# Finite-Cat Thermal Channel — Numerical Evidence

**Timestamp:** 2026-08-07 16:21 EDT  
**Status:** Exploratory numerical result; not an analytic theorem

A reproducible truncation-based scan is in

`numerics/thermal_cat_scan.py`.

---

## 1. Question

The weak-cat analysis proves that a thermal attenuator transfers source-receiver entanglement when

$$
\eta>\eta_{\rm EB}
=\frac{\bar n}{\bar n+1}
$$

for infinitesimal branch separation.

The unresolved question is whether a finite coherent branch separation

$$
N_\Delta=4|a|^2
$$

can become separable again at a finite value even though the channel itself is non-entanglement-breaking.

---

## 2. Numerical construction

The thermal attenuator is implemented explicitly by

1. preparing the environment in a thermal Fock-state mixture;
2. mixing signal and environment through a beam-splitter unitary of transmissivity $\eta$;
3. tracing the environment;
4. constructing

$$
\frac{|L\rangle|+a\rangle+|R\rangle|-a\rangle}{\sqrt2}
$$

and applying the channel to the bosonic mode;
5. partially transposing the source qubit and summing negative eigenvalues.

Fock cutoffs of 24--28 were used in the first scan, with output traces checked numerically.

---

## 3. Parameter scan

Initial cases checked:

$$
\bar n=0.1,\ 0.5,\ 1.0,
$$

with transmissivities

- slightly below $\eta_{\rm EB}$;
- approximately $5\%$ above $\eta_{\rm EB}$;
- moderately above threshold;
- $\eta=0.8$.

Branch separations scanned:

$$
N_\Delta
=0.01,0.05,0.1,0.2,0.5,1,2,4,8.
$$

---

## 4. Numerical pattern

### Below the entanglement-breaking boundary

For

$$
\eta<\frac{\bar n}{\bar n+1},
$$

the computed negativity remained zero to numerical/truncation precision throughout the scanned branch separations.

### Above the boundary

For

$$
\eta>\frac{\bar n}{\bar n+1},
$$

the negativity was positive for every finite $N_\Delta$ tested.

The qualitative shape was always

$$
\boxed{
\text{small cat}
\to
\text{growing entanglement}
\to
\text{finite optimum}
\to
\text{decay toward zero for a very large cat}.
}
$$

Thus finite branch amplitude does not monotonically help. A very large branch-dependent field again leaves a highly distinguishable environmental record.

---

## 5. Example near threshold

For

$$
\bar n=0.5,
\qquad
\eta_{\rm EB}=1/3,
$$

and

$$
\eta=0.35,
$$

only slightly above threshold, the first scan gave approximately

$$
\begin{array}{c|c}
N_\Delta & \mathcal N_{AB}\\
\hline
0.01 & 1.90\times10^{-4}\\
0.1 & 1.69\times10^{-3}\\
0.5 & 5.57\times10^{-3}\\
1 & 7.22\times10^{-3}\\
2 & 6.91\times10^{-3}\\
4 & 3.94\times10^{-3}\\
8 & 8.86\times10^{-4}
\end{array}
$$

The state remained NPT across the scanned finite branch separations but the entanglement became extremely small again for large cats.

---

## 6. Current conjecture

The numerical evidence suggests the stronger statement

$$
\boxed{
\eta>\frac{\bar n}{\bar n+1}
\quad\Longrightarrow\quad
\mathcal N_{AB}(N_\Delta)>0
\ \text{for every finite }N_\Delta>0
}
$$

for the binary coherent source-cat family passed through a thermal attenuator.

Conversely, below the entanglement-breaking boundary the output must be separable for every input by definition.

The forward implication above has **not** been proved here.

---

## 7. Why the conjecture would matter

If true, the binary coherent gravitational difference mode would be a particularly strong probe of thermal-channel nonclassicality:

> every non-entanglement-breaking thermal attenuator would entangle the source qubit with the receiver for every finite nonzero branch separation, even though the entanglement can become arbitrarily small for an excessively large cat.

This would strengthen the wave-zone Gedankenexperiment because no delicate source-cat amplitude threshold would exist for the **presence** of entanglement—only for its measurable magnitude.

---

## 8. Immediate next step

Seek an analytic proof or counterexample. Possible routes:

1. exploit displacement covariance of the thermal attenuator;
2. construct an NPT principal minor adapted to finite coherent amplitude;
3. use the exact Gaussian-channel action on coherent-state dyads;
4. search literature on entangled coherent states through thermal attenuators.

Until then this result remains numerical evidence only.