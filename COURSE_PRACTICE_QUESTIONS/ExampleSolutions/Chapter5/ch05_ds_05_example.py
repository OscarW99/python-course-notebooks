# Chapter 5: Data Structures

#* 1. Simple Unpacking
amino_acids = ['Alanine', 'Cysteine', 'Glycine']
# Solution:
ala, cys, gly = amino_acids
print(ala, cys, gly)


#* 2. Nested List Unpacking
gene_info = [['Gene1', 150], ['Gene2', 200], ['Gene3', 250]]
# Solution:
for gene, expression in gene_info:
    print(gene, expression)


#* 3. Unpacking with Star Expressions
gene_details = ['GeneX', 'Regulatory', 'Human', 120, 'Chromosome 1']
# Solution:
gene, gene_type, *details = gene_details
print(gene, gene_type, details)


#* 4. Unpacking a String
dna_sequence = "AGTC"
# Solution:
a, t, c, g = dna_sequence
print(a, t, c, g)
