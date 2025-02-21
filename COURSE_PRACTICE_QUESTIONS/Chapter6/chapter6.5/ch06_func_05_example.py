# Chapter 4: Functions and Libraries

#* 1. Using any() and all()
enzyme_activities = [False, False, 0.05, 0.00, False]
sample_quality = [True, True, True, False, True]
any_significant_activity = any(enzyme_activities)
all_samples_pass = all(sample_quality)
print(f"Any significant activity: {any_significant_activity}")
print(f"All samples pass: {all_samples_pass}")

#* 2. Formatting Numbers
protein_concentration = 0.7654
mutation_rate = 0.0352
gene_expression = 45.6789
formatted_protein_concentration = format(protein_concentration, ".2f")
formatted_mutation_rate = format(mutation_rate, ".1%")
formatted_gene_expression = format(gene_expression, ".2E")
print(f"Protein concentration: {formatted_protein_concentration}")
print(f"Mutation rate: {formatted_mutation_rate}")
print(f"Gene expression: {formatted_gene_expression}")

#* 3. Working with Fragment Lengths
fragment_lengths = [150, 250, 300, 75, 200]
max_fragment_length = max(fragment_lengths)
formatted_max_length = format(max_fragment_length, ".1f")
any_long_fragment = any(length > 200 for length in fragment_lengths)
print(f"Max fragment length: {formatted_max_length}")
print(f"Any fragment longer than 200: {any_long_fragment}")
