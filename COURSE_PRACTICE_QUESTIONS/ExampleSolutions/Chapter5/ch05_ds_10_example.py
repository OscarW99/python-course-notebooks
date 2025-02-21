# Chapter 5: Data Structures

#* 1. Creating a Tuple
# Solution:
codon = ('A', 'U', 'G')
print(codon)


#* 2. Accessing Tuple Elements
amino_acids = ('Alanine', 'Glycine', 'Serine')
# Solution:
print(amino_acids[1])


#* 3. Tuple to List Conversion
bases = ('A', 'T', 'C', 'G')
# Solution:
base_list = list(bases)
print(base_list)


#* 4. Nested Tuple Acces
rna_codons = (('AUG', 'Methionine'), ('UUU', 'Phenylalanine'), ('GGA', 'Glycine'))
# Solution:
for codon, amino_acid in rna_codons:
    if codon == 'UUU':
        print(amino_acid)


#* 5. Tuple Iteratio
proteins = ('Actin', 'Myosin', 'Tubulin')
# Solution:
for protein in proteins:
    print(protein)


#* 6. Tuple Unpackin
gene_info = ('GeneA', 'Chromosome 1', 'Human')
# Solution:
gene_name, chromosome, species = gene_info
print(gene_name, chromosome, species)


#* 7. Tuple Unpacking with Ignored Elemen
lab_results = ('Sample123', 'Positive', 10.5, 'mg/dL')
# Solution:
sample_id, result, value, _ = lab_results
print(sample_id, result, value)


#* 8. Converting and Modifyin
amino_acids = ('Alanine', 'Cysteine', 'Glycine')
# Solution:
amino_acid_list = list(amino_acids)
amino_acid_list.append('Serine')
amino_acids = tuple(amino_acid_list)
print(amino_acids)
