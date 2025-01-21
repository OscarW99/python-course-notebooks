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

# Load datasets
mutations_df = pd.read_csv('data/mutations.csv')
clinical_df = pd.read_csv('data/clinical.csv')
protein_df = pd.read_csv('data/protein.csv')
pathway_df = pd.read_csv('data/pathway.csv')

#* 1. Grouping and Aggregating
# Use groupby() and mean() for expression levels
#$ mean_expression = 
# Use groupby() and size() for counts
#$ mutation_counts = 

#* 2. Creating and Melting a Pivot Table
# First create pivot table with index, columns, and values parameters
#$ pivot_result = 
# Then melt using id_vars parameter
#$ melted_result = 

#* 3. Merging DataFrames
# Use merge with 'how' parameter to keep all proteins and mutations
#$ mutations_proteins = 

#* 4. Joining DataFrames
# First select needed columns from each DataFrame
clinical_subset = clinical_df[['Treatment_Group', 'Response_Status']]
mutations_subset = mutations_df[['Mutation_Type', 'Gene_ID']]
# Then join using set_index and how='inner'
#$ joined_data = 

#* 5. Refining DataFrames
# Steps:
# 1. Merge protein_df and pathway_df
# 2. Use dropna with thresh parameter
# 3. Drop duplicates
# 4. Drop unwanted columns
#$ refined_proteins =