# Chapter 6: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.csv"
# Windows: "data\\example.csv" or r"data\example.csv"
# Python generally handles forward slashes (/) well on all platforms.

#$ This Just Makes Sure We're Starting in the Right Directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Reading a CSV File
# Your solution here

#* 2. Writing to a TSV File
gene_data = [
    ["Gene1", 2.5, 3.7],
    ["Gene2", 4.2, 2.0],
    ["Gene3", 1.2, 1.2]
]
# Your solution here

#* 3. Skipping Headers and Calculating Average Expression
# Your solution here

#* 4. Filtering Rows and Writing to a New File
# Your solution here