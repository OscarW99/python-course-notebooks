
dna = "ATGGCCTAA"

codons = []
for i in range(0, len(dna), 3):
    codons.append(dna[i:i+3])


complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
reversed_sequence = dna[::-1]
complement = ""
for base in reversed_sequence:
    complement += complement_dict[base]