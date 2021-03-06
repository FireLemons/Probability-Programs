# Usage: python3 de_mere_1.py <n> <mute_output>
#   n:                      The number of four dice roll experiments to simulate
#   mute_output(optional):  If the value is "mute" or "m" the results of individual experiments are not printed

# Example Usage: python3 de_mere_1.py 10

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
    random_dice_experiment_count = int(args[1])

except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert n to an integer")

# Argument is negtive
if 'random_dice_experiment_count' in globals() and random_dice_experiment_count < 0:
    bad_input = True
    print("ERROR: n cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 de_mere_1.py <n> <mute_output>")
    print("  n is the number of four dice roll experiments to simulate")
    print("  mute_output(optional) can be set to \"mute\" or \"m\" to hide the results of indivdual experiments")
    print("\nExample Usage: python3 de_mere_1.py 10")
    sys.exit(1)

######################
# Dice Roll Experiment
######################
mute_output = len(args) >= 3 and (args[2] == "m" or args[2] == "mute")
successCount = 0

for i in range(random_dice_experiment_count):
    currentExperimentResults = []
    for i in range(4):
        currentExperimentResults.append(random.randint(1, 6))
 
    if not mute_output:
        print(currentExperimentResults)
    try:
        currentExperimentResults.index(6)
        successCount += 1
    except ValueError:
        pass

##########################
# Print Experiment Results
##########################
print("Number of successes: ", successCount)
print("Proportion of successes: ", successCount/random_dice_experiment_count)
