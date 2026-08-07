# Compact-Object Receiver Tradeoff

**Timestamp:** 2026-08-07 18:00 EDT  
**Status:** Conceptual receiver-class comparison. This note shows why the Planck-bandwidth result is not universal and identifies the next fundamental receiver tradeoff.

## 1. Weakly gravitating bound states are not the end of the story

The Planck-area literature implies for weak quantum bound-state gravitational transitions a scaling

$$
\frac{\Gamma_g}{\omega}
\sim(k\ell_P)^2,
$$

so their natural gravitational linewidth is fantastically narrow.

That does **not** imply that every object coupled to gravity must have a Planck-suppressed fractional linewidth.

Strongly self-gravitating compact objects provide an immediate counterexample class.

---

## 2. Schwarzschild black-hole benchmark

The fundamental Schwarzschild $l=2$ gravitational quasinormal frequency is conventionally written approximately as

$$
M\omega
\simeq
0.3737-0.0890i
$$

in geometric units.

The corresponding modal quality factor is only

$$
\boxed{
Q_{\rm BH}
\sim
\frac{\operatorname{Re}\omega}
{2|\operatorname{Im}\omega|}
\sim2.1.
}
$$

Thus

$$
\boxed{
\frac{\Gamma_g}{\omega}
=O(10^{-1})
}
$$

rather than

$$
O[(k\ell_P)^2].
$$

A black hole therefore demonstrates that the Planck-suppressed fractional linewidth is a property of weakly gravitating bound receivers, not a universal property of gravitational interaction.

The natural length scale is

$$
R\sim r_s,
$$

and the natural mode frequency is

$$
\omega\sim c/r_s,
$$

so

$$
kR=O(1).
$$

Peak gravitational absorption and scattering areas are correspondingly of order the geometric/horizon area rather than Planck area.

---

## 3. Why a black hole is not automatically the ideal Gedanken receiver

A large gravitational linewidth is only one resource.

Experiment 01 requires a receiver that can

1. acquire the incoming branch-dependent gravitational state coherently;
2. retain source–receiver entanglement long enough to verify it;
3. support a controllable eraser or joint witness;
4. expose the relevant receiver degree of freedom to an observer.

A horizon behaves naturally as an absorber/sink. Treating black-hole microstates as the receiver Hilbert space raises issues absent from the ordinary oscillator memory:

- operational access to the stored state;
- retrieval/readout through Hawking radiation or another channel;
- scrambling among enormous internal degrees of freedom;
- horizon thermality;
- defining the source–receiver bipartition in quantum gravity.

Thus

$$
\boxed{
\text{large gravitational coupling}
\not\Rightarrow
\text{useful controllable quantum memory}.
}
$$

---

## 4. Hawking occupation at the Schwarzschild $l=2$ scale

For a Schwarzschild black hole,

$$
k_BT_H
=\frac{\hbar c^3}{8\pi GM}.
$$

Using

$$
M\omega_R\simeq0.3737
$$

in geometric units,

$$
\frac{\hbar\omega_R}{k_BT_H}
\simeq
8\pi(0.3737)
\simeq9.39.
$$

A naive Bose occupation at that frequency is therefore

$$
\boxed{
\bar n_H(\omega_R)
\sim
\frac1{e^{9.39}-1}
\sim8\times10^{-5}.
}
$$

So the immediate obstacle is not simply “the black hole is thermally full of resonant gravitons.” The harder issue is that the absorbing horizon/internal state is not a simple accessible quantum memory mode.

Greybody factors, rotation, superradiance, and the actual open-system decomposition would be needed for a serious black-hole receiver model.

---

## 5. Neutron-star-like intermediate regime

Compact stars provide a useful intermediate thought experiment.

Typical neutron-star fluid $f$-modes lie in the kilohertz range and can damp through gravitational-wave emission on subsecond-to-second timescales.

Therefore their gravitational fractional linewidth is vastly larger than that of laboratory bound states while still much narrower than a black-hole quasinormal mode.

A rough order-of-magnitude example,

$$
f\sim2\,\mathrm{kHz},
\qquad
\tau_g\sim0.1\text{--}1\,\mathrm s,
$$

gives

$$
Q_g\sim\frac{\omega\tau_g}{2}
\sim10^3\text{--}10^4.
$$

Thus compactness can indeed buy enormous gravitational oscillator strength.

But realistic neutron stars are thermally hot on the quantum scale of a kHz oscillator. Since

$$
\frac{\hbar\omega}{k_B}
\sim10^{-7}\,\mathrm K
$$

at kilohertz frequencies, an astrophysical temperature of even

$$
10^6\,\mathrm K
$$

corresponds to occupation of order

$$
\boxed{
\bar n\sim10^{13}.
}
$$

Any receiver mode strongly equilibrated with such internal matter is overwhelmingly classicalized even though its gravitational coupling is strong.

---

## 6. Receiver phase-space picture

The candidate receivers now populate three qualitatively different regions.

### Laboratory quantum matter

$$
\mathcal C_B\ll1,
\qquad
\beta_B\ll1.
$$

Advantages:

- state preparation and measurement are conceptually available;
- thermal occupation may be reduced;
- eraser operations are imaginable.

Disadvantage:

$$
\kappa_g/\kappa_{\rm tot}\ll1.
$$

### Compact-star collective modes

$$
\mathcal C_B=O(10^{-1}),
\qquad
\beta_B=O(10^{-1}\text{--}1).
$$

Advantages:

- much larger gravitational branching;
- substantial radiative bandwidth.

Disadvantages:

- huge environmental Hilbert space;
- enormous thermal occupation in realistic settings;
- essentially no microscopic quantum control.

### Black-hole/gravity-dominated modes

$$
\mathcal C_B=O(1),
\qquad
\beta_B=O(1),
\qquad
Q_g=O(1).
$$

Advantage:

- gravitational coupling and bandwidth are no longer small.

Disadvantage:

- receiver degrees of freedom are horizon/geometry degrees;
- storage is strongly scrambling/absorptive;
- operational readout and erasure become the central problem.

---

## 7. New receiver triangle

The strongest receiver problem is therefore naturally three-dimensional.

Define conceptually:

### Gravitational capture

$$
\mathcal G
\sim
\frac{\kappa_\Delta}{\kappa_{\rm tot}}.
$$

### Coherence

A measure of how little uncontrolled noise/decoherence enters the stored mode, e.g.

$$
\mathcal C
\sim
1-\frac{\Gamma_{\rm noise}}{\kappa_\Delta}
$$

within the Gaussian model.

### Accessibility

$$
\mathcal A
$$

measures whether the receiver degree of freedom can be coherently manipulated/read out sufficiently to perform the source–receiver witness or eraser.

A useful gravitational quantum receiver needs all three:

$$
\boxed{
\mathcal G\text{ large},
\qquad
\mathcal C\text{ large},
\qquad
\mathcal A\text{ non-negligible}.
}
$$

Weak matter tends to have

$$
(\mathcal G\ll1,\ \mathcal C\text{ potentially large},\ \mathcal A\text{ large}),
$$

while strongly gravitating objects tend toward

$$
(\mathcal G\text{ large},\ \mathcal C/\mathcal A\text{ problematic}).
$$

This is a more general formulation than a universal Planck-area receiver bound.

---

## 8. Consequence for the strongest-path research program

The passive nonrelativistic vacuum ceiling remains highly relevant to laboratory matter,

$$
\mathcal N_{\max}^{\rm WZ}
\lesssim
\frac{25\mathcal O}{24\zeta^2}
Q_B\mathcal C_B\beta_B^3,
$$

but it should **not** be generalized to all gravitational receivers.

The strongest next theoretical question is instead:

> **Is there a general information-theoretic tradeoff between gravitational capture strength and accessible recoverable coherence for passive receivers, including relativistic/strong-gravity systems?**

A result of that type could unify

- laboratory quantum resonators;
- relativistic field modes;
- compact stars;
- black-hole-like absorbers.

---

## 9. Immediate next step

1. Formulate accessibility operationally through a channel from the gravitationally absorbing receiver degree of freedom to a controllable readout register.
2. Treat the total gravitational experiment as a **two-stage channel**:
   $$
   \text{source}\to\text{gravitational receiver mode}\to\text{accessible register}.
   $$
3. Derive whether the exact binary-coherent Gaussian theorem composes into a simple criterion for the complete chain.
4. Test the result on:
   - weak material receiver;
   - thermally occupied compact-star mode;
   - idealized black-hole absorber followed by a noisy retrieval channel.

The relevant question is no longer merely whether a system absorbs gravitons efficiently, but whether the absorbed branch information remains **recoverable quantum information**.