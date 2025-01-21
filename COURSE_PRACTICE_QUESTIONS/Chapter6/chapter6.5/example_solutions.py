# Chapter 6: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/gene_expression.csv"
# Windows: "data\\gene_expression.csv" or r"data\gene_expression.csv"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Reading a CSV File
df = pd.read_csv('data/gene_expression.csv')
print(df.head())

#* 2. Filtering Data and Writing to CSV
df_filtered = df[df['Fold_Change'] > 2]
df_filtered.to_csv('output/upregulated_genes.csv', index=False)

#* 3. Reading TSV and Calculating Average Age
patient_df = pd.read_csv('data/patient_data.tsv', sep='\t')
average_age = patient_df['Age'].mean()
print(f"Average age of patients: {average_age}")

#* 4. Creating and Writing DataFrame
data = {
    'Protein': ['P53', 'BRCA1', 'EGFR', 'TNF', 'IL6'],
    'Expression': [0.8, 1.2, 1.5, 0.6, 1.1]
}

protein_df = pd.DataFrame(data)
print(protein_df.head())
protein_df.to_csv('output/protein_expression.tsv', sep='\t', index=False)