import math

# define globals
mass = 361779338 # in kilograms
cross_area = 86987.4 # in meters^2
# drag_coeff = 1.42 # semispehere opposite flow
drag_coeff = 2.1 # rectangular box
gravity_constant = float(9.80665)


term_vel = 0
density_value = 0

altitude_density = [[80000, 1.846e-05], [70000, 8.283e-05], [60000, 0.0003097], [50000, 0.001027], [40000, 0.003996], [30000, 0.01841], [25000, 0.04008], [20000, 0.08891], [15000, 0.1948], [10000, 0.4135], [9000, 0.4671], [8000, 0.5258], [7000, 0.59], [6000, 0.6601], [5000, 0.7364], [4000, 0.8194], [3000, 0.9093], [2000, 1.007], [1000, 1.112], [0, 1.225]]
# in meters and kg/m^3

def FindTerminal(gravity, density):
    # import pdb; pdb.set_trace()
    terminal_velocity = math.sqrt((2 * mass * gravity_constant)/(density * cross_area * drag_coeff))
    return terminal_velocity

def FindDensity(alt_input, grav_input):
    density_value = altitude_density[len(altitude_density) - 1][1]
    for r in range(0, len(altitude_density) - 1):
        if alt_input < altitude_density[r][0] and alt_input >= altitude_density[r+1][0]:
            density_value = altitude_density[r+1][1]
            break
        elif alt_input > altitude_density[0][0]: # aka if altitude is too damn high
            density_value = altitude_density[0][1] # set it to lowest possible value
            break

    # import pdb; pdb.set_trace()

    term_vel = FindTerminal(grav_input, density_value)
    return term_vel

# main(500)
# main(1000)
# main(1500)
# main(40000)
# main(81000)
# test cases
