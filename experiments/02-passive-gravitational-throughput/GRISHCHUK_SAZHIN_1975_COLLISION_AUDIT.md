# Grishchuk–Sazhin 1975 Collision Audit

## Source

L. P. Grishchuk and M. V. Sazhin, **“Excitation and detection of standing gravitational waves,”** Sov. Phys. JETP 41, 787–793 (1975/1976 English translation of ZhETF 68, 1569–1582).

Primary full text inspected from the JETP archive.

---

## 1. Why this source is closer prior art than the initial Experiment 02 audit assumed

This paper does not merely discuss a gravitational receiver supplied with an external incident field. It explicitly constructs a complete laboratory system containing

```text
EM resonator radiator
-> generated gravitational field
-> EM resonator detector
-> resonant detector response
-> signal/noise condition
-> combined system-parameter limitation.
```

The authors state at the outset that the scheme includes both a source and a receiver. They then calculate a concrete toroidal electromagnetic radiator, the gravitational field it generates, the resonant response of an electromagnetic detector, and finally a constraint involving parameters of the complete system.

Therefore Experiment 02 must not claim novelty merely for

- including both a gravitational source and receiver;
- deriving a relation between source and receiver parameters;
- obtaining an end-to-end limitation for a gravitational laboratory link;
- using wave-zone propagation in a complete generator-detector calculation.

Those elements existed by 1975.

---

## 2. Architecture and regime

The Grishchuk–Sazhin source is an **active electromagnetic toroidal resonator**, not passive compact nonrelativistic mechanical matter.

Its gravitational radiation is coherently focused by the spatially extended source to produce a standing cylindrical gravitational field near the symmetry axis. The detector is another electromagnetic resonator placed in this focal region.

The authors emphasize coherent source volume, phase/retardation engineering, and resonant enhancement. The radiator can be actively replenished with electromagnetic energy when its finite Q would otherwise limit the experiment duration.

For their final feasibility estimate, radiator and detector are placed near the **boundary of the wave zone**, with their physical sizes themselves of order the gravitational wavelength. The paper explicitly notes that wave-zone formulas are being used near the limit of their applicability and that Newtonian effects become comparable when separation approaches a wavelength.

This is therefore materially outside the Experiment 02 theorem class:

```text
Grishchuk–Sazhin:
active EM + extended/coherent aperture + focal standing field + R ~ lambda

Experiment 02:
passive linear bosonic matter + compact quadrupole + direct one-way propagating wave zone + kR >> 1.
```

---

## 3. End-to-end limitation actually derived

The detector calculation gives a resonant electromagnetic response whose amplitude contains the gravitational field amplitude `A` and detector quality factor `Q`. The signal accumulation time is of order

```math
T\sim\frac{2Q}{\Omega}.
```

The authors derive detection conditions from the requirement that the generated detector signal exceed their assumed electromagnetic quantum-noise scale.

They then make the crucial end-to-end step: because the gravitational amplitude `A` and frequency are themselves fixed by the radiator, they state that the detector requirement produces **general limitations on the properties of the system as a whole**.

At the wave-zone boundary they substitute the radiator amplitude into the detector condition and obtain a combined relation of the schematic form

```math
\lambda^{5/2} E^2 H Q
\sim
\text{constant}/G,
```

where `E` characterizes the radiator electromagnetic field, `H` the detector field, `Q` the detector resonant quality factor, and `lambda` the gravitational wavelength.

Thus a source-to-receiver constraint is unequivocally historical prior art.

---

## 4. Why this does not reproduce Experiment 02

Despite the important collision above, the 1975 result is structurally different from the Experiment 02 theorem.

### It is not a frequency-integrated transfer norm

There is no analogue of

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int d\omega\,
\operatorname{Tr}[T^\dagger(\omega)T(\omega)].
```

The calculation is a resonant signal/noise feasibility condition for a specific active architecture.

### It does not eliminate Q through a passive spectral-resource theorem

On the contrary, large detector Q is an explicit resource in the final feasibility condition. The paper exploits resonant accumulation rather than proving that peak gain must be paid for by shrinking integrated bandwidth.

### It does not bound both endpoint gravitational coupling resources by a matter sum rule

There is no source/receiver analogue of

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
```

The source is driven electromagnetic field energy, and the detector uses externally maintained electromagnetic fields.

### It does not contain the passive H2 cut set

There is no basis-independent bound by

```math
\eta_{\max}
\min[\operatorname{Tr}\Gamma_{g,A},
     \operatorname{Tr}\Gamma_{g,B}].
```

### It does not contain the compact TT singular-value ceiling

The geometry is an extended coherent toroidal radiator creating a focal standing wave. It is specifically an architecture that lies outside the compact-quadrupole directivity ceiling used by Experiment 02.

---

## 5. Novelty consequence

After full-text inspection, the novelty boundary must be narrower than “two-ended passive gravitational transduction closure” if that phrase is read broadly.

The following concepts are definitely historical:

```text
complete gravitational generator + detector
source-to-receiver parameter relation
wave-zone generator-detector calculation
end-to-end feasibility limitation
resonant Q-assisted receiver response.
```

The candidate Experiment 02 contribution that survives is instead the specific theorem structure

```text
frequency-integrated coherent transfer
-> passive selected-port H2 cut set
-> minimum of source/receiver gravitational coupling traces
-> independent EWSR closure of both traces
-> normalized compact TT propagation singular-value ceiling.
```

No equivalent statement was found in the inspected Grishchuk–Sazhin paper.

---

## 6. Referee-safe positioning after this collision

A safer manuscript statement is:

> Earlier laboratory gravitational-wave studies already analyzed complete generator–detector systems and derived architecture-specific source-to-receiver feasibility constraints. Here we ask a different question: for a direct compact wave-zone link whose matter interfaces are passive, what upper bound follows for the frequency-integrated coherent transfer when the gravitational oscillator-strength resources of both endpoints are bounded microscopically?

A stronger but still restrained description of the candidate contribution is:

> We combine established passive linear-system identities, mass-quadrupole spectral sum rules at both matter interfaces, and a normalized compact-TT propagation bound to obtain a Q-independent frequency-integrated ceiling for direct passive gravitational transduction.

Do not use “first end-to-end gravitational bound,” “first source-receiver gravitational link theorem,” or equivalent language.

---

## 7. Updated collision status

```text
GENERATOR + RECEIVER IN ONE CALCULATION:   COLLISION — HISTORICAL
END-TO-END SYSTEM PARAMETER LIMITATION:    COLLISION — HISTORICAL
Q-ASSISTED RESONANT RECEIVER:              COLLISION — HISTORICAL
PASSIVE H2 INTEGRATED CUT SET:             NO COLLISION FOUND HERE
BOTH-ENDPOINT EWSR CLOSURE:                NO COLLISION FOUND HERE
COMPACT TT SINGULAR-VALUE RESOURCE SANDWICH:
                                           NO COLLISION FOUND HERE
EXPERIMENT 02 PHYSICS DEFECT:              NONE FOUND FROM THIS SOURCE
```

The highest-priority unresolved historical source remains Hirakawa, Narihara, and Fujimoto (1976), because its abstract explicitly advertises emission, reception, directivity, and eigenmode antenna theory in one framework.
