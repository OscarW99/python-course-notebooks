# Chapter 10: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd

# Load datasets
mutations_df = pd.read_csv('data/mutations.csv')
clinical_df = pd.read_csv('data/clinical.csv')
protein_df = pd.read_csv('data/protein.csv')
pathway_df = pd.read_csv('data/pathway.csv')

#* 1. Grouping and Aggregating
mean_expression = mutations_df.groupby(['Chromosome', 'Mutation_Type'])['Expression_Level'].mean()
mutation_counts = mutations_df.groupby('Chromosome').size().rename('Mutation_Count')

#* 2. Creating and Melting a Pivot Table
pivot_result = pathway_df.pivot_table(index='Category', columns='Pathway', values='Number_of_Genes', fill_value=0)
melted_result = pivot_result.reset_index().melt(id_vars='Category', var_name='Pathway', value_name='Gene_Count')

#* 3. Merging DataFrames
mutations_proteins = pd.merge(protein_df, mutations_df, on='Gene_ID', how='left')

#* 4. Joining DataFrames
clinical_subset = clinical_df[['Treatment_Group', 'Response_Status']].set_index(clinical_df['Patient_ID'])
mutations_subset = mutations_df[['Mutation_Type', 'Gene_ID']].set_index(mutations_df['Patient_ID'])
joined_data = clinical_subset.join(mutations_subset, how='inner').reset_index()

#* 5. Refining DataFrames
merged_df = pd.merge(protein_df, pathway_df, on='Pathway', how='left')
thresh = len(merged_df) * 0.5
refined_proteins = merged_df.dropna(thresh=thresh, axis=1).drop_duplicates(subset='Protein_ID', keep='first').drop('Category', axis=1)