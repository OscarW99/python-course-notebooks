# Chapter 7: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Navigating and Creating Directories
# Print current working directory
# Navigate to project_files
# Create analysis directory
# Confirm creation
# Navigate back to the original starting directory
# Confirm current working directory


#* 2. Identifying Specific Files
# Identify FASTA files in bio_data
# Print identified files


#* 3. Modifying the Directory Structure
# Rename raw_data to input_data
# Confirm renaming


#* 4. Removing Files and Directories
# Remove notes.txt
# Remove results directory
# Confirm removal


#* 5. Building Paths
# Build path to final_report.txt
# Print path
# Confirm path validity


#* 6. Move a File
# Move gene_data.csv to analysis directory
# Confirm move


#* 7. Rename Files
# Rename CSV files in analysis
# Confirm renaming
