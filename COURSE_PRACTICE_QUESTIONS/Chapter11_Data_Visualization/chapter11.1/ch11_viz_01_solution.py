# Chapter 11: Data Visualization

# Note: File paths differ between operating systems. 
# Use forward slashes (/) for Linux and macOS, and backslashes (\) for Windows.
# For example:
# Linux/macOS: "data/example.file"
# Windows: "data\\example.file" or r"data\example.file"
# Python generally handles forward slashes (/) well on all platforms.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
weather_data = pd.read_csv('data/temperature_data.csv')

#* 1. Scatter Plot of Temperature vs. Humidity
# Create basic scatter plot
# Customize with transparency and grid

#* 2. Diverging Bar Plot for Temperature Deviations
# Calculate temperature deviations
# Create diverging bar plot
# Color bars based on deviation

#* 3. Lollipop Chart for Average Humidity by Climate Zone
# Calculate and sort average humidity by climate zone
# Create lollipop chart
# Customize stems and markers