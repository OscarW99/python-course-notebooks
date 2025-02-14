# Chapter 3: Data Structures

#* 1. Updating a Single Element
bases = ['A', 'T', 'C', 'G']
# Solution:
bases[1] = 'U'
print(bases)


#* 2. Inserting Elements in a DNA Sequence
dna_sequence = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C']
# Solution:
dna_sequence[4:4] = ['A', 'T']
print(dna_sequence)


#* 3. Replacing a Slice with a Longer Sequence
dna_sequence = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C']
# Solution:
dna_sequence[2:5] = ['C', 'G', 'T', 'A', 'C']
print(dna_sequence)


#* 4. Deleting a Slice of Elements
dna_sequence = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C']
# Solution:
del dna_sequence[1:4]
print(dna_sequence)
