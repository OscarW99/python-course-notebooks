# Chapter 9: Regular Expressions

import re

#* 1. Identifying DNA Motifs with Specific Start and End
sequence = "GCATCGTAGCTTTTCGAGCAAAACG"
pattern1 = re.compile(r'GC.*CG')
matches1 = pattern1.finditer(sequence)
for match in matches1:
    print(f"Match: {match.group()}, Span: {match.span()}")

#* 2. Finding Genes Based on Start and Stop Codons
dna_sequence = "ATGCCGTAATGCGTTGATGCCCTGA"
pattern2 = re.compile(r'ATG(?:(?!T(?:AA|AG|A))[\w])*(?:T(?:AA|AG|A))')
matches2 = pattern2.findall(dna_sequence)
for match in matches2:
    print(f"Gene sequence found: {match}")

#* 3. Parsing Mixed-Format Data
data_string = "ID001:MKLP, ID002:YKLM; ID003:KLMP ID004:PLMK"
pattern3 = re.compile(r'[;, ]')
components = re.split(pattern3, data_string)
for component in components:
    if ':' in component:
        id, seq = component.split(':')
        print(f"ID: {id}, Sequence: {seq}")

#* 4. Cleaning DNA Sequences
dna_sequence = "ATGXBYATGCRNKTAT"
pattern4 = re.compile(r'[^ACGT]')
cleaned_sequence = pattern4.sub('N', dna_sequence)
print(f"Cleaned sequence: {cleaned_sequence}")

#* 5. Validating Accession Numbers
accession_numbers = ["XP_123", "XP_1234", "XM_123", "XP123"]
pattern5 = re.compile(r'^X[PM]_[0-9]{3}$')
valid_accessions = [num for num in accession_numbers if pattern5.match(num)]
print(f"Valid accession numbers: {valid_accessions}")

#* 6. Matching Repeats in DNA Sequence
sequence = "AATCGGTTA"
pattern6 = re.compile(r'([ATCG])\1')
matches6 = pattern6.finditer(sequence)
for match in matches6:
    print(f"Repeated nucleotide: {match.group(1)} at position {match.start()}")

#* 7. FASTA File Parser using Regular Expressions
def fasta_parser(fasta_file_path):
    pattern_header = re.compile(r'^>(\w+)\s*(.*)')
    pattern_sequence = re.compile(r'^[ACGTacgt]+$')
    sequences = {}
    with open(fasta_file_path, 'r') as file:
        identifier = description = sequence = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if identifier:
                    if not pattern_sequence.match(sequence):
                        raise ValueError(f"Invalid sequence for {identifier}")
                    sequences[identifier] = {'description': description, 'sequence': sequence}
                header_match = pattern_header.match(line)
                identifier, description = header_match.groups()
                sequence = ''
            else:
                sequence += line
        if identifier:
            if not pattern_sequence.match(sequence):
                raise ValueError(f"Invalid sequence for {identifier}")
            sequences[identifier] = {'description': description, 'sequence': sequence}
    return sequences


# Test cases for FASTA parser (Nothing for you to change here)
#$ This Just Makes Sure We're Starting in the Right Directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

try:
    print("Parsing valid sequences:")
    valid_sequences = fasta_parser('data/valid_sequences.fasta')
    print(valid_sequences)
except ValueError as e:
    print(f"Unexpected error with valid file: {e}")

try:
    print("\nParsing invalid sequences:")
    invalid_sequences = fasta_parser('data/invalid_sequences.fasta')
    print(invalid_sequences)
except ValueError as e:
    print(f"Expected error with invalid file: {e}")


#* 8. Protein Motif Identification using Regular Expressions
protein_sequence = "MKKLVVVGAALVLLAAATVGAAPAAQAPAPAAQAAKAAAPAAPAPAAQAAPAPAAQAPAPAAQAAKAAAPAAAPAPAAQAPAPAAQAAKAAAPAPAPAAQAAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQAAKAAAPAPAPAAQAPAPAAQ"
motif_pattern = re.compile(r'M[^P][ST][^P]')
def protein_motif_finder(protein_sequence, motif_pattern):
    matches = motif_pattern.finditer(protein_sequence)
    return [{'match': match.group(), 'start': match.start()} for match in matches]

#* 9. Email Validation with Regular Expressions
email = "user.name@example.com"
pattern9 = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
if pattern9.match(email):
    print(f"Email '{email}' is valid")
else:
    print(f"Email '{email}' is not valid")

#* 10. Chromosome Information Extraction
genomic_data = "Chromosome 1: size 249250621, genes 2000. ChrX: size 155270560, genes 800"
pattern10 = re.compile(r'(?:Chromosome|Chr)(\s*\w+):\s*size\s*(\d+),\s*genes\s*(\d+)')
matches10 = pattern10.finditer(genomic_data)
for match in matches10:
    chromosome, size, genes = match.groups()
    print(f"Chromosome: {chromosome.strip()}, Size: {size}, Genes: {genes}")