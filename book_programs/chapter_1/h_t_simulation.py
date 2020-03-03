#!/usr/bin/python3

# Usage: python3 de_mere_2.py <m> <n> <mute_output>
#   m:              The number of coin flips in each experiment
#   n:              The number of coin flip experiments to run
#                       If n is set to 1 the winnings will be plotted
#                       If n is greater than 1 the distributions of overall winnings and times in the lead will be plotted
#   mute_output:    If the value is "mute" or "m" the results of the experiments will not be plotted

# Example Usage: python3 h_t_simulation.py

import matplotlib.pyplot as pyplot
import random
import sys

args = sys.argv

################
# Error checking
################
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
    print("ERROR: Could not convert n to an integer")

try:
    random_coin_experiment_count = int(args[2])
except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert m to an integer")

# Argument n is negtive
if 'random_coin_experiment_count' in globals() and random_coin_experiment_count < 0:
    bad_input = True
    print("ERROR: n cannot be negative")

# Argument m is negtive
if 'coin_flip_count' in globals() and coin_flip_count < 0:
    bad_input = True
    print("ERROR: m cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 h_t_simulation.py <m> <n> <mute_output>")
    print("  m is the number of coin flips in each experiment")
    print("  n is the number of coin flip experiments to run")
    print("    If n is set to 1 the winnings will be plotted")
    print("    If n is greater than 1 the distributions of overall winnings and times in the lead will be plotted")
    print("  mute_output:    If the value is \"mute\" or \"m\" the results of the experiments will not be plotted")
    sys.exit(1)

######################
# Coin flip simulation
######################
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

        if current_winnings > 0 or (current_winnings == 0 and previous_winnings > 0 ):
            lead += 1

        previous_winnings = current_winnings
    times_in_lead_list.append(lead)

##################
# Plotting Results
##################

# Functions to reformat data for plotting
 
def number_list_to_frequency_list(recurring_number_list):
    """
    Converts a list of numbers into a frequency representation

        Args:
            recurring_number_list (list): A list of numbers

        Returns:
            dict: A dictionary where the keys are values from number_list and the values are how frequently they appear in number_list

        Raises:
           TypeError: If recurring_number_list contains a non numeric value
    """
    frequency_table = {}

    for elem in recurring_number_list:
        if elem in frequency_table:
            frequency_table[elem] += 1
        else:
            frequency_table[elem] = 1

    unique_elements = frequency_table.keys()

    for elem in unique_elements:
        if not(isinstance(elem, float) or isinstance(elem, int)):
            raise TypeError("ERROR: An element of recurring_number_list was not numeric")

    return frequency_table

if random_coin_experiment_count == 0:
    pass
# n = 1
elif random_coin_experiment_count == 1:
    #Plot figure 1.1
    pyplot.plot(range(len(toss_list)), toss_list)
    pyplot.suptitle("1.1 Winnings in " + str(coin_flip_count) + " plays of heads or tails")
    pyplot.xlabel("coin flips")
    pyplot.ylabel("winnings")
    pyplot.show()
# n > 1
else:
    pyplot.figure()
    #Plot figure 1.2
    #Plot figure 1.3
    frequency_data = number_list_to_frequency_list(times_in_lead_list)
    pyplot.subplot(212)
    pyplot.suptitle("Figure 1.3: Distribution of number of times in the lead.")
    pyplot.stem(frequency_data.keys(), frequency_data.values(), use_line_collection=True)

    pyplot.show()

