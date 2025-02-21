# Chapter 3: Data Structures

#* 1. Creating a Set
# Solution:
dna_bases = {'adenine', 'cytosine', 'guanine', 'thymine'}
print(dna_bases)


#* 2. Converting a List to a Set
rna_bases_list = ['adenine', 'cytosine', 'guanine', 'uracil', 'adenine']
# Solution:
unique_rna_bases = set(rna_bases_list)
print(unique_rna_bases)


#* 3. Adding and Removing Elements
test_bases = {'A', 'T', 'C', 'G'}
# Solution:
test_bases.add('U')
test_bases.remove('T')
print(test_bases)


#* 4. Using discard()
sample_bases = {'adenine', 'cytosine', 'guanine', 'thymine'}
# Solution:
sample_bases.discard('guanine')
sample_bases.discard('nonsense')
print(sample_bases)


#* 5. Clearing a Set
protein_bases = {'arginine', 'lysine', 'methionine'}
# Solution:
protein_bases.clear()
print(protein_bases)


#* 6. Set Operations with Lists
sequence_bases = ['A', 'C', 'G', 'T', 'A', 'G']
# Solution:
unique_sequence_bases = set(sequence_bases)
print(unique_sequence_bases)


#* 7. Set Uniqueness in Bioinformatics
sequences = ['ATCG', 'ATCG', 'GCTA', 'CGAT', 'ATCG']
# Solution:
unique_sequences = set(sequences)
print(unique_sequences)
