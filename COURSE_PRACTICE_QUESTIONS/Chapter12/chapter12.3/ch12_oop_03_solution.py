# Chapter 11: Object-Orientated Programming

#* 1. Cell and StemCell Inheritance
# Base Cell class
class Cell:
    def __init__(self, cell_type, size):
        # Initialize attributes
        pass

# Derived StemCell class
class StemCell(Cell):
    # Add your methods here
    pass

#* 2. Experiment Class Hierarchy
# Base Experiment class
class Experiment:
    def __init__(self, name, duration, temperature):
        # Initialize attributes with validation
        pass
    
    def get_status(self):
        # Return status based on duration
        pass

# Derived PCRExperiment class
class PCRExperiment(Experiment):
    def __init__(self, name, duration, temperature, num_cycles, denaturation_temp=95):
        # Call super().__init__() and add new attributes
        pass
    
    def calculate_total_duration(self):
        # Calculate and return total duration
        pass