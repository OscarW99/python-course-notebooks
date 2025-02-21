# Chapter 12: Object-Orientated Programming

#* 1. Gene Class with Initialization
class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
    
    def display(self):
        print(f"Gene Name: {self.name}, Sequence: {self.sequence}")

#* 2. DNA Class with Sequence Operations
class DNA:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def display(self):
        print(f"DNA Sequence: {self.sequence}")
    
    def get_length(self):
        return len(self.sequence)
    
    def mutate(self, position, base):
        if position < 0 or position >= len(self.sequence):
            raise ValueError("Position out of range")
        self.sequence = self.sequence[:position] + base + self.sequence[position+1:]

#* 3. Protein Class for Amino Acid Sequences
class Protein:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
    
    def mutate(self, position, new_residue):
        if position < 0 or position >= len(self.sequence):
            raise ValueError("Position out of range")
        self.sequence = self.sequence[:position] + new_residue + self.sequence[position+1:]
    
    def is_valid(self):
        return self.sequence.isalpha() and self.sequence.isupper()

#* 4. Cell Class for Protein Storage
class Cell:
    def __init__(self, name):
        self.name = name
        self.proteins = []
    
    def add_protein(self, protein):
        if isinstance(protein, Protein):
            self.proteins.append(protein)
        else:
            raise TypeError("Only Protein objects can be added")
    
    def display_proteins(self):
        if not self.proteins:
            print(f"No proteins in {self.name}")
        else:
            print(f"Proteins in {self.name}:")
            for protein in self.proteins:
                print(protein.name)