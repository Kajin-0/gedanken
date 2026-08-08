# Numerical Audits

These scripts are **independent checks**, not components of the analytic proofs.

Their purpose is to realize relevant Gaussian channels and gravitational normalization tests through constructions that do not simply call the analytic formula being audited, then test convergence or closed-form constants numerically.

## Pinned active environment

The active CI environment is

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

Install with

```bash
python -m pip install -r requirements.txt
```

No finite-dimensional numerical result in this directory should be treated as proof of an infinite-dimensional statement. Near an entanglement-breaking boundary, finite Fock truncation and finite quadrature order can create small spurious negative PT eigenvalues. Convergence is part of the test.

---

## 1. Thermal attenuator

Script:

```text
thermal_cat_scan.py
```

Construction:

- signal coherent dyads;
- thermal environment;
- beam-splitter unitary;
- explicit environment trace.

For transmissivity `eta` and environment occupation `nbar`,

$$
\tau=\eta,
\qquad
m=(1-\eta)\bar n,
$$

with exact EB boundary

$$
\eta\le\frac{\bar n}{\bar n+1}.
$$

Exploratory run:

```bash
python thermal_cat_scan.py
```

---

## 2. Thermal amplifier

Script:

```text
amplifier_cat_scan.py
```

Construction:

$$
a_{\rm out}
=\sqrt G\,a_{\rm in}
+\sqrt{G-1}\,e^\dagger
$$

implemented by an explicit finite-matrix two-mode squeezer with a thermal environment.

Repository convention:

$$
\tau=G,
$$

$$
m=(G-1)(n_E+1),
$$

with exact EB threshold

$$
\boxed{n_E\ge\frac1{G-1}.}
$$

Canonical non-EB regression case:

```text
G=1.5, n_E=0.5, a=0.4
```

with minimum PT eigenvalue near

```text
-5.8575e-2
```

as the Fock cutoff is increased.

The EB control uses

```text
G=1.5, n_E=3.0, a=0.4
```

and verifies that the finite-cutoff negative PT floor shrinks with increasing cutoff.

---

## 3. Unit-gain additive Gaussian noise

Script:

```text
additive_noise_cat_scan.py
```

Construction:

$$
\Phi_m(\rho)
=\int\frac{d^2z}{\pi m}
\exp(-|z|^2/m)
D(z)\rho D^\dagger(z),
$$

implemented directly using tensor-product Gauss--Hermite quadrature.

Here

$$
\tau=1,
$$

and the exact EB boundary is

$$
\boxed{m\ge1.}
$$

The committed scans cross the boundary from both sides and explicitly track the quadrature/Fock numerical floor.

---

## 4. Near-boundary stress harness

Script:

```text
near_boundary_stress.py
```

This approaches

$$
\delta=\tau-m=0
$$

from both sides using the independent additive-noise and thermal-amplifier implementations.

Its purpose is not to prove the analytic boundary numerically. It tests how long the finite numerical realization continues to resolve the predicted sign before truncation/quadrature error dominates.

---

## 5. Canonical TT one-graviton normalization

Script:

```text
tt_mode_overlap_25_16_check.py
```

This independently checks the publication-critical TT angular-mode overlap used in V7.

It verifies

1. direct TT angular quadrature against the analytic expression;
2. outgoing + time-reversed decomposition;
3. normalization $S(0)\to1$;
4. wave-zone convergence to amplitude coefficient $5/4$.

The associated workflow is

```text
.github/workflows/tt-normalization.yml
```

and passes under the pinned environment above.

---

## 6. Fast scientific regression suite

CI harness:

```text
scientific_regression_checks.py
```

Workflow:

```text
.github/workflows/scientific-regressions.yml
```

This is the fast repository-level regression suite. It checks:

### Independent channel realizations

- thermal attenuator: safely non-EB case plus strong EB control;
- thermal amplifier: documented non-EB PT eigenvalue plus shrinking EB truncation floor;
- additive noise: non-EB / EB controls;
- additive-noise near-boundary sign resolution.

### V7 closed-form scientific constants

- finite-spoke series for
  $$
  \mathcal A(q),\quad\mathcal C_Q(q),\quad\mathcal C_\kappa(q);
  $$
- the aggressive V7 benchmark values
  $$
  \kappa_g,
  \quad
  \beta_g,
  \quad
  \eta_{\rm store},
  \quad
  \eta_Q^{\rm link},
  \quad
  4e^{-2}\eta_Q^{\rm link};
  $$
- the exact binary-coherent pure-loss negativity weak-link asymptotic.

First workflow run:

```text
31266390454
```

passed all checks under the pinned environment.

---

## 7. What constitutes a successful finite-Fock audit

A numerical channel case is useful only if all of the following are checked:

1. output trace is close to one;
2. non-EB negative PT eigenvalue is stable as numerical resolution increases;
3. EB-side residual negative eigenvalues shrink toward zero with increasing resolution;
4. channel parameters are independently mapped to the repository's $(\tau,m)$ convention;
5. implementation does not call the analytic coherent-dyad formula being tested.

Near

$$
|\tau-m|\ll1,
$$

absolute PT eigenvalues can be extremely small, so convergence requirements become correspondingly stricter.

---

## 8. Coverage status

| Scientific item | Independent executable check | CI regression |
|---|---|---|
| thermal attenuation | `thermal_cat_scan.py` | yes, representative case |
| thermal amplification | `amplifier_cat_scan.py` | yes |
| additive Gaussian noise | `additive_noise_cat_scan.py` | yes |
| near-EB boundary | `near_boundary_stress.py` / additive boundary checks | yes, representative case |
| TT $25/16$ normalization | `tt_mode_overlap_25_16_check.py` | yes, dedicated workflow |
| finite-spoke coefficients | closed-form regression | yes |
| V7 benchmark constants | closed-form regression | yes |
| exact-negativity asymptotic | closed-form regression | yes |

The exploratory scans remain available for deeper convergence studies; CI intentionally uses a smaller deterministic subset to keep runtime bounded.
