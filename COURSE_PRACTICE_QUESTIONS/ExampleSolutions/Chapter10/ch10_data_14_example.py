# Chapter 10: Data Manipulation

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
    if pd.isna(length):
        return "Unknown"
    elif length < 100:
        return "Small"
    elif length <= 500:
        return "Medium"
    else:
        return "Large"

protein_df['Size_Category'] = protein_df['Length'].apply(categorize_size)

#* 2. Normalizing Hydrophobicity
protein_df['Normalized_Hydrophobicity'] = protein_df['Hydrophobicity'].apply(lambda x: (x + 4.5) / 9 if not pd.isna(x) else np.nan)

#* 3. Assessing Protein Viability
def assess_viability(row):
    if pd.isna(row['Stability_Score']) or pd.isna(row['Expression_Level']):
        return "Insufficient Data"
    elif row['Stability_Score'] > 0.7 and row['Expression_Level'] > 50:
        return "High Viability"
    elif row['Stability_Score'] < 0.3 or row['Expression_Level'] < 10:
        return "Low Viability"
    else:
        return "Moderate Viability"

protein_df['Viability'] = protein_df.apply(assess_viability, axis=1)

#* 4. Categorizing Protein Location
def categorize_location(value):
    if pd.isna(value):
        return "Unknown"
    elif 'nucleus' in value.lower():
        return "Nuclear"
    elif 'membrane' in value.lower():
        return "Membrane"
    else:
        return "Other"

protein_df['Location_Type'] = protein_df['Cellular_Location'].apply(categorize_location)

#* 5. Classifying Protein Quality
def classify_protein(row):
    if pd.isna(row['Length']) or pd.isna(row['Stability_Score']) or pd.isna(row['Expression_Level']):
        return "Insufficient Data"
    elif row['Length'] > 200 and row['Stability_Score'] > 0.6 and row['Expression_Level'] > 40:
        return "High Quality"
    elif row['Length'] > 100 and row['Stability_Score'] > 0.4 and row['Expression_Level'] > 20:
        return "Medium Quality"
    else:
        return "Low Quality"

protein_df['Protein_Quality'] = protein_df.apply(classify_protein, axis=1)

print(protein_df)