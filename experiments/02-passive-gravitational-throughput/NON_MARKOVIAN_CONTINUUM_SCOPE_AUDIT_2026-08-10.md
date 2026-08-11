# Non-Markovian Continuum Scope Audit — 2026-08-10

## Trigger

A reviewer-style critique asked whether excluding genuinely non-Markovian continua materially narrows the applicability of the passive gravitational spectral-area theorem to real macroscopic crystalline structures.

## Disposition

**The concern is partly valid, but the original wording was too broad.**

The current bounded-port Markov proof is not a theorem for arbitrary hereditary constitutive laws, singular continuum baths, or unbounded boundary-control/observation systems without a separate admissibility analysis. However, it is incorrect to infer that a finite crystal or every response with a memory kernel is therefore outside the theorem's logic.

## 1. Finite crystalline bodies are not automatically frequency continua

At the atomistic harmonic level, a finite crystal has finitely many mechanical degrees of freedom. At the continuum-elastic level, a bounded ideal elastic body with standard free or clamped boundary conditions has a discrete normal-mode spectrum. A useful primary mathematical reference is:

- M. Capoferri, L. Friedlander, M. Levitin, and D. Vassiliev, *Two-Term Spectral Asymptotics in Linear Elasticity*, Journal of Geometric Analysis **33**, 242 (2023), DOI `10.1007/s12220-023-01269-y`.

The only fact used here is the standard discreteness of the bounded linear-elastic eigenvalue problem; no claim depends on the disputed details of higher-order spectral asymptotics.

Therefore a macroscopic finite crystalline endpoint is not excluded merely because one uses continuum elasticity.

## 2. Non-Markovian reduced dynamics can arise from eliminating passive degrees of freedom

An exact generalized-Langevin equation can be obtained by projecting out a harmonic environment. The reduced observable then obeys a memory-kernel equation even though the full enlarged system is local in time and Hamiltonian/passive. A direct solid/open-system example is:

- L. Stella, C. D. Lorenz, and L. Kantorovich, *Generalized Langevin equation: An efficient approach to nonequilibrium molecular dynamics of open systems*, Physical Review B **89**, 134303 (2014), DOI `10.1103/PhysRevB.89.134303`.

Thus the statement

```text
non-Markovian reduced response => outside the theorem
```

is too strong.

The correct statement is conditional:

```text
If the eliminated passive degrees of freedom can be restored to an enlarged
well-posed passive state realization, and the gravitational observation on
that enlarged space satisfies the required admissibility / finite-trace
condition, then the passive Gramian cut can be applied on the enlarged state.
```

Memory in a chosen reduced coordinate is therefore not, by itself, a loophole.

## 3. Unbounded PDE operators are a proof obligation, not a physical-class veto

Infinite-dimensional passive-system theory contains well-posed scattering-passive realizations with unbounded internal and boundary operators. A primary reference particularly close to the present energy-balance structure is:

- O. J. Staffans and G. Weiss, *A Physically Motivated Class of Scattering Passive Linear Systems*, SIAM Journal on Control and Optimization **50**, 3083--3112 (2012), DOI `10.1137/110846403`.

That paper treats beam and Maxwell-type examples and proves scattering-passive energy balances in an operator/system-node framework.

Therefore the previous wording

```text
arbitrary unbounded PDE ports are excluded
```

remains correct as a statement about what has been proved here, but should not be read as saying that unbounded distributed systems cannot satisfy an analogous passive cut.

## 4. What still is not proved

The present theorem has not established all of the following for an arbitrary continuum bath or hereditary medium:

1. existence of a passive well-posed realization/dilation on an enlarged Hilbert space;
2. admissibility of the selected control and observation maps when they are unbounded;
3. Hilbert--Schmidt / finite-trace regularity of the gravitational observation after enlargement;
4. preservation of the sector-resolved retained-frequency resource under that realization;
5. an all-frequency replacement for the retained-modal ceiling.

Items 3--5 are the gravity-specific obstacles. Generic passive-system realizability alone does not close them.

## 5. Consequence for real macroscopic crystalline structures

For a finite macroscopic crystal operated in a narrow mechanical band, the theorem is not invalidated merely because microscopic damping ultimately arises from phonons, defects, anharmonicity, or other eliminated degrees of freedom. A standard finite-mode or bounded-domain elastic description can still be a legitimate retained model if its passive reduction is justified.

What remains application-specific is whether that reduction gives a quantitatively controlled representation of the actual device over the measured band. Strong frequency-dependent internal friction, dense bath structure, branch cuts, long-memory kernels, or singular boundary couplings can invalidate a simple finite Markov approximation even while preserving overall passivity. In that case the current proof does not automatically deliver the inertia-controlled coefficient.

## 6. Manuscript decision

The submission text should be changed from a blanket exclusion of "genuinely non-Markov continua" to the narrower and more defensible statement:

> Non-Markovianity of a reduced coordinate is not itself an escape from the bound. The present proof applies directly to the stated bounded-port realization and conditionally to enlarged passive realizations that satisfy the required admissibility and finite gravitational-trace properties. It does not establish a universal result for arbitrary hereditary or continuum reduced models for which no such realization and trace control have been proved.

No theorem coefficient changes. No active-system scope is added. The high-frequency retained-sector limitation remains independent and unresolved.