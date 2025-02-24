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
    # TODO: Add error handling for file existence
    # If file doesn't exist, write to stderr and exit with status 1
    
    try:
        # TODO: Read the CSV file into a DataFrame
        # TODO: Verify it has the required columns: SequenceID, DNASequence, Type
        # If columns are missing, write to stderr and exit
        
        # TODO: Verify sequences only contain valid DNA letters (A, T, G, C)
        # Hint: You could use str.contains() with a regular expression
        
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
    # TODO: Add a Length column containing sequence lengths
    
    # TODO: Add a GC_Content column containing GC percentage
    # Hint: Use apply() with a lambda function to count G and C, divide by length
    
    return data

def create_visualizations(data, output_folder):
    """
    Creates two plots:
    1. Boxplot of GC content by sequence type
    2. Scatter plot of sequence length vs GC content, colored by type
    Saves both plots to the output folder.
    """
    # TODO: Create and save GC content boxplot
    # Use title: 'GC Content Distribution by Sequence Type'
    # x-axis: Type
    # y-axis: GC Content (%)
    
    # TODO: Create and save scatter plot
    # Use title: 'Sequence Length vs GC Content'
    # x-axis: Sequence Length (bp)
    # y-axis: GC Content (%)
    # Color points by Type
    
def main():
    """
    Main function that runs the pipeline:
    1. Checks command line arguments
    2. Creates output directory if needed
    3. Runs analysis pipeline
    4. Saves results
    """
    # Command line validation already implemented
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python sequence_analyzer.py <input_file.csv> <output_folder>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_folder = sys.argv[2]

    # TODO: Create output_folder if it doesn't exist
    # Hint: Use os.path.exists() and os.mkdir()

    # Execute pipeline
    print("Reading sequences...")
    data = read_sequences(input_file)
    
    print("Analyzing sequences...")
    data = analyze_sequences(data)
    
    print("Generating visualizations...")
    create_visualizations(data, output_folder)
    
    # TODO: Save final DataFrame to output_folder/sequence_analysis.csv
    # Hint: Use os.path.join() for the file path
    
    print(f"Analysis complete. Results saved in {output_folder}")

# Call main function
main()