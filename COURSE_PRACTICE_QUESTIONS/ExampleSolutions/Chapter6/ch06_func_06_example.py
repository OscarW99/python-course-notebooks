# Chapter 6: Functions and Libraries

#* 1. Creating a Greeting Function
def greet():
    print("Hello, welcome to the Python course!")
greet()

#* 2. DNA Sequence Printer
def print_dna(sequence):
    print(sequence)
print_dna("ATGC")
print_dna("CGTA")

#* 3. Sequence Length Calculator
def print_sequence_length(sequence):
    length = len(sequence)
    print(f"Length of the sequence: {length}")
print_sequence_length("ATGC")
print_sequence_length("CGTACGTA")

#* 4. Nucleotide Counter
def count_a(sequence):
    a_count = sequence.count('A')
    print(f"Number of 'A' nucleotides: {a_count}")
count_a("ATGC")
count_a("AATTCCGG")
