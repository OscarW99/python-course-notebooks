# Chapter 10: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import numpy as np
import pandas as pd
from Bio import SeqIO, NCBIWWW, NCBIXML
from Bio.Seq import Seq
from scipy import stats
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Using NumPy for Gene Expression Analysis
expression_values = np.array([2.1, 4.2, 1.5, 3.8, 2.9])
mean_expression = np.mean(expression_values)
above_mean = expression_values > mean_expression
normalized_values = (expression_values - expression_values.min()) / (expression_values.max() - expression_values.min())
print("Mean Expression:", mean_expression)
print("Values Above Mean:", expression_values[above_mean])
print("Normalized Values:", normalized_values)

#* 2. Analyzing Patient Response Data with Pandas
df = pd.read_csv('data/patient_records.csv')
response_rates = df.groupby('Treatment')['Response'].value_counts(normalize=True).unstack().fillna(0)['Yes'].sort_values(ascending=False)
print("Response Rates:\n", response_rates)

#* 3. Processing DNA Sequences with BioPython
sequences = SeqIO.parse('data/dna_sequences.fasta', 'fasta')
lengths = {record.id: len(record.seq) for record in sequences}
for seq_id, seq_len in lengths.items():
    print(f"{seq_id}: Length = {seq_len}")
longest = max(lengths, key=lengths.get)
print("Longest Sequence:", longest, "with length", lengths[longest])

#* 4. Protein Expression Analysis with Pandas
protein_df = pd.read_csv('data/protein_expression.csv')
control_mean = protein_df[['Control_1', 'Control_2']].mean(axis=1)
treatment_mean = protein_df[['Treatment_1', 'Treatment_2']].mean(axis=1)
fold_changes = treatment_mean / control_mean
proteins_high_fold = protein_df.loc[fold_changes > 1.5, 'Protein_ID']
print("Proteins with High Fold Change:", proteins_high_fold.tolist())

#* 5. Gene Expression Statistics with NumPy
expression_matrix = np.loadtxt('data/expression_matrix.txt')
gene_means = np.mean(expression_matrix, axis=1)
sample_means = np.mean(expression_matrix, axis=0)
gene_stds = np.std(expression_matrix, axis=1)
z_scores = (expression_matrix - gene_means[:, np.newaxis]) / gene_stds[:, np.newaxis]
print("Gene Means:", gene_means)
print("Sample Means:", sample_means)
print("Gene Standard Deviations:", gene_stds)
print("Z-Scores:\n", z_scores)

#* 6. Protein Sequence Analysis with BioPython
sequences = []
for record in SeqIO.parse('data/protein_sequences.fasta', 'fasta'):
    rna_seq = record.seq.transcribe()
    mol_weight = rna_seq.molecular_weight()
    if mol_weight > 10000:  # Note: This is just for demonstration; weights are usually much lower for proteins
        sequences.append(record)
SeqIO.write(sequences, 'output/high_mass_proteins.fasta', 'fasta')

#* 7. Clinical Trials Data Analysis with Pandas
trials_df = pd.read_csv('data/clinical_trials.csv')
cleaned_df = trials_df.fillna({'Blood_Pressure': trials_df['Blood_Pressure'].mode()[0], 'Cholesterol': trials_df['Cholesterol'].mean()})
age_groups = pd.cut(cleaned_df['Age'], bins=[0, 30, 50, 70, np.inf], labels=['0-30', '31-50', '51-70', '71+'])
success_rates = cleaned_df.groupby(age_groups)['Outcome'].apply(lambda x: (x == 'Success').mean())
success_rates.to_csv('output/age_group_analysis.csv')
print("Success Rates by Age Group:\n", success_rates)

#* 8. Sequence BLAST Analysis with BioPython
with open('data/query.fasta') as query_handle:
    query_sequence = query_handle.read()
    result_handle = NCBIWWW.qblast("blastn", "nr", query_sequence)
    blast_results = NCBIXML.parse(result_handle)
    hits = []
    for record in blast_results:
        for alignment in record.alignments[:5]:
            for hsp in alignment.hsps[:1]:  # Only take the first HSP for simplicity
                hits.append({
                    'Hit_ID': alignment.hit_id, 
                    'E-value': hsp.expect, 
                    'Identity': hsp.identities / hsp.align_length, 
                    'Coverage': hsp.align_length / len(query_sequence)
                })
    result_handle.close()
blast_df = pd.DataFrame(hits)
print("BLAST Results:\n", blast_df)

#* 9. Time Series Gene Expression Analysis
time_series_df = pd.read_csv('data/time_series_expression.csv')
rates = time_series_df.iloc[:, 1:].diff(axis=1)
increasing = np.all(rates > 0, axis=1)
decreasing = np.all(rates < 0, axis=1)
summary = pd.DataFrame({
    'Gene': time_series_df['Gene'],
    'Trend': np.where(increasing, 'Increasing', np.where(decreasing, 'Decreasing', 'Variable'))
})
print("Time Series Trend Summary:\n", summary)

#* 10. Statistical Analysis with SciPy
variant_sequences = SeqIO.parse('data/variants.fasta', 'fasta')
gc_contents = [{'Patient_ID': seq_record.id, 'GC_Content': Seq(seq_record.seq).gc()} for seq_record in variant_sequences]
gc_df = pd.DataFrame(gc_contents)

patient_df = pd.read_csv('data/patient_data.csv')
merged_data = pd.merge(patient_df, gc_df, on='Patient_ID')

control_group = merged_data[merged_data['Group'] == 'Control']['GC_Content']
treatment_group = merged_data[merged_data['Group'] == 'Treatment']['GC_Content']

t_statistic, p_value = stats.ttest_ind(control_group, treatment_group)

print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("There's a statistically significant difference in GC content between the groups.")
else:
    print("There's no significant difference in GC content between the groups.")