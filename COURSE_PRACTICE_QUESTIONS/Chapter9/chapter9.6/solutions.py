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

#* 1. Reading CSV into DataFrame
#$ df1 = 

#* 2. Reading TSV into DataFrame
#$ df2 = 

#* 3. Reading JSON into DataFrame
#$ df3 = 

#* 4. Saving DataFrame to Different Formats
# Saving DataFrame to different formats
data = {
    'Gene': ['Gene1', 'Gene2', 'Gene3'],
    'Expression': [10.5, 8.2, 12.1]}
df4 = pd.DataFrame(data)
#$ df4.
#$ df4.