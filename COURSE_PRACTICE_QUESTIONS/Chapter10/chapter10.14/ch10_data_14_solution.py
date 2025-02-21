# Chapter 9: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import numpy as np
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
protein_df = pd.read_csv('data/protein_analysis.csv')

#* 1. Categorizing Protein Size
def categorize_size(length):
    pass

#$ protein_df['Size_Category'] = 

#* 2. Normalizing Hydrophobicity
#$ protein_df['Normalized_Hydrophobicity'] = 

#* 3. Assessing Protein Viability
def assess_viability(row):
    pass

protein_df['Viability'] = protein_df.apply(assess_viability, axis=1)

#* 4. Categorizing Protein Location
def categorize_location(value):
    pass
    
#$ protein_df['Location_Type'] = 

#* 5. Classifying Protein Quality
def classify_protein(row):
    pass

protein_df['Protein_Quality'] = protein_df.apply(classify_protein, axis=1)