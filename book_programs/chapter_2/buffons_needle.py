# Usage: python3 buffons_needle.py <n> 
#   n:   The Number of Needles used

# Example Usage: python3 buffons_needle.py 5000

import matplotlib.pyplot as pyplot
import random
import math
import numpy as np
import sys

args = sys.argv

#####################
# User Input Handling
#####################
bad_input = False

# Less than 1 argument
if len(args) < 1:
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
    print("  n:   The Number of Needles used")
    sys.exit(1)

###################
# Buffons Needle  #
###################
class DefineNeedle:
    def __init__(self, x=None, y=None, theta=None, length=0.5):
        if x is None:
            x = random.uniform(0, 1)
        if y is None:
            y = random.uniform(0, 1)
        if theta is None:
            theta = random.uniform(0, math.pi)

        self.needle_coordinates = np.array([x, y])
        self.complex_representation = np.array(
            [length/2 * math.cos(theta), length/2*math.sin(theta)])
        self.end_points = np.array([np.add(self.needle_coordinates, -1*np.array(
            self.complex_representation)), np.add(self.needle_coordinates, self.complex_representation)])

    def intersects_with_y(self, y):
        return self.end_points[0][1] < y and self.end_points[1][1] > y


class BuffonSimulation:
    def __init__(self):
        self.floor = []
        self.boards = 2
        self.list_of_needle_objects = []
        self.number_of_intersections = 0

        fig = pyplot.figure(figsize=(10, 10))
        self.buffon = pyplot.subplot()
        self.results_text = fig.text(
            0, 0, self.estimate_pi(), size=15)
        self.buffon.set_xlim(-0.1, 1.1)
        self.buffon.set_ylim(-0.1, 1.1)

    def plot_floor_boards(self):
        for j in range(self.boards):
            self.floor.append(0+j)
            self.buffon.hlines(
                y=self.floor[j], xmin=0, xmax=1, color='black', linestyle='--', linewidth=2.0)

    def toss_needles(self):
        needle_object = DefineNeedle()
        self.list_of_needle_objects.append(needle_object)
        x_coordinates = [needle_object.end_points[0]
                         [0], needle_object.end_points[1][0]]
        y_coordinates = [needle_object.end_points[0]
                         [1], needle_object.end_points[1][1]]

        for board in range(self.boards):
            if needle_object.intersects_with_y(self.floor[board]):
                self.number_of_intersections += 1
                self.buffon.plot(x_coordinates, y_coordinates,
                                 color='green', linewidth=1)
                return
        self.buffon.plot(x_coordinates, y_coordinates,
                         color='red', linewidth=1)

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

##################
# Plotting Results
##################

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
