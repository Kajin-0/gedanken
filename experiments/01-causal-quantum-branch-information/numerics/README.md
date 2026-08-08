# Numerical Audits

These scripts are **independent checks**, not components of the analytic proofs.

Their purpose is to realize the relevant Gaussian channels by constructions that do not use the coherent-state matrix-element formula in `../DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`, assemble the qubit–bosonic output state in a truncated Fock basis, partially transpose the qubit, and inspect the minimum PT eigenvalue / negativity.

## Requirements

- Python 3.10+
- NumPy
- SciPy

Example environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install numpy scipy
```

No result in this directory should be treated as proof of an infinite-dimensional statement. Near an entanglement-breaking boundary, finite Fock truncation and finite quadrature order can create small spurious negative PT eigenvalues. Convergence is part of the test.

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

and the exact EB boundary is

$$
\eta\le\frac{\bar n}{\bar n+1}.
$$

Run:

```bash
python thermal_cat_scan.py
```

This is the oldest script in the audit suite and performs a grid scan in coherent branch separation around the thermal-loss EB threshold.

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

Repository channel parameters:

$$
\tau=G,
$$

$$
m=(G-1)(n_E+1).
$$

The exact EB threshold is

$$
\boxed{n_E\ge\frac1{G-1}.}
$$

Default regression run:

```bash
python amplifier_cat_scan.py
```

This evaluates

- `G = 1.5, n_E = 0.5, a = 0.4` — safely non-EB;
- `G = 1.5, n_E = 3.0, a = 0.4` — EB control;

for Fock cutoffs 10, 12, 14, 16, 18.

Expected non-EB minimum PT eigenvalues converge approximately as

```text
N=10  -5.85654e-2
N=12  -5.85734e-2
N=14  -5.85749e-2
N=16  -5.85752e-2
N=18  -5.85752e-2
```

On the EB control, the finite-cutoff PT minimum is spuriously negative but its magnitude decreases with cutoff, e.g.

```text
N=10  -6.22e-3
N=12  -3.79e-3
N=14  -2.53e-3
N=16  -1.68e-3
N=18  -1.11e-3
```

The trend toward zero is the expected truncation behavior. A persistent finite negative value on the EB side would be a red flag.

Custom run:

```bash
python amplifier_cat_scan.py --gain 1.2 --n-env 2.0 --amplitude 0.3 --cutoffs 10 12 14
```

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

implemented directly using tensor-product Gauss–Hermite quadrature over the displacement plane.

Here

$$
\tau=1,
$$

and the exact EB boundary is

$$
\boxed{m\ge1.}
$$

Default regression run:

```bash
python additive_noise_cat_scan.py
```

uses coherent branches `|±0.35>` at Fock cutoff 16 and scans

```text
m = 0.70, 0.95, 1.05, 1.30
```

across quadrature orders 12, 16, and 20.

Representative converged values at sufficiently high quadrature order are

```text
m=0.70   lambda_min(PT) ≈ -2.228e-2   non-EB
m=0.95   lambda_min(PT) ≈ -2.581e-3   non-EB
m=1.05   lambda_min(PT) ≈ few × 10^-6 negative numerical floor   EB
m=1.30   lambda_min(PT) ≈ few × 10^-6 negative numerical floor   EB
```

The EB-side residual must be interpreted as quadrature/Fock error and tested for convergence rather than as physical NPT.

Custom run:

```bash
python additive_noise_cat_scan.py --noise 0.999 --amplitude 0.35 --dim 18 --orders 16 20 24
```

---

## 4. What constitutes a successful audit

A numerical case is useful only if all of the following are checked:

1. the output trace is close to one;
2. the non-EB negative PT eigenvalue is stable as numerical resolution increases;
3. EB-side residual negative eigenvalues shrink toward zero with increasing resolution;
4. channel parameters are independently mapped to the repository's $(\tau,m)$ convention;
5. the implementation does not call the analytic coherent-dyad formula being tested.

Near

$$
|\tau-m|\ll1,
$$

absolute PT eigenvalues can be extremely small, so the convergence requirements become correspondingly stricter.

---

## 5. Current coverage

The three main phase-insensitive realizations now have committed executable audits:

| Channel | Independent realization | Script |
|---|---|---|
| thermal attenuator | beam splitter + thermal environment | `thermal_cat_scan.py` |
| thermal amplifier | two-mode squeezer + thermal environment | `amplifier_cat_scan.py` |
| additive noise | Gaussian random displacements | `additive_noise_cat_scan.py` |

This substantially improves reproducibility relative to the earlier repository state, where amplifier and additive-noise results were documented only as numerical tables.

---

## 6. Next numerical target

The next useful addition is a controlled near-boundary stress suite rather than a large brute-force scan.

Recommended cases:

- thermal attenuator with relative boundary offsets $|\tau-m|/\max(\tau,m)$ from $10^{-1}$ down to $10^{-4}$;
- amplifier with $n_E=(1\pm\epsilon)/(G-1)$;
- additive noise with $m=1\pm\epsilon$;
- several coherent separations from weak overlap breaking to nearly orthogonal branches;
- at least one strongly unequal branch-weight case.

For each case, store convergence versus numerical resolution, not just one PT eigenvalue.
