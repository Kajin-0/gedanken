# Current State V7 — Equal-Charge Local Encoding and the Gravitational Quantum Link Budget

**Date:** 2026-08-08  
**Status:** **CURRENT RECOVERY POINT — READ AFTER LIVE `main` AND BEFORE `PAPER_CORE_V6_LINK_BUDGET.md`**

> Live `main` always wins. The repository may be edited concurrently. Before every write, fetch current HEAD, inspect intervening commits, and never overwrite a file from a stale SHA.

---

# 1. Project center

The active publication target is no longer a standalone Gaussian-channel theorem and no longer a single waveform/front calculation.

The strongest defensible gravity paper is a **source-resolved remote quantum-link normalization**:

$$
\boxed{
\text{equal-charge local source code}
\to
\text{conserved quadrupole}
\to
\text{gravitational source port}
\to
\text{retarded free-space mode}
\to
\text{receiver memory}
\to
\text{accessible readout}.}
$$

The candidate contribution is the closure and normalization of these interfaces in one explicit weak-gravity architecture.

Do not claim novelty for the individual ingredients.

---

# 2. Central coherent-transfer link budget

For the vacuum/coherent, narrowband linear amplitude-damping network after the local bosonic code has been instantiated,

$$
\boxed{
\tau_{A\to B}(t)
=
\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
\mathcal T_f(t).}
$$

Here

$$
\boxed{
\beta_{g,A}
=\frac{\kappa_{g,A}}{\kappa_A}}
$$

is source gravitational branching,

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2}}
$$

is normalized wave-zone source-mode capture,

$$
\boxed{
\beta_{g,B}
=\frac{\kappa_{g,B}}{\kappa_B}}
$$

is receiver gravitational branching, and

$$
\boxed{
\mathcal T_f(t)
=\kappa_B
\left|
\int_0^t ds\,
e^{-\kappa_B(t-s)/2}f(s)
\right|^2
\le1}
$$

is temporal loading.

Define

$$
\boxed{
\eta_Q^{\rm link}
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}.}
$$

Then

$$
\boxed{
\tau_{A\to B}(t)
=\eta_Q^{\rm link}\mathcal T_f(t),
\qquad
\tau_{A\to B}\le\eta_Q^{\rm link}.}
$$

This is a **coherent-transfer coefficient**, not a universal quantum-capability scalar for arbitrary non-Gaussian source/receiver noise.

Canonical notes:

- `END_TO_END_QUANTUM_LINK_BUDGET.md`
- `UNITARY_NETWORK_FACTORIZATION_CHECK.md`

---

# 3. Independent no-double-counting check

The four-factor product is reproduced without the gravitational self-energy by an explicit bosonic cascade:

$$
G
=\sqrt{\beta_{g,A}}A
+\sqrt{1-\beta_{g,A}}V_A,
$$

$$
H
=\sqrt{\eta_{\rm store}}G
+\sqrt{1-\eta_{\rm store}}V_P,
$$

followed by

$$
\dot b_B
=-\frac{\kappa_B}{2}b_B
+\sqrt{\kappa_{g,B}}\,b_{g,B}^{\rm in}
+\cdots.
$$

This yields

$$
\tau
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f.
$$

Thus source branching, propagation, receiver branching, and temporal loading are genuinely different canonical stages.

---

# 4. Friis interpretation of propagation

For the aligned plus-quadrupole channel,

$$
\boxed{G_A=G_B=5/2.}
$$

The critical reciprocal receiver effective area is

$$
A_e
=\frac{5\pi}{2k^2}
=\frac{5\lambda^2}{8\pi}.
$$

Hence

$$
\boxed{
\eta_{\rm store}
=\mathcal O G_AG_B
\left(\frac{\lambda}{4\pi R}\right)^2
=\frac{25\mathcal O}{16(kR)^2}.}
$$

The propagation stage is therefore ordinary reciprocal far-field antenna physics specialized to the spin-2 quadrupole channel.

Do not claim the coefficient or Friis structure as new.

Canonical note:

- `GRAVITATIONAL_FRIIS_LINK_FORM.md`

---

# 5. Conserved finite-spoke source

Define

$$
q=\omega L/c_s.
$$

Exact spoke/end-mass relation:

$$
\boxed{m_r/\mu=q\tan q.}
$$

Total branch-difference plus quadrupole:

$$
\boxed{
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx}.}
$$

Mode mass:

$$
\boxed{
M_{\rm eff}=4\mu A(q),
\qquad
A(q)=\frac12+\frac{q}{\sin2q}.}
$$

One-phonon quadrupole:

$$
\boxed{
q_{01}
=4\mu L\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}\omega}}.}
$$

Intrinsic graviton linewidth:

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\mathcal C_\kappa(q),}
$$

$$
\boxed{
\mathcal C_\kappa(q)
=\frac{(\tan q/q)^2}{A(q)}
=1+\frac{q^2}{3}+O(q^4).}
$$

The complete source is conserved to the working elastic/weak-field order.

Canonical source files:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`
- `QUANTIZED_PLUS_MODE_SOURCE.md`
- `DISTRIBUTED_EIGENSTRAIN_ENCODER.md`

---

# 6. Local encoder

Use a degenerate equal-charge reference qubit and branch-common work mode.

Recommended notation:

- reference qubit: \(S\) or \(Q\), not \(R\) because \(R\) is also distance;
- work mode: \(w\), not \(c\) because \(c\) is light speed;
- work coherent amplitude: \(\zeta\), not \(\beta\) because \(\beta=\omega L/c\).

Encoder:

$$
\boxed{
H_{\rm enc}
=\hbar g\sigma_z(a^\dagger w+a w^\dagger).}
$$

Lossless branch amplitudes:

$$
\alpha_s(t)
=-is\zeta\sin gt,
$$

$$
\gamma_w(t)
=\zeta\cos gt.
$$

With source damping,

$$
\Omega=\sqrt{g^2-\kappa_A^2/16},
$$

and exact controller-empty handoff time

$$
\boxed{
T_*
=\frac{
\pi-\arctan(4\Omega/\kappa_A)
}{\Omega}.}
$$

At handoff,

$$
\gamma_w(T_*)=0,
$$

$$
\alpha_s(T_*)
=-is\zeta e^{-\kappa_AT_*/4}.
$$

For coherent/vacuum inputs the work mode is factorized and branch common at handoff.

---

# 7. Encoder timing scope — causal origin is not bosonic-channel handoff

There are two distinct times.

### local causal origin

$$
\boxed{t=t_s}
$$

when the branch-controlled local intervention begins;

### fixed bosonic-code handoff

$$
\boxed{t=t_s+T_*}
$$

when the work mode is branch common and the complete branch-distance norm has reached its fixed virtual-mode value.

During the encoder, the bosonic branch separation is still being created.

Lossless example:

$$
\boxed{
N_{\Delta,{\rm all}}(t)
=4|\zeta|^2\sin^2(gt).}
$$

At the damped controller-empty handoff,

$$
\boxed{
N_{\Delta,A}(T_*)
+
\sum_jN_{\Delta,j}^{\rm enc}
=4|\zeta|^2.}
$$

After handoff, the total branch-distance norm is fixed and only redistributed by branch-independent linear dynamics.

Therefore:

$$
\boxed{
\text{during encoder: controlled qubit→multimode state generation},}
$$

$$
\boxed{
\text{after handoff: fixed virtual bosonic channel}.}
$$

The causal clock starts at

$$
t_s,
$$

not at

$$
t_s+T_*.
$$

Canonical note:

- `ENCODER_HANDOFF_CHANNEL_SCOPE.md`

---

# 8. Virtual difference-mode theorem

For coherent/vacuum linear dynamics, remove all branch-common displacements and write the complete branch-conditioned bosonic states as

$$
\boxed{
|\Psi_s\rangle
=|s\boldsymbol\alpha\rangle.}
$$

Define

$$
A=\|\boldsymbol\alpha\|
$$

and the collective difference mode

$$
\boxed{
d
=\frac1A\sum_j\alpha_j^*b_j.}
$$

A branch-independent passive mode rotation gives

$$
\boxed{
|s\boldsymbol\alpha\rangle
\to
|sA\rangle_d\otimes|0\rangle_\perp.}
$$

For a physical receiver memory branch amplitude

$$
\alpha_B,
$$

the receiver is exactly a pure-loss projection of

$$
d
$$

with

$$
\boxed{
\eta_B
=\frac{|\alpha_B|^2}{A^2}
=\frac{N_{\Delta,B}}
{N_{\Delta,{\rm all}}}.}
$$

After the encoder handoff this equals the V6 four-factor transmissivity.

This is the formal bridge from the physical local encoder to the standard binary-coherent bosonic-channel theorem.

Canonical note:

- `VIRTUAL_DIFFERENCE_MODE_REDUCTION.md`

---

# 9. Gravitational dressing and equal-charge code

Do **not** justify source locality using ordinary local-QFT commuting subalgebras.

Gauge-invariant gravitational matter operators require nonlocal dressing already perturbatively.

Use the first-order gravitational-splitting structure instead.

The two V6 branches satisfy, to the working order,

$$
\boxed{
\Delta P^\mu=0,
\qquad
\Delta M^{\mu\nu}=0.}
$$

Reason:

- total energy is parity even;
- inversion-symmetric momentum cancels;
- radial motion gives zero angular momentum;
- center of energy remains at the hub;
- reference qubit is assumed degenerate;
- ideal controller energy/momentum is branch common.

Therefore the branch pair can be assigned a common first-order standard asymptotic dressing.

The quadrupole differs but is not a Poincare charge.

Branch-dependent physical receiver response is generated by the conserved difference stress tensor

$$
\Delta T^{\mu\nu}
$$

and its retarded curvature/tidal field.

Canonical notes:

- `GRAVITATIONAL_DRESSING_CAUSALITY_REFINEMENT.md`
- `EQUAL_CHARGE_CODE_REPLACER_STATEMENT.md`

Relevant literature:

- Donnelly & Giddings, arXiv:1607.01025;
- Donnelly & Giddings, arXiv:1805.11095.

---

# 10. Correct pre-arrival replacer statement

On the equal-charge encoded code subspace,

$$
V_{\mathcal C}^\dagger O_BV_{\mathcal C}
=c_B(O_B)I_{\mathcal C}
+O(\kappa^2)
$$

for physical receiver observables before their causal past intersects the branch-dependent intervention history.

Thus

$$
\boxed{
\mathcal A_t(\rho_Q)
=\sigma_B(t)\Tr\rho_Q
+O(\kappa^2)}
$$

on that code subspace before causal arrival.

This is the properly scoped pre-arrival replacer/EB statement.

Do not claim it for arbitrary states carrying different total mass, momentum, or other asymptotic charges.

---

# 11. Retarded finite-source causal bound

For a centrally triggered source point

$$
\mathbf x_0,
$$

a material point

$$
\mathbf x
$$

cannot acquire branch dependence before

$$
t_x-t_s\ge|\mathbf x-\mathbf x_0|/c.
$$

A later disturbance reaching receiver point

$$
\mathbf y
$$

obeys

$$
 t_{\rm arr}-t_s
\ge
\frac{|\mathbf x-\mathbf x_0|+|\mathbf y-\mathbf x|}{c}
\ge
\frac{|\mathbf y-\mathbf x_0|}{c}.
$$

Thus the center-origin

$$
R/c
$$

lower bound remains valid for the centrally triggered finite source.

For arbitrary distributed interventions use the actual worldtube separation.

---

# 12. Branch-common controller radiation

A branch-common controller can radiate gravitationally without carrying which-branch information.

If the selected gravitational field branches are

$$
|\gamma_C+\alpha\rangle,
\qquad
|\gamma_C-\alpha\rangle,
$$

a common displacement removes

$$
\gamma_C.
$$

Thus

$$
N_\Delta=4|\alpha|^2
$$

and NPT/EB are unchanged by the common coherent field.

For a coherent work mode, controller fluctuations are vacuum limited and add no positive scalar occupation

$$
m.
$$

Thermal/nonclassical controller fluctuations do add noise and must be propagated separately.

Canonical note:

- `BRANCH_COMMON_CONTROLLER_RADIATION_NOISE.md`

---

# 13. Source dephasing is not a branching loss

The four-factor scalar product is exact for coherent transfer through the linear amplitude-damping network.

Pure phase diffusion can destroy entanglement without changing energy branching.

For complete phase randomization of

$$
\frac{|0\rangle|+a\rangle+|1\rangle|-a\rangle}{\sqrt2},
$$

one obtains

$$
\boxed{
\rho
=\sum_n
p_n
|\chi_n\rangle\langle\chi_n|_R
\otimes
|n\rangle\langle n|,}
$$

which is manifestly separable even if

$$
\beta_{g,A}=1.
$$

Therefore high gravitational energy branching does not by itself guarantee source coherence.

For non-Gaussian source dephasing, write a separate source channel

$$
\mathcal D_A
$$

rather than hiding it inside

$$
\beta_{g,A}
$$

or the Gaussian scalar

$$
m_A.
$$

Canonical note:

- `SOURCE_DEPHASING_BEYOND_BRANCHING.md`

---

# 14. Narrowband scope of constant branching fractions

For frequency-dependent linear port couplings,

$$
N_{\Delta,j}
=4\int\frac{d\Omega}{2\pi}
\kappa_j(\omega_0+\Omega)
|\widetilde\alpha(\Omega)|^2.
$$

The waveform-weighted gravitational fraction is

$$
\boxed{
\beta_{g,A}[\alpha]
=\frac{
\int d\Omega\,
\kappa_g(\omega_0+\Omega)
|\widetilde\alpha|^2
}{
\int d\Omega\,
\kappa_{\rm tot}(\omega_0+\Omega)
|\widetilde\alpha|^2
}.}
$$

Only in the narrowband Markov regime does this reduce to

$$
\kappa_g(\omega_0)/\kappa_{\rm tot}(\omega_0).
$$

Preserve

$$
g,\kappa_A,\kappa_B,1/T\ll\omega_0.
$$

---

# 15. Pure-loss entanglement amount

For complete vacuum link transmissivity

$$
\eta=\tau_{A\to B}
$$

and virtual branch amplitude

$$
A,
$$

define

$$
 s_E=e^{-2(1-\eta)A^2},
$$

$$
 s_B=e^{-2\eta A^2}.
$$

The exact reference–receiver negativity is

$$
\boxed{
\mathcal N(\eta,A)
=
\frac{
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
}{4}.}
$$

For fixed

$$
A>0
$$

and weak link,

$$
\boxed{
\mathcal N
=\eta
\frac{2A^2}{e^{2A^2}-1}
+O(\eta^2).}
$$

Optimizing the branch amplitude gives

$$
\boxed{
A_{\rm opt}^2
\sim\sqrt\eta,}
$$

and

$$
\boxed{
\mathcal N_{\max}(\eta)
=\eta-2\eta^{3/2}
+\frac{13}{3}\eta^2
+O(\eta^{5/2}).}
$$

Thus the deliverable entanglement is asymptotically linear in the complete weak-link transmissivity.

Canonical note:

- `EXACT_PURE_LOSS_REFERENCE_RECEIVER_NEGATIVITY.md`

---

# 16. Thermal Gaussian link and memory quantum excess

With source Gaussian noise

$$
m_A
$$

and receiver noise

$$
m_B(t),
$$

$$
\boxed{
\tau_c(t)
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f(t),}
$$

$$
\boxed{
m_c(t)
=m_B(t)
+\eta_{\rm store}\beta_{g,B}\mathcal T_f(t)m_A.}
$$

Define

$$
\boxed{
\Delta_{\rm mem}(t)
=\tau_c(t)-m_c(t).}
$$

The phase-insensitive Gaussian memory channel is non-EB iff

$$
\boxed{\Delta_{\rm mem}>0.}
$$

Equivalently,

$$
\boxed{
\eta_{\rm store}\beta_{g,B}\mathcal T_f
[\beta_{g,A}-m_A]
>m_B.}
$$

The binary-coherent NPT theorem is prior art; V7 only derives the gravitational channel parameters and physical local preparation.

---

# 17. Accessible readout is a separate final stage

The four-factor V6/V7 link ends at the receiver memory.

Append readout

$$
\Phi_r=\Phi_{\tau_r,m_r}.
$$

Then

$$
\boxed{
\tau_{\rm acc}
=\tau_r\tau_c,}
$$

$$
\boxed{
m_{\rm acc}
=m_r+\tau_r m_c.}
$$

Define

$$
\boxed{
\Delta_{\rm acc}
=\tau_{\rm acc}-m_{\rm acc}.}
$$

Then

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_{\rm mem}-m_r.}
$$

Accessible quantum capability requires

$$
\boxed{\Delta_{\rm acc}>0.}
$$

A strong absorber is not automatically an accessible quantum receiver.

Canonical note:

- `ACCESSIBLE_END_TO_END_LINK_BUDGET.md`

---

# 18. Waveform hierarchy

At fixed physical branch fractions:

### matched passive exponential

$$
\boxed{
\mathcal T_{\max}
=4e^{-2}
\simeq0.541341;}
$$

### finite local encoder + matched passive tail

$$
\boxed{
\mathcal T_{\rm full}^{\max}
=4e^{-2}
\left[
1+\left(1-\frac\pi4\right)\frac\kappa g
+O((\kappa/g)^2)
\right];}
$$

### smooth \(\sin^4\)

$$
\boxed{
\mathcal T_{\max}\simeq0.7980213;}
$$

### target-time optimized

$$
\boxed{
\mathcal T_{\rm opt}(t)
=1-e^{-\kappa_Bt}\to1.}
$$

Temporal shaping is order unity once interface branch fractions are fixed.

---

# 19. Passive source broadening no-go

At fixed intrinsic

$$
\kappa_{g,A}
$$

and receiver parameters, let

$$
r=\kappa_A/\kappa_B.
$$

Optimized passive transfer is

$$
\boxed{
\tau_{A\to B}^{\max}(r)
=4\frac{\kappa_{g,A}\kappa_\Delta}
{\kappa_B^2}
 r^{2r/(1-r)}.}
$$

Since

$$
\boxed{
\frac{d}{dr}
\ln r^{2r/(1-r)}
=
\frac{2(\ln r+1-r)}{(1-r)^2}<0,}
$$

adding passive nongravitational source damping strictly worsens end-to-end transfer.

Coherent source shaping can remove bandwidth mismatch without deliberately adding a lossy source port, but it cannot alter the branch-distance ratio of unchanged physical output couplings.

---

# 20. Coherent source shaping cost

For

$$
\alpha(t)=\alpha_{\rm pk}g(t),
$$

$$
C_g=\frac1T\int_0^T|g(t)|^2dt,
$$

$$
\boxed{
E_{\rm pk}T
=\frac{\hbar\omega}
{4\kappa_{g,A}C_g}
N_{\Delta,g}.}
$$

For

$$
g(t)=\sin^4(\pi t/T),
$$

$$
\boxed{
E_{\rm pk}T
=\frac{32}{35}
\frac{\hbar\omega}{\kappa_{g,A}}
N_{\Delta,g}.}
$$

This is an architecture-specific energy-duration relation, not a universal quantum speed limit.

---

# 21. Passive nonrelativistic class ceiling

For a passive stationary nonrelativistic quadrupole mode,

$$
\boxed{
\frac{\kappa_g}{\omega}
\lesssim
\frac23\mathcal C\beta^3.}
$$

Therefore

$$
\boxed{
\beta_g
\lesssim
\min\left[
1,
\frac23Q\mathcal C\beta^3
\right].}
$$

If both ends are in this class,

$$
\boxed{
\eta_Q^{\rm link}
\lesssim
\frac{25\mathcal O}{16(kR)^2}
\prod_{j=A,B}
\min\left[
1,
\frac23Q_j\mathcal C_j\beta_j^3
\right].}
$$

Unsaturated:

$$
\boxed{
\eta_Q^{\rm link}
\lesssim
\frac{25\mathcal O}{36(kR)^2}
Q_AQ_B
\mathcal C_A\mathcal C_B
\beta_A^3\beta_B^3.}
$$

Passive-class only.

---

# 22. Active collective receiver loophole

If a collective factor

$$
F
$$

multiplies all gravitational receiver rates while internal loss

$$
\kappa_i
$$

stays fixed,

$$
\boxed{
\beta_{\rm useful}(F)
=\beta_{\rm mode}
\frac{F\kappa_{g,0}}
{F\kappa_{g,0}+\kappa_i}.}
$$

Thus collectivity can overcome fixed internal loss and speed the interaction, but if all gravitational modes are enhanced equally,

$$
\boxed{
\beta_{\rm useful}\to\beta_{\rm mode}.}
$$

Known favorable \(N^2\) states also have \(N^2\)-enhanced gravitational vacuum decay, so a full active receiver requires separate non-Gaussian channel analysis.

Canonical note:

- `ACTIVE_COLLECTIVE_RECEIVER_REFINEMENT.md`

---

# 23. Benchmark

Use

$$
M_e=4\,{\rm kg},
\quad
L=1\,{\rm m},
\quad
f=1\,{\rm MHz},
\quad
Q=10^{12},
\quad
kR=10,
\quad
\mathcal O=1.
$$

Leading explicit four-spoke branching:

$$
\boxed{
\beta_g
\simeq1.09386\times10^{-20}.}
$$

Propagation factor:

$$
\boxed{
\eta_{\rm store}=1.5625\times10^{-2}.}
$$

Four interface cases:

### ordinary source + ordinary receiver

$$
\boxed{
\eta_Q^{\rm link}
\simeq1.87\times10^{-42};}
$$

### one ideal gravitational interface

$$
\boxed{
\eta_Q^{\rm link}
\simeq1.71\times10^{-22};}
$$

### both ideal

$$
\boxed{
\eta_Q^{\rm link}=1.5625\times10^{-2}.}
$$

Matched passive ordinary/ordinary:

$$
\boxed{
\tau_{\max}\simeq1.01\times10^{-42}.}
$$

The exact optimized pure-loss negativity is the same scale at leading order.

Intrinsic gravitational linewidth of benchmark matter:

$$
\boxed{
\kappa_g
\simeq6.87\times10^{-26}\,\mathrm{s}^{-1},}
$$

so a purely gravitational passive source lifetime is

$$
\boxed{
\kappa_g^{-1}
\simeq4.6\times10^{17}\,\mathrm{yr}.}
$$

---

# 24. Corrections that survived audit

### finite source size

$$
\boxed{
\kappa_g(q,\beta)
=\kappa_g^{(Q)}(q)
\left[
1-\frac{2a(q)}7\beta^2
+O(\beta^4)
\right],}
$$

$$
a(q)=\frac12+\frac{\cot q}{q}-\frac1{q^2}.
$$

As

$$
q\to0,
$$

$$
\boxed{
\kappa_g
=\kappa_g^{(Q)}
[1-\beta^2/21+O(\beta^4)].}
$$

### nonlinear branch-carrying quadrupole

For endpoint coordinates

$$
X=L+u,
\quad
Y=L-u,
$$

$$
\boxed{Q_{xx}-Q_{yy}=8\mu Lu}
$$

exactly. The leading \(u^2\) term is branch even and primarily dc/\(2\omega\).

### reciprocal feedback

$$
\boxed{
|L(\nu)|
\le4\eta_{\rm store}\beta_{g,A}\beta_{g,B}.}
$$

First source-controlled round-trip echo appears only after approximately

$$
3R/c.
$$

### encoder thermal noise

extra source noise is suppressed by

$$
O(\kappa_A/g)
$$

in the fast-encoder regime.

---

# 25. Novelty boundary

Do not claim novelty for

- Gaussian EB/NPT criteria;
- finite binary coherent survival;
- branch-conditioned coherent graviton radiation;
- \(N_\Delta\) normalization;
- propagating-graviton entanglement;
- resonant graviton reception;
- photon↔graviton transduction;
- cavity-QED graviton transducers;
- stimulated graviton absorption/emission;
- critical-coupling \(l=2\) cross sections;
- Friis/link-budget logic itself;
- collective gravitational transition enhancement.

The defensible candidate contribution is

$$
\boxed{
\text{one explicit locally initialized conserved remote gravitational quantum link with all interfaces normalized consistently}.}
$$

Canonical novelty files:

- `PRIOR_ART_MATRIX_V5_END_TO_END.md`
- `FINAL_TRANSDUCER_PRIOR_ART_AUDIT_V6.md`
- `STORAGE_25_OVER_16_PRIOR_ART_SCOPE.md`

---

# 26. Current manuscript status

Existing draft:

- `manuscript_v6/main.tex`
- `manuscript_v6/references.bib`

V6 is scientifically useful but **now behind the research state**.

It still needs revisions for

1. gravitational dressing/equal-charge code;
2. code-restricted pre-arrival replacer statement;
3. notation collisions:
   - reference \(R\) versus distance \(R\);
   - controller \(c\) versus light speed \(c\);
   - controller amplitude \(\beta\) versus \(\beta=\omega L/c\);
4. virtual difference-mode proof;
5. encoder handoff versus causal-origin timing;
6. source-dephasing caveat;
7. branch-common controller radiation/noise;
8. Friis interpretation;
9. exact pure-loss negativity scaling;
10. accessible readout extension;
11. Donnelly–Giddings dressing citations.

Do not treat the current LaTeX draft as referee ready until those changes are propagated.

A version bump to V7 is preferable to repeatedly patching the V6 conceptual structure.

---

# 27. Recommended V7 paper center

The main body should be organized around five logically distinct layers.

## Layer I — local equal-charge preparation

Show

$$
\Delta P^\mu=\Delta M^{\mu\nu}=0
$$

and common first-order dressing.

## Layer II — fixed bosonic handoff

At

$$
T_*,
$$

controller branch common and total branch-distance norm fixed.

Use the virtual difference mode.

## Layer III — coherent gravitational link budget

$$
\tau_c
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f.
$$

## Layer IV — noise / memory capability

$$
\Delta_{\rm mem}
=\tau_c-m_c.
$$

## Layer V — accessible readout

$$
\Delta_{\rm acc}
=\tau_r\Delta_{\rm mem}-m_r.
$$

This hierarchy is cleaner than making one waveform coefficient or one Gaussian theorem the paper's center.

---

# 28. Highest-value next work

Unless live `main` has advanced, proceed in this order:

1. **Create manuscript V7**, rather than further expanding V6.
2. Add Donnelly–Giddings dressing references and equal-charge causal-code language.
3. Use clean notation:
   - \(S\) for retained reference qubit;
   - \(w\) for work mode;
   - \(\zeta\) for work coherent amplitude;
   - \(R\) only for distance;
   - \(\beta=\omega L/c\) only for mechanical velocity parameter.
4. State explicitly that the fixed bosonic channel begins at encoder handoff
   $$
   T_*
   $$
   while the causal clock begins at
   $$
   t_s.
   $$
5. Add one compact virtual-mode lemma proving the local encoder really reduces to the binary-coherent channel form after handoff.
6. Present the four-factor scalar as a coherent-transfer budget and separate non-Gaussian source/receiver dephasing.
7. Add exact pure-loss negativity as the quantitative feasibility measure:
   $$
   \mathcal N_{\max}\sim\eta_Q^{\rm link}.
   $$
8. End the main link at the memory and append the readout condition
   $$
   \Delta_{\rm acc}=\tau_r\Delta_{\rm mem}-m_r>0.
   $$
9. Keep active collective receivers as a scoped loophole/discussion, not part of the main theorem chain.
10. Only after V7 text is stable should figures be produced.

---

# 29. Research method reminder

Continue adversarially.

For every strong sentence ask:

1. does it assume exact locality in gravity?
2. is it a source-local or true end-to-end quantity?
3. is an amplitude-damping efficiency being mistaken for phase coherence?
4. is a fixed bosonic channel being invoked before the local code is actually created?
5. is readout omitted?
6. is a standard transducer/antenna theorem being repackaged as novelty?
7. is a passive-class bound being inflated into a universal bound?

The project is strongest when each of these distinctions remains explicit.
