# Experiment 03 — two-soft-mode crossover derivation

**Date:** 2026-08-16

## Purpose

The calibrated Gaussian one-loop rate ceases to be trustworthy as the 20-mK periodic instanton approaches the thermal sphaleron.  The static sphaleron has a degenerate first-Matsubara cosine/sine pair, so the crossover is a **two-soft-coordinate** problem.

This note derives the part that follows directly from the current bath-integrated Euclidean action.  It deliberately does **not** claim a complete uniform physical escape rate yet.

Primary literature context:

- I. Affleck, *Quantum-Statistical Metastability*, Phys. Rev. Lett. 46, 388 (1981), DOI 10.1103/PhysRevLett.46.388.
- H. Grabert and U. Weiss, *Crossover from Thermal Hopping to Quantum Tunneling*, Phys. Rev. Lett. 53, 1787 (1984), DOI 10.1103/PhysRevLett.53.1787.
- H. Grabert, U. Weiss, and P. Hänggi, *Quantum Tunneling in Dissipative Systems at Finite Temperatures*, Phys. Rev. Lett. 52, 2193 (1984), DOI 10.1103/PhysRevLett.52.2193.
- J. E. Lawrence, *Semiclassical instanton theory for reaction rates at any temperature: How a rigorous real-time derivation solves the crossover temperature problem*, J. Chem. Phys. 161, 184115 (2024), DOI 10.1063/5.0237368; arXiv:2409.02820.

Lawrence's uniform theory is useful structurally because it shows that a smooth crossover requires both an instanton-side erfc term and a companion barrier/transition-state term.  Its full multidimensional Hamiltonian rate formula is **not automatically proven** for the present nonlocal bath-integrated action.

## 1. Degenerate soft plane

At the static sphaleron, the first nonzero Matsubara cosine and sine modes have identical quadratic eigenvalue because the Euclidean action is time-translation invariant.  Denote their orthonormal amplitudes by

\[
q_c,\qquad q_s,
\]

and

\[
\rho^2=q_c^2+q_s^2.
\]

The leading rotationally invariant reduced action is

\[
\boxed{
B_{\rm red}(\rho)
=B_{\rm sph}
+\frac{\lambda_1}{2}\rho^2
+\frac{g_4}{4}\rho^4+O(\rho^6).
}
\]

Here \(\lambda_1\) is the normalized first-Matsubara sphaleron Hessian eigenvalue.  The exact crossover is

\[
\boxed{\lambda_1(T_\times)=0.}
\]

For the second-order branch found in Experiment 03, \(g_4>0\).

## 2. Broken-symmetry periodic-instanton ring below crossover

For \(T<T_\times\),

\[
\lambda_1<0.
\]

Stationarity gives

\[
\rho_0^2=-\frac{\lambda_1}{g_4}.
\]

All polar angles represent Euclidean-time translations of the same periodic orbit.  The action difference between the sphaleron and periodic instanton is therefore

\[
\Delta B
\equiv B_{\rm sph}-B_{\rm inst}
=\frac{\lambda_1^2}{4g_4}.
\]

Hence

\[
\boxed{
g_4=\frac{\lambda_1^2}{4\Delta B}.}
\]

Define the natural uniform coordinate

\[
z\equiv\frac{\lambda_1}{2\sqrt{g_4}}.
\]

Then on the instanton side

\[
\boxed{z=-\sqrt{\Delta B}.}
\]

The numerical workflow `calculations/soft_mode_uniform_ingredients.py` verifies this identity directly from the full nonlocal saddle family.

## 3. Exact quartic soft-plane integral

The soft-plane contribution to the Euclidean fluctuation integral is

\[
I_{\rm soft}(\lambda_1,g_4)
=\int_{\mathbb R^2}dq_c\,dq_s\,
\exp\!\left[-\frac{\lambda_1}{2}\rho^2
            -\frac{g_4}{4}\rho^4\right].
\]

Using polar coordinates,

\[
I_{\rm soft}
=2\pi\int_0^\infty \rho\,d\rho\,
 e^{-\lambda_1\rho^2/2-g_4\rho^4/4}.
\]

With \(u=\rho^2\), this evaluates exactly to

\[
\boxed{
I_{\rm soft}
=\frac{\pi^{3/2}}{\sqrt{g_4}}
 \exp\!\left(\frac{\lambda_1^2}{4g_4}\right)
 \operatorname{erfc}\!\left(\frac{\lambda_1}{2\sqrt{g_4}}\right).
}
\]

Below crossover this becomes

\[
I_{\rm soft}
=\frac{\pi^{3/2}}{\sqrt{g_4}}
 e^{\Delta B}
 \operatorname{erfc}(-\sqrt{\Delta B}).
\]

## 4. Recovery of the ordinary instanton orbit factor

Far below crossover, the integral can be evaluated by steepest descent about the ring \(\rho=\rho_0\).  The angular direction is the translation zero mode and the radial curvature is

\[
B''_{\rho\rho}(\rho_0)=2|\lambda_1|.
\]

The ring Gaussian asymptotic is

\[
I_{\rm ring}^{\rm Gauss}
\sim
\frac{2\pi^{3/2}}{\sqrt{g_4}}e^{\Delta B}.
\]

Therefore

\[
\boxed{
\frac{I_{\rm soft}}{I_{\rm ring}^{\rm Gauss}}
=\frac12\operatorname{erfc}(-\sqrt{\Delta B}).
}
\]

This factor tends to 1 for \(\Delta B\gg1\) and to 1/2 as the periodic orbit collapses into the sphaleron.

This is the precise local meaning of the erfc weight in the present two-soft-mode normal form.

## 5. Numerical action-space proximity to crossover

At the current one-loop rate-constrained / high-tilt points:

| delta | DeltaB = Bsph-Binst | z=-sqrt(DeltaB) | 0.5 erfc(z) | T0/Tx |
|---:|---:|---:|---:|---:|
| .210 | 4.52445 | -2.12708 | 0.998686 | 0.83924 |
| .211 | 3.32233 | -1.82273 | 0.995027 | 0.87103 |
| .212 | 2.12936 | -1.45923 | 0.980475 | 0.90966 |
| .213 | 0.92406 | -0.96128 | 0.912999 | 0.96151 |
| .214* | 0.35814 | -0.59845 | 0.801318 | 0.99020 |

`*` The .214 row uses the closest scanned periodic point, not an accepted `Gamma=1e-6/s` Gaussian root.

Thus .212 is still relatively far from the collapse in action space, whereas .213 and especially .214 are genuinely nonuniform.

## 6. Why this does not yet supply the full physical rate

It would be incorrect to define

\[
\Gamma_{\rm uniform}
\stackrel{\rm wrong}{=}
\frac12\operatorname{erfc}(-\sqrt{\Delta B})\,
\Gamma_{\rm inst}^{\rm Gaussian}
\]

and stop there.

That expression only uniformizes the instanton-orbit soft-plane contribution.  A complete physical crossover rate must also contain the sphaleron / transition-state contribution with the correct unstable-flux normalization, arranged so the total expression remains finite and continuously matches the high-temperature regime.

Lawrence's rigorous Hamiltonian result has exactly this structure: an erfc-weighted instanton contribution plus a companion parabolic-barrier term and a cancellation term; multi-orbit corrections remove additional lower-temperature parabolic singularities.

For Experiment 03 the remaining proof obligation is to derive the corresponding companion term after integrating out the linear passive bath.  The nonlocal Euclidean kernel changes the Matsubara spectrum and crossover condition but preserves time-translation symmetry; this strongly suggests a related uniform structure, but that extension is presently a **conjecture**, not an accepted theorem.

## 7. Current design consequence

Until the nonlocal uniform rate is derived:

- `.212` is the highest fully accepted Gaussian one-loop dark-rate point;
- `.213` is soft-mode provisional;
- `.214` has no accepted Gaussian root before the crossover;
- no design beyond `.212` may be promoted merely because its photon-capture screen is favorable.

If the matched 2-ns capture frontier continues increasing from `.210` through `.212`, then the current reduced-model optimum is **dark-theory-boundary limited** and the next task is the uniform nonlocal crossover rate—not further tilt optimization.
