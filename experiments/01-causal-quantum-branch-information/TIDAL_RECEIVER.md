# Gauge-Invariant Tidal Receiver

**Timestamp:** 2026-08-07 14:09 EDT  
**Status:** Replaces the single-free-mass receiver as the clean local GR receiver

This note resolves an equivalence-principle issue in the earlier quadrupole calculation. A genuinely local freely falling receiver cannot measure a uniform gravitational acceleration. Its leading local observable is **geodesic deviation**, equivalently the electric/tidal part of the Riemann/Weyl tensor.

The previously derived $R^{-4}$ quadrupole force is appropriate only when the probe is referenced to an external support or laboratory structure. For a self-contained freely falling receiver, the clean observable is a differential mode and the near-zone response acquires one additional spatial derivative.

---

## 1. Fermi-normal coupling

Around a freely falling reference worldline, Fermi normal coordinates remove the uniform-acceleration term. To leading order in the size of a localized nonrelativistic system, curvature enters the Hamiltonian as

$$
H_{\rm curv}
=\frac{\mu_Bc^2}{2}
R_{0i0j}(t)\,\xi^i\xi^j,
$$

up to Riemann-sign convention. This is the quantum Hamiltonian counterpart of geodesic deviation.

Define the physical tidal tensor

$$
\mathcal E_{ij}\equiv c^2R_{0i0j}.
$$

In the Newtonian weak-field limit, $\mathcal E_{ij}$ is the Hessian of the Newtonian potential up to sign convention,

$$
\mathcal E_{ij}\simeq \partial_i\partial_j\Phi.
$$

For a one-dimensional differential receiver with equilibrium baseline $L_B$ and quantum differential coordinate $x_B$,

$$
\xi=L_B+x_B.
$$

Expanding the tidal potential gives

$$
H_{\rm curv}
=\frac{\mu_B}{2}\mathcal E_{nn}(L_B+x_B)^2.
$$

The branch-dependent linear drive on the quantum differential mode is therefore

$$
\boxed{
H_{\rm drive}
=\mu_BL_B\,\mathcal E_{nn}(t)\,x_B,
}
$$

and the branch-to-branch generalized force difference is

$$
\boxed{
|\Delta F_B|
=\mu_BL_B|\Delta\mathcal E_{nn}|.
}
$$

Here $\mu_B$ is the effective/reduced mass of the differential mode. For two equal freely falling masses $m$ described by their relative coordinate, $\mu_B=m/2$.

This receiver is gauge-invariant at the level relevant to the approximation because it is driven by curvature rather than a coordinate-dependent gravitational force.

---

## 2. Near-zone response to the conserved source quadrupole

Use the axisymmetric branch-difference STF quadrupole

$$
\Delta Q_{ij}(t)
=q(t)\left(n_in_j-\frac13\delta_{ij}\right).
$$

On-axis, the branch-dependent Newtonian quadrupole potential is

$$
|\Delta\Phi_Q|
=\frac{G|q|}{R^3}.
$$

Taking the radial Hessian,

$$
\frac{d^2}{dR^2}\left(\frac{Gq}{R^3}\right)
=\frac{12Gq}{R^5},
$$

so the branch-dependent radial tidal tensor is

$$
\boxed{
|\Delta\mathcal E_{nn}^{\rm NZ}|
=\frac{12G|q(t_R)|}{R^5},
\qquad
t_R=t-R/c.
}
$$

The differential quantum receiver therefore feels

$$
\boxed{
|\Delta F_B^{\rm NZ}|
=\frac{12G\mu_BL_B}{R^5}|q(t_R)|.
}
$$

This supersedes the $R^{-4}$ force scaling for a single mass relative to an external support.

---

## 3. Conditional oscillator displacement

Let the differential mode be harmonic with frequency $\omega_B$ and

$$
x_{\rm zpf}=\sqrt{\frac{\hbar}{2\mu_B\omega_B}}.
$$

The branch-dependent coherent displacement difference is

$$
\boxed{
\Delta\alpha_B(T)
=\frac{12iG\mu_BL_Bx_{\rm zpf}}{\hbar R^5}
\int_0^{T-R/c}dt\,q(t)e^{i\omega_B(t+R/c)}
}
$$

in the retarded near-zone approximation.

Thus the narrow-band response coefficient per quadrupole amplitude is

$$
\boxed{
|\mathcal R_{B,\rm tidal}^{\rm NZ}|
=\frac{12G\mu_BL_Bx_{\rm zpf}}{\hbar R^5}.
}
$$

---

## 4. Complementary graviton record

For the same quadrupole convention, the coherent branch-difference graviton spectrum obtained from the standard quadrupole radiation formula has robust scaling

$$
S_G(\omega)
\propto
\frac{G}{\hbar c^5}\omega^5.
$$

Using the convention adopted in `GRAVITY_QUADRUPOLE_LIMIT.md`,

$$
S_G(\omega)
\simeq
\frac{2G}{15\hbar c^5}\omega^5,
$$

up to one-sided/two-sided Fourier factors of order unity.

This radiative spectrum is only the clean outgoing-graviton contribution to the complementary record. A complete gravity calculation must also treat dressing/soft/near-field issues consistently. The operational $C_\Xi$ definition remains valid even when the decomposition into separate field sectors is subtle.

---

## 5. Near-zone history-transfer rate

Define

$$
\gamma_{\rm hist}^{(G)}
=\frac{|\mathcal R_B^{(G)}|^2}{S_G(\omega_B)}.
$$

Substituting the tidal response gives

$$
\boxed{
\gamma_{\rm hist,tidal}^{\rm NZ}
\simeq
540\,
\frac{G\mu_BL_B^2c^5}
{R^{10}\omega_B^6}
}
$$

within the stated convention.

The robust scaling is

$$
\boxed{
\gamma_{\rm hist,tidal}^{\rm NZ}
\propto
R^{-10}\omega_B^{-6}.
}
$$

Including differential-mode amplitude damping $\kappa_B$ gives the **tidal history cooperativity**

$$
\boxed{
\mathcal C_{\rm hist,tidal}^{\rm NZ}
\simeq
540\,
\frac{G\mu_BL_B^2c^5}
{\kappa_BR^{10}\omega_B^6}
}
$$

or, with $Q_B=\omega_B/\kappa_B$,

$$
\boxed{
\mathcal C_{\rm hist,tidal}^{\rm NZ}
\simeq
540\,
\frac{G\mu_BL_B^2c^5Q_B}
{R^{10}\omega_B^7}.
}
$$

The optimized strong history-transfer witness can beat **radiative graviton leakage plus receiver damping alone** only if

$$
\mathcal C_{\rm hist,tidal}^{\rm NZ}>1.
$$

Technical and environmental decoherence would add additional record/noise terms and make the real threshold harder.

---

## 6. Critical radius and depth of the near zone

The radiation-only critical radius is

$$
\boxed{
R_c
\simeq
\left[
540\,
\frac{G\mu_BL_B^2c^5Q_B}
{\omega_B^7}
\right]^{1/10}.
}
$$

Illustrative values:

- two approximately $1\,\mathrm g$ receiver masses ($\mu_B\approx0.5\,\mathrm g$), $L_B=0.1\,\mathrm m$, $f_B=1\,\mathrm{Hz}$, $Q_B=10^8$: $R_c\approx1.6\,\mathrm{km}$;
- two approximately $1\,\mathrm{kg}$ receiver masses ($\mu_B\approx0.5\,\mathrm{kg}$), $L_B=1\,\mathrm m$, $f_B=100\,\mathrm{Hz}$, $Q_B=10^6$: $R_c\approx1.3\times10^2\,\mathrm m$.

Again these are **information-efficiency** thresholds against ideal graviton radiation, not signal-to-noise or detectability claims.

Define

$$
\epsilon=\frac{\omega_BR}{c}
$$

and

$$
\nu_G
=\frac{G\mu_BL_B^2Q_B\omega_B^3}{c^5}.
$$

Then

$$
\boxed{
\mathcal C_{\rm hist,tidal}^{\rm NZ}
\simeq
540\,\nu_G\,\epsilon^{-10}.
}
$$

For laboratory parameters $\nu_G$ is fantastically small. In the first illustrative example,

$$
\nu_G\sim3.4\times10^{-48},
$$

and the critical radius corresponds to

$$
\epsilon_c\sim3.4\times10^{-5}.
$$

Thus the strong local-receiver regime is parametrically **deep inside the near zone**.

---

## 7. Wave-zone curvature response

In the far wave zone, the radiative metric is

$$
h_{ij}^{TT}(t,R)
=\frac{2G}{c^4R}
\ddot Q_{ij}^{TT}(t-R/c),
$$

and the physical tidal tensor is

$$
\mathcal E_{ij}^{\rm GW}
=c^2R_{0i0j}
=-\frac12\ddot h_{ij}^{TT}
=-\frac{G}{c^4R}Q_{ij}^{(4),TT}.
$$

For a transverse differential receiver define a dimensionless angular/polarization projection $\mathcal A$ by

$$
\mathcal E_{ee}^{\rm GW}
=\mathcal A\frac{G}{c^4R}q^{(4)}.
$$

At angular frequency $\omega_B$,

$$
\boxed{
|\mathcal R_{B,\rm tidal}^{\rm WZ}|
=\mathcal A
\frac{G\mu_BL_Bx_{\rm zpf}\omega_B^4}
{\hbar c^4R}.
}
$$

Using the same total outgoing-graviton record spectrum gives

$$
\boxed{
\gamma_{\rm hist,tidal}^{\rm WZ}
\simeq
\frac{15\mathcal A^2}{4}
\frac{G\mu_BL_B^2\omega_B^2}
{c^3R^2},
}
$$

and

$$
\boxed{
\mathcal C_{\rm hist,tidal}^{\rm WZ}
\simeq
\frac{15\mathcal A^2}{4}
\frac{G\mu_BL_B^2Q_B\omega_B}
{c^3R^2}.
}
$$

Equivalently,

$$
\boxed{
\mathcal C_{\rm hist,tidal}^{\rm WZ}
\simeq
\frac{15\mathcal A^2}{4}
\nu_G\epsilon^{-2}.
}
$$

The exact numerical coefficient depends on angular collection, quadrupole convention, and spectral normalization. The parametric conclusion is robust: around the dynamical wave-zone crossover $\epsilon\sim1$, a **single local differential receiver** has history-transfer efficiency of order the tiny dimensionless gravity parameter $\nu_G$.

---

## 8. Strong-witness local-receiver tradeoff

For a local freely falling differential receiver:

### Near zone

$$
\mathcal C_{\rm hist}^{\rm NZ}
\sim
\nu_G\epsilon^{-10}.
$$

### Wave zone

$$
\mathcal C_{\rm hist}^{\rm WZ}
\sim
\nu_G\epsilon^{-2}.
$$

At $\epsilon\sim1$ both asymptotic descriptions imply, up to geometric factors,

$$
\mathcal C_{\rm hist}\sim O(\nu_G)\ll1.
$$

Therefore the **strong history-transfer witness** has a severe local-receiver tradeoff:

- to beat the total unobserved gravitational record, operate deep in the reactive near zone;
- to make retardation dynamically obvious, move toward the wave zone, where a local receiver captures only a tiny fraction of the outgoing branch record.

This is **not a no-go theorem for gravitationally generated entanglement**. The witness $\mathcal M_\Xi>0$ is sufficient rather than necessary, and the denominator here uses the total outgoing radiative record. The result is best described as a strong-witness or information-capture limitation for a local receiver.

---

## 9. Full crossover kernel target

The electric part of the retarded quadrupolar field must interpolate schematically as

$$
\mathcal E_{ij}(\omega,R)
=\frac{Gq(\omega)}{R^5}
\mathcal P_{ij}(\epsilon,\Omega),
\qquad
\epsilon=\frac{\omega R}{c},
$$

where the dimensionless tensor transfer function contains near, induction, and radiation terms through order

$$
1,\quad i\epsilon,\quad \epsilon^2,\quad i\epsilon^3,\quad \epsilon^4.
$$

The limiting behavior is

$$
\mathcal P\to O(1)
\qquad(\epsilon\ll1),
$$

and

$$
\mathcal P\to O(\epsilon^4)
\qquad(\epsilon\gg1),
$$

which reproduces the $R^{-5}$ tidal near field and $\omega^4/(c^4R)$ radiative curvature field.

Deriving the exact gauge-invariant tensor $\mathcal P_{ij}$ from the retarded linearized Einstein equations for a **conserved** source is the next central calculation.

---

## 10. Literature boundary

The curvature coupling itself is established. Fermi-normal treatments of localized quantum systems give a leading Hamiltonian correction proportional to $mR_{0i0j}x^ix^j/2$, and gravitational-wave detectors fundamentally measure geodesic deviation. A July 2026 Physical Review D paper by Hirotani and Matsumura also studies classical-quantum gravity specifically through geodesic deviation and predicted strain spectra.

Therefore **using geodesic deviation is not novel**. The potentially distinctive contribution remains the history-transfer construction: pairing a gauge-invariant curvature receiver with the source-probe coherence margin and the complementary gravitational branch-record spectrum.

---

## 11. Immediate next step

Derive the exact retarded quadrupolar electric-Weyl transfer function $\mathcal P_{ij}(\epsilon,\Omega)$ and use it to compute a single crossover history cooperativity

$$
\mathcal C_{\rm hist}^{(G)}(\epsilon)
$$

valid from near zone to wave zone. Then compare:

1. one local differential receiver;
2. an ideal angularly mode-matched enclosing receiver.

The main candidate result is a quantitative statement of how **causal retardation visibility and local coherent branch-information capture compete across the gravitational near-to-wave-zone transition**.
