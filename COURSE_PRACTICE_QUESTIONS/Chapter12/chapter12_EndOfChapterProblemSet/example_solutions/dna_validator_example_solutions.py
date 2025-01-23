#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("Please provide a DNA sequence as an argument.")
    sys.exit(1)

sequence = sys.argv[1]
valid_bases = set("ATGC")

if set(sequence.upper()) <= valid_bases:
    print("The sequence is valid.")
else:
    print("The sequence contains invalid bases.")