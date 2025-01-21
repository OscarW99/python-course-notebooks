# Chapter 6: Working with Files

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Navigating and Creating Directories
print("Current working directory:", os.getcwd())
os.chdir("data/project_files")
os.mkdir("analysis")
print("Directories in project_files:", os.listdir())

#* 2. Identifying Specific Files
bio_data_path = "data/bio_data"
fasta_files = [f for f in os.listdir(bio_data_path) if f.endswith('.fasta')]
print("FASTA files found:", fasta_files)

#* 3. Modifying the Directory Structure
os.rename("raw_data", "input_data")
print("Updated directories in project_files:", os.listdir())

#* 4. Removing Files and Directories
os.remove("data/bio_data/notes.txt")
os.rmdir("data/project_files/results")
print("Updated bio_data contents:", os.listdir("data/bio_data"))
print("Updated project_files contents:", os.listdir("data/project_files"))

#* 5. Building Paths
path = os.path.join("project_files", "analysis", "final_report.txt")
print(f"Windows path: {os.path.join('data', path).replace('/', '\\')}")
print(f"Unix-like path: {os.path.join('data', path)}")
if os.path.exists(os.path.join('data', path)):
    print("Path exists")
else:
    print("Path does not exist")

#* 6. Move a File
# Rename the file to mimic moving by using full paths
os.rename("data/bio_data/gene_data.csv", "data/project_files/analysis/gene_data.csv")
print("bio_data after move:", os.listdir("data/bio_data"))
print("analysis after move:", os.listdir("data/project_files/analysis"))

#* 7. Rename Files
analysis_path = "project_files/analysis"
for filename in os.listdir(analysis_path):
    if filename.endswith('.csv'):
        os.rename(os.path.join(analysis_path, filename), os.path.join(analysis_path, filename.replace('.csv', '_final.csv')))
print("Files in analysis after renaming:", os.listdir(analysis_path))