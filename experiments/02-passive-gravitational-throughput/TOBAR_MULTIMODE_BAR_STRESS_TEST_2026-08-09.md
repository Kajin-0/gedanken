# Tobar–Pikovski–Tobar Multimode-Bar Stress Test — 2026-08-09

## Purpose

Test Experiment 02 against a modern design that appears, at first reading, to attack its central physical claim.

Tobar, Pikovski, and Tobar propose a strongly coupled multimode resonant bar in which several normal modes are described as retaining the gravitational-wave coupling of the largest (tonne-scale) mass while acquiring effective masses comparable to much smaller terminal elements. Their paper emphasizes that several slightly detuned normal modes can each have a graviton absorption rate set by the large primary mass.

That sounds superficially like the forbidden strategy

```text
one large gravitational oscillator strength
-> split into N passive normal modes
-> each mode retains the original strength
-> total gravitational resource grows ~ N.
```

If that interpretation were correct, it would be a direct counterexample to the Experiment 02 cumulative resource theorem.

It is not.

---

## 1. The published multimode Hamiltonian

The three-mode lumped system is driven only through the first coordinate `x_1`,

```math
H
=H_{\rm mech}+g(t)x_1.
```

After diagonalizing the coupled mechanical system, the paper expands the first coordinate in normal coordinates and obtains the quantized interaction

```math
\hat H_{\rm int}
=\sum_j
\frac{P_{1j}}{\pi^2}
L\ddot h(t)
\sqrt{\frac{\hbar M}{\omega_j}}
(\hat b_j^\dagger+\hat b_j).
```

The stimulated graviton absorption rate of mode `j` is then

```math
\boxed{
\Gamma_{{\rm stim},j}
=
P_{1j}^2
\frac{v_s^2}{4\pi^3\hbar}
M h^2.
}
```

The paper explicitly notes that the multimode result differs from the single-mode bar rate by the squared normal-coordinate conversion factor `P_{1j}^2`.

This factor is the key.

---

## 2. Why the apparent N-fold enhancement does not occur

The normal-mode transformation is obtained by diagonalizing a real positive quadratic mechanical Hamiltonian. In mass-weighted coordinates it is an orthogonal transformation.

Let `y_1` denote the mass-weighted coordinate corresponding to the directly driven large element and `q_j` the orthonormal normal coordinates. Then

```math
y_1=\sum_j P_{1j}q_j,
```

with

```math
\boxed{
\sum_j |P_{1j}|^2=1.
}
```

Therefore the squared gravitational drive amplitudes obey

```math
\boxed{
\sum_j |g_j|^2
=|g_{\rm bare}|^2
\sum_j|P_{1j}|^2
=|g_{\rm bare}|^2.
}
```

For the stimulated rates displayed by Tobar et al., if the frequencies are close enough that the common prefactor may be treated as the same across the split multiplet,

```math
\boxed{
\sum_j\Gamma_{{\rm stim},j}
=
\Gamma_{\rm bare}.
}
```

More generally, if the frequencies differ, the transformation still redistributes the drive norm; frequency weighting must be retained mode by mode. Nothing in the canonical transformation creates new oscillator strength.

Thus the phrase that the modes "retain" the coupling of the largest mass means that individual `P_{1j}` can remain order unity for a small number of strongly hybridized modes. It cannot mean that an arbitrarily large number of orthogonal modes each acquire `P_{1j}=1`.

For `N` comparable bright modes, orthogonality instead requires a characteristic scaling

```math
|P_{1j}|^2\sim\frac1N,
```

up to nonuniform redistribution.

---

## 3. Relation to the Experiment 02 trace resource

Experiment 02 uses the basis-invariant gravitational damping trace

```math
\operatorname{Tr}\Gamma_g
=\operatorname{Tr}(G^\dagger G).
```

Under an internal unitary/orthogonal change of mechanical basis

```math
G\mapsto GU,
```

one has

```math
\operatorname{Tr}[(GU)^\dagger(GU)]
=
\operatorname{Tr}(U^\dagger G^\dagger G U)
=
\operatorname{Tr}(G^\dagger G).
```

The Tobar multimode transformation is exactly this kind of operation at the level of the driven mechanical coordinate.

Their factors `P_{1j}` therefore give a concrete contemporary example of the abstract statement

> coherent passive mode hybridization can redistribute a gravitationally bright coordinate among several normal modes, but it cannot increase the total squared coupling trace.

This is one of the main physical messages of Experiment 02.

---

## 4. Why the Tobar proposal can still be advantageous

There is no conflict between the two works because Tobar et al. optimize a different resource.

Their key gain is **measurement transduction**. The gravitational field drives the large first mass, but strong mechanical hybridization makes the resulting normal modes observable through an extremely small terminal mass. Their optomechanical coupling to the end element scales approximately as

```math
g_j
\propto
P_{Nj}\sqrt{\frac{1}{m_N\omega_j}},
```

and they emphasize enhancements of order

```math
\sqrt{m_1/m_N}
```

(or `m_1/m_N` for certain quadratic readouts) relative to reading the largest mass directly.

That improves the ability to resolve the absorbed energy quantum after the GW interaction.

Experiment 02 does **not** say passive internal engineering cannot improve readout, noise matching, peak response, or experimental observability. It says it cannot increase the cumulative gravitational oscillator strength available at the external gravitational interface beyond the matter-resource ceiling.

In compact form:

```text
Tobar multimode chain:
    improves graviton -> measurable end-mass transduction

Experiment 02 bound:
    constrains total external GW -> matter oscillator strength
```

These statements are compatible.

---

## 5. Frequency sweep versus spectral-area theorem

Tobar et al. exploit several slightly detuned normal modes against a chirping neutron-star signal. Successive modes can therefore encounter different portions of the incident waveform.

This does not imply multiplication of the passive spectral resource. It is precisely the situation for which a frequency-integrated metric is preferable to peak efficiency:

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
```

Splitting one bright coordinate among several resonances can improve spectral coverage and matching to a chirp. The integrated oscillator-strength budget remains constrained.

This is analogous to redistributing a fixed spectral weight across several poles rather than creating additional total weight.

---

## 6. Important limitation of this comparison

The published Tobar stimulated rate is for a prescribed incident GW strain and a detector/readout problem. Experiment 02 concerns the full passive source--propagation--receiver link and an energy-normalized transfer metric.

Therefore one should not identify their `Gamma_stim` numerically with the Experiment 02 `kappa_g` or `Gamma_coh` without a separate normalization calculation.

The comparison here is narrower and robust:

```text
normal-mode participation factors redistribute the driven-coordinate norm;
they do not create N independent copies of the original coupling.
```

That statement follows directly from the canonical normal-mode transformation used in their own Hamiltonian.

---

## 7. Stress-test outcome

```text
APPARENT MANY-MODE COUNTEREXAMPLE:        NO
EACH MODE HAS PARTICIPATION P_1j:         YES
SUM_j |P_1j|^2 FOR COMPLETE BASIS:        1
PASSIVE HYBRIDIZATION CREATES RESOURCE:   NO
READOUT / TRANSDUCTION CAN IMPROVE:       YES
SPECTRAL COVERAGE CAN IMPROVE:            YES
EXPERIMENT 02 TRACE PRINCIPLE:            SUPPORTED
DIRECT NUMERICAL RATE IDENTIFICATION:     NOT CLAIMED
```

## 8. Publication value

This is a stronger motivating example than an abstract statement that "adding modes does not help."

A recent graviton-detection proposal explicitly uses several strongly hybridized mechanical modes, each inheriting substantial coupling from a massive gravitationally driven element. Experiment 02 explains the resource accounting behind that design:

> the hybrid modes can all be useful, but their gravitational brightness is a partition of the same underlying passive coupling resource.

The manuscript should consider mentioning this example briefly in the discussion, with careful wording that does not criticize or contradict the Tobar proposal.

## Reference

G. Tobar, I. Pikovski, and M. E. Tobar, **"Detecting kHz gravitons from a neutron star merger with a multi-mode resonant mass detector,"** Classical and Quantum Gravity **42**, 055017 (2025), arXiv:2406.16898.
