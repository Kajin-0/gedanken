#!/usr/bin/env python3
"""Launch the coupled-Lindblad Padé SDP probe with explicit bath constants.

`coupled_lindblad_pade_sdp.py` uses `fp.HBAR` only in its detailed-balance
reporting diagnostic.  `heom_fp_harmonic_oracle` does not guarantee that symbol
as a public module attribute, so bind it explicitly from the canonical bath
module before calling the probe.  This changes no SDP, bath coefficient,
physical parameter, or acceptance logic.
"""
from direct_port_bath_correlation import HBAR
import coupled_lindblad_pade_sdp as probe

probe.fp.HBAR = HBAR

if __name__ == "__main__":
    probe.main()
