# Chapter 7: Error Handling and Logging

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

#$ This Just Makes Sure We're Starting in the Right Directory
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

#* 1. Handling FileNotFoundError
try:
    with open('data/experiment_data.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")

#* 2. Handling PermissionError
try:
    with open('data.csv', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied. Cannot open the file.")

#* 3. Handling Multiple Exceptions
try:
    with open('data/file_to_process.txt', 'r') as file:
        content = file.read()
        # Assume we expect integers in the file
        numbers = [int(x) for x in content.split()]
except FileNotFoundError:
    print("File not found for processing!")
except ValueError:
    print("File content not in expected format. Expected integers.")

#* 4. Handling ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

#* 5. General Exception Handling
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")