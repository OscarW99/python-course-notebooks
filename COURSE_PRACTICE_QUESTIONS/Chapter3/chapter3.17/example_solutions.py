# Chapter 3: Data Structures

#* 1. Creating a Nested Protein Dictionary
# Solution:
protein_info = {
    "Insulin": {"mass": 5.8, "function": "hormone", "location": "pancreas"},
    "Albumin": {"mass": 66.5, "function": "transport", "location": "blood"},
    "Hemoglobin": {"mass": 64.5, "function": "oxygen transport", "location": "blood cells"}
}
print(protein_info)


#* 2. Accessing Cell Data
cell_data = {
    "nucleus": {"size": 5, "shape": "round", "count": 1},
    "mitochondria": {"size": 1, "shape": "oval", "count": 300},
    "ribosome": {"size": 0.1, "shape": "round", "count": 10000}
}
# Solution:
mitochondria_shape = cell_data["mitochondria"]["shape"]
ribosome_count = cell_data["ribosome"]["count"]
nucleus_data = cell_data["nucleus"]
print(mitochondria_shape)
print(ribosome_count)
print(nucleus_data)


#* 3. Modifying Cell Data
# Solution:
# Add lysosome
cell_data["lysosome"] = {"size": 0.5, "shape": "spherical", "count": 100}

# Modify mitochondria count
cell_data["mitochondria"]["count"] = 400

# Add nucleus function
cell_data["nucleus"]["function"] = "genetic material storage"
print(cell_data)


#* 4. Creating Experiment Results Dictionary
# Solution:
experiment_results = {
    "experiment1": {"date": "2023-01-01", "temperature": 37, "outcome": "success"},
    "experiment2": {"date": "2023-01-02", "temperature": 25, "outcome": "failure"},
    "experiment3": {"date": "2023-01-03", "temperature": 30, "outcome": "success"}
}
print(experiment_results)


#* 5. Working with Gene Families
gene_families = {
    "kinases": {"count": 15, "studied": True, "members": ["KIN1", "KIN2", "KIN3"]},
    "phosphatases": {"count": 12, "studied": False, "members": ["PHOS1", "PHOS2"]},
    "receptors": {"count": 25, "studied": True, "members": ["REC1", "REC2", "REC3"]}
}
# Solution:
# Add new kinase member
gene_families["kinases"]["members"].append("KIN4")

# Print receptor members
print(gene_families["receptors"]["members"])

# Update phosphatases status
gene_families["phosphatases"]["studied"] = True
print(gene_families)
