#!/usr/bin/env python3

import sys

# Get script name
script_name = sys.argv[0]

# Get number of additional arguments
num_args = len(sys.argv) - 1

# Print required information
print(f"Script name: {script_name}")
print(f"Number of arguments provided: {num_args}")
print("Arguments:", " ".join(sys.argv[1:]) if num_args > 0 else "None")