#!/usr/bin/python3

# Usage: python3 de_mere_2.py <m> <n> 
# Param m:       The number of <n> double dice roll experiments to simulate
# Param n:       The number of times to roll a pair of dice to see if a pair of sixes show up

# Example Usage: python3 de_mere_2.py 24 10

import random
import sys

args = sys.argv

# Error checking
bad_input = False

# Less than 2 arguments
if len(args) < 3:
    bad_input = True
    print("ERROR: Insufficient arguments")

# Try to convert arguments into integers
try:
    random_dice_experiment_count = int(args[1])
except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert param m to an integer")

try:
    dice_roll_count = int(args[2])
except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert param n to an integer")

# Argument m is negtive
if 'random_dice_experiment_count' in globals() and random_dice_experiment_count < 0:
    bad_input = True
    print("ERROR: Param m cannot be negative")

# Argument n is negtive
if 'dice_roll_count' in globals() and dice_roll_count < 0:
    bad_input = True
    print("ERROR: Param n cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 de_mere_1.py <m> <n>")
    print("  m is the number of <n> double dice roll experiments to simulate")
    print("  n is the number of times to roll a pair of dice to see if a pair of sixes show up")
    sys.exit(1)

successCount = 0

for i in range(random_dice_experiment_count):
    currentExperimentResults = []
    for i in range(dice_roll_count):
        currentExperimentResults.append((random.randint(1, 6), random.randint(1, 6)))
    print(currentExperimentResults)
    print()
    try:
        currentExperimentResults.index((6, 6))
        successCount += 1
    except ValueError:
        pass

print("Number of successes: ", successCount)
print("Proportion of successes: ", successCount/random_dice_experiment_count)
