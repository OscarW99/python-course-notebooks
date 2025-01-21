# Chapter 8: Regular Expressions

import re

#* 1. DNA Motif Finding
sequence = "GCATCGTAGCTTTTCGAGCAAAACG"
# a) Create and compile pattern
pattern = re.compile(r'GC.*CG')
# b) Find all non-overlapping matches
matches = pattern.finditer(sequence)
# c) Print position of each match
for match in matches:
    start, end = match.span()
    print(f"Match found at position {start} to {end-1}")

#* 2. Gene Sequence Finding
dna_sequence = "ATGCCGTAATGCGTTGATGCCCTGA"
# Find all possible gene sequences
gene_pattern = re.compile(r'ATG(?:(?!T(?:AA|AG|A))[\w])*(?:T(?:AA|AG|A))')
gene_matches = gene_pattern.findall(dna_sequence)
for match in gene_matches:
    print(f"Gene sequence found: {match}")

#* 3. Initiation Codon Check
sequences = ["ATGGCT", "TATATG", "GTATTT", "ATGCCC"]
for seq in sequences:
    if re.match(r'^ATG', seq):
        print(f"{seq} starts with ATG")
    else:
        print(f"{seq} does not start with ATG")

#* 4. ID-Sequence Pair Extraction
data_string = "ID001:MKLP, ID002:YKLM; ID003:KLMP ID004:PLMK"
# Separate into ID-sequence pairs
id_pattern = re.compile(r'(\w+):([\w]+)')
pairs = id_pattern.findall(data_string)
for pair in pairs:
    print(f"ID: {pair[0]}, Sequence: {pair[1]}")

#* 5. Replace Invalid Nucleotides
dna_sequence = "ATGXBYATGCRNKTAT"
# Replace invalid nucleotides
corrected_sequence = re.sub(r'[^ATGC]', 'N', dna_sequence)
print(f"Corrected sequence: {corrected_sequence}")

#* 6. Accession Number Filtering
accession_numbers = ["XP_123", "XP_1234", "XM_123", "XP123"]
# Check accession number format
pattern = re.compile(r'^X[PM]_[0-9]{3}$')
matching_numbers = [num for num in accession_numbers if pattern.match(num)]
print(f"Matching accession numbers: {matching_numbers}")