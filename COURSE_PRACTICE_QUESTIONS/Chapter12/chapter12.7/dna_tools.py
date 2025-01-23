def count_gc(sequence):
    """Calculate the GC content of a DNA sequence as a percentage."""
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

# Current code that needs to be restructured:
sequence = "ATCGCGTA"
result = count_gc(sequence)
print(f"GC content: {result}%")