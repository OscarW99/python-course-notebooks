# Chapter 6: Functions and Libraries

#* 1. Using the Math Module
import math

# Calculate the square root of 64
sqrt_result = math.sqrt(64)
print(sqrt_result)

# Calculate the Euclidean distance between points (0,0) and (3,4)
distance = math.dist((0, 0), (3, 4))
print(distance)

# Calculate π²
pi_squared = math.pi ** 2
print(pi_squared)


#* 2. Introduction to the Random Module
import random

amino_acids = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I']

# Select a random amino acid from the list
random_acid = random.choice(amino_acids)
print(random_acid)

# Select 3 unique amino acids
three_acids = random.sample(amino_acids, 3)
print(three_acids)

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
print(random_number)


#* 3. Using the Datetime Module
import datetime

# Create a datetime object for December 25, 2025, at 2:30 PM
december_25 = datetime.datetime(2025, 12, 25, 14, 30)
print(december_25)

# Get the current time
current_time = datetime.datetime.now()
print(current_time)

# Calculate the difference in days
time_difference = (current_time - december_25).days
print(time_difference)

# Add 30 days to the datetime object
future_date = december_25 + datetime.timedelta(days=30)
print(future_date)
