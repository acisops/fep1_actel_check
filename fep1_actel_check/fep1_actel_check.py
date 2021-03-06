#!/usr/bin/env python

"""
========================
fep1_actel_check
========================

This code generates backstop load review outputs for checking the ACIS
FEP1 Actel temperature. It also generates FEP1 Actel model validation
plots comparing predicted values to telemetry for the previous three
weeks.
"""

# Matplotlib setup
# Use Agg backend for command-line (non-interactive) operation
import matplotlib
matplotlib.use('Agg')

import sys
from acis_thermal_check import \
    DPABoardTempCheck, \
    get_options
import os

model_path = os.path.abspath(os.path.dirname(__file__))


class FEP1ActelCheck(DPABoardTempCheck):
    def __init__(self):
        valid_limits = {'TMP_FEP1_ACTEL': [(1, 2.0), (50, 1.0), (99, 2.0)],
                        'PITCH': [(1, 3.0), (99, 3.0)],
                        'TSCPOS': [(1, 2.5), (99, 2.5)]
                        }
        hist_limit = [25., 20.0] # First limit is >=, second limit is <=
        super(FEP1ActelCheck, self).__init__("tmp_fep1_actel", "fep1_actel",
                                             valid_limits, hist_limit)


def main():
    args = get_options("fep1_actel", model_path)
    fep1_actel_check = FEP1ActelCheck()
    try:
        fep1_actel_check.run(args)
    except Exception as msg:
        if args.traceback:
            raise
        else:
            print("ERROR:", msg)
            sys.exit(1)

if __name__ == '__main__':
    main()
