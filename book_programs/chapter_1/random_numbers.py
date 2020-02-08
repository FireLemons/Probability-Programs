#!/usr/bin/python

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
    print("ERROR: Insufficient arguments\n")

# Try to convert argument into an integer
try:
    random_number_count = int(args[1])

    # Argument is negtive
    if random_number_count < 0:
        bad_input = True
        print("ERROR: Param n cannot be negative")
except ValueError:
    bad_input = True
    print("ERROR: Could not convert param n to an integer")


# Print usage help when arguments are bad
if bad_input:
    print("Usage: python3 random_numbers.py <n>\n  n is the number of random values between 0 and 1 to generate")

