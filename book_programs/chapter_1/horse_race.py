#!/usr/bin/python3

# Usage: python3 horse_race.py <n> <mute_output>
#   n:                      The number of horse races to simulate
#   mute_output(optional):  If the value is "mute" or "m" the results of individual experiments are not printed

# Example Usage: python3 horse_race.py 10

import random
import sys

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
    horse_race_count = int(args[1])

except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert n to an integer")

# Argument is negtive
if 'horse_race_count' in globals() and horse_race_count < 0:
    bad_input = True
    print("ERROR: n cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 horse_race.py <n> <mute_output>")
    print("  n is the number of horse races to simulate")
    print("  mute_output(optional) can be set to \"mute\" or \"m\" to hide the results of the experiments")
    print("\nExample Usage: python3 horse_race.py 10")
    sys.exit(1)

#######################
# Horse Race Simulation
#######################
mute_output = len(args) >= 3 and (args[2] == "m" or args[2] == "mute")
win_counters = {
    "Acorn":    0,
    "Balky":    0,
    "Chestnut": 0,
    "Dolby":    0
}

for i in range(horse_race_count):
    random_number = random.uniform(0, 1)
    if random_number < 0.3:
        if not mute_output:
            print("Acorn Wins")
        win_counters["Acorn"] += 1

    elif random_number < 0.7:
        if not mute_output:
            print("Balky Wins")
        win_counters["Balky"] += 1

    elif random_number < 0.9:
        if not mute_output:
            print("Chestnut Wins")
        win_counters["Chestnut"] += 1

    else:
        if not mute_output:
            print("Dolby Wins")
        win_counters["Dolby"] += 1

if not mute_output:
    print()


#######################
# Print Overall Results
#######################
print("Acorn won ", win_counters["Acorn"] / horse_race_count, "% of races")
print("Balky won ", win_counters["Balky"] / horse_race_count, "% of races")
print("Chestnut won ", win_counters["Chestnut"] / horse_race_count, "% of races")
print("Dolby won ", win_counters["Dolby"] / horse_race_count, "% of races")
