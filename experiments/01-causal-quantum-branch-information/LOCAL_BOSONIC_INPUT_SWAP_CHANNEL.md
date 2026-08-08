# Local Bosonic Input Swap → Full Gravitational Output Channel

**Date:** 2026-08-07  
**Status:** **CANONICAL CHANNEL-INPUT CONSTRUCTION — ARBITRARY LOCAL BOSONIC INPUT, NO PRE-EXISTING BRANCH-DISPLACED MECHANICAL SOURCE REQUIRED**

## 1. Why this construction is stronger

The passive source notes begin with a prepared mechanical source mode and then calculate its future gravitational output.

That is an excellent emission model, but a strict source-controlled communication channel should begin with a quantum input localized in the source laboratory before the radiating mechanical branch is created.

The cleanest solution is not to use the source qubit itself as the channel input.

Instead introduce a local bosonic memory mode

$$
\boxed{d}
$$

at the source and transfer its arbitrary quantum state into the finite-spoke plus mode

$$
\boxed{a}
$$

through an ordinary resonant beam-splitter swap.

This gives a genuine Gaussian channel input that can be entangled with an untouched reference in the standard entanglement-breaking test.

The specific binary coherent state

$$
\frac{|0\rangle_R|+\alpha\rangle_d
+|1\rangle_R|-\alpha\rangle_d}{\sqrt2}
$$

is then only one possible probe.

---

# 2. Local input and source modes

Let

- $d$ = compact local bosonic input/memory mode;
- $a$ = finite-spoke gravitational source plus mode;
- both have angular frequency $\omega$.

Before the encoding begins, take

$$
\boxed{
\rho_{Rd}
\otimes
|0\rangle_a\langle0|
\otimes
\rho_{\rm env},
}
$$

where $R$ is an untouched reference and the external source baths are initially independent of the state of $d$.

The source-local encoding Hamiltonian is

$$
\boxed{
H_{\rm swap}
=\hbar g(a^\dagger d+a d^\dagger).
}
$$

No branch-dependent actuator is required. The input state itself carries the quantum information.

The interaction conserves total oscillator excitation:

$$
[H_{\rm swap},a^\dagger a+d^\dagger d]=0.
$$

---

# 3. Ideal lossless state swap

In the interaction picture,

$$
\boxed{
a(t)=a(0)\cos(gt)-i d(0)\sin(gt),}
$$

$$
\boxed{d(t)=d(0)\cos(gt)-i a(0)\sin(gt).}
$$

At

$$
\boxed{T_{\rm sw}=\frac\pi{2g},}
$$

$$
\boxed{
a(T_{\rm sw})=-i d(0),}
$$

$$
\boxed{d(T_{\rm sw})=-i a(0).}
$$

For source vacuum

$$
a(0)|0\rangle_a=0,
$$

the local memory is reset to vacuum and its **entire arbitrary quantum state** is transferred into the radiating finite-spoke mode, up to a known phase rotation.

Thus for any input state

$$
\rho_d,
$$

$$
\boxed{
\rho_d\otimes|0\rangle_a\langle0|
\longrightarrow
|0\rangle_d\langle0|
\otimes
\mathcal R_{-\pi/2}(\rho_d)_a.
}
$$

The same holds when $d$ is entangled with an external reference $R$.

This is the correct local encoding primitive for an entanglement-breaking channel test.

---

# 4. Binary coherent probe as a special case

Take

$$
|\Psi\rangle_{Rd}
=\frac{
|0\rangle_R|+\alpha_0\rangle_d
+|1\rangle_R|-\alpha_0\rangle_d
}{\sqrt2}.
$$

After the ideal half-swap,

$$
\boxed{
|\Psi\rangle_{Ra}
=\frac{
|0\rangle_R|-i\alpha_0\rangle_a
+|1\rangle_R|+i\alpha_0\rangle_a
}{\sqrt2},
}
$$

while

$$
\boxed{d\text{ is vacuum}.}
$$

A local phase-space rotation of the source mode converts the branch pair to real $|\pm\alpha_0\rangle$ if desired.

The source qubit/reference is now correctly separated from the bosonic channel input.

---

# 5. Include source damping during the swap

Let the finite-spoke source mode couple to Markov output ports $j$ with rates

$$
\kappa_j,
$$

and total

$$
\boxed{
\kappa_A=\sum_j\kappa_j.
}
$$

The gravitational port is one of them:

$$
\boxed{
\kappa_{g,A}\subset\kappa_A.
}
$$

During the swap,

$$
\dot a
=-\frac{\kappa_A}{2}a
-igd
-\sum_j\sqrt{\kappa_j}\,b_j^{\rm in},
$$

$$
\dot d=-iga.
$$

Assume first that all source baths are vacuum.

For the coefficient multiplying the initial input operator $d(0)$, define

$$
a(t)=h(t)d(0)+\text{vacuum terms},
$$

$$
d(t)=r(t)d(0)+\text{vacuum terms}.
$$

Then

$$
\dot h=-\frac{\kappa_A}{2}h-igr,
$$

$$
\dot r=-igh,
$$

with

$$
h(0)=0,
\qquad
r(0)=1.
$$

---

# 6. Exact damped swap solution

For

$$
\boxed{g>\kappa_A/4,}
$$

define

$$
\boxed{
\Omega
=\sqrt{g^2-\frac{\kappa_A^2}{16}}.
}
$$

The exact coefficients are

$$
\boxed{
r(t)
=e^{-\kappa_A t/4}
\left[
\cos(\Omega t)
+\frac{\kappa_A}{4\Omega}
\sin(\Omega t)
\right],
}
$$

$$
\boxed{
h(t)
=-i\frac{g}{\Omega}
 e^{-\kappa_A t/4}
\sin(\Omega t).
}
$$

Choose the first positive time $T_*$ at which

$$
\boxed{r(T_*)=0.}
$$

Equivalently,

$$
\boxed{
\tan(\Omega T_*)
=-\frac{4\Omega}{\kappa_A},
}
$$

with

$$
\boxed{
T_*
=
\frac{
\pi-\arctan(4\Omega/\kappa_A)
}{\Omega}.
}
$$

At that time,

$$
\boxed{
h(T_*)=-i e^{-\kappa_A T_*/4}.}
$$

Therefore the source mode contains a pure-loss version of the local input with encoder transmissivity

$$
\boxed{
\eta_{\rm enc}
=e^{-\kappa_A T_*/2}.
}
$$

The local memory output has **zero coefficient** from the nonvacuum input mode.

Because every other input is vacuum, the memory mode $d(T_*)$ is exactly vacuum and factorizes from the remaining system.

---

# 7. Do not mistake $\eta_{\rm enc}$ for an additional end-to-end loss

If one throws away all radiation emitted during the encoding interval and starts the channel only at $T_*$, then the remaining mechanical source indeed contains only the fraction

$$
\eta_{\rm enc}
$$

of the local input.

But the supposedly “lost” fraction was not destroyed.

It already left through the physical source output ports during the local swap.

If the complete source-controlled outgoing field is retained from the moment the encoding begins, there is no additional encoder loss beyond the actual physical branching among those ports.

This is the central simplification.

---

# 8. Full source response to the local input

Keep the swap coupling active until $T_*$ and then decouple $d$ locally.

For

$$
0\le t\le T_*,
$$

$$
\boxed{
h(t)
=-i\frac{g}{\Omega}
 e^{-\kappa_A t/4}
\sin(\Omega t).}
$$

After the memory is emptied and decoupled, the source mode evolves passively:

$$
\boxed{
h(t)
=-i e^{-\kappa_A T_*/4}
 e^{-\kappa_A(t-T_*)/2},
\qquad t\ge T_*.
}
$$

The coefficient is continuous at the handoff.

---

# 9. Exact normalization identity

During the encoder, the single-input amplitude satisfies

$$
\boxed{
\frac{d}{dt}
\left(
|h|^2+|r|^2
\right)
=-\kappa_A|h|^2.
}
$$

At

$$
t=0,
$$

$$
|h|^2+|r|^2=1.
$$

At

$$
t=T_*,
$$

$$
r(T_*)=0.
$$

The later passive tail completely decays.

Therefore

$$
\boxed{
\kappa_A
\int_0^\infty dt\,|h(t)|^2
=1.
}
$$

This identity is exact and independent of $g$ as long as the memory is emptied and the source is allowed to decay fully.

---

# 10. One normalized full source temporal mode

Define

$$
\boxed{
f_{\rm full}(t)
=i\sqrt{\kappa_A}\,h(t).}
$$

Then

$$
\boxed{
\int_0^\infty dt\,|f_{\rm full}(t)|^2=1.}
$$

Explicitly,

### Encoding interval

$$
\boxed{
f_{\rm full}(t)
=
\sqrt{\kappa_A}
\frac{g}{\Omega}
 e^{-\kappa_A t/4}
\sin(\Omega t),
\qquad0<t<T_*.
}
$$

### Passive tail

$$
\boxed{
f_{\rm full}(t)
=
\sqrt{\kappa_A}
 e^{-\kappa_A T_*/4}
 e^{-\kappa_A(t-T_*)/2},
\qquad t>T_*.
}
$$

The encoder precursor and passive tail are therefore not two unrelated signals. They are two pieces of one normalized causal output mode generated by the local source input.

---

# 11. Exact local-input → gravitational-output pure-loss channel

The gravitational output obeys

$$
 b_g^{\rm out}(t)
=b_g^{\rm in}(t)
+\sqrt{\kappa_{g,A}}\,a(t).
$$

Project onto the normalized full mode:

$$
\boxed{
B_g^{\rm out}[f_{\rm full}]
=\int_0^\infty dt\,
 f_{\rm full}^*(t)b_g^{\rm out}(t).
}
$$

The coefficient of the local input operator $d(0)$ is

$$
\sqrt{\kappa_{g,A}}
\int_0^\infty dt\,
 f_{\rm full}^*(t)h(t).
$$

Using

$$
f_{\rm full}=i\sqrt{\kappa_A}h,
$$

and

$$
\kappa_A\int|h|^2dt=1,
$$

its magnitude is

$$
\boxed{
\sqrt{\frac{\kappa_{g,A}}{\kappa_A}}.
}
$$

Define

$$
\boxed{
\eta_g
=\frac{\kappa_{g,A}}{\kappa_A}.}
$$

Then

$$
\boxed{
B_g^{\rm out}[f_{\rm full}]
=e^{i\phi}\sqrt{\eta_g}\,d(0)
+\sqrt{1-\eta_g}\,v,
}
$$

where $v$ is a canonical vacuum mode assembled from the gravitational input vacuum and the other source vacuum ports.

Therefore the **complete local-input → matched gravitational-output channel is exactly**

$$
\boxed{
\mathcal L_{\eta_g},
}
$$

independent of the swap rate $g$.

The role of $g$ is to change the temporal waveform and the partition between precursor and passive tail, not the total gravitational branching fraction.

---

# 12. Information distribution among source output ports

For any output port $j$,

$$
\boxed{
\eta_j=\frac{\kappa_j}{\kappa_A}.}
$$

The matched full temporal mode in that port receives the local input with amplitude

$$
\sqrt{\eta_j}.
$$

The branching fractions satisfy

$$
\boxed{
\sum_j\eta_j=1.}
$$

Thus the arbitrary source input is distributed unitarily among the physical output channels.

For a purely gravitational source,

$$
\boxed{
\eta_g=1,}
$$

and the complete local bosonic input is eventually mapped into one outgoing gravitational temporal mode, up to a known phase.

This statement includes the encoding precursor and passive tail together.

---

# 13. Encoder precursor fraction

The norm of the full temporal mode inside the encoding interval is

$$
\epsilon_{\rm pre}
=\int_0^{T_*}|f_{\rm full}(t)|^2dt.
$$

Using the exact internal-mode conservation identity,

$$
\boxed{
\epsilon_{\rm pre}
=1-e^{-\kappa_A T_*/2}.}
$$

The passive tail carries

$$
\boxed{
1-\epsilon_{\rm pre}
=e^{-\kappa_A T_*/2}.}
$$

For

$$
\kappa_A\ll g,
$$

$$
\boxed{
\epsilon_{\rm pre}
=\frac{\pi\kappa_A}{4g}
+O\left(\frac{\kappa_A^2}{g^2}\right).
}
$$

The local encoder can therefore be made fast enough that the canonical passive exponential tail dominates the normalized source mode while the precursor remains fully accounted for.

---

# 14. Receiver driven by the complete causal mode

After retarded free-space propagation, use

$$
f_R(t)=f_{\rm full}(t-R/c)\Theta(t-R/c)
$$

up to the carrier phase and normalized spatial storage amplitude.

For receiver useful loading rate

$$
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B},
$$

the local incident-mode → receiver transfer parameter is

$$
\boxed{
\tau_{\rm full}(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}
 f_{\rm full}(s)
\right|^2.
}
$$

For vacuum ordinary source ports, the complete local-memory → receiver Gaussian channel is therefore

$$
\boxed{
\Phi_{d\to B}(t)
=
\Phi_{\eta_g\tau_{\rm full}(t),\,m_B(t)}.
}
$$

Hence

$$
\boxed{
\Phi_{d\to B}(t)\text{ is non-EB}
\iff
\eta_g\tau_{\rm full}(t)>m_B(t).
}
$$

This is now a genuine end-to-end Gaussian channel from a localized bosonic input mode, not merely a receiver channel conditioned on a pre-existing mechanical branch state.

---

# 15. Exact matched-linewidth receiver response after the encoder

For a compact analytic benchmark, take

$$
\boxed{
\kappa_A=\kappa_B=\kappa.}
$$

Define receiver-local time after the encoder handoff

$$
\tau=t-T_*,
$$

and

$$
x=\kappa\tau.
$$

Let

$$
\boxed{
r=e^{-\kappa T_*/4}.}
$$

The receiver convolution accumulated during the encoding interval is

$$
I_*
=\int_0^{T_*}ds\,
 e^{-\kappa(T_*-s)/2}
 f_{\rm full}(s).
$$

Using the exact controller-empty root,

$$
\boxed{
I_*
=
\frac{\sqrt\kappa}{g}
 e^{-\kappa T_*/2}
\left[
1+\frac{\kappa}{2g}
 e^{\kappa T_*/4}
\right].
}
$$

Define the dimensionless precursor-loading amplitude

$$
\boxed{
A
=\sqrt\kappa I_*
=
\frac{\kappa}{g}
 e^{-\kappa T_*/2}
\left[
1+\frac{\kappa}{2g}
 e^{\kappa T_*/4}
\right].
}
$$

For $t\ge T_*$,

$$
\boxed{
\sqrt\kappa
\int_0^t ds\,
 e^{-\kappa(t-s)/2}
 f_{\rm full}(s)
=
 e^{-x/2}(A+rx).
}
$$

Therefore

$$
\boxed{
\tau_{\rm full}(T_*+\tau)
=
\frac{\kappa_\Delta}{\kappa}
 e^{-x}(A+rx)^2.
}
$$

This is the exact post-encoder matched-linewidth loading curve for the complete normalized local-input waveform.

---

# 16. Exact maximum

For

$$
A<2r,
$$

the post-encoder maximum occurs at

$$
\boxed{
x_*=2-\frac{A}{r}.}
$$

The maximum is

$$
\boxed{
\tau_{\rm full}^{\max}
=
4e^{-2}
\frac{\kappa_\Delta}{\kappa}
 r^2e^{A/r}.
}
$$

The pure exponential-tail benchmark is

$$
\tau_{\exp}^{\max}
=4e^{-2}\frac{\kappa_\Delta}{\kappa}.
$$

Thus the exact ratio is

$$
\boxed{
\frac{\tau_{\rm full}^{\max}}
{\tau_{\exp}^{\max}}
=r^2e^{A/r}.
}
$$

---

# 17. Fast-encoder expansion

Let

$$
\delta=\kappa/g\ll1.
$$

Then

$$
\boxed{
gT_*
=\frac\pi2+rac\delta4+O(\delta^2),}
$$

$$
\boxed{
r
=1-\frac\pi8\delta+O(\delta^2),}
$$

$$
\boxed{
A
=\delta+O(\delta^2).}
$$

Therefore

$$
\boxed{
x_*
=2-\delta+O(\delta^2),}
$$

and

$$
\boxed{
\frac{\tau_{\rm full}^{\max}}
{\tau_{\exp}^{\max}}
=
1+\left(1-\frac\pi4\right)
\frac\kappa g
+O\left(\frac{\kappa^2}{g^2}\right).
}
$$

Since

$$
1-\frac\pi4
\simeq0.214602,
$$

the complete encoder precursor changes the optimized receiver loading only at relative order

$$
O(\kappa/g).
$$

For the chosen phase convention it slightly **increases** the maximum because the coherent precursor begins loading the receiver before the passive tail is fully established.

The crucial result is not the sign but the controlled scaling.

---

# 18. Causal meaning

The local bosonic input mode exists in the source laboratory before the gravitational signaling operation.

The causal clock begins when the local swap interaction is enabled.

Before its future light cone reaches the receiver, microcausality implies that the receiver state is independent of the input state in $d$.

After causal arrival, the exact retarded waveform is the propagated version of

$$
f_{\rm full}(t),
$$

including the short encoding precursor.

Thus the same physical protocol now supplies both

1. a genuinely local arbitrary quantum channel input; and
2. the explicit source waveform used in the receiver calculation.

No pre-existing branch-displaced mechanical source is needed for the fundamental channel definition.

---

# 19. Gravitationally dark input-memory requirement

For the strongest operational interpretation, choose the local memory encoding so that the logical/input alternatives do not themselves produce the far-field gravitational signal being tested before the swap.

For the binary coherent probe, the two memory states $|+\alpha\rangle_d$ and $|-\alpha\rangle_d$ have equal energy.

A compact internal mode whose opposite coherent phases have the same branch energy density/mass multipoles is therefore preferable.

Then the source input can carry quantum phase information locally while the external gravitational source multipole remains branch common until that information is swapped into the finite-spoke mode.

A complete microscopic realization of such a dark local memory is not required for the Gaussian channel algebra, but it is the clean physical choice for the causal Gedanken protocol.

This point should be related cautiously to perturbative gravitational-splitting/localized-information results rather than to an exact factorization claim in full quantum gravity.

---

# 20. Relation to the sign-controlled controller encoder

`EXACT_LOCAL_GAUSSIAN_SOURCE_ENCODER.md` uses

$$
H\propto\sigma_z(a^\dagger c+a c^\dagger)
$$

to create the specific $|\pm\alpha\rangle$ mechanical branches from a branch-common coherent work mode while returning that work mode to vacuum.

That construction is useful when one wants an explicit source-qubit preparation mechanism.

The present ordinary swap is more fundamental for the **channel** statement because

- its input $d$ is an arbitrary bosonic quantum mode;
- it can be entangled with an untouched reference;
- it defines a standard Gaussian input→output channel;
- the local memory empties after the swap.

Use the ordinary bosonic swap as the canonical communication-channel encoder and the sign-controlled construction as a specialized preparation protocol.

---

# 21. What remains open

At the normal-mode channel level, the preparation/causality gap is now substantially closed.

Remaining physical refinements are

1. a microscopic compact realization of the local memory/source coupling;
2. a spatial stress-energy audit of the branch-common coupling switch;
3. finite-temperature noise in the input memory and swap coupler;
4. counter-rotating corrections outside
   $$g\ll\omega;$$
5. gravity-specific prior-art search for an equivalent local-memory→radiating-quadrupole→receiver channel construction.

The main end-to-end structure no longer depends on declaring a branch-displaced mechanical state as an unexplained initial condition.

---

# 22. Recommended canonical chain

For the strongest paper-level quantum-channel formulation use

$$
\boxed{
\text{local bosonic input }d
\xrightarrow{\text{local swap}}
\text{finite-spoke mode }a
\xrightarrow{\text{all source outputs}}
\text{matched graviton mode}
\xrightarrow{R/c}
\text{noisy resonant receiver}.
}
$$

At source-vacuum noise level the first two stages together reduce exactly to

$$
\boxed{
\mathcal L_{\eta_g},
\qquad
\eta_g=\kappa_{g,A}/\kappa_A,
}
$$

when the complete encoding-plus-tail gravitational temporal mode is retained.

The final receiver channel is non-entanglement-breaking when

$$
\boxed{
\eta_g\tau_{\rm full}(t)>m_B(t).
}
$$

This is the cleanest current end-to-end channel statement in the repository.
