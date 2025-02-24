# Chapter 4: AI-Powered Programming# Chapter 4: AI-Powered Programming

#* 1. Correcting the Loop Range
for i in range(5, 16):
    print(i ** 2)


#* 2. Fixing a Syntax Error
num = 7
if num % 2 == 0:  # Corrected the assignment operator to comparison operator
    print("Even")
else:
    print("Odd")


#* 3. Understanding Code
def calculate_protein_mass(protein_sequence):
    """Calculates the approximate molecular weight of the Insulin B chain (simplified)."""
    amino_acid_masses = {  # Simplified masses (Da)
        'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
        'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
        'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
        'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
    }
    mass = 0
    for amino_acid in protein_sequence:
        mass += amino_acid_masses.get(amino_acid, 0)  # Handle unknown amino acids
    return mass

protein = "MALWMRLLPLLALLALWGPDPA"  # Insulin B chain
mass = calculate_protein_mass(protein)
print(mass)

# Explanation:
# Overall purpose: The function calculate_protein_mass calculates the approximate molecular weight of a given protein sequence based on the simplified masses of amino acids.
# How it works: It uses a dictionary to store the masses of amino acids. It iterates through the protein sequence, looks up each amino acid's mass, and sums them up to get the total mass.
# Potential issues: The function assumes all amino acids in the sequence are known and listed in the dictionary. If an unknown amino acid is encountered, it will be ignored (mass of 0).