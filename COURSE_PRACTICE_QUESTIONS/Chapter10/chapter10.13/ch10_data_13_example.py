# Chapter 9: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
mutations_df = pd.read_csv('data/genetic_variants.csv')

#* 1. Selecting High Impact Variants
impact_condition = (mutations_df['Pathogenicity_Score'] > 0.7) & (mutations_df['Frequency'] > 0.05)
high_impact_variants = mutations_df[impact_condition]
print(high_impact_variants)

#* 2. Selecting Chromosome 7 Mutations
type_condition = mutations_df['Mutation_Type'].isin(["Missense", "Frameshift"])
chr_condition = mutations_df['Chromosome'] == "7"
chr7_mutations_df = mutations_df[type_condition & chr_condition]
print(chr7_mutations_df)

#* 3. Selecting G Variants in a Specific Region
position_condition = (mutations_df['Position'] >= 100000) & (mutations_df['Position'] <= 200000)
ref_condition = mutations_df['Reference_Allele'] == "G"
g_variants_region = mutations_df[position_condition & ref_condition]
print(g_variants_region)

#* 4. Selecting Splice Variants
splice_pattern = mutations_df['Mutation_Type'].str.contains("splice", case=False)
path_condition = mutations_df['Pathogenicity_Score'] > 0.6
splice_variants = mutations_df[splice_pattern & path_condition]
print(splice_variants)

#* 5. Selecting Severe Variants
path_condition = mutations_df['Pathogenicity_Score'] > 0.8
freq_condition = mutations_df['Frequency'] > 0.01
type_condition = mutations_df['Mutation_Type'] == "Missense"
pos_condition = mutations_df['Position'] > 150000
severe_variants = mutations_df[path_condition & freq_condition & type_condition & pos_condition]
print(severe_variants)