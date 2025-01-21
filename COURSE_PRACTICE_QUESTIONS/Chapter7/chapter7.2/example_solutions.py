# Chapter 7: Error Handling and Logging

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
        sequences = file.readlines()
        print(f"Successfully read {len(sequences)} sequences")
    finally:
        if file:
            file.close()
            print("File closed")


#* 2. Validate Protein Sequence
valid_amino_acids = {'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'}
def validate_protein_sequence(filename):
    try:
        with open(filename, 'r') as file:
            sequence = file.read().strip()
            for index, amino_acid in enumerate(sequence, start=1):
                if amino_acid not in valid_amino_acids:
                    raise ValueError(f"Invalid amino acid {amino_acid} found at position {index}")
    except FileNotFoundError:
        print("File not found")
    except ValueError as e:
        print(e)


#* 3. Divide Numbers from File
def divide_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            num1, num2 = map(float, file.read().splitlines())
            result = num1 / num2
            print(f"Result: {result}")
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid number found in file")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Operation completed")


#* 4. Check Sequence Length
def check_sequence_length(filename, expected_length):
    try:
        with open(filename, 'r') as file:
            sequence = file.read().strip()
            actual_length = len(sequence)
            if actual_length != expected_length:
                raise ValueError(f"Sequence length {actual_length} does not match expected length {expected_length}")
    except FileNotFoundError:
        print("File not found")
    except ValueError as e:
        print(e)
    else:
        print("Sequence length is valid")
    finally:
        print("File operation completed")