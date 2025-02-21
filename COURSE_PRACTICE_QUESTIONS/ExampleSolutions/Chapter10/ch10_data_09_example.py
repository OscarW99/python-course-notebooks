# Chapter 10: Data Manipulation

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

#* 1. Viewing Column Names
df1 = pd.read_csv('data/samples.csv')
columns = df1.columns
print(columns)

#* 2. Renaming Columns
data2 = {
    'Patient_ID': [1, 2, 3],
    'Blood_Sugar': [120, 130, 140],
    'Age': [25, 30, 35]
}
df2 = pd.DataFrame(data2)
df2 = df2.rename(columns={'Patient_ID': 'id', 'Blood_Sugar': 'glucose'})
print(df2.columns)

#* 3. Converting Column Names to Lowercase
data3 = {
    'Sample_ID': ['A1', 'A2', 'A3'],
    'Test_Result': ['+', '-', '+'],
    'Sample_Date': ['2023-01-01', '2023-01-02', '2023-01-03']
}
df3 = pd.DataFrame(data3)
df3.columns = [col.lower() for col in df3.columns]
print(df3.columns)