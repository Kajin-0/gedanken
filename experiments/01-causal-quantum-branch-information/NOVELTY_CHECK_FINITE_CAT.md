# Novelty Check — Exact Finite-Cat Thermal Theorem

**Timestamp:** 2026-08-07 16:58 EDT  
**Status:** Targeted literature check; promising but not sufficient for a novelty claim.

## Result being checked

For the hybrid source-cat family

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle+|1\rangle|-a\rangle}{\sqrt2},
\qquad 0<|a|<\infty,
$$

with the bosonic subsystem sent through a one-mode thermal attenuator of transmissivity $\eta$ and environmental mean occupation $\bar n$, the current theorem proves

$$
\boxed{
\rho_{AB}\text{ is NPT for every finite }a\neq0
\iff
\eta>\frac{\bar n}{\bar n+1}.
}
$$

Equivalently, this particular finite-amplitude hybrid family is NPT **everywhere and only everywhere** the thermal attenuator is not entanglement breaking.

The gravitational application combines this exact family result with a retarded matched receiver to derive an amplitude-independent causal NPT front.

---

## 1. Closest predecessor: Kreis & van Loock (2012)

**Karsten Kreis and Peter van Loock,** “Classifying, quantifying, and witnessing qudit-qumode hybrid entanglement,” *Physical Review A* **85**, 032307 (2012), arXiv:1111.0478.

This is the most important prior-art result found so far because it studies the **same input state and essentially the same thermal channel**.

Their Eq. (24) is

$$
|\psi\rangle_{AB}
=\frac{|0\rangle_A|\alpha\rangle_B+|1\rangle_A|-\alpha\rangle_B}{\sqrt2}.
$$

They transmit subsystem $B$ through a thermal photon-noise channel modeled by a beam splitter coupling it to a thermal environment and tracing the environment out.

They derive the exact output-state expansion and show that the thermal channel produces truly hybrid qubit–qumode states.

However, their entanglement analysis at nonzero temperature uses a Shchukin–Vogel moment determinant. Their sufficient condition is their Eq. (41),

$$
\bar n
<
\frac{4\eta|\alpha|^2}
{(1-\eta)(2e^{4|\alpha|^2}-1)}.
$$

This condition depends strongly on $|\alpha|$ and has an optimal witness amplitude near $|\alpha|\simeq0.44$.

Crucially, their footnote [47] explicitly compares Eq. (41) with the known thermal-channel entanglement-breaking condition

$$
\bar n\ge\frac{\eta}{1-\eta},
$$

and states that their witness may fail to detect entangled states in the region below the EB threshold.

### Relation to the current result

The present theorem appears to close exactly this gap for their state family:

$$
\boxed{
\bar n<\frac{\eta}{1-\eta}
\quad\Longrightarrow\quad
\rho_{AB}\text{ is NPT for every finite }\alpha\neq0.
}
$$

Thus the current result is **not** novel in proposing the state, channel, or hybrid-entanglement problem. Its possible novelty is an exact necessary-and-sufficient NPT theorem for the full finite-amplitude family, replacing a previously sufficient witness.

---

## 2. Sabapathy, Ivan & Simon (2011)

**K. K. Sabapathy, J. Solomon Ivan, and R. Simon,** “Robustness of non-Gaussian entanglement against noisy amplifier and attenuator environments,” *Physical Review Letters* **107**, 130501 (2011), arXiv:1103.1311.

This work analytically studies noisy bosonic attenuator/amplifier channels using Kraus representations and applies PPT tests to non-Gaussian states.

The explicit families treated are two-mode non-Gaussian states such as NOON states and photon-number entangled states. It establishes important robustness results, but the targeted inspection did not reveal the hybrid qubit–coherent family above or an equivalent all-finite-amplitude iff theorem.

This is nevertheless relevant mathematical prior art because it demonstrates analytic non-Gaussian PPT analysis under noisy attenuators.

---

## 3. Kato (2015)

**Kentaro Kato,** “Quasi-Bell entangled coherent states and its quantum discrimination problem in the presence of thermal noise,” arXiv:1508.01597 (2015).

This studies **two-mode** quasi-Bell entangled coherent states under one-sided thermal noise. It derives matrix representations and evaluates a lower bound on entanglement of formation.

The state family differs from the hybrid DV–CV state here: both of Kato's subsystems are bosonic coherent-state modes. The targeted inspection did not identify an iff statement equivalent to the current hybrid theorem.

---

## 4. Other nearby literature

The targeted searches also found:

- coherent-state entanglement under pure amplitude damping;
- continuous-variable quantum benchmarks for entanglement-breaking channels;
- later optical hybrid-entanglement generation and Bell-test proposals;
- general Gaussian-channel entanglement-breaking criteria.

These establish the surrounding ingredients but have not yet yielded the exact theorem under consideration.

---

## 5. Current novelty assessment

### Definitely not new

- the hybrid state $|0\rangle|\alpha\rangle+|1\rangle|-\alpha\rangle$;
- sending only its bosonic subsystem through a thermal beam-splitter channel;
- hybrid entanglement surviving some thermal noise;
- the thermal attenuator entanglement-breaking boundary;
- use of PPT/moment witnesses for these systems.

### Potentially new

The exact family statement

$$
\boxed{
\forall\,0<|\alpha|<\infty:
\qquad
\rho_{AB}\text{ NPT}
\iff
\text{thermal attenuator non-EB}
}
$$

appears not to have been established in the targeted literature search.

The most compelling novelty evidence is that the 2012 paper on the **same state and channel** explicitly stops at a sufficient witness and notes the undetected region below the EB boundary. The present proof claims to characterize that entire region exactly.

### Still required before claiming originality

1. citation-forward search of papers citing Kreis & van Loock (2012), especially work on true hybrid entanglement under thermal noise;
2. search for general theorems implying that every binary coherent-state hybrid probe detects non-EB thermal attenuation;
3. independent mathematical review of the normal-ordered block factorization and domain-safe negative-vector argument;
4. check alternative Gaussian-channel parameter conventions carefully to avoid a hidden equivalence to an existing theorem.

---

## 6. Gravity-specific novelty remains separate

Even if the finite-cat theorem itself exists elsewhere, the project may still contain a distinct gravity result when it is combined with:

1. a retarded gravitational branch-difference mode;
2. source–receiver spin-2 mode overlap $\mathcal O_{SB}$;
3. gravitational receiver rate $\kappa_g$;
4. thermal injection rate $\Gamma_{\rm th}$;
5. waveform-optimal coherent capture.

This produces the exact finite-cat causal front

$$
T_{\rm NPT}^{\min}
=
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\mathcal O_{SB}\kappa_g}
{\mathcal O_{SB}\kappa_g-\Gamma_{\rm th}}
\right],
$$

within the stated receiver model.

The literature search so far has not located this retarded, waveform-optimal entanglement-onset construction.

---

## 7. Current conclusion

The finite-cat theorem should presently be described as

> **a candidate analytic completion of a thermal hybrid-entanglement problem studied explicitly by Kreis & van Loock (2012), with novelty promising but unverified.**

That is a stronger and more defensible position than claiming the underlying state/channel construction as new.
