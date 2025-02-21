# Chapter 3: Data Structures

#* 1. Extracting a Subsequence
dna_sequence = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C', 'A', 'T']
# Solution:
subsequence = dna_sequence[2:8]
print(subsequence)


#* 2. Reversing a Sequence
amino_acids = ['Alanine', 'Cysteine', 'Glycine', 'Isoleucine']
# Solution:
reversed_amino_acids = amino_acids[::-1]
print(reversed_amino_acids)


#* 3. Extracting Odd Indexed Elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Solution:
odd_indexed_elements = numbers[1::2]
print(odd_indexed_elements)


#* 4. Slicing in Nested Lists
patient_records = [['ID1', 23, 'A+'], ['ID2', 35, 'B-'], ['ID3', 42, 'O+']]
# Solution:
for record in patient_records:
    print(record[0], record[1])
