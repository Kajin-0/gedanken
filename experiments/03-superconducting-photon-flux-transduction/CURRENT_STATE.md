# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**.

## 1. Current physical question

Can one absorbed LWIR photon reshape a proximity-Josephson/rf-SQUID metastable potential rapidly enough that the phase enters a directionally favored basin with **high probability**, remains there as persistent superconducting flux after recovery, and simultaneously satisfies a very low cold false-switch target under one physically consistent electromagnetic environment?

Current internal description:

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

Generation A uses external flux tilt and is **not photovoltaic**. Generation B remains reserved for a later zero-external-flux mechanism if one survives collision review.

## 2. Current mechanism hierarchy

```text
absorbed LWIR photon
 -> electronic thermalization / local energy delivery to weak link
 -> temperature-dependent CPR and phase potential change rapidly
 -> phase is displaced and accelerated
 -> finite transient barrier may be crossed even before the static fold disappears
 -> potential reforms during cooling
 -> trajectory distribution is captured into competing cold basins
 -> successful event leaves persistent superconducting flux.
```

The quasistatic fold remains an organizing limit, but

```math
\boxed{T_{peak}\ge T_f}
```

is neither necessary nor sufficient in the fast-pulse regime.

## 3. Deterministic equation and exact phase-work identity

Current scalar-environment diagnostic:

```math
\boxed{LC\ddot x+\frac{L}{R}\dot x+F[x,T_e(t)]=0.}
```

The exact scalar-R phase-energy balance is

```math
\boxed{
\frac{d}{dt}
\left[
\frac12LC\dot x^2+U(x,T)
\right]
=U_T(x,T)\dot T-\frac{L}{R}\dot x^2.
}
```

Thus optical/thermal evolution performs parametric work on the phase coordinate while the environment removes phase energy.

Damping has opposite roles:

```text
launch/crossing: excessive damping removes useful phase energy
post-crossing: damping helps suppress return/retrapping.
```

Consequently the pulled-back finite-time basin is folded rather than separated by one monotonic damping threshold.

## 4. Static CPR / two-gap baseline retained

The current static CPR baseline is the Titov–Beenakker arbitrary-length graphene secular equation evaluated with the Hagymasi–Kormanyos–Cserti Matsubara method, plus an empirically anchored realistic-skewness interface envelope.

Never collapse

```text
Delta_ind -> induced/minigap controlling ABS spectrum, Ic(T), CPR and thermal sensitivity
Delta_s   -> parent-electrode gap controlling hot-carrier escape / calorimetric confinement.
```

Representative retuned `A=100 um^2`, `beta~0.8` family:

| `rDelta` | `Tf` | `L` | cold barrier/kB | provisional `Cmin,Q` | `lambda_fold` |
|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.905 K | 87.8 pH | 9.10 K | 161 fF | 11.8 um |
| 0.8 | 0.813 K | 96.8 pH | 8.12 K | 181 fF | 14.7 um |
| 0.6 | 0.695 K | 111.5 pH | 6.87 K | 215 fF | 20.1 um |
| 0.5 | 0.623 K | 123.1 pH | 6.10 K | 244 fF | 25.0 um |
| 0.4 | 0.540 K | 140.3 pH | 5.22 K | 287 fF | 33.3 um |

`lambda_fold` is only the quasistatic well-disappearance scale, not the detector cutoff.

## 5. Nonadiabatic spectral hierarchy

Let `x_c` be the cold metastable phase and `x_s(T)` the retained hot saddle. Define

```math
\mathcal B_q(T)=U[x_s(T),T]-U(x_c,T).
```

The ideal fixed-hot sudden-quench threshold satisfies

```math
\boxed{\mathcal B_q(T_q)=0.}
```

Current full-CPR values:

```text
rDelta=.8: Tq~0.718 K, Tf~0.812 K, lambda_fold~14.7 um, lambda_quench~18.8 um
rDelta=.6: Tq~0.615 K, Tf~0.694 K, lambda_fold~20.1 um, lambda_quench~25.6 um.
```

For the retained families,

```math
\boxed{\lambda_{fold}<\lambda_{dynamic}<\lambda_{quench}.}
```

These are model scales, not universal detector cutoffs.

## 6. Finite-rise deterministic checkpoint

For one absorbed `14 um` photon, current scalar-R dynamics give approximately

```text
rDelta=.8:
  ordinary capture survives through ~9 ps rise;
  becomes weak-damping/settling sensitive near ~9.5–10 ps.

rDelta=.6:
  capture survives through ~30 ps rise;
  broadly absent near ~32 ps.
```

Using Huang's characteristic cross-device diffusion scale only as an order-of-magnitude geometry screen, these rise windows correspond to energy delivery within a few micrometres of the Josephson-sensitive region. Large optical collection area therefore requires localized antenna/cavity delivery rather than uniform heating of a large graphene sheet.

## 7. The detector criterion is now basin probability, not one trajectory

Let `Omega_R^0` be the target cold basin pulled back through the finite pulse dynamics to the initial phase plane. Define normalized velocity

```math
u=\dot x/\omega_c.
```

The present initial-state probability object is

```math
\boxed{
P_{cap}^{init}
=\iint_{\Omega_R^0}\rho_W(x,u)\,dx\,du.
}
```

The pulled-back basin contains multiple alternating strips. Therefore deterministic center-state success can coexist with substantial wrong-basin probability.

The physically relevant future operating set is

```math
\boxed{
\mathcal O(p_*,D_*)
=\{\theta:P_{cap}(\theta)\ge p_*,\;\Gamma_{dark}(\theta)\le D_*\},
}
```

with `theta` containing optical pulse, material/CPR, `L,C`, flux tilt, thermal transport and the environment.

## 8. Cold harmonic quantum width

For the cold harmonic phase mode,

```math
\sigma_x^2
=\frac{\hbar}{2C\bar\Phi^2\omega_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right),
\qquad
\sigma_{u}=\sigma_x.
```

Current values at `T0=20 mK`:

```text
rDelta=.8: sigma_x~0.11559 rad, hbar omega_c/(kBT0)~76.9
rDelta=.6: sigma_x~0.11499 rad, hbar omega_c/(kBT0)~65.4.
```

The initial width is overwhelmingly zero-point rather than thermal.

## 9. Converged initial-Wigner basin probabilities

Canonical methods:

```text
calculations/quantum_basin_integral.py
calculations/quantum_basin_xgrid.py
.github/workflows/experiment03-quantum-xgrid.yml
run 31908931322
```

The velocity direction is integrated by explicitly resolving all target/non-target basin strips. The remaining Gaussian `x` integral is evaluated on a nested standard-normal grid with explicit omitted-tail mass.

Current one-photon `14 um` results:

```text
rDelta=.6, rise=20 ps, R=75 ohm:
  Pcap(init)=0.813771–0.813778

rDelta=.6, rise=20 ps, R=120 ohm:
  nx=33 Pcap(init)=0.966397
  Gaussian-tail upper=0.966404
  one further x refinement desired because nx17->33 shifted ~0.0034

rDelta=.8, rise=5 ps, R=300 ohm:
  Pcap(init)=0.767736–0.767743

rDelta=.8, rise=5 ps, R=185 ohm:
  nx=9,17,33 ->0.634,0.669,0.684; not yet x-converged.
```

At representative interior points, the `rDelta=.6` family is currently much more robust to cold zero-point spread than the `.8` family.

## 10. Critical quantum caveat

The initial harmonic Wigner state above is exact for the assumed cold quadratic well, but each sample is then propagated by the **classical nonlinear RCSJ map**.

For a closed nonlinear phase Hamiltonian,

```math
\partial_tW
=-\frac{p}{m}\partial_xW
+U'\partial_pW
-\frac{\hbar^2}{24}U'''\partial_p^3W
+O(\hbar^4).
```

The current sampled-trajectory calculation omits the Moyal terms. It is therefore a truncated-Wigner / semiclassical initial-state treatment, not exact nonlinear quantum evolution.

The current cold barrier/action ratio is only about

```text
DeltaU/(hbar omega_c) ~5.3
```

for both `.8` and `.6` retained points, and the transient hot barrier is smaller. High-fidelity claims therefore require an explicit quantum benchmark.

A fixed-hot closed-system exact-quantum quench benchmark has now been added:

```text
calculations/quantum_quench_benchmark.py
.github/workflows/experiment03-quantum-quench.yml
```

It compares split-operator Schrodinger evolution against classical propagation of the same cold Wigner distribution.

## 11. Exact harmonic quantum closures

Let

```math
\Delta U_c=(\bar\Phi^2/L)u_b,
\qquad
S=\Delta U_c/(\hbar\omega_c).
```

Then

```math
\boxed{
\sigma_x^2S
=\frac{u_b}{2\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At low temperature,

```math
\boxed{\sigma_x^2S=u_b/(2\kappa_c).}
```

For a locally planar pulled-back basin boundary at normal distance `d_n`,

```math
\boxed{P_{cap}^{local}=\Phi(d_n/\sigma_x).}
```

Thus a deterministic boundary is locally a 50% quantum-capture contour.

For persistent cold flux-state separation

```math
\Delta\Phi=\zeta\Phi_0,
\qquad
\Delta I=\zeta\Phi_0/L,
```

the harmonic width/speed/current identity is

```math
\boxed{
\sigma_x^2\tau_0\Delta I
=\frac{2\pi e\zeta}{\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right),
\qquad
\tau_0=1/\omega_c.
}
```

At low T, localization, intrinsic phase speed and circulating-current state scale cannot all be independently improved by tuning `L` and `C`.

If local capture probability `p` requires `d_n>=z_p sigma_x` and the available pulse interval satisfies `t_avail>=g tau_0`, then

```math
\boxed{
\Delta I\,t_{avail}
\ge
\frac{2\pi e\zeta g z_p^2}{\kappa_c d_n^2}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

This is a harmonic/local-basin necessary condition, not a global result for folded basins.

## 12. Causal environment is now mandatory

A physical environment cannot provide deterministic damping without associated fluctuations and quantum-escape modification.

For `q=barPhi x`, the required linear open-system form is

```math
C\ddot q(t)
+\int_{-\infty}^{t}y(t-t')\dot q(t')dt'
+\partial_qU
=I_N(t).
```

Using a two-sided symmetrized PSD convention,

```math
\boxed{
S_I^{sym}(\omega)
=\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT_b}\right)
\operatorname{Re}Y(\omega).
}
```

Current phase frequencies are about `27–32 GHz`, corresponding to `hf/k_B~1.3–1.5 K`, comparable with the `~0.6–0.8 K` transient/fold temperatures. Classical white Johnson noise is therefore not a controlled bath approximation over the phase-mode band.

The same `Y(omega)` must eventually enter

```text
real-time damping/memory,
pulse-time fluctuations,
cold dissipative MQT,
and reactive loading.
```

The old cubic `alpha_Q~7.2` MQT expression remains only a screening surrogate.

## 13. Phase-space contraction

For the scalar-R deterministic flow,

```math
\dot x=v,
\qquad
\dot v=-v/(RC)-F(x,t)/(LC),
```

```math
\boxed{\nabla\cdot\dot{\mathbf z}=-1/(RC),}
```

so infinitesimal phase-space area contracts as

```math
\boxed{J(t)=e^{-t/(RC)}.}
```

The alternating basin strips are therefore consistent with folding under a dissipatively contracting nonlinear map, not automatically numerical artifacts.

## 14. Prior-art boundary

No novelty claim is authorized.

Broad collisions include

```text
superconducting MIR/LWIR single-photon detection
photon-heated graphene Josephson switching
thermal Ic suppression -> SQUID detection
single photon -> persistent superconducting flux memory
optically written persistent flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven phase batteries/vorticity
engineered proximity ABS / induced-gap sensitivity
graphene thermal-transport optimization
generic rate-induced tipping
quantum/classical probability of Josephson basin capture
noisy graphene-JJ phase escape
frequency-dependent impedance changing retrapping
dissipation modifying macroscopic quantum tunneling.
```

The remaining possible publication route is a detector-specific **single-LWIR-photon -> nonadiabatic proximity-JJ dynamics -> persistent superconducting flux** feasibility/optimality/impossibility closure with simultaneous capture/dark/environment constraints.

## 15. Immediate work queue

1. Finish the probability-optimal scalar-R scouting scan and refine only the best points.
2. Run and validate the exact closed-system quantum quench benchmark against truncated-Wigner propagation.
3. Add a fluctuation-dissipation-consistent Ohmic bath to quantify pulse-time environmental noise at fixed `R,L,C`.
4. Replace Ohmic `R` by a low-order causal `Y(omega)` and use the same spectral density in dissipative quantum escape.
5. Add spatial electronic heat stochasticity / weak-link-weighted local state.
6. Determine whether the operating set `O(p_*,D_*)` remains nonempty.
7. Only then restore detailed 8–14-um absorptance, readout and reset.
8. If a compact closure survives, perform the narrow paper + patent collision audit.

## 16. Verdict

**GO for continued theory. NO-GO for manuscript.**

The architecture remains theoretically alive, but deterministic capture is no longer enough. The current frontier is the joint problem of **quantum initial spread, nonlinear basin geometry, causal dissipation/noise and dark quantum escape**.
