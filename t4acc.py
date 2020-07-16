import sys
import math
from decimal import Decimal

# global variables
# earth radius in meters (6.37 million)
r_earth = Decimal(6370000)
# speed of light in m/s
c_speed = Decimal(299792458)
# constant in meters per second, squared
grav_const = Decimal(9.80665)
# iteration count
iter_count = int(0)

def printOutputs(oStore):
    for i in oStore:
        print(i, "\n")

def dataInit(alt, iter):
    alt = Decimal(alt) * 1000
    alt_incr = alt
    grav_constant = Decimal(9.80665)
    grav_new = grav_constant
    time_total = Decimal(0)
    time_incr = time_total
    vel_total = Decimal(0)
    vel_incr = vel_total
    iter = int(iter)
    data = [alt, alt_incr, grav_constant, grav_new, time_total, time_incr, vel_total, vel_incr, iter]
        # 0 alt
        # 1 alt_incr
        # 2 grav_constant
        # 3 grav_new
        # 4 time_total
        # 5 time_incr
        # 6 vel_total
        # 7 vel_incr
        # 8 iterator
    return data

def calcGravity(gStore):
    gStore[3] = ((r_earth / (r_earth + dataStore[1])) ** 2)
    gStore[3] *= gStore[2]
    return gStore

def calcTime(tStore):
    # tStore[5] = -1 * (math.sqrt((2 * tStore[8] * tStore[3]) + (tStore[7] ** 2) + tStore[7]) / tStore[3])
    import pdb; pdb.set_trace()

    tStore[5] = tStore[8] * tStore[3]
    tStore[5] *= 2
    tStore[5] += (tStore[7] ** 2)
    tStore[5] = math.sqrt(tStore[5])
    tStore[5] += tStore[7]
    tStore[5] /= tStore[3]
    tStore[5] *= (-1)

    return tStore

def calcVelocity(vStore):
    vStore[7] = vStore[3] * vStore[5]
    return vStore

def main(altitude, iterator):

    dataStore = dataInit(altitude, iterator)

    while (dataStore[1] > 0):
        dataStore = calcTime(dataStore)
        dataStore = calcGravity(dataStore)
        dataStore = calcVelocity(dataStore)

        # decrement altitude
        dataStore[1] -= dataStore[8]
        # increment time
        dataStore[4] += dataStore[5]
        # increment velocity
        dataStore[6] += dataStore[7]
        # increment counter
        iter_count += 1

    printOutputs(dataStore)
    print(iter_count)
# /main

main(sys.argv[1], sys.argv[2])
