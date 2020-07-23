import math

veelo = float(0)
gravoo = 9.8
timeTot = 10
timeInc = .01

i = 0
while i != timeTot:
    veelo += gravoo * timeInc
    i += timeInc
    if i > timeTot:
        break

print("Averaged velocity: ", gravoo * timeTot)
print("Summed velocity: ", veelo)

# test to see if velocity can be summed over time as well as averaged
# essentially bruteforcing an integral
