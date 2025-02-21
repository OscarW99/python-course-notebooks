# Chapter 3: Data Structures

#* 1. Accessing Elements in a Nested List
nucleotide_pairs = [['A', 'T'], ['C', 'G'], ['G', 'C']]
for pair in nucleotide_pairs:
    print(pair)

#* 2. Printing each nucleotide individually
for pair in nucleotide_pairs:
    for nucleotide in pair:
        print(nucleotide)
