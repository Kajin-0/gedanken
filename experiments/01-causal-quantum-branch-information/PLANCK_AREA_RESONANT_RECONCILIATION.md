# Planck-Area Absorption versus Resonant Gravitational Storage

**Timestamp:** 2026-08-07 18:00 EDT  
**Status:** Reconciliation of the Planck-area graviton-absorption literature with the resonant input-output receiver model used in Experiment 01.

## 1. Apparent contradiction

Two results initially appear inconsistent.

### Planck-area absorption literature

Palessandro & Sloth (2020) derive for gravitational absorption by quantum bound states a cross section of the form

$$
\boxed{
\sigma_{\rm abs}
=\tilde\kappa\,\ell_P^2,
}
$$

with

$$
\ell_P^2=\frac{\hbar G}{c^3}.
$$

Their Appendix A also emphasizes that the **frequency-averaged** absorption cross section is Planckian up to a dimensionless coefficient.

A later gravitational-atom detector calculation again finds a total absorption cross section

$$
\boxed{
\sigma_{\rm abs}^{\rm tot}
=\beta\,\ell_P^2
}
$$

with an order-unity-or-smaller dimensionless coefficient depending on the bound-state quantum numbers.

### Resonant receiver result in Experiment 01

The input-output/partial-wave analysis gives an ideal one-channel resonant **storage/absorption ceiling** for an $l=2$ gravitational transition of

$$
\boxed{
\sigma_{\rm abs,max}^{(l=2)}
=\frac{5\pi}{2k^2},
}
$$

where

$$
k=\omega/c.
$$

For ordinary frequencies,

$$
k^{-2}\gg\ell_P^2.
$$

The two expressions cannot refer to the same bandwidth/time-resolution quantity.

---

## 2. The missing variable is linewidth

The 2020 QFT calculation gives not only a Planckian cross section but also a transition rate.

In natural units their result is schematically

$$
\boxed{
\Gamma_g
=\tilde\kappa\,\ell_P^2\omega^3,
}
$$

because they define

$$
\sigma_{\rm abs}
=\frac{\Gamma_g}{\omega^3}
=\tilde\kappa\ell_P^2.
$$

Restoring $c$ only changes the placement of $c$ factors; the dimensionless fractional gravitational linewidth is

$$
\boxed{
\frac{\Gamma_g}{\omega}
\sim
\tilde\kappa\,(k\ell_P)^2.
}
$$

Thus the natural gravitational line is extraordinarily narrow.

This is exactly the scale needed to reconcile a peak area of order $k^{-2}$ with a frequency-averaged area of order $\ell_P^2$:

$$
\boxed{
\frac1{k^2}
\frac{\Gamma_g}{\omega}
\sim
\tilde\kappa\ell_P^2.
}
$$

The Planck suppression is therefore a **time-bandwidth/oscillator-strength suppression**, not necessarily a universal upper bound on the peak cross section of a perfectly resonant, perfectly mode-matched absorber.

---

## 3. Resonance-line picture

Consider one quadrupolar resonant receiver with

- gravitational input/output linewidth $\kappa_g$;
- coherent storage/shelving/internal channel $\kappa_s$.

A standard single-resonance absorptive line has the schematic Breit-Wigner/coupled-mode form

$$
\sigma_{\rm abs}(\omega)
=\sigma_{\rm sca,max}^{(l=2)}
\frac{\kappa_g\kappa_s/4}
{(\omega-\omega_0)^2+[(\kappa_g+\kappa_s)/2]^2},
$$

where

$$
\sigma_{\rm sca,max}^{(l=2)}
=\frac{10\pi}{k^2}.
$$

At critical coupling,

$$
\kappa_s=\kappa_g,
$$

the on-resonance absorption reaches

$$
\boxed{
\sigma_{\rm abs,max}^{(l=2)}
=\frac{5\pi}{2k^2}.
}
$$

But the linewidth is then only

$$
\Delta\omega\sim2\kappa_g.
$$

The frequency-integrated line strength satisfies schematically

$$
\frac1{\omega_0}
\int d\omega\,
\sigma_{\rm abs}(\omega)
\sim
\frac1{k^2}
\frac{\kappa_g}{\omega_0}.
$$

When

$$
\frac{\kappa_g}{\omega_0}
\sim(k\ell_P)^2,
$$

this becomes

$$
\boxed{
\frac1{\omega_0}
\int d\omega\,
\sigma_{\rm abs}(\omega)
\sim O(\ell_P^2).
}
$$

Thus a wavelength-scale resonant peak and a Planck-area frequency-averaged strength are mutually compatible.

Numerical prefactors depend on polarization, partial-wave normalization, transition matrix element, and exactly how the spectral average is defined. The robust scaling is

$$
\boxed{
\sigma_{\rm peak}
\times
\frac{\Delta\omega}{\omega}
\sim
\ell_P^2.
}
$$

for the bound-state cases with gravitational linewidth

$$
\Delta\omega/\omega\sim(k\ell_P)^2.
$$

---

## 4. Time-domain interpretation

The same reconciliation is clearer in time.

A wavepacket with bandwidth of order the carrier frequency,

$$
\Delta\omega\sim\omega,
$$

interacts with the bound system for only order one oscillation period. Its effective absorption probability samples the tiny oscillator strength and produces the Planck-area scale.

A time-reversed spontaneously emitted wavepacket instead has bandwidth

$$
\boxed{
\Delta\omega\sim\kappa_g
}
$$

and duration

$$
\boxed{
T_{\rm load}\sim\kappa_g^{-1}.
}
$$

It coherently drives the same transition for approximately

$$
\boxed{
N_{\rm cyc}\sim\frac{\omega}{\kappa_g}
\sim(k\ell_P)^{-2}
}
$$

carrier cycles.

That enormous coherent interaction time is what permits the resonant storage cross section to approach the wavelength-squared partial-wave ceiling.

Therefore

> **The Planck area is paid in bandwidth/time, not necessarily in peak resonant area.**

---

## 5. Why this matters for Experiment 01

The compact resonant gravitational receiver model assumes an incoming branch-difference mode that is

1. spatially/polarization matched to the receiver's gravitational emission mode;
2. spectrally matched to the receiver transition;
3. temporally shaped approximately as the time reverse of the receiver ringdown.

Under those assumptions the free-space state-transfer coefficient

$$
\eta_{\rm store}(R)
\simeq
\frac{25\mathcal O}{16(kR)^2}
$$

is a **peak narrowband coherent-storage coefficient**, not a broadband graviton-detection cross section.

The loading dynamics still know about the tiny gravitational oscillator strength through

$$
\kappa_g.
$$

The best loading time is

$$
T_{\rm load}\sim\kappa_{\rm tot}^{-1},
$$

and for a gravity-dominated bound state

$$
\kappa_{\rm tot}\sim\kappa_g
\sim\omega(k\ell_P)^2.
$$

Hence

$$
\boxed{
T_{\rm load}
\sim
\frac1\omega
\left(\frac1{k\ell_P}\right)^2,
}
$$

which is fantastically long at laboratory frequencies.

The large resonant cross section therefore does **not** imply practical graviton detection.

---

## 6. Relation to the causal-front theorem

This time-bandwidth penalty is already present in the exact front law.

For a cold gravity-dominated receiver,

$$
\kappa_{\rm tot}\simeq\kappa_g.
$$

A finite-certification front contains the factor

$$
\boxed{
\kappa_g^{-1}
}
$$

in its build time.

Thus the Gedanken experiment naturally separates

- **spatial mode capture**, which can have a resonant wavelength-scale cross section;
- **temporal quantum capture**, whose timescale is set by the tiny gravitational linewidth.

This is the correct interpretation of the receiver's apparent wavelength-squared cross section.

---

## 7. Gravitational-atom special case

For gravitationally bound states, the bound-state scaling itself implies

$$
\frac{\kappa_g}{\omega}
\sim(k\ell_P)^2
$$

up to dimensionless quantum-number factors.

Consequently

$$
\sigma_{\rm peak}
\frac{\kappa_g}{\omega}
\sim\ell_P^2.
$$

The newer gravitational-atom calculation's Planckian total cross section is therefore naturally interpreted as the same oscillator-strength budget seen without resolving/exploiting the ultra-narrow coherent resonance over its full loading time.

---

## 8. Important caveat: terminology

The literature quantity called an “absorption cross section” and the input-output quantity called “maximum resonant absorption/storage cross section” are defined operationally differently.

The safest paper language is:

- **Planck-area weak/broadband or frequency-averaged absorption strength** for the Golden-Rule bound-state result;
- **wavelength-scale peak resonant storage cross section** for a fully mode-matched narrowband quantum memory;
- explicitly quote the corresponding linewidth/loading time.

Do not state that one paper is wrong or that the Planck-area result is superseded.

---

## 9. Strongest consequence

The useful receiver invariant is not cross section alone but a time-bandwidth product such as

$$
\boxed{
\mathcal B_G
\equiv
\sigma_{\rm peak}
\frac{\kappa_g}{\omega}.
}
$$

For gravitationally bound states,

$$
\boxed{
\mathcal B_G
\sim O(\ell_P^2).
}
$$

This explains simultaneously why

- a perfectly resonant gravitational transition can have an order-$\lambda^2$ peak cross section;
- generic/broadband graviton absorption remains Planck suppressed;
- the time required for coherent quantum loading is enormous.

---

## 10. Literature basis

### Palessandro & Sloth (2020)

Appendix A explicitly derives a Planckian frequency-averaged absorption cross section and then a QFT transition rate satisfying

$$
\sigma_{\rm abs}=\Gamma/\omega^3
=\tilde\kappa\ell_P^2.
$$

The same relation implies

$$
\Gamma/\omega
=\tilde\kappa(k\ell_P)^2.
$$

### Palessandro (2025)

The gravitational-atom detector paper derives transition rates using Fermi's golden rule and, after summing over allowed graviton frequencies/transitions, obtains a total Planckian absorption cross section

$$
\sigma_{\rm abs}^{\rm tot}
=\beta\ell_P^2.
$$

These results are consistent with the ultra-narrow oscillator-strength interpretation above.

---

## 11. Next strongest path

1. Derive the exact Lorentzian storage/scattering line from the same gravitational input-output model, including all numerical factors, to turn the scaling reconciliation into an equality under a specified coupling architecture.
2. Evaluate the gravitational-atom loading time from the published transition rate and compare it with the Planck-area cross section numerically.
3. Replace the phrase “effective cross section” in the main paper with an explicit pair $\{\sigma_{\rm peak},\Delta\omega\}$ to prevent ambiguity.
4. Use the time-bandwidth result when assessing relativistic/gravity-only receiver loopholes.