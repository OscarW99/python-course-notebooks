# Question 1 Example Solution
import sys

print("Enter DNA sequences (type 'END' to finish):")
while True:
    sequence = sys.stdin.readline().rstrip()
    if sequence == "END":
        break
    valid_bases = set('ATGC')
    if set(sequence.upper()).issubset(valid_bases):
        sys.stdout.write("Valid sequence:\n")
    else:
        sys.stdout.write(f"Invalid sequence: {sequence}\n")