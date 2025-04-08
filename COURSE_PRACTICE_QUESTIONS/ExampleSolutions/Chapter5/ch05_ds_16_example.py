# Chapter 5: Data Structures

#* 1. Working with Amino Acid Properties
amino_acids = {
    "Lysine": "Basic",
    "Alanine": "Nonpolar",
    "Histidine": "Basic",
    "Glycine": "Nonpolar"
}
# Print keys only
for amino_acid in amino_acids.keys():
    print(amino_acid)
# Print values only
for property in amino_acids.values():
    print(property)
# Print both
for amino_acid, property in amino_acids.items():
    print(f"Amino acid {amino_acid} is {property}")


#* 2. Finding High Expression Genes
expression_levels = {
    "BRCA1": 120,
    "TP53": 85,
    "KRAS": 95,
    "EGFR": 150
}
# Find high expression genes
for gene, expression in expression_levels.items():
    if expression > 100:
        print(gene)


#* 3. Filtering Protein Weights
protein_weights = {
    "Insulin": 5.8,
    "Albumin": 66.5,
    "Hemoglobin": 64.5,
    "Lysozyme": 14.3
}
# Create new dictionary with heavy proteins
heavy_proteins = {protein: weight for protein, weight in protein_weights.items() if weight > 20}
print(heavy_proteins)


#* 4. Working with Nested Protein Data
protein_data = {
    "Insulin": {"weight": 5.8, "function": "hormone"},
    "Albumin": {"weight": 66.5, "function": "transport"},
    "Hemoglobin": {"weight": 64.5, "function": "oxygen transport"}
}
# Print protein names and functions
for protein, data in protein_data.items():
    print(f"{protein}: {data['function']}")


#* 5. Comparing Metabolite Levels
morning_levels = {"glucose": 5.5, "lactate": 2.2, "pyruvate": 1.1}
evening_levels = {"glucose": 4.8, "lactate": 2.8, "pyruvate": 1.3}
# Compare metabolite levels
for metabolite, morning_value in morning_levels.items():
    evening_value = evening_levels[metabolite]
    if evening_value > morning_value:
        print(f"{metabolite} increased from {morning_value} to {evening_value}")
