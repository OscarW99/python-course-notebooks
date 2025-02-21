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
relative_path_to_fasta = ""
print(relative_path_to_fasta)


#* 2. Navigating with the Double-dot Syntax
path_to_experiment_results = ""
print(path_to_experiment_results)


#* 3. Open and Read a File in various modes
#$ dna_file_r = 
#$ dna_file_a = 
#$ dna_file_w = 

#* 4. Using the `with` Statement