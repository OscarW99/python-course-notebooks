#!/usr/bin/env python3

import pandas as pd
import sys
import os
from matplotlib import pyplot as plt
import seaborn as sns

def read_sequences(file_path):
    """
    Reads and validates the input CSV file.
    Returns a pandas DataFrame if successful.
    """
    if not os.path.exists(file_path):
        sys.stderr.write(f"Error: File {file_path} does not exist.\n")
        sys.exit(1)
    
    try:
        data = pd.read_csv(file_path)
        required_columns = ['SequenceID', 'DNASequence', 'Type']
        if not all(col in data.columns for col in required_columns):
            sys.stderr.write(f"Error: Missing required columns. Required: {', '.join(required_columns)}\n")
            sys.exit(1)
        
        # Verify sequences only contain valid DNA letters (A, T, G, C)
        invalid_sequences = data[~data['DNASequence'].str.contains('^[ATGCatgc]+$', regex=True)]
        if not invalid_sequences.empty:
            sys.stderr.write(f"Error: Invalid DNA sequences found in:\n{invalid_sequences['SequenceID'].tolist()}\n")
            sys.exit(1)
        
        return data
    except Exception as e:
        sys.stderr.write(f"Error reading file: {str(e)}\n")
        sys.exit(1)

def analyze_sequences(data):
    """
    Calculates and adds these columns to the DataFrame:
    - Length: Length of each sequence
    - GC_Content: Percentage of G and C bases (rounded to 2 decimals)
    """
    data['Length'] = data['DNASequence'].apply(len)
    data['GC_Content'] = data['DNASequence'].apply(lambda seq: round((seq.upper().count('G') + seq.upper().count('C')) / len(seq) * 100, 2))
    
    return data

def create_visualizations(data, output_folder):
    """
    Creates two plots:
    1. Boxplot of GC content by sequence type
    2. Scatter plot of sequence length vs GC content, colored by type
    Saves both plots to the output folder.
    """
    # GC content boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Type', y='GC_Content', data=data)
    plt.title('GC Content Distribution by Sequence Type')
    plt.xlabel('Type')
    plt.ylabel('GC Content (%)')
    plt.savefig(os.path.join(output_folder, 'gc_content_boxplot.png'))
    plt.close()

    # Scatter plot of sequence length vs GC content
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Length', y='GC_Content', hue='Type', data=data)
    plt.title('Sequence Length vs GC Content')
    plt.xlabel('Sequence Length (bp)')
    plt.ylabel('GC Content (%)')
    plt.savefig(os.path.join(output_folder, 'length_vs_gc_scatter.png'))
    plt.close()

def main():
    """
    Main function that runs the pipeline:
    1. Checks command line arguments
    2. Creates output directory if needed
    3. Runs analysis pipeline
    4. Saves results
    """
    # Command line validation
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python sequence_analyzer.py <input_file.csv> <output_folder>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_folder = sys.argv[2]

    # Create output_folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Execute pipeline
    print("Reading sequences...")
    data = read_sequences(input_file)
    
    print("Analyzing sequences...")
    data = analyze_sequences(data)
    
    print("Generating visualizations...")
    create_visualizations(data, output_folder)
    
    # Save final DataFrame to output_folder/sequence_analysis.csv
    data.to_csv(os.path.join(output_folder, 'sequence_analysis.csv'), index=False)
    
    print(f"Analysis complete. Results saved in {output_folder}")

# Call main function
main()