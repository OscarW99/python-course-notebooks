#!/usr/bin/env python3

import sys

total_length = 0
while True:
    sequence = sys.stdin.readline().strip()
    if sequence == 'END':
        break
    total_length += len(sequence)

print(f"Total sequence length: {total_length}")