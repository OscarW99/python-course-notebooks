import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
import os

# This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
expression_data = pd.read_csv('data/gene_expression.csv')

#* 1. Creating 1x2 Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left Subplot: Bar plot of mean expression by tissue
mean_expression = expression_data.groupby('tissue_type')['expression_level'].mean()
mean_expression.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title('Mean Gene Expression by Tissue Type')
ax1.set_xlabel('Tissue Type')
ax1.set_ylabel('Mean Expression Level')

# Right Subplot: Line plot of BRCA1 expression over time by tissue
brca1_data = expression_data[expression_data['gene_id'] == 'BRCA1']
for tissue, group in brca1_data.groupby('tissue_type'):
    group.plot(x='time_point', y='expression_level', ax=ax2, label=tissue, marker='o')
ax2.set_title('BRCA1 Expression Over Time by Tissue')
ax2.set_xlabel('Time Point')
ax2.set_ylabel('Expression Level')
ax2.legend(title='Tissue Type')

plt.tight_layout()
plt.show()

#* 2. Creating 2x2 Subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# [0, 0]: Bar plot of mean expression by condition
mean_expression_condition = expression_data.groupby('condition')['expression_level'].mean()
mean_expression_condition.plot(kind='bar', ax=axs[0, 0], color=['skyblue', 'salmon'])
axs[0, 0].set_title('Mean Gene Expression by Condition')
axs[0, 0].set_xlabel('Condition')
axs[0, 0].set_ylabel('Mean Expression Level')

# [0, 1]: Scatter plot of expression at 0h vs 12h, colored by tissue
time_0 = expression_data[expression_data['time_point'] == 0]
time_12 = expression_data[expression_data['time_point'] == 12]
merged_data = pd.merge(time_0, time_12, on=['gene_id', 'tissue_type'], suffixes=('_0h', '_12h'))
scatter = axs[0, 1].scatter(merged_data['expression_level_0h'], merged_data['expression_level_12h'], c=merged_data['tissue_type'].astype('category').cat.codes, cmap='viridis')
axs[0, 1].set_title('Expression at 0h vs 12h by Tissue')
axs[0, 1].set_xlabel('Expression Level at 0h')
axs[0, 1].set_ylabel('Expression Level at 12h')
tissue_types = merged_data['tissue_type'].astype('category').cat.categories
handles, _ = scatter.legend_elements()
axs[0, 1].legend(handles, tissue_types, title='Tissue Type')

# [1, 0]: Pie chart of gene distribution across tissues
tissue_counts = expression_data['tissue_type'].value_counts()
axs[1, 0].pie(tissue_counts, labels=tissue_counts.index, autopct='%1.1f%%', startangle=90)
axs[1, 0].set_title('Gene Distribution Across Tissues')

# [1, 1]: Line plot of TP53 expression over time by condition
tp53_data = expression_data[expression_data['gene_id'] == 'TP53']
for condition, group in tp53_data.groupby('condition'):
    group.plot(x='time_point', y='expression_level', ax=axs[1, 1], label=condition, marker='o')
axs[1, 1].set_title('TP53 Expression Over Time by Condition')
axs[1, 1].set_xlabel('Time Point')
axs[1, 1].set_ylabel('Expression Level')
axs[1, 1].legend(title='Condition')

plt.tight_layout()
plt.show()

#* 3. Using GridSpec for Complex Layout
fig = plt.figure(figsize=(14, 8))
gs = GridSpec(2, 2, figure=fig)

# Top plot: EGFR expression over time by tissue
ax1 = fig.add_subplot(gs[0, :])
egfr_data = expression_data[expression_data['gene_id'] == 'EGFR']
for tissue, group in egfr_data.groupby('tissue_type'):
    group.plot(x='time_point', y='expression_level', ax=ax1, label=tissue, marker='o')
ax1.set_title('EGFR Expression Over Time by Tissue')
ax1.set_xlabel('Time Point')
ax1.set_ylabel('Expression Level')
ax1.legend(title='Tissue Type')

# Bottom left plot: Histogram of expression at 0h
ax2 = fig.add_subplot(gs[1, 0])
time_0_expression = expression_data[expression_data['time_point'] == 0]['expression_level']
ax2.hist(time_0_expression, bins=10, color='skyblue', alpha=0.7)
ax2.set_title('Expression Level Distribution at 0h')
ax2.set_xlabel('Expression Level')
ax2.set_ylabel('Frequency')

# Bottom right plot: Boxplot of expression by condition
ax3 = fig.add_subplot(gs[1, 1])
sns.boxplot(x='condition', y='expression_level', data=expression_data, ax=ax3, palette=['skyblue', 'salmon'])
ax3.set_title('Expression Level by Condition')
ax3.set_xlabel('Condition')
ax3.set_ylabel('Expression Level')

plt.tight_layout()
plt.show()