# Gravitational Dressing and the Causal Source-Controlled Channel

**Date:** 2026-08-08  
**Status:** **CAUSALITY SCOPE CORRECTION — REPLACES OVERSTRONG LOCAL-QFT MICROCAUSALITY LANGUAGE FOR GRAVITY**

## 1. Why the previous wording is too strong

Earlier notes sometimes justified the pre-arrival receiver channel by importing the ordinary local-QFT statement

$$
[O_A,O_B]=0
$$

for spacelike separated source and receiver regions and then declaring the source-controlled receiver map to be an exact replacer channel.

That logic is too naive for gravity.

In a diffeomorphism-invariant gravitational theory, matter operators with nonzero Poincare charges must be gravitationally dressed. The dressing extends outside the nominal matter support, and physical observables do not organize into the same exactly local commuting subalgebras as nongravitational local QFT.

Donnelly and Giddings make this obstruction explicit already in perturbation theory about flat spacetime:

- W. Donnelly and S. B. Giddings, **“Observables, gravitational dressing, and obstructions to locality and subsystems,”** arXiv:1607.01025.
- W. Donnelly and S. B. Giddings, **“Gravitational splitting at first order: Quantum information localization in gravity,”** arXiv:1805.11095.

Therefore the V6 paper should **not** claim an exact nonperturbative tensor-factorized local source subsystem or derive causality solely from a local-operator commutator theorem.

The needed statement is narrower and survives.

---

# 2. What gravitational splitting gives at first order

The first-order gravitational-splitting construction shows that suitably dressed states localized to a region can be chosen so that measurements outside an enlarged neighborhood are insensitive to their internal information except through the total Poincare charges.

At leading order in the gravitational coupling, the exterior metric matrix elements depend on

$$
\boxed{
P_\mu
}
$$

and

$$
\boxed{
M_{\mu\nu}
}
$$

of the dressed source state, rather than on arbitrary internal details of the matter distribution.

Thus, for a subspace whose states have the same matrix elements of these charges, one can choose a common standard dressing such that the internal quantum information is not encoded in distinct asymptotic Coulombic fields to this order.

This is the correct perturbative localization structure to use for V6.

It is approximate and first order; it is not an assertion of exact locality in full quantum gravity.

---

# 3. Equal-charge condition for the two source branches

The V6 source branches are related by plus-mode parity. To the working order they have the same total Poincare charges.

Write the difference between the two branch charges as

$$
\boxed{
\Delta P^\mu
=P_+^\mu-P_-^\mu,
}
$$

$$
\boxed{
\Delta M^{\mu\nu}
=M_+^{\mu\nu}-M_-^{\mu\nu}.
}
$$

For the ideal source architecture,

$$
\boxed{
\Delta P^\mu=0,
\qquad
\Delta M^{\mu\nu}=0
}
$$

to the order retained in the elastic/weak-field model.

The individual components can be checked explicitly.

---

# 4. Equal total energy

The two mechanical branches are

$$
 u_+(t)=+u(t),
\qquad
u_-(t)=-u(t).
$$

The mechanical Hamiltonian is parity even,

$$
H_m(-u,-p_u)=H_m(u,p_u).
$$

Therefore the source-mode energy is the same in both branches.

At the distributed-elastic level,

- kinetic energy densities depend on
  $$
  \dot\xi^2;
  $$
- linear elastic energy densities depend quadratically on strain relative to the branch-controlled eigenstrain;
- the controlled-parity/eigenstrain architecture makes the leading controller backreaction energy branch common.

Thus

$$
\boxed{\Delta P^0=0}
$$

for the ideal branch pair to the working order.

The retained reference qubit is assumed degenerate in the branch basis, so it contributes no branch-dependent rest-energy splitting.

A branch-common controller or work reservoir may carry a large energy, but by construction its contribution to

$$
P^0
$$

is the same in both branches.

---

# 5. Equal total spatial momentum

The four-spoke plus mode is inversion symmetric.

For each spoke element or endpoint at

$$
+\mathbf x,
$$

there is an identical partner at

$$
-\mathbf x
$$

with opposite physical velocity vector under the radial plus motion.

Their linear momenta cancel pairwise.

Hence, for each branch separately,

$$
\boxed{\mathbf P_{\rm mech}=0.}
$$

The compact hub has no net force in the ideal plus mode, and the controller contribution is branch common.

Therefore

$$
\boxed{\Delta P^i=0.}
$$

---

# 6. Equal angular momentum

The ideal spoke/end-mass motion is radial along the coordinate axes.

For each material element,

$$
\mathbf r\parallel\mathbf p,
$$

so its orbital contribution

$$
\mathbf r\times\mathbf p
$$

vanishes.

Opposite-spoke tractions also produce zero net torque at the hub.

The plus mode therefore has

$$
\boxed{\mathbf J_{\rm mech}=0}
$$

in both branches.

Any internal reference/control angular momentum is assumed branch common in the ideal encoder.

Thus

$$
\boxed{\Delta M^{ij}=0.}
$$

---

# 7. Equal boost / center-of-energy charges

The mixed Lorentz charges

$$
M^{0i}
$$

are tied to the total momentum and center of energy.

By inversion symmetry the center of energy of the four-spoke source remains at the hub in both mirrored branches. Since the total spatial momentum also vanishes,

$$
\boxed{\Delta M^{0i}=0}
$$

to the working order.

This condition is stronger than merely requiring zero mass dipole of the endpoint masses; it applies to the complete symmetric source including spoke and ideal branch-common controller energy.

Finite hub/controller asymmetries are a separate correction already bounded in

`HUB_CONTROLLER_RESIDUAL_BOUND.md`.

---

# 8. The quadrupole can differ without changing the Poincare charges

The intended branch signal is

$$
\boxed{
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx}.}
$$

This does not contradict

$$
\Delta P^\mu=0,
\qquad
\Delta M^{\mu\nu}=0.
$$

The quadrupole is not a global Poincare charge.

Thus the two branches can share the same asymptotic charge dressing while differing in internal quadrupolar structure and subsequently emitting branch-dependent radiation when that structure is changed dynamically.

This is exactly the separation needed by the source-resolved protocol:

$$
\boxed{
\text{common asymptotic charge dressing}
\quad+\quad
\text{retarded branch-dependent multipole radiation}.}
$$

---

# 9. Controlled difference stress tensor

Define the branch-difference complete source stress tensor

$$
\boxed{
\Delta T^{\mu\nu}(x)
=T_+^{\mu\nu}(x)-T_-^{\mu\nu}(x).}
$$

Because both branches are individually conserved,

$$
\boxed{
\partial_\mu\Delta T^{\mu\nu}=0.}
$$

Choose the two complete histories to be identical before a local source intervention begins at

$$
t=t_s.
$$

Then

$$
\boxed{
\Delta T^{\mu\nu}(x)=0
\qquad
\text{before the intervention support}.}
$$

In the linearized retarded solution, the controlled metric difference is schematically

$$
\boxed{
\Delta\bar h_{\mu\nu}(t,\mathbf x)
=\frac{4G}{c^4}
\int d^3x'
\frac{
\Delta T_{\mu\nu}
(t-|\mathbf x-\mathbf x'|/c,\mathbf x')
}{|\mathbf x-\mathbf x'|}
}
$$

in harmonic-gauge notation, with the physical receiver response ultimately expressed through gauge-invariant curvature/tidal observables.

The key property is support, not gauge notation:

> **The retarded controlled difference vanishes at a receiver event whose past light cone does not intersect the branch-dependent intervention history.**

No instantaneous branch-dependent radiative or tidal signal is generated by changing the internal equal-charge source state.

---

# 10. Common dressing versus retarded radiation

The full physical gravitational state contains more than the radiative TT field.

It may contain

- Coulombic/constraint dressing associated with total charges;
- branch-common controller fields;
- vacuum correlations;
- radiative gravitons.

The V6 causal observable is the **controlled difference** between two equal-charge histories with the same chosen standard dressing before the intervention.

To first order in weak gravity:

### common charge dressing

is the same in the two branches and cancels from the controlled difference;

### pre-existing vacuum correlations

are common to the histories and cannot by themselves encode the later branch choice in the receiver reduced state;

### branch-dependent multipole response

is generated by

$$
\Delta T^{\mu\nu}
$$

and propagates with the retarded Green function.

This is the correct operational decomposition for the manuscript.

---

# 11. Receiver observable should be gauge invariant

The receiver should not be described as measuring a coordinate-dependent metric component at a point.

A physical mechanical receiver couples through gauge-invariant local tidal response, e.g. the electric Weyl/Riemann tensor in the detector frame,

$$
\boxed{
\mathcal E_{ij}
=R_{0i0j}
}
$$

at linear order, or equivalently through the already derived quadrupole input-output coupling after gauge-invariant reduction.

The source-controlled receiver signal is therefore the change in an actual detector degree of freedom driven by the retarded curvature field.

For the conserved source difference,

$$
\boxed{
\Delta\mathcal E_{ij}(x)=0
}
$$

outside the causal future of the branch-dependent intervention in the working retarded linearized model.

This is safer than asserting that an undressed local metric operator commutes exactly with a compact source operator.

---

# 12. Correct pre-arrival channel statement

The old strong wording was

> “By microcausality the exact source-to-receiver channel is a replacer before \(R/c\).”

Replace it with:

> **Within the perturbative linearized-gravity model, choose the branch inputs to have identical Poincare charges and a common standard asymptotic dressing before the local intervention. The branch-dependent complete stress history then has retarded support. For any receiver observable constructed from the local physical detector response, the controlled output is independent of the branch input until the receiver event lies in the causal future of that intervention. Relative to this controlled equal-charge encoding, the pre-arrival map is therefore input independent (replacer/EB) to the working order.**

Symbolically,

$$
\boxed{
\mathcal A_{\rm ctrl}(t)[\rho_S]
=\sigma_B(t)\,\Tr\rho_S
+O(G^2,\text{model corrections})
}
$$

before causal arrival, where the correction notation emphasizes that the statement belongs to the perturbative model rather than to a claimed exact nonperturbative subsystem factorization of quantum gravity.

---

# 13. Finite source support and the \(R/c\) lower bound

The exact causal statement is formulated using the source-intervention worldtube

$$
\mathcal W_A
$$

and the receiver worldtube

$$
\mathcal W_B.
$$

For a centrally triggered extended source, let

$$
\mathbf x_0
$$

be the local trigger location. Causality of the source material implies a source point

$$
\mathbf x
$$

cannot acquire branch dependence before

$$
 t_x-t_s
\ge
\frac{|\mathbf x-\mathbf x_0|}{c}
$$

(or more strongly using the actual material signal speed where appropriate).

A disturbance emitted there and received at

$$
\mathbf y
$$

must satisfy

$$
 t_{\rm arr}-t_s
\ge
\frac{|\mathbf x-\mathbf x_0|+|\mathbf y-\mathbf x|}{c}.
$$

The triangle inequality gives

$$
\boxed{
 t_{\rm arr}-t_s
\ge
\frac{|\mathbf y-\mathbf x_0|}{c}.}
$$

Thus the familiar center-origin

$$
R/c
$$

lower bound survives for a centrally triggered extended source.

For a generic distributed intervention, the paper should use the minimum null separation of the actual operation and receiver supports rather than a center-to-center shorthand.

---

# 14. What this does not prove

This note does **not** prove

- exact tensor factorization of the Hilbert space into source, gravity, and receiver subsystems in full quantum gravity;
- exact commuting compactly localized gauge-invariant observables;
- all-orders gravitational splitting;
- absence of nonperturbative soft/infrared structure;
- absence of pre-existing source-field or field-receiver correlations.

Those statements would exceed the scope of the weak linearized construction.

The result needed by V6 is more modest:

$$
\boxed{
\text{equal-charge branch information can be given common first-order dressing, while the controlled branch-dependent receiver response is retarded.}
}
$$

That is sufficient for the operational causal link budget developed in the manuscript.

---

# 15. Manuscript consequences

The V6 causality section should be revised in four ways.

## 15.1 Remove exact local-QFT microcausality language

Do not say that gravity has ordinary compactly supported commuting source and receiver algebras.

## 15.2 State the equal-charge condition

Include

$$
\boxed{
\Delta P^\mu=0,
\qquad
\Delta M^{\mu\nu}=0
}
$$

to the working order for the encoded branch pair.

## 15.3 Use a common standard dressing

State that the two equal-charge branches are compared with the same asymptotic charge dressing in the perturbative gravitational-splitting sense.

## 15.4 Define causality through the controlled retarded detector response

Use

$$
\Delta T^{\mu\nu}
\to
\Delta R_{0i0j}
\to
\text{receiver mode}
$$

rather than a bare local metric-operator commutator.

---

# 16. Strongest corrected causal statement

> **Gravity obstructs exact local subsystem factorization because gauge-invariant matter operators carry nonlocal gravitational dressing. The present Gedankenexperiment does not require such a factorization. The two source branches are engineered to have identical total Poincare charges and therefore admit a common standard asymptotic dressing at first perturbative order. Their controlled difference stress tensor is conserved and begins only with the local source intervention. The branch-dependent tidal field and receiver response are consequently retarded. Before the receiver lies in the causal future of the intervention, the controlled equal-charge input cannot change the receiver output within the working linearized model, so the corresponding difference channel is input independent/entanglement breaking to that order.**

This should replace the stronger microcausal-replacer claim in the main paper.
