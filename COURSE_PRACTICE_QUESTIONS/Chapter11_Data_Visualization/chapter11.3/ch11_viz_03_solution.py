# Chapter 11: Data Visualization

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
gene_data = pd.read_csv('data/gene_categories.csv')

#* 1. Pie Chart of Functional Categories
# Calculate category frequencies
# Create pie chart with percentages
# Add title

#* 2. Bar Chart of Functional Categories
# Create bar chart
# Add labels and rotate x-axis
# Add grid

#* 3. Line Graph of Gene Expression Over Time
# Create line graph
# Add markers and customize line
# Add labels