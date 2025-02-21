# Question 3 Solution
import sys

if len(sys.argv) > 1:
    number_of_files = len(sys.argv) - 1  # Subtract 1 for the script name
    print(f"Number of FASTA files to process: {number_of_files}")
else:
    print("Error: No FASTA files provided.")