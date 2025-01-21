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
# Configure logging here

try:
    # Add division by zero code
    pass
except Exception as e:
    # Add exception logging code
    pass

#* 2. Sequence Validator with Logging
def validate_sequence(dna_sequence):
    """
    Validates a DNA sequence.
    Raises ValueError if invalid characters found.
    """
    pass

#* 3. Process Data with Different Logging Approaches
def process_data(data):
    """
    Demonstrates both logging.exception() and logging.error() approaches.
    Raises TypeError if data is wrong type.
    Raises ValueError if data is invalid.
    """
    pass

#* 4. Logging for Multiple Error Types
# Set up your logging configuration for multiple handlers
# Remember to use addHandler() for each handler

# Test code that raises both error types