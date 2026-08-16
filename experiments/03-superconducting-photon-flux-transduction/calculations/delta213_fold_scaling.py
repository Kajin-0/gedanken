#!/usr/bin/env python3
"""Run the validated periodic-fold scaling regression at delta=.213.

This point is the current crossover-independent dark-rate candidate.  The result
locates its actual finite-amplitude periodic fold and replaces obsolete safety
criteria based on the earlier local sphaleron instability r_x.
"""
import full_dynamic_rfsquid as fd
import periodic_fold_scaling as fs

if __name__=='__main__':
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        fs.run(.213)
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
