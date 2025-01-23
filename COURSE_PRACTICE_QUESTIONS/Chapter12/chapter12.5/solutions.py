# Chapter 12: Creating Executable Python Scripts

#* 1. Simple OOP
class SequenceAnalyzer:
    def __init__(self, sequence):
        # Initialize with sequence
        pass
    
    def count_bases(self):
        # Return dictionary of base counts
        pass
    
    def get_length(self):
        # Return sequence length
        pass

# Test your class:
analyzer = SequenceAnalyzer("ATCGGATC")
print(analyzer.count_bases())
print(analyzer.get_length())


#* 2. Functional Programming
def count_amino_acids(protein_seq):
    """Return count of each amino acid in sequence."""
    # Return dictionary with counts of each amino acid
    pass

def is_hydrophobic(amino_acid):
    """Return True if amino acid is hydrophobic (A, V, L, I, P, F, M, W)."""
    # Check if amino acid is in hydrophobic group
    pass

# Test your functions:
protein = "MATVWL"
print(f"Amino acid counts: {count_amino_acids(protein)}")
print(f"Is M hydrophobic? {is_hydrophobic('M')}")


#* 3. Procedural Programming
# Mutation frequencies (in %) across different populations:
mutation_frequencies = [12.5, 45.2, 38.7, 28.1, 17.3, 42.8]

# Write code to:
# 1. Calculate the average mutation frequency
# 2. Find the highest and lowest frequencies
# 3. Count how many populations have high mutation rates (>30%)
# 4. Print all results with clear labels