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
try:
    # File reading and division code
    with open('data/numbers.txt', 'r') as file:
        line_number = 1  # Track the line number manually
        for line in file:
            # Convert the line to a number
            number = int(line.strip())
            # Perform division and print the result
            result = 1000/ number
            print(f"Line {line_number}: 1000 / {number} = {result}")
            line_number += 1
except ZeroDivisionError:
    logging.error(f"Error on line {line_number}: Cannot divide by zero", exc_info=True)
except ValueError:
    logging.error(f"Error on line {line_number}: Invalid number format in file", exc_info=True)
finally:
    logging.info("File operation completed")


#* 4. Multiple Handlers Logging Configuration
import logging

# Step 1: Create a custom logger
logger = logging.getLogger('custom_logger')
logger.setLevel(logging.DEBUG)  # Set the overall logging level

# Step 2: Configure the first handler - Write all messages to logs/dna_analysis.log
file_handler = logging.FileHandler('logs/dna_analysis.log')
file_handler.setLevel(logging.DEBUG)  # Logs messages of DEBUG level and above
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

# Step 3: Configure the second handler - Write only CRITICAL messages to logs/errors.log
critical_handler = logging.FileHandler('logs/errors.log')
critical_handler.setLevel(logging.CRITICAL)  # Logs only CRITICAL level messages
critical_format = logging.Formatter('%(asctime)s - CRITICAL ISSUE: %(message)s')
critical_handler.setFormatter(critical_format)

# Step 4: Add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(critical_handler)

# Step 5: Test the configuration with messages at various levels
logger.debug('This is a DEBUG message.')      # Will only appear in dna_analysis.log
logger.info('This is an INFO message.')       # Will only appear in dna_analysis.log
logger.warning('This is a WARNING message.')  # Will only appear in dna_analysis.log
logger.error('This is an ERROR message.')     # Will only appear in dna_analysis.log
logger.critical('This is a CRITICAL message.')  # Appears in both dna_analysis.log and errors.log


#* 5. Gene Data Processing
### Configuration ###
# Reset logging to avoid confusion
logging.getLogger().handlers = []  # Remove all existing handlers 
# All logs from this point will go to a new file at level DEBUG
logging.basicConfig(filename='logs/new_log_file.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
#######

def process_gene_data(file_path):
    invalid_lines = 0
    try:
        with open(file_path, 'r') as file:
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

process_gene_data('data/gene_data.txt')


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

# Call function
print(analyze_protein('MAGWFLPTDSVYHIK'))
print(analyze_protein('KLYGDSRTPHINACF'))
print(analyze_protein('WLHFTZGYRPIVDQM'))


#* 7. Function Debugging
def calculate_gc_content(sequence):
    logging.debug(f"Entering calculate_gc_content with sequence: {sequence}")
    gc_count = sequence.count('G') + sequence.count('C')
    result = (gc_count / len(sequence)) * 100
    logging.debug(f"Exiting calculate_gc_content with result: {result}")
    return result

calculate_gc_content("ATGC")
calculate_gc_content("ATCGGCTGCA")
calculate_gc_content("ATCCTGGCTGCA")


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
    else:
        logging.info("Sequence is valid")

validate_dna("ATGCGTACGTAG")
validate_dna("ATGCGTACGTAGX")  # This will raise an error
validate_dna("ATGCGTACGTAGC")


#* 9. Sequence Processing with Different Logging Approaches
def process_sequence_file(filename):
    """Process a sequence file and check for invalid characters.
    Log errors using both logging.exception() and logging.error() to understand 
    the difference between these approaches."""
    invalid_chars = set()
    valid_chars = {'A', 'T', 'G', 'C', 'N'}
    
    try:
        # Attempt to open the file
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                # Skip header lines that start with '>'
                if line.startswith('>'):
                    continue
                
                # Validate characters in the sequence
                for char in line.strip().upper():
                    if char not in valid_chars:
                        invalid_chars.add(char)
                        logging.error(f"Invalid character '{char}' found on line {line_num}")
    except FileNotFoundError:
        logging.exception("File not found")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")
    
    # Log invalid characters summary
    if invalid_chars:
        logging.info(f"Invalid characters found: {', '.join(invalid_chars)}")
    else:
        logging.info("No invalid characters detected.")

# Test the function with the provided file
process_sequence_file('data/sequences.txt')


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