def main():
    x_values = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000, 80000]
    # altitude in meters
    y_values = [1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5900, 0.5258, 0.4671, 0.4135, 0.1948, 0.08891, 0.04008, 0.01841, 0.003996, 0.001027, 0.0003097, 0.00008283, 0.00001846]
    # density in kg/m^3
    template = "{0}, {1}"
    combined = "[" # initialize string to-be-concatenated-onto

    # import pdb; pdb.set_trace()

    # iterate over x
    # for each x, concatenate (X, Y;)
    for i in range(0, len(x_values)):
        combined += template.format(x_values[i], y_values[i])
        if i == (len(x_values)-1):
            break
        combined += "; "
    combined += "]"
    print(combined)
main()
