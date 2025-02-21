#!/usr/bin/env python3

import pandas as pd
import os
import sys

if len(sys.argv) < 2:
    print("Please provide a CSV file name as an argument.", file=sys.stderr)
    sys.exit(1)

csv_file = sys.argv[1]
if not os.path.isfile(csv_file):
    print(f"Error: File '{csv_file}' does not exist.", file=sys.stderr)
    sys.exit(1)

df = pd.read_csv(csv_file)
cleaned_df = df.dropna()

# Get file name without extension
base_name = os.path.splitext(os.path.basename(csv_file))[0]
output_file = os.path.join(os.path.dirname(csv_file), f"{base_name}_cleaned.csv")
cleaned_df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")