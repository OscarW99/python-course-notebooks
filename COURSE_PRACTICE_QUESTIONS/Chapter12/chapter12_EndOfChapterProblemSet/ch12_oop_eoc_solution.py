# Chapter 12: Object-Orientated Programming

#* 1. Basic Cell Class
class Cell:
    def __init__(self, cell_type, size):
        self.cell_type = cell_type
        self.size = size
    
    def describe(self):
        print(f"Cell type: {self.cell_type}, Size: {self.size}")

# Create instances and call describe


#* 2. Inheritance with Species
class Species:
    def __init__(self, name, habitat):
        pass
    
    def describe(self):
        pass

class Mammal(Species):
    def __init__(self, name, habitat, is_warm_blooded):
        # Use super() here to initialize name and habitat
        pass
    
    def describe(self):
        # Override describe to include is_warm_blooded
        pass

# Create an instance of Mammal

# Demonstrate accessing and modifying the is_warm_blooded 

# Call the describe method on your instance


#* 3. Polymorphism in Microorganisms
class Microorganism:
    def grow(self):
        pass

class Bacteria(Microorganism):
    def grow(self):
        pass

class Virus(Microorganism):
    def grow(self):
        pass

def cultivate(microbe):
    pass

# Create instances and demonstrate polymorphism

#* 4. Encapsulation for Enzyme Properties
class Enzyme:
    def __init__(self):
        pass
    
    def get_activity(self):
        pass
    
    def set_activity(self, activity):
        pass

    def get_substrate(self):
        pass
    
    def set_substrate(self, substrate):
        pass

# Create instance, set activity, show error

#* 5. String Representation for Molecules
class Molecule:
    def __init__(self, name, molecular_formula, mass):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass

# Create molecule and demonstrate representations

#* 6. Arithmetic Operations on DNA Molecules
class DNAMolecule:
    def __init__(self, sequence):
        pass
    
    def __add__(self, other):
        pass

# Demonstrate DNA concatenation

#* 7. Comparing Protein Sequences
class Protein:
    def __init__(self, sequence):
        pass
    
    # Implement __eq__ method

# Demonstrate protein comparison

#* 8. Indexing in RNA Sequences
class RNA:
    def __init__(self, sequence):
        pass
    
    # Implement __getitem__ method 

# Demonstrate indexing and slicing

#* 9. Mutation in Genes
class Gene:
    def __init__(self, name, sequence):
        pass
    
    def mutate(self, position, new_nucleotide):
        pass

# Create gene, mutate, display change

#* 10. A Class System for Biological Pathways
class Pathway:
    def __init__(self):
        pass

class MetabolicPathway(Pathway):
    def __init__(self, energy_change):
        pass
    
    def describe(self):
        pass

class SignalingPathway(Pathway):
    def __init__(self, signal_molecule):
        pass
    
    def describe(self):
        pass

# Create instances, set attributes, access them