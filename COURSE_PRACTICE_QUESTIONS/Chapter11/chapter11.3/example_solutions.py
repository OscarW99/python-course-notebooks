# Chapter 11: Object-Orientated Programming

#* 1. Cell and StemCell Inheritance
class Cell:
    def __init__(self, cell_type, size):
        self.cell_type = cell_type
        self.size = size

class StemCell(Cell):
    DIFFERENTIATION_OPTIONS = {
        "totipotent": ["neural", "blood", "muscle", "epithelial"],
        "pluripotent": ["neural", "blood", "muscle"],
        "multipotent": ["neural", "blood"]
    }
    
    def __init__(self, cell_type, size, potency_type):
        super().__init__(cell_type, size)
        self.potency_type = potency_type
    
    def get_differentiation_options(self):
        return self.DIFFERENTIATION_OPTIONS.get(self.potency_type, [])

#* 2. Experiment Class Hierarchy
class Experiment:
    def __init__(self, name, duration, temperature):
        if not (0 <= temperature <= 100):
            raise ValueError("Temperature must be between 0 and 100°C")
        
        self.name = name
        self.duration = duration
        self.temperature = temperature
    
    def get_status(self):
        return "Running" if self.duration > 0 else "Completed"

class PCRExperiment(Experiment):
    def __init__(self, name, duration, temperature, num_cycles, denaturation_temp=95):
        super().__init__(name, duration, temperature)
        
        if not (0 <= denaturation_temp <= 100):
            raise ValueError("Denaturation temperature must be between 0 and 100°C")
        
        self.num_cycles = num_cycles
        self.denaturation_temp = denaturation_temp
    
    def calculate_total_duration(self):
        # Assuming each cycle takes the full duration time
        return self.duration * self.num_cycles