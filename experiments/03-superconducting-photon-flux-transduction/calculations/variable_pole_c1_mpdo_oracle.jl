#!/usr/bin/env julia
# Deterministic small-system ITensorMPS oracle for Experiment-03 Gate C.1.
#
# This is an implementation oracle only.  It uses the same two-auxiliary toy
# realization as variable_pole_c1_liouvillian_oracle.py and compares:
#   1. the OpSum/MPO Liouvillian contracted back to a dense matrix against the
#      independently assembled column-vectorized dense generator;
#   2. two-site TDVP MPDO evolution against exact dense exp(L*t) at multiple
#      times.
#
# No Experiment-03 nonlinear open-system result is calculated here.

using LinearAlgebra
using ITensors
using ITensorMPS

const I2 = Matrix{ComplexF64}(I, 2, 2)
const B = ComplexF64[0 1; 0 0]
const BD = Matrix(adjoint(B))
const NOP = BD * B
const SX = ComplexF64[0 1; 1 0]
const SZ = ComplexF64[1 0; 0 -1]

leftop(A) = kron(I2, A)
rightop(A) = kron(transpose(A), I2)
sandop(A, C) = kron(transpose(C), A)

function only4(d, A)
  d == 4 || error("C1 MPDO oracle custom super-site operator requires d=4, got d=$d")
  return A
end

# Local Liouville-space operators, in local column-major vectorization.
ITensors.op(::OpName"LSx", ::SiteType"Qudit", d::Int) = only4(d, leftop(SX))
ITensors.op(::OpName"RSx", ::SiteType"Qudit", d::Int) = only4(d, rightop(SX))
ITensors.op(::OpName"LSz", ::SiteType"Qudit", d::Int) = only4(d, leftop(SZ))
ITensors.op(::OpName"RSz", ::SiteType"Qudit", d::Int) = only4(d, rightop(SZ))
ITensors.op(::OpName"Lb",  ::SiteType"Qudit", d::Int) = only4(d, leftop(B))
ITensors.op(::OpName"Lbd", ::SiteType"Qudit", d::Int) = only4(d, leftop(BD))
ITensors.op(::OpName"LN",  ::SiteType"Qudit", d::Int) = only4(d, leftop(NOP))
ITensors.op(::OpName"Rb",  ::SiteType"Qudit", d::Int) = only4(d, rightop(B))
ITensors.op(::OpName"Rbd", ::SiteType"Qudit", d::Int) = only4(d, rightop(BD))
ITensors.op(::OpName"RN",  ::SiteType"Qudit", d::Int) = only4(d, rightop(NOP))
ITensors.op(::OpName"Sb",  ::SiteType"Qudit", d::Int) = only4(d, sandop(B, BD))

function kronall(xs)
  z = ComplexF64[1;;]
  for x in xs
    z = kron(z, x)
  end
  return z
end

function embed(op, site, dims)
  return kronall([j == site ? op : Matrix{ComplexF64}(I, dims[j], dims[j]) for j in eachindex(dims)])
end

function dense_liouvillian(H, cs)
  D = size(H, 1)
  Ibig = Matrix{ComplexF64}(I, D, D)
  L = -1im * (kron(Ibig, H) - kron(transpose(H), Ibig))
  for c in cs
    n = adjoint(c) * c
    L += kron(conj(c), c) - 0.5 * kron(Ibig, n) - 0.5 * kron(transpose(n), Ibig)
  end
  return L
end

function unravel0(q, dims)
  out = zeros(Int, length(dims))
  x = q
  for j in length(dims):-1:1
    out[j] = mod(x, dims[j])
    x = div(x, dims[j])
  end
  return out
end

function ravel0(q, dims)
  x = 0
  for j in eachindex(dims)
    x = x * dims[j] + q[j]
  end
  return x
end

# mapping[site-vector index] = global column-vectorization index.
function site_to_column_mapping(dims)
  D = prod(dims)
  pdims = dims .^ 2
  mapping = zeros(Int, D^2)
  for r0 in 0:(D - 1), c0 in 0:(D - 1)
    r = unravel0(r0, dims)
    c = unravel0(c0, dims)
    pair = [r[j] + dims[j] * c[j] for j in eachindex(dims)]
    si = ravel0(pair, pdims) + 1
    ci = r0 + D * c0 + 1
    mapping[si] = ci
  end
  all(mapping .> 0) || error("invalid site/column permutation")
  return mapping
end

function mpo_to_site_dense(W, sites)
  T = contract(W)
  outs = prime.(sites)
  # Reversed axis order makes the last chain site the fastest linear index,
  # matching ordinary Kronecker-product basis ordering.
  A = array(T, reverse(outs)..., reverse(sites)...)
  N = prod(dim.(sites))
  return reshape(A, N, N)
end

function mps_to_site_vector(psi, sites)
  T = contract(psi)
  A = array(T, reverse(sites)...)
  return vec(A)
end

function site_to_column(vsite, mapping)
  vcol = similar(vsite)
  for j in eachindex(mapping)
    vcol[mapping[j]] = vsite[j]
  end
  return vcol
end

function build_dense_model()
  Hb = ComplexF64[0.73 0.21-0.08im; 0.21+0.08im 1.31]
  Lc = ComplexF64[0.37 0.0; 0.09+0.04im 0.28]
  Gamma = Lc * adjoint(Lc)
  g = ComplexF64[0.17+0.03im, -0.06+0.02im]

  dims = [2, 2, 2]
  Sx = embed(SX, 1, dims)
  Sz = embed(SZ, 1, dims)
  bs = [embed(B, j + 1, dims) for j in 1:2]

  H = 0.41 * Sz
  for j in 1:2, k in 1:2
    H += Hb[j, k] * adjoint(bs[j]) * bs[k]
  end
  for j in 1:2
    H += Sx * (g[j] * adjoint(bs[j]) + conj(g[j]) * bs[j])
  end

  cs = Matrix{ComplexF64}[]
  for mu in 1:2
    c = zeros(ComplexF64, prod(dims), prod(dims))
    for j in 1:2
      c += sqrt(2.0) * conj(Lc[j, mu]) * bs[j]
    end
    push!(cs, c)
  end
  return Hb, Lc, Gamma, g, dims, H, cs
end

function build_mpo(Hb, Gamma, g)
  sites = siteinds("Qudit", 3; dim=4)
  os = OpSum()

  # -i[0.41 sz, rho]
  os += (-1im * 0.41, "LSz", 1)
  os += ( 1im * 0.41, "RSz", 1)

  # -i[sum_jk Hb_jk b_j^dag b_k, rho]
  for j in 1:2, k in 1:2
    sj, sk = j + 1, k + 1
    h = Hb[j, k]
    if j == k
      os += (-1im * h, "LN", sj)
      os += ( 1im * h, "RN", sj)
    else
      os += (-1im * h, "Lbd", sj, "Lb", sk)
      os += ( 1im * h, "Rbd", sj, "Rb", sk)
    end
  end

  # -i[Sx sum_j(g_j b_j^dag + g_j* b_j), rho]
  for j in 1:2
    s = j + 1
    os += (-1im * g[j],       "LSx", 1, "Lbd", s)
    os += (-1im * conj(g[j]), "LSx", 1, "Lb",  s)
    os += ( 1im * g[j],       "RSx", 1, "Rbd", s)
    os += ( 1im * conj(g[j]), "RSx", 1, "Rb",  s)
  end

  # Direct Kossakowski form:
  # 2 Gamma_jk [ b_k rho b_j^dag - 1/2 {b_j^dag b_k, rho} ].
  for j in 1:2, k in 1:2
    sj, sk = j + 1, k + 1
    gam = Gamma[j, k]
    if j == k
      os += (2 * gam, "Sb", sj)
      os += (-gam, "LN", sj)
      os += (-gam, "RN", sj)
    else
      os += (2 * gam, "Rbd", sj, "Lb", sk)
      os += (-gam, "Lbd", sj, "Lb", sk)
      os += (-gam, "Rbd", sj, "Rb", sk)
    end
  end

  return sites, MPO(os, sites)
end

function half_trace_distance(a, b)
  return 0.5 * sum(svdvals(a - b))
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

  # Product density |0><0| on system and both auxiliaries, represented as a
  # product vector on local Liouville super-sites.
  A0 = zeros(ComplexF64, 4, 4, 4)
  A0[1, 1, 1] = 1.0
  psi0 = MPS(A0, sites; cutoff=0.0, maxdim=64)
  v0site = mps_to_site_vector(psi0, sites)
  v0col = site_to_column(v0site, mapping)

  D = prod(dims)
  rho0 = reshape(v0col, D, D)
  abs(tr(rho0) - 1) < 1e-14 || error("MPDO initial trace mismatch")

  # Oracle settings are deliberately much tighter than the production matrix;
  # they are committed before this workflow is first run.
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
      psi0;
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
    println("C1_MPDO_POINT tau=$(t) half_trace=$(htd) trace_err=$(terr) antiherm=$(anti) vec_rel=$(vrel) bond=$(maxlinkdim(psi))")
  end

  println("C1_MPDO_PACKAGES ITensorMPS=$(Base.pkgversion(ITensorMPS)) ITensors=$(Base.pkgversion(ITensors))")
  println("C1_MPDO_ORACLE mpo_dense_rel=$(mpo_rel) max_half_trace=$(max_half) max_trace_err=$(max_trace) max_antiherm=$(max_anti) max_vec_rel=$(max_vec_rel) max_bond=$(max_bond) oracle_dt=$(oracle_dt)")

  mpo_rel < 1e-12 || error("OpSum/MPO dense generator mismatch")
  max_half < 1e-9 || error("MPDO half-trace-distance oracle failure")
  max_trace < 1e-10 || error("MPDO trace oracle failure")
  max_anti < 1e-10 || error("MPDO Hermiticity oracle failure")
  println("VARIABLE_POLE_C1_MPDO_ORACLE_PASS")
end

main()
