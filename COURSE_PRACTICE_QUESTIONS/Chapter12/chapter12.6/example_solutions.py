
## QUESTION 1
# dna_tools.py
def calculate_a_freq(sequence):
    # TODO: Count 'A' bases in the sequence
    a_count = sequence.count('A')
    # TODO: Calculate the frequency of 'A' bases
    freq = a_count / len(sequence) if sequence else 0
    return freq


## QUESTION 2
# dna_tools.py
def count_bases(sequence):
    """
    Count the number of each base in the given DNA sequence.
    
    Args:
    sequence (str): A string representing a DNA sequence.
    
    Returns:
    dict: A dictionary with base counts.
    """
    return {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }

# file_parser.py
def read_fasta(filename):
    """
    Simulate reading a FASTA file by printing a message.
    
    Args:
    filename (str): The name of the FASTA file to be read.
    
    Returns:
    None
    """
    print(f"Reading {filename}")