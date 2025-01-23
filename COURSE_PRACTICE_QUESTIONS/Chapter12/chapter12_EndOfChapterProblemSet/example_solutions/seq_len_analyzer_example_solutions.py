#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 2:
    print("Please provide a FASTA file name as an argument.", file=sys.stderr)
    sys.exit(1)

fasta_file = sys.argv[1]
if not os.path.isfile(fasta_file):
    print(f"Error: File '{fasta_file}' does not exist.", file=sys.stderr)
    sys.exit(1)

sequence = ""
with open(fasta_file, 'r') as file:
    for line in file:
        line = line.strip()
        if not line.startswith('>'):
            sequence += line

print(f"Sequence length: {len(sequence)}")