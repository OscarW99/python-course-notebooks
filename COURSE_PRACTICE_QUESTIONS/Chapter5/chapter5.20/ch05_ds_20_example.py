# Chapter 5: Data Structures

#* 1. Case Manipulation and Counting
sequence = "agctTAGCta"
print(sequence.upper())
print(sequence.lower())
print(sequence.lower().count('a'))


#* 2. Character Type Checking
print("ATCG123".isalpha())
print("12345".isdigit())
print("ATCG".isalpha())


#* 3. Splitting and Joining
sequence = "ATCG-TAGC-GCTA"
split_sequence = sequence.split('-')
print(split_sequence)
joined_sequence = '|'.join(split_sequence)
print(joined_sequence)


#* 4. Pattern Checking
print("ATATATCG".startswith("ATA"))
print("GCGCTAT".endswith("TAT"))
print("ATGCTA".find("GC"))


#* 5. Advanced Counting
sequence = "ATAGATAGATAG"
print(sequence.count("TAG"))
print(sequence.count("TAG", 0, 6))
print(sequence.count("TAG", 3, 9))
