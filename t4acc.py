import sys
import math

# need to separate and blackbox
# what functions do we need?
# one to initialize variables/accept inputs

def data_init(iter, alt):
    alt = float(alt) * 1000
    iter = float(iter)

    incr_count = 0

    alt_inc = alt
    r_earth = 6370000
