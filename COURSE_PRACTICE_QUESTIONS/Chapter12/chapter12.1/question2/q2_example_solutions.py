# Question 2 Solution
file_format = input("Enter the file format (fasta/fastq/sam): ")
min_length = input("Enter the minimum sequence length: ")
try:
    min_length = int(min_length)
    print(f"You have selected the format {file_format} with a minimum sequence length of {min_length}.")
except ValueError:
    print("Please enter a valid number for the minimum sequence length.")