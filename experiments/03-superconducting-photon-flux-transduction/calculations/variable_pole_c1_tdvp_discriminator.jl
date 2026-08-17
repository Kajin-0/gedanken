#!/usr/bin/env julia
# Frozen non-Hermitian TDVP discriminator for Experiment-03 C1.
# See VARIABLE_POLE_C1_TDVP_DISCRIMINATOR_FREEZE_2026-08-17.md.
#
# This uses only the small toy dense oracle. No accepted rank-16 physical
# harmonic evolution and no nonlinear C1 calculation is performed here.

using LinearAlgebra
using ITensors
using ITensorMPS

srcpath = joinpath(@__DIR__, "variable_pole_c1_mpdo_oracle.jl")
src = read(srcpath, String)
src = replace(src, r"\nmain\(\)\s*$" => "\n")
include_string(Main, src, srcpath * "[definitions-only]")

const TTEST = 1.0e-3
const DTS = (2.0e-5, 1.0e-5, 5.0e-6, 2.5e-6)

function expanded_initial(Lmpo, sites, dims, mapping)
  A0 = zeros(ComplexF64, 4, 4, 4)
  A0[1, 1, 1] = 1.0
  psi0 = MPS(A0, sites; cutoff=0.0, maxdim=64)
  v0 = site_to_column(mps_to_site_vector(psi0, sites), mapping)
  psi0x = expand(
    psi0,
    Lmpo;
    alg="global_krylov",
    krylovdim=4,
    cutoff=1e-14,
    apply_kwargs=(; maxdim=64, cutoff=1e-14),
  )
  vx = site_to_column(mps_to_site_vector(psi0x, sites), mapping)
  init_rel = norm(vx - v0) / norm(v0)
  D = prod(dims)
  init_trace = abs(tr(reshape(vx, D, D)) - 1)
  println("C1_TDVP_DISCRIM_INIT rel=$(init_rel) trace_err=$(init_trace) bond=$(maxlinkdim(psi0x))")
  init_rel < 1e-13 || error("expanded initial state changed")
  init_trace < 1e-13 || error("expanded initial trace changed")
  return psi0x, v0
end

function point(Lmpo, psi0x, v0, vex, D; nsite, reverse_step, dt, label)
  nstep = round(Int, TTEST / dt)
  abs(nstep * dt - TTEST) < 1e-14 || error("TTEST/dt not integer")
  psi = tdvp(
    Lmpo,
    TTEST,
    psi0x;
    time_step=dt,
    nsite=nsite,
    reverse_step=reverse_step,
    order=2,
    maxdim=64,
    cutoff=1e-14,
    normalize=false,
    updater_backend="exponentiate",
    updater_kwargs=(; tol=1e-13, krylovdim=30),
    outputlevel=0,
  )
  mapping = site_to_column_mapping([2,2,2])
  vtn = site_to_column(mps_to_site_vector(psi, siteinds(psi)), mapping)
  rtn = reshape(vtn, D, D)
  rex = reshape(vex, D, D)
  htd = half_trace_distance(rtn, rex)
  terr = abs(tr(rtn) - 1)
  anti = norm(rtn - adjoint(rtn))
  vrel = norm(vtn - vex) / norm(vex)
  bond = maxlinkdim(psi)
  ok = htd < 1e-9 && terr < 1e-10 && anti < 1e-10
  println("C1_TDVP_DISCRIM label=$(label) nsite=$(nsite) reverse=$(reverse_step) dt=$(dt) nstep=$(nstep) half_trace=$(htd) trace_err=$(terr) antiherm=$(anti) vec_rel=$(vrel) bond=$(bond) oracle_ok=$(ok ? 1 : 0)")
  return (; label, nsite, reverse_step, dt, htd, terr, anti, vrel, bond, ok)
end

function convergence_summary(rows, label)
  r = filter(x -> x.label == label, rows)
  sort!(r; by=x -> x.dt, rev=true)
  println("C1_TDVP_SERIES label=$(label)")
  for j in 2:length(r)
    prev, cur = r[j-1], r[j]
    ratio_h = prev.htd / max(cur.htd, eps(Float64))
    ratio_t = prev.terr / max(cur.terr, eps(Float64))
    p_h = log(ratio_h) / log(2)
    p_t = log(ratio_t) / log(2)
    println("C1_TDVP_RATIO label=$(label) dt_hi=$(prev.dt) dt_lo=$(cur.dt) half_ratio=$(ratio_h) half_order=$(p_h) trace_ratio=$(ratio_t) trace_order=$(p_t)")
  end
  finest = r[end]
  anyok = any(x -> x.ok, r)
  println("C1_TDVP_FINEST label=$(label) dt=$(finest.dt) half_trace=$(finest.htd) trace_err=$(finest.terr) any_oracle_pass=$(anyok ? 1 : 0)")
  return anyok
end

function main()
  Hb, Lc, Gamma, g, dims, H, cs = build_dense_model()
  Ldense = dense_liouvillian(H, cs)
  sites, Lmpo = build_mpo(Hb, Gamma, g)
  mapping = site_to_column_mapping(dims)

  Lsite = mpo_to_site_dense(Lmpo, sites)
  Lfrommpo = zeros(ComplexF64, size(Ldense))
  for a in eachindex(mapping), b in eachindex(mapping)
    Lfrommpo[mapping[a], mapping[b]] = Lsite[a, b]
  end
  mpo_rel = norm(Lfrommpo - Ldense) / norm(Ldense)
  mpo_rel < 1e-12 || error("MPO/dense generator mismatch")

  psi0x, v0 = expanded_initial(Lmpo, sites, dims, mapping)
  vex = exp(Ldense * TTEST) * v0
  D = prod(dims)

  rows = NamedTuple[]
  for dt in DTS
    push!(rows, point(Lmpo, psi0x, v0, vex, D; nsite=2, reverse_step=true,  dt=dt, label="two_reverse"))
  end
  for dt in DTS
    push!(rows, point(Lmpo, psi0x, v0, vex, D; nsite=1, reverse_step=true,  dt=dt, label="one_reverse"))
  end
  for dt in DTS
    push!(rows, point(Lmpo, psi0x, v0, vex, D; nsite=2, reverse_step=false, dt=dt, label="two_noreverse"))
  end

  pass_two = convergence_summary(rows, "two_reverse")
  pass_one = convergence_summary(rows, "one_reverse")
  pass_norev = convergence_summary(rows, "two_noreverse")

  println("C1_TDVP_DISCRIM_SUMMARY mpo_dense_rel=$(mpo_rel) standard_two_pass=$(pass_two ? 1 : 0) one_site_candidate=$(pass_one ? 1 : 0) noreverse_diagnostic_pass=$(pass_norev ? 1 : 0)")
  println("VARIABLE_POLE_C1_TDVP_DISCRIMINATOR_COMPLETE")
end

main()
