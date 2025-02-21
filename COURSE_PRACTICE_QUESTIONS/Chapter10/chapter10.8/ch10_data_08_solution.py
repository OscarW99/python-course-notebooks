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

#* 1. Identifying Duplicates
df1 = pd.read_csv('data/patient_data.csv')
#$ duplicates1 =

#* 2. Removing Duplicates - Keep First
data = {
    'ID': ['P1', 'P2', 'P1', 'P3', 'P2'],
    'Value': [100, 200, 100, 300, 200]
}
df2 = pd.DataFrame(data)
#$ no_duplicates_first =

#* 3. Removing All Duplicates
#$ no_duplicates_none =

#* 4. Removing Duplicates In-Place - Keep Last
df4 = pd.read_csv('data/measurements.csv')
#$ df4.

#* 5. Checking Number of Duplicates
#$ initial_shape =
#$ df_no_duplicates =
#$ final_shape =