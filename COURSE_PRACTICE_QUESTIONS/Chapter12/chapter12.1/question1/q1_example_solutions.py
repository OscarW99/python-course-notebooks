# Question 1 Solution
sequence = input("Enter a DNA sequence: ")
valid_bases = set('ATGC')
if set(sequence.upper()).issubset(valid_bases):
    print("The sequence is valid.")
else:
    print("The sequence is invalid. It should only contain A, T, G, and C.")