# Chapter 5: Data Structures

#* 1. Creating a New List of Squares
numbers = [1, 2, 3, 4, 5]
# Solution:
squares = [x**2 for x in numbers]
print(squares)


#* 2. Filtering Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Solution:
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


#* 3. Finding Sequences with Specific End Nucleotides
dna_sequences = ['ATCG', 'GCTA', 'CGTA', 'ATC', 'TAT', 'ATGGCT']
# Solution:
sequences_ending_in_A = [seq for seq in dna_sequences if seq.endswith('A')]
print(sequences_ending_in_A)


#* 4. Concatenating Strings in a List
genes = ['Gene1', 'Gene2', 'Gene3']
# Solution:
prefixed_genes = ['ID-' + gene for gene in genes]
print(prefixed_genes)
