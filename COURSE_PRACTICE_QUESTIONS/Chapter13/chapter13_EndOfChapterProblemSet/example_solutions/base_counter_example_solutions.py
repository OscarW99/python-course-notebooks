#!/usr/bin/env python3

def count_bases(sequence):
    return {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }

# Get the DNA sequence from user input
sequence = input("Enter a DNA sequence: ")
base_counts = count_bases(sequence)

# Print the count for each base
for base, count in base_counts.items():
    print(f"{base}: {count}")