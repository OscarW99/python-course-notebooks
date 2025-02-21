# Chapter 6: Functions and Libraries

#* 1. Global Variable Modification
total_sequences_processed = 0
def process_sequence():
    global total_sequences_processed
    total_sequences_processed += 1
    print(total_sequences_processed)

process_sequence()
process_sequence()
process_sequence()

#* 2. Using Global Inside a Function
enzyme = "DNA Polymerase"
def display_enzyme():
    global enzyme
    print(enzyme)
    enzyme = "RNA Polymerase"
    print(enzyme)

display_enzyme()
print(enzyme)

#* 3. Global List Modification
dna_sequences = []
def add_sequence(seq):
    dna_sequences.append(seq)

def clear_sequences():
    global dna_sequences
    dna_sequences = []

add_sequence("ATGC")
add_sequence("CGTA")
print(dna_sequences)
clear_sequences()
print(dna_sequences)

#* 4. Multiple Global Variables
sequence_count = 0
total_length = 0
def track_sequence(seq):
    global sequence_count, total_length
    sequence_count += 1
    total_length += len(seq)

track_sequence("ATGC")
track_sequence("CGTA")
print(sequence_count, total_length)

#* 5. Local vs Global Conflict
value = 10
def demonstrate_scope():
    global value
    value = 20
    print(f"Local value: {value}")
print(f"Global value: {value}")
demonstrate_scope()
print(f"Global value after function call: {value}")
