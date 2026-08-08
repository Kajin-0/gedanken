# Branch-Common Controller Radiation — Displacement Versus Genuine Channel Noise

**Date:** 2026-08-08  
**Status:** **SOURCE-LOOP CLOSURE — COMMON CONTROLLER RADIATION DOES NOT CARRY WHICH-BRANCH INFORMATION, BUT NONVACUUM CONTROLLER FLUCTUATIONS MUST BE COUNTED**

## 1. Question

The V6 local source uses a branch-common work/controller subsystem to prepare opposite source amplitudes while avoiding a hidden which-branch record.

Even if the controller stress-energy is identical in the two branches, a moving or time-dependent controller can still radiate gravitationally.

A referee can therefore ask:

> Does branch-common controller radiation invalidate the source→receiver channel by adding a large uncontrolled field at the receiver?

The answer separates cleanly into two pieces:

1. a **deterministic/common coherent displacement**, which does not affect entanglement or the entanglement-breaking boundary;
2. controller **quantum/statistical fluctuations**, which can add genuine channel noise and must be included if they exceed vacuum.

---

# 2. Branch-conditioned gravitational field with a common controller component

Let the gravitational field selected by the receiver contain

- a branch-common controller amplitude
  $$
  \gamma_C;
  $$
- a branch-odd source amplitude
  $$
  \pm\alpha.
  $$

Then the two gravitational branch states are

$$
\boxed{
|\psi_+\rangle_G
=|\gamma_C+\alpha\rangle,
\qquad
|\psi_-\rangle_G
=|\gamma_C-\alpha\rangle.}
$$

Apply the branch-independent displacement

$$
D(-\gamma_C).
$$

It gives

$$
\boxed{
D(-\gamma_C)|\psi_\pm\rangle
=|\pm\alpha\rangle}
$$

up to the irrelevant coherent-state phase convention.

Thus the common controller field is related to the zero-background problem by a local unitary on the gravitational mode.

---

# 3. Branch distance is unchanged

The branch coherent-state separation is

$$
\Delta\alpha
=(\gamma_C+\alpha)-(\gamma_C-\alpha)
=2\alpha.
$$

Therefore

$$
\boxed{
N_\Delta
=|\Delta\alpha|^2
=4|\alpha|^2}
$$

is completely independent of the common controller displacement.

Likewise the branch overlap is

$$
\left|\langle\gamma_C+\alpha
|\gamma_C-\alpha\rangle\right|
=e^{-2|\alpha|^2},
$$

again independent of

$$
\gamma_C.
$$

Therefore deterministic branch-common controller radiation carries no which-branch information.

---

# 4. Receiver channel covariance under common displacement

For a phase-insensitive Gaussian channel

$$
\Phi_{\tau,m},
$$

displacements transform covariantly:

$$
\boxed{
\Phi_{\tau,m}
\bigl[D(\gamma)\rho D^\dagger(\gamma)\bigr]
=
D(\sqrt\tau\,\gamma)
\Phi_{\tau,m}(\rho)
D^\dagger(\sqrt\tau\,\gamma).}
$$

Thus an input controller displacement produces only a branch-common receiver displacement.

A local displacement on the receiver does not change

- positivity of the partial transpose;
- negativity;
- separability;
- whether the channel is entanglement breaking.

Therefore

$$
\boxed{
\text{a known branch-common coherent gravitational drive does not alter the V6 NPT/non-EB condition.}}
$$

It may be experimentally inconvenient because it can consume dynamic range, but that is a measurement-engineering issue rather than a loss of quantum branch coherence.

---

# 5. Linear-network interpretation

Let the selected incident receiver mode be

$$
H
=t_A A+t_C C+\sum_r t_rV_r,
$$

where

- \(A\) carries the source branch information;
- \(C\) is the controller gravitational output mode;
- the \(V_r\) are vacuum/environmental modes.

Suppose

$$
C|\gamma_C\rangle
=\gamma_C|\gamma_C\rangle.
$$

Then

$$
H
=t_A A
+t_C\gamma_C
+t_C\delta C
+\sum_r t_rV_r,
$$

where

$$
\delta C=C-\gamma_C.
$$

The mean term

$$
t_C\gamma_C
$$

is just a receiver displacement.

Only the fluctuations

$$
\delta C
$$

can contribute genuine input-independent channel noise.

---

# 6. Coherent controller state is vacuum limited

For a coherent controller state,

$$
|\gamma_C\rangle,
$$

the fluctuation mode

$$
\delta C
$$

has vacuum covariance:

$$
\boxed{
\langle\delta C^\dagger\delta C\rangle=0.}
$$

Therefore a linear gravitational coupling from a coherent work mode contributes

- a common coherent displacement;
- ordinary vacuum fluctuations required by the canonical transformation;
- **no positive vacuum-output occupation** in the repository's Gaussian \((\tau,m)\) convention.

Hence the ideal coherent work reservoir assumed by the local encoder does not generate an additional thermal-noise parameter merely because its mean motion is large.

This is the same reason a strong coherent optical pump can be separated into a classical mean field plus vacuum fluctuations in a linearized quantum-optical network.

---

# 7. Thermal controller fluctuations do add noise

If instead the controller output mode has thermal fluctuation occupation

$$
\boxed{
\langle\delta C^\dagger\delta C\rangle
=\bar n_C,}
$$

then the receiver-incident mode acquires occupation

$$
\boxed{
m_C^{\rm in}
=|t_C|^2\bar n_C.}
$$

After receiver temporal loading with downstream intensity coefficient

$$
\tau_{C\to B}(t),
$$

the controller contribution to the receiver vacuum-output occupation is

$$
\boxed{
m_C^{B}(t)
=\tau_{C\to B}(t)\bar n_C.}
$$

The complete receiver noise budget should then be written schematically as

$$
\boxed{
m_B^{\rm total}(t)
=m_B^{\rm bath}(t)
+m_B^{\rm source}(t)
+m_B^{\rm ctrl}(t)
+\cdots.}
$$

The V6 non-EB condition survives unchanged in form after replacing

$$
m_B
\to
m_B^{\rm total}.
$$

---

# 8. Squeezed/nonclassical controller fluctuations

If the work mode is squeezed or otherwise nonclassical, its fluctuation covariance is anisotropic.

Then the effective downstream noise need not remain phase insensitive.

The channel should be written in the full Gaussian covariance form

$$
V\mapsto KVK^T+Y
$$

rather than compressed into one scalar

$$
m.
$$

This does not invalidate the source architecture, but it removes the convenience of the phase-insensitive scalar EB criterion unless the controller noise is symmetrized or negligibly coupled to the selected receiver mode.

Thus the clean V6 benchmark should continue to use a coherent/vacuum-limited work mode.

---

# 9. Branch-asymmetric controller radiation is a different problem

The analysis above assumes the controller gravitational output is branch common.

If the controller has residual branch-dependent energy redistribution,

$$
\Delta T_{\rm ctrl}^{\mu\nu}\ne0,
$$

then it contributes directly to the branch-difference gravitational field and can

- reinforce the intended source branch mode;
- cancel it;
- radiate into orthogonal branch-record modes.

That is not removable by a common displacement.

It is the separate problem already bounded in

`HUB_CONTROLLER_RESIDUAL_BOUND.md`.

Thus two controller requirements must be distinguished:

### branch-difference requirement

$$
\Delta Q_{\rm ctrl}
$$

must be absent or bounded;

### branch-common fluctuation requirement

controller noise above vacuum must be included in

$$
m.
$$

A large common classical field by itself violates neither requirement.

---

# 10. Relation to the nonlinear \(2\omega\) source radiation

The leading quadratic source quadrupole is branch even:

$$
Q_{ij}^{(2)}
\propto
u^2\,\mathrm{diag}(1,1,-2).
$$

For the mirrored branches

$$
u_+(t)=-u_-(t),
$$

one has

$$
u_+^2=u_-^2.
$$

Therefore the deterministic nonlinear gravitational radiation at dc/\(2\omega\) is also branch common.

At the mean-field level it is exactly analogous to the common controller displacement discussed above and cannot carry the source-qubit branch record.

Its quantum fluctuations and possible leakage into the receiver band remain higher-order corrections already controlled by the small-strain/nonlinear audit.

---

# 11. Practical receiver implication

A very large branch-common controller field could still matter operationally by

- saturating a detector;
- shifting its operating point;
- producing classical technical noise through nonlinearities;
- leaking into the selected measurement band because of imperfect filtering.

Those are real engineering limitations.

They should not be confused with the theoretical entanglement-breaking question in the ideal linear receiver.

The Gedanken benchmark is allowed to subtract or coherently displace a known branch-common field because such a displacement is a local reversible operation independent of the quantum source input.

---

# 12. Adversarial verdict

The existence of branch-common controller radiation does **not** reopen the source which-path loophole.

For an ideal coherent work mode:

$$
\boxed{
\text{controller radiation}
=
\text{common displacement}
+\text{vacuum fluctuations}.}
$$

The common displacement does not alter branch distance, entanglement, or the EB boundary, and the vacuum fluctuations add no positive thermal occupation in the linear phase-insensitive convention.

The source model must nevertheless retain two explicit caveats:

1. branch-asymmetric controller quadrupole residuals are bounded separately;
2. nonvacuum controller fluctuations contribute genuine receiver noise and must be added to the channel noise budget.

This closes the mean-controller-radiation objection without assuming that the work reservoir is gravitationally invisible.
