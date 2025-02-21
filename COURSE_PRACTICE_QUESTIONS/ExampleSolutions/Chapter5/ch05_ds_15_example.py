# Chapter 5: Data Structures

#* 1. Working with Protein Levels
protein_levels = {"Insulin": 45.6, "Albumin": 82.3, "Fibrinogen": 63.7}
# Solution:
proteins = list(protein_levels.keys())
concentrations = list(protein_levels.values())
protein_concentration_pairs = list(protein_levels.items())
print(proteins)
print(concentrations)
print(protein_concentration_pairs)


#* 2. Manipulating Gene Expression Dictionary
expression = {"BRCA1": 150, "TP53": 85, "KRAS": 95}
# Solution:
# Add EGFR
expression.update({"EGFR": 120})
print(expression)

# Remove and print last item
last_item = expression.popitem()
print(last_item)

# Remove and print TP53 expression
TP53_expression = expression.pop("TP53")
print(TP53_expression)


#* 3. Combining Metabolite Data
metabolites_1 = {"glucose": 5.5, "lactate": 2.2, "pyruvate": 1.1}
metabolites_2 = {"lactate": 2.5, "pyruvate": 1.3, "citrate": 0.9}
# Solution:
# Combine dictionaries
metabolites_1.update(metabolites_2)
print(metabolites_1)


#* 4. DNA Motifs Dictionary Operations
dna_motifs = {
    "TATA": "promoter",
    "AAGCTT": "restriction site",
    "GCGC": "methylation site"
}
# Solution:
# Print keys
print(dna_motifs.keys())

# Print values
print(dna_motifs.values())

# Clear dictionary
dna_motifs.clear()
print(dna_motifs)


#* 5. Nested Dictionary Operations
protein_data = {
    "Insulin": {"weight": 5.8, "function": "hormone"},
    "Albumin": {"weight": 66.5, "function": "transport"},
    "Hemoglobin": {"weight": 64.5, "function": "oxygen transport"}
}
# Solution:
protein_names = list(protein_data.keys())
protein_weights = [data["weight"] for data in protein_data.values()]
albumin_data = protein_data.pop("Albumin")
print(protein_names)
print(protein_weights)
print(albumin_data)
