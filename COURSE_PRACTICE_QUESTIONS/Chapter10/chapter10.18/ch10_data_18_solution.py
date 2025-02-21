# Chapter 9: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

from Bio import Align
from Bio import AlignIO
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Pairwise Sequence Alignment
# Create Align.PairwiseAligner
# Configure scoring parameters
# Perform alignment
# Print alignment details and score

#* 2. Reading Multiple Sequence Alignment
# Read Clustal format alignment file
# Calculate and print alignment length
# Iterate and print each sequence

#* 3. Extracting Conserved Columns
# Load multiple sequence alignment
# Find conserved columns
# Print or collect conserved columns