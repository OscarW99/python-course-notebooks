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
logging.basicConfig(
    filename='logs/dna_analysis.log',
    filemode='a',
    format='%(levelname)s:%(message)s',
    encoding='utf-8',
    level=logging.DEBUG
)

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

#* 2. Protein Weight Calculation
def calculate_protein_weight(sequence):
    """
    Calculate molecular weight of protein sequence.
    Use logging to record:
    - Input sequence (DEBUG level)
    - Calculation progress (INFO level)
    - Any invalid amino acids (WARNING level)
    """
    weights = {
        'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 'C': 121.2, 'Q': 146.2,
        'E': 147.1, 'G': 75.1, 'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2,
        'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1, 'T': 119.1, 'W': 204.2,
        'Y': 181.2, 'V': 117.1
    }
    logging.debug(f"Input sequence: {sequence}")
    total_weight = 0
    valid_amino_acids = set(weights.keys())
    for amino_acid in sequence.upper():
        if amino_acid in valid_amino_acids:
            total_weight += weights[amino_acid]
            logging.info(f"Adding weight for amino acid {amino_acid}: {weights[amino_acid]}")
        else:
            logging.warning(f"Invalid amino acid detected: {amino_acid}")
    logging.info(f"Total molecular weight calculated: {total_weight}")
    return total_weight

#* 3. Custom Logging Format
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
logging.info('Custom formatted log message')

#* 4. DNA Sequence Validation
def validate_dna(sequence):
    logging.basicConfig(
        format='%(asctime)s %(filename)s:%(funcName)s %(levelname)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
    valid_nucleotides = {'A', 'T', 'G', 'C'}
    if not set(sequence.upper()).issubset(valid_nucleotides):
        logging.error(f"Invalid nucleotide(s) in sequence: {sequence}")
    else:
        logging.info(f"Valid DNA sequence: {sequence}")

# Test the DNA validator
validate_dna("ATXGC")