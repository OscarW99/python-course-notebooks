# Chapter 6: Functions and Libraries

#* 1. Analyzing Protein Weights
protein_weights = [45.3, 17.8, 56.9, 22.4, 34.2]
heaviest = max(protein_weights)
lightest = min(protein_weights)
total_weight = sum(protein_weights)
length = len(protein_weights)
print(f"Heaviest: {heaviest}")
print(f"Lightest: {lightest}")
print(f"Total weight: {total_weight}")
print(f"Length: {length}")

#* 2. Basic Math Operations
power = 5 ** 3
rounded_value = round(67.8899, 2)
absolute_value = abs(-12.34)
print(f"5 to the power of 3: {power}")
print(f"Rounded value: {rounded_value}")
print(f"Absolute value: {absolute_value}")

#* 3. Comparing Gene Expression Data
expression_day1 = [12.3, 15.8, 9.2, 14.5]
expression_day2 = [11.8, 16.2, 8.9, 15.0]
highest_expression = max(max(expression_day1), max(expression_day2))
total_expression_day1 = sum(expression_day1)
total_expression_day2 = sum(expression_day2)
rounded_day1 = [round(value, 1) for value in expression_day1]
rounded_day2 = [round(value, 1) for value in expression_day2]
print(f"Highest expression: {highest_expression}")
print(f"Total expression day 1: {total_expression_day1}")
print(f"Total expression day 2: {total_expression_day2}")
print(f"Rounded day 1: {rounded_day1}")
print(f"Rounded day 2: {rounded_day2}")
