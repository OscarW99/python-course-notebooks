# Chapter 6: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.fasta"
# Windows: "data\\example.fasta" or r"data\example.fasta"
# Python generally handles forward slashes (/) well on all platforms.

#$ This Just Makes Sure We're Starting in the Right Directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  


#* 1. Open 'example.fasta' and read its content
with open('data/example.fasta', 'r') as fasta_file:
    content = fasta_file.read()
    print(content)  # Prints the entire content of the file

#* 2. Reading File Line by Line
with open('data/example.fasta', 'r') as fasta_file:
    for line in fasta_file:
        print(line, end='')  # end='' prevents adding extra newlines

#* 3. Removing Newline Characters
with open('data/example.fasta', 'r') as fasta_file:
    for line in fasta_file:
        print(line.strip())  # `strip()` removes leading/trailing whitespace including newlines

#* 4. Extracting Sequence Headers
with open('data/example.fasta', 'r') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            print(line.strip())  # Print headers without newlines

#* 5. Using `.readlines()` Method
with open('data/example.fasta', 'r') as fasta_file:
    lines = fasta_file.readlines()
    for line in lines:
        print(line.strip())  # Print each line without newline

#* 6. Counting Sequence Lengths
sequence_lengths = []
with open('data/example.fasta', 'r') as fasta_file:
    sequence = ''
    for line in fasta_file:
        if line.startswith('>'):
            if sequence:  # If we've collected a sequence, add its length
                sequence_lengths.append(len(sequence))
            sequence = ''  # Reset sequence
        else:
            sequence += line.strip()  # Add to sequence, strip whitespace

    if sequence:  # Add length of last sequence if it exists
        sequence_lengths.append(len(sequence))

print("Sequence lengths:", sequence_lengths)
average_length = sum(sequence_lengths) / len(sequence_lengths)
print("Average sequence length:", average_length)