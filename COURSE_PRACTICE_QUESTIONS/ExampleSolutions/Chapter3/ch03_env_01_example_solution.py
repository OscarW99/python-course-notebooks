# Chapter 3: Local Development Environment Problem Set

#* 1. Test Script
print("Hello World")


#* 2. Count T nucleotides
sequence = "ACGTCGTTATGCGAAGCTAGTATCGCTATTA"
tcount = 0
# write your for loop here
for nucleotide in sequence:
    if nucleotide == 'T':
        tcount += 1
print("Number of T nucleotides:", tcount)


#* 3. Protein Motif Analysis
proteins = ["ASDFGHJKLKFERQWERTYUIOP",
    "QWERTYUIOPASDFGHJKL",
    "ZXCVBNMKFERQ",
    "POIUYTREWQ",
    "KFERQABCDEFG",
    "asdfKFERQzxcv",
    "asdfkferq",
    "KFERQ"]
# write your for loop here
motif = "KFERQ"
for protein in proteins:
    if motif in protein:
        print("Protein containing motif:", protein)


#* 4. Temperature Data Analysis
temperature = 50
while temperature > 30:
    print("Temperature:", temperature)
    temperature -= 1