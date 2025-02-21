# Chapter 6: Functions and Libraries

#* 1. Counting Guanine Nucleotides
def count_guanine(dna_sequence):
    return dna_sequence.count('G')
print(count_guanine("ATGCGC"))
print(count_guanine("GCGCGC"))

#* 2. String Reversal
def reverse_string(input_string):
    return input_string[::-1]
print(reverse_string("ATGC"))
print(reverse_string("CGTA"))

#* 3. Flexible Nucleotide Counter
def count_nucleotides(dna_sequence, nucleotide='A'):
    return dna_sequence.count(nucleotide)
print(count_nucleotides("ATTAGTC"))
print(count_nucleotides("ATTAGTC", 'T'))

#* 4. GC Content Calculator
def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100
gc_content = calculate_gc_content("ATGCGC")
print(gc_content)

#* 5. Sequence Length Analyzer
def analyze_sequence(dna_sequence, min_length=5, max_length=20):
    length = len(dna_sequence)
    if length < min_length:
        return "Too short"
    elif length > max_length:
        return "Too long"
    else:
        return "Ok"
print(analyze_sequence("ATCGATCGATCG"))
print(analyze_sequence("ATCGATCGATCG", min_length=3, max_length=10))
