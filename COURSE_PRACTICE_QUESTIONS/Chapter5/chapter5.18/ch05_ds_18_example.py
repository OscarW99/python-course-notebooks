# Chapter 3: Data Structures

#* 1. Converting Protein Weights
protein_weights = {"Insulin": 5.8, "Albumin": 66.5, "Hemoglobin": 64.5, "Lysozyme": 14.3}
protein_weights_da = {protein: weight * 1000 for protein, weight in protein_weights.items()}
print(protein_weights_da)


#* 2. Processing Gene Expression Data
expression_data = {"BRCA1": 150, "TP53": 85, "KRAS": 95, "EGFR": 120}
high_expression = {gene: expression for gene, expression in expression_data.items() if expression > 100}
print(high_expression)
max_expression = max(expression_data.values())
normalized_expression = {gene: expression / max_expression for gene, expression in expression_data.items()}
print(normalized_expression)


#* 3. Filtering DNA Sequences
sequences = {"seq1": "ATCG", "seq2": "GCTA", "seq3": "TTAGCT", "seq4": "CG"}
long_sequences = {seq: sequence for seq, sequence in sequences.items() if len(sequence) > 3}
print(long_sequences)


#* 4. Filtering Amino Acids
amino_acids = {"Lysine": "Basic", "Alanine": "Nonpolar", "Histidine": "Basic", "Glycine": "Nonpolar"}
basic_amino_acids = {amino_acid: property for amino_acid, property in amino_acids.items() if property == "Basic"}
print(basic_amino_acids)


#* 5. Temperature Conversion
celsius_temps = {"Morning": 15, "Noon": 25, "Evening": 20, "Night": 10}
fahrenheit_temps = {time: temp * 9/5 + 32 for time, temp in celsius_temps.items()}
print(fahrenheit_temps)
