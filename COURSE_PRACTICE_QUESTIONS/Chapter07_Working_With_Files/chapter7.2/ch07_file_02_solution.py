# Chapter 7: Working with Files

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
    pass
    #$ content = 
    # Remove the pass statement and print content here


#* 2. Reading File Line by Line
# Add your code here


#* 3. Removing Newline Characters
# Add your code here


#* 4. Extracting Sequence Headers
# Add your code here


#* 5. Using `.readlines()` Method
# Add your code here


#* 6. Counting Sequence Lengths
# Add your code here
