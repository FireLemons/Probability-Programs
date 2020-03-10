#!/usr/bin/python3

# Usage: python3 coin_tosses.py <n> <mute_output>
#   n:                      The number of coin tosses to simulate
#   mute_output(optional):  If the value is "mute" or "m" the results of the experiments are not printed

# Example Usage: python3 coin_tosses.py 10

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
    random_coin_toss_count = int(args[1])

except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert n to an integer")

# Argument is negtive
if 'random_coin_toss_count' in globals() and random_coin_toss_count < 0:
    bad_input = True
    print("ERROR: n cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 coin_tosses.py <n> <mute_output>")
    print("  n is the number of coin tosses to simulate")
    print("  mute_output(optional) can be set to \"mute\" or \"m\" to hide the results of the experiments")
    print("\nExample Usage: python3 coin_tosses.py 10")
    sys.exit(1)

######################
# Coin Flip Simulation
######################
headsCount = 0
results = ""

for i in range(random_coin_toss_count):
    if random.uniform(0, 1) < 0.5:
        headsCount += 1
        results += "H"
    else:
        results += "T"

##########################
# Print Experiment Results
##########################
if not(len(args) >= 3 and (args[2] == "m" or args[2] == "mute")):
    print(results)
    print()

print("The proportion in n tosses is ", random_coin_toss_count, " is ", headsCount / random_coin_toss_count)
