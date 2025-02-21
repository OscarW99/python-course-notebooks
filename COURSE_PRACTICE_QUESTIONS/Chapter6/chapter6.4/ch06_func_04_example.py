# Chapter 6: Functions and Libraries

#* 1. Working with iter() and next()
# Creating an iterator from the DNA codons list and printing three codons
dna_codons = ['ATG', 'CCA', 'GGT', 'TAA']
codon_iterator = iter(dna_codons)

print(next(codon_iterator))
print(next(codon_iterator))
print(next(codon_iterator))


#* 2. Using enumerate() and zip()
seq1 = ['A', 'T', 'G', 'C']
seq2 = ['T', 'A', 'C', 'G']

# Printing each nucleotide with its index from seq1
for index, nucleotide in enumerate(seq1):
    print(f"Index {index}: {nucleotide}")

# Creating a list of tuples pairing corresponding nucleotides from seq1 and seq2
paired_nucleotides = list(zip(seq1, seq2))
print(paired_nucleotides)


#* 3. Sorting and Reversing
expression = [45.1, 32.7, 67.8, 21.9, 54.3]

# Creating a sorted version in descending order
sorted_values = sorted(expression, reverse=True)
print(sorted_values)

# Converting it to a reversed iterator and printing the first three values
reverse_iterator = iter(sorted_values)
print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))
