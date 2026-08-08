# Numerical Stress Results — Approaching the Gaussian EB Boundary

**Date:** 2026-08-07  
**Status:** **INDEPENDENT NUMERICAL STRESS CHECK — CONSISTENT WITH ANALYTIC SIGN BOUNDARY**

## 1. Purpose

The coherent theorem predicts, for the phase-insensitive channel,

$$
\boxed{
\Delta\equiv\tau-m>0
\iff
\rho_{\rm out}\text{ NPT}.
}
$$

A useful adversarial numerical test is therefore to approach

$$
\Delta=0
$$

from both sides and ask whether

1. the non-EB negative PT eigenvalue stabilizes under increasing numerical resolution;
2. the EB-side false negative shrinks toward zero with increasing Fock cutoff / quadrature accuracy.

This note records the first controlled stress test for the **unit-gain additive Gaussian noise channel** using the independent random-displacement implementation.

Committed harness:

- `numerics/near_boundary_stress.py`

The harness now scans both Fock cutoff and Gauss–Hermite order.

---

## 2. Channel and state

For additive Gaussian noise,

$$
\tau=1,
$$

so define

$$
\Delta=1-m.
$$

The exact EB boundary is

$$
m=1.
$$

The test input was the balanced binary coherent hybrid state with branches

$$
|\pm a\rangle,
\qquad
a=0.35.
$$

The displacement integral was evaluated independently using tensor-product Gauss–Hermite quadrature. No analytic coherent-dyad kernel was used in the simulation.

---

## 3. Moderate boundary offset: $|\Delta|=10^{-1}$

At

$$
\Delta=+0.1,
\qquad
m=0.9,
$$

the minimum PT eigenvalue converges to approximately

$$
\boxed{
\lambda_{\min}^{\rm PT}
\simeq-5.52651\times10^{-3}.
}
$$

At Gauss–Hermite orders 12, 16, 20 with Fock cutoff $N=16$:

$$
\begin{array}{c|c}
\text{order}&\lambda_{\min}^{\rm PT}\\
\hline
12&-5.52464\times10^{-3}\\
16&-5.52647\times10^{-3}\\
20&-5.52651\times10^{-3}
\end{array}
$$

The physical negative eigenvalue is stable.

For the EB control

$$
\Delta=-0.1,
\qquad
m=1.1,
$$

the apparent negative eigenvalue falls from

$$
-1.44\times10^{-4}
$$

at low quadrature order to the few-$10^{-6}$ finite-basis floor.

---

## 4. Offset $|\Delta|=10^{-2}$

For

$$
\Delta=+10^{-2},
\qquad
m=0.99,
$$

the high-order result stabilizes near

$$
\boxed{
\lambda_{\min}^{\rm PT}
\simeq-4.895\times10^{-4}.
}
$$

At $N=16$:

$$
\begin{array}{c|c}
\text{order}&\lambda_{\min}^{\rm PT}\\
\hline
12&-5.28965\times10^{-4}\\
16&-4.89567\times10^{-4}\\
20&-4.89477\times10^{-4}
\end{array}
$$

For the EB-side control

$$
\Delta=-10^{-2},
$$

the apparent negative PT eigenvalue decreases strongly with quadrature order:

$$
-3.47\times10^{-4}
\to
-1.85\times10^{-5}
\to
-2.50\times10^{-6}
$$

for orders 12, 16, 20 at $N=16$.

The two sides therefore show qualitatively different convergence.

---

## 5. Offset $|\Delta|=10^{-3}$: Fock-cutoff discrimination

The most informative check combines fixed high quadrature order with increasing Fock cutoff.

Use Gauss–Hermite order 24.

### Non-EB side

$$
\Delta=+10^{-3},
\qquad
m=0.999.
$$

The minimum PT eigenvalue is

$$
\begin{array}{c|c}
N&\lambda_{\min}^{\rm PT}\\
\hline
16&-4.8374542\times10^{-5}\\
18&-4.8374548\times10^{-5}\\
20&-4.8374552\times10^{-5}
\end{array}
$$

Thus the physical negative eigenvalue is stable to roughly seven significant digits across this cutoff range.

### EB side

$$
\Delta=-10^{-3},
\qquad
m=1.001.
$$

The finite-cutoff false negative is

$$
\begin{array}{c|c}
N&\lambda_{\min}^{\rm PT}\\
\hline
16&-2.47825\times10^{-6}\\
18&-6.10570\times10^{-7}\\
20&-1.47473\times10^{-7}
\end{array}
$$

The false negative decreases by a factor of approximately

$$
\boxed{16.8}
$$

between $N=16$ and $N=20$, while the non-EB value is unchanged at

$$
\sim4.84\times10^{-5}.
$$

At $N=20$, the physical non-EB magnitude exceeds the EB numerical floor by roughly

$$
\boxed{3.3\times10^2}.
$$

This is a strong numerical discrimination.

---

## 6. Offset $|\Delta|=10^{-4}$

At order 24:

### Non-EB side

$$
\Delta=+10^{-4},
\qquad
m=0.9999,
$$

$$
\begin{array}{c|c}
N&\lambda_{\min}^{\rm PT}\\
\hline
16&-4.8319144\times10^{-6}\\
18&-4.8319670\times10^{-6}\\
20&-4.8320059\times10^{-6}
\end{array}
$$

Again the physical negative eigenvalue is stable under increasing Fock cutoff.

### EB side

$$
\Delta=-10^{-4},
\qquad
m=1.0001,
$$

$$
\begin{array}{c|c}
N&\lambda_{\min}^{\rm PT}\\
\hline
16&-2.48006\times10^{-6}\\
18&-6.11802\times10^{-7}\\
20&-2.16059\times10^{-7}
\end{array}
$$

At $N=20$, the physical non-EB negative eigenvalue is approximately

$$
\boxed{22.4}
$$

times larger in magnitude than the EB numerical floor.

The $10^{-4}$ test is therefore still resolved at this numerical precision, although the safety margin is much smaller than at $10^{-3}$.

---

## 7. Scaling observation

The stabilized physical PT minimum is approximately linear in the small positive channel excess $\Delta$ over the tested range:

$$
\lambda_{\min}^{\rm PT}
\approx
-4.84\times10^{-2}\,\Delta
$$

for the particular input amplitude

$$
a=0.35
$$

near the additive-noise EB point.

For example,

$$
\Delta=10^{-3}
\Rightarrow
\lambda_{\min}^{\rm PT}\simeq-4.84\times10^{-5},
$$

and

$$
\Delta=10^{-4}
\Rightarrow
\lambda_{\min}^{\rm PT}\simeq-4.83\times10^{-6}.
$$

This empirical linearity is consistent with a regular first-order crossing of the PT spectrum at the analytic EB boundary.

It is an observed numerical scaling, not an independent proof.

---

## 8. Adversarial interpretation

This is the behavior expected if the analytic boundary is genuine:

### Non-EB side

The negative eigenvalue converges to a finite negative value that scales down continuously as

$$
\Delta\to0^+.
$$

### EB side

The apparent negative eigenvalue is resolution dependent and collapses toward zero as the Fock cutoff increases.

The two sides do **not** converge to the same negative numerical artifact.

No counterexample or boundary shift was observed through

$$
|\tau-m|=10^{-4}
$$

for the additive-noise implementation.

---

## 9. Next numerical attacks

1. Repeat the same controlled offset test for the thermal amplifier, where the Stinespring cutoff behaves differently.
2. Repeat for thermal attenuation with independently chosen environmental occupations.
3. Vary coherent separation $a$ over at least an order of magnitude.
4. Add strongly unequal source weights $p$ as an implementation-level check of the analytic cancellation.
5. If practical, push additive-noise tests to $|\Delta|=10^{-5}$ with larger Fock cutoffs to locate the numerical resolution limit.

The numerical program remains secondary to the prior-art search because the analytic proof already gives the exact sign criterion.
