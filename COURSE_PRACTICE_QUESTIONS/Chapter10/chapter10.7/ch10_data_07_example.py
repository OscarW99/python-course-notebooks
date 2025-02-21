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

#* 1. Reading CSV into DataFrame with Index
df = pd.read_csv('data/bio_study_data.csv', index_col='SampleID')
first_rows = df.head(3)
print(first_rows)

#* 2. Displaying DataFrame Information
info = df.info()
# info will print to console by default, no need to explicitly print

#* 3. Displaying Last Rows and Shape
last_rows = df.tail(4)
print(last_rows)
shape = df.shape
print(f"Shape of DataFrame: {shape}")