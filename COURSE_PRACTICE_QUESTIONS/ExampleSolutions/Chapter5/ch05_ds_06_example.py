# Chapter 5: Data Structures

#* 1. Appending to a List
enzymes = ['EcoRI', 'HindIII', 'BamHI']
enzymes.append('SmaI')
print(enzymes)


#* 2. Extending a List
nucleotides = ['A', 'T', 'C']
additional_nucleotides = ['G', 'U', 'A']
nucleotides.extend(additional_nucleotides)
print(nucleotides)


#* 3. Inserting into a List
amino_acids = ['Alanine', 'Cysteine', 'Glycine']
amino_acids.insert(1, 'Isoleucine')
print(amino_acids)


#* 4. Removing from a List
genes = ['GeneA', 'GeneB', 'GeneC', 'GeneD']
genes.remove('GeneC')
print(genes)


#* 5. Popping from a List
experimental_results = [32, 45, 22, 38, 55]
popped_result = experimental_results.pop(2)
print(popped_result)


#* 6. Using del with Lists
dna_sequence = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'C', 'A', 'T']
del dna_sequence[3:7]
print(dna_sequence)


#* 7. Clearing a List
dna_sequences = ['ATG', 'CGT', 'TAC', 'GCA']
dna_sequences.clear()
print(dna_sequences)


#* 8. Finding Index in a List
patient_ids = ['P100', 'P101', 'P102', 'P103']
index_p102 = patient_ids.index('P102')
print(index_p102)


#* 9. Counting Occurrences in a List
protein_sequence = ['Ala', 'Gly', 'Ala', 'Ser', 'Val', 'Ala', 'Ser']
count_ala = protein_sequence.count('Ala')
print(count_ala)


#* 10. Sorting a List
amino_acid_frequencies = [120, 200, 80, 150, 90]
amino_acid_frequencies.sort(reverse=True)
print(amino_acid_frequencies)


#* 11. Reversing a List
dna_sequence = ['A', 'T', 'G', 'C', 'A', 'T']
dna_sequence.reverse()
print(dna_sequence)


#* 12. Copying a List
dna_sequence = ['A', 'T', 'G', 'C', 'A', 'T']
dna_sequence_copy = dna_sequence.copy()
print(dna_sequence_copy)