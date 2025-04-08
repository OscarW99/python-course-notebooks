# Chapter 7: Working with Files

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
# Open 'output/greetings.txt' in write mode and write the message


#* 2. Appending to a File
additional_message = "\nExploring file operations in Python."
# Open 'output/greetings.txt' in append mode and append the additional message


#* 3. Writing Multiple Lines with Loop
genes = ["BRCA1 - DNA repair", "TP53 - Cell cycle regulation", "EGFR - Signal transduction"]
# Open 'output/gene_info.txt' in write mode and use a loop to write each gene's information


#* 4. Using `.writelines()` to Write a List
sequences = ["Sequence A: ATCG", "Sequence B: GCTA", "Sequence C: CGAT"]
# Open 'output/sequence_list.txt' in write mode and use .writelines() to write the sequences