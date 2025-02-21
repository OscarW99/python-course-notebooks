# Chapter 10: Data Visualization

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
protein_data = pd.read_csv('data/protein_levels.csv')

#* 1. Histogram of Protein Expression Levels
# Create histogram of expression levels
# Add labels and title
# Customize appearance with alpha and grid

#* 2. Density Plot of Expression Levels by Treatment
# Split data by treatment
# Create density plots
# Add legend and labels

#* 3. Boxplot of Expression Levels by Treatment
# Create boxplot
# Add title and labels
# Customize colors