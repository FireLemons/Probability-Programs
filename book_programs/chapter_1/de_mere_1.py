#!/usr/bin/python3

# Example Usage: python3 de_mere_1.py <n> 
# Param n:       The number of four dice roll experiments to simulate

import random
import sys

args = sys.argv

# Error checking
bad_input = False

# No arguments
if len(args) < 2:
    bad_input = True
    print("ERROR: Insufficient arguments")

# Try to convert argument into an integer
try:
    random_dice_experiment_count = int(args[1])

except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert param n to an integer")

# Argument is negtive
if 'random_dice_experiment_count' in globals() and random_dice_experiment_count < 0:
    bad_input = True
    print("ERROR: Param n cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 de_mere_1.py <n>\n  n is the number of four dice roll experiments to simulate")
    sys.exit(1)

successCount = 0

for i in range(random_dice_experiment_count):
    currentExperimentResults = []
    for i in range(4):
        currentExperimentResults.append(random.randint(1, 6))
    print(currentExperimentResults)
    try:
        currentExperimentResults.index(6)
        successCount += 1
    except ValueError:
        pass

print("Number of successes: ", successCount)
print("Proportion of successes: ", successCount/random_dice_experiment_count)
