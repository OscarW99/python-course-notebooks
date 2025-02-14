# Chapter 3: Data Structures



#* 1. Set Comprehension for Unique Nucleotides
dna_sequences = ['ATCG', 'GCTA', 'ATCG', 'TAGC']
# Solution:
unique_sequences = {nucleotide for sequence in dna_sequences for nucleotide in sequence}
print(unique_sequences)


#* 2. Set Comprehension for Heavy Proteins
protein_data = [('Albumin', 66.5), ('Insulin', 5.8), ('Hemoglobin', 64.5), ('Lysozyme', 14.3)]
# Solution:
heavy_proteins = {protein for protein, weight in protein_data if weight > 50}
print(heavy_proteins)


#* 3. Creating Nested Data Structures
data = (('Alanine', 89.1), ('Lysine', 146.2), ('Alanine', 89.1), ('Histidine', 155.2))
# Solution:
amino_list_tuples = list(data)
amino_tuple_sets = tuple({aa for aa in data})
amino_set_tuples = {aa for aa in data}
print(amino_list_tuples)
print(amino_tuple_sets)
print(amino_set_tuples)


#* 4. Gene Expression Analysis
gene_data = [('BRCA1', 120), ('TP53', 85), ('KRAS', 95), ('EGFR', 150)]
# Solution:
for gene, expression in gene_data:
    if expression > 100:
        print(f"{gene}: Highly expressed")
    else:
        print(f"{gene}: Lowly expressed")


#* 5. Set Comprehension for Low Expression Genes
# Solution:
low_expression_genes = {gene for gene, expression in gene_data if expression < 100}
print(low_expression_genes)
