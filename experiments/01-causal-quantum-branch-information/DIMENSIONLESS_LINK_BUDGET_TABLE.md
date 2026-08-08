# Dimensionless End-to-End Quantum Link Comparison

**Date:** 2026-08-08  
**Status:** **FEASIBILITY TABLE FOR V6 — SEPARATES SOURCE AND RECEIVER BRANCHING FROM TEMPORAL LOADING**

## 1. Purpose

The V6 manuscript reduces the vacuum-source coherent transfer to

$$
\boxed{
\tau_{A\to B}(t)
=
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t),
\qquad
0\le\mathcal T_f(t)\le1.
}
$$

Define the waveform-independent link ceiling

$$
\boxed{
\eta_Q^{\rm link}
\equiv
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}.}
$$

This note uses one deliberately aggressive historical benchmark to show separately what is gained by improving

- the source gravitational branching fraction;
- the receiver gravitational branching fraction;
- temporal mode matching.

The purpose is not to propose an experiment. It is to make the multiplicative bottlenecks visible.

---

# 2. Benchmark

Use

$$
\boxed{
M_e=4\,\mathrm{kg},
\quad
L=1\,\mathrm m,
\quad
f=1\,\mathrm{MHz},
\quad
Q=10^{12},
\quad
kR=10,
\quad
\mathcal O=1.
}
$$

For the endpoint-leading V6 quadrupole mode,

$$
\boxed{
\mathcal C_e
=\frac{2GM_e}{c^2L}
\simeq5.94093\times10^{-27},}
$$

and

$$
\boxed{
\beta
=\frac{\omega L}{c}
\simeq2.09585\times10^{-2}.}
$$

The explicit source/receiver gravitational branching fraction is

$$
\boxed{
\beta_g
=\frac15Q\mathcal C_e\beta^3
\simeq1.09386\times10^{-20}.}
$$

Finite-spoke corrections multiply this by

$$
\mathcal C_\kappa(q)=1+O(q^2)
$$

and are omitted from this order-of-magnitude comparison.

At

$$
kR=10,
$$

$$
\boxed{
\eta_{\rm store}
=\frac{25}{16(10)^2}
=1.5625\times10^{-2}.}
$$

---

# 3. Four interface cases

Let **ordinary** mean the benchmark branching

$$
\beta_g=1.09386\times10^{-20},
$$

and **ideal gravitational interface** mean

$$
\beta_g=1.
$$

Then:

| Source interface | Receiver interface | \(\beta_{g,A}\) | \(\beta_{g,B}\) | \(\eta_Q^{\rm link}=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\) |
|---|---|---:|---:|---:|
| ordinary | ordinary | \(1.09386\times10^{-20}\) | \(1.09386\times10^{-20}\) | \(1.87\times10^{-42}\) |
| ideal | ordinary | \(1\) | \(1.09386\times10^{-20}\) | \(1.71\times10^{-22}\) |
| ordinary | ideal | \(1.09386\times10^{-20}\) | \(1\) | \(1.71\times10^{-22}\) |
| ideal | ideal | \(1\) | \(1\) | \(1.5625\times10^{-2}\) |

More precisely,

$$
\boxed{
\eta_{Q,\rm oo}^{\rm link}
\simeq1.8696\times10^{-42},}
$$

$$
\boxed{
\eta_{Q,\rm io}^{\rm link}
=
\eta_{Q,\rm oi}^{\rm link}
\simeq1.7092\times10^{-22},}
$$

$$
\boxed{
\eta_{Q,\rm ii}^{\rm link}
=1.5625\times10^{-2}.}
$$

The symmetry between source and receiver branching is exact in the ideal vacuum one-way link budget.

---

# 4. Temporal waveform comparison

The coherent transfer is

$$
\tau^{\max}
=\eta_Q^{\rm link}\mathcal T_{\max}.
$$

Use three representative temporal factors:

### Matched passive exponential

$$
\boxed{
\mathcal T_{\exp}^{\max}=4e^{-2}=0.541341.}
$$

### Smooth \(\sin^4\) waveform

$$
\boxed{
\mathcal T_{\sin^4}^{\max}=0.7980213.}
$$

### Ideal target-time shaping

$$
\boxed{
\mathcal T_{\rm ideal}^{\max}=1.}
$$

The resulting comparison is:

| Source | Receiver | link ceiling \(\eta_Q^{\rm link}\) | matched exponential | \(\sin^4\) | ideal temporal shape |
|---|---|---:|---:|---:|---:|
| ordinary | ordinary | \(1.87\times10^{-42}\) | \(1.01\times10^{-42}\) | \(1.49\times10^{-42}\) | \(1.87\times10^{-42}\) |
| ideal | ordinary | \(1.71\times10^{-22}\) | \(9.25\times10^{-23}\) | \(1.36\times10^{-22}\) | \(1.71\times10^{-22}\) |
| ordinary | ideal | \(1.71\times10^{-22}\) | \(9.25\times10^{-23}\) | \(1.36\times10^{-22}\) | \(1.71\times10^{-22}\) |
| ideal | ideal | \(1.5625\times10^{-2}\) | \(8.46\times10^{-3}\) | \(1.247\times10^{-2}\) | \(1.5625\times10^{-2}\) |

The key numerical values are

$$
\boxed{
\tau_{\rm oo,exp}^{\max}
\simeq1.0121\times10^{-42},}
$$

$$
\boxed{
\tau_{\rm oo,sin4}^{\max}
\simeq1.4920\times10^{-42},}
$$

$$
\boxed{
\tau_{\rm io,sin4}^{\max}
=\tau_{\rm oi,sin4}^{\max}
\simeq1.3639\times10^{-22}.}
$$

---

# 5. What the table says immediately

## Temporal shaping is secondary

For fixed physical interfaces, changing from the matched passive exponential to an ideal temporal mode buys only

$$
\boxed{
\frac1{4e^{-2}}
=\frac{e^2}{4}
\simeq1.85.}
$$

The \(\sin^4\) pulse already recovers about

$$
79.8\%
$$

of the ideal temporal ceiling.

## One bad matter-gravity interface is enough to dominate

Making **only one** end ideal changes the link from

$$
10^{-42}
$$

to

$$
10^{-22},
$$

but the remaining ordinary interface still suppresses the link by twenty orders of magnitude.

## Both interfaces must improve for a strong link

Only when

$$
\beta_{g,A}\sim\beta_{g,B}\sim1
$$

does the link approach the geometric/mode-capture scale

$$
\eta_{\rm store}\sim10^{-2}
$$

at this deliberately close wave-zone separation.

Thus the hierarchy of priorities is

$$
\boxed{
\text{matter–gravity branching}
\gg
\text{free-space mode capture}
\gg
\text{temporal pulse optimization}
}
$$

for the ordinary-matter benchmark.

---

# 6. Why the old \(10^{-22}\) receiver-local benchmark reappears

Earlier receiver calculations started with a **normalized incoming gravitational wavepacket**.

That evaluates

$$
\eta_{\rm store}\beta_{g,B}\mathcal T_f
$$

rather than the complete mechanical-source link

$$
\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f.
$$

Setting

$$
\beta_{g,A}=1
$$

in the new table therefore recovers the old receiver-local scale.

For the \(\sin^4\) waveform,

$$
\boxed{
(1)(0.015625)
(1.09386\times10^{-20})
(0.7980213)
\simeq1.36\times10^{-22}.}
$$

The old result was a conditional receiver result, not an end-to-end mechanical-source transmissivity.

---

# 7. Branching is not just a numerical nuisance

For the benchmark total receiver linewidth,

$$
\kappa_B
=\omega/Q
\simeq6.28319\times10^{-6}\,\mathrm{s}^{-1}.
$$

The intrinsic gravitational linewidth is

$$
\boxed{
\kappa_g
=\beta_g\kappa_B
\simeq6.8729\times10^{-26}\,\mathrm{s}^{-1}.}
$$

A hypothetical source made purely gravitational by eliminating all ordinary damping would have natural lifetime

$$
\boxed{
\kappa_g^{-1}
\simeq4.61\times10^{17}\,\mathrm{yr}.}
$$

Therefore the ordinary branching factor cannot simply be set to unity while keeping the original mechanical response time unchanged.

This is the passive speed–efficiency tradeoff derived separately in

`PASSIVE_OPTIMIZATION_SCOPE_AND_SPEED_TRADEOFF.md`.

Coherent source control can reshape the temporal mode without adding dissipative source broadening, but it cannot change the branch-distance partition among physical source output ports unless those couplings themselves are changed.

---

# 8. Thermal interpretation

For a stationary receiver with thermal occupation

$$
n_{{\rm th},B},
$$

the ideal vacuum-source non-EB condition is schematically

$$
\eta_Q^{\rm link}\mathcal T_f
>n_{{\rm th},B}
$$

for the stationary-noise specialization.

The table therefore immediately sets the required occupation scale.

However the manuscript should prefer

$$
n_{{\rm th},B}
$$

over converting every row to temperature, because

- occupation is the natural channel variable;
- the temperature conversion is logarithmic at \(n\ll1\);
- source noise and nonstationary receiver preparation can modify the simple equilibrium interpretation.

---

# 9. Recommended manuscript use

Use a compact version of the four-case table in the main paper.

The purpose should be conceptual rather than promotional:

> **The table shows exactly where the old twenty-order discrepancy comes from. A normalized incoming graviton mode tests the receiver interface only. A physical mechanical source must first branch into gravity. Once source and receiver are placed in the same link budget, ordinary matter suppresses the transfer twice.**

The table also makes clear why pulse-shape optimization should be discussed after interface quality, not before it.

---

# 10. Strongest conclusion

For the present weak-field architecture,

$$
\boxed{
\eta_Q^{\rm link}
=
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
}
$$

is the correct waveform-independent performance ceiling.

The benchmark hierarchy is

$$
\boxed{
10^{-42}
\quad\text{ordinary/ordinary},
}
$$

$$
\boxed{
10^{-22}
\quad\text{one ideal interface},
}
$$

$$
\boxed{
10^{-2}
\quad\text{two ideal interfaces at }kR=10.
}
$$

This is a far more informative feasibility summary than quoting one receiver-local negativity or one special pulse coefficient in isolation.
