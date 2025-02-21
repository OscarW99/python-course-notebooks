# Chapter 11: Data Visualization

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Scatter Plot Visualization of Gene Expression
# Load data for scatter plot
# Create scatter plot with transparency
# Add labels and title
# Save plot

#* 2. Diverging Bar Plot for Disease Outcomes
# Calculate treatment response deviations
# Create diverging bar plot
# Save plot

#* 3. Lollipop Chart for Gene Frequency
# Prepare data for lollipop chart
# Sort and plot
# Add custom background color
# Save plot

#* 4. Histogram of Protein Lengths
# Create histogram with gradient color
# Add custom title font

#* 5. Density Plot for Patient Ages
# Split data by disease
# Create density plots with different colors
# Add legend

#* 6. Boxplot for Gene Expression by Condition
# Prepare data for boxplot
# Plot boxplot with custom palette
# Save plot

#* 7. Pie Chart for Disease Distribution
# Count disease types
# Plot pie chart with percentages and explode effect
# Save plot

#* 8. Bar Chart of Treatment Responses
# Count responses
# Create bar chart with grid lines

#* 9. Line Graph for Time Series Data
# Filter for TP53 gene
# Plot time series with markers and fill_between

#* 10. Heatmap Visualization of Gene Expression
# Step 1: Read gene expression data
gene_expression_df = pd.read_csv('data/gene_expression.csv', index_col=0)  # Assuming the first column is gene names

# Step 2: Prepare data for heatmap
# Here, we're choosing to visualize expression across samples
# You might want to normalize data first, but for simplicity, we'll use raw values
#$ heatmap_data = 

# Step 3: Create the heatmap with clustering
#$ plt.figure(figsize=(10, 10))
#$ sns.clustermap(

# Step 4: Customize the heatmap
#$ plt.title()

# Step 5: Save the plot
#$ plt.savefig(