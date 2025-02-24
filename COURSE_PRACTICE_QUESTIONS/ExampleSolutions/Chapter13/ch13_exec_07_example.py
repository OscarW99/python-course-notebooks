# Chapter 13: Creating Executable Python Scripts

# #* 1. Restructuring Code with `if __name__ == "__main__":`
# @ This code would be in dna_tools.py
# def count_gc(sequence):
#     """Calculate the GC content of a DNA sequence as a percentage."""
#     gc_count = sequence.count('G') + sequence.count('C')
#     return (gc_count / len(sequence)) * 100

# def main():
#     sequence = "ATCGCGTA"
#     result = count_gc(sequence)
#     print(f"GC content: {result}%")

# if __name__ == "__main__":
#     main()

# #* 2. Examining and Fixing Script Structure
# @ This code would be in sequence_analyzer.py
# def analyze_sequence(seq):
#     """Return the length of a DNA sequence."""
#     if not seq:
#         raise ValueError("Sequence cannot be empty")
#     return len(seq)

# def main():
#     sequence = "ATCG"
#     try:
#         length = analyze_sequence(sequence)
#         print(f"Sequence length: {length}")
#     except ValueError as e:
#         print(f"Error: {e}")
#
# if __name__ == "__main__":
#     main()


#* Question 1 import code:
from dna_tools import count_gc
count_gc("ATCGCGTA")

#* Question 2 import code:
from sequence_analyzer import analyze_sequence
analyze_sequence("ATCG")
analyze_sequence("") # Should raise an error