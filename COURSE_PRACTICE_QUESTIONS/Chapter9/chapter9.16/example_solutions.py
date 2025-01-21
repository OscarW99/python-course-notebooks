# Chapter 9: Data Manipulation

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#* 1. Demonstrating Seq Object Operations
dna_seq = Seq("ATGCGTACG")
print("Original Sequence:", dna_seq)
print("Complement:", dna_seq.complement())
print("Reverse Complement:", dna_seq.reverse_complement())
print("Transcription to RNA:", dna_seq.transcribe())

#* 2. Translating DNA to Protein and Creating SeqRecord
dna_seq_protein = Seq("CCTAGGACTG")
protein_seq = dna_seq_protein.translate()
print("Protein Sequence:", protein_seq)
seq_record = SeqRecord(protein_seq, id="example_gene", description="Sample bacterial gene sequence")
print(seq_record)

#* 3. Concatenation and Slicing of Seq Objects
seq1 = Seq("ATGCTA")
seq2 = Seq("CGGATC")
combined_seq = seq1 + seq2
substring = combined_seq[3:6]  # Slicing to get 3 bases starting from index 3
print("Combined Sequence:", combined_seq)
print("Substring:", substring)
print("Length of Substring:", len(substring))