# Chapter 12: Object-Orientated Programming

#* 1. Basic Cell Class
class Cell:
    def __init__(self, cell_type, size):
        self.cell_type = cell_type
        self.size = size
    
    def describe(self):
        print(f"Cell type: {self.cell_type}, Size: {self.size}")

neuron = Cell("neuron", "small")
muscle = Cell("muscle", "large")
neuron.describe()
muscle.describe()


#* 2. Inheritance with Species
class Species:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def describe(self):
        print(f"Name: {self.name}, Habitat: {self.habitat}")

class Mammal(Species):
    def __init__(self, name, habitat, is_warm_blooded):
        super().__init__(name, habitat)
        self.is_warm_blooded = is_warm_blooded
    
    def describe(self):
        super().describe()
        print(f"Is Warm-Blooded: {self.is_warm_blooded}")

whale = Mammal("Blue Whale", "Ocean", True)
print("Before modification:", whale.is_warm_blooded)
whale.is_warm_blooded = False
print("After modification:", whale.is_warm_blooded)
whale.describe()


#* 3. Polymorphism in Microorganisms
class Microorganism:
    def grow(self):
        print("Growing")

class Bacteria(Microorganism):
    def grow(self):
        print("Bacteria is multiplying")

class Virus(Microorganism):
    def grow(self):
        print("Virus is replicating")

def cultivate(microbe):
    microbe.grow()

bacterium = Bacteria()
virus = Virus()

cultivate(bacterium)  
cultivate(virus)  

#* 4. Encapsulation for Enzyme Properties
class Enzyme:
    def __init__(self):
        self.__activity = 0
        self.__substrate = ""
    
    def get_activity(self):
        return self.__activity
    
    def set_activity(self, activity):
        if 0 <= activity <= 100:
            self.__activity = activity
        else:
            raise ValueError("Activity must be between 0 and 100")
    
    def get_substrate(self):
        return self.__substrate
    
    def set_substrate(self, substrate):
        self.__substrate = substrate

enzyme = Enzyme()
enzyme.set_activity(50)
print("Current activity:", enzyme.get_activity())

try:
    enzyme.set_activity(150)  
except ValueError as e:
    print(e)

#* 5. String Representation for Molecules
class Molecule:
    def __init__(self, name, molecular_formula, mass):
        self.name = name
        self.molecular_formula = molecular_formula
        self.mass = mass
    
    def __str__(self):
        return f"{self.name} ({self.molecular_formula}) - {self.mass} g/mol"
    
    def __repr__(self):
        return f"Molecule('{self.name}', '{self.molecular_formula}', {self.mass})"

water = Molecule("Water", "H2O", 18.01528)
print(str(water))  
print(repr(water))  

#* 6. Arithmetic Operations on DNA Molecules
class DNAMolecule:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def __add__(self, other):
        if isinstance(other, DNAMolecule):
            return DNAMolecule(self.sequence + other.sequence)
        raise TypeError("Can only add DNAMolecule to DNAMolecule")

dna1 = DNAMolecule("ATCG")
dna2 = DNAMolecule("GGTA")
dna3 = dna1 + dna2
print(dna3.sequence)  # Should print "ATCGGGTA"

#* 7. Comparing Protein Sequences
class Protein:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
    
    def __eq__(self, other):
        if isinstance(other, Protein):
            return self.sequence == other.sequence
        return False

protein1 = Protein("ATGC")
protein2 = Protein("atgc")
protein3 = Protein("TTAA")

print(protein1 == protein2)  
print(protein1 == protein3)  

#* 8. Indexing in RNA Sequences
class RNA:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def __getitem__(self, key):
        return self.sequence[key]

rna = RNA("AUGCUA")
print(rna[0])  
print(rna[1:3])  

#* 9. Mutation in Genes
class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
    
    def mutate(self, position, new_nucleotide):
        if position < 0 or position >= len(self.sequence):
            raise IndexError("Position out of range")
        self.sequence = self.sequence[:position] + new_nucleotide + self.sequence[position + 1:]

gene = Gene("BRCA1", "ATGC")
print("Before mutation:", gene.sequence)
gene.mutate(2, "C")
print("After mutation:", gene.sequence)

#* 10. A Class System for Biological Pathways
class Pathway:
    def __init__(self):
        self.steps = []

    def describe(self):
        print(f"Pathway steps: {len(self.steps)}")

class MetabolicPathway(Pathway):
    def __init__(self, energy_change):
        super().__init__()
        self.energy_change = energy_change
    
    def describe(self):
        super().describe()
        print(f"Energy Change: {self.energy_change} kJ/mol")

class SignalingPathway(Pathway):
    def __init__(self, signal_molecule):
        super().__init__()
        self.signal_molecule = signal_molecule
    
    def describe(self):
        super().describe()
        print(f"Signal Molecule: {self.signal_molecule}")

metabolic = MetabolicPathway(50)
metabolic.steps = ["Reaction A", "Reaction B"]
metabolic.describe()

signaling = SignalingPathway("Insulin")
signaling.steps = ["Receptor Binding", "Signal Transduction"]
signaling.describe()