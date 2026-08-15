# Experiment 03 — Interface/CPR Envelope Checkpoint — 2026-08-15

## Purpose

Stress-test the favorable ideal arbitrary-length graphene fold against two effects that are known to change graphene Josephson CPRs:

1. realistic superconductor–graphene interface/contact physics;
2. self-consistent proximity depletion and current depairing.

The central result is that the usual CPR skewness `S` is **not sufficient** to determine the rf-SQUID fold. The fold is controlled much more directly by the normalized CPR slope near `phi = pi`.

This checkpoint materially weakens the earlier high-doping ideal-interface optimism and identifies a better experimental/model descriptor for the detector problem.

## 1. Literature constraint

Nanda et al., *Nano Letters* 17, 3396–3401 (2017), DOI `10.1021/acs.nanolett.7b00097`, directly measured the CPR of ballistic MoRe/graphene JJs and defined

```math
S=\frac{2\phi_{max}}{\pi}-1.
```

Their realistic-interface tight-binding calculations and measurements show:

```text
strong p doping: average S ~0.23
strong n doping: average S ~0.27
near CNP: measured S ~0.1
```

They explicitly state that skewness depends sensitively on the number of channels and on graphene–superconductor interface transparency/contact resistance. The CPR becomes approximately sinusoidal by 4.2 K because higher harmonics are thermally suppressed.

The same paper notes that earlier self-consistent theory predicted about

```text
S ~0.15
```

for n-doped `L < xi0` graphene junctions, whereas a non-self-consistent ABS-only calculation gave roughly

```text
S ~0.42.
```

Black-Schaffer and Linder, *Phys. Rev. B* 82, 184522 (2010), DOI `10.1103/PhysRevB.82.184522`, show why this matters: rigid-boundary treatments omit inverse proximity suppression in the superconductors and current depairing. Their self-consistent BdG calculation finds significantly smaller current and altered CPR shape; in short junctions current depairing can even shift the critical phase below `pi/2`, while longer junctions recover positive or only weakly negative skewness and approach harmonic behavior faster with temperature.

Therefore the ideal rigid-boundary CPR must be treated as an **upper-skew / upper-tail-slope sensitivity model**, not a realistic default.

## 2. Shape audit of the current ideal arbitrary-length model

Using the current canonical Matsubara solver at

```text
ell=L_JJ/xi0 = 1.1
delta         = 0.05
T             = 20 mK
```

the cold CPR shape is approximately:

| `mu/Delta0` | `S_cold` | `phi_max/pi` | `x_fold` | `beta_fold` | tangent slope `1/beta_fold` |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.329 | 0.665 | -0.109 | 0.463 | 2.16 |
| 10 | 0.539 | 0.769 | -0.091 | 0.325 | 3.08 |
| 20 | 0.549 | 0.774 | -0.031 | 0.201 | 4.97 |

The favorable `mu/Delta0=10–20` ideal folds therefore come from CPRs far more sawtooth-like than the experimentally representative strong-doping value `S~0.27`.

This explains why the ideal arbitrary-length model produced a very low normalized fold (`~0.2`) and a large cold barrier at `beta_cold=0.8`.

Canonical reproducibility script:

```text
calculations/arbitrary_cpr_shape_audit.py
```

## 3. Skewness is not the fold variable

Let the physical normalized CPR near `phi=pi` be

```math
j(\pi+x)
=-\chi_\pi x+\frac{\zeta_\pi}{6}x^3+O(x^5),
```

where

```math
\boxed{
\chi_\pi
=-\frac1{I_c}\left.\frac{dI_s}{d\phi}\right|_{\phi=\pi}
}
```

is the normalized **tail slope**, and

```math
\boxed{
\zeta_\pi
=\frac1{I_c}\left.\frac{d^3 I_s}{d\phi^3}\right|_{\phi=\pi}.
}
```

In the Experiment-03 canonical `x=phi-pi` convention,

```math
f(x)=\chi_\pi x-\frac{\zeta_\pi}{6}x^3+O(x^5).
```

For small external tilt `delta`, the fold conditions give

```math
\delta\simeq\frac{\beta\zeta_\pi}{3}a^3,
```

```math
\beta\chi_\pi-1
\simeq\frac{\beta\zeta_\pi}{2}a^2,
```

where `x_f=-a`.

Eliminating `a` gives the local tail formula

```math
\boxed{
\beta_{fold}
\simeq
\frac1{\chi_\pi}
\left[
1+\frac12
\left(\frac{\zeta_\pi}{\chi_\pi}\right)^{1/3}
(3\delta)^{2/3}
\right].
}
```

As `delta -> 0`,

```math
\boxed{\beta_{fold}\to1/\chi_\pi.}
```

Thus the **near-pi normalized tail slope**, not `phi_max`, is the leading cold-bistability variable.

This formula reduces to the previous sinusoidal result for `chi_pi=zeta_pi=1`.

## 4. Same measured skewness, different fold

To show explicitly that `S` does not determine the fold, construct the time-reversal-symmetric Fourier family

```math
I(\phi)
=I_0[
\sin\phi+a_2\sin2\phi+a_3\sin3\phi
].
```

For each chosen `a3`, solve analytically for `a2` so that the unique current maximum occurs at the target

```math
\phi_{max}=\frac\pi2(1+S).
```

Retain only CPRs that:

```text
are positive for 0<phi<pi
have a single interior maximum
reproduce the target S within numerical tolerance.
```

At the experimentally representative n-doped target

```text
S = 0.27
```

75 acceptable three-harmonic CPRs were found in the scanned family.

Despite having the same `S`, they span

```text
chi_pi             = 1.361 – 1.628
beta_fold(delta=.05)= 0.751 – 0.867.
```

The local `chi_pi/zeta_pi` fold formula reproduces the exact numerical folds across this accepted `S=0.27` family to within about **0.94% maximum relative error**.

This makes the result operationally useful: low-order tail derivatives summarize the fold much better than skewness.

## 5. Direct consequence for the current `beta_cold=0.8` design

For the same `S=0.27` family and

```text
beta_cold = 0.8
Ic scale  = 3 uA
delta     = 0.05
```

only

```text
28 / 75
```

accepted CPRs remain bistable.

The exact cold barriers among those surviving members span only

```text
DeltaU_c/k_B ~ 4e-4 – 0.655 K,
```

and the existing provisional cubic-MQT diagnostic gives

```text
C_min,Q ~ 11.2 pF to extremely large values near the fold.
```

The largest-barrier member of this measured-skewness envelope is therefore still dramatically less stable than the current ideal-interface `mu/Delta0=20`, `beta=0.8` point:

```text
ideal arbitrary-length model:  DeltaU_c/k_B ~16.7 K, C_min,Q ~71 fF
S=0.27 low-order envelope:      DeltaU_c/k_B <=0.655 K, C_min,Q >=11.2 pF
```

This is a **major falsification warning** for the favorable ideal-interface checkpoint.

At

```text
beta_cold = 0.9,
```

all accepted `S=0.27` family members are bistable, with

```text
DeltaU_c/k_B ~0.387 – 3.19 K
provisional C_min,Q ~0.878 – 19.7 pF.
```

Thus realistic CPR rounding may shift the useful operating region toward larger cold `beta`, at the cost of greater optical fold energy and/or larger capacitance.

## 6. Self-consistent-skewness envelope is even less decisive

For target

```text
S=0.15
```

representative of the self-consistent n-doped short-junction result cited by Nanda, the same admissible three-harmonic construction gives

```text
beta_fold(delta=.05) ~0.792 – 1.128.
```

Therefore a design with `beta_cold=0.8` is at best marginal and can easily be **monostable already in the dark** depending on the CPR tail harmonics.

Again, `S=0.15` itself does not determine which side of the fold the circuit occupies.

## 7. Why the ideal model looked much better

For the ideal rigid-boundary `mu/Delta0=20` calculation,

```text
S_cold ~0.55
x_fold ~-0.031
beta_fold ~0.201
```

so the fold tangency requires a normalized local slope

```math
\partial_x f(x_f)=1/\beta_{fold}\approx4.97.
```

By contrast, measured-skewness three-harmonic CPRs around `S=0.27` have tail slopes only about

```text
chi_pi ~1.36 – 1.63.
```

The favorable ideal corridor is therefore driven by a very steep near-`pi` CPR tail that realistic interfaces/self-consistency may strongly round.

This is now the **dominant static-model risk**.

## 8. Better experimental/model descriptor

For Experiment 03, future CPR validation should report at minimum

```text
S             phase-of-maximum skewness
chi_pi        normalized tail slope near phi=pi
zeta_pi       normalized tail cubic coefficient
Ic(T)         amplitude
```

rather than `S` or `Ic` alone.

For a finite external tilt, `chi_pi` and `zeta_pi` can already predict the fold accurately when the tangency remains near `pi`.

This suggests an experimentally practical calibration route:

```text
measure full CPR
-> fit local tail near pi
-> extract chi_pi(T), zeta_pi(T)
-> predict fold beta_f(T,delta)
-> only then optimize L, C and optical threshold.
```

## 9. Consequence for the research program

The previous conclusion

```text
"high doping buys cold stability"
```

is now **conditional on the ideal-interface CPR retaining its steep near-pi tail**.

It must not be treated as a robust material-design conclusion.

The immediate physics question becomes:

```text
What tail-slope envelope chi_pi(T), zeta_pi(T) is achievable in a realistic
intermediate-length MoRe/graphene weak link once interface transparency,
contact-induced doping, inverse proximity and current depairing are included?
```

If realistic interfaces cap `chi_pi` near the measured low-order envelope, the earlier `beta=0.8` ideal corridor largely collapses and the circuit must be re-optimized at higher `beta`.

If a steep `chi_pi >> 2` can be experimentally retained despite moderate global skewness, the favorable fold may survive even though `S` is only ~0.27. Full-CPR data, not skewness alone, are required to decide.

## 10. Reproducibility

```text
calculations/cpr_skewness_envelope.py
calculations/arbitrary_cpr_shape_audit.py
```

The first generates admissible equal-skewness Fourier CPR families and propagates them through the exact fold/barrier calculation. The second audits the skewness and fold-tail slope of the current ideal arbitrary-length model.

## Status

**GO for continued theory, but the high-doping ideal-interface optimism is downgraded. NO-GO for manuscript.**
