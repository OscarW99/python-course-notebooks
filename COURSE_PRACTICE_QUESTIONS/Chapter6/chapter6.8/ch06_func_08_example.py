# Chapter 6: Functions and Libraries

#* 1. Analyzing Multiple Gene Sequences
def analyze_gene_sequences(*args):
    for sequence in args:
        print(f"Gene Sequence: {sequence}")
analyze_gene_sequences("ATGC", "CGTA", "GCTA")

#* 2. Calculating Average Gene Length
def average_gene_length(*args):
    return sum(args) / len(args)
print(average_gene_length(100, 200, 300))

#* 3. Creating Protein Records
def create_protein_record(**kwargs):
    for key, value in kwargs.items():
        print(f"Property: {key}, Value: {value}")
create_protein_record(name="Hemoglobin", sequence="ATGC", function="Oxygen transport")

#* 4. Analyzing Data with Units
def analyze_data(*args, **kwargs):
    units = kwargs.get('units', 'meters')
    for data_point in args:
        print(f"Data: {data_point} {units}")
analyze_data(10, 20, 30, units="cm")
