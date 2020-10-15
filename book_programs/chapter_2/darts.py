# Usage: python3 darts.py <n> <mute_output>
#   n:                      The number of dart throwns to be simulated
#   mute_output(optional):  If the value is "mute" or "m" the distances of the individual darts and the graph of the results is not shown.

# Example Usage: python3 darts.py 5

import random
import sys
import math
import matplotlib.pyplot as pyplot

args = sys.argv

#####################
# User Input Handling
#####################
bad_input = False

# No arguments
if len(args) < 2:
    bad_input = True
    print("ERROR: Insufficient arguments")

# Try to convert argument into an integer
try:
    dart_throws_count = int(args[1])

except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert n to an integer")

# Argument is negtive
if 'dart_throws' in globals() and dart_throws < 0:
    bad_input = True
    print("ERROR: n cannot be negative")


# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 darts.py <n> <mute_output>")
    print("  n is the number of dart throws to simulate")
    print("  mute_output(optional) can be set to \"mute\" or \"m\" to hide the results of indivdual experiments")
    print("\nExample Usage: python3 darts.py 10")
    sys.exit(1)

###################
# Darts Simulation #
###################
mute_output = len(args) >= 3 and (args[2] == "m" or args[2] == "mute")
dart_distances = []

if not mute_output:
    print("Distances of the darts: ")

for i in range(dart_throws_count):
    current_distance = math.sqrt(random.uniform(0, 1)**2 + random.uniform(0, 1)**2)
    while current_distance > 1:
        current_distance = math.sqrt(random.uniform(0, 1)**2 + random.uniform(0, 1)**2)
    if not mute_output:
        print(round(current_distance, 3))
    dart_distances.append(current_distance)

##################
# Graphing Results
##################

pyplot.suptitle("1.1 Distribution of Darts by ranges")
pyplot.xlabel("Distance from the center")
pyplot.ylabel("Share of darts in this range")
pyplot.xlim(0, 1)

for i in range(10):
    current_range_count = 0
    if dart_throws_count > 0:
        current_range_count = sum(i/10 <= distance < (i+1)/10 for distance in dart_distances)/dart_throws_count
    pyplot.bar((i+0.5)/10, current_range_count, width=0.08)

pyplot.show()
