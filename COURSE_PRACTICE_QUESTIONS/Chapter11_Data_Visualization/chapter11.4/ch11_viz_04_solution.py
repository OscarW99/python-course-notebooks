# Chapter 11: Data Visualization

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
# Create and customize scatter plot
# Save in multiple formats