# Full Encoder + Passive Tail Loading Correction

**Date:** 2026-08-08  
**Status:** **EXACT MATCHED-LINEWIDTH RESULT IN THE UNDERDAMPED LOCAL-ENCODER MODEL; FAST-ENCODER EXPANSION CONTROLS THE PASSIVE LIMIT**

## 1. Purpose

`PAPER_CORE_V5_LOCAL_END_TO_END.md` uses

$$
4e^{-2}
$$

as the clean temporal loading factor for a naturally decaying exponential source captured by a constant-coupling passive receiver with matched linewidth.

The actual locally initialized protocol is slightly different: before the passive exponential tail begins, the sign-controlled source encoder already populates the mechanical source and emits a short precursor into every source output port.

This note computes the receiver loading for the **complete encoder-plus-tail waveform** and shows that

$$
4e^{-2}
$$

is the controlled

$$
g/\kappa\to\infty
$$

limit of the local protocol.

The first correction is positive.

---

# 2. Matched source and receiver

Set

$$
\boxed{
\kappa_A=\kappa_B=\kappa.
}
$$

Let the encoder coupling be

$$
g>\kappa/4
$$

and define

$$
\boxed{
\Omega=\sqrt{g^2-\kappa^2/16}.}
$$

Introduce

$$
\boxed{
\epsilon\equiv\frac{\kappa}{g}.
}
$$

The controller-empty time is

$$
\boxed{
T_*
=\frac{
\pi-\arctan(4\Omega/\kappa)
}{\Omega}
=\frac{
\pi/2+\arctan(\kappa/4\Omega)
}{\Omega}.
}
$$

Define the dimensionless handoff time

$$
\boxed{y\equiv\kappa T_*.}
$$

For

$$
\epsilon\ll1,
$$

$$
\boxed{
T_*
=\frac{\pi}{2g}
+\frac{\kappa}{4g^2}
+\frac{\pi\kappa^2}{64g^3}
+O\!\left(\frac{\kappa^3}{g^4}\right),
}
$$

so

$$
\boxed{
y
=\frac\pi2\epsilon
+\frac14\epsilon^2
+O(\epsilon^3).}
$$

---

# 3. Complete normalized source waveform

The normalized source waveform is

$$
\boxed{
 f_{\rm full}(t)
=\sqrt\kappa\frac g\Omega
 e^{-\kappa t/4}\sin(\Omega t),
\qquad0<t<T_*,
}
$$

and

$$
\boxed{
 f_{\rm full}(t)
=\sqrt\kappa
 e^{-\kappa T_*/4}
 e^{-\kappa(t-T_*)/2},
\qquad t>T_*.
}
$$

It obeys

$$
\int_0^\infty|f_{\rm full}(t)|^2dt=1.
$$

The receiver amplitude kernel is

$$
\boxed{
I(t)
=\int_0^t ds\,
 e^{-\kappa(t-s)/2}
 f_{\rm full}(s).
}
$$

The coherent receiver parameter is

$$
\boxed{
\tau_{\rm full}(t)
=\kappa_\Delta|I(t)|^2.
}
$$

Define

$$
\boxed{
\beta_\Delta
=\frac{\kappa_\Delta}{\kappa}.}
$$

Then

$$
\frac{\tau_{\rm full}}{\beta_\Delta}
=|\sqrt\kappa I|^2.
$$

---

# 4. Exact precursor contribution at the handoff

At

$$
t=T_*,
$$

$$
I_{\rm pre}(T_*)
=\sqrt\kappa\frac g\Omega
 e^{-\kappa T_*/2}
\int_0^{T_*}ds\,
 e^{\kappa s/4}\sin(\Omega s).
$$

Use

$$
\left(\frac\kappa4\right)^2+\Omega^2=g^2.
$$

The controller-empty condition implies

$$
\cos(\Omega T_*)
=-\frac\kappa{4\Omega}
\sin(\Omega T_*),
$$

and therefore

$$
\boxed{
\sin(\Omega T_*)=\frac\Omega g.}
$$

The integral reduces exactly to

$$
\int_0^{T_*}ds\,
 e^{\kappa s/4}\sin(\Omega s)
=
\frac\Omega{g^2}
\left[
1+\frac\kappa{2g}e^{y/4}
\right].
$$

Hence

$$
\boxed{
\sqrt\kappa I_{\rm pre}(T_*)
=
\epsilon e^{-y/2}
\left[
1+\frac\epsilon2 e^{y/4}
\right].}
$$

---

# 5. Receiver amplitude after the handoff

Let

$$
\boxed{x\equiv\kappa t.}
$$

For

$$
t>T_*,
$$

the precursor contribution simply rings down in the receiver:

$$
\sqrt\kappa I_{\rm pre}(t)
=
 e^{-(x-y)/2}
\sqrt\kappa I_{\rm pre}(T_*).
$$

The passive-tail contribution is

$$
\sqrt\kappa I_{\rm tail}(t)
=(x-y)e^{-x/2}e^{y/4}.
$$

Adding them gives the compact exact result

$$
\boxed{
\sqrt\kappa I(t)
=e^{-x/2}
\left[
\epsilon
+e^{y/4}
\left(
 x-y+\frac{\epsilon^2}{2}
\right)
\right],
\qquad x>y.}
$$

This formula contains both

- the short local-encoder precursor;
- the freely decaying passive source tail.

---

# 6. Exact post-handoff optimum

Differentiate the amplitude with respect to

$$
x.
$$

The interior stationary point satisfies

$$
\boxed{
 x_*
=2+y
-\frac{\epsilon^2}{2}
-\epsilon e^{-y/4}.}
$$

For the intended fast-encoder regime

$$
\epsilon\ll1,
$$

one has

$$
x_*>y,
$$

so this is the relevant maximum after controller handoff.

At the stationary point, the bracket in the amplitude equals

$$
2e^{y/4}.
$$

Therefore

$$
\boxed{
\frac{\tau_{\rm full}^{\max}}
{\beta_\Delta}
=
4e^{-2}
\exp\left[
\epsilon e^{-y/4}
-\frac y2
+\frac{\epsilon^2}{2}
\right].}
$$

This is the exact matched-linewidth full-waveform peak within the underdamped constant-

$$
g
$$

encoder model, provided the maximum lies after

$$
T_*.
$$

The repository only needs the controlled regime

$$
\epsilon\ll1,
$$

where that condition is automatically satisfied.

---

# 7. Fast-encoder expansion

Using

$$
y
=\frac\pi2\epsilon
+\frac14\epsilon^2
+O(\epsilon^3),
$$

we find

$$
\epsilon e^{-y/4}
-\frac y2
+\frac{\epsilon^2}{2}
=
\left(1-\frac\pi4\right)\epsilon
+\frac{3-\pi}{8}\epsilon^2
+O(\epsilon^3).
$$

Hence

$$
\boxed{
\tau_{\rm full}^{\max}
=
4e^{-2}\beta_\Delta
\left[
1+
\left(1-\frac\pi4\right)
\frac\kappa g
+O\!\left(\frac{\kappa^2}{g^2}\right)
\right].}
$$

Numerically,

$$
\boxed{
1-\frac\pi4
\simeq0.2146018366.}
$$

Thus the leading encoder correction is positive.

---

# 8. Why the correction is positive

The pure exponential result

$$
4e^{-2}
$$

assumes the receiver starts seeing the source only when the fully prepared passive tail begins.

The local protocol is physically more complete:

- while the controller transfers amplitude into the source mode;
- the source mode is already weakly coupled to the gravitational output;
- that precursor reaches the receiver earlier;
- part of it remains stored when the passive tail arrives.

The precursor therefore supplies a small amount of useful pre-loading.

It is not an uncontrolled artifact. It is part of the normalized source mode required by the local preparation protocol.

---

# 9. End-to-end gravitational specialization

For vacuum nongravitational source loss,

$$
\tau_{A\to B}
=\beta_{g,A}\tau_{\rm full},
$$

with

$$
\beta_{g,A}
=\kappa_{g,A}/\kappa_A.
$$

Also

$$
\beta_\Delta
=\eta_{\rm store}\beta_{g,B},
$$

where

$$
\beta_{g,B}=\kappa_{g,B}/\kappa_B.
$$

For matched total source and receiver linewidths,

$$
\kappa_A=\kappa_B=\kappa,
$$

we obtain

$$
\boxed{
\tau_{A\to B}^{\max}
=
4e^{-2}
\beta_{g,A}\beta_{g,B}\eta_{\rm store}
\exp\left[
\epsilon e^{-y/4}
-\frac y2
+\frac{\epsilon^2}{2}
\right].}
$$

In the fast-encoder limit,

$$
\boxed{
\tau_{A\to B}^{\max}
=
4e^{-2}
\beta_{g,A}\beta_{g,B}\eta_{\rm store}
\left[
1+
\left(1-\frac\pi4\right)
\frac\kappa g
+O\!\left(\frac{\kappa^2}{g^2}\right)
\right].}
$$

With

$$
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2},
$$

$$
\boxed{
\tau_{A\to B}^{\max}
=
\frac{25e^{-2}}4
\frac{\mathcal O}{(kR)^2}
\beta_{g,A}\beta_{g,B}
\left[
1+
\left(1-\frac\pi4\right)
\frac\kappa g
+\cdots
\right].}
$$

---

# 10. Consequence for the paper

The simple formula

$$
\boxed{
\tau_{\rm passive}^{\max}
=4e^{-2}\beta_{g,A}\beta_{g,B}\eta_{\rm store}
}
$$

is safe as the leading fast-encoder passive benchmark.

It should be described as

> the
> $$
> g/\kappa\to\infty
> $$
> limit of the locally initialized encoder-plus-tail protocol,

not as the exact finite-

$$
g
$$

maximum.

If one correction is retained in the main text, use

$$
\boxed{
\frac{\tau_{\rm full}^{\max}}
{4e^{-2}\beta_{g,A}\beta_{g,B}\eta_{\rm store}}
=
1+
\left(1-\frac\pi4\right)
\frac\kappa g
+O\!\left(\frac{\kappa^2}{g^2}\right).}
$$

The exact exponential expression belongs in an appendix.

---

# 11. Adversarial verdict

The local preparation step does not invalidate the passive \(4e^{-2}\) result.

Instead:

1. the complete encoder-plus-tail waveform has an analytic receiver convolution;
2. its matched-linewidth maximum is known exactly in the intended post-handoff regime;
3. the passive exponential result is the controlled fast-encoder limit;
4. the first local-encoder correction is small and positive;
5. the same hierarchy
   $$
   \kappa\ll g\ll\omega
   $$
   simultaneously controls precursor norm, encoder thermal contamination, and the RWA.

This removes the protocol-mixing ambiguity identified after `PAPER_CORE_V5_LOCAL_END_TO_END.md`.
