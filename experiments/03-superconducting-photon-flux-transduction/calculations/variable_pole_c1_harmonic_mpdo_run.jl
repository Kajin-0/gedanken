#!/usr/bin/env julia
# Frozen finite-bosonic harmonic MPDO runner for Experiment-03 Gate C.1.
# Cases H0/H1/H2 are defined in
# VARIABLE_POLE_C1_FINITE_BOSONIC_HARMONIC_ACCEPTANCE_2026-08-17.md.

using LinearAlgebra
using DelimitedFiles
using JSON3
using ITensors
using ITensorMPS

# Reuse the exact physical-input loader and Liouvillian construction which are
# independently exercised by the construction preflight. Strip only its main().
buildpath=joinpath(@__DIR__,"variable_pole_c1_harmonic_mpdo_build.jl")
src=read(buildpath,String)
src=replace(src,r"\nmain\(\)\s*$"=>"\n")
include_string(Main,src,buildpath*"[definitions-only]")

ITensors.state(::StateName"VacL", ::SiteType"Qudit", d::Int) = vcat(ComplexF64[1],zeros(ComplexF64,d-1))
function ITensors.state(::StateName"TraceL", ::SiteType"Qudit", d::Int)
  h=hilbert_dim(d); v=zeros(ComplexF64,d)
  for n in 0:(h-1); v[1+n+h*n]=1; end
  return v
end
function ITensors.state(::StateName"TopL", ::SiteType"Qudit", d::Int)
  h=hilbert_dim(d); v=zeros(ComplexF64,d); n=h-1; v[1+n+h*n]=1; return v
end

function reduced_system(psi,sites)
  T=psi[1]
  for j in 2:length(sites)
    T *= psi[j]*state(sites[j],"TraceL")
  end
  v=vec(array(T,sites[1]))
  h=hilbert_dim(dim(sites[1]))
  return reshape(v,h,h)
end

function fulltrace(psi,sites)
  bra=MPS(sites,fill("TraceL",length(sites)))
  return inner(bra,psi)
end

function top_population(psi,sites,j)
  names=[k==j ? "TopL" : "TraceL" for k in eachindex(sites)]
  return inner(MPS(sites,names),psi)
end

function oscillator_ops(h)
  b=boson(h); bd=adjoint(b)
  x=SIGMA0[]*(b+bd)
  u=1im*SIGMA0[]*(bd-b)
  return Matrix(x),Matrix(u)
end

function read_ref(dir)
  return readcomplex(joinpath(dir,"rho_fdt16.csv"),(16,16))
end

function halftrace(A,B)
  return 0.5*sum(svdvals(A-B))
end

function metrics(psi,sites,rhoref,targetx,targetu,tau)
  rho=reduced_system(psi,sites)
  h=size(rho,1); x,u=oscillator_ops(h)
  trsys=tr(rho); trfull=fulltrace(psi,sites)
  anti=norm(rho-adjoint(rho))
  rh=0.5*(rho+adjoint(rho)); ev=eigvalsh(Hermitian(rh)); neg=sum(max(-q,0.0) for q in ev)
  mx=real(tr(rho*x)); mu=real(tr(rho*u))
  vx=max(real(tr(rho*(x*x)))-mx*mx,0.0); vu=max(real(tr(rho*(u*u)))-mu*mu,0.0)
  sx=sqrt(vx); su=sqrt(vu)
  qp=0.5*real(tr(rho*(x*u+u*x)))-mx*mu
  qpn=abs(qp)/max(sx*su,1e-300)
  relx=sx/targetx-1; relu=su/targetu-1; maxwidth=max(abs(relx),abs(relu))
  re=zeros(ComplexF64,16,16); re[1:h,1:h]=rho
  htd=halftrace(re,rhoref)
  tops=[real(top_population(psi,sites,j)) for j in eachindex(sites)]
  out=(;tau,rho,trsys,trfull,anti,neg,sx,su,relx,relu,maxwidth,qpn,htd,tops,bond=maxlinkdim(psi))
  println("C1_HARMONIC_MPDO_POINT tau=$(tau) trfull=$(trfull) trsys=$(trsys) anti=$(anti) neg=$(neg) sx=$(sx) su=$(su) relx=$(relx) relu=$(relu) maxwidth=$(maxwidth) qp=$(qpn) half_fdt=$(htd) bond=$(out.bond) sys_top=$(tops[1]) bath0_top=$(tops[2]) bath_top_max=$(maximum(tops[2:end]))")
  return out
end

function casecfg(name)
  if name=="H0"
    return (;high=false,dt=.02,maxdim=128,cutoff=1e-25,krylov=1e-11)
  elseif name=="H1"
    return (;high=false,dt=.01,maxdim=256,cutoff=1e-27,krylov=1e-13)
  elseif name=="H2"
    return (;high=true,dt=.01,maxdim=256,cutoff=1e-27,krylov=1e-13)
  end
  error("unknown frozen case $name")
end

function propagate_segment(L,psi,dtau,cfg)
  n=round(Int,dtau/cfg.dt)
  abs(n*cfg.dt-dtau)<1e-12 || error("checkpoint segment not divisible by frozen dt")
  return tdvp(
    L,dtau,psi;
    time_step=cfg.dt,nsite=2,reverse_step=true,order=2,
    maxdim=cfg.maxdim,cutoff=cfg.cutoff,normalize=false,
    updater_backend="exponentiate",
    updater_kwargs=(;tol=cfg.krylov,krylovdim=30),outputlevel=0,
  )
end

function main()
  length(ARGS)>=2 || error("usage: julia variable_pole_c1_harmonic_mpdo_run.jl INPUT_DIR H0|H1|H2")
  dir,name=ARGS[1],ARGS[2]; cfg=casecfg(name)
  Hb,Gamma,g,meta=loadinputs(dir)
  sites,L,hdim=build_liouvillian(Hb,Gamma,g;high=cfg.high)
  rhoref=read_ref(dir); targetx=Float64(meta.fdt_target_x); targetu=Float64(meta.fdt_target_u)
  psi=MPS(sites,fill("VacL",length(sites)))
  println("C1_HARMONIC_MPDO_START case=$(name) dt=$(cfg.dt) maxdim=$(cfg.maxdim) cutoff=$(cfg.cutoff) krylov=$(cfg.krylov) mpo_maxlink=$(maximum(linkdims(L))) initial_bond=$(maxlinkdim(psi))")
  abs(fulltrace(psi,sites)-1)<1e-13 || error("initial MPDO trace failure")

  checkpoints=(160.0,200.0,220.0,240.0); rows=NamedTuple[]; prev=0.0
  for tau in checkpoints
    psi=propagate_segment(L,psi,tau-prev,cfg); prev=tau
    push!(rows,metrics(psi,sites,rhoref,targetx,targetu,tau))
  end

  f=rows[end]; m220=rows[end-1]; m200=rows[end-2]
  late240=halftrace(f.rho,m220.rho); late220=halftrace(m220.rho,m200.rho)
  wd240=max(abs(f.sx/m220.sx-1),abs(f.su/m220.su-1))
  wd220=max(abs(m220.sx/m200.sx-1),abs(m220.su/m200.su-1))
  phys=all(abs(r.trfull-1)<1e-8 && abs(r.trsys-1)<1e-8 && r.anti<1e-8 && r.neg<5e-8 for r in rows)
  fdt=f.maxwidth<1e-5 && f.htd<2e-5 && f.qpn<2e-5
  stationary=late240<2e-6 && late220<5e-6 && wd240<2e-6 && wd220<5e-6
  println("C1_HARMONIC_MPDO_FINAL case=$(name) physical=$(phys ? 1 : 0) fdt=$(fdt ? 1 : 0) stationary=$(stationary ? 1 : 0) half220_240=$(late240) half200_220=$(late220) width220_240=$(wd240) width200_220=$(wd220) final_width=$(f.maxwidth) final_half=$(f.htd) final_qp=$(f.qpn) maxbond=$(maximum(r.bond for r in rows))")

  # Per-case gates are enforced here. Cross-case H0/H1/H2 convergence is
  # evaluated by a separate deterministic reducer after the complete matrix.
  phys || error("finite-bosonic harmonic physicality failure")
  fdt || error("finite-bosonic harmonic exact-FDT failure")
  stationary || error("finite-bosonic harmonic late-stationarity failure")
  println("VARIABLE_POLE_C1_HARMONIC_MPDO_CASE_PASS case=$(name)")
end

main()
