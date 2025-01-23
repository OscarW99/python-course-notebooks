# Question 4 Solution
import sys

if len(sys.argv) != 3:
    print("Error: This script requires exactly two arguments: input file and minimum length.")
    sys.exit(1)

filename = sys.argv[1]
try:
    min_length = int(sys.argv[2])
    print(f"Processing {filename} with minimum length of {min_length}.")
except ValueError:
    print("Error: Minimum length must be an integer.")
    sys.exit(1)