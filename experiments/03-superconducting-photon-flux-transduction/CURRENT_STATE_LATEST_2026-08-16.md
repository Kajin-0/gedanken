# Experiment 03 — CURRENT STATE (latest handoff)

**Updated:** 2026-08-16  
**Status:** theory alive; **NO-GO for manuscript**.

This file is the current handoff.  Older `CURRENT_STATE.md` sections describing the pure `B=37.61` electrical rescue or barrier-shape rescue as the leading design are historical and must not be treated as the active frontier.

## 1. Active physical problem

Optimize a nonadiabatic superconducting metastable flux latch for an actual 14-um photon under one passive two-pole environment, subject to a finite-temperature dark-switch constraint.

Generation A remains externally tilted and is not photovoltaic.

Capture probabilities remain symmetrized-FDT truncated-Wigner / semiclassical screening quantities, not exact quantum photodetection efficiencies.

## 2. Current dark constraint

The accepted reduced-model dark constraint is the calibrated finite-temperature Gaussian one-loop rate

\[
\boxed{\Gamma_{1\ell}(20\,\mathrm{mK};\delta,r)=10^{-6}\ \mathrm{s}^{-1}.}
\]

The escape saddle is the same-environment nonlocal finite-period instanton.  Its one-loop prefactor is

\[
A_{1\ell}=\omega_c\sqrt{\frac{I_s}{2\pi}}D_{\rm raw,corr},
\qquad
\Gamma_{1\ell}=A_{1\ell}e^{-B_{20}}.
\]

The determinant UV tail is analytically corrected.  The determinant normalization was independently calibrated against the exact cubic metastable benchmark, reproducing \(\sqrt{60}\) to about \(4.1\times10^{-5}\) relative error.

## 3. Exact electrical finite-T similarity

For

\[
C\to r^2C,\qquad R\to R/r,
\]

at fixed static potential and normalized bath topology,

\[
\boxed{B(T;r)=rB_0(rT)},
\qquad
\boxed{T_\times(r)=T_{\times,0}/r}.
\]

Away from the immediate crossover soft mode,

\[
A_{1\ell}(T;r)=r^{-1/2}A_{1\ell,0}(rT).
\]

## 4. Accepted one-loop high-tilt dark manifold

Key points:

| delta | r_rate | C | R | fc | B20 | T0/Tx | status |
|---:|---:|---:|---:|---:|---:|---:|---|
| .200 | 7.6097 | 12.45 pF | 10.51 ohm | 2.884 GHz | 39.482 | .588 | accepted |
| .205 | 8.517859912 | 15.599 pF | 9.392 ohm | 2.537 GHz | 39.345 | .712 | accepted |
| .2075 | 9.096702522 | 17.791 pF | 8.794 ohm | 2.355 GHz | 39.269 | .775 | accepted |
| .210 | 9.825701561 | 20.757 pF | 8.142 ohm | 2.161 GHz | 39.184 | .839 | accepted |
| .211 | 10.18791311 | 22.316 pF | 7.852 ohm | 2.077 GHz | 39.149 | .871 | accepted |
| .212 | 10.62175909 | 24.257 pF | 7.532 ohm | 1.985 GHz | 39.115 | .910 | accepted |
| .213 | 11.19986413 | 26.969 pF | 7.143 ohm | 1.875 GHz | 39.107 | .962 | **soft-mode provisional** |
| .214 | — | — | — | — | — | — | **no accepted Gaussian root** |

Thus `.212` is the highest presently admissible Gaussian one-loop dark point.

## 5. Current 2-ns capture frontier at actual 14 um

All points use 20-ps rise and dt=.125 ps.

Approximate point-estimate 99% areas:

\[
A_{99}(.200)\sim420\ \mu\mathrm m^2,
\]

\[
A_{99}(.205)\sim454\ \mu\mathrm m^2
\]
(after correction to the exact self-consistent `r_rate=8.517859912`),

\[
A_{99}(.2075)\sim473\ \mu\mathrm m^2,
\]

and a binomial-logistic fit to the near-frontier data gives approximately

\[
A_{99}(.210)\approx484.95\ \mu\mathrm m^2,
\]

\[
A_{99}(.211)\approx484.98\ \mu\mathrm m^2,
\]

\[
A_{99}(.212)\approx489.30\ \mu\mathrm m^2.
\]

Approximate Wald/delta-method 95% intervals from those coarse logistic fits are broad:

- `.210`: ~474.5–495.4 um^2;
- `.211`: ~479.9–490.1 um^2;
- `.212`: ~482.9–495.7 um^2.

Therefore the `.210-.212` ordering is **not statistically resolved**.  The frontier has flattened into a shallow plateau.

A high-statistics matched calculation is active:

```text
workflow: Experiment 03 one-loop plateau high statistics
run: 31946257956
```

It uses

- deltas `.210,.211,.212`;
- common area grid `472,476,480,484,488,492 um^2`;
- `N=8192` main trajectories per area;
- common-random-number base seed across tilts;
- independent `N=4096` audit seed at `476,484,492 um^2`;
- 2-ns horizon.

This is the immediate numerical design gate.

## 6. Do not convert the large A99 values into physical far-IR wavelength claims

The reduced thermal similarity

\[
A_p\lambda=\mathrm{constant}
\]

is exact only inside the reduced assumptions: fixed absorption efficiency, fixed material/thermal law, fixed circuit, and wavelength-independent energy deposition.

At the current large areas it would algebraically imply very long equivalent wavelengths, but those are **energy-density-equivalent coordinates only**, not physical detector predictions.  Wavelength-dependent absorption, thermalization, heat capacity validity, and superconducting/proximity electrodynamics have not been restored.

The robust design metric is therefore `A99 at actual 14 um`.

## 7. Soft-mode crossover structure

The static sphaleron has a degenerate first-Matsubara cosine/sine pair.  Near the second-order crossover,

\[
B_{\rm red}=B_{\rm sph}
+\frac{\lambda_1}{2}(q_c^2+q_s^2)
+\frac{g_4}{4}(q_c^2+q_s^2)^2+\cdots.
\]

Below crossover,

\[
\Delta B=B_{\rm sph}-B_{\rm inst}
=\frac{\lambda_1^2}{4g_4},
\]

and the exact quartic soft-plane correction relative to the ordinary instanton ring Gaussian is

\[
\boxed{w_{\rm inst}=\frac12\operatorname{erfc}(-\sqrt{\Delta B}).}
\]

Numerically:

| delta | DeltaB | w_inst |
|---:|---:|---:|
| .210 | 4.52445 | .998686 |
| .211 | 3.32233 | .995027 |
| .212 | 2.12936 | .980475 |
| .213 | .92406 | .912999 |
| .214* | .35814 | .801318 |

`*` closest scanned periodic point, not a valid Gaussian rate root.

Thus `.212` remains relatively controlled; `.213+` requires a uniform crossover rate.

## 8. Hamiltonian embedding of the nonlocal bath

The passive linear environment can be represented by harmonic bath coordinates and integrated out exactly.  For full Hessian

\[
H_{\rm full}=\begin{pmatrix}H_{xx}&K^T\\K&H_b\end{pmatrix},
\]

with positive bath block,

\[
H_{\rm eff}=H_{xx}-K^TH_b^{-1}K,
\]

and

\[
\det H_{\rm full}=\det H_b\det H_{\rm eff}.
\]

Thus determinant ratios, Morse index, and the translation zero mode of the nonlocal reduced action are the Schur-complement projections of the full local phase+bath problem under the linear-equilibrium-bath assumptions.

See `NONLOCAL_TO_HAMILTONIAN_UNIFORMIZATION_PATH_2026-08-16.md`.

## 9. Uniform-rate first-orbit probe: diagnostic only

A provisional dissipative parabolic-barrier + first-orbit uniform calculation was implemented in

```text
calculations/uniform_rate_first_orbit_probe.py
```

It passes an exact undamped Matsubara-product regression to ~1e-11 or better.

At the Gaussian-rate designs:

| delta | Gaussian Gamma | first-orbit diagnostic Gamma_u1 |
|---:|---:|---:|
| .210 | ~1.000e-6/s | 9.959e-7/s |
| .211 | ~1.000e-6/s | 9.847e-7/s |
| .212 | ~1.000e-6/s | 9.364e-7/s |
| .213 | ~1.000e-6/s | 5.764e-7/s |
| .214* | 1.991e-6/s | negative / unphysical |

The `.214` failure means the provisional dissipative uniform generalization/truncation is not yet acceptable near crossover.  Do **not** use it to admit `.213/.214` as physical design points.

The full uniform theory must be matched carefully to the dissipative instanton and parabolic-barrier normalizations, including the multi-orbit structure where appropriate.

## 10. Immediate queue

1. Finish and analyze high-statistics `.210/.211/.212` plateau run `31946257956`.
2. Decide whether the accepted capture optimum is an interior point or statistically flat across the plateau.
3. Update this handoff with the high-stat result.
4. Independently verify the first-crossover residue cancellation in the dissipative uniform-rate construction before extending the dark manifold above `.212`.
5. Only after that, consider full multi-orbit uniformization.
6. Publication blockers remain: detailed-balance-preserving nonlinear quantum capture, competing dark channels, physical wavelength-dependent optics/thermalization.

## Publication status

\[
\boxed{\text{GO for continued theory; NO-GO for manuscript.}}
\]
