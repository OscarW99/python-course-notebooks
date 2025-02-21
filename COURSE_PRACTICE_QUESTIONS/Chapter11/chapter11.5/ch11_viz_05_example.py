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
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Left subplot: Bar plot
mean_expression = expression_data.groupby('tissue_type')['expression_level'].mean()
mean_expression.plot(kind='bar', ax=ax1)
ax1.set_title('Mean Expression by Tissue Type')
ax1.set_xlabel('Tissue Type')
ax1.set_ylabel('Mean Expression Level')

# Right subplot: Line plot for BRCA1
brca1_data = expression_data[expression_data['gene_id'] == 'BRCA1']
for tissue, group in brca1_data.groupby('tissue_type'):
    group.pivot(index='time_point', columns='tissue_type', values='expression_level').plot(ax=ax2, label=tissue)
ax2.set_title('Expression Over Time for BRCA1 Gene')
ax2.set_xlabel('Time Point')
ax2.set_ylabel('Expression Level')
ax2.legend(title='Tissue Type')

plt.tight_layout()
plt.show()

#* 2. Creating 2x2 Subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Bar plot
expression_data.groupby('gene_id')['expression_level'].mean().plot(kind='bar', ax=axs[0, 0])
axs[0, 0].set_title('Mean Expression by Gene')
axs[0, 0].set_xlabel('Gene ID')
axs[0, 0].set_ylabel('Expression Level')

# Scatter plot
scatter = axs[0, 1].scatter(expression_data['time_point'], expression_data['expression_level'], c=expression_data['gene_id'].astype('category').cat.codes, cmap='viridis')
axs[0, 1].set_title('Expression vs Time')
axs[0, 1].set_xlabel('Time Point')
axs[0, 1].set_ylabel('Expression Level')
gene_ids = expression_data['gene_id'].astype('category').cat.categories
handles, _ = scatter.legend_elements()
axs[0, 1].legend(handles, gene_ids, title='Gene ID')

# Pie chart
gene_counts = expression_data['gene_id'].value_counts()
axs[1, 0].pie(gene_counts, labels=gene_counts.index, autopct='%1.1f%%')
axs[1, 0].set_title('Gene Distribution')

# Line plot
for gene, group in expression_data.groupby('gene_id'):
    group.pivot_table(index='time_point', columns='gene_id', values='expression_level', aggfunc='mean').plot(ax=axs[1, 1], label=gene)
axs[1, 1].set_title('Expression Over Time by Gene')
axs[1, 1].set_xlabel('Time Point')
axs[1, 1].set_ylabel('Expression Level')
axs[1, 1].legend(title='Gene ID')

plt.tight_layout()
plt.show()

#* 3. Using GridSpec for Complex Layout
fig = plt.figure(figsize=(10, 8))
gs = GridSpec(2, 2, figure=fig)

# Top plot spanning all columns
ax1 = fig.add_subplot(gs[0, :])

# Aggregate the data to ensure unique combinations of time_point and gene_id
aggregated_data = expression_data.groupby(['time_point', 'gene_id']).agg({'expression_level': 'mean'}).reset_index()

# Pivot the aggregated data
pivot_data = aggregated_data.pivot(index='time_point', columns='gene_id', values='expression_level')

# Plot the pivoted data
pivot_data.plot(ax=ax1)
ax1.set_title('Expression Over Time for All Genes')
ax1.set_xlabel('Time Point')
ax1.set_ylabel('Expression Level')

# Bottom left plot
ax2 = fig.add_subplot(gs[1, 0])
control_data = expression_data[expression_data['condition'] == 'control']
control_data.groupby('tissue_type')['expression_level'].mean().plot(kind='bar', ax=ax2, color='skyblue')
ax2.set_title('Mean Expression in Control Condition by Tissue')
ax2.set_xlabel('Tissue Type')
ax2.set_ylabel('Mean Expression Level')

# Bottom right plot
ax3 = fig.add_subplot(gs[1, 1])
treated_data = expression_data[expression_data['condition'] == 'treated']
treated_data.groupby('tissue_type')['expression_level'].mean().plot(kind='bar', ax=ax3, color='lightcoral')
ax3.set_title('Mean Expression in Treated Condition by Tissue')
ax3.set_xlabel('Tissue Type')
ax3.set_ylabel('Mean Expression Level')

plt.tight_layout()
plt.show()