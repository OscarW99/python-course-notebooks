# Chapter 6: Functions and Libraries

#* 1. Global Variable Modification
total_sequences_processed = 0
# Add your code here


#* 2. Using Global Inside a Function
enzyme = "DNA Polymerase"
# Add your code here


#* 3. Global List Modification
dna_sequences = []
# Add your code here


#* 4. Multiple Global Variables
sequence_count = 0
total_length = 0
# Add your code here


#* 5. Local vs Global Conflict
value = 10
def demonstrate_scope():
    value = 20
    print(f"Local value: {value}")
print(f"Global value: {value}")

# Play around with the function and using the global keyword with value