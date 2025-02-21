# Chapter 4: Functions and Libraries

#* 1. Creating and Documenting a Function
def analyze_protein_structure(protein_sequence):
    """
    Analyzes the structure of a given protein sequence.

    Parameters:
    protein_sequence (str): The protein sequence to analyze.

    Returns:
    None
    """
    pass

#* 2. Using map() Function
def convert_to_rna(dna_sequence):
    return dna_sequence.replace('T', 'U')

sequences = ["ATGCGA", "CCGTAG", "GGCCTA"]
rna_sequences = list(map(convert_to_rna, sequences))
print(rna_sequences)

#* 3. Filtering with filter() Function
def is_short_sequence(sequence):
    return len(sequence) < 15

gene_sequences = ["ATGCTTGA", "CCGTACTGCAG", "GGCCTA"]
short_sequences = list(filter(is_short_sequence, gene_sequences))
print(short_sequences)

#* 4. Basic Sorting
sequences = ["ATGC", "A", "ATGCGCTA", "AT"]
sorted_sequences = sorted(sequences, key=len)
print(sorted_sequences)

sorted_sequences_desc = sorted(sequences, key=len, reverse=True)
print(sorted_sequences_desc)

#* 5. Complex Sorting
def gc_content(sequence):
    return (sequence.count('G') + sequence.count('C')) / len(sequence)

dna_sequences = ["ATGC", "GCGC", "ATAT", "CGCG"]
sorted_by_gc = sorted(dna_sequences, key=gc_content)
print(sorted_by_gc)

#* 6. Calculate Melting Temperature
def calculate_melting_temperature(dna_sequence):
    """
    Calculates the DNA melting temperature.

    Parameters:
    dna_sequence (str): The DNA sequence to analyze.

    Returns:
    float: The calculated melting temperature.
    """
    at_pairs = dna_sequence.count('A') + dna_sequence.count('T')
    gc_pairs = dna_sequence.count('G') + dna_sequence.count('C')
    tm = 2 * at_pairs + 4 * gc_pairs
    return tm

print(calculate_melting_temperature("ATGCATGC"))
