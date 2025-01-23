# Chapter 12: Creating Executable Python Scripts

#* 1. Simple OOP
class SequenceAnalyzer:
    def __init__(self, sequence):
        # Verify input is a string
        if not isinstance(sequence, str):
            raise ValueError("Sequence must be a string")
        self.sequence = sequence
    
    def count_bases(self):
        # Count each base in the sequence
        return {
            'A': self.sequence.count('A'),
            'T': self.sequence.count('T'),
            'G': self.sequence.count('G'),
            'C': self.sequence.count('C')
        }
    
    def get_length(self):
        # Return the length of the sequence
        return len(self.sequence)

# Test your class:
analyzer = SequenceAnalyzer("ATCGGATC")
print(analyzer.count_bases())
print(analyzer.get_length())


#* 2. Functional Programming
def count_amino_acids(protein_seq):
    """Return count of each amino acid in sequence."""
    # Initialize a dictionary to hold counts
    counts = {}
    for aa in protein_seq:
        counts[aa] = counts.get(aa, 0) + 1
    return counts

def is_hydrophobic(amino_acid):
    """Return True if amino acid is hydrophobic (A, V, L, I, P, F, M, W)."""
    hydrophobic_aa = set('AVLIPFMW')
    return amino_acid in hydrophobic_aa

# Test your functions:
protein = "MATVWL"
print(f"Amino acid counts: {count_amino_acids(protein)}")
print(f"Is M hydrophobic? {is_hydrophobic('M')}")


#* 3. Procedural Programming
# Mutation frequencies (in %) across different populations:
mutation_frequencies = [12.5, 45.2, 38.7, 28.1, 17.3, 42.8]

def analyze_mutation_frequencies(frequencies):
    if not frequencies:
        return "No data provided"

    # Calculate average mutation frequency
    avg_frequency = sum(frequencies) / len(frequencies)
    
    # Find highest and lowest frequencies
    highest = max(frequencies)
    lowest = min(frequencies)
    
    # Count high mutation rates
    high_mutation_count = sum(1 for freq in frequencies if freq > 30)

    return {
        "Average mutation frequency": f"{avg_frequency:.2f}%",
        "Highest frequency": f"{highest:.2f}%",
        "Lowest frequency": f"{lowest:.2f}%",
        "Number of high mutation populations": high_mutation_count
    }

# Analyze and print results
results = analyze_mutation_frequencies(mutation_frequencies)
for key, value in results.items():
    print(f"{key}: {value}")