#!/usr/bin/python3

# Usage: python3 de_mere_2.py <m> <n> <mute_output>
# Param m:              The number of coins flipped in each experiment
# Param n:              The number of coin flip experiments to run
#                       If n is set to 1 the results of the experiment will be graphed
# Param mute_output:    If the value is "mute" or "m" the results of the experiments are not printed

# Example Usage: python3 h_t_simulation.py

import matplotlib.pyplot as pyplot
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
    coin_flip_count = int(args[1])
except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert param n to an integer")

try:
    random_coin_experiment_count = int(args[2])
except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert param m to an integer")

# Argument m is negtive
if 'random_coin_experiment_count' in globals() and random_coin_experiment_count < 0:
    bad_input = True
    print("ERROR: Param m cannot be negative")

# Argument n is negtive
if 'coin_flip_count' in globals() and coin_flip_count < 0:
    bad_input = True
    print("ERROR: Param n cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 h_t_simulation.py <m> <n> <mute_output>")
    print("  m is the number of times to flip a coin in each experiment")
    print("  n is the number of double coin flip experiments to run")
    print("  mute_output can be set to \"mute\" or \"m\" to hide the results of the experiments")
    sys.exit(1)

mute_output = len(args) >= 4 and (args[3] == "m" or args[3] == "mute")
