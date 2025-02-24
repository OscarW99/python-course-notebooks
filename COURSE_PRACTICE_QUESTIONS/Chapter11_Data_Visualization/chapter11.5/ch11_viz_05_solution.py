# Chapter 11: Data Visualization

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
expression_data = pd.read_csv('data/gene_expression.csv')

#* 1. Creating 1x2 Subplots
# Create 1x2 subplot grid
# Add bar plot and line plot
# Customize labels and layout


#* 2. Creating 2x2 Subplots
# Create 2x2 subplot grid
# Add different plot types
# Add titles and labels


#* 3. Using GridSpec for Complex Layout
# Create GridSpec layout
# Add spanning plot and bottom plots
# Customize appearance