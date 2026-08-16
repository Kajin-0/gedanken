#!/usr/bin/env python3
"""Persist deposited-energy-density robustness for the R80/alpha=.90 branch."""
from pathlib import Path
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson

OUT=Path('../RESULTS_ENERGY_DENSITY_ROBUSTNESS_2026-08-15.md')

def main():
    model=DynamicForce(.6,quick=False,Tmax=1.05)
    lines=['# Experiment 03 — Deposited-Energy-Density Robustness — 2026-08-15','',
           'R=80 ohm, alpha=.90, delta=.05, C=215 fF; stationary external-bath TWA/GLE.','',
           '```text']
    for s in (.70,.75,.80,.85,.90,.95,1.,1.05,1.10,1.15,1.20,1.25,1.30):
        o=run_case(model,8.,R=80.,alpha=.90,ntraj=2048,dt_ps=.25,seed=313131,
                   area_um2=100./s,rise_ps=20.)
        n=int(o['ntraj']);k=int(o['n_right_final']);lo,hi=wilson(k,n)
        lines.append(f'energyScale={s:.3f}; Aeff={100/s:.6f} um2; '
                     f'coldReg=({o["cold_reg_x"]:.6f},{o["cold_reg_u"]:.6f}); '
                     f'P_reform={o["P_xright_reform"]:.8f}; P_final={o["P_right_final"]:.8f}; '
                     f'CI95=[{lo:.8f},{hi:.8f}]; fail={n-k}; reform={o["reform_ps"]:.4f} ps; '
                     f'xR={o["mean_x_reform"]:+.6f}+-{o["sigma_x_reform"]:.6f}; '
                     f'uR={o["mean_u_reform"]:+.6f}+-{o["sigma_u_reform"]:.6f}')
    lines += ['```','',
              'This is a deterministic energy-density sensitivity scan under the stationary external bath; stochastic electron-phonon/partition noise is not generated explicitly.']
    OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'wrote {OUT}')
if __name__=='__main__':main()
