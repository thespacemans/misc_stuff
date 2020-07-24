import sys # handle arguments from coommand line
from math import pow, sqrt # exponentials and square roots
from os import system, name # attributes to update commandline display live

# initialize globals
# earth radius in meters (6.37 million)
radius_earth = float(6370000)
# speed of light in m/s
lunar_dist = float(384402000) # average distance to moon
# constant in meters per second, squared
gravity_const = float(9.80665)

# terminal velocity globals
mass = 361779338 # in kilograms
cross_area = 86987.4 # in meters^2
drag_coeff = 1.42 # semisphere opposite flow -- 2097s for 4000m at .5g
# drag_coeff = 2.1 # rectangular box -- this gives me 2117s for 4000km at .5g
# drag_coeff = 10 # what the fuck -- this gives me a time of 2200s for 4000km at .5g
# oddly, this isn't a huge factor

altitude_density = [[80000, 1.846e-05], [70000, 8.283e-05], [60000, 0.0003097], [50000, 0.001027], [40000, 0.003996], [30000, 0.01841], [25000, 0.04008], [20000, 0.08891], [15000, 0.1948], [10000, 0.4135], [9000, 0.4671], [8000, 0.5258], [7000, 0.59], [6000, 0.6601], [5000, 0.7364], [4000, 0.8194], [3000, 0.9093], [2000, 1.007], [1000, 1.112], [0, 1.225]]

# ------------------------------------------------------------------------------

# function to clear the output screen for visualization
def clear():
    # if windows, use cls
    if name == 'nt':
        _ = system('cls')
    # if mac or linux, use clear
    else:
        _ = system('clear')

# print data in nice formatting
def PrintOut(altitude, iterator, time, velocity, loops):
    print("\n", "      Altitude: ", altitude, " m", "\n", "Lunar Distance: ", lunar_dist, " m", "\n", "--------------| ", round((altitude/lunar_dist) * 100, 2), "% of lunar distance", "\n", "      Iterator: ", iterator, " m", "\n", "  Time elapsed: ", round(time, 8), " seconds", "\n", "--------------| ", round((time / 3600.0), 3), " hours", "\n", "Final velocity: ", round(velocity, 8), " m/s", "\n", "    Loop count: ", loops)

# calculate gravity at new altitude
def CalculateGravity(altitude):
    gravity = gravity_const * pow((radius_earth / (radius_earth + altitude)), 2)
    return gravity
    # gnew = g(re/re+h)^2

# calculate velocity at new altitude
def CalculateVelocity(time, gravity):
    # import pdb; pdb.set_trace()
    velocity = gravity * time
    return velocity
    # vi = gt

# calculate time taken to travel (iterator) given velocity
def CalculateTime(i, g, v):
    time = (((-v)+sqrt((2*i*g) + pow(v, 2)))/g)
    return time
    # t = frac(-v+sqrt(2dg + v^2), g)
    # t = -frac(v+sqrt(2dg + v^2), g)
    # could be both

# find atmospheric density for given altitude
def FindDensity(alt_input):
    density_value = altitude_density[len(altitude_density) - 1][1] # lowest value
    for r in range(0, len(altitude_density) - 1):
        if alt_input < altitude_density[r][0] and alt_input >= altitude_density[r+1][0]:
            density_value = altitude_density[r+1][1]
            break
        elif alt_input > altitude_density[0][0]: # aka if altitude is too damn high
            density_value = altitude_density[0][1] # set it to lowest possible value
            break
    return density_value

# calculate terminal velocity for given density and gravity
def FindTerminal(gravity, density):
    terminal_velocity = sqrt((2 * mass * gravity)/(density * cross_area * drag_coeff))
    return terminal_velocity
# -------------------------------------------------------------------

def main(altitude, iterator):
    # initialize user input here
    iterator = float(iterator) # cast str input to float
    altitude = float(altitude) * 1000.0 # ensure this immutable input is correct
    alt_counter = altitude # altitude converted to meters
    gravity_new = CalculateGravity(alt_counter) # find gravity at current alt
    time_counter = float(0.0) # start at zero time
    time_total = time_counter # summation starts at zero
    velocity_counter = float(0) # initial velocity is zero
    terminal_velocity = 0 # terminal velocity in m/s
    density_value = 0 # initialize at 0
    # initialize this now to avoid name error later

    # counter for my own sanity
    loop_count = int(0)

    while (alt_counter > 0):

        time_counter = CalculateTime(iterator, gravity_new, velocity_counter)
        time_total += time_counter

        density_value = FindDensity(alt_counter)

        alt_counter -= iterator

        velocity_counter += CalculateVelocity(time_counter, gravity_new)
        # find terminal, give bespoke gravity value each iteration
        terminal_velocity = FindTerminal(CalculateGravity(alt_counter), density_value)
        # define terminal velocity here
        if velocity_counter > terminal_velocity: # if velocity would exceed terminal
            velocity_counter = terminal_velocity
            # who said they have to accelerate at all?
            # why not just Not Accelerate? Cap the velocity?
            # or accelerate on an extremely small scale
            # they might end up going slow but who cares
            # to fall 500km in 12 hours, you would need to travel
            # 500,000m in 43,200s or about 11.5 m/s
        velocity_counter = 11 # m/s, or 24.6 mph
        # this should allow for a ~12hr fall from 500km

        gravity_new = CalculateGravity(alt_counter)



        loop_count += 1


        if iterator == 0.1:
            modulo = 10000
        elif iterator == 0.01:
            modulo = 100000
        elif iterator == 0.001:
            modulo = 10000000
        else:
            modulo = 5000

        if (loop_count % modulo == 0):
            clear()
            print("Velocity: ", velocity_counter)
            print("Terminal: ", terminal_velocity)
            print("Gravity:  ", gravity_new)
            print("Altitude: ", alt_counter)
            print("Time:     ", time_total, "\n")

    # import pdb; pdb.set_trace()
    PrintOut(altitude, iterator, time_total, velocity_counter, loop_count)

main(sys.argv[1], sys.argv[2])
