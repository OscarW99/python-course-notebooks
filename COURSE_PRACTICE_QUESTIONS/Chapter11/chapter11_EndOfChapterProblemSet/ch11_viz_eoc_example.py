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
import numpy as np
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Scatter Plot Visualization of Gene Expression
data = pd.read_csv('data/gene_expression.csv')
time_0 = data[data['time_point'] == 0]
time_24 = data[data['time_point'] == 24]

plt.figure(figsize=(10, 6))
plt.scatter(time_0['expression_level'], time_24['expression_level'], alpha=0.5)
plt.xlabel('Expression at 0 hours')
plt.ylabel('Expression at 24 hours')
plt.title('Gene Expression: 0 vs 24 Hours')
plt.savefig('output/scatter_plot.png', dpi=300)
plt.close()

#* 2. Diverging Bar Plot for Disease Outcomes
clinical_data = pd.read_csv('data/clinical_data.csv')
mean_response = clinical_data['treatment_response'].mean()
deviations = clinical_data.groupby('disease')['treatment_response'].mean() - mean_response

plt.figure(figsize=(8, 6))
for i, (disease, dev) in enumerate(deviations.items()):
    color = 'green' if dev > 0 else 'red'
    plt.hlines(y=disease, xmin=0, xmax=dev, color=color, lw=2)
    plt.text(dev, i, f'{dev:.2f}', verticalalignment='center', color=color)

plt.axvline(x=0, color='k', linestyle='--')
plt.title('Disease Treatment Response Deviations from Mean')
plt.xlabel('Deviation from Average Response')
plt.ylabel('Disease')
plt.savefig('output/diverging_bar.pdf', bbox_inches='tight')
plt.close()

#* 3. Lollipop Chart for Gene Frequency
gene_counts = pd.read_csv('data/gene_counts.csv')
gene_counts = gene_counts.melt(id_vars=['gene'], var_name='sample', value_name='count')
gene_freq = gene_counts.groupby('gene')['count'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
markerline, stemline, baseline = plt.stem(gene_freq.index, gene_freq.values, basefmt=' ', linefmt='r-', markerfmt='bo')
plt.setp(markerline, markersize=10)
plt.setp(stemline, linewidth=2)
plt.gca().set_facecolor('lightgrey')
plt.title('Gene Frequency Across Samples')
plt.xlabel('Gene')
plt.ylabel('Frequency')
plt.savefig('output/lollipop_chart.png', format='png')
plt.savefig('output/lollipop_chart.svg', format='svg')
plt.close()

#* 4. Histogram of Protein Lengths
protein_lengths = pd.read_csv('data/protein_lengths.csv')
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(protein_lengths['length'], bins=20, edgecolor='black')
for patch in patches:
    patch.set_facecolor(plt.cm.viridis((patch.get_x() - min(bins))/(max(bins) - min(bins))))
plt.title('Histogram of Protein Lengths', fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.xlabel('Protein Length')
plt.ylabel('Number of Proteins')
plt.savefig('output/histogram_protein_lengths.png')
plt.close()

#* 5. Density Plot for Patient Ages
clinical_data = pd.read_csv('data/clinical_data.csv')
plt.figure(figsize=(10, 6))
for disease, group in clinical_data.groupby('disease'):
    sns.kdeplot(data=group, x='age', label=disease)
plt.legend(markerscale=2)
plt.title('Density Plot of Patient Ages by Disease')
plt.xlabel('Age')
plt.ylabel('Density')
plt.savefig('output/density_plot_patient_ages.png')
plt.close()

#* 6. Boxplot for Gene Expression by Condition
gene_expression = pd.read_csv('data/gene_expression.csv')
plt.figure(figsize=(10, 6))
sns.boxplot(x='condition', y='expression_level', hue='condition', data=gene_expression, palette="Set2", legend=False)
plt.title('Gene Expression by Condition')
plt.xlabel('Condition')
plt.ylabel('Expression Level')
plt.savefig('output/boxplot_gene_expression.png')
plt.close()

#* 7. Pie Chart for Disease Distribution
disease_counts = clinical_data['disease'].value_counts()
explode = [0.1 if i == disease_counts.idxmax() else 0 for i in disease_counts.index]
plt.figure(figsize=(10, 6))
plt.pie(disease_counts, labels=disease_counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
plt.title('Distribution of Diseases')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.savefig('output/disease_distribution.png')
plt.close()

#* 8. Bar Chart of Treatment Responses
response_counts = clinical_data['treatment_response'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(response_counts.index, response_counts.values, color=['blue', 'green', 'red'])
plt.grid(axis='y', linestyle='--')
plt.title('Treatment Responses')
plt.xlabel('Response Type')
plt.ylabel('Number of Patients')
plt.savefig('output/bar_chart_treatment_responses.png')
plt.close()

#* 9. Line Graph for Time Series Data
time_series = pd.read_csv('data/gene_time_series.csv')
tp53_data = time_series[time_series['gene_id'] == 'TP53']
plt.figure(figsize=(10, 6))
plt.plot(tp53_data['time_point'], tp53_data['expression_level'], marker='o')
threshold = tp53_data['expression_level'].mean()
plt.fill_between(tp53_data['time_point'], threshold, tp53_data['expression_level'], where=tp53_data['expression_level'] > threshold, alpha=0.3, color='green')
plt.fill_between(tp53_data['time_point'], threshold, tp53_data['expression_level'], where=tp53_data['expression_level'] < threshold, alpha=0.3, color='red')
plt.title('TP53 Expression Over Time')
plt.xlabel('Time Point')
plt.ylabel('Expression Level')
plt.savefig('output/line_graph_tp53_expression.png')
plt.close()

#* 10. Heatmap Visualization of Gene Expression
gene_expression_df = pd.read_csv('data/gene_expression.csv', index_col=0)  # Assuming the first column is gene names
heatmap_data = gene_expression_df.drop(columns=['condition']).T  # Drop the 'condition' column and transpose

sns.clustermap(heatmap_data, 
               cmap="YlOrRd",  # Yellow to Orange to Red color map
               annot=True,  # Annotate each cell
               annot_kws={'size': 8},  # Adjust text size for annotations
               cbar_kws={'label': 'Expression Level'})  # Label for color bar

# Step 4: Customize the heatmap
plt.title('Clustered Heatmap of Gene Expression Across Samples', fontsize=16)

# Step 5: Save the plot
plt.savefig('output/gene_expression_heatmap.pdf', bbox_inches='tight')
plt.close()
