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

#* 1. Computing Basic Statistics
#$ df1 = 
#$ stats1 = 

#* 2. Counting Conditions
data2 = {
    'Condition': ['Flu', 'Cold', 'Flu', 'Fever', 'Cold', 'Flu'],
    'Age': [25, 30, 45, 28, 35, 42]
}
df2 = pd.DataFrame(data2)
#$ counts2 = 

#* 3. Frequency of Blood Types
#$ df3 = 
#$ blood_stats3 = 

#* 4. Correlations Between Metrics
#$ df4 = 
#$ numerical_df4 = 
#$ correlations4 = 

#* 5. Most Frequent Smoking Status
#$ df5 = 
#$ smoking_stats5 =