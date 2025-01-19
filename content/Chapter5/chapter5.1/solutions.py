# Chapter 5: Local Development Environment Problem Set

# 1. Test Script
print("hello world")


# 2. Sequence Transformation
# Define initial list of DNA sequences
sequences = ['tATGaagC', 'gGGCcaTA', 'TAGC', 'cagt', 'GGttGG']

# Lambda function to convert sequences to uppercase
uppercase_converter = # TODO: your implementation here

# Use map() to convert sequences to uppercase
uppercase_sequences = # TODO: your implementation here

# function to count nucleotides
def count_nucleotide(sequence, nucleotide):
    # TODO: your implementation here
    pass

# Use filter() to keep sequences with at least two 'G' nucleotides
g_rich_sequence = # TODO: your implementation here

# Optional: print results to verify
print("Original Sequences:", sequences)
print("Uppercase Sequences:", uppercase_sequences)
print("G-rich Sequences:", g_rich_sequences)


# 3. Protein Analysis Function
def analyze_proteins(protein_sequences, length_threshold=50):
    """
    Analyze protein sequences and return statistics.
    
    Args:
        protein_sequences (list): List of protein sequences
        length_threshold (int): Length threshold for filtering sequences
        
    Returns:
        dict: Dictionary containing analysis results
    """
    # Your implementation here
    pass


# 4. Temperature Data Analysis
def analyze_temperatures(temperatures, threshold=30):
    """
    Analyze temperature readings and return statistics.
    
    Args:
        temperatures (list): List of temperature readings
        threshold (float): Temperature threshold in Celsius
        
    Returns:
        dict: Dictionary containing analysis results
    """
    # Your implementation here
    pass