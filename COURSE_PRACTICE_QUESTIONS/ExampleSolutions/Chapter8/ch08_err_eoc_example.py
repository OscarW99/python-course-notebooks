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
logging.basicConfig(filename='logs/dna_analysis.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning')
logging.error('This is an error')
logging.critical('This is a critical error')

#* 2. File Reading with Error Handling
def read_sequence_file():
    try:
        with open('data/sequences.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error("File 'sequences.txt' not found")
        return None
    except Exception as e:
        logging.exception("Unexpected error while reading file")
        return None

#* 3. Division with Error Handling
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s %(lineno)d')

try:
    with open('data/numbers.txt', 'r') as file:
        num1, num2 = map(float, file.read().splitlines())
        result = num1 / num2
        print(f"Result: {result}")
except ZeroDivisionError:
    logging.error("Cannot divide by zero", exc_info=True)
except ValueError:
    logging.error("Invalid number format in file", exc_info=True)
finally:
    logging.info("File operation completed")

#* 4. Multiple Handlers Logging Configuration
dna_handler = logging.FileHandler('logs/dna_analysis.log')
error_handler = logging.FileHandler('logs/errors.log')

dna_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d')

dna_handler.setFormatter(dna_formatter)
error_handler.setFormatter(error_formatter)

dna_handler.setLevel(logging.DEBUG)
error_handler.setLevel(logging.CRITICAL)

logger = logging.getLogger('multi_handler_logger')
logger.addHandler(dna_handler)
logger.addHandler(error_handler)

logger.debug('Debug message for DNA analysis')
logger.info('Info message for DNA analysis')
logger.warning('Warning message for DNA analysis')
logger.error('Error message for DNA analysis')
logger.critical('Critical error message for DNA analysis')

#* 5. Gene Data Processing
def process_gene_data():
    invalid_lines = 0
    try:
        with open('data/gene_data.txt', 'r') as file:
            for line_num, line in enumerate(file, 1):
                try:
                    gene_id, sequence = line.strip().split('\t')
                    # Process valid line here
                    logging.info(f"Processed gene {gene_id}")
                except ValueError:
                    invalid_lines += 1
                    logging.warning(f"Line {line_num} does not match expected format")
    except Exception as e:
        logging.exception("Error occurred while processing gene data")
    logging.info(f"Finished processing. Invalid lines: {invalid_lines}")

#* 6. Protein Analysis with Error Handling
def analyze_protein(sequence):
    molecular_weight = 0
    amino_acid_weights = {'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 'C': 121.2, 'E': 147.1, 
                    'Q': 146.2, 'G': 75.1, 'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2, 
                    'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1, 'T': 119.1, 'W': 204.2, 
                    'Y': 181.2, 'V': 117.1}
    try:
        for amino_acid in sequence.upper():
            molecular_weight += amino_acid_weights[amino_acid]
    except KeyError as e:
        logging.error(f"Invalid amino acid encountered: {e}")
        return -1
    except Exception as e:
        logging.exception("Unexpected error in protein analysis")
        return -1
    return molecular_weight

#* 7. Function Debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')

def calculate_gc_content(sequence):
    logging.debug(f"Entering calculate_gc_content with sequence: {sequence}")
    gc_count = sequence.count('G') + sequence.count('C')
    result = (gc_count / len(sequence)) * 100
    logging.debug(f"Exiting calculate_gc_content with result: {result}")
    return result

calculate_gc_content("ATGC")

#* 8. Sequence Validation with Error Handling
def validate_dna(sequence):
    valid_bases = {'A', 'T', 'G', 'C'}
    logging.debug(f"Sequence length: {len(sequence)}")
    try:
        for i, base in enumerate(sequence.upper()):
            if base not in valid_bases:
                raise ValueError(f"Invalid base '{base}' found at position {i + 1}")
    except ValueError as e:
        logging.error(str(e))
        raise
    else:
        logging.info("Sequence is valid")

#* 9. Sequence Processing with Different Logging Approaches
def process_sequence_file(filename):
    """Process a sequence file and check for invalid characters.
    Log errors using both logging.exception() and logging.error() to understand 
    the difference between these approaches."""
    invalid_chars = set()
    valid_chars = {'A', 'T', 'G', 'C', 'N'}
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                for char in line.strip().upper():
                    if char not in valid_chars:
                        invalid_chars.add(char)
                        logging.error(f"Invalid character '{char}' found", exc_info=True)
    except FileNotFoundError:
        logging.exception("File not found")
    except Exception as e:
        logging.exception(f"An error occurred: {e}")
    if invalid_chars:
        logging.info(f"Invalid characters found: {', '.join(invalid_chars)}")

#* 10. Sequence Comparison with Logging
def compare_sequences(seq1, seq2):
    logging.debug("Entering compare_sequences")
    if len(seq1) != len(seq2):
        logging.error("Sequences have different lengths")
        return []
    differences = []
    try:
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                differences.append(i)
                logging.info(f"Difference found at position {i}")
    except IndexError:
        logging.error("Index error during sequence comparison", exc_info=True)
    logging.debug(f"Exiting compare_sequences with {len(differences)} differences")
    return differences

compare_sequences("ATGC", "ATCG")