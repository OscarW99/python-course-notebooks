# Chapter 9: Data Manipulation

from Bio import Entrez
from Bio.Data import CodonTable

# Set up email
Entrez.email = "your.email@example.com"

#* 1. Fetching GenBank Record
handle = Entrez.efetch(db="nucleotide", id="NM_000207.3", rettype="gb", retmode="text")
record = handle.read()
handle.close()
# Extract organism name and gene description
organism = record.split("ORGANISM  ")[1].split("\n")[0].strip()
description = record.split("gene=")[1].split("]")[0].strip()
print("Organism:", organism)
print("Gene Description:", description)

#* 2. PubMed Search Function
def search_pubmed(term, year):
    search_query = f"{term} AND {year}[pdat]"
    handle = Entrez.esearch(db="pubmed", term=search_query, retmax=5)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

# Example usage:
ids = search_pubmed("COVID-19 variants", 2024)
print("PubMed IDs:", ids)

#* 3. Comparing Codon Tables
standard_table = CodonTable.unambiguous_dna_by_id[1]
mito_table = CodonTable.unambiguous_dna_by_id[2]
differences = []
for codon in standard_table.forward_table:
    if standard_table.forward_table[codon] != mito_table.forward_table.get(codon, 'Stop'):
        differences.append((codon, standard_table.forward_table[codon], mito_table.forward_table.get(codon, 'Stop')))
for diff in differences:
    print(f"Codon {diff[0]} encodes {diff[1]} in standard but {diff[2]} in vertebrate mitochondrial.")

#* 4. Searching PubMed for Review Articles
search_term = "Smith J[Author] AND review[pt] AND 2020:2025[pdat]"
handle = Entrez.esearch(db="pubmed", term=search_term, retmax=3, rettype="medline")
record = Entrez.read(handle)
handle.close()
ids = record["IdList"]
if ids:
    fetch_handle = Entrez.efetch(db="pubmed", id=",".join(ids), rettype="medline", retmode="text")
    data = fetch_handle.read().split("\n\n")
    fetch_handle.close()
    for article in data:
        if "TI  -" in article:
            print(article.split("TI  -")[1].strip())