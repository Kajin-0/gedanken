# Finite-Strength Causal Certification Front

**Timestamp:** 2026-08-07 17:12 EDT  
**Status:** Exact within the binary-coherent thermal-channel + stationary passive Markov receiver model.

## 1. Why the bare NPT front is not enough

The exact finite-cat theorem shows that the **sign** of source-receiver entanglement is independent of finite coherent branch separation:

$$
\rho_{AB}\text{ NPT}
\iff
\eta>m.
$$

Therefore an arbitrarily small nonzero source cat can cross the NPT boundary at the same receiver time as a large cat.

Physically, however, the amount of entanglement/witness violation tends to zero with source branch strength. A measurable prediction should therefore distinguish

1. the mathematical NPT front;
2. a **finite-strength certification front** at which an exact witness violation reaches a specified nonzero margin.

---

## 2. Exact logarithmic witness margin

For the symmetric binary coherent state

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle+|1\rangle|-a\rangle}{\sqrt2},
$$

define

$$
N_\Delta=4|a|^2.
$$

For a phase-insensitive Gaussian channel with coherent gain/transmission $\tau$ and vacuum-output thermal occupation $m>0$, the exact optimized three-element witness obeys

$$
\frac{|z_v|^2}{p_0p_v}
=
\exp\left[
\frac{N_\Delta}{m}(\tau-m)
\right].
$$

Define the dimensionless logarithmic certification margin

$$
\boxed{
\Lambda
\equiv
\ln\left(
\frac{|z_v|^2}{p_0p_v}
\right).
}
$$

Then

$$
\boxed{
\Lambda
=\frac{N_\Delta}{m}(\tau-m).
}
$$

Thus

$$
\Lambda>0
$$

is exactly equivalent to NPT for the binary coherent family, but the magnitude of $\Lambda$ directly tracks the strength of the witness violation.

---

## 3. Passive gravitational receiver

For the stationary passive Markov receiver,

$$
\dot c
=-\frac{\kappa_{\rm tot}}2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_a\sqrt{\kappa_a}\,b_a^{\rm in},
$$

with

$$
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a,
$$

the stationary thermal occupation is

$$
\boxed{
m_*=\frac{\Gamma_{\rm th}}{\kappa_{\rm tot}}.}
$$

For any normalized incoming branch-mode waveform, the coherent transfer coefficient obeys

$$
\eta_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
\left(1-e^{-\kappa_{\rm tot}\tau}\right),
\qquad
\tau=t-R/c.
$$

The time-reversed receiver kernel saturates this inequality. Therefore the largest possible exact witness margin at time $\tau$ is

$$
\Lambda_{\max}(\tau)
=
\frac{N_\Delta}{m_*}
\left[
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau})
-m_*
\right].
$$

Using $m_*=\Gamma_{\rm th}/\kappa_{\rm tot}$ gives

$$
\boxed{
\Lambda_{\max}(\tau)
=
\frac{N_\Delta}{\Gamma_{\rm th}}
\left[
\kappa_\Delta
(1-e^{-\kappa_{\rm tot}\tau})
-\Gamma_{\rm th}
\right].
}
$$

This expression is exact within the model whenever $\Gamma_{\rm th}>0$.

---

## 4. Bare NPT front as the zero-margin case

Setting

$$
\Lambda_{\rm req}=0
$$

gives

$$
\kappa_\Delta
(1-e^{-\kappa_{\rm tot}\tau})
=\Gamma_{\rm th},
$$

so

$$
T_{\rm NPT}^{\min}
=\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right],
$$

recovering the exact causal-front theorem.

---

## 5. Finite-strength certification front

Now require a nonzero witness margin

$$
\Lambda\ge\Lambda_{\rm req}>0.
$$

The optimal receiver must satisfy

$$
\kappa_\Delta
(1-e^{-\kappa_{\rm tot}\tau})
\ge
\Gamma_{\rm th}
\left(1+rac{\Lambda_{\rm req}}{N_\Delta}\right).
$$

Therefore the earliest possible certification time is

$$
\boxed{
T_{\Lambda}^{\min}
=
\frac Rc
-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{\Gamma_{\rm th}}{\kappa_\Delta}
\left(1+rac{\Lambda_{\rm req}}{N_\Delta}\right)
\right].
}
$$

This exists only if

$$
\boxed{
\Gamma_{\rm th}
\left(1+rac{\Lambda_{\rm req}}{N_\Delta}\right)
<\kappa_\Delta.
}
$$

Thus the source branch strength enters exactly when one asks for a **finite observable quantum margin**, even though it cancels from the infinitesimal NPT sign boundary.

---

## 6. Maximum available witness margin

At infinite optimized capture time,

$$
\eta_\infty
=\frac{\kappa_\Delta}{\kappa_{\rm tot}}.
$$

Hence

$$
\boxed{
\Lambda_\infty
=N_\Delta
\left(
\frac{\kappa_\Delta}{\Gamma_{\rm th}}-1
\right).
}
$$

Equivalently, using

$$
\epsilon_Q
=1-\frac{\Gamma_{\rm th}}{\kappa_\Delta},
$$

$$
\boxed{
\Lambda_\infty
=N_\Delta
\frac{\epsilon_Q}{1-\epsilon_Q}.
}
$$

Therefore a finite source cannot generate an arbitrarily strong certificate arbitrarily close to the EB boundary.

There are two independent resources:

- channel quantum excess $\epsilon_Q$;
- source difference-mode strength $N_\Delta$.

The maximum exact certification margin is their product in the form above.

---

## 7. Excess delay beyond the NPT front

Let

$$
T_0=T_{\rm NPT}^{\min}.
$$

Then

$$
T_\Lambda^{\min}-T_0
=
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{1-\Gamma_{\rm th}/\kappa_\Delta}
{1-(\Gamma_{\rm th}/\kappa_\Delta)(1+\Lambda_{\rm req}/N_\Delta)}
\right].
$$

For a small required margin,

$$
\boxed{
T_\Lambda^{\min}-T_0
\simeq
\frac{\Gamma_{\rm th}}
{\kappa_{\rm tot}(\kappa_\Delta-\Gamma_{\rm th})}
\frac{\Lambda_{\rm req}}{N_\Delta}.
}
$$

So the measurable-front delay diverges both when

- the receiver approaches the EB boundary;
- the source branch-difference mode becomes weak.

This resolves the apparent paradox of an amplitude-independent mathematical NPT onset.

---

## 8. Insert the gravitational source amplitude

For a conserved nonrelativistic quadrupole history,

$$
\boxed{
N_\Delta
=
\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

For the narrow-band plus-type branch quadrupole

$$
\Delta Q_{xx}=q_0 f(t)\cos\omega_0t,
\qquad
\Delta Q_{yy}=-\Delta Q_{xx},
$$

$$
\boxed{
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}{5\hbar c^5},
\qquad
T_f=\int dt\,|f(t)|^2.
}
$$

Thus the finite-strength gravitational certification front can be written entirely in terms of

- source quadrupole amplitude and waveform;
- source-receiver separation $R$;
- source-receiver mode overlap through $\kappa_\Delta$;
- receiver linewidths;
- receiver thermal occupations;
- required witness margin.

---

## 9. Feynman-level interpretation

> **The first infinitesimal entanglement does not care how large the cat is; it only asks whether the receiver channel is quantum-capable. But a usable certificate does care. A weak source writes only a tiny quantum branch record, so after the light cone arrives one must wait longer for a fixed witness violation—or may never reach it at all. The exact certification front therefore separates three clocks: propagation time, channel-quantum build time, and finite-signal accumulation time.**

---

## 10. Strongest next step

1. Choose a physically normalized source quadrupole waveform and receiver mode and produce the first complete spacetime plot of signal, NPT, and finite-certification fronts.
2. Extend the certification-front formula to the general phase-insensitive Gaussian channel theorem, including active receiver gain.
3. Determine whether this finite-strength front or its gravity-specific form already appears in quantum-channel speed-limit literature.
