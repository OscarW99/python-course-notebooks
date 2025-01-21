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

#* 1. Identifying Missing Values
#$ df1 = 
#$ missing = 

#* 2. Removing Rows with Missing Values
data2 = {
    'Patient': ['P1', 'P2', 'P3', 'P4'],
    'Age': [25, None, 35, 28],
    'Status': ['Positive', 'Negative', None, 'Positive']
}
#$ df2 = 
#$ clean_df2 = 

#* 3. Filling Missing Numerical Values with Mean
#$ df3 = 
#$ numerical_cols = 

#* 4. Filling Missing Categorical Values with Mode
#$ df4 = 
#$ mode = 

#* 5. Comparing DataFrame Shapes Before and After Dropping Missing Values
#$ df5 = 
#$ before = 
#$ after = 