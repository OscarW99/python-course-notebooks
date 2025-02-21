# Chapter 9: Regular Expressions

import re

#* 1. Case-Insensitive Pattern Matching
sequence = "ATGCTATGC"
pattern = re.compile(r'atg', re.IGNORECASE)
matches = pattern.finditer(sequence)
for match in matches:
    print(f"Match found: '{match.group()}' at position {match.start()}-{match.end()-1}")

#* 2. Multiline Pattern Matching
multiline_seq = """ATGC
TAGC
ATGC"""
pattern = re.compile(r'^.{4}$', re.MULTILINE)  # Matches lines with exactly 4 characters
matches = pattern.finditer(multiline_seq)
for match in matches:
    line_number = multiline_seq[:match.start()].count('\n') + 1
    print(f"Match '{match.group()}' found on line {line_number}")

#* 3. Verbose Pattern Matching
dna_sequence = "ATGCCCTAACATGGGGTAA"
pattern = re.compile(r"""
    ATG          # Start codon
    [ATCG]+      # Any number of nucleotides in between
    TAA          # End codon
""", re.VERBOSE)
matches = pattern.finditer(dna_sequence)
for match in matches:
    print(f"Match: {match.group()}, Length: {len(match.group())}")

#* 4. Back-reference for Repeated Nucleotides
sequence = "AATCGGTTA"
pattern = re.compile(r'([ATGC])\1')  # \1 refers back to the first captured group
matches = pattern.finditer(sequence)
for match in matches:
    print(f"Repeated nucleotide pair: {match.group()}")

#* 5. Named Groups for Sequence Parts
sequence = "ATGCCCTAA"
pattern = re.compile(r'(?P<start>ATG)(?P<middle>[ATCG]+)(?P<end>TAA|TAG|TGA)')
match = pattern.search(sequence)
if match:
    print(f"Start codon: {match.group('start')}")
    print(f"Middle sequence: {match.group('middle')}")
    print(f"End codon: {match.group('end')}")

#* 6. Non-capturing Groups for Start Codons
sequence = "ATGCCGTGCGTGCC"
pattern = re.compile(r'(?:ATG|GTG)')
matches = pattern.finditer(sequence)
for match in matches:
    print(f"Match '{match.group()}' starts at position {match.start()}")

#* 7. Positive Lookahead for ATG-CG
sequence = "ATGCGATGTAA"
pattern = re.compile(r'ATG(?=CG)')  # ATG only if followed by CG
matches = pattern.finditer(sequence)
for match in matches:
    print(f"ATG followed by CG found at: {match.group()}")

#* 8. Negative Lookbehind for TAA
sequence = "CCCTAATGCCCTAA"
pattern = re.compile(r'(?<!ATG)TAA')  # TAA not preceded by ATG
matches = pattern.finditer(sequence)
for match in matches:
    start = max(0, match.start() - 3)
    print(f"TAA not preceded by ATG found at: '{sequence[start:match.end()]}', TAA at position {match.start()}")