#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 2:
    print("Please provide a file name as an argument.", file=sys.stderr)
    sys.exit(1)

file_name = sys.argv[1]
if not os.path.isfile(file_name):
    print(f"Error: File '{file_name}' does not exist.", file=sys.stderr)
else:
    print(f"File '{file_name}' exists.")