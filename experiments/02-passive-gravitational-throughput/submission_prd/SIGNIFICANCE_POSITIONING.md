# Significance Positioning — PRD

## Strongest defensible framing

Experiment 02 is a **conceptual passive-resource/no-go theorem** for propagating linearized gravity. Its value is not near-term experimental accessibility; it removes a large class of passive engineering degrees of freedom from the leading frequency-integrated ceiling.

Within the theorem class, high quality factor, additional retained resonances, passive mode hybridization, endpoint asymmetry, and same-two-endpoint recurrence can reshape spectral transfer but cannot raise the cumulative ceiling beyond

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}\min(I_{2,A},I_{2,B}).
```

## What `Gamma_coh` means

`Gamma_coh` is the band-limited squared `H2` norm of the selected transfer block: the integral of power transmissivity over envelope detuning. With energy-normalized ports and a spectrally flat input PSD `S_in` across the retained band, the corresponding transmitted output power is `S_in Gamma_coh`.

It has units `s^-1`, but it is **not** an information rate, bit rate, detector sensitivity, or strain-noise PSD. It becomes an information-theoretic quantity only after adding a noise model and signaling protocol.

## Concrete scale

For a uniform sphere, `I_2=(3/5)Ma^2`, so for equal endpoints

```math
\Gamma_{\rm coh}\lesssim \frac{5G\omega_0^2Ma^2}{4c^3R^2}.
```

For `M=1000 kg`, `a=1 m`, `f_0=1 kHz`, and a representative far-zone choice `k_0R=100`, one has `R≈4.77×10^6 m` and

```text
Gamma_coh ≲ 5.4×10^-39 s^-1.
```

This is not a one-event or one-bit waiting-time estimate. It demonstrates that the macroscopic mechanical far-zone ceiling is extraordinarily weak and reinforces the conceptual, rather than experimental, significance claim.

## Dominant referee risk

The most likely substantive publication objection is significance:

> Once historical resonant-mass response, arbitrary-body modal theory, material sum rules, generic passive `H2`, and wave-propagation bounds are credited, is the residual complete two-ended closure sufficiently nontrivial to merit publication?

The response should emphasize the elimination accomplished by the final theorem: the passive internal architecture of **both** endpoints collapses to a scalar second-moment resource, while the separated TT link contributes an independent propagation cut.

## Scope discipline

Do not broaden beyond compact, narrowband, wave-zone, retained carrier-scale bounded-port assumptions. In particular:

- higher-frequency off-resonant sectors require separate control;
- `k_0R≲1` near-field/reactive transfer is outside the propagation theorem;
- active systems, relays, external cavities, extended apertures, non-Markov continua, and unbounded PDE boundary ports are outside scope.

## What to emphasize

The result is a clean cut-set/resource law for a physically specific interaction: within the declared class, passive resonant engineering cannot manufacture cumulative gravitational oscillator strength or overcome the smaller endpoint resource.
