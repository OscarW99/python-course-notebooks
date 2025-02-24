# main.py
# Write the absolute import statement to import calculate_a_freq from dna_tools.py

from sequence.dna_tools import calculate_a_freq


# Test the import:
sequence = "ATCGCC"
a_freq = calculate_a_freq(sequence)
print(f"A frequency: {a_freq}")