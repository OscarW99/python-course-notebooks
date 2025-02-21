# Chapter 12: Object Orientated Programming

#* 1. Gene Class Creation and Usage
# Define the Gene class
class Gene:
    def display(self):
        print("This is a gene.")

# Create two instances
gene1 = Gene()
gene2 = Gene()

# Call display on each instance
gene1.display()
gene2.display()

#* 2. DNA Class Creation and Usage
class DNA:
    def display(self):
        print("This is a DNA sequence")
    
    def get_length(self):
        return 100

# Create an instance
dna_seq = DNA()

# Call both methods
dna_seq.display()
print(dna_seq.get_length())  # Prints the length returned by get_length()