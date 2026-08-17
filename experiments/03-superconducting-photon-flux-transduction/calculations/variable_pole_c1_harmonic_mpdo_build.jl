#!/usr/bin/env julia
# Physical rank-16 harmonic MPDO Liouvillian construction preflight.
# Builds the exact accepted 17-site finite-bosonic generator but performs no
# physical time propagation and no nonlinear C1 calculation.

using LinearAlgebra
using DelimitedFiles
using JSON3
using ITensors
using ITensorMPS

const SIGMA0 = Ref(0.0)
const LAMBDA_CT = Ref(0.0)

# Compatibility helper used here and by the runner which imports this file.
# Julia LinearAlgebra exposes eigvals(Hermitian(...)); unlike NumPy it has no
# eigvalsh symbol.
eigvalsh(A::Hermitian)=eigvals(A)

function hilbert_dim(superdim::Int)
  h = round(Int, sqrt(superdim))
  h*h == superdim || error("Liouville site dimension $superdim is not a square")
  return h
end

function boson(h::Int)
  b = zeros(ComplexF64,h,h)
  for n in 1:(h-1)
    b[n,n+1] = sqrt(n)
  end
  return b
end

leftop(A) = kron(Matrix{ComplexF64}(I,size(A,1),size(A,1)), A)
rightop(A) = kron(transpose(A), Matrix{ComplexF64}(I,size(A,1),size(A,1)))
sandop(A,C) = kron(transpose(C), A)

function localops(d::Int)
  h=hilbert_dim(d); b=boson(h); bd=adjoint(b); n=bd*b
  return h,b,Matrix(bd),Matrix(n)
end

ITensors.op(::OpName"LB",  ::SiteType"Qudit", d::Int) = leftop(localops(d)[2])
ITensors.op(::OpName"LBD", ::SiteType"Qudit", d::Int) = leftop(localops(d)[3])
ITensors.op(::OpName"LN",  ::SiteType"Qudit", d::Int) = leftop(localops(d)[4])
ITensors.op(::OpName"RB",  ::SiteType"Qudit", d::Int) = rightop(localops(d)[2])
ITensors.op(::OpName"RBD", ::SiteType"Qudit", d::Int) = rightop(localops(d)[3])
ITensors.op(::OpName"RN",  ::SiteType"Qudit", d::Int) = rightop(localops(d)[4])
ITensors.op(::OpName"SB",  ::SiteType"Qudit", d::Int) = sandop(localops(d)[2],localops(d)[3])

function sys_x(h)
  b=boson(h); return SIGMA0[]*(b+adjoint(b))
end
function sys_h(h)
  b=boson(h); n=adjoint(b)*b; x=sys_x(h)
  return Matrix(n + 0.5I + LAMBDA_CT[]*(x*x))
end
ITensors.op(::OpName"LSYS", ::SiteType"Qudit", d::Int) = leftop(sys_h(hilbert_dim(d)))
ITensors.op(::OpName"RSYS", ::SiteType"Qudit", d::Int) = rightop(sys_h(hilbert_dim(d)))
ITensors.op(::OpName"LX",   ::SiteType"Qudit", d::Int) = leftop(sys_x(hilbert_dim(d)))
ITensors.op(::OpName"RX",   ::SiteType"Qudit", d::Int) = rightop(sys_x(hilbert_dim(d)))

function readcomplex(path, shape)
  z=readdlm(path,',',Float64;header=true)[1]
  vals=ComplexF64.(z[:,1]) .+ 1im.*ComplexF64.(z[:,2])
  if length(shape)==1
    return reshape(vals,shape[1])
  end
  return permutedims(reshape(vals,shape[2],shape[1]))
end

function loadinputs(dir)
  meta=JSON3.read(read(joinpath(dir,"meta.json"),String))
  H=readcomplex(joinpath(dir,"H16.csv"),(16,16))
  G=readcomplex(joinpath(dir,"Gamma16.csv"),(16,16))
  g=readcomplex(joinpath(dir,"g16.csv"),(16,))
  SIGMA0[]=Float64(meta.sigma0); LAMBDA_CT[]=Float64(meta.counterterm_lambda)
  return H,G,g,meta
end

function build_liouvillian(Hb,Gamma,g; high=false)
  hs = high ? 8 : 6
  hb = high ? vcat([8],fill(6,15)) : vcat([6],fill(4,15))
  hdim=vcat([hs],hb)
  sites=[Index(h*h,"Site,Qudit,n=$(j)") for (j,h) in enumerate(hdim)]
  os=OpSum()
  os += (-1im,"LSYS",1); os += (1im,"RSYS",1)

  for j in 1:16, k in 1:16
    h=Hb[j,k]
    iszero(h) && continue
    sj=j+1; sk=k+1
    if j==k
      os += (-1im*h,"LN",sj); os += (1im*h,"RN",sj)
    else
      os += (-1im*h,"LBD",sj,"LB",sk)
      os += ( 1im*h,"RBD",sj,"RB",sk)
    end
  end

  for j in 1:16
    gj=g[j]; sj=j+1
    iszero(gj) && continue
    os += (-1im*gj,      "LX",1,"LBD",sj)
    os += (-1im*conj(gj),"LX",1,"LB", sj)
    os += ( 1im*gj,      "RX",1,"RBD",sj)
    os += ( 1im*conj(gj),"RX",1,"RB", sj)
  end

  for j in 1:16, k in 1:16
    gam=Gamma[j,k]
    iszero(gam) && continue
    sj=j+1; sk=k+1
    if j==k
      os += (2gam,"SB",sj)
      os += (-gam,"LN",sj)
      os += (-gam,"RN",sj)
    else
      os += (2gam,"RBD",sj,"LB",sk)
      os += (-gam,"LBD",sj,"LB",sk)
      os += (-gam,"RBD",sj,"RB",sk)
    end
  end
  return sites,MPO(os,sites),hdim
end

function main()
  length(ARGS)>=1 || error("usage: julia variable_pole_c1_harmonic_mpdo_build.jl INPUT_DIR [primary|high]")
  high=length(ARGS)>=2 && ARGS[2]=="high"
  Hb,Gamma,g,meta=loadinputs(ARGS[1])
  hermH=norm(Hb-adjoint(Hb))/norm(Hb)
  hermG=norm(Gamma-adjoint(Gamma))/norm(Gamma)
  mineig=minimum(eigvalsh(Hermitian(Gamma)))
  sites,L,hdim=build_liouvillian(Hb,Gamma,g;high=high)
  links=linkdims(L)
  println("C1_HARMONIC_MPO_BUILD class=$(high ? "high" : "primary") sites=$(length(sites)) hilbert_dims=$(join(hdim,',')) super_dims=$(join(dim.(sites),','))")
  println("C1_HARMONIC_MPO_STRUCTURE links=$(join(links,',')) maxlink=$(maximum(links)) Hherm=$(hermH) Gherm=$(hermG) Gmineig=$(mineig) gtail=$(norm(g[2:end])/norm(g)) sigma0=$(SIGMA0[]) lambda=$(LAMBDA_CT[])")
  hermH < 1e-12 || error("H bath Hermiticity regression")
  hermG < 1e-12 || error("Gamma Hermiticity regression")
  mineig > -1e-12 || error("Gamma positivity regression")
  maximum(links) <= 1024 || error("physical Liouvillian MPO bond exceeds preflight feasibility ceiling")
  println("VARIABLE_POLE_C1_HARMONIC_MPDO_BUILD_PASS")
end

main()
