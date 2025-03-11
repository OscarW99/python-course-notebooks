
sequence = "ATGCCCGTATGCATGCATGC"

gc_count = sequence.count('G') + sequence.count('C')
gc_percentage = (gc_count / len(sequence)) * 100


motif = "ATG"
positions = []
for i in range(len(sequence) - len(motif) + 1):
    if sequence[i:i+len(motif)] == motif:
        positions.append(i)