# Chapter 10: Data Manipulation

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO
from Bio.Seq import Seq
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#* 1. Performing a BLAST Search
dna_seq = Seq("ATGCGACTTGACCTAGATCCTAGGCTAA")
result_handle = NCBIWWW.qblast("blastn", "nt", dna_seq)
blast_records = NCBIXML.parse(result_handle)
first_record = next(blast_records)
if first_record.alignments:
    first_alignment = first_record.alignments[0]
    print("Title:", first_alignment.title)
    print("Score:", first_alignment.hsps[0].score)
result_handle.close()

#* 2. Parsing BLAST XML Results
blast_result = SearchIO.read("data/blast_results.xml", "blast-xml")
hit_ids = []
align_lengths = []
num_gaps = []
for hit in blast_result:
    hit_ids.append(hit.id)
    align_lengths.append(hit.hsps[0].aln_span)
    num_gaps.append(hit.hsps[0].gaps)
print("Hit IDs:", hit_ids)
print("Alignment Lengths:", align_lengths)
print("Number of Gaps:", num_gaps)

#* 3. Function for Protein BLAST Search
def protein_blast_search(sequence, output_filename):
    result_handle = NCBIWWW.qblast("blastp", "nr", sequence)
    with open(output_filename, "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()
    print(f"BLAST results saved to {output_filename}")

# Example usage:
sequence = "MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNG"
output_file = "output/protein_blast_output.xml"
protein_blast_search(sequence, output_file)