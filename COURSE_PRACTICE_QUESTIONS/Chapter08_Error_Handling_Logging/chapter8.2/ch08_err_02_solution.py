# Chapter 8: Error Handling and Logging

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

#$ This Just Makes Sure We're Starting in the Right Directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Reading DNA Sequences
def read_dna_file(filename):
    file = None
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print("File not found")
    else:
        # Read all lines from the file and store them in a list called 'sequences'.
        # Print "Successfully read {number} sequences" with the count of sequences
        pass
    finally:
        # Check if file exists using 'if file:'
        # Close the file if it exists
        # Print "File closed" after closing
        pass


#* 2. Validate Protein Sequence
valid_amino_acids = {'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'}
# Your code here


#* 3. Divide Numbers from File
def divide_numbers_from_file(filename):
    # Try block for file operations and division
    # Except blocks for exceptions
    pass


#* 4. Check Sequence Length
def check_sequence_length(filename, expected_length):
    # Try block for file operations and length check
    # Except blocks for exceptions
    # Else block for success message
    # Finally block for cleanup
    pass