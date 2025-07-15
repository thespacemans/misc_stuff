# sys for argument acceptance, math for operations
import sys
import math
from decimal import Decimal

# Globals
# earth radius in meters (6.37 million)
r_earth = 6370000
# speed of light in m/s
c_speed = 299792458
# constant in meters per second, squared
grav_const = 9.80665


def printOutput(alt, iter, time_total, vel_total):
    print("Altitude: ", alt, "m | ", "Iterator: ", iter, " m")
    print("Time (hrs): ", round((time_total / 3600), 2), " hrs")
    print("Time total: ", time_total, " s")
    print("Final velocity: ", round(vel_total, 3), " m/s")
    print("Speed of light: ", c_speed, " m/s | ", round((vel_total / c_speed), 3), "c")


def calcGravity(alt_inc):
    grav_new = grav_const * math.pow((r_earth / (r_earth + alt_inc)), 2)
    grav_new = round(grav_new, 4)
    return grav_new


def main(iter, alt):

    # cast arguments to floats to avoid bugs
    # convert kilometers to meters
    alt = Decimal(alt) * 1000
    # already in meters or fractions of meters
    iter = Decimal(iter)

    inc_count = 0  # iteration counter for debugging

    alt_inc = alt  # assign total altitude to counter variable

    grav_new = calcGravity(alt_inc)

    time_inc = 0  # time increment in fractions of seconds
    time_total = 0  # time totaled from increments

    vel_total = 0  # total velocity summed from acceleration operations

    while alt_inc > 0:
        # import pdb; pdb.set_trace() # start debug

        # find time taken to travel iter given grav_new
        time_inc = math.sqrt((2 * iter) / grav_new)
        time_inc = round(time_inc, 4)

        # add time increment to total
        time_total = time_total + time_inc

        # find new altitude
        alt_inc = alt_inc - iter

        # re-evaluate gravity at new altitude
        grav_new = calcGravity(alt_inc)

        vel_total += grav_new * time_inc
        inc_count += 1

    printOutput(alt, iter, time_total, vel_total)


main(sys.argv[1], sys.argv[2])

# py timeforacceleration.py .1 400
