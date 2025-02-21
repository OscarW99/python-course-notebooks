# Chapter 9: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

from Bio import Align
from Bio import AlignIO
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Pairwise Sequence Alignment
aligner = Align.PairwiseAligner()
aligner.match_score = 2  # Example scoring
aligner.mismatch_score = -1
aligner.open_gap_score = -0.5
aligner.extend_gap_score = -0.1

sequences = ["ACCGT", "ACGT"]
alignments = aligner.align(sequences[0], sequences[1])
for alignment in alignments:
    print(alignment)
    print("Score:", alignment.score)

#* 2. Reading Multiple Sequence Alignment
alignment = AlignIO.read("data/protein_alignment.clustal", "clustal")
print("Alignment Length:", alignment.get_alignment_length())
for record in alignment:
    print(f"{record.id}: {record.seq}")

#* 3. Extracting Conserved Columns
alignment = AlignIO.read("data/gene_family.clustal", "clustal")
columns = list(zip(*[str(record.seq) for record in alignment])) # This line converts sequence rows to position columns using a list comprehension and unpacking (*), enabling column-wise analysis.
conserved_columns = [col for col in columns if len(set(col)) == 1]  # All characters are the same in the column
for i, col in enumerate(conserved_columns):
    print(f"Conserved column at position {i}: {col[0]}")