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

floor = []
boards = 2
list_of_needles = []
number_of_intersections = 0

# Creates a "needle" represented by a list of 2 endpoints
#   returns A list containing 2 dictionarys; each representing the coordinates of an endpoint
def make_needle():
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

    return needle

def is_needle_intersecting_with_y(needle, y):
    first_end_point = needle[0]
    second_end_point = needle[1]

    return first_end_point["y"] < y and second_end_point["y"] > y

def estimate_pi(needles_tossed):
    global number_of_intersections
    if number_of_intersections == 0:
        estimated_pi = 0
    else:
        estimated_pi = needles_tossed / number_of_intersections

    error = abs(((math.pi - estimated_pi) / math.pi) * 100)
    return (f"Intersections: {number_of_intersections}\n Total Needles: {needles_tossed}\n Approximation of Pi: {estimated_pi}\n Error:{error}%")

fig = pyplot.figure(figsize=(10, 10))
buffon = pyplot.subplot()
buffon.set_xlim(-0.1, 1.1)
buffon.set_ylim(-0.1, 1.1)

# Don't show incomplete graphs
#pyplot.close()
results_text = fig.text(0, 0, estimate_pi(0), size=15)

def plot_floor_boards():
    for j in range(boards):
        floor.append(0 + j)
        buffon.hlines(y=floor[j], xmin=0, xmax=1, color='black', linestyle='--', linewidth=2.0)

def toss_needles():
    global number_of_intersections
    needle = make_needle()
    list_of_needles.append(needle)

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

    for board in range(boards):
        if is_needle_intersecting_with_y(needle, floor[board]):
            number_of_intersections += 1
            buffon.plot(x_coordinates, y_coordinates, color='green', linewidth=1)
            return
    buffon.plot(x_coordinates, y_coordinates, color='red', linewidth=1)

def plot_needles():
    for needle in range(n):
        toss_needles()
        results_text.set_text(estimate_pi(needle + 1))
        if (needle + 1) % 200 == 0:
            pyplot.pause(1 / 200)
    pyplot.title("The simulated estimate for Pi is ")

def plot():
    plot_floor_boards()
    plot_needles()
    pyplot.show()

plot()
