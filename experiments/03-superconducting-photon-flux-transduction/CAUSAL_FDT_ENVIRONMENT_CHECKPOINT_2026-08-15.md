# Experiment 03 — Causal FDT Environment Checkpoint — 2026-08-15

## Scope

This checkpoint records the transition from a scalar deterministic resistor to a physically consistent linear electromagnetic environment. It also corrects the apparent broad `>99%` initial-Wigner capture corridor that appeared in a coarse damping scan.

The results below are theory/model diagnostics, not fabricated-device predictions. No novelty claim is authorized.

---

## 1. High-resolution initial-Wigner refinement removes the broad >99% plateau

The coarse scalar-`R` scouting scan at `rDelta=0.6`, `14 um`, `rise=20 ps` suggested a broad initial-state capture plateau above 99% around `R~160–400 ohm`.

A nested geometry-aware full-resolution refinement gives instead

```text
rDelta=.6, rise=20 ps:
  R=160 ohm -> Pcap(init)=0.980124, Gaussian-tail upper ~0.980131
  R=250 ohm -> Pcap(init)=0.990094, Gaussian-tail upper ~0.990101
  R=400 ohm -> Pcap(init)=0.987070, Gaussian-tail upper ~0.987077

rDelta=.8, rise=5 ps:
  R=400 ohm -> Pcap(init)~0.79747
  R=600 ohm -> Pcap(init)~0.80976.
```

Therefore the broad coarse `>99%` plateau was a numerical-resolution artifact. Only the `rDelta=.6`, `R~250 ohm` point barely remains above 99% in the **initial harmonic Wigner + classical nonlinear propagation + scalar-R** model, before pulse-time bath noise or exact open-system quantum dynamics.

This correction is important because the closed-system exact-quantum quench benchmark already showed percent-level deviations from truncated-Wigner propagation. A `~0.99` semiclassical result is therefore not a certified 99% detector efficiency.

Canonical refinement:

```text
.github/workflows/experiment03-quantum-optima.yml
run 31909593573
```

---

## 2. Scalar R is replaced by a passive causal two-pole environment

Use the passive network

```text
port -- L_f --+-- R -- ground
              |
              C_f
              |
            ground
```

with driving-point impedance

```math
Z(\omega)
=i\omega L_f+
\frac{R}{1+i\omega R C_f}.
```

Choose

```math
\boxed{
L_f=\frac{\sqrt2 R}{\omega_D},
\qquad
C_f=\frac{1}{\sqrt2 R\omega_D}.
}
```

Then the dissipative part of the admittance is exactly

```math
\boxed{
\operatorname{Re}Y(\omega)
=\frac{1/R}{1+(\omega/\omega_D)^4}.
}
```

This environment is passive, causal and realizable. It retains

```math
Y(0)=1/R
```

while suppressing high-frequency dissipation as `omega^-4`.

The design motivation is now explicit:

```text
fast launch/crossing -> suppress dissipative loading
slow recovery/retrapping -> retain low-frequency dissipation.
```

Canonical code/workflow:

```text
calculations/causal_two_pole_environment.py
.github/workflows/experiment03-causal-two-pole.yml
run 31912551283
```

---

## 3. Exact deterministic energy balance of the passive environment

Define

```math
\bar\Phi=\Phi_0/(2\pi),
\qquad
d=\frac{L I_{env}}{\bar\Phi},
\qquad
w=\frac{V_C}{\bar\Phi}.
```

The augmented deterministic equations can be written

```math
LC\ddot x+d+F(x,T)=0,
```

```math
\dot d=\frac{L}{L_f}(\dot x-w),
```

```math
\dot w=\frac{d}{L C_f}-\frac{w}{R C_f}.
```

With `E_L=barPhi^2/L`, the total normalized energy is

```math
\frac{E}{E_L}
=\frac12LC\dot x^2+U_x(x,T)
+\frac12\frac{L_f}{L}d^2
+\frac12LC_f w^2.
```

Direct differentiation gives

```math
\boxed{
\frac{d}{dt}\frac{E}{E_L}
=\partial_TU_x\,\dot T
-\frac{L}{R}w^2.
}
```

Thus the filter does not create free or hidden dissipation. `L_f` and `C_f` store energy reversibly; only the resistor term is irreversible.

This is the causal-environment replacement for the scalar-R phase-work identity.

---

## 4. Deterministic filter sweep is non-monotonic

For `rDelta=.6`, `rise=20 ps`, `omega_c/2pi~27.24 GHz`, the center trajectory does not respond to `omega_D` as a simple effective-resistance rescaling.

Example at `R=75 ohm`:

```text
omega_D/omega_c = 0.20 -> right
                    0.35 -> right
                    0.50 -> left
                    0.75 -> left
                    1.00 -> left
                    1.50 -> right
                    3.00 -> right.
```

At `R=160–400 ohm`, the tested center trajectory remains in the right basin over most/all of the tested cutoff range.

Therefore the causal environment itself reshapes the finite-time basin. Center-state success is again insufficient; the eventual criterion must be target-basin probability under the same environment.

---

## 5. Quantum FDT must use the same admittance

Using the retained two-sided symmetrized convention,

```math
\boxed{
S_I^{sym}(\omega)
=\hbar|\omega|
\coth\!\left(
\frac{\hbar|\omega|}{2k_BT_b}
\right)
\operatorname{Re}Y(\omega).
}
```

For the quartic-rolloff environment,

```math
\operatorname{Re}Y\sim\omega^{-4}
```

at high frequency. Since the cold harmonic susceptibility satisfies `|chi|^2~omega^-4`, both reduced phase-coordinate and phase-velocity variances are ultraviolet convergent.

At the candidate `rDelta=.6`, `R=250 ohm` region:

```text
alpha=omega_D/omega_c=0.20:
  sigma_x/sigma_x,isolated ~0.9970
  sigma_v/sigma_v,isolated ~1.0037

alpha=0.35:
  sigma_x/sigma_x,isolated ~0.9954
  sigma_v/sigma_v,isolated ~1.0064

alpha=0.50:
  sigma_x/sigma_x,isolated ~0.9942
  sigma_v/sigma_v,isolated ~1.0088

alpha=1.00:
  sigma_x/sigma_x,isolated ~0.9915
  sigma_v/sigma_v,isolated ~1.0159.
```

Thus a useful finite-band environment does not obviously destroy the cold phase state through large marginal broadening. The marginal change is percent-scale in the tested region.

Canonical code/workflow:

```text
calculations/two_pole_cold_variance.py
.github/workflows/experiment03-two-pole-variance.yml
run 31912578292
```

---

## 6. Important rejected route: arbitrary auxiliary-state sampling

A linear covariance calculation was also performed for the augmented lumped variables

```math
[x-x_c,\;u=\dot x/\omega_c,\;d,\;s=V_C/(\bar\Phi\omega_c)].
```

For example, at `R=250 ohm`, `alpha=.35`, the finite numerical integration gives

```text
sigma_x ~0.11446 rad
sigma_u ~0.11572
sigma_d ~0.00687
sigma_s ~0.661
rho_xd ~+0.258
rho_us ~-0.012.
```

However, the auxiliary capacitor-voltage coordinate is not a robust reduced observable of an ideal quantum resistor realization. At asymptotically high frequency the corresponding spectrum behaves approximately as

```math
S_{V_C}(\omega)\sim\omega^{-1},
```

so its variance is logarithmically ultraviolet sensitive. The quoted `sigma_s` therefore depends on the implicit numerical high-frequency cutoff / circuit realization.

A 4D Gauss-Hermite capture scout using these auxiliary coordinates was completed, but its apparent probabilities are **not canonical physical detector results** and must not be used as evidence for or against viability.

Correct interpretation:

```text
use Y(omega) and its reduced memory/noise kernel as the physical environment;
do not promote arbitrary auxiliary circuit coordinates to unique detector-state observables.
```

The physically controlled next object is the reduced generalized-Langevin/open-system phase dynamics generated by the specified spectral density.

Rejected/scouting code retained for provenance:

```text
calculations/two_pole_joint_covariance.py
calculations/two_pole_joint_capture_scout.py
```

---

## 7. Integrated bath-force scale for the quartic rolloff

At `T -> 0`,

```math
\langle I_N^2\rangle
=\frac{1}{\pi}
\int_0^\infty
\hbar\omega\operatorname{Re}Y(\omega)d\omega.
```

For

```math
\operatorname{Re}Y
=\frac{1/R}{1+(\omega/\omega_D)^4},
```

use

```math
\int_0^\infty\frac{x}{1+x^4}dx=\frac{\pi}{4}
```

to obtain

```math
\boxed{
\langle I_N^2\rangle
=\frac{\hbar\omega_D^2}{4R}.
}
```

For the dimensionless phase-force noise

```math
n=\frac{L I_N}{\bar\Phi},
```

```math
\boxed{
\sigma_n
=\frac{L\omega_D}{\bar\Phi}
\sqrt{\frac{\hbar}{4R}}.
}
```

Relative to the cold harmonic restoring-force fluctuation,

```math
\boxed{
\frac{\sigma_n}{\kappa_c\sigma_x}
=\alpha\sqrt{\frac{g}{2}},
\qquad
\alpha=\omega_D/\omega_c,
\qquad
g=\frac{1}{RC\omega_c}.
}
```

At `rDelta=.6`, `R=250 ohm`, `alpha=.35`, this ratio is only about `0.08` in the **cold harmonic well**.

This does not establish small pulse-time noise. The transient barrier/curvature softens strongly during switching, so the same bath-force scale can become much larger relative to the instantaneous restoring dynamics.

---

## 8. Exact FDT stochastic-work identity for a prescribed trajectory

For any prescribed deterministic port-voltage waveform `V(t)` coupled to a linear equilibrium environment,

```math
Q_{diss}
=\int\frac{d\omega}{2\pi}
\operatorname{Re}Y(\omega)|\tilde V(\omega)|^2.
```

Define noise work

```math
W_N=\int V(t)I_N(t)dt.
```

For the Gaussian linear bath,

```math
\operatorname{Var}W_N
=\int\frac{d\omega}{2\pi}
\hbar|\omega|
\coth\!\left(
\frac{\hbar|\omega|}{2k_BT}
\right)
\operatorname{Re}Y(\omega)|\tilde V(\omega)|^2.
```

Hence exactly for the prescribed waveform,

```math
\boxed{
\operatorname{Var}W_N
=\epsilon_{bath}^{eff}Q_{diss},
}
```

where

```math
\boxed{
\epsilon_{bath}^{eff}
=
\frac{
\int \hbar|\omega|\coth(\cdots)\operatorname{Re}Y|\tilde V|^2d\omega
}{
\int \operatorname{Re}Y|\tilde V|^2d\omega
}.
}
```

Classical limit:

```math
\boxed{
\operatorname{Var}W_N=2k_BT\,Q_{diss}.
}
```

The function

```math
\epsilon(\omega)
=\hbar|\omega|\coth[\hbar|\omega|/(2k_BT)]
```

is monotone increasing with `|omega|`. Therefore, **at fixed dissipated energy for a prescribed trajectory, shifting dissipation toward lower frequencies lowers the unavoidable FDT work variance per unit dissipated energy.**

This gives a second reason, independent of deterministic launch-energy preservation, to prefer spectrally separated damping:

```text
high-frequency launch -> low dissipation
lower-frequency retrapping -> stronger dissipation.
```

Causality and finite capture time prevent assuming this separation can be made arbitrarily sharp; that is an active next question.

Canonical code/workflows:

```text
calculations/causal_phase_work_noise.py
.github/workflows/experiment03-fdt-work-noise.yml
run 31912819454

calculations/causal_phase_work_convergence.py
.github/workflows/experiment03-fdt-work-convergence.yml
```

---

## 9. First trajectory work-noise scale — provisional pending window convergence

For the current full-CPR `rDelta=.6`, `14 um`, `rise=20 ps`, `T_bath=20 mK` trajectories, the initial 1.5-ns spectral calculation gives roughly

```text
R=120, alpha=.35:
  Q_diss/kB ~3.44 K
  epsilon_eff/kB ~0.73 K
  sigma_W/kB ~1.58 K

R=160, alpha=.35:
  Q_diss/kB ~2.71 K
  epsilon_eff/kB ~0.85 K
  sigma_W/kB ~1.52 K

R=250, alpha=.20:
  Q_diss/kB ~0.89 K
  epsilon_eff/kB ~0.39 K
  sigma_W/kB ~0.59 K

R=250, alpha=.35:
  Q_diss/kB ~2.28 K
  epsilon_eff/kB ~0.81 K
  sigma_W/kB ~1.36 K

R=250, alpha=.50:
  Q_diss/kB ~3.86 K
  epsilon_eff/kB ~1.03 K
  sigma_W/kB ~1.99 K

R=400, alpha=.35:
  Q_diss/kB ~1.48 K
  epsilon_eff/kB ~0.96 K
  sigma_W/kB ~1.19 K.
```

These correspond to about `9–29%` of the retained `6.87 k_B K` cold barrier, but **the cold barrier is not the correct dynamic switching margin**. The transient separatrix/barrier is smaller and time dependent.

The FFT/time-domain dissipated-energy consistency is already good (~1–2%) for several points but is poorer for the most strongly filtered `R=250, alpha=.20` point (~24% mismatch) and ~10% at `R=250, alpha=.35`. A longer recovery-window convergence workflow is active. Do not freeze the numerical work-noise values until that check passes or bounds the truncation error.

Also, `sigma_W` is a symmetrized quantum-FDT work fluctuation. It must **not** be naively converted into a classical activation/error probability at 20 mK. Classical sampling of zero-point noise would violate quantum detailed balance. The work variance is currently a robustness/susceptibility diagnostic, not a detector-efficiency calculation.

---

## 10. Current physical conclusion

The scalar-resistance optimization problem has been replaced by the joint spectral-environment problem

```math
\boxed{
\text{choose a passive causal }Y(\omega)
\text{ that maximizes capture margin}
\text{ while minimizing dark escape and FDT noise.}
}
```

The strongest candidate family remains `rDelta~0.6`; the `.8` family is now strongly disfavored by initial-state basin geometry.

However, the `rDelta=.6` initial-state capture margin is much thinner than the coarse scan suggested: the best currently refined scalar-R point is only about `0.9901` before pulse-time environment fluctuations and exact open-system quantum dynamics.

The FDT work scale is therefore potentially first-order rather than a small correction.

---

## Next decisive work

1. Finish recovery-window convergence of the FDT work functional.
2. Replace the cold-barrier normalization by a trajectory/basin-relevant dynamic robustness measure.
3. Formulate the reduced generalized-Langevin/open-system problem directly from `Y(omega)` rather than sampled UV-sensitive auxiliary coordinates.
4. Use quantum-consistent bath dynamics; do not treat the symmetrized zero-point PSD as an ordinary classical activation source.
5. Use the same spectral density in dissipative quantum escape / dark-count calculations.
6. Determine whether any operating set remains with both high `P_capture` and acceptable `Gamma_dark`.
7. Only then return to detailed optical absorptance, readout and reset.

## Verdict

**GO for continued theory. NO-GO for manuscript.**

The architecture remains alive, but the environment/noise problem is now quantitatively central. A negative bound remains an acceptable outcome.
