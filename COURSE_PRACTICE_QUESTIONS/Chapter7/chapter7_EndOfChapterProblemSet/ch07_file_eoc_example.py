# Chapter 6: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import os
import csv
from datetime import date

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))        

#* 1. Listing FASTA Files
sequences_path = "data/sequences"
fasta_files = [f for f in os.listdir(sequences_path) if f.endswith('.fasta')]
print("FASTA files:", fasta_files)

#* 2. Extracting Differential Genes
with open('data/gene_expression_2024.csv', 'r', newline='') as infile, open('output/differential_genes.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    headers = next(reader)
    writer.writerow(headers)
    for row in reader:
        if row[3] == 'Yes':
            writer.writerow(row)

#* 3. Appending to Log File
today = date.today()
today_string = today.strftime("%Y-%m-%d")
with open('data/experiment_log.txt', 'a') as log_file:
    log_file.write(f"\n{today_string} - Data analysis completed")

#* 4. Combining Patient Data Files
with open('output/combined_patient_data.tsv', 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter='\t')
    with open('data/patient_data_batch1.tsv', 'r', newline='') as batch1:
        reader = csv.reader(batch1, delimiter='\t')
        headers = next(reader)
        writer.writerow(headers)
        writer.writerows(reader)
    with open('data/patient_data_batch2.tsv', 'r', newline='') as batch2:
        reader = csv.reader(batch2, delimiter='\t')
        next(reader)  # Skip header
        writer.writerows(reader)

#* 5. Creating Subdirectories
results_path = 'output/results'
if not os.path.exists(results_path):
    os.makedirs(results_path)
for subdir in ['raw', 'processed', 'final']:
    os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

#* 6. Counting Sequences in FASTA
sequence_count = 0
with open('data/sequence_data.fasta', 'r') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            sequence_count += 1
print(f"Number of sequences: {sequence_count}")

#* 7. Cleaning Genotype Data
with open('data/genotype_data.csv', 'r', newline='') as infile, open('output/cleaned_genotype_data.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        cleaned_row = [val if val != 'NA' else '0' for val in row]
        writer.writerow(cleaned_row)

#* 8. Calculating Average Molecular Weight
total_weight = 0
count = 0
with open('data/protein_weights.txt', 'r') as infile:
    for line in infile:
        protein, weight = line.strip().split('\t')
        total_weight += float(weight)
        count += 1
avg_weight = total_weight / count if count else 0
with open('data/protein_weights.txt', 'a') as outfile:
    outfile.write(f"\nAverage Molecular Weight: {avg_weight}")

#* 9. Archiving Old Records
import time
archive_path = 'data/archive'
os.makedirs(archive_path, exist_ok=True)
for filename in os.listdir('data/old_records'):
    file_path = os.path.join('data/old_records', filename)
    if time.gmtime(os.path.getmtime(file_path)).tm_year < 2024:
        os.rename(file_path, os.path.join(archive_path, filename))

#* 10. Gene Names to Uppercase with Numbering
with open('data/gene_names.txt', 'r') as infile, open('output/gene_names_uppercase.txt', 'w') as outfile:
    for i, line in enumerate(infile, 1):
        outfile.write(f"{i}: {line.strip().upper()}\n")