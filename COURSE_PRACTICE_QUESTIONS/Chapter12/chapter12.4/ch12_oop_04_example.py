# Chapter 11: Object-Orientated Programming

#* 1. Enzyme Polymorphism
class Enzyme:
    def __init__(self, reaction_rate, substrate_conc):
        if reaction_rate <= 0 or substrate_conc <= 0:
            raise ValueError("Reaction rate and substrate concentration must be positive.")
        self.reaction_rate = reaction_rate
        self.substrate_conc = substrate_conc
    
    def calculate_activity(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Kinase(Enzyme):
    def calculate_activity(self):
        return self.reaction_rate * self.substrate_conc

class Phosphatase(Enzyme):
    def calculate_activity(self):
        return self.reaction_rate * (1 / self.substrate_conc)

def analyze_enzyme(enzyme):
    print(f"Enzyme activity: {enzyme.calculate_activity()}")

#* 2. Sample Analysis Polymorphism
class Sample:
    def __init__(self, sample_id, collection_date):
        self.sample_id = sample_id
        self.collection_date = collection_date
    
    def process_data(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def quality_check(self):
        raise NotImplementedError("Subclass must implement abstract method")

class BloodSample(Sample):
    def __init__(self, sample_id, collection_date, temperature, cell_count):
        super().__init__(sample_id, collection_date)
        self.temperature = temperature
        self.cell_count = cell_count
    
    def process_data(self):
        print(f"Processing blood sample {self.sample_id} collected on {self.collection_date}")
        # Add blood-specific processing logic here
    
    def quality_check(self):
        return 36 <= self.temperature <= 38 and self.cell_count > 0

class TissueSample(Sample):
    def __init__(self, sample_id, collection_date, weight, preservation_method):
        super().__init__(sample_id, collection_date)
        self.weight = weight
        self.preservation_method = preservation_method
    
    def process_data(self):
        print(f"Processing tissue sample {self.sample_id} collected on {self.collection_date}")
        # Add tissue-specific processing logic here
    
    def quality_check(self):
        return self.weight > 0 and self.preservation_method in ['frozen', 'paraffin']

def analyze_sample(sample):
    sample.process_data()
    quality = sample.quality_check()
    print(f"Sample quality check: {'Passed' if quality else 'Failed'}")