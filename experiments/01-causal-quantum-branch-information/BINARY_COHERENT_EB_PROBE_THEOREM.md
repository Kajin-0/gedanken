# Binary Coherent Hybrid Probe Theorem for Thermal Attenuators

**Timestamp:** 2026-08-07 17:04 EDT  
**Status:** Analytic generalization of the exact finite-cat theorem; novelty unverified.

## 1. Statement

Consider the general pure hybrid qubit–bosonic state

$$
\boxed{
|\Psi\rangle
=
\sqrt p\,|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}\,|1\rangle|\beta\rangle,
}
$$

with

$$
0<p<1,
\qquad
\alpha\neq\beta,
\qquad
|\alpha|,|\beta|<\infty.
$$

Send only the bosonic subsystem through a one-mode phase-insensitive thermal attenuator with coherent transmissivity $\eta$ and environment occupation $\bar n$. Define

$$
\boxed{m=(1-\eta)\bar n.}
$$

Then

> **Binary coherent hybrid probe theorem.** Every nontrivial state above gives an NPT qubit–receiver output if and only if the thermal attenuator is not entanglement breaking:
>
> $$
> \boxed{
> (I\otimes\mathcal E_{\eta,\bar n})(|\Psi\rangle\langle\Psi|)
> \text{ is NPT}
> \iff
> \eta>m
> \iff
> \eta>\frac{\bar n}{\bar n+1}.
> }
> $$

Thus the threshold is independent of:

- the coherent-state separation magnitude, provided it is finite and nonzero;
- the coherent-state midpoint in phase space;
- the orientation of the coherent-state separation in phase space;
- the nonzero branch probability $p$;
- the relative source phase $\phi$.

These parameters control the **amount** of entanglement, not the sign boundary.

---

## 2. Reduction to the symmetric theorem

Define

$$
\gamma=\frac{\alpha+\beta}{2},
\qquad
\delta=\alpha-\beta.
$$

Then

$$
|\alpha\rangle
=D(\gamma)|\delta/2\rangle
$$

and

$$
|\beta\rangle
=D(\gamma)|-\delta/2\rangle
$$

up to branch-dependent phases that can be absorbed into a local qubit phase rotation.

The thermal attenuator is displacement covariant,

$$
\mathcal E_{\eta,\bar n}
[D(\gamma)\rho D^\dagger(\gamma)]
=
D(\sqrt\eta\gamma)
\mathcal E_{\eta,\bar n}(\rho)
D^\dagger(\sqrt\eta\gamma).
$$

The output displacement is a local unitary and cannot change entanglement.

The channel is also phase covariant, so a local phase-space rotation can map

$$
\delta/2
\rightarrow
|\delta|/2\equiv a>0.
$$

Therefore every binary coherent pair reduces locally to the symmetric pair

$$
|\pm a\rangle,
\qquad
a=|\alpha-\beta|/2.
$$

---

## 3. Unequal branch weights do not move the threshold

After the local reductions, the source-receiver output has block form

$$
\rho_{AB}
=
\begin{pmatrix}
 p\rho_+ & e^{-i\phi}\sqrt{p(1-p)}X\\
 e^{i\phi}\sqrt{p(1-p)}X^\dagger & (1-p)\rho_-
\end{pmatrix}.
$$

For the symmetric finite-cat proof,

$$
\rho_+=L_+L_+^\dagger,
\qquad
\rho_-=L_-L_-^\dagger,
\qquad
X=tL_+L_-^\dagger.
$$

Now define

$$
\widetilde L_+=\sqrt p\,L_+,
\qquad
\widetilde L_-=\sqrt{1-p}\,L_-.
$$

Then

$$
p\rho_+=\widetilde L_+\widetilde L_+^\dagger,
$$

$$
(1-p)\rho_-=\widetilde L_-\widetilde L_-^\dagger,
$$

and

$$
\sqrt{p(1-p)}X
=t\widetilde L_+\widetilde L_-^\dagger.
$$

Thus the factors of $p$ and $1-p$ cancel from the normalized off-diagonal operator in the partial-transpose congruence. The relative phase $\phi$ is removed by a local source phase rotation.

The same parameter

$$
q
=\exp\left[
\frac{2a^2}{m}(\eta-m)
\right]
$$

therefore controls the sign.

Since

$$
a=|\alpha-\beta|/2,
$$

the general expression is

$$
\boxed{
q
=\exp\left[
\frac{|\alpha-\beta|^2}{2m}(\eta-m)
\right].
}
$$

For every finite distinct pair $\alpha\neq\beta$,

$$
q>1
\iff
\eta>m.
$$

The explicit normalizable negative-vector construction from `EXACT_FINITE_CAT_THERMAL_THEOREM.md` then gives the NPT direction. The converse follows because $\eta\le m$ is exactly the entanglement-breaking region of the thermal attenuator.

---

## 4. Degenerate limits

The exclusions in the theorem are necessary.

### $p=0$ or $p=1$

Only one source branch is populated, so the input is a product state.

### $\alpha=\beta$

The bosonic state is independent of the source branch, so the input factorizes as

$$
(\sqrt p|0\rangle+e^{i\phi}\sqrt{1-p}|1\rangle)|\alpha\rangle.
$$

### Vacuum environment $m=0$

The channel is pure loss. Every $\eta>0$ is non-EB and every nontrivial binary hybrid coherent state retains some NPT entanglement after the channel; $\eta=0$ is the EB endpoint.

---

## 5. Interpretation

Within the thermal attenuator family, **binary coherent hybrid states are complete EB probes**:

$$
\boxed{
\text{any nontrivial finite binary coherent hybrid input}
\quad\text{detects}\quad
\text{non-entanglement-breaking attenuation}.
}
$$

This is much stronger than saying that there exists some optimized entangled input that survives whenever the channel is non-EB.

For this channel family, one does not have to tune the coherent separation or branch probability to cross the fundamental sign boundary. Any nonzero finite coherent separation and any nonzero pair of branch weights work in principle. Optimization is needed only to maximize the measurable amount of entanglement.

---

## 6. Relevance to Experiment 01

The gravitational source need not produce perfectly opposite coherent difference-mode amplitudes or exactly equal branch weights for the channel-capability result to hold.

If two source histories produce any distinct finite coherent amplitudes

$$
\beta_L\neq\beta_R
$$

in the selected gravitational branch mode, then, within the thermal receiver model, the receiver is NPT-entangled with the source exactly when its effective thermal attenuator is non-EB.

Therefore the causal-front sign condition is robust to moderate source imbalance:

$$
\boxed{
\eta_f(t)>m(t)
}
$$

remains the exact boundary.

The gravitational waveform geometry controls

- branch-mode separation;
- entanglement magnitude;
- source–receiver mode overlap;
- detectability;

but not the fundamental thermal sign boundary once the two branch-conditioned coherent outputs are distinct.

---

## 7. Independent numerical audit

A separate truncated beam-splitter dilation was evaluated for:

- unequal source weights $p$;
- nonsymmetric complex coherent amplitudes $\alpha,\beta$;
- several thermal occupations and transmissivities above/below the EB boundary.

Above the predicted boundary, NPT negativity was found for all tested nontrivial inputs. Below the boundary, exact separability follows from the EB property; tiny apparent negative values at insufficient Fock cutoffs are numerical truncation artifacts.

---

## 8. Novelty status

The closest known predecessor, Kreis & van Loock (2012), treats the balanced symmetric special case and a thermal beam-splitter channel, but uses a sufficient moment witness rather than proving the exact iff boundary.

The targeted searches performed so far have not located the stronger statement that **every** nontrivial binary coherent hybrid probe, including arbitrary coherent-state pair and branch weights, is NPT iff the thermal attenuator is non-EB.

This is still **novelty unverified**. A general channel-theory result may imply it indirectly.

---

## 9. Strongest next question

Does an existing structural theorem for phase-insensitive Gaussian channels imply this binary-probe completeness result? If not, the generalized theorem may be a cleaner standalone quantum-information result than the symmetric cat special case, with the gravitational causal-front theorem as its physical application.
