# Current State — Experiment 02

**Status:** **SECTOR-RESOLVED THEOREM VALIDATED; SUBMISSION SCIENCE FROZEN AT `3bf26c7535919597d711fdcd781e6098b76b5d68`.**

Canonical checkpoint:

`SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md`

## 1. Operational quantity

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

`Gamma_coh` is a coherent-transfer spectral area with units `s^-1`, not an information capacity or bit rate.

Use physical band frequency `omega(nu)=omega_0+nu`, lower band edge `omega_->0`, retained modal ceiling `Omega`, compact endpoint radii `a_A,a_B`, and separation axis `Rhat`.

Define

```math
I_Rhat = int rho [r^2-(Rhat.x)^2] d^3x,
Z_Rhat = int rho (Rhat.x)^2 d^3x,
I_2 = I_Rhat + Z_Rhat.
```

`I_Rhat` is the conventional moment of inertia about the line joining the endpoints.

## 2. Strongest finite-band closure

Within the retained bounded-port Markov endpoint model and outgoing compact-quadrupole TT propagation model,

```math
\boxed{
Gamma_coh <= [G Omega^4/(5 c^5)] min[G_A(R),G_B(R)]
}
```

with

```math
G_X(R)=
4 eta2bar I_Rhat,X
+ eta1bar (2 I_Rhat,X + 4 Z_Rhat,X)
+ eta0bar [(2/3) I_Rhat,X + (8/3) Z_Rhat,X],
```

where `etambar` is the supremum over the actual measured band of the exact outgoing compact-TT sector power singular value.

This form retains propagation variation over the measured band; it no longer freezes the propagator at `omega_0`.

## 3. Far-zone theorem

The exact outgoing sector powers are

```math
eta_2(z)=25(z^8-2z^6+3z^4-9z^2+9)/(16 z^10),
eta_1(z)=25(z^6-3z^4+36)/(4 z^10),
eta_0(z)=225(z^4+3z^2+9)/(4 z^10),
```

with `z=omega R/c`. Their leading orders are `R^-2`, `R^-4`, and `R^-6`, respectively. Therefore only `|m|=2` survives at leading far-zone power order.

The rigorous asymptotic theorem is

```math
\boxed{
limsup_{R->infty} R^2 Gamma_coh
<= [5 G Omega^4/(4 c^3 omega_-^2)]
min(I_Rhat,A,I_Rhat,B).
}
```

For a carrier-scale retained narrow band:

```math
\boxed{
Gamma_coh
lesssim
[5 G omega_0^2/(4 c^3 R^2)]
min(I_Rhat,A,I_Rhat,B).
}
```

This replaces the older `25/12 * min(I_2A,I_2B)` headline.

## 4. Sector-resolved endpoint completeness

For STF quadrupole projections relative to `Rhat`,

```math
sum_n Q_2,n^2/mu_n <= 4 I_Rhat,
sum_n Q_1,n^2/mu_n <= 2 I_Rhat + 4 Z_Rhat,
sum_n Q_0,n^2/mu_n <= (2/3) I_Rhat + (8/3) Z_Rhat.
```

The three right-hand sides sum to `(20/3) I_2`. For a complete displacement basis each unweighted sector projection sum is a Parseval equality.

This resolves the earlier concern that the final constant multiplied independently optimized endpoint and propagation ceilings. The leading `5/4` coefficient arises after projecting the endpoint resource into the actually propagating `|m|=2` sector.

## 5. Tightness checks

At the abstract retained-modal projection level, complete `|m|=2` Parseval saturation together with retained modes at `Omega` saturates the chained resource-propagation coefficient `5/4`. This does not establish realizability by an arbitrary homogeneous elastic body.

For an ideal slender free-free bar observed in its maximum-radiation transverse direction, the fundamental longitudinal mode occupies

```math
48/pi^4 ~= 0.493
```

of the complete leading `|m|=2` endpoint resource.

For a uniform sphere,

```math
I_Rhat=2Ma^2/5,
Z_Rhat=Ma^2/5,
```

so

```math
Gamma_coh lesssim G omega_0^2 M a^2/(2 c^3 R^2).
```

At `M=1000 kg`, `a=1 m`, `f_0=1 kHz`, and `k_0R=100`, the leading value is approximately `2.15e-39 s^-1`; the exact finite-`z` sector assembly differs by about `+0.020%` before finite-source multipole corrections.

## 6. High-frequency/off-resonant boundary

The modal expression

```math
kappa_g,n=[G omega_n^4/(5 c^5)](q_n:q_n)/mu_n
```

is an on-shell linewidth at `omega_n`. It cannot be assigned unchanged to the low-frequency tail of a far-detuned mode. Such tails require the frequency-dependent elastic/radiative response.

However, the retained-modal ceiling remains a real mathematical assumption: scalar or sector completeness controls an unweighted modal projection sum, not its fourth frequency moment. A whole-spectrum inertia-only theorem therefore needs additional constitutive regularity, microscopic cutoff information, or a different frequency-domain argument.

## 7. Generic finite-band fallback

Even without the inertia closure, retained compact-TT propagation has rank at most five and passive endpoint scattering blocks are contractions, so a finite measured band cannot acquire an unbounded transfer area merely from uncontrolled internal complexity. The resulting generic bound is much looser and contains no useful endpoint material resource.

## 8. Validation state

Validated science/manuscript SHA:

```text
3bf26c7535919597d711fdcd781e6098b76b5d68
```

All six physics workflows and the PRD manuscript workflow passed on that exact SHA. Artifact and run details are in `SECTOR_RESOLVED_THEOREM_CHECKPOINT_2026-08-10.md`.

## 9. Research mode

The hostile review triggered a legitimate theorem reopening and resulted in the stronger sector-resolved closure above. That objection is now closed at the declared model level. Further theorem work requires a new concrete technical issue, direct collision, or substantive external objection.
