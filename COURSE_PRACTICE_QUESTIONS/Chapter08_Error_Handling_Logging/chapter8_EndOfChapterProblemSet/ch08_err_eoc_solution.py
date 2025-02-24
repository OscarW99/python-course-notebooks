# Chapter 8: Error Handling and Logging

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import os
import logging

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Configure Logging
# Configure logging here
# Hint: Use basicConfig() with format parameter
# Format should include: %(asctime)s - %(levelname)s - %(message)s
# Remember to set level=logging.DEBUG

#* 2. File Reading with Error Handling
def read_sequence_file():
    try:
        # Add file reading code here
        pass
    except FileNotFoundError:
        # Add error handling here
        pass
    except Exception as e:
        # Add general error handling here
        pass

#* 3. Division with Error Handling
# Add logging configuration here
try:
    # File reading and division code here
    pass
except ZeroDivisionError:
    # Handle division by zero
    pass
except ValueError:
    # Handle invalid numbers
    pass
finally:
    # Add cleanup code
    pass

#* 4. Multiple Handlers Logging Configuration
# Create and configure handlers here
# Hint: Use logging.FileHandler() and setFormatter()

# Test with log messages

#* 5. Gene Data Processing
def process_gene_data():
    invalid_lines = 0
    try:
        # Add file processing code
        pass
    except Exception as e:
        # Add error handling
        pass
# Hint: Use try-except within a loop for each line
# Check if line matches expected format (split by '\t')
# Use logging.warning for invalid lines
# Keep track with counter variable
# Log final summary with logging.info

#* 6. Protein Analysis with Error Handling
def analyze_protein(sequence):
    molecular_weight = 0
    amino_acid_weights = {'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 'C': 121.2, 'E': 147.1, 
                    'Q': 146.2, 'G': 75.1, 'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2, 
                    'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1, 'T': 119.1, 'W': 204.2, 
                    'Y': 181.2, 'V': 117.1}
    try:
        # Calculate molecular weight by summing weights
        pass
    except KeyError as e:
        pass
    except Exception as e:
        pass
    return molecular_weight  # Placeholder return to avoid undefined function errors

#* 7. Function Debugging
def calculate_gc_content(sequence):
    # Add logging statements
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

#* 8. Sequence Validation with Error Handling
def validate_dna(sequence):
    valid_bases = {'A', 'T', 'G', 'C'}
    # Add try-except-else structure
    # Add logging statements
    for i, base in enumerate(sequence):
        if base not in valid_bases:
            # Add error handling here
            pass
            
#* 9. Sequence Processing with Different Logging Approaches
def process_sequence_file(filename):
    """Process a sequence file and check for invalid characters.
    Log errors using both logging.exception() and logging.error() to understand 
    the difference between these approaches."""
    invalid_chars = set()
    valid_chars = {'A', 'T', 'G', 'C', 'N'}
    
    try:
        # Add file reading code here
        # Track any invalid characters found
        # Use both logging approaches for different scenarios
        pass
    except FileNotFoundError:
        logging.exception("File not found")
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
    if invalid_chars:
        logging.info(f"Invalid characters found: {', '.join(invalid_chars)}")

#* 10. Sequence Comparison with Logging
def compare_sequences(seq1, seq2):
    # Add debug logging here
    differences = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            differences.append(i)
    return differences