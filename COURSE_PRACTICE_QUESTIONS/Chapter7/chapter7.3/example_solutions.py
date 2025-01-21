# Chapter 7: Error Handling and Logging

#* 1. DNA Sequence Validation
dna_sequence = "ATGCCTGAATTC"
total_reads = 1500
quality_scores = [32, 35, 40, 28, 31, 29, 33, 35, 38, 40, 37, 39]
assert len(dna_sequence) == len(quality_scores), "Sequence length does not match number of quality scores"
assert all(score > 25 for score in quality_scores), "All quality scores must be above 25"
assert total_reads > 0, "Total reads must be a positive number"


#* 2. GC Content Calculation
def calculate_gc_content(sequence):
    """
    Calculate the GC content of a DNA sequence.
    Returns a float between 0 and 1.
    Example:
        'GCGC' -> 1.0 (100% GC content)
        'ATAT' -> 0.0 (0% GC content)
    """
    valid_nucleotides = {'A', 'T', 'G', 'C'}
    assert set(sequence.upper()) <= valid_nucleotides, "Sequence contains invalid nucleotides"
    gc_count = sum(1 for nuc in sequence.upper() if nuc in 'GC')
    return gc_count / len(sequence)

# Test cases
assert calculate_gc_content("GCGC") == 1.0
assert calculate_gc_content("ATAT") == 0.0
assert calculate_gc_content("ATGC") == 0.5


#* 3. Protein Sequence Validation
def validate_protein_sequence(sequence, molecular_weight, isoelectric_point):
    """
    Validates a protein sequence and its properties.
    Returns True if all validations pass.

    Parameters:
    sequence: str - protein sequence using one-letter amino acid codes
    molecular_weight: float - sum of weights of all amino acids (in Daltons)
    isoelectric_point: float - pH at which protein has neutral charge (between 0-14)
    """
    aa_weights = {
        'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 'C': 121.2, 
        'E': 147.1, 'Q': 146.2, 'G': 75.1, 'H': 155.2, 'I': 131.2,
        'L': 131.2, 'K': 146.2, 'M': 149.2, 'F': 165.2, 'P': 115.1,
        'S': 105.1, 'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1
    }
    valid_amino_acids = set(aa_weights.keys())
    assert set(sequence.upper()) <= valid_amino_acids, "Invalid amino acid in sequence"
    
    calculated_weight = sum(aa_weights[aa] for aa in sequence.upper())
    assert abs(calculated_weight - molecular_weight) < 0.1, "Molecular weight does not match within tolerance"

    assert 0 <= isoelectric_point <= 14, "Isoelectric point must be between 0 and 14"
    return True

# Test cases
assert validate_protein_sequence("AAKK", 470.6, 9.74)
assert not validate_protein_sequence("AAKKZ", 470.6, 9.74)
assert not validate_protein_sequence("AAKK", 400, 9.74)
assert not validate_protein_sequence("AAKK", 470.6, -1)


#* 4. Experimental Data Validation
time_points = [0, 2, 4, 8, 12, 24]
replicate_counts = {'control': 3, 'treatment': 3}
missing_values = ['NA', 'NA', 'NA', '2.4', '2.8', '3.1']
assert all(time_points[i] < time_points[i+1] for i in range(len(time_points)-1)), "Time points must be in ascending order"
assert replicate_counts['control'] == replicate_counts['treatment'], "Number of replicates must be equal"
assert missing_values.count('NA') / len(missing_values) <= 0.5, "Missing values exceed 50% of measurements"