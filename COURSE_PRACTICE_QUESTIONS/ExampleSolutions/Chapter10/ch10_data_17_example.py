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
record = SeqIO.read("data/mouse_gene.fasta", "fasta")
print("Sequence ID:", record.id)
print("Sequence Content:", record.seq)

#* 2. Creating and Writing SeqRecord
seq = Seq("ATGCGATCGATCGATCG")
seq_record = SeqRecord(seq, id="sample_sequence")
SeqIO.write(seq_record, "data/output_sequence.fasta", "fasta")

#* 3. Converting FASTQ to FASTA
SeqIO.convert("data/raw_reads.fastq", "fastq", "data/processed_reads.fasta", "fasta")

#* 4. Indexing and Accessing FASTA File
fasta_index = SeqIO.index("data/genome_sequences.fasta", "fasta")
specific_sequence = fasta_index["seq2"]
print("Sequence 'seq2':", specific_sequence.seq)

#* 5. Extracting Annotations from GenBank File
for record in SeqIO.parse("data/gene_annotations.gb", "genbank"):
    for feature in record.features:
        if feature.type == "gene":
            print(f"Gene Name: {feature.qualifiers.get('gene', ['Unknown'])[0]}")
            print(f"Location: {feature.location}")