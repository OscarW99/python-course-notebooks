# Chapter 7: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/dna_sequence.txt"
# Windows: "data\\dna_sequence.txt" or r"data\dna_sequence.txt"
# Python generally handles forward slashes (/) well on all platforms.

#$ This Just Makes Sure We're Starting in the Right Directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Create a Relative Path
relative_path_to_fasta = "data/genome_sequence.fasta"
print(relative_path_to_fasta)  # Output: data/genome_sequence.fasta


#* 2. Navigating with the Double-dot Syntax
path_to_experiment_results = "../../experiment_results.csv"
print(path_to_experiment_results)  # Output: ../../experiment_results.csv


#* 3. Open and Read a File in various modes
dna_file_r = open('data/dna_sequence.txt', 'r')
print(dna_file_r)  # Output: <open file 'data/dna_sequence.txt', mode 'r' at ...>

dna_file_a = open('data/dna_sequence.txt', 'a')
print(dna_file_a)  # Output: <open file 'data/dna_sequence.txt', mode 'a' at ...>

dna_file_w = open('data/dna_sequence.txt', 'w')
print(dna_file_w)  # Output: <open file 'data/dna_sequence.txt', mode 'w' at ...>

# Closing all files
dna_file_r.close()
dna_file_a.close()
dna_file_w.close()


#* 4. Using the `with` Statement
with open('data/dna_sequence.txt', 'r') as file:
    print(file)  # Output: <open file 'data/dna_sequence.txt', mode 'r' at ...>