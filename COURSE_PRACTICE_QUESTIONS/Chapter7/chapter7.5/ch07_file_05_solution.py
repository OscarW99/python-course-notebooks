# Chapter 7: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/gene_expression.csv"
# Windows: "data\\gene_expression.csv" or r"data\gene_expression.csv"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Reading a CSV File
# Your solution here

#* 2. Filtering Data and Writing to CSV
# Your solution here

#* 3. Reading TSV and Calculating Average Age
# Your solution here

#* 4. Creating and Writing DataFrame
data = {
    'Protein': ['P53', 'BRCA1', 'EGFR', 'TNF', 'IL6'],
    'Expression': [0.8, 1.2, 1.5, 0.6, 1.1]
}
# Your solution here