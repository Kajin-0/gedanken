# Experiment 03 — Dark-action / electrical-speed invariant — 2026-08-15

## Status

**Exact consequence of the electrical similarity of the current reduced zero-temperature passive-network model. Not novelty-audited.**

This is a direct extension of `ELECTRICAL_DARK_ACTION_SIMILARITY_2026-08-15.md`.

## 1. Electrical similarity

At fixed loop inductance, static CPR potential, normalized two-pole bath topology and physical photon rise time, apply

\[
C' = r^2C,
\qquad
R'=R/r,
\qquad
\omega_D'=\omega_D/r.
\]

Then

\[
\omega_c'=\omega_c/r,
\]

while the full zero-temperature Euclidean bounce action scales exactly as

\[
B'=rB.
\]

## 2. Exact invariant

Therefore

\[
\boxed{B'\omega_c'=B\omega_c.}
\]

For a fixed physical photon-rise time `tau_rise`, define

\[
\rho=\omega_c\tau_{\rm rise}.
\]

Then

\[
\rho'=\rho/r
\]

and hence

\[
\boxed{B'\rho'=B\rho.}
\]

Thus the pure electrical-rescaling direction trades dark tunneling action against the phase clock one-for-one in logarithmic scale.

## 3. Capture-imposed action ceiling

Suppose the full photon-capture problem for a selected thermal pulse requires

\[
\rho\ge\rho_{\min}
\]

along this electrical-similarity family. Then the electrical scaling factor is bounded by

\[
r\le\rho_0/\rho_{\min},
\]

so the maximum zero-temperature tunneling action reachable by **pure electrical similarity** is

\[
\boxed{
B_{\max}
=B_0\frac{\rho_0}{\rho_{\min}}
}.
\]

This statement is independent of the tunneling prefactor.

Conversely, if a desired dark-action target requires `B >= B_req`, then the normalized physical rise must satisfy

\[
\boxed{
\rho\le\rho_0\frac{B_0}{B_{\rm req}}
}
\]

along the similarity family.

Whether smaller `rho` helps or hurts capture is determined by the actual nonlinear finite-pulse dynamics; the invariant itself does not assume the sign of that dependence.

## 4. Current numerical scale

For the current `rDelta=.6`, `C=215 fF`, `R=80 ohm`, `alpha=.90`, 20-ps-rise baseline:

\[
B_0\approx29.7656,
\qquad
\rho_0\approx3.4251.
\]

Therefore

\[
\boxed{B\rho\approx101.95.}
\]

A dark-action rescue near `r~1.264` would have roughly

\[
B\sim37.6,
\qquad
\rho\sim2.71,
\]

with the same product.

These values are only illustrations. The physical dark-count target also requires the fluctuation determinant/prefactor, and the physical capture probability requires a detailed-balance-preserving open-system treatment.

## 5. Persistent signal

Because loop inductance is fixed under this scaling,

\[
\Delta I=\zeta\Phi_0/L
\]

is unchanged.

Thus this scaling direction has the unusually clean structure

```text
persistent-current signal: unchanged
zero-T tunneling action:    multiplied by r
electrical frequency scale: divided by r
normalized physical rise:   divided by r
```

The cost of dark stabilization is therefore dynamical speed/matching, not signal amplitude.

## 6. Design implication

If the joint dark/capture Pareto scan finds a maximum allowable scaling `r_cap` before high-fidelity photon capture fails, then pure electrical rescaling has the exact action ceiling

\[
\boxed{B_{\rm electrical,max}=r_{\rm cap}B_0.}
\]

If that ceiling is below the required dark action, the next design lever must alter something outside the similarity class, such as

- the static barrier shape/tilt;
- normalized loop topology;
- CPR shape;
- photon thermal history;
- or bath topology itself.

No novelty claim is authorized.
