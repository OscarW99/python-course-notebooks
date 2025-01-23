# Chapter 10: Data Visualization

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
protein_data = pd.read_csv('data/protein_levels.csv')

#* 1. Histogram of Protein Expression Levels
plt.figure(figsize=(10, 6))
plt.hist(protein_data['expression_level'], bins=30, alpha=0.6, color='blue', edgecolor='black')
plt.xlabel('Protein Expression Level')
plt.ylabel('Frequency')
plt.title('Distribution of Protein Expression Levels')
plt.grid(linestyle='--')
plt.show()

#* 2. Density Plot of Expression Levels by Treatment
plt.figure(figsize=(10, 6))
sns.kdeplot(data=protein_data[protein_data['treatment'] == 'Control'], x='expression_level', color='blue', alpha=0.7, label='Control')
sns.kdeplot(data=protein_data[protein_data['treatment'] == 'Treatment'], x='expression_level', color='red', alpha=0.7, label='Treatment')
plt.xlabel('Protein Expression Level')
plt.ylabel('Density')
plt.title('Density Plot of Expression Levels by Treatment')
plt.legend()
plt.show()

#* 3. Boxplot of Expression Levels by Treatment
plt.figure(figsize=(10, 6))
sns.boxplot(x='treatment', y='expression_level', data=protein_data, palette={'Control': 'blue', 'Treatment': 'red'})
plt.title('Protein Expression by Treatment')
plt.xlabel('Treatment')
plt.ylabel('Protein Expression Level')
plt.show()