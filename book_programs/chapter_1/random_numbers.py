#!/usr/bin/python3

# Example Usage: python3 random_numbers.py <n> 
# Param n:       The number of random values between 0 and 1 to generate

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
    random_number_count = int(args[1])

except IndexError:
    pass
except ValueError:
    bad_input = True
    print("ERROR: Could not convert param n to an integer")

# Argument is negtive
if 'random_number_count' in globals() and random_number_count < 0:
    bad_input = True
    print("ERROR: Param n cannot be negative")

# Print usage help when arguments are bad
if bad_input:
    print("\nUsage: python3 random_numbers.py <n>\n  n is the number of random values between 0 and 1 to generate")
    sys.exit(1)

for i in range(random_number_count):
    print(random.uniform(0, 1))
