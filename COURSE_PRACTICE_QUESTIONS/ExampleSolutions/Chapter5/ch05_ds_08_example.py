# Chapter 5: Data Structures

#* 1. Accessing Tuple Elements
amino_acid_pair = ('lysine', 'arginine')
print(amino_acid_pair[0])


#* 2. Creating a Tuple
dna_bases = ('adenine', 'thymine')
print(dna_bases)


#* 3. Trying to Modify
dna_pair = ('cytosine', 'guanine')
try:
    dna_pair[0] = 'adenine'
except TypeError as e:
    # Handle the error here
    print("Error:", e)
