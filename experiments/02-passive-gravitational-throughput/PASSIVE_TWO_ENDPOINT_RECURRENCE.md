# Passive Two-Endpoint Recurrence Bound

**Stage:** F  
**Status:** analytic derivation; dedicated matrix adversary pending.  
**Scope:** repeated passive gravitational returns between the same two separated compact endpoints. Added relays/cavities and near-field coupling are not included.

## 1. Question

Stages A–E treat the separated gravitational propagation as a one-hop operator. A possible loophole is repeated reflection:

```text
A -> B -> A -> B -> ...
```

Could a passive source and receiver use those returns as an effective gravitational cavity and increase the leading `1/R^2` throughput coefficient?

## 2. Exact two-endpoint scattering resolvent

At one envelope frequency, let

- `P_+ = P_BA` map outgoing gravitational waves at A to incoming waves at B;
- `P_- = P_AB` map outgoing waves at B back to incoming waves at A;
- `R_A` and `R_B` be the gravitational reflection blocks of the full passive endpoint scattering operators.

Let `s_A` be the gravitational wave launched from the source side before recurrence. If `b` is the total incoming gravitational wave at B, then

```math
b
=P_+s_A+P_+R_AP_-R_Bb.
```

Hence

```math
\boxed{
P_{\rm eff}
=(I-L)^{-1}P_+,
\qquad
L=P_+R_AP_-R_B.
}
```

This is the exact geometric multiple-scattering resolvent whenever `I-L` is invertible. The network-composition idea is historical scattering theory; Redheffer's 1962 scattering/transfer formalism is a primary antecedent.

## 3. Passivity bounds the loop gain

Because `R_A` and `R_B` are subblocks of passive endpoint scattering matrices with all loss ports retained,

```math
\|R_A\|_{\rm op}\le1,
\qquad
\|R_B\|_{\rm op}\le1.
```

Define

```math
p_+=\|P_+\|_{\rm op},
\qquad
p_-=\|P_-\|_{\rm op}.
```

Then

```math
\boxed{
\|L\|_{\rm op}
\le p_+p_-.
}
```

If `p_+p_-<1`, the Neumann series converges and

```math
\|(I-L)^{-1}\|_{\rm op}
\le\frac1{1-p_+p_-}.
```

Therefore

```math
\boxed{
\|P_{\rm eff}\|_{\rm op}
\le
\frac{p_+}{1-p_+p_-}.
}
```

No phase choice or passive endpoint reflection can exceed this ceiling.

## 4. Reciprocal separated propagation

For reciprocal free propagation the forward and reverse one-hop norm ceilings are equal:

```math
p_+=p_-=p.
```

Define the one-hop power ceiling

```math
\eta=p^2.
```

Then

```math
\boxed{
\|P_{\rm eff}\|_{\rm op}^2
\le
\frac{\eta}{(1-\eta)^2}.
}
```

This is an **upper bound** on recurrent transfer. It is not an equality for a generic physical link. Phases can make the actual recurrent transfer smaller.

The scalar perfectly phase-aligned passive-reflection case saturates the norm inequality and is therefore the appropriate worst-case adversary.

## 5. Leading wave-zone coefficient is unchanged

Stage C gives

```math
p=O((kR)^{-1}),
```

with

```math
\limsup_{kR\to\infty}(kR)^2p^2\le\frac{25}{16}.
```

Hence

```math
p_+p_-=O((kR)^{-2}),
```

so

```math
\frac1{(1-p_+p_-)^2}\to1.
```

It follows directly that

```math
\boxed{
\limsup_{kR\to\infty}
(kR)^2\|P_{\rm eff}\|_{\rm op}^2
\le\frac{25}{16}.
}
```

Thus arbitrary passive returns between the **same two compact separated endpoints** do not change the retained leading `1/R^2` power coefficient.

If one temporarily writes the reciprocal one-hop upper ceiling as `eta`, the recurrent upper ceiling expands as

```math
\frac{\eta}{(1-\eta)^2}
=\eta+2\eta^2+O(\eta^3).
```

Since `eta=O((kR)^-2)`, the **upper-ceiling correction** begins at `O((kR)^-4)` in power.

The correct statement is therefore

```math
\eta_{\rm eff}^{\rm ceiling}
\le
\eta+O((kR)^{-4}),
```

not

```math
\eta_{\rm actual}=\eta+O((kR)^{-4}).
```

The latter would incorrectly exclude destructive recurrent interference.

## 6. Consequence for the inertia theorem

The Stage-A cut can use the recurrent propagation norm in place of the one-hop norm. Since the recurrent norm has the same leading wave-zone coefficient,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
}
```

retains the same leading coefficient when arbitrary passive A↔B returns between those endpoints are included.

This does not claim that recurrence is numerically irrelevant at moderate `kR`; it claims it cannot create a new leading `1/R^2` resource coefficient in the separated asymptotic regime.

## 7. What this does not cover

Not included:

- an added third gravitational relay;
- engineered external mirrors or an extended cavity surrounding both endpoints;
- active phase-sensitive feedback or gain;
- overlapping/nonseparable source and receiver regions;
- reactive near-field exchange where `p` is not `O(1/kR)`;
- curved-background focusing or external gravitational lenses.

These change the propagation architecture rather than merely resumming returns between the same two compact endpoints.

## 8. Prior-art boundary

Multiple-scattering/network composition is established mathematics. A primary historical anchor is:

R. Redheffer, *On the Relation of Transmission-Line Theory to Scattering and Transfer*, Journal of Mathematics and Physics **41**, 1–41 (1962), DOI `10.1002/sapm19624111`.

Experiment 02 does not claim a new star-product or multiple-scattering formalism. The purpose here is only to show that this established recurrence machinery cannot alter the retained leading compact gravitational coefficient under the declared separation/passivity assumptions.

## 9. Required adversarial regression

`numerics/verify_passive_two_endpoint_recurrence.py` should:

1. generate random complex contraction reflections `R_A,R_B`;
2. generate random forward/reverse propagation matrices with prescribed norms `p_+,p_-`;
3. evaluate the exact resolvent `(I-P_+R_AP_-R_B)^-1 P_+`;
4. check `||P_eff|| <= p_+/(1-p_+p_-)`;
5. include the scalar aligned case that exactly saturates the ceiling;
6. verify that `(kR)^2||P_eff||^2` approaches the same `25/16` leading ceiling as separation grows.
