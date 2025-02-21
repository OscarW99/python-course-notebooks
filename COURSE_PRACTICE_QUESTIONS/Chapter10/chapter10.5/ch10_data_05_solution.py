# Chapter 10: Data Manipulation

import pandas as pd

#* 1. Creating DataFrame from Dictionary
#$ data1 = 
#$ df1 = 

#* 2. Custom Row Indices
data2 = {
    'Sample': ['A1', 'B1', 'C1'],
    'pH': [7.2, 6.8, 7.5],
    'Temperature': [37.5, 37.0, 37.8]
}
#$ df2 = 

#* 3. Setting Column as Index
data3 = {
    'Sample': ['P1', 'P2', 'P3', 'P4'],
    'Concentration': [0.5, 0.8, 0.4, 0.9],
    'Time': [10, 20, 10, 20]
}
df3 = pd.DataFrame(data3)
#$ indexed_df3 = 

#* 4. Concatenating DataFrames
df4a = pd.DataFrame({
    'ID': ['A1', 'A2', 'A3'],
    'Value': [100, 200, 300]
})
df4b = pd.DataFrame({
    'ID': ['B1', 'B2', 'B3'],
    'Value': [400, 500, 600]
})
#$ result = 

#* 5. Adding Conditional Column
df5 = pd.DataFrame({
    'Protein': ['P1', 'P2', 'P3', 'P4'],
    'Value': [45, 78, 23, 95]
})
#$ df5['Status'] = 