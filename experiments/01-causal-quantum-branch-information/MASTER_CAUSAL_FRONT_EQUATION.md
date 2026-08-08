# Stationary Optimized-Envelope Causal Front

**Updated:** 2026-08-07 20:04 EDT  
**Status:** Correct but **special-case** closed-form result. This file no longer represents the universal receiver front. The general fixed-source result is in `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`.

## 1. Scope correction

The previously derived logarithmic front

$$
T_{\rm cap}^{\rm env}(R)
=\frac Rc+
\frac1\kappa
\ln\frac{\kappa_\Delta(R)}
{\kappa_\Delta(R)-\Gamma_{\rm th}}
$$

is obtained only when **both** of the following are imposed:

1. the receiver begins in its stationary thermal state,
   $$
   n_0=\Gamma_{\rm th}/\kappa;
   $$
2. for every target observation time, the incoming temporal mode is separately chosen to saturate the Cauchy–Schwarz loading bound.

It is therefore a **protocol-optimized envelope**, not the trajectory of one fixed physical gravitational source pulse.

For an actual source waveform $f$, the general criterion is instead

$$
\boxed{
\tau_f(t)>m(t),
}
$$

with

$$
\boxed{
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
e^{-\kappa(t-s)/2}f(s)
\right|^2
}
$$

and

$$
\boxed{
m(t)
=n_0e^{-\kappa t}
+\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-\kappa t}).
}
$$

See `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`.

---

## 2. Derivation of the optimized envelope

For any normalized temporal input supported up to target time $t$,

$$
\int_0^t ds\,|f(s)|^2\le1.
$$

Cauchy–Schwarz gives

$$
\tau_f(t)
\le
\frac{\kappa_\Delta}{\kappa}
(1-e^{-\kappa t}).
$$

The bound is saturated by a waveform proportional to

$$
f_t(s)
\propto
e^{-\kappa(t-s)/2}
$$

on $0<s<t$.

The subscript matters: the saturating waveform changes when the target time changes.

Define

$$
\boxed{
\tau_{\rm env}(t)
=\frac{\kappa_\Delta}{\kappa}
(1-e^{-\kappa t}).
}
$$

---

## 3. Arbitrary receiver initial occupation

Compare the envelope with

$$
m(t)
=n_0e^{-\kappa t}
+\frac{\Gamma_{\rm th}}{\kappa}(1-e^{-\kappa t}).
$$

The envelope can become non-entanglement-breaking only if

$$
\boxed{
\kappa_\Delta>\Gamma_{\rm th}.
}
$$

When this holds, the earliest optimized-envelope crossing is

$$
\boxed{
T_{\rm cap}^{\rm env}
=\frac1\kappa
\ln\left[
1+
\frac{\kappa n_0}
{\kappa_\Delta-\Gamma_{\rm th}}
\right].
}
$$

Restoring propagation delay gives

$$
\boxed{
T_{\rm cap}^{\rm env}(R)
=\frac Rc+
\frac1\kappa
\ln\left[
1+
\frac{\kappa n_0}
{\kappa_\Delta(R)-\Gamma_{\rm th}}
\right].
}
$$

---

## 4. Stationary receiver: old logarithmic formula

If

$$
n_0=\Gamma_{\rm th}/\kappa,
$$

then

$$
\boxed{
T_{\rm cap}^{\rm env}(R)
=\frac Rc+
\frac1\kappa
\ln\frac{\kappa_\Delta(R)}
{\kappa_\Delta(R)-\Gamma_{\rm th}}.
}
$$

This is the old logarithmic result.

It remains useful as a best-case stationary benchmark, but it must not be described as a universal causal gravitational front.

Near

$$
\kappa_\Delta\to\Gamma_{\rm th}^{+},
$$

this optimized stationary benchmark diverges logarithmically.

That divergence is **not universal**: a fixed finite pulse can instead exhibit a finite EB $\to$ non-EB $\to$ EB window whose two boundaries merge at a finite time.

---

## 5. Gravitational wave-zone specialization

For the aligned plus-quadrupole source/receiver link used in Experiment 01,

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g.
}
$$

For the stationary optimized envelope,

$$
\boxed{
T_{\rm cap}^{\rm env}(R)
=\frac Rc-
\frac1\kappa
\ln\left[
1-
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
\right].
}
$$

The corresponding envelope radius is

$$
\boxed{
R_{\rm env}
=\frac5{4k}
\sqrt{
\frac{\mathcal O\kappa_g}
{\Gamma_{\rm th}}
}.
}
$$

This is an upper-envelope capability scale. A specified physical source waveform generally has a smaller capability range.

For example, the matched decaying exponential source in `EXPONENTIAL_SOURCE_QUANTUM_WINDOW.md` has

$$
R_{\rm exp}
\simeq0.804742\,R_{\rm env}.
$$

---

## 6. What should be cited as the general result

The paper-level hierarchy is now:

### General fixed-source channel

$$
\boxed{
\tau_f(t)>m(t).
}
$$

### Protocol-optimized envelope

$$
\tau_f(t)
\le
\frac{\kappa_\Delta}{\kappa}(1-e^{-\kappa t}).
$$

### Stationary optimized-envelope special case

The logarithmic formula in this file.

This distinction is essential because recent noisy gravitational receiver models already contain fixed time-dependent transfer channels with signal probabilities that grow quadratically while thermal occupation grows linearly.

---

## 7. Finite certification correction

The normalized ratio

$$
\Lambda
=\ln\frac{|z|^2}{p_0p_v}
$$

remains an exact **sign/boundary** diagnostic for the binary coherent Gaussian theorem, but it should not be used by itself as a practical finite-certification strength near vanishing transmission.

The preferred next metric is an absolute quantity such as

- the negative eigenvalue of the matched $2\times2$ partial-transpose block;
- a rigorous lower bound on full negativity;
- or the exact full negativity where available.

---

## 8. Current role of this file

This file is retained because the optimized logarithmic envelope is analytically useful. It should now be read as:

> **the best-case stationary thermal receiver front under target-time-specific temporal-mode optimization.**

It is no longer the central universal prediction of Experiment 01.