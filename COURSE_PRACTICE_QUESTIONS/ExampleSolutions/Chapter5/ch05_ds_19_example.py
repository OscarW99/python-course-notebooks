# Chapter 5: Data Structures

#* 1. Basic String Indexing
dna_sequence = "ATCGATCG"
print(dna_sequence[0])
print(dna_sequence[1:5])
print(dna_sequence[-3:])


#* 2. String Slicing with Protein Sequence
protein_sequence = "MKWVTFISLLLLFSSAYS"
print(protein_sequence[:3])
print(protein_sequence[-4:])
print(protein_sequence[::2])


#* 3. Demonstrating String Immutability
# Incorrect way (will raise error)
sequence = "AGCT"
# sequence[1] = "T"  # Uncommenting this line will raise an error
# Correct way
new_sequence = sequence[:1] + "T" + sequence[2:]
print(new_sequence)


#* 4. Finding Middle Character
sequence = "ATCGA"
print(sequence[len(sequence) // 2])


#* 5. Advanced Slicing
sequence = "AATTCCGG"
print(sequence[2:])
print(sequence[:-2])
