# Chapter 6: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import os
import csv
from datetime import date

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Listing FASTA Files
# Use os.listdir() to get files in the directory
# Remember to filter for .fasta extension

#* 2. Extracting Differential Genes
# Hint: Use csv.reader and csv.writer
# Steps:
# 1. Open input file with csv.reader
# 2. Open output file with csv.writer
# 3. Read header row first (use next()) and write it to output file
# 4. For each row, check the 'Differential' column (using list indexing)
# 5. Write selected rows to output file

#* 3. Appending to Log File
# Hint: Use 'a' mode for appending
# To get today's date:
# from datetime import date
# today = date.today()
# today_string = today.strftime("%Y-%m-%d")
# Don't forget to add a newline character (\n) before new content

#* 4. Combining Patient Data Files
# Steps:
# 1. Open and read first file
# 2. Store header separately
# 3. Open and read second file (skip header)
# 4. Write combined data to new file

#* 5. Creating Subdirectories
# Hint: Use os.path.exists() to check directory existence
# Use os.makedirs() to create directories
# Remember to use os.path.join() for paths

#* 6. Counting Sequences in FASTA
# Hint: Initialize a counter
# Read file line by line
# Check if line starts with '>'

#* 7. Cleaning Genotype Data
# Since we're working with CSV files, let's break this down:
# 1. Use csv.reader to read the input file
# 2. Use csv.writer for the output file
# 3. For each row in the reader:
#    - Create a new row where you replace 'NA' with '0'
#    - Write the new row to the output file
# Hint: You can use the list replace() method to help

#* 8. Calculating Average Molecular Weight
# Steps:
# 1. Read all lines and calculate average
# 2. Open file in append mode
# 3. Write average at the end

#* 9. Archiving Old Records
# Hint: Use os.path.getmtime() to get modification time of a file
# Use os.rename() to move files
# Import time module for timestamp comparison

#* 10. Gene Names to Uppercase with Numbering
# Steps:
# 1. Read input file line by line
# 2. Use enumerate() for line numbers
# 3. Convert each line to uppercase
# 4. Write to new file