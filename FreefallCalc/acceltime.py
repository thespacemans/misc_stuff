import sys
import math
from os import system, name

# initialize globals
# earth radius in meters (6.37 million)
radius_earth = float(6370000)
# speed of light in m/s
lightspeed = float(299792458)
# constant in meters per second, squared
gravity_const = float(9.80665)

# function to clear the output screen for visualization
def clear():
    # if windows, use cls
    if name == 'nt':
        _ = system('cls')
    # if mac or linux, use clear
    else:
        _ = system('clear')

# print func here
def PrintOut(altitude, iterator, time, velocity, loops):
    print("")
    print("      Altitude: ", altitude, " m")
    print("      Iterator: ", iterator, " m")
    print("  Time elapsed: ", round(time, 8), " seconds")
    print("--------------| ", round((time / 3600.0), 3), " hours")
    print("Final velocity: ", round(velocity, 8), " m/s")
    print("--------------| ", round(100 * (velocity / lightspeed), 2), "% of c")
    print("    Loop count: ", loops)

# calculate gravity at new altitude
def CalculateGravity(altitude):
    gravity = gravity_const * math.pow((radius_earth / (radius_earth + altitude)), 2)
    gravity *= 0.5 # fraction of total gravity
    return gravity
    # gnew = g(re/re+h)^2

# calculate velocity at new altitude
def CalculateVelocity(time, gravity):
    # import pdb; pdb.set_trace()
    velocity = gravity * time

    # define terminal velocity here
    # FUTURE: find terminal velocity as a function of atmospheric density
    # if (velocity > 56):
    #     return 56

    return velocity
    # vi = gt

# calculate time taken to travel (iterator) given velocity
def CalculateTime(i, g, v):
    time = (((-v)+math.sqrt((2*i*g) + math.pow(v, 2)))/g)
    return time
    # t = frac(-v+sqrt(2dg + v^2), g)
    # t = -frac(v+sqrt(2dg + v^2), g)
    # could be both

# -------------------------------------------------------------------

def main(altitude, iterator):
    # initialize user input here
    iterator = float(iterator) # cast str input to float
    altitude = float(altitude) * 1000.0 # ensure this immutable input is correct
    alt_counter = altitude # altitude converted to meters
    gravity_new = CalculateGravity(alt_counter)
    time_counter = float(0.0) # start at zero time
    time_total = time_counter # summation starts at zero
    velocity_counter = float(0) # initial velocity is zero

    # counter for my own sanity
    loop_count = int(0)

    while (alt_counter > 0):
        pass
        time_counter = CalculateTime(iterator, gravity_new, velocity_counter)
        time_total += time_counter

        alt_counter -= iterator

        velocity_counter = CalculateVelocity(time_total, gravity_new)

        gravity_new = CalculateGravity(alt_counter)

        loop_count += 1

        if (loop_count % 1000 == 0):
            clear()
            print("Velocity: ", velocity_counter)
            print("Gravity:  ", gravity_new)
            print("Altitude: ", alt_counter)
            print("Time:     ", time_total)

    # import pdb; pdb.set_trace()
    PrintOut(altitude, iterator, time_total, velocity_counter, loop_count)

main(sys.argv[1], sys.argv[2])
