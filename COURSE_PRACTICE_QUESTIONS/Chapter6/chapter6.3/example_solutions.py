# Chapter 6: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "output/greetings.txt"
# Windows: "output\\greetings.txt" or r"output\greetings.txt"
# Python generally handles forward slashes (/) well on all platforms.

#$ This Just Makes Sure We're Starting in the Right Directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Writing a Simple Message
message = "Hello, World of Bioinformatics!"
with open('output/greetings.txt', 'w') as file:
    file.write(message)

#* 2. Appending to a File
additional_message = "\nExploring file operations in Python."
with open('output/greetings.txt', 'a') as file:
    file.write(additional_message)

#* 3. Writing Multiple Lines with Loop
genes = ["BRCA1 - DNA repair", "TP53 - Cell cycle regulation", "EGFR - Signal transduction"]
with open('output/gene_info.txt', 'w') as file:
    for gene in genes:
        file.write(gene + '\n')

#* 4. Using `.writelines()` to Write a List
sequences = ["Sequence A: ATCG", "Sequence B: GCTA", "Sequence C: CGAT"]
with open('output/sequence_list.txt', 'w') as file:
    file.writelines([sequence + '\n' for sequence in sequences])