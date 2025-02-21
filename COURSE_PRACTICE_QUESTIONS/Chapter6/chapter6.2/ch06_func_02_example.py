# Chapter 6: Functions and Libraries

#* 1. Basic Data Type Conversions
string_value = "3.14159"
float_value = float(string_value)
int_value = int(float_value)
string_again = str(int_value)
print(type(string_value))
print(type(float_value))
print(type(int_value))
print(type(string_again))

#* 2. Collection Type Conversions
protein_lengths = [("Insulin", 51), ("Hemoglobin", 574), ("Albumin", 585)]
protein_dict = dict(protein_lengths)
keys_set = set(protein_dict.keys())
values_list = list(protein_dict.values())
print(keys_set)
print(values_list)

#* 3. Boolean Conversions
empty_string = ""
zero = 0
dna_sequence = "ATGC"
empty_list = []
negative = -5
print(bool(empty_string))
print(bool(zero))
print(bool(dna_sequence))
print(bool(empty_list))
print(bool(negative))
