# Active Collective Receiver Refinement — What \(N^2\) Enhancement Can Really Improve

**Date:** 2026-08-08  
**Status:** **CORRECTION TO OVERSTRONG NO-GAIN LANGUAGE — COLLECTIVITY CAN REMOVE INTERNAL LOSS, BUT SATURATES AT GRAVITATIONAL MODE SELECTIVITY**

## 1. Why the earlier wording needs refinement

The repository correctly noted that in the collective-atom model of Quiñones, Oniga, Varcoe, and Wang the favorable states enhance both

- response to stochastic gravitational waves;
- vacuum gravitational transitions

with the same approximate

$$
N^2
$$

factor.

That fact does **not** imply that collective enhancement is useless for quantum reception.

If a receiver is initially dominated by nongravitational internal loss,

$$
\kappa_i\gg\kappa_g,
$$

then increasing **all gravitational couplings** by a collective factor can still raise the gravitational branching fraction toward unity.

The correct statement is more precise:

> **Collective enhancement can remove internal-loss suppression and shorten the gravitational interaction time, but if it enhances all gravitational modes equally it cannot improve the fraction of gravitational coupling belonging to the one desired source mode.**

---

# 2. Generic collective enhancement model

Let one receiver transition have baseline gravitational rates

$$
\boxed{
\kappa_{\Delta,0}
}
$$

into the selected source-difference mode and

$$
\boxed{
\kappa_{\perp,0}
}
$$

into orthogonal gravitational modes.

Define

$$
\boxed{
\kappa_{g,0}
=\kappa_{\Delta,0}+\kappa_{\perp,0}.}
$$

Let its nongravitational internal loss be

$$
\kappa_i.
$$

Now suppose a collective state multiplies the relevant quadrupole matrix-element squared by a factor

$$
\boxed{F.}
$$

If the enhancement is mode independent over the relevant gravitational continuum,

$$
\boxed{
\kappa_\Delta(F)=F\kappa_{\Delta,0},
\qquad
\kappa_\perp(F)=F\kappa_{\perp,0}.}
$$

The total receiver linewidth is then

$$
\boxed{
\kappa_{\rm tot}(F)
=F\kappa_{g,0}+\kappa_i.}
$$

---

# 3. Total gravitational branching does improve

Define the baseline ratio

$$
\boxed{
\rho_0
=\frac{\kappa_{g,0}}{\kappa_i}.}
$$

The total gravitational branching fraction is

$$
\boxed{
\beta_g(F)
=\frac{F\kappa_{g,0}}
{F\kappa_{g,0}+\kappa_i}
=\frac{F\rho_0}{1+F\rho_0}.}
$$

Thus

$$
\boxed{
\beta_g(F)\to1
\qquad(F\to\infty).}
$$

So a sufficiently large genuine matter-gravity coupling enhancement can make gravitational dynamics dominate over fixed ordinary loss.

This is a real quantum-interface improvement, not merely a larger classical output voltage.

---

# 4. Useful selected-mode branching saturates

Define the intrinsic gravitational mode selectivity

$$
\boxed{
\beta_{\rm mode}
=\frac{\kappa_{\Delta,0}}
{\kappa_{g,0}},
\qquad
0\le\beta_{\rm mode}\le1.}
$$

The fraction of the receiver's total linewidth that is useful for the selected source mode is

$$
\beta_{\rm useful}(F)
=\frac{F\kappa_{\Delta,0}}
{F\kappa_{g,0}+\kappa_i}.
$$

Therefore

$$
\boxed{
\beta_{\rm useful}(F)
=\beta_{\rm mode}
\frac{F\rho_0}{1+F\rho_0}.}
$$

As

$$
F\to\infty,
$$

$$
\boxed{
\beta_{\rm useful}(F)
\longrightarrow
\beta_{\rm mode}.}
$$

### Main result

$$
\boxed{
\text{collectivity can remove }\kappa_i\text{ from the bottleneck, but it cannot by itself make }\beta_{\rm mode}>1\text{ or improve it at all if every gravitational channel is enhanced equally.}
}
$$

This is the active analogue of the gravitational beta-factor bound.

---

# 5. Relation to the V5 free-space link

For the pointlike/aligned wave-zone receiver used in V5,

$$
\beta_{\rm mode}
$$

is the normalized source-mode overlap contained in

$$
\eta_{\rm store}
\simeq
\frac{25\mathcal O}{16(kR)^2}.
$$

If collective enhancement changes only the total quadrupole oscillator strength but not the far-field normalized emission pattern, then

$$
\boxed{
\beta_{\rm useful}(F)
\to
\eta_{\rm store}
}
$$

when gravitational coupling dominates all ordinary receiver loss.

Thus arbitrarily large collective enhancement does **not** make a point receiver absorb the entire source wavepacket. It only removes the additional suppression from internal receiver loss.

A genuine improvement beyond this limit requires changing the gravitational coupling vector itself through

- directivity;
- enclosing geometry;
- a cavity/environmental mode structure;
- another mechanism that increases source-mode overlap.

---

# 6. Required enhancement to overcome ordinary loss

To reach a desired total gravitational branching fraction

$$
0<b<1,
$$

solve

$$
\frac{F\rho_0}{1+F\rho_0}=b.
$$

Then

$$
\boxed{
F
=\frac{b}{1-b}
\frac1{\rho_0}.}
$$

For

$$
b=1/2,
$$

$$
\boxed{F=1/\rho_0.}
$$

For

$$
b=0.9,
$$

$$
\boxed{F=9/\rho_0.}
$$

Therefore an initial matter-gravity branching ratio of

$$
10^{-20}
$$

requires an enhancement of order

$$
10^{20}
$$

just to make gravitational and ordinary decay comparable.

---

# 7. Passive bright-mode scaling versus active \(N^2\) scaling

For a conventional normalized passive bright single-excitation mode, one generally expects an integrated subwavelength collective enhancement of order

$$
F\sim N.
$$

Then reaching

$$
F\rho_0\sim1
$$

requires

$$
\boxed{N\sim\rho_0^{-1}.}
$$

For the favorable active correlated states discussed by Quiñones et al., selected decay/excitation rates can scale as

$$
F\sim\frac{N^2}{4}.
$$

At the rate-model level, gravitational dominance would then require only

$$
\boxed{
N
\sim
\frac{2}{\sqrt{\rho_0}}.}
$$

This is parametrically much smaller in particle number.

But this does **not** yet establish a usable quantum receiver, because those same favorable states possess an enhanced vacuum decay channel.

---

# 8. What the 2017 collective model actually says about lifetime

Quiñones, Oniga, Varcoe, and Wang explicitly find favorable many-body states for which both

- stochastic gravitational-wave excitation/decay;
- vacuum-spacetime-fluctuation decay

receive an approximately

$$
N^2
$$

collective enhancement.

For their short-time vacuum-decay examples near the middle of the many-body ladder, the relaxation time scales as

$$
\boxed{
\tau_{\rm vac}
=\frac{4}{N^2\Gamma_0}.}
$$

Thus the very same collective factor that accelerates gravitational response also makes the prepared active state intrinsically short lived against gravitational vacuum decay.

This is not merely a generic amplifier analogy; it is explicit in the published collective gravitational master equation.

Primary source:

- D. A. Quiñones, T. Oniga, B. T. H. Varcoe, C. H.-T. Wang, **Phys. Rev. D 96, 044018 (2017)**, arXiv:1702.03905.

---

# 9. Correct interpretation of the common \(N^2\) factor

The old shorthand

> “signal and vacuum both scale as \(N^2\), so collectivity does not improve the quantum channel”

is too strong.

The common factor implies instead:

### It can improve

- total gravitational branching relative to **fixed nongravitational loss**;
- interaction bandwidth;
- response time.

### It does not automatically improve

- selected-mode fraction within the gravitational continuum;
- source-wavepacket overlap;
- signal/vacuum ratio inside the gravitational sector;
- active-state lifetime measured in units of the collectively enhanced gravitational rate.

The active state can therefore be **faster and more gravitationally dominated** without becoming more mode selective.

---

# 10. Why vacuum enhancement is not identical to thermal amplifier noise

For a passive harmonic receiver, coupling to orthogonal gravitational vacuum modes appears primarily as pure loss, not as a positive thermal occupation in the Gaussian

$$
\Phi_{\tau,m}
$$

convention.

Therefore increasing gravitational coupling relative to an occupied internal bath can genuinely improve an entanglement-preserving channel even if desired and orthogonal **vacuum** rates are enhanced together.

This is why the quantum-limited phase-insensitive amplifier toy model in `ACTIVE_RECEIVER_AMPLIFIER.md` should not be treated as an exact representation of an \(N^2\) collective gravitational transition.

The collective many-body state has a more complicated issue: it is itself excited and can make real spontaneous transitions into other internal states.

Those jumps alter the receiver state before/during capture and can generate genuine input-independent mixture/noise rather than mere attenuation.

A full channel calculation must keep that distinction.

---

# 11. Minimal active collective channel model still needed

To decide whether the favorable \(N^2\) state improves source-reference entanglement transfer, one must derive a reduced channel including at least

1. desired source-mode absorption coupling;
2. spontaneous downward gravitational transitions of the prepared receiver;
3. orthogonal gravitational modes;
4. nongravitational internal decay/dephasing;
5. state-preparation timing;
6. pump/preparation environment, if maintained actively.

The decisive quantity is not raw

$$
N^2\Gamma_0
$$

but the complete channel's entanglement-preserving margin.

For a Gaussian approximation this would be

$$
\tau-m.
$$

For the actual finite-level Dicke ladder, a non-Gaussian channel treatment is likely required.

---

# 12. A useful timed-reception interpretation

The enhanced vacuum lifetime

$$
\tau_{\rm vac}\sim1/(F\Gamma_0)
$$

does not necessarily kill the idea outright.

It means the collective active state must be prepared only shortly before the expected retarded source wavepacket arrives.

If the desired selected-mode interaction rate also scales as

$$
F\Gamma_0,
$$

then both the useful interaction window and the spontaneous-decay window shrink together.

Therefore the collective factor can make the protocol faster without parametrically increasing the number of useful coherent interaction times available before vacuum decay.

This is the temporal analogue of the mode-selectivity saturation above.

---

# 13. Consequence for the main V5 paper

The current V5 manuscript should **not** attempt to solve this active-receiver problem.

It should say:

> The passive nonrelativistic receiver bound can be evaded by active collective states. A collective factor can make gravitational coupling dominate fixed internal loss, but if it multiplies all gravitational channels equally the useful branching fraction saturates at the source-mode overlap. Known \(N^2\)-enhanced atomic states additionally acquire an \(N^2\)-enhanced vacuum decay rate, so whether they improve entanglement transfer requires a separate non-Gaussian channel analysis.

That is precise enough to close the obvious referee loophole without adding an unresolved active-receiver paper inside the source-resolved V5 manuscript.

---

# 14. Strongest next project if the active loophole is pursued separately

Construct a minimal three-state segment of the collective ladder

$$
|p-1\rangle,
\quad
|p\rangle,
\quad
|p+1\rangle
$$

near

$$
p\sim N/2,
$$

coupled to

- one selected incoming graviton wavepacket;
- the orthogonal gravitational vacuum;
- internal loss.

Then calculate the exact channel from the incoming source mode to an accessible receiver register conditioned on no/allowed spontaneous jumps.

The key scaling question is whether the optimized source-reference negativity behaves as

$$
N^2,
\quad
N,
\quad
N^0,
$$

or saturates at the gravitational mode beta factor.

That would be a distinct follow-on project rather than a necessary ingredient of V5.
