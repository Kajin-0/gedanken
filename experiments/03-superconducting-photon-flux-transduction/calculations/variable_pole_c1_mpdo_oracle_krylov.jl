#!/usr/bin/env julia
# Repaired Experiment-03 C1 MPDO oracle after the product-start TDVP diagnostic.
#
# The original oracle source is retained unchanged as provenance.  This wrapper
# loads its independently validated generator/MPO definitions without executing
# its original main(), then applies the predeclared global-Krylov MPS basis
# expansion frozen in VARIABLE_POLE_C1_MPDO_INITIALIZATION_AMENDMENT_2026-08-17.md.

using LinearAlgebra
using ITensors
using ITensorMPS

srcpath = joinpath(@__DIR__, "variable_pole_c1_mpdo_oracle.jl")
src = read(srcpath, String)
src = replace(src, r"\nmain\(\)\s*$" => "\n")
include_string(Main, src, srcpath * "[definitions-only]")

function repaired_main()
  Hb, Lc, Gamma, g, dims, H, cs = build_dense_model()
  Ldense = dense_liouvillian(H, cs)
  sites, Lmpo = build_mpo(Hb, Gamma, g)
  mapping = site_to_column_mapping(dims)

  # Keep the original independent MPO-to-dense generator check.
  Lsite = mpo_to_site_dense(Lmpo, sites)
  Lfrommpo = zeros(ComplexF64, size(Ldense))
  for a in eachindex(mapping), b in eachindex(mapping)
    Lfrommpo[mapping[a], mapping[b]] = Lsite[a, b]
  end
  mpo_rel = norm(Lfrommpo - Ldense) / norm(Ldense)

  A0 = zeros(ComplexF64, 4, 4, 4)
  A0[1, 1, 1] = 1.0
  psi0 = MPS(A0, sites; cutoff=0.0, maxdim=64)
  v0site = mps_to_site_vector(psi0, sites)
  v0col = site_to_column(v0site, mapping)

  D = prod(dims)
  rho0 = reshape(v0col, D, D)
  abs(tr(rho0) - 1) < 1e-14 || error("MPDO initial trace mismatch")

  # Frozen implementation repair: enlarge the variational basis with four
  # global Krylov vectors while leaving the represented initial state unchanged.
  psi0x = expand(
    psi0,
    Lmpo;
    alg="global_krylov",
    krylovdim=4,
    cutoff=1e-14,
    apply_kwargs=(; maxdim=64, cutoff=1e-14),
  )
  v0x = site_to_column(mps_to_site_vector(psi0x, sites), mapping)
  init_rel = norm(v0x - v0col) / norm(v0col)
  init_trace = abs(tr(reshape(v0x, D, D)) - 1)
  println("C1_MPDO_KRYLOV_INIT rel=$(init_rel) trace_err=$(init_trace) bond=$(maxlinkdim(psi0x))")
  init_rel < 1e-13 || error("global-Krylov expansion changed initial MPDO")
  init_trace < 1e-13 || error("global-Krylov expansion changed initial trace")

  # Original oracle settings and thresholds remain unchanged.
  oracle_dt = 1.0e-5
  times = (0.001, 0.003, 0.005)
  max_half = 0.0
  max_trace = 0.0
  max_anti = 0.0
  max_vec_rel = 0.0
  max_bond = 0

  for t in times
    nstep = round(Int, t / oracle_dt)
    abs(nstep * oracle_dt - t) < 1e-14 || error("oracle time not divisible by dt")
    psi = tdvp(
      Lmpo,
      t,
      psi0x;
      time_step=oracle_dt,
      nsite=2,
      maxdim=64,
      cutoff=1e-14,
      normalize=false,
      updater_kwargs=(; tol=1e-13, krylovdim=30),
      outputlevel=0,
    )
    max_bond = max(max_bond, maxlinkdim(psi))
    vtn = site_to_column(mps_to_site_vector(psi, sites), mapping)
    vex = exp(Ldense * t) * v0col
    rtn = reshape(vtn, D, D)
    rex = reshape(vex, D, D)
    htd = half_trace_distance(rtn, rex)
    terr = abs(tr(rtn) - 1)
    anti = norm(rtn - adjoint(rtn))
    vrel = norm(vtn - vex) / norm(vex)
    max_half = max(max_half, htd)
    max_trace = max(max_trace, terr)
    max_anti = max(max_anti, anti)
    max_vec_rel = max(max_vec_rel, vrel)
    println("C1_MPDO_KRYLOV_POINT tau=$(t) half_trace=$(htd) trace_err=$(terr) antiherm=$(anti) vec_rel=$(vrel) bond=$(maxlinkdim(psi))")
  end

  println("C1_MPDO_KRYLOV_PACKAGES ITensorMPS=$(Base.pkgversion(ITensorMPS)) ITensors=$(Base.pkgversion(ITensors))")
  println("C1_MPDO_KRYLOV_ORACLE mpo_dense_rel=$(mpo_rel) init_rel=$(init_rel) max_half_trace=$(max_half) max_trace_err=$(max_trace) max_antiherm=$(max_anti) max_vec_rel=$(max_vec_rel) max_bond=$(max_bond) oracle_dt=$(oracle_dt)")

  mpo_rel < 1e-12 || error("OpSum/MPO dense generator mismatch")
  max_half < 1e-9 || error("MPDO half-trace-distance oracle failure")
  max_trace < 1e-10 || error("MPDO trace oracle failure")
  max_anti < 1e-10 || error("MPDO Hermiticity oracle failure")
  println("VARIABLE_POLE_C1_MPDO_KRYLOV_ORACLE_PASS")
end

repaired_main()
