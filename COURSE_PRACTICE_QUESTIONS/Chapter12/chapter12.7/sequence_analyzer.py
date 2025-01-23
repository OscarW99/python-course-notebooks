def analyze_sequence(seq):
    """Return the length of a DNA sequence."""
    return len(seq)

def main():
    sequence = "ATCG"
    length = analyze_sequence(sequence)
    print(f"Sequence length: {length}")

