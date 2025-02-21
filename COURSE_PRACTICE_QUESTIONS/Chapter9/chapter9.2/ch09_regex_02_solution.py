# Chapter 8: Regular Expressions

import re

#* 1. Case-Insensitive Pattern Matching
sequence = "ATGCTATGC"
#$ pattern = 
#$ matches =  # Use finditer() to get match objects
for match in matches:
    # Print each match and its position
    pass

#* 2. Multiline Pattern Matching
multiline_seq = """ATGC
TAGC
ATGC"""
#$ pattern = 
#$ matches =  # Use finditer() to get match objects
for match in matches:
    # Calculate line number and print match with line number
    pass

#* 3. Verbose Pattern Matching
dna_sequence = "ATGCCCTAACATGGGGTAA"
#$ pattern = 
#$ matches =  # Use finditer() to get matches
for match in matches:
    # Print match and its length
    pass

#* 4. Back-reference for Repeated Nucleotides
sequence = "AATCGGTTA"
#$ pattern = 
#$ matches =  # Use finditer() to get matches
for match in matches:
    # Print repeated nucleotide pairs
    pass

#* 5. Named Groups for Sequence Parts
sequence = "ATGCCCTAA"
#$ pattern = 
#$ match =  # Use search() to find pattern
if match:
    # Print each named group
    pass

#* 6. Non-capturing Groups for Start Codons
sequence = "ATGCCGTGCGTGCC"
#$ pattern = 
#$ matches = 

#* 7. Positive Lookahead for ATG-CG
sequence = "ATGCGATGTAA"
#$ pattern = 
#$ matches = 

#* 8. Negative Lookbehind for TAA
sequence = "CCCTAATGCCCTAA"
#$ pattern = 
#$ matches = 