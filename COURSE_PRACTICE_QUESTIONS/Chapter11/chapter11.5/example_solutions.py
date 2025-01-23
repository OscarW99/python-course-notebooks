# Chapter 11: Object-Orientated Programming

#* 1. Encapsulated Protein Class
class Protein:
    def __init__(self, name, molecular_weight, stability_score):
        self.__name = name
        self.__molecular_weight = molecular_weight
        self.__stability_score = stability_score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        self.__name = name

    def get_molecular_weight(self):
        return self.__molecular_weight

    def set_molecular_weight(self, weight):
        if weight <= 0:
            raise ValueError("Molecular weight must be positive.")
        self.__molecular_weight = weight

    def get_stability_score(self):
        return self.__stability_score

    def set_stability_score(self, score):
        if not 0 <= score <= 1:
            raise ValueError("Stability score must be between 0 and 1.")
        self.__stability_score = score


# Example Usage:
protein = Protein("ProteinA", 50000, 0.8)
print(protein.get_name())  # To get the name
protein.set_name("NewName")  # To set the name


#* 2. Protected Genetic Sequence Class
class GeneticSequence:
    def __init__(self, sequence, quality_scores):
        self.__sequence = sequence
        self.__quality_scores = quality_scores

    def get_sequence(self):
        return self.__sequence

    def set_sequence(self, seq):
        if not all(base in 'ATCG' for base in seq.upper()):
            raise ValueError("Sequence must contain only A, T, C, G.")
        self.__sequence = seq.upper()

    def get_quality_scores(self):
        return self.__quality_scores

    def set_quality_scores(self, scores):
        if len(scores) != len(self.__sequence):
            raise ValueError("Quality scores length must match sequence length.")
        if not all(0 <= score <= 100 for score in scores):
            raise ValueError("All quality scores must be between 0 and 100.")
        self.__quality_scores = scores

    def update_quality_scores(self, new_scores):
        if len(new_scores) != len(self.__sequence):
            raise ValueError("New quality scores length must match sequence length.")
        if not all(0 <= score <= 100 for score in new_scores):
            raise ValueError("All new quality scores must be between 0 and 100.")
        self.__quality_scores = new_scores

    def display_with_quality(self):
        return ' '.join([f"{base}({score})" for base, score in zip(self.__sequence, self.__quality_scores)])


# Example Usage:
sequence = GeneticSequence("ATCG", [50, 60, 70, 80])
print(sequence.get_sequence())  # To get the sequence
sequence.set_sequence("GCTA")  # To set the sequence