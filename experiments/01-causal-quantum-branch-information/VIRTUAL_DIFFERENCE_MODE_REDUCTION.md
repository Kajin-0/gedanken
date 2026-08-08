# Virtual Difference-Mode Reduction for the Locally Encoded Source

**Date:** 2026-08-08  
**Status:** **EXACT VACUUM/COHERENT LINEAR-NETWORK REDUCTION — JUSTIFIES APPLYING BINARY-COHERENT CHANNEL RESULTS AFTER LOCAL ENCODING**

## 1. Conceptual gap being closed

The V6 local protocol begins with

- a reference qubit;
- a branch-common coherent work mode;
- the mechanical source in vacuum;
- vacuum field/loss ports.

The source qubit controls the sign of a linear source/work interaction. It does **not** begin with a bosonic source mode already entangled with the reference in the textbook state

$$
\frac{|+\rangle|+a\rangle+|-\rangle|-a\rangle}{\sqrt2}.
$$

A referee can therefore ask:

> Why is it legitimate to use the known binary-coherent entanglement-survival theorem for a bosonic channel to infer NPT of the final reference–receiver state?

For the ideal coherent/vacuum linear network, the answer is exact.

The complete controlled evolution creates two multimode coherent states whose displacement vectors differ only by sign after common displacements are removed. A branch-independent mode rotation compresses that entire branch difference into one **virtual collective bosonic mode**. The physical receiver is then exactly one pure-loss projection of that virtual mode.

Thus the final reference–receiver state is unitarily equivalent to the output of a standard binary-coherent probe sent through a one-mode attenuator, even though the one-mode probe is an emergent collective coordinate rather than a literal input oscillator present before the encoder.

---

# 2. Global branch-conditioned coherent states

Let the total branch-sensitive linear bosonic degrees of freedom at some chosen final time include

- residual source mechanics;
- controller/work modes;
- emitted gravitational modes;
- nongravitational source-loss modes;
- receiver mode;
- receiver output/loss modes.

Collect their annihilation operators into a column vector

$$
\mathbf b
=(b_1,b_2,\ldots,b_N)^T
$$

or the corresponding continuum generalization.

For branch

$$
s=\pm1,
$$

the ideal controlled-parity linear dynamics produce a coherent Gaussian state

$$
\boxed{
|\Psi_s\rangle
=|\boldsymbol\gamma+s\boldsymbol\alpha\rangle,}
$$

where

- \(\boldsymbol\gamma\) is the complete branch-common displacement vector;
- \(\boldsymbol\alpha\) is the branch-odd displacement vector.

All branch covariances are vacuum because the input states are coherent/vacuum and the conditional bosonic dynamics are passive linear transformations plus displacements.

A branch-independent multimode displacement removes

$$
\boldsymbol\gamma.
$$

Therefore the entanglement-relevant state is unitarily equivalent to

$$
\boxed{
|\Psi_s\rangle
\sim
|s\boldsymbol\alpha\rangle.}
$$

---

# 3. Total branch distance

The coherent-state separation between the two global branch states is

$$
\Delta\boldsymbol\alpha
=(+\boldsymbol\alpha)-(-\boldsymbol\alpha)
=2\boldsymbol\alpha.
$$

Hence the total squared coherent-state distance is

$$
\boxed{
N_{\Delta,{\rm all}}
=\|\Delta\boldsymbol\alpha\|^2
=4\|\boldsymbol\alpha\|^2.}
$$

This norm includes every physical subsystem that still carries a branch record at the chosen time.

If the source/control cycle has completely emptied into output ports, this is the total emitted branch distance.

At finite time, residual source/controller branch amplitudes simply contribute additional components of

$$
\boldsymbol\alpha.
$$

Nothing in the reduction requires the source to have fully decayed.

---

# 4. Define the virtual difference mode

Let

$$
\boxed{
A\equiv\|\boldsymbol\alpha\|.}
$$

For

$$
A>0,
$$

define the normalized collective annihilation operator

$$
\boxed{
 d
=\frac{1}{A}
\sum_j\alpha_j^*b_j
}
$$

with the corresponding continuum inner product when needed.

Because

$$
\sum_j|\alpha_j|^2=A^2,
$$

$$
[d,d^\dagger]=1.
$$

Complete

$$
d
$$

to an orthonormal bosonic mode basis

$$
(d,e_2,e_3,\ldots).
$$

This is implemented by a branch-independent passive Gaussian unitary

$$
U_{\rm mode}.
$$

Under that mode rotation,

$$
\boxed{
U_{\rm mode}
|s\boldsymbol\alpha\rangle
=|sA\rangle_d
\otimes
|0\rangle_{e_2}
\otimes
|0\rangle_{e_3}
\otimes\cdots.}
$$

Thus **all branch distinguishability lives in one virtual bosonic mode**.

The construction is exact for coherent branch states, regardless of how many physical source, field, or environmental modes participate.

---

# 5. Reference-entangled global state

The total state including the retained logical reference is therefore

$$
|\Omega\rangle
=\frac{1}{\sqrt2}
\left(
|+\rangle_R
|+\boldsymbol\alpha\rangle
+
|-\rangle_R
|-\boldsymbol\alpha\rangle
\right)
$$

after removal of branch-common displacement.

Applying

$$
U_{\rm mode}
$$

to the bosonic degrees of freedom gives

$$
\boxed{
(I_R\otimes U_{\rm mode})|\Omega\rangle
=
\frac{
|+\rangle_R|+A\rangle_d
+|-\rangle_R|-A\rangle_d
}{\sqrt2}
\otimes|0\rangle_\perp.}
$$

This is exactly the standard binary-coherent hybrid entangled state on

$$
R\otimes d.
$$

The virtual mode

$$
d
$$

need not have existed as a physical oscillator before the local encoder. It is a collective mode of the **final branch-difference displacement vector**.

Entanglement is invariant under the branch-independent mode rotation, so this representation is physically exact for the bipartitions of interest.

---

# 6. Isolating the physical receiver mode

Let

$$
b_B
$$

be the physical accessible receiver memory mode at the chosen time.

Its branch-odd coherent amplitude is one component

$$
\alpha_B
$$

of

$$
\boldsymbol\alpha.
$$

Define

$$
\boxed{
\eta_B
\equiv
\frac{|\alpha_B|^2}{A^2}
=
\frac{N_{\Delta,B}}
{N_{\Delta,{\rm all}}}.}
$$

Then

$$
0\le\eta_B\le1.
$$

Because

$$
b_B
$$

is one normalized projection of the global difference mode, there exists a normalized orthogonal collective mode

$$
e
$$

such that

$$
\boxed{
 b_B
=\sqrt{\eta_B}\,d
+\sqrt{1-\eta_B}\,e.}
$$

The orthogonal input mode

$$
e
$$

is vacuum in the mode-rotated representation.

Therefore the reduced map

$$
d\to b_B
$$

is exactly a pure-loss channel

$$
\boxed{
\mathcal L_{\eta_B}.}
$$

No approximation has been made beyond the coherent/vacuum linear-network assumptions.

---

# 7. Reduced reference–receiver state

Tracing every physical bosonic degree of freedom except the receiver gives

$$
\boxed{
\rho_{RB}
=
(I_R\otimes\mathcal L_{\eta_B})
\left[
|\Phi_A\rangle\langle\Phi_A|
\right],}
$$

where

$$
\boxed{
|\Phi_A\rangle
=
\frac{
|+\rangle_R|+A\rangle_d
+|-\rangle_R|-A\rangle_d
}{\sqrt2}.}
$$

Thus the locally encoded source protocol produces **exactly the same reference–receiver state** as a standard binary-coherent entangled probe sent through a pure-loss channel of transmissivity

$$
\eta_B.
$$

This is the missing bridge between the physical local encoder and the abstract binary-coherent channel theorem.

---

# 8. Identification with the V6 four-factor link budget

For the vacuum-source one-way link, the receiver branch-distance fraction is

$$
\boxed{
\eta_B(t)
=
\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
\mathcal T_f(t).}
$$

Therefore

$$
\boxed{
\eta_B(t)
=\tau_{A\to B}(t).}
$$

The V6 coherent-transfer parameter is literally the fraction of the complete branch-difference coherent-state norm that resides in the accessible receiver memory mode.

This gives an especially transparent interpretation:

$$
\boxed{
\tau_{A\to B}(t)
=
\frac{
N_{\Delta,B}(t)
}{
N_{\Delta,{\rm all}}
}}
$$

for the ideal coherent/vacuum unitary dilation, with the logical branch amplitude normalized to the total difference mode.

Equivalently, in amplitude form,

$$
\boxed{
|\alpha_B|
=\sqrt{\tau_{A\to B}}\,A.}
$$

---

# 9. Why residual source branch information is already included

At finite time, the mechanical source may still carry branch amplitude

$$
\alpha_A(t).
$$

That amplitude is simply another component of

$$
\boldsymbol\alpha.
$$

Likewise uncollected gravitational radiation and ordinary source-loss outputs occupy other components.

Tracing them is exactly the complementary channel of

$$
\mathcal L_{\eta_B}.
$$

Therefore no extra ``residual source decoherence factor'' should be multiplied onto

$$
\tau_{A\to B}
$$

in the ideal linear coherent model.

Doing so would double count the complementary branch record.

The pure-loss reduction already knows that all norm not present in

$$
b_B
$$

is in the environment.

---

# 10. Why the local encoder precursor is also included

Radiation emitted during the finite encoder contributes components to

$$
\boldsymbol\alpha.
$$

Later passive-tail radiation contributes additional temporal components.

The complete source waveform

$$
f_{\rm full}(t)
$$

is just a convenient basis choice for the gravitational portion of that total branch-difference vector.

Whether a graviton was emitted

- during the local encoder;
- during the passive tail;
- during an actively shaped pulse

is irrelevant to the difference-mode reduction.

The receiver only sees the projection of the complete displacement vector onto its accepted temporal/spatial mode.

This is why the finite encoder precursor can be included coherently rather than treated as an additional uncontrolled source of decoherence.

---

# 11. Relation to the binary-coherent NPT theorem

The reduced state has exactly the form obtained by applying a one-mode attenuator to one half of a binary-coherent hybrid entangled state.

Therefore all established results for such probes apply directly.

In particular, for an ideal pure-loss receiver projection,

$$
\eta_B>0
$$

preserves NPT for every finite nonzero coherent branch amplitude.

For the noisy phase-insensitive Gaussian extension

$$
\Phi_{\tau,m},
$$

the known NPT/non-EB threshold can be applied after the effective receiver map has been derived.

The novelty of V6 is not this Gaussian theorem. The important result here is that the **locally initialized gravitational source protocol is exactly reducible to the theorem's input structure in the vacuum/coherent linear limit**.

---

# 12. Extension to common Gaussian covariance

The coherent/vacuum case is exact and sufficient for the clean V6 benchmark.

A partial generalization is possible when the two branch-conditioned global bosonic states are displaced versions of the same Gaussian covariance matrix,

$$
\rho_s
=D(s\boldsymbol\alpha)
\rho_0
D^\dagger(s\boldsymbol\alpha).
$$

A symplectic/mode transformation can still align the displacement vector with one canonical mode, but the covariance need not factor into

$$
\rho_d\otimes\rho_\perp.
$$

Correlations between the difference mode and orthogonal modes can therefore make the reduced channel more general than pure loss.

This is the correct place for source thermal/controller noise to enter.

The clean scalar link budget then remains the coherent-transfer part, while the covariance/noise matrix must be propagated separately.

---

# 13. Pure dephasing and nonlinear noise are outside the pure-loss reduction

The exact virtual-mode proof assumes the branch-conditioned bosonic evolution remains linear Gaussian with coherent/vacuum inputs.

Mechanisms such as

- phonon-number dephasing;
- stochastic frequency noise;
- nonlinear loss;
- non-Gaussian controller noise

need not be representable as passive redistribution of one coherent displacement vector.

They can reduce reference–receiver entanglement even when the energy branching fractions are unchanged.

Thus the V6 link formula

$$
\tau
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f
$$

should be described as the **coherent-transfer coefficient** of the linear network, with non-amplitude-damping source noise included separately in the channel-noise model.

---

# 14. Strongest theorem-style statement

### Virtual difference-mode theorem for the V6 vacuum network

Consider a controlled linear bosonic network with a two-level reference label

$$
s=\pm1,
$$

coherent/vacuum bosonic inputs, and branch-conditioned output states that differ only by the sign of a displacement vector after branch-common displacements are removed:

$$
|\Psi_s\rangle=|s\boldsymbol\alpha\rangle.
$$

Then there exists a branch-independent passive Gaussian unitary mapping the full bosonic output to

$$
|sA\rangle_d\otimes|0\rangle_\perp,
\qquad
A=\|\boldsymbol\alpha\|.
$$

For any selected physical output mode

$$
b_B
$$

with branch amplitude

$$
\alpha_B,
$$

the reduced reference–output state is exactly equal to the state produced by sending the virtual mode

$$
d
$$

through a pure-loss channel with

$$
\boxed{
\eta_B=|\alpha_B|^2/A^2.}
$$

Applied to the V6 gravitational network,

$$
\boxed{
\eta_B(t)
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).}
$$

This theorem closes the formal gap between the local source encoder and the one-mode binary-coherent entanglement witness.

---

# 15. Manuscript consequence

The main paper should add one compact paragraph before invoking the Gaussian NPT theorem:

> Although the physical protocol begins with a reference qubit, a branch-common work mode, and source vacuum rather than a pre-existing qubit–bosonic entangled state, the vacuum linear network admits an exact virtual difference-mode reduction. After branch-common displacements are removed, the complete two branch outputs are opposite multimode coherent displacement vectors. A branch-independent passive mode rotation concentrates this displacement into one collective bosonic mode. The physical receiver is a pure-loss projection of that mode with transmissivity equal to the receiver's fraction of the total branch-distance norm, which is precisely the four-factor link coefficient. The reduced reference–receiver state is therefore exactly of the standard binary-coherent channel form.

This is a stronger and cleaner justification than simply calling the local encoder ``equivalent'' to an initial coherent probe without proving the equivalence.
