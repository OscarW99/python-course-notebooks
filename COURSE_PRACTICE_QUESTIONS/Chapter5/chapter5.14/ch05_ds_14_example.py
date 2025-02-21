# Chapter 3: Data Structures

#* 1. Creating Protein Weight Dictionary
# Question 1 Solution
protein_weights = {
    'Insulin': 5.8,
    'Albumin': 66.5,
    'Hemoglobin': 64.5
}
print(protein_weights)


#* 2. Accessing Dictionary Elements
# Question 2 Solution
albumin_weight = protein_weights['Albumin']
print(albumin_weight)
myoglobin_weight = protein_weights.get('Myoglobin', 'Protein not found')
print(myoglobin_weight)


#* 3. Counting Nucleotides
# Question 3 Solution
sequence = "AATCGGCTAA"
dna_counts = {}
for nucleotide in sequence:
    if nucleotide in dna_counts:
        dna_counts[nucleotide] += 1
    else:
        dna_counts[nucleotide] = 1
print(dna_counts)


#* 4. Accessing Gene Expression Data
# Question 4 Solution
expression_data = {"BRCA1": 150, "TP53": 85, "KRAS": 95, "EGFR": 120}

# Using square brackets
try:
    mdm2_expression = expression_data['MDM2']
except KeyError:
    mdm2_expression = 'Protein not found'
print(mdm2_expression)

# Using get() method
mdm2_expression = expression_data.get('MDM2', 'Protein not found')
print(mdm2_expression)


#* 5. Creating a Complex Protein Dictionary
# Question 5 Solution
protein_info = {
    'Insulin': [5.8, 'Hormone'],
    'Albumin': [66.5, 'Transport'],
    'Hemoglobin': [64.5, 'Oxygen carrier']
}
print(protein_info)
