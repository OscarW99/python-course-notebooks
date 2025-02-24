# Chapter 4: AI-Powered Programming

#* 1. AI-Assisted Loop Modification
# Calculate Factorial numbers up to the 15th term
import math

factorials = []
for i in range(1, 16):
    factorials.append(f"{i}! = {math.factorial(i)}")

print(factorials)


#* 2. Security Audit
# Improved Code
import os

def process_patient_data(id):
    # Sanitize input to prevent path traversal
    if not id.isalnum():
        raise ValueError("Invalid ID format")

    file_path = f"{id}.txt"
    
    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    # Use context manager for file handling
    with open(file_path, 'r') as file:
        data = file.read()
    
    return data.upper()
