# Chapter 10: Data Visualization

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import matplotlib.pyplot as plt
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
clinical_data = pd.read_csv('data/clinical_data.csv')

#* 1. Scatter Plot of Age vs BMI
plt.figure(figsize=(10, 6))
plt.scatter(clinical_data['Age'], clinical_data['BMI'], alpha=0.5, color='blue')
plt.title('Age vs BMI Scatter Plot')
plt.xlabel('Age (Years)')
plt.ylabel('BMI')
plt.grid(linestyle='--')
plt.savefig('output/age_vs_bmi.png', dpi=300, bbox_inches='tight')
plt.savefig('output/age_vs_bmi.pdf', bbox_inches='tight')
plt.show()