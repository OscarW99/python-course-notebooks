# Chapter 10: Data Visualization

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
category_counts = gene_data['functional_category'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(category_counts, labels=[f"{cat}: {percent:.1f}%" for cat, percent in zip(category_counts.index, category_counts/category_counts.sum()*100)], autopct='', startangle=90)
plt.title('Distribution of Gene Numbers by Functional Category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

#* 2. Bar Chart of Functional Categories
plt.figure(figsize=(12, 6))
categories = category_counts.index
counts = category_counts.values
plt.bar(categories, counts, color='skyblue', edgecolor='black')
plt.xlabel('Functional Category')
plt.ylabel('Number of Genes')
plt.title('Number of Genes per Functional Category')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

#* 3. Line Graph of Gene Expression Over Time
tp53_data = gene_data[gene_data['gene_id'] == 'TP53']
time_points = ['expression_0h', 'expression_2h', 'expression_4h', 'expression_8h', 'expression_12h', 'expression_24h']
expression_values = tp53_data[time_points].values.flatten()
plt.figure(figsize=(10, 5))
plt.plot(time_points, expression_values, marker='o', linestyle='--', color='green')
plt.xlabel('Time Points (Hours)')
plt.ylabel('Expression Level')
plt.title('Expression Levels of TP53 Over Time')
plt.grid(True, linestyle='--')
plt.show()