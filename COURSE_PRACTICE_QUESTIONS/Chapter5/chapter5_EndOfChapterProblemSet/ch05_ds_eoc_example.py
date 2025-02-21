# Chapter 5: Data Structures

#* 1. List Manipulation
dna_sequences = ['ATCG', 'GCTA', 'TAGC', 'CAGT']
dna_sequences.append('ACGT')
dna_sequences.pop(1)
dna_sequences.insert(2, 'TGCA')
print(dna_sequences)


#* 2. Nested List Processing
gene_data = [['GeneA', 120], ['GeneB', 85], ['GeneC', 150]]
highest_expression_gene = max(gene_data, key=lambda x: x[1])[0]
average_expression = sum(gene[1] for gene in gene_data) / len(gene_data)
gene_names = [gene[0] for gene in gene_data]
print(f"Highest expression gene: {highest_expression_gene}")
print(f"Average expression level: {average_expression}")
print(f"Gene names: {gene_names}")


#* 3. Tuple Immutability Challenge
amino_acids = ('Alanine', 'Cysteine', 'Glycine')
try:
    amino_acids[1] = 'Valine'
except TypeError as e:
    print(f"Error: {e}")
amino_acids = amino_acids[:1] + ('Valine',) + amino_acids[2:]
print(amino_acids)


#* 4. Set Operations
gene_set1 = {'BRCA1', 'TP53', 'KRAS'}
gene_set2 = {'EGFR', 'KRAS', 'PIK3CA'}
intersection = gene_set1 & gene_set2
unique_genes = gene_set1 | gene_set2
is_brca1_present = 'BRCA1' in unique_genes
print(f"Intersection: {intersection}")
print(f"Unique genes: {unique_genes}")
print(f"Is BRCA1 present: {is_brca1_present}")


#* 5. Dictionary Creation and Manipulation
proteins = {
    'Insulin': {'weight': 5.8, 'function': 'hormone'},
    'Albumin': {'weight': 66.5, 'function': 'transport'}
}
proteins['Hemoglobin'] = {'weight': 64.5, 'function': 'oxygen transport'}
protein_names = list(proteins.keys())
insulin_function = proteins['Insulin']['function']
print(f"Protein names: {protein_names}")
print(f"Function of Insulin: {insulin_function}")


#* 6. String Method Applications
dna_sequence = "atgctagctatgctagct"
dna_sequence_upper = dna_sequence.upper()
a_count = dna_sequence_upper.count('A')
starts_with_atg = dna_sequence_upper.startswith('ATG')
replaced_sequence = dna_sequence_upper.replace('A', 'X')
print(f"Uppercase sequence: {dna_sequence_upper}")
print(f"Count of 'A': {a_count}")
print(f"Starts with 'ATG': {starts_with_atg}")
print(f"Replaced sequence: {replaced_sequence}")


#* 7. Nested Dictionary Exploration
experiment_data = {
    'Experiment1': {'temperature': 37, 'pH': 7.4, 'results': 'positive'},
    'Experiment2': {'temperature': 42, 'pH': 7.0, 'results': 'negative'}
}
for exp, data in experiment_data.items():
    print(f"{exp} results: {data['results']}")
high_temp_experiments = any(data['temperature'] > 40 for data in experiment_data.values())
experiment_data['Experiment3'] = {'temperature': 35, 'pH': 7.2, 'results': 'positive'}
print(f"Any experiment above 40 degrees: {high_temp_experiments}")
print(f"Updated experiment data: {experiment_data}")


#* 8. List Comprehension Challenge
expression_levels = [120, 85, 150, 95, 200]
high_expression_levels = [level for level in expression_levels if level > 100]
max_expression = max(expression_levels)
normalized_expression_levels = [level / max_expression for level in expression_levels]
print(f"High expression levels: {high_expression_levels}")
print(f"Normalized expression levels: {normalized_expression_levels}")


#* 9. Set Comprehension
dna_sequences = ['ATCG', 'GCTA', 'ATCG', 'TAGC']
unique_nucleotides = {nucleotide for seq in dna_sequences for nucleotide in seq}
print(f"Unique nucleotides: {unique_nucleotides}")


#* 10. Tuple Unpacking
gene_data = [('BRCA1', 150), ('TP53', 85), ('KRAS', 95)]
for gene, expression in gene_data:
    print(f"Gene: {gene}, Expression level: {expression}")
high_expression_genes = [gene for gene, expression in gene_data if expression > 100]
print(f"Genes with expression levels above 100: {high_expression_genes}")
