# test_script.py
from sequence_analysis.dna_tools import count_bases
from data_processing.file_parser import read_fasta

# Test dna_tools
dna_sequence = "ATCGATCG"
print("Base Counts:", count_bases(dna_sequence))

# Test file_parser
read_fasta("example.fasta")