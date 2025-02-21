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
df = pd.read_csv('data/patient_records.csv', index_col='Patient_ID')
print(df.head())

#* 1. Extracting Age as Series
age_series = df['Age']
print(type(age_series))
print(age_series.head(3))

#* 2. Creating DataFrame with Blood Pressure and Cholesterol
vitals_df = df[['Blood_Pressure', 'Cholesterol']]
print(vitals_df)

#* 3. Extracting Data by Patient IDs
patient_subset = df.loc['P001':'P003']
print(patient_subset)

#* 4. Extracting First Three Rows
first_three = df.iloc[:3]
print(first_three)

#* 5. Extracting Specific Rows and Columns
measurements = df.iloc[1:4, [4, 5]]  # Note: Python indexing starts at 0
print(measurements)