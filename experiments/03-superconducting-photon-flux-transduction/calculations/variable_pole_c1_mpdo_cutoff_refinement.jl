#!/usr/bin/env julia
# Frozen nonzero-cutoff refinement for Experiment-03 C1 MPDO oracle.
# No accepted rank-16 physical state and no nonlinear C1 state are used.

using LinearAlgebra
using ITensors
using ITensorMPS

srcpath = joinpath(@__DIR__, "variable_pole_c1_mpdo_oracle.jl")
src = read(srcpath, String)
src = replace(src, r"\nmain\(\)\s*$" => "\n")
include_string(Main, src, srcpath * "[definitions-only]")

const TTEST = 1.0e-3
const DT = 1.0e-5
const CUTOFFS = (1e-20,1e-21,1e-22,1e-23,1e-24,1e-25,1e-26,1e-27,1e-28,1e-29,1e-30,0.0)

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

  A0 = zeros(ComplexF64, 4,4,4); A0[1,1,1]=1.0
  psi0 = MPS(A0, sites; cutoff=0.0, maxdim=64)
  v0 = site_to_column(mps_to_site_vector(psi0,sites),mapping)
  psi0x = expand(
    psi0,Lmpo;
    alg="global_krylov",krylovdim=4,cutoff=1e-30,
    apply_kwargs=(;maxdim=64,cutoff=1e-30),
  )
  vx = site_to_column(mps_to_site_vector(psi0x,sites),mapping)
  init_rel = norm(vx-v0)/norm(v0)
  init_rel < 1e-13 || error("expanded initial state changed")
  println("C1_CUTOFF_REFINE_INIT rel=$(init_rel) bond=$(maxlinkdim(psi0x))")

  vex = exp(Ldense*TTEST)*v0
  passes = Float64[]
  for cutoff in CUTOFFS
    psi = tdvp(
      Lmpo,TTEST,psi0x;
      time_step=DT,nsite=2,reverse_step=true,order=2,
      maxdim=64,cutoff=cutoff,normalize=false,
      updater_backend="exponentiate",
      updater_kwargs=(;tol=1e-13,krylovdim=30),outputlevel=0,
    )
    vtn = site_to_column(mps_to_site_vector(psi,siteinds(psi)),mapping)
    rtn = reshape(vtn,D,D); rex=reshape(vex,D,D)
    htd = half_trace_distance(rtn,rex)
    terr = abs(tr(rtn)-1)
    anti = norm(rtn-adjoint(rtn))
    vrel = norm(vtn-vex)/norm(vex)
    bond = maxlinkdim(psi)
    ok = htd < 1e-9 && terr < 1e-10 && anti < 1e-10
    if ok && cutoff > 0
      push!(passes,cutoff)
    end
    println("C1_CUTOFF_REFINE_POINT cutoff=$(cutoff) half_trace=$(htd) trace_err=$(terr) antiherm=$(anti) vec_rel=$(vrel) bond=$(bond) oracle_ok=$(ok ? 1 : 0)")
  end

  epsstar = isempty(passes) ? 0.0 : maximum(passes)
  eligible = epsstar >= 1e-26
  primary = eligible ? epsstar*1e-2 : 0.0
  tight = eligible ? epsstar*1e-4 : 0.0
  println("C1_CUTOFF_REFINE_SELECTION epsilon_star=$(epsstar) two_site_eligible=$(eligible ? 1 : 0) primary_cutoff=$(primary) tight_cutoff=$(tight) mpo_dense_rel=$(mpo_rel)")
  epsstar > 0 || error("no nonzero cutoff passed frozen oracle")
  println("VARIABLE_POLE_C1_MPDO_CUTOFF_REFINEMENT_COMPLETE")
end

main()
