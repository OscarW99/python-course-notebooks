# Chapter 4: Functions and Libraries

#* 1. Custom Function Creation
aa_weights = {
    'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 
    'C': 121.2, 'Q': 146.2, 'E': 147.1, 'G': 75.1, 
    'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2, 
    'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1, 
    'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1
}

def calculate_protein_weight(sequence):
    """
    Calculate the total molecular weight of a protein sequence.
    
    Parameters:
    sequence (str): The protein sequence
    
    Returns:
    float: The total molecular weight of the protein
    """
    return sum(aa_weights[aa] for aa in sequence)


#* 2. Lambda Function for Sequence Manipulation
clean_sequence = lambda seq: ''.join(filter(lambda x: x in 'ATGC', seq.upper()))


#* 3. Function with Default Parameters
def analyze_gene_expression(gene_name, expression_level, threshold=100):
    if expression_level > threshold:
        print(f"{gene_name} is highly expressed.")
    else:
        print(f"{gene_name} is lowly expressed.")


#* 4. Using *args in a Function
def calculate_average_sequence_length(*sequences):
    total_length = sum(len(seq) for seq in sequences)
    return total_length / len(sequences) if sequences else 0


#* 5. Using **kwargs in a Function
def protein_database_entry(**details):
    description = f"Protein: {details.get('name', 'Unknown')}\n"
    description += f"Function: {details.get('function', 'Unknown')}\n"
    description += f"Molecular Weight: {details.get('molecular_weight', 'Unknown')}\n"
    print(description)


#* 6. Recursive Function for Factorial
def calculate_factorial(num):
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")
    if num in [0, 1]:
        return 1
    return num * calculate_factorial(num - 1)


#* 7. Standard Library Modules
import random
import statistics

sequences = [''.join(random.choice('ATGC') for _ in range(random.randint(5, 20))) for _ in range(10)]
mean_length = statistics.mean(len(seq) for seq in sequences)
print(f"Mean sequence length: {mean_length}")


#* 8. Advanced Function with Libraries
import math

def analyze_sequence_distribution(sequences):
    lengths = [len(seq) for seq in sequences]
    mean_length = sum(lengths) / len(lengths)
    variance = sum((x - mean_length) ** 2 for x in lengths) / len(lengths)
    return math.sqrt(variance)


#* 9. Lambda and Built-in Functions
sequences = ['ATGC', 'GCTA', 'TAGC', 'CAGT']
reverse_sequences = list(map(lambda seq: seq[::-1], sequences))
filtered_sequences = list(filter(lambda seq: len(seq) >= 10, sequences))


#* 10. Docstring and Placeholder Function
def sequence_alignment(sequences, alignment_method, scoring_matrix):
    """
    Aligns sequences using the specified alignment method and scoring matrix.
    
    Parameters:
    sequences (list): List of sequences to align
    alignment_method (str): The alignment method to use (e.g., 'global', 'local')
    scoring_matrix (dict): The scoring matrix to use for alignment
    
    Returns:
    None
    """
    pass
