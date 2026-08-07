# Novelty Check — Causal Quantum-Front Speed Limit

**Timestamp:** 2026-08-07 16:27 EDT  
**Status:** Preliminary literature boundary, not a novelty claim

## Candidate result being checked

Within the stationary Markov single-mode receiver model, any normalized incoming branch-difference waveform obeys

$$
\eta_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau}).
$$

Therefore weak-cat source-receiver NPT cannot occur earlier than

$$
\boxed{
T_{\rm NPT}
\ge
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right],
}
$$

with

$$
\Gamma_{\rm th}=\sum_a\bar n_a\kappa_a,
$$

provided $\kappa_\Delta>\Gamma_{\rm th}$. The time-reversed matched waveform saturates the ideal bound.

Equivalently,

$$
\epsilon_Q
=1-\Gamma_{\rm th}/\kappa_\Delta,
$$

$$
T_{\rm NPT}^{\min}-R/c
=-\kappa_{\rm tot}^{-1}\ln\epsilon_Q.
$$

## Closest literature found so far

### Entanglement-breaking time / quantum speed limits

Sakuldee and Rudnicki, arXiv:2209.08689, study **bounds on the breaking time for entanglement-breaking channels** under Lindblad dynamics. Their direction is the loss of pre-existing entanglement: how quickly a dynamical map becomes entanglement breaking.

This is mathematically neighboring but operationally opposite to the present problem, which asks how soon a causal receiver can first **acquire** source entanglement after a retarded signal arrives.

### Gravity-induced quantum channel threshold

Mari, Zippilli, and Vitali, Phys. Rev. D 113, L021905 (2026), model a gravity-induced optical link as a Gaussian thermal attenuator and use the transition from entanglement-breaking to non-entanglement-breaking behavior as a test of gravitational nonclassicality.

This is directly relevant prior art for the static channel threshold. Their published abstract emphasizes the thermal EB transition and asymptotic quantum communication, not a retarded light-cone onset optimized over finite wavepacket capture.

## Preliminary distinction

The potentially distinctive structure in Experiment 01 is the conjunction

$$
\boxed{
\text{retarded causal arrival }R/c
+\text{finite receiver build-up}
+\text{thermal EB boundary}
+\text{waveform-optimal onset bound}.
}
$$

The Cauchy-Schwarz part of the derivation is elementary and is not novel mathematics. Any novelty would lie in recognizing and applying it as a **causal gravitational entanglement-front speed limit**.

## Current novelty status

**Promising but unverified.** Targeted searches did not reveal the exact result, but this is not sufficient to claim novelty.

Before a paper claim, search should be extended to:

- quantum state-transfer latency in cavity/input-output systems;
- entanglement generation times in thermal bosonic channels;
- relativistic detector communication onset;
- quantum network state-transfer speed limits;
- gravity-mediated channel latency / retardation papers.
