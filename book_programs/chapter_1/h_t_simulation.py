#!/usr/bin/python3

# Usage: python3 de_mere_2.py <m> <n> <mute_output>
# Param m:              The number of coin flips in each experiment
# Param n:              The number of coin flip experiments to run
#                       If n is set to 1 the results of the experiment will be graphed unless the output is muted
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

# Argument n is negtive
if 'random_coin_experiment_count' in globals() and random_coin_experiment_count < 0:
    bad_input = True
    print("ERROR: Param n cannot be negative")

# Argument m is negtive
if 'coin_flip_count' in globals() and coin_flip_count < 0:
    bad_input = True
    print("ERROR: Param m cannot be negative")

# Print usage help when arguments are bad
if bad_input:
#                       If n is set to 1 the results of the experiment will be graphed unless the output is muted
# Param mute_output:    If the value is "mute" or "m" the results of the experiments are not printed
    print("\nUsage: python3 h_t_simulation.py <m> <n> <mute_output>")
    print("  m is the number of coin flips in each experiment")
    print("  n is the number of coin flip experiments to run")
    print("    If n is set to 1 the results of the experiment will be graphed unless the output is muted")
    print("  mute_output can be set to \"mute\" or \"m\" to hide the results of the experiments")
    sys.exit(1)

# Coin flip simulation
mute_output = len(args) >= 4 and (args[3] == "m" or args[3] == "mute")
times_in_lead_list = []
toss_list = []
winnings_list = []

for i in range(random_coin_experiment_count):
    current_winnings = 0
    previous_winnings = 0
    lead = 0

    for j in range(coin_flip_count):
        if random.uniform(0, 1) < .5:
            current_winnings += 1
        else:
            current_winnings -= 1

        if random_coin_experiment_count == 1 and not mute_output:
            toss_list.append(current_winnings)

pyplot.plot(range(len(toss_list)), toss_list)
pyplot.ylabel("winnings")
pyplot.xlabel("coin flips")
pyplot.show()
