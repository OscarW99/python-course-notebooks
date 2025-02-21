# Chapter 7: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.csv"
# Windows: "data\\example.csv" or r"data\example.csv"
# Python generally handles forward slashes (/) well on all platforms.

import csv
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Reading a CSV File
with open('data/example.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip the header row
    for i, row in enumerate(reader):
        if i < 5:
            print(row[0], row[2])  # Assuming Gene ID is in the first column and Expr B in the third
        else:
            break

#* 2. Writing to a TSV File
gene_data = [
    ["Gene1", 2.5, 3.7],
    ["Gene2", 4.2, 2.0],
    ["Gene3", 1.2, 1.2]
]

with open('output/gene_expression.tsv', 'w', newline='') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    for gene in gene_data:
        writer.writerow(gene)

#* 3. Skipping Headers and Calculating Average Expression
with open('data/example.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip the header row
    for row in reader:
        expr_a = float(row[1])  # Assuming Expr A is in the second column
        expr_b = float(row[2])  # Assuming Expr B is in the third column
        avg_expr = (expr_a + expr_b) / 2
        print(row[0], avg_expr)  # Assuming Gene ID is in the first column

#* 4. Filtering Rows and Writing to a New File
with open('data/example.tsv', 'r') as infile, open('output/upregulated_genes.tsv', 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter='\t')
    writer = csv.writer(outfile, delimiter='\t')
    
    headers = next(reader)  # Skip and capture the header
    writer.writerow(headers)  # Write the header to the output file
    for row in reader:
        if row[3] == 'Up':  # Assuming Notes column is in the fourth position
            writer.writerow(row)