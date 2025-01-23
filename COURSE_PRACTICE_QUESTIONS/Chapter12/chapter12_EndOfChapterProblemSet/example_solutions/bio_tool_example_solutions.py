#!/usr/bin/env python3

import sys

def gc_content(sequence):
    gc = sequence.count('G') + sequence.count('C')
    return (gc / len(sequence)) * 100 if sequence else 0

def sequence_length(sequence):
    return len(sequence)

def reverse_sequence(sequence):
    return sequence[::-1]

if len(sys.argv) < 2:
    print("Please provide an action: gc, length, or reverse.", file=sys.stderr)
    sys.exit(1)

action = sys.argv[1].lower()
sequence = sys.stdin.read().strip()

if action == 'gc':
    sys.stdout.write(f"GC content: {gc_content(sequence):.2f}%\n")
elif action == 'length':
    sys.stdout.write(f"Sequence length: {sequence_length(sequence)}\n")
elif action == 'reverse':
    sys.stdout.write(f"Reversed sequence: {reverse_sequence(sequence)}\n")
else:
    print("Invalid action provided.", file=sys.stderr)
    sys.exit(1)