# Chapter 8: Error Handling and Logging

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
# Uncomment code and write your try-except block here
# try:
#     # Open file code here
# except FileNotFoundError:
#     # Error message here


#* 2. Handling PermissionError
# Modify the code to handle PermissionError
try:
    with open('data.csv', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")


#* 3. Handling Multiple Exceptions
# Uncomment code and write your try-except block for multiple exceptions
# try:
#     # File processing code here
# # Except block 1

# # Except block 2


#* 4. Handling ZeroDivisionError
# Uncomment code and write your division try-except block
# try:
#     # Division code here
# # Except block here


#* 5. General Exception Handling
# Uncomment code and modify to use Exception as e
# try:
#     # Division code here
# # Exception as e block here
#     # Print exception message here