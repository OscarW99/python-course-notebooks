# Chapter 7: Error Handling and Logging

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Basic Exception Logging
logging.basicConfig(filename='logs/errors.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

try:
    result = 10 / 0
except Exception as e:
    logging.exception("An error occurred during division")

#* 2. Sequence Validator with Logging
def validate_sequence(dna_sequence):
    """
    Validates a DNA sequence.
    Raises ValueError if invalid characters found.
    """
    valid_nucleotides = set('ATGC')
    for index, char in enumerate(dna_sequence.upper()):
        if char not in valid_nucleotides:
            logging.error(f"Invalid nucleotide '{char}' found at position {index + 1}", exc_info=True)
            raise ValueError(f"Invalid nucleotide '{char}' found at position {index + 1}")

#* 3. Process Data with Different Logging Approaches
def process_data(data):
    """
    Demonstrates both logging.exception() and logging.error() approaches.
    Raises TypeError if data is wrong type.
    Raises ValueError if data is invalid.
    """
    try:
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        if len(data) < 5:
            raise ValueError("Data list must contain at least 5 elements")
    except TypeError as e:
        logging.exception(f"Type error occurred: {e}")
    except ValueError as e:
        logging.error(f"Value error occurred: {e}", exc_info=True)

#* 4. Logging for Multiple Error Types
type_logger = logging.getLogger('type_error_logger')
value_logger = logging.getLogger('value_error_logger')

type_handler = logging.FileHandler('type_errors.log')
value_handler = logging.FileHandler('value_errors.log')

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

type_handler.setFormatter(formatter)
value_handler.setFormatter(formatter)

type_logger.addHandler(type_handler)
value_logger.addHandler(value_handler)

# Test code that raises both error types
try:
    raise TypeError("This is a test TypeError")
except TypeError as e:
    type_logger.exception("TypeError caught:")

try:
    raise ValueError("This is a test ValueError")
except ValueError as e:
    value_logger.error("ValueError caught:", exc_info=True)