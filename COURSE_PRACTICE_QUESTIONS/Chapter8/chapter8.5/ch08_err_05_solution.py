# Chapter 8: Error Handling and Logging

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

#$ This Just Makes Sure We're Starting in the Right Directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

import logging
from datetime import datetime

#* 1. Logging to File
# Configure logging here

#* 2. Protein Weight Calculation
def calculate_protein_weight(sequence):
    """
    Calculate molecular weight of protein sequence.
    Use logging to record:
    - Input sequence (DEBUG level)
    - Calculation progress (INFO level)
    - Any invalid amino acids (WARNING level)
    """
    
    # Amino acid weights (complete list)
    weights = {
        'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 'C': 121.2, 'Q': 146.2,
        'E': 147.1, 'G': 75.1, 'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2,
        'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1, 'T': 119.1, 'W': 204.2,
        'Y': 181.2, 'V': 117.1
    }
    pass

#* 3. Custom Logging Format
# Configure logging here


#* 4. DNA Sequence Validation
def validate_dna(sequence):
    pass