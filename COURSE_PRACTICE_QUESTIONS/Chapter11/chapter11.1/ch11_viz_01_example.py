# Chapter 10: Data Visualization

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
plt.figure(figsize=(10, 6))
plt.scatter(weather_data['Temperature'], weather_data['Humidity'], alpha=0.5, color='blue')
plt.title('Temperature vs. Humidity Scatter Plot')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.grid(linestyle='--')
plt.show()

#* 2. Diverging Bar Plot for Temperature Deviations
mean_temp = weather_data['Temperature'].mean()
weather_data['Temp_Deviation'] = weather_data['Temperature'] - mean_temp
plt.figure(figsize=(10, 6))
for i, (city, deviation) in enumerate(zip(weather_data['City'], weather_data['Temp_Deviation'])):
    color = 'green' if deviation > 0 else 'red'
    plt.hlines(y=i, xmin=0, xmax=deviation, color=color, linewidth=2)
    plt.text(deviation, i, f'{deviation:.1f}', va='center')
plt.yticks(range(len(weather_data)), weather_data['City'])
plt.title('Temperature Deviation from Mean by City')
plt.xlabel('Temperature Deviation (°C)')
plt.axvline(x=0, color='black', linestyle='--')
plt.grid(axis='x', linestyle='--')
plt.show()

#* 3. Lollipop Chart for Average Humidity by Climate Zone
zone_humidity = weather_data.groupby('Climate_Zone')['Humidity'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
markerline, stemline, baseline = plt.stem(zone_humidity.index, zone_humidity.values, basefmt=" ")
plt.setp(markerline, color='blue', marker='o', markersize=10)
plt.setp(stemline, color='red', linewidth=2)
plt.title('Average Humidity by Climate Zone')
plt.xlabel('Climate Zone')
plt.ylabel('Average Humidity (%)')
plt.grid(axis='y', linestyle='--')
plt.show()