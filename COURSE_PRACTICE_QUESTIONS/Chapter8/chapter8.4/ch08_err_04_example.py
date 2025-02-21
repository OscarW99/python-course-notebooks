# Chapter 7: Error Handling and Logging

import logging

# Configure logging to show all messages
logging.basicConfig(level=logging.DEBUG)

#* 1. Logging Severity Levels
logging.debug("Sequence comparison started")
logging.info("Processing sequence with ID: SEQ12345")
logging.warning("Sequence contains potential SNPs")
logging.error("Invalid sequence format detected")
logging.critical("Database connection lost during sequence retrieval")

#* 2. DNA Sequence Processing
def process_dna_sequence(sequence):
    logging.debug(f"Processing DNA sequence: {sequence}")
    logging.info(f"Sequence length: {len(sequence)}")
    
    if len(sequence) < 10:
        logging.warning("Sequence length is shorter than recommended for analysis")
    
    if not set(sequence.upper()).issubset({'A', 'T', 'G', 'C'}):
        logging.error("Invalid nucleotides detected in sequence")
    
    if not sequence:
        logging.critical("Empty sequence provided")

#* 3. Changing Logging Level
# Set the logging level to DEBUG to make all messages visible, then set it to different levels and take note of the output
logging.basicConfig(level=logging.DEBUG)

logging.debug("Starting DNA processing...")
logging.info("Reading sequence file...")
logging.warning("Sequence contains ambiguous nucleotides")
logging.error("Failed to align sequences")
logging.critical("Out of memory - cannot continue processing")