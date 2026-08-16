# Experiment 03 — ABS Occupation / CPR Response Closure — 2026-08-15

## Purpose

The current full dynamic force uses the equilibrium current-phase relation evaluated at the instantaneous electronic temperature,

```math
I_s(\phi,t)=I_{eq}[\phi,T_e(t)].
```

Electron-electron thermalization of the graphene distribution is not sufficient by itself to justify this assumption. The occupations of the Andreev spectrum that carry the Josephson current must also evolve rapidly enough.

This checkpoint gives the minimal microscopic interpretation of the phenomenological `tau_CPR` tolerance model.

---

## 1. Supercurrent from Andreev occupations

For discrete Andreev levels `E_j(phi)` with positive-energy occupation `n_j`, the supercurrent can be written schematically as

```math
\boxed{
I_s(\phi,\{n_j\})
=\sum_j I_j^{(0)}(\phi)\,[1-2n_j],
}
```

where

```math
I_j^{(0)}(\phi)
=-\frac{2e}{\hbar}\frac{\partial E_j}{\partial\phi}
```

up to the adopted positive/negative-energy counting convention.

At thermal equilibrium,

```math
n_j=f[E_j(\phi),T],
```

which recovers the usual equilibrium CPR weighting by `tanh(E_j/2kT)`.

---

## 2. Minimal occupation kinetics

Introduce a relaxation-time kinetic model

```math
\boxed{
\dot n_j
=-\frac{
 n_j-f[E_j(\phi(t)),T_e(t)]
}{\tau_j}.
}
```

This equation is only a reduced kinetic orientation model. Real processes can include parity constraints, continuum exchange, electron-phonon transitions, microwave-induced transitions, Landau-Zener dynamics and energy-dependent relaxation times.

It is nevertheless sufficient to expose the key assumption:

```text
instantaneous equilibrium CPR
<=>
tau_j is short compared with every timescale on which the equilibrium
occupation target changes along the write trajectory.
```

---

## 3. Reduction to one effective CPR response time

Suppose, as a screening approximation,

```text
- the relevant current-carrying levels have similar relaxation time tau_CPR;
- their equilibrium-current amplitudes are linearized about the trajectory;
- redistribution among levels can be represented by one dominant occupation mode.
```

Then the total supercurrent deviation obeys approximately

```math
\boxed{
\tau_{CPR}\dot I_s+I_s
\simeq I_{eq}[\phi(t),T_e(t)].
}
```

In the normalized rf-SQUID variables this becomes exactly the phenomenological response-lag model implemented in

```text
calculations/cpr_relaxation_tolerance.py.
```

Thus `tau_CPR` should be interpreted as an **effective Andreev/supercurrent occupation-response time**, not as an electromagnetic filter time.

---

## 4. Frequency-domain meaning

For a small harmonic perturbation around a fixed operating point,

```math
\delta I_{eq}\propto e^{-i\omega t},
```

the one-pole model gives

```math
\boxed{
\frac{\delta I_s}{\delta I_{eq}}
=\frac{1}{1-i\omega\tau_{CPR}}.
}
```

Hence

```math
|H_{CPR}|=rac{1}{\sqrt{1+(\omega\tau_{CPR})^2}},
```

and phase lag

```math
\phi_{CPR}=\tan^{-1}(\omega\tau_{CPR}).
```

The relevant Experiment-03 frequencies are not only the inverse thermal rise `~1/tau_r`; the phase mode itself is in the tens-of-GHz range and the equilibrium CPR target changes strongly as both `phi(t)` and `T_e(t)` evolve.

Therefore a response time that appears short relative to `20 ps` can still generate substantial phase lag at `20–30 GHz`.

---

## 5. Two limiting physical regimes

### Fast occupation relaxation

```math
\omega\tau_{CPR}\ll1.
```

Then

```text
occupations track the hot distribution;
instantaneous equilibrium CPR is approximately valid;
thermal suppression of the Josephson landscape occurs promptly.
```

### Slow occupation relaxation

```math
\omega\tau_{CPR}\gtrsim1.
```

Then

```text
Andreev occupations retain memory of the colder state;
the supercurrent can remain larger than the equilibrium hot CPR would predict;
barrier suppression and reformation phase are shifted;
energy-density capture lobes move or disappear.
```

The direction of the effect is not generically monotonic because delayed current also changes the dynamical phase accumulated before recovery.

---

## 6. Why this gate is stronger than generic graphene thermalization

Sub-picosecond electron-electron redistribution can establish a hot electronic distribution without guaranteeing that the current-carrying Andreev occupations immediately reach the corresponding equilibrium values.

The detector requires the chain

```text
photon energy deposition
 -> electronic distribution changes
 -> Andreev occupations / spectral current respond
 -> CPR changes
 -> rf-SQUID landscape changes.
```

The slowest relevant link controls the effective write rise seen by the phase coordinate.

Therefore literature on generic graphene hot-carrier relaxation is insufficient to validate the CPR assumption. A junction-specific occupation/admittance calculation or measurement-equivalent theoretical bound is required.

---

## 7. Relation to intrinsic admittance

The CPR-response gate and the intrinsic-admittance gate are not independent.

The same microscopic transitions that relax Andreev occupations generally contribute to the dissipative dynamic susceptibility

```math
\operatorname{Re}Y_{JJ}(\omega,\phi,T_e).
```

Causality and fluctuation-dissipation therefore imply a three-way linkage:

```text
rapid occupation relaxation
<-> dissipative susceptibility
<-> intrinsic fluctuations.
```

A model that demands extremely fast `tau_CPR` while simultaneously assuming negligible `Re Y_JJ` would require microscopic justification.

This is potentially a central feasibility tradeoff for Experiment 03.

---

## 8. Immediate decision rule

The current numerical tolerance workflow scans

```text
tau_CPR = 0 ... 150 ps
```

under the otherwise best external-bath candidate.

Interpretation:

```text
capture remains robust for tau_CPR ~ tens of ps
 -> microscopic occupation kinetics are unlikely to be the dominant gate;

capture collapses for tau_CPR of only a few ps
 -> architecture requires exceptionally fast ABS/supercurrent relaxation,
    and microscopic Y_JJ + occupation kinetics become the next no-go test.
```

Survival of the phenomenological lag test is necessary but not sufficient because the lag model itself does not include the additional FDT noise associated with the relaxation channel.

---

## Status

**Derived kinetic interpretation / mandatory feasibility gate.**

No novelty claim. No microscopic relaxation time is assumed.

**GO for continued theory. NO-GO for manuscript.**
