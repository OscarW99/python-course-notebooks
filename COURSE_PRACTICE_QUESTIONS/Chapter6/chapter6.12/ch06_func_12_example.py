# Chapter 4: Functions and Libraries

#* 1. Basic Lambda Syntax
square = lambda x: x ** 2
add_three = lambda x, y, z: x + y + z
to_lower = lambda s: s.lower()
# Test cases
print(square(4))
print(add_three(1, 2, 3))
print(to_lower("HELLO"))

#* 2. Lambda with Filter
proteins = ["MKKFT", "MLASP", "WPKNS", "NRWVS", "MLKYT"]
m_start_filter = list(filter(lambda s: s.startswith('M'), proteins))
k_content_filter = list(filter(lambda s: 'K' in s, proteins))
length_gr4_filter = list(filter(lambda s: len(s) > 4, proteins))
print(m_start_filter)
print(k_content_filter)
print(length_gr4_filter)

#* 3. Lambda with Map
sequences = ["ATGC", "CGTA", "TGCA"]
lowercase_map = list(map(lambda s: s.lower(), sequences))
length_map = list(map(lambda s: len(s), sequences))
prefix_map = list(map(lambda s: f"DNA:{s}", sequences))
print(lowercase_map)
print(length_map)
print(prefix_map)

#* 4. Lambda with Sorting
sequence_data = [("ATGC", 4), ("GC", 2), ("AAATTT", 6)]
sort_by_length = sorted(sequence_data, key=lambda x: x[1])
sort_by_sequence = sorted(sequence_data, key=lambda x: x[0])
sort_by_length_descending = sorted(sequence_data, key=lambda x: x[1], reverse=True)
print(sort_by_length)
print(sort_by_sequence)
print(sort_by_length_descending)

#* 5. Combining Lambda Functions
dna_sequences = ["ATGC", "GCTA", "TTAA", "GTAAT"]
at_filter = list(filter(lambda s: 'AT' in s, dna_sequences))
length_map = list(map(lambda s: len(s), at_filter))
length_sort = sorted(length_map)
print(length_sort)

#* 6. Lambda vs Regular Function
def check_gc_balance(sequence):
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return g_count == c_count

gc_balance_lambda = lambda s: s.count('G') == s.count('C')

# Regular function test
print(check_gc_balance("GCGC"))
print(check_gc_balance("GCGT"))

# Lambda function test
print(gc_balance_lambda("GCGC"))
print(gc_balance_lambda("GCGT"))
