#!/usr/bin/env julia
# Physical rank-16 one-step production-setting TDVP smoke.
# Frozen by VARIABLE_POLE_C1_HARMONIC_ONE_STEP_FREEZE_2026-08-17.md.
# No FDT/equilibrium interpretation is performed here.

using LinearAlgebra
using ITensors
using ITensorMPS

runpath=joinpath(@__DIR__,"variable_pole_c1_harmonic_mpdo_run.jl")
src=read(runpath,String)
src=replace(src,r"\nmain\(\)\s*$"=>"\n")
include_string(Main,src,runpath*"[definitions-only]")

function main()
  length(ARGS)>=1 || error("usage: julia variable_pole_c1_harmonic_one_step.jl INPUT_DIR")
  Hb,Gamma,g,meta=loadinputs(ARGS[1])
  sites,L,hdim=build_liouvillian(Hb,Gamma,g;high=false)
  cfg=casecfg("H0")
  psi=MPS(sites,fill("VacL",length(sites)))

  tr0=fulltrace(psi,sites)
  abs(tr0-1)<1e-13 || error("initial full trace mismatch")

  psi=propagate_segment(L,psi,.02,cfg)
  rho=reduced_system(psi,sites)
  trfull=fulltrace(psi,sites)
  trsys=tr(rho)
  anti=norm(rho-adjoint(rho))
  rh=0.5*(rho+adjoint(rho))
  ev=eigvalsh(Hermitian(rh))
  neg=sum(max(-q,0.0) for q in ev)
  bond=maxlinkdim(psi)
  tops=[real(top_population(psi,sites,j)) for j in eachindex(sites)]

  fullerr=abs(trfull-1); syserr=abs(trsys-1)
  println("C1_HARMONIC_ONE_STEP tau=0.02 full_trace=$(trfull) full_err=$(fullerr) sys_trace=$(trsys) sys_err=$(syserr) anti=$(anti) negmass=$(neg) bond=$(bond) sys_top=$(tops[1]) bath0_top=$(tops[2]) bath_top_max=$(maximum(tops[2:end])) mpo_maxlink=$(maximum(linkdims(L)))")

  fullerr<1e-9 || error("one-step full trace failure")
  syserr<1e-9 || error("one-step reduced trace failure")
  anti<1e-9 || error("one-step Hermiticity failure")
  neg<5e-9 || error("one-step reduced positivity failure")
  bond<=128 || error("one-step maxdim saturation beyond frozen cap")
  println("VARIABLE_POLE_C1_HARMONIC_ONE_STEP_PASS")
end

main()
