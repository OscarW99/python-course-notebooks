# Question 2 Example Solution
import sys

genes = ['BRCA1', 'P53', 'APC', 'K', 'KRAS', 'AT']
for gene in genes:
    if len(gene) < 4:
        sys.stderr.write(f"Warning: Gene {gene} is too short.\n")
    else:
        sys.stdout.write(f"{gene}\n")