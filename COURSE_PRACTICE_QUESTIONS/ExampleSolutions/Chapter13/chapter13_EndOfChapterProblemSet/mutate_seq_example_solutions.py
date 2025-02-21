#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("Usage: python mutate_seq.py <sequence> <mutation_position>")
    sys.exit(1)

sequence, mutation_pos = sys.argv[1], int(sys.argv[2]) - 1  # -1 because indexing starts at 0
if mutation_pos < 0 or mutation_pos >= len(sequence):
    print(f"Error: Mutation position {mutation_pos + 1} is out of range for sequence length {len(sequence)}.")
    sys.exit(1)

mutated_sequence = sequence[:mutation_pos] + 'X' + sequence[mutation_pos+1:]
print(f"Mutated sequence: {mutated_sequence}")