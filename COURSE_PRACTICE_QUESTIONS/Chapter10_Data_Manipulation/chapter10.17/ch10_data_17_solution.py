# Chapter 10: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Reading Single Sequence from FASTA
# Read single sequence from data/mouse_gene.fasta
# Print sequence ID and content

#* 2. Creating and Writing SeqRecord
# Create SeqRecord with DNA sequence
# Write to data/output_sequence.fasta

#* 3. Converting FASTQ to FASTA
# Convert data/raw_reads.fastq to data/processed_reads.fasta

#* 4. Indexing and Accessing FASTA File
# Index data/genome_sequences.fasta
# Retrieve specific sequence by ID

#* 5. Extracting Annotations from GenBank File
# Read data/gene_annotations.gb
# Extract and print feature annotations