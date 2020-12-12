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
list_of_needles = []
intersecting_needle_count = 0

number_of_lines = 2
lines = range(number_of_lines)

experiment_error_percentage = 0

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

    # Test each line for needle instersection
    for line_y in lines:
        lesser_y = min(needle[0]["y"], needle[1]["y"])
        greater_y = max(needle[0]["y"], needle[1]["y"])
        # If the needle is intersecting with a line
        if lesser_y <= line_y and line_y <= greater_y:
            intersecting_needle_count += 1

if n > 0: # Check in case of divide by zero error when n is set to 0
    pi_estimated_value = n / intersecting_needle_count
else:
    pi_estimated_value = 0

experiment_error_percentage = abs(((math.pi - pi_estimated_value) / math.pi) * 100)

print(f"The simulated estimate for pi is: {pi_estimated_value} with error: {experiment_error_percentage}%")
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

    # Color intersecting needles green and non intersecting needles red
    needle_color = "red"

    # Test each line for needle instersection
    for line_y in lines:
        lesser_y = min(needle[0]["y"], needle[1]["y"])
        greater_y = max(needle[0]["y"], needle[1]["y"])
        # If the needle is intersecting with a line
        if lesser_y <= line_y and line_y <= greater_y:
            needle_color = "green"

    buffon.plot(x_coordinates, y_coordinates, color=needle_color, linewidth=1)

    if i % 200 == 0:
        pyplot.pause(1 / 200)

pyplot.title("The simulated estimate for Pi is ")
results_text.set_text(f"Intersections: {intersecting_needle_count}\n Total Needles: {n}\n Approximation of Pi: {pi_estimated_value}\n Error:{experiment_error_percentage}%")
pyplot.show()
