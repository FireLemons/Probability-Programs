# Usage: python3 monte_carlo.py <n> <xmin> <xmax> <ymax>
#   n:      number of random numbers
#   xmin:   start of interval in which random numbers are generated
#   xmax:   end of interval in which random numbers are generated
#   ymax:   largest y value to be considered
#
#   f:      function to be inspected - defined in the python file
#
# Example Usage: python3 monte_carlo.py 100 0 1 1

import random
import sys
import matplotlib.pyplot as pyplot
import numpy as np

import math


args = sys.argv


#####################
# User Input
#####################

def inspected_function(x):
    return math.cos(x)


#####################
# User Input Handling
#####################


bad_input = False

# No arguments
if len(args) < 5:
    bad_input = True
    print("ERROR: Insufficient arguments")

# Check if the function is defined
try:
    x_min = float(args[2])
    x_max = float(args[3])
    y_max = float(args[4])
    inspected_function(x_min)
except:
    bad_input = True
    print("ERROR: f is not a valid function - could not solve for xmin")

# Check if x_max is larger than x_min
if 'x_min' in globals() and 'x_max' in globals() and x_min > x_max:
    bad_input = True
    print("ERROR: xmin is larger than xmax")

# Check if y_max is smaller or equal than 0
if 'y_max' in globals() and y_max <= 0:
    bad_input = True
    print("ERROR: ymin is no larger than 0")

# Try to convert argument into an integer
try:
    random_numbers_count = int(args[1])
except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert n to an integer")

# Argument is negtive
if 'random_numbers_count' in globals() and random_numbers_count < 0:
    bad_input = True
    print("ERROR: n cannot be negative")


# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 monte_carlo.py <n> <f> <xmin> <xmax> <ymax>")
    print("  n:      number of random numbers")
    print("  xmin:   start of interval in which random numbers are generated")
    print("  xmax:   end of interval in which random numbers are generated")
    print("  ymax:   largest y value to be considered")
    print("  f:      function to be inspected - defined in the python file")
    print("\nExample Usage: python3 monte_carlo.py 100 0 1 1")

    sys.exit(1)

###################
# Name of Program #
###################

points = []
points_under_function_count = 0

for i in range(random_numbers_count):
    point = {'x': random.uniform(x_min, x_max), 'y': random.uniform(0, y_max)}
    if point['y'] <= inspected_function(point['x']):
        points_under_function_count += 1
    points.append(point)

area_estimate = (points_under_function_count / random_numbers_count) * y_max * (x_max - x_min)

##################
# Graphing Results
##################

print("Area Estimate: ", round(area_estimate, 3))

random_xs = [point['x'] for point in points]
random_ys = [point['y'] for point in points]

increment = (x_max - x_min) / 20
function_xs = np.arange(x_min, x_max + increment, increment)
function_ys = [inspected_function(x) for x in function_xs]


pyplot.suptitle("1.1 Function and generated Points")
pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.xlim(x_min, x_max)
pyplot.ylim(0, y_max)

pyplot.plot(random_xs, random_ys, 'o')
pyplot.plot(function_xs, function_ys)

pyplot.show()
