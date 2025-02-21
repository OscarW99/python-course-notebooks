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

#* 1. Computing Basic Statistics
df1 = pd.read_csv('data/health_records.csv')
stats1 = df1.describe()
print(stats1)

#* 2. Counting Conditions
data2 = {
    'Condition': ['Flu', 'Cold', 'Flu', 'Fever', 'Cold', 'Flu'],
    'Age': [25, 30, 45, 28, 35, 42]
}
df2 = pd.DataFrame(data2)
counts2 = df2['Condition'].value_counts()
print(counts2)

#* 3. Frequency of Blood Types
df3 = pd.read_csv('data/blood_type_records.csv')
blood_stats3 = df3['Blood_Type'].value_counts()
print(blood_stats3)

#* 4. Correlations Between Metrics
df4 = pd.read_csv('data/health_metrics.csv')
numerical_df4 = df4.select_dtypes(include=['number'])
correlations4 = numerical_df4.corr()
print(correlations4)

#* 5. Most Frequent Smoking Status
df5 = pd.read_csv('data/health_records.csv')
smoking_stats5 = df5['Smoking_Status'].value_counts()
print(f"Most frequent smoking status: {smoking_stats5.index[0]}, Frequency: {smoking_stats5.iloc[0]}")