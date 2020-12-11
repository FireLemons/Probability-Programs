# Usage: python3 buffons_needle.py <n> 
#   n:   The Number of Needles used

# Example Usage: python3 buffons_needle.py 5000

import matplotlib.pyplot as pyplot
import random
import math
import sys

args = sys.argv

#######################
# User Input Handling #
#######################
bad_input = False

# Less than 1 argument
if len(args) < 2:
    bad_input = True
    print("ERROR: Insufficient arguments")

# Convert args into integers
try:
    n = int(args[1])
except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert n to an integer")

# Arg is negative
if 'n' in globals() and n < 0:
    bad_input = True
    print("ERROR: argument cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 buffons_needle.py <n>")
    print("  n:   The Number of Needles used\n")
    print("Example Usage: python3 buffons_needle.py 5000")
    sys.exit(1)

##################
# Buffons Needle #
##################
lines = []
list_of_needles = []
number_of_lines = 2
number_of_intersections = 0

# Create needles as a list containing 2 dictionarys each representing an endpoint of the needle
for i in range(n):
    needle = []

    length = 0.5
    center_x = random.uniform(0, 1)
    center_y = random.uniform(0, 1)
    theta = random.uniform(0, math.pi)
    delta_x = length / 2 * math.cos(theta)
    delta_y = length / 2 * math.sin(theta)

    needle.append({
        "x": center_x - delta_x,
        "y": center_y - delta_y,
    })
    needle.append({
        "x": center_x + delta_x,
        "y": center_y + delta_y,
    })

    list_of_needles.append(needle)

####################
# Plotting Results #
####################
fig = pyplot.figure(figsize=(10, 10))
buffon = pyplot.subplot()
buffon.set_xlim(-0.1, 1.1)
buffon.set_ylim(-0.1, 1.1)

results_text = fig.text(0, 0, "Intersections: 0\n Total Needles: 0\n Approximation of Pi: 0\n Error: 100%", size=15)

# Plot lines
for j in range(number_of_lines):
    lines.append(j)
    buffon.hlines(y=lines[j], xmin=0, xmax=1, color='black', linestyle='--', linewidth=2.0)

# Plot needles
for i in range(1, n + 1):
    needle = list_of_needles[i - 1]
    first_end_point = needle[0]
    second_end_point = needle[1]

    x_coordinates = [
        first_end_point["x"],
        second_end_point["x"]
    ]

    y_coordinates = [
        first_end_point["y"],
        second_end_point["y"]
    ]

    # If the needle is intersecting with a line
    if any(first_end_point["y"] < line_y and second_end_point["y"] > line_y for line_y in lines):
        number_of_intersections += 1
        buffon.plot(x_coordinates, y_coordinates, color='green', linewidth=1)
    else:
        buffon.plot(x_coordinates, y_coordinates, color='red', linewidth=1)

    needles_tossed = i
    estimated_pi = needles_tossed / number_of_intersections if number_of_intersections > 0 else 0

    error = abs(((math.pi - estimated_pi) / math.pi) * 100)

    results_text.set_text(f"Intersections: {number_of_intersections}\n Total Needles: {needles_tossed}\n Approximation of Pi: {estimated_pi}\n Error:{error}%")

    if i % 200 == 0:
        pyplot.pause(1 / 200)

pyplot.title("The simulated estimate for Pi is ")
pyplot.show()
