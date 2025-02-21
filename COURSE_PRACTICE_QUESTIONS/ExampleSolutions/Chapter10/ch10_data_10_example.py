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

#* 1. Identifying Missing Values
df1 = pd.read_csv('data/medical_records.csv')
missing = df1.isna().sum()
print(missing)

#* 2. Removing Rows with Missing Values
data2 = {
    'Patient': ['P1', 'P2', 'P3', 'P4'],
    'Age': [25, None, 35, 28],
    'Status': ['Positive', 'Negative', None, 'Positive']
}
df2 = pd.DataFrame(data2)
clean_df2 = df2.dropna()
print(clean_df2)

#* 3. Filling Missing Numerical Values with Mean
df3 = pd.read_csv('data/patient_vitals.csv')
numerical_cols = df3.select_dtypes(exclude=['object']).columns
df3[numerical_cols] = df3[numerical_cols].fillna(df3[numerical_cols].mean())
print(df3)

#* 4. Filling Missing Categorical Values with Mode
df4 = pd.read_csv('data/blood_samples.csv')
mode = df4['Blood_Type'].mode()[0]
df4['Blood_Type'] = df4['Blood_Type'].fillna(mode)
print(df4)

#* 5. Comparing DataFrame Shapes Before and After Dropping Missing Values
df5 = pd.read_csv('data/test_results.csv')
before = df5.shape
after = df5.dropna().shape
print(f"Shape Before: {before}")
print(f"Shape After: {after}")