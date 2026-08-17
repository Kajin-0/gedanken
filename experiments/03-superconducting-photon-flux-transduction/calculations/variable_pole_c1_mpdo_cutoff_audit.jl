#!/usr/bin/env julia
# Frozen cutoff-semantics audit for Experiment-03 C1 MPDO oracle.
# No accepted rank-16 or nonlinear physical state is used.

using LinearAlgebra
using ITensors
using ITensorMPS

srcpath = joinpath(@__DIR__, "variable_pole_c1_mpdo_oracle.jl")
src = read(srcpath, String)
src = replace(src, r"\nmain\(\)\s*$" => "\n")
include_string(Main, src, srcpath * "[definitions-only]")

const TTEST = 1.0e-3
const DT = 1.0e-5
const CUTOFFS = (1.0e-12, 1.0e-14, 1.0e-16, 1.0e-18, 1.0e-20, 0.0)

function initial_expanded(Lmpo, sites, mapping)
  A0 = zeros(ComplexF64, 4, 4, 4)
  A0[1,1,1] = 1.0
  psi0 = MPS(A0, sites; cutoff=0.0, maxdim=64)
  v0 = site_to_column(mps_to_site_vector(psi0, sites), mapping)
  psi0x = expand(
    psi0, Lmpo;
    alg="global_krylov", krylovdim=4, cutoff=1e-18,
    apply_kwargs=(; maxdim=64, cutoff=1e-18),
  )
  vx = site_to_column(mps_to_site_vector(psi0x, sites), mapping)
  rel = norm(vx-v0)/norm(v0)
  rel < 1e-13 || error("expanded initial state changed")
  println("C1_CUTOFF_INIT rel=$(rel) bond=$(maxlinkdim(psi0x))")
  return psi0x, v0
end

function dense_schmidt(vsite)
  A = reshape(vsite, 4, 16)
  Bm = reshape(vsite, 16, 4)
  return svdvals(A), svdvals(Bm)
end

function main()
  Hb, Lc, Gamma, g, dims, H, cs = build_dense_model()
  Ldense = dense_liouvillian(H, cs)
  sites, Lmpo = build_mpo(Hb, Gamma, g)
  mapping = site_to_column_mapping(dims)
  D = prod(dims)

  Lsite = mpo_to_site_dense(Lmpo, sites)
  Lfrommpo = zeros(ComplexF64, size(Ldense))
  for a in eachindex(mapping), b in eachindex(mapping)
    Lfrommpo[mapping[a], mapping[b]] = Lsite[a,b]
  end
  mpo_rel = norm(Lfrommpo-Ldense)/norm(Ldense)
  mpo_rel < 1e-12 || error("MPO/dense mismatch")

  psi0x, v0 = initial_expanded(Lmpo, sites, mapping)
  vex = exp(Ldense*TTEST)*v0
  vsite_exact = similar(vex)
  for j in eachindex(mapping)
    vsite_exact[j] = vex[mapping[j]]
  end
  s1, s2 = dense_schmidt(vsite_exact)
  println("C1_CUTOFF_SCHMIDT cut=1 values=" * join(["$(x)" for x in s1], ","))
  println("C1_CUTOFF_SCHMIDT cut=2 values=" * join(["$(x)" for x in s2], ","))
  println("C1_CUTOFF_SCHMIDT4 cut=1 s4=$(s1[4]) s4sq=$(s1[4]^2) cut=2 s4=$(s2[4]) s4sq=$(s2[4]^2)")

  anypass = false
  firstpass = nothing
  for cutoff in CUTOFFS
    psi = tdvp(
      Lmpo, TTEST, psi0x;
      time_step=DT,
      nsite=2,
      reverse_step=true,
      order=2,
      maxdim=64,
      cutoff=cutoff,
      normalize=false,
      updater_backend="exponentiate",
      updater_kwargs=(; tol=1e-13, krylovdim=30),
      outputlevel=0,
    )
    vtn = site_to_column(mps_to_site_vector(psi, siteinds(psi)), mapping)
    rtn = reshape(vtn,D,D)
    rex = reshape(vex,D,D)
    htd = half_trace_distance(rtn,rex)
    terr = abs(tr(rtn)-1)
    anti = norm(rtn-adjoint(rtn))
    vrel = norm(vtn-vex)/norm(vex)
    bond = maxlinkdim(psi)
    ok = htd < 1e-9 && terr < 1e-10 && anti < 1e-10
    anypass |= ok
    if ok && isnothing(firstpass)
      firstpass = cutoff
    end
    println("C1_CUTOFF_POINT cutoff=$(cutoff) half_trace=$(htd) trace_err=$(terr) antiherm=$(anti) vec_rel=$(vrel) bond=$(bond) oracle_ok=$(ok ? 1 : 0)")
  end

  println("C1_CUTOFF_SUMMARY mpo_dense_rel=$(mpo_rel) any_oracle_pass=$(anypass ? 1 : 0) first_pass_cutoff=$(firstpass)")
  anypass || error("no cutoff in frozen audit recovered the MPDO oracle")
  println("VARIABLE_POLE_C1_MPDO_CUTOFF_AUDIT_PASS")
end

main()
