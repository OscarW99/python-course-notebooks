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
    #$ content = 
    # print content here

#* 2. Reading File Line by Line

#* 3. Removing Newline Characters

#* 4. Extracting Sequence Headers

#* 5. Using `.readlines()` Method

#* 6. Counting Sequence Lengths