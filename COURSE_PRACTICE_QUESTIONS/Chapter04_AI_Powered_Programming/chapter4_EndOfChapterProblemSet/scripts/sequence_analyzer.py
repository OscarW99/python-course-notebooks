# Input DNA sequence
sequence = "ATGCCCGTATGCATGCATGC"

# Calculate GC content
gc_count = sequence.count('G') + sequence.count('C')
gc_percentage = (gc_count / len(sequence)) * 100

# Find specific motif
motif = "ATG"
positions = []
for i in range(len(sequence) - len(motif) + 1):
    if sequence[i:i+len(motif)] == motif:
        positions.append(i)