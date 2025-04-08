# Chapter 7: Working with Files

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
os.chdir("../..")
print("Back to original directory:", os.getcwd())

#* 2. Identifying Specific Files
bio_data_path = "data/bio_data"
fasta_files = [f for f in os.listdir(bio_data_path) if f.endswith('.fasta')]
print("FASTA files found:", fasta_files)

#* 3. Modifying the Directory Structure
os.rename("data/project_files/raw_data", "data/project_files/input_data")
print("Updated directories in project_files:", os.listdir("data/project_files"))

#* 4. Removing Files and Directories
# Safely remove the notes.txt file from the bio_data directory
if os.path.exists("data/bio_data/notes.txt"):
    os.remove("data/bio_data/notes.txt")
    print(f"File '{"data/bio_data/notes.txt"}' has been removed successfully.")
else:
    print(f"File '{"data/bio_data/notes.txt"}' does not exist.")

# Ensure the results directory inside project_files is empty before removal
if os.path.exists("data/project_files/results"):
    if not os.listdir("data/project_files/results"):  # Check if the directory is empty
        os.rmdir("data/project_files/results")
        print(f"Directory '{"data/project_files/results"}' has been removed successfully.")
    else:
        print(f"Directory '{"data/project_files/results"}' is not empty and cannot be removed using os.rmdir().")
else:
    print(f"Directory '{"data/project_files/results"}' does not exist.")

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
# Define source and destination paths
source_path = "data/bio_data/gene_data.csv"
destination_path = "data/project_files/analysis/gene_data.csv"
# Check if the source file exists
if os.path.exists(source_path):
    # Rename the file to mimic moving by using full paths
    os.rename(source_path, destination_path)
    print(f"File moved from '{source_path}' to '{destination_path}'.")
    # Print the updated directory structures
    print("bio_data after move:", os.listdir("data/bio_data"))
    print("analysis after move:", os.listdir("data/project_files/analysis"))
else:
    print(f"Source file '{source_path}' does not exist. Unable to move the file.")

#* 7. Rename Files
analysis_path = "data/project_files/analysis"
for filename in os.listdir(analysis_path):
    if filename.endswith('.csv'):
        os.rename(os.path.join(analysis_path, filename), os.path.join(analysis_path, filename.replace('.csv', '_final.csv')))
print("Files in analysis after renaming:", os.listdir(analysis_path))