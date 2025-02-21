# Chapter 9: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
mutations_df = pd.read_csv('data/genetic_variants.csv')

#* 1. Selecting High Impact Variants
#$ impact_condition = 
#$ high_impact_variants = 

#* 2. Selecting Chromosome 7 Mutations
#$ type_condition = 
#$ chr_condition = 
#$ chr7_mutations_df = 

#* 3. Selecting G Variants in a Specific Region
#$ position_condition = 
#$ ref_condition = 
#$ g_variants_region = 

#* 4. Selecting Splice Variants
#$ splice_pattern = 
#$ path_condition = 
#$ splice_variants = 

#* 5. Selecting Severe Variants
#$ path_condition = 
#$ freq_condition = 
#$ type_condition = 
#$ pos_condition = 
#$ severe_variants =