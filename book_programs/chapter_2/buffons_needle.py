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

def make_needle():
    needle = {}

    length = 0.5
    center_x = random.uniform(0, 1)
    center_y = random.uniform(0, 1)
    theta = random.uniform(0, math.pi)
    delta_x = length / 2 * math.cos(theta)
    delta_y = length / 2 * math.sin(theta)

    needle["theta"] = theta
    needle["end_points"] = []
    needle["end_points"].append({
        "x": center_x - delta_x,
        "y": center_y - delta_y,
    })
    needle["end_points"].append({
        "x": center_x + delta_x,
        "y": center_y + delta_y,
    })

    return needle

def is_needle_intersecting_with_y(needle, y):
    first_end_point = needle["end_points"][0]
    second_end_point = needle["end_points"][1]

    return first_end_point["y"] < y and second_end_point["y"] > y

class BuffonSimulation:
    def __init__(self):
        self.floor = []
        self.boards = 2
        self.list_of_needles = []
        self.number_of_intersections = 0

        fig = pyplot.figure(figsize=(10, 10))
        self.buffon = pyplot.subplot()
        self.results_text = fig.text(0, 0, self.estimate_pi(), size=15)
        self.buffon.set_xlim(-0.1, 1.1)
        self.buffon.set_ylim(-0.1, 1.1)

    def plot_floor_boards(self):
        for j in range(self.boards):
            self.floor.append(0+j)
            self.buffon.hlines(y=self.floor[j], xmin=0, xmax=1, color='black', linestyle='--', linewidth=2.0)

    def toss_needles(self):
        needle = make_needle()
        self.list_of_needles.append(needle)

        first_end_point = needle["end_points"][0]
        second_end_point = needle["end_points"][1]

        x_coordinates = [
            first_end_point["x"],
            second_end_point["x"]
        ]

        y_coordinates = [
            first_end_point["y"],
            second_end_point["y"]
        ]

        for board in range(self.boards):
            if is_needle_intersecting_with_y(needle, self.floor[board]):
                self.number_of_intersections += 1
                self.buffon.plot(x_coordinates, y_coordinates, color='green', linewidth=1)
                return
        self.buffon.plot(x_coordinates, y_coordinates, color='red', linewidth=1)

    def estimate_pi(self, needles_tossed=0):
        if self.number_of_intersections == 0:
            estimated_pi = 0
        else:
            estimated_pi = (needles_tossed) / \
                (1 * self.number_of_intersections)
        error = abs(((math.pi - estimated_pi)/math.pi)*100)
        return (" Intersections:" + str(self.number_of_intersections) +
                "\n Total Needles: " + str(needles_tossed) +
                "\n Approximation of Pi: " + str(estimated_pi) +
                "\n Error: " + str(error) + "%")

####################
# Plotting Results #
####################

    def plot_needles(self):
        for needle in range(n):
            self.toss_needles()
            self.results_text.set_text(self.estimate_pi(needle+1))
            if (needle+1) % 200 == 0:
                pyplot.pause(1/200)
        pyplot.title("The simulated estimate for Pi is ")

    def plot(self):
        self.plot_floor_boards()
        self.plot_needles()
        pyplot.show()

simulation = BuffonSimulation()
simulation.plot()
