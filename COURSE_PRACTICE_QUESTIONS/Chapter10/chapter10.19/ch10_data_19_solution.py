# Chapter 9: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO
from Bio.Seq import Seq
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Performing a BLAST Search
# Create Seq object
# Perform BLAST search
# Parse results
# Print first alignment info

#* 2. Parsing BLAST XML Results
# Read the BLAST XML file
# Create empty lists for storing data
# Extract required information from each hit
# Return the collected data

#* 3. Function for Protein BLAST Search
# Define function with parameters
# Perform protein BLAST search
# Save results to specified file
# Close handle and print confirmation