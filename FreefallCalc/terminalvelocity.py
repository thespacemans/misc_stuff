import sys
import math

# define globals
mass = 361779338 # in kilograms
cross_area = 86987.4 # in meters^2
drag_coeff = 1.42 # of hemisphere opposite flow

# earth radius in meters (6.37 million)
radius_earth = float(6370000)
# constant in meters per second, squared
gravity_const = float(9.80665)

altitude_density = [[0, 1.225], [1000, 1.112], [2000, 1.007], [3000, 0.9093], [4000, 0.8194], [5000, 0.7364], [6000, 0.6601], [7000, 0.59], [8000, 0.5258], [9000, 0.4671], [10000, 0.4135], [15000, 0.1948], [20000, 0.08891], [25000, 0.04008], [30000, 0.01841], [40000, 0.003996], [50000, 0.001027], [60000, 0.0003097], [70000, .00008283], [80000, .00001846]]
# in meters and kg/m^3

def FindTerminal(gravity, density):
    terminal_velocity = math.sqrt((2 * mass * gravity)/(density * cross_area * drag_coeff))
    return terminal_velocity

def CalcGravityStuff(altitude):
    gravity = gravity_const * math.pow((radius_earth / (radius_earth + altitude)), 2)
    return gravity

def main():
    term_vel = 0
    # import pdb; pdb.set_trace()
    altitude_density.reverse()
    for r in range(0, len(altitude_density) - 1):
        print(term_vel)
        # print(altitude_density[r][0])
        # print(altitude_density[r][1], "\n")
        gravity_new = CalcGravityStuff(altitude_density[r][0])
        term_vel += FindTerminal(gravity_new, altitude_density[r][1])

    print(round(term_vel / 20, 2), "m/s average")
    print("Don't do an average, instead output a different speed for each altitude range!")

main()
# use the array, use a for loop to iterate on each altitude
