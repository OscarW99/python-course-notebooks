# Chapter 3: Local Development Environment Problem Set

## Setup Instructions
1. Open VSCode
2. Open this markdown file in one panel
3. Open the Python file (solutions.py) in another panel
4. Use the "Split Editor" feature (or Ctrl+\) to view both files side by side

## Practice Problems

### 1. Test Script
Run a simple "Hello World" program to verify your Python setup is working correctly.

### 2. Sequence Transformation
Create a function that manipulates DNA sequences:
* Write a lambda function to convert DNA sequences to uppercase
* Use the `map()` function to apply this transformation to a list of sequences
* Create a function to count the occurrence of a specific nucleotide
* Use `filter()` to keep sequences with at least two 'G' nucleotides

### 3. Protein Analysis Function
Create a function that analyzes a list of protein sequences:
* Write a function `analyze_proteins` that takes a list of protein sequences as input
* Calculate the average length of the sequences
* Identify sequences longer than a given threshold
* Return a dictionary with the following information:
   * Total number of sequences
   * Average sequence length
   * List of sequences longer than the threshold (default 50)

### 4. Temperature Data Analysis
Write a function to process a list of temperature readings:
* Create a function that takes a list of temperatures
* Calculate the average temperature
* Identify temperatures above a specific threshold
* Return a dictionary with:
   * Total number of readings
   * Average temperature
   * List of temperatures above the threshold (default 30°C)