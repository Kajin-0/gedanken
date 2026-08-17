#!/usr/bin/env julia
# Zero-time/derivative smoke test for the physical rank-16 finite-bosonic MPDO.
# This checks state-vectorization, trace bras, partial trace, and trace
# preservation of the exact accepted Liouvillian. It performs no time evolution.

using LinearAlgebra
using ITensors
using ITensorMPS

runpath=joinpath(@__DIR__,"variable_pole_c1_harmonic_mpdo_run.jl")
src=read(runpath,String)
src=replace(src,r"\nmain\(\)\s*$"=>"\n")
include_string(Main,src,runpath*"[definitions-only]")

function main()
  length(ARGS)>=1 || error("usage: julia variable_pole_c1_harmonic_mpdo_smoke.jl INPUT_DIR")
  Hb,Gamma,g,meta=loadinputs(ARGS[1])
  sites,L,hdim=build_liouvillian(Hb,Gamma,g;high=false)
  psi=MPS(sites,fill("VacL",length(sites)))

  tr0=fulltrace(psi,sites)
  rho0=reduced_system(psi,sites)
  target=zeros(ComplexF64,hdim[1],hdim[1]); target[1,1]=1
  rho0err=norm(rho0-target)
  anti0=norm(rho0-adjoint(rho0))

  # One exact MPO application probes the full Kossakowski/Hamiltonian generator
  # without introducing TDVP or SVD time-stepping error.
  dpsi=apply(L,psi;cutoff=0.0,maxdim=4096)
  dtrfull=fulltrace(dpsi,sites)
  drho=reduced_system(dpsi,sites)
  dtrsys=tr(drho)
  danti=norm(drho-adjoint(drho))
  dbond=maxlinkdim(dpsi)

  println("C1_HARMONIC_MPDO_SMOKE tr0=$(tr0) rho0err=$(rho0err) anti0=$(anti0) dtrfull=$(dtrfull) dtrsys=$(dtrsys) danti=$(danti) mpo_maxlink=$(maximum(linkdims(L))) derivative_bond=$(dbond)")

  abs(tr0-1)<1e-13 || error("initial full trace mismatch")
  rho0err<1e-13 || error("initial reduced vacuum mismatch")
  anti0<1e-13 || error("initial reduced state not Hermitian")
  abs(dtrfull)<1e-10 || error("full Liouvillian is not trace preserving")
  abs(dtrsys)<1e-10 || error("reduced derivative trace is not zero")
  danti<1e-10 || error("reduced derivative is not Hermiticity preserving")
  println("VARIABLE_POLE_C1_HARMONIC_MPDO_SMOKE_PASS")
end

main()
