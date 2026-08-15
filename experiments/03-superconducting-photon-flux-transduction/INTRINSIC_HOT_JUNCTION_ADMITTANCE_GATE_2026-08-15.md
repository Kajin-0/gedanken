# Experiment 03 — Intrinsic Hot-Junction Admittance Gate — 2026-08-15

## Why this gate exists

The current nonlinear stationary-bath TWA/GLE model uses one engineered external passive environment at the cold bath temperature. That model is internally consistent for the external port, but it does **not** yet include dissipative admittance generated inside the photon-heated Josephson weak link itself.

This omission matters because the favorable write trajectory heats the electronic weak-link degree of freedom to roughly `0.8–0.9 K` and passes through the phase region near `phi~pi`, where high-transmission Andreev levels can become very low in energy.

Therefore the current `>99%` semiclassical capture region is conditional on

```text
intrinsic Re Y_JJ(omega,phi,T_e)
being small enough over the vulnerable write interval.
```

This is now a mandatory physics gate before treating the external-bath optimum as a device-level result.

---

## 1. Short-channel orientation scale

For a short superconducting channel of transmission `Tn`, the Andreev level is

```math
\boxed{
E_A(\phi)
=\Delta_{ind}
\sqrt{1-\mathcal T_n\sin^2(\phi/2)}.
}
```

This standard weak-link result is used here only as a kinematic orientation scale. The retained Experiment-03 CPR is arbitrary-length and must not be replaced wholesale by the short-channel formula.

At the crossing region `phi~pi`,

```math
E_A(\pi)
=\Delta_{ind}\sqrt{1-\mathcal T_n}.
```

A direct two-quasiparticle Andreev transition at drive frequency `f` becomes kinematically possible when

```math
2E_A\lesssim hf.
```

Hence at `phi~pi`,

```math
\boxed{
\mathcal T_n
\gtrsim
1-\left(
\frac{hf}{2\Delta_{ind}}
\right)^2.
}
```

---

## 2. Current numerical scale

For the retained `rDelta=.6` induced-gap scale,

```text
Delta_ind ~0.78 meV.
```

At the cold phase-mode frequency around

```text
f ~27 GHz,
```

```text
hf ~0.112 meV,
hf/2 ~0.056 meV,
```

so the phase-pi threshold is approximately

```math
\boxed{\mathcal T\gtrsim0.995.}
```

At `50 GHz`,

```math
\boxed{\mathcal T\gtrsim0.982}
```

is sufficient kinematically.

Ballistic graphene weak links can contain highly transmitting channels, so low-energy Andreev transitions cannot be excluded by energy scale alone.

This does **not** imply a large absorption rate. Matrix elements, finite-length spectrum, channel distribution, relaxation broadening and occupation all matter. In particular, the exact perfect-transmission limit can suppress some transition matrix elements.

---

## 3. Hot occupation is not exponentially negligible

The strongest current energy-density lobe reaches approximately

```text
T_peak ~0.886 K.
```

Then

```text
k_B T_peak ~0.076 meV.
```

For an Andreev level near the 27-GHz pair threshold,

```text
E_A ~0.056 meV,
```

so

```math
E_A/(k_BT_e)\sim0.7.
```

Such low-energy states are not in a deep frozen-occupation limit during the hot interval. Thermally occupied ABS/quasiparticle processes can therefore contribute to the dissipative ac response.

---

## 4. General FDT consequence

If the heated junction contributes intrinsic dissipative admittance

```math
G_{JJ}(\omega,\phi,T_e)
=\operatorname{Re}Y_{JJ}(\omega,\phi,T_e)>0,
```

then a local-equilibrium symmetrized fluctuation spectrum must satisfy

```math
\boxed{
S_{I,JJ}^{sym}(\omega)
=\hbar|\omega|
\coth\left(
\frac{\hbar|\omega|}{2k_BT_e}
\right)
G_{JJ}(\omega,\phi,T_e).
}
```

Thus the junction cannot be assigned intrinsic damping without its corresponding fluctuations.

The current external-bath TWA/GLE screen includes only

```text
Y_external(omega), T_bath=20 mK.
```

A device-level calculation needs

```math
\boxed{
Y_{tot}(\omega,t)
=Y_{external}(\omega)
+Y_{JJ}[\omega,\phi(t),T_e(t)]
}
```

with the associated nonstationary/open-system fluctuations treated consistently.

---

## 5. Why this is especially relevant to the write trajectory

The switching path deliberately approaches/passes the phase region around `phi~pi` because that is where the current-phase landscape softens most strongly.

That is also the region in which high-transmission Andreev levels are most likely to become low energy.

Therefore there is a possible conflict:

```text
large thermal/Josephson susceptibility near pi
        versus
low intrinsic microwave dissipation near pi.
```

This is now a first-order material/device criterion, not a secondary correction.

---

## 6. Immediate falsification strategy

Do not assume a microscopic intrinsic admittance before it is derived.

Use two levels:

### A. Parametric conductance tolerance

Add a pulse-activated intrinsic dissipative channel and determine the maximum allowed

```math
\operatorname{Re}Y_{JJ}
```

for which the current high-fidelity basin survives.

This gives a detector requirement without pretending to know the answer microscopically.

### B. Microscopic comparison

Then calculate or bound `Y_JJ(omega,phi,T_e)` from the same weak-link spectrum used for the CPR, including:

```text
channel/Andreev spectrum,
finite-length effects,
occupation,
transition matrix elements,
relaxation broadening,
continuum channels.
```

Compare the microscopic result against the tolerance from A.

If the required conductance is much smaller than unavoidable weak-link loss, the architecture fails even if the external bath is optimized.

---

## 7. Literature boundary

Frequency-dependent weak-link admittance and dissipation from Andreev/quasiparticle transitions are established Josephson physics. This gate is not a novelty route.

Relevant primary theory includes the short-weak-link admittance treatment by Kos, Nigg and Glazman and ac-response theory for SNS weak links. Their role here is to prevent the detector model from treating the Josephson element as a purely reactive CPR while simultaneously heating it into a regime where internal excitations may absorb at the phase-dynamics frequency.

---

## Current verdict

The external causal-bath optimization remains a valid **conditional** result.

But

```text
>99% stationary-bath TWA/GLE capture
```

must now be read as

```text
>99% in the model with intrinsic hot-junction dissipation omitted.
```

A microscopic or tolerance-based intrinsic-admittance gate is mandatory before the result can be promoted.

**GO for continued theory. NO-GO for manuscript.**
